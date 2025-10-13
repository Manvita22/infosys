"""
Deepfake Detection Module
Based on: https://github.com/yermandy/deepfake-detection
"""
import os
import torch
from huggingface_hub import hf_hub_download
from PIL import Image
from transformers import CLIPProcessor
import io


class DeepfakeDetector:
    """Deepfake detection model using CLIP-based approach."""
    
    def __init__(self):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
        self.model = None
        self.preprocess = None
        torch.set_float32_matmul_precision("high")
    
    def load_model(self):
        """Load the deepfake detection model from HuggingFace."""
        if self.model is not None:
            return  # Already loaded
        
        print("Loading deepfake detection model...")
        
        # Download model from HuggingFace
        repo_id = "yermandy/deepfake-detection"
        filename = "model.torchscript"
        
        model_path = hf_hub_download(
            repo_id=repo_id, 
            filename=filename, 
            local_dir="weights"
        )
        
        # Load torchscript model
        self.model = torch.jit.load(model_path, map_location=self.device)
        self.model.eval()
        self.model = self.model.to(self.device).to(self.dtype)
        
        # Load preprocessing function
        self.preprocess = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
        
        print("Model loaded successfully!")
    
    def preprocess_image(self, image):
        """Preprocess a PIL image for the model."""
        if self.preprocess is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Preprocess using CLIP processor
        processed = self.preprocess(images=image, return_tensors="pt")["pixel_values"][0]
        return processed
    
    def detect(self, image):
        """
        Detect if an image is a deepfake.
        
        Args:
            image: PIL Image or file path
        
        Returns:
            dict: {
                "is_fake": bool,
                "fake_probability": float,
                "real_probability": float,
                "confidence": float
            }
        """
        if self.model is None:
            self.load_model()
        
        # Load image if path is provided
        if isinstance(image, str):
            image = Image.open(image)
        elif isinstance(image, bytes):
            image = Image.open(io.BytesIO(image))
        
        # Preprocess
        processed_image = self.preprocess_image(image)
        batch = processed_image.unsqueeze(0).to(self.device).to(self.dtype)
        
        # Inference
        with torch.no_grad():
            if torch.cuda.is_available():
                with torch.autocast(device_type="cuda", dtype=self.dtype):
                    output = self.model(batch)
                    softmax_output = output.softmax(dim=1).cpu().numpy()[0]
            else:
                output = self.model(batch)
                softmax_output = output.softmax(dim=1).cpu().numpy()[0]
        
        p_real, p_fake = softmax_output
        
        return {
            "is_fake": p_fake > p_real,
            "fake_probability": float(p_fake),
            "real_probability": float(p_real),
            "confidence": float(max(p_real, p_fake))
        }
    
    def detect_batch(self, images):
        """
        Detect deepfakes in a batch of images.
        
        Args:
            images: List of PIL Images or file paths
        
        Returns:
            list: List of detection results
        """
        if self.model is None:
            self.load_model()
        
        # Load and preprocess all images
        pil_images = []
        for img in images:
            if isinstance(img, str):
                pil_images.append(Image.open(img))
            elif isinstance(img, bytes):
                pil_images.append(Image.open(io.BytesIO(img)))
            else:
                pil_images.append(img)
        
        # Preprocess all images
        processed = torch.stack([self.preprocess_image(img) for img in pil_images])
        batch = processed.to(self.device).to(self.dtype)
        
        # Inference
        with torch.no_grad():
            if torch.cuda.is_available():
                with torch.autocast(device_type="cuda", dtype=self.dtype):
                    output = self.model(batch)
                    softmax_output = output.softmax(dim=1).cpu().numpy()
            else:
                output = self.model(batch)
                softmax_output = output.softmax(dim=1).cpu().numpy()
        
        results = []
        for p_real, p_fake in softmax_output:
            results.append({
                "is_fake": p_fake > p_real,
                "fake_probability": float(p_fake),
                "real_probability": float(p_real),
                "confidence": float(max(p_real, p_fake))
            })
        
        return results


# Global detector instance
_detector = None


def get_detector():
    """Get or create the global detector instance."""
    global _detector
    if _detector is None:
        _detector = DeepfakeDetector()
    return _detector
