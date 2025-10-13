# Deepfake Detection Demo

This file demonstrates how to use the deepfake detection feature.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Flask app:**
   ```bash
   python api.py
   ```

3. **Open your browser:**
   Navigate to http://127.0.0.1:5000/

4. **Use the Deepfake Detector:**
   - Click on the "Deepfake Detector" tab
   - Upload a facial image (PNG, JPG, etc.)
   - Click "Analyze Image"
   - View the results

## Using the API Directly

You can also call the API endpoint directly using curl or any HTTP client:

```bash
curl -X POST http://127.0.0.1:5000/detect-deepfake \
  -F "image=@path/to/your/image.jpg"
```

Example response:
```json
{
  "success": true,
  "result": {
    "is_fake": false,
    "fake_probability": 0.15,
    "real_probability": 0.85,
    "confidence": 0.85
  },
  "filename": "image.jpg"
}
```

## Using in Python Code

```python
from deepfake_detector import get_detector
from PIL import Image

# Get the detector instance
detector = get_detector()

# Load an image
image = Image.open("path/to/image.jpg")

# Detect
result = detector.detect(image)

print(f"Is fake: {result['is_fake']}")
print(f"Confidence: {result['confidence']:.2%}")
print(f"Real probability: {result['real_probability']:.2%}")
print(f"Fake probability: {result['fake_probability']:.2%}")
```

## Batch Detection

```python
from deepfake_detector import get_detector

detector = get_detector()

# List of image paths
images = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Batch detection
results = detector.detect_batch(images)

for i, result in enumerate(results):
    print(f"Image {i+1}: {'FAKE' if result['is_fake'] else 'REAL'} "
          f"(confidence: {result['confidence']:.2%})")
```

## Important Notes

- **First run:** The model (~350MB) will be automatically downloaded from HuggingFace on first use
- **GPU support:** CUDA-enabled GPU is automatically detected and used if available
- **Image requirements:** Best results with clear facial images
- **Model source:** Based on research by Yermakov et al. (2025) - [arXiv:2503.19683](https://arxiv.org/abs/2503.19683)

## Model Performance

The model was trained on FaceForensics++ and generalizes well to:
- Celeb-DF-v2
- DFDC (Deepfake Detection Challenge)
- FFIW
- Other deepfake datasets

For detailed performance metrics, refer to the [research paper](https://arxiv.org/abs/2503.19683).

## Troubleshooting

### Model download fails
- Check your internet connection
- Ensure you have enough disk space (~500MB)
- Try manually downloading from https://huggingface.co/yermandy/deepfake-detection

### Out of memory errors
- The model requires ~2GB GPU memory or ~4GB RAM
- Try processing one image at a time instead of batches
- Reduce image resolution before processing

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+ recommended)

## Credits

This integration uses the deepfake detection model from:
- GitHub: https://github.com/yermandy/deepfake-detection
- Paper: "Unlocking the Hidden Potential of CLIP in Generalizable Deepfake Detection"
- Authors: Andrii Yermakov, Jan Cech, Jiri Matas (2025)
