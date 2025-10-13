# 🚀 AI Tweet Generator, Sentiment Analyzer & Deepfake Detector

An AI-powered web app that generates tweets, compares them, predicts engagement, performs sentiment analysis, and **detects deepfakes in images** — powered by **Google Gemini API**, **CLIP-based deepfake detection**, and **Flask**.  

---

## 🧠 Overview

This project allows users to:
- Enter a **prompt** (e.g., a product, idea, or topic)
- Generate multiple **AI-crafted tweets**
- Compare their predicted performance
- Post tweets directly to **Twitter (X)** via the Twitter API
- Analyze tweet sentiment and engagement insights using Gemini AI
- **Detect deepfakes in facial images** using state-of-the-art CLIP-based AI model

---

## 🏗️ Project Structure

```
.
├── api.py                  # Flask backend server (routes & API endpoints)
├── run_prompt.py           # Core logic to interact with Gemini AI
├── sentiment-analysis.py   # Script for batch tweet sentiment analysis
├── deepfake_detector.py    # Deepfake detection module using CLIP model
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend UI for AI Tweet Generator & Deepfake Detector
├── create_tweets.py        # (Referenced in api.py) Generates tweet variations
├── constants.py            # (Referenced in api.py) Contains Twitter API client setup
├── extracted_tweets.json   # Input tweets for sentiment analysis
├── analyzed_tweets.json    # (Output) Sentiment-analyzed tweet data
└── weights/                # (Auto-created) Downloaded AI models
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, TailwindCSS, JavaScript |
| **Backend** | Flask (Python) |
| **AI Engines** | Google Gemini API (`google-genai`), CLIP-based Deepfake Detection |
| **Deep Learning** | PyTorch, Transformers (HuggingFace) |
| **Deployment** | Localhost |

---

## 🚀 Features

✅ **AI Tweet Generation**  
Generates creative, concise tweets using Gemini 2.5 Flash Lite  
Provides sentiment, keywords, and engagement predictions  

✅ **Comparison & Prediction**  
Compares two tweet versions  
Predicts which tweet will perform better

✅ **Sentiment Analysis**  
Analyzes a batch of tweets from `extracted_tweets.json`  
Outputs `analyzed_tweets.json` with detailed emotional and engagement data

✅ **Deepfake Detection** 🆕  
Upload facial images to detect if they are AI-generated or manipulated  
Uses CLIP-based model trained on FaceForensics++ dataset  
Provides confidence scores and real/fake probabilities  
Based on research: [Unlocking the Hidden Potential of CLIP in Generalizable Deepfake Detection](https://arxiv.org/abs/2503.19683)

---

## 🧩 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Renders the main UI (`index.html`) |
| `/generate?prompt=<text>` | GET | Generates AI tweets & predictions |
| `/detect-deepfake` | POST | Detects if an uploaded image is a deepfake |
| `/tweet_a` | POST | Posts Tweet A |
| `/tweet_b` | POST | Posts Tweet B |

---

## 💡 How It Works

### Tweet Generation
1. User enters a **prompt** on the web UI.  
2. The prompt is sent to the Flask `/generate` API.  
3. The backend calls `execute_gemini_for_tweets()` and `execute_gemini_for_tweet_pred()` from `run_prompt.py`.  
4. Gemini returns:
   - Tweet A & Tweet B  
   - Predicted winner  
   - Explanation of the prediction  
5. The results appear dynamically in the chat-like interface.

### Deepfake Detection
1. User uploads a facial image via the web UI.
2. The image is sent to the Flask `/detect-deepfake` API endpoint.
3. The backend loads the CLIP-based deepfake detection model from HuggingFace.
4. The model analyzes the image and returns:
   - Real/Fake classification
   - Confidence score
   - Probability distributions
5. Results are displayed with color-coded indicators.

---

## 🧠 Sentiment Analysis Workflow

1. Place tweets inside `extracted_tweets.json`.  
2. Run:
   ```bash
   python sentiment-analysis.py
   ```
3. Gemini analyzes each tweet’s emotional tone, keywords, and engagement.  
4. Output is saved in `analyzed_tweets.json`.  

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/ai-tweet-generator.git
cd ai-tweet-generator
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Note:** The deepfake detection model requires PyTorch. Installation may take several minutes.
If you encounter issues, ensure you have CUDA installed for GPU support (optional but recommended).

### 4. Add API Keys
Edit **`run_prompt.py`** and replace:
```python
GEMINI_API_KEY = "your_google_gemini_api_key"
```
If using Twitter posting, update credentials inside **`constants.py`**.

### 5. Run the Flask App
```bash
python api.py
```

The app will run on:
```
http://127.0.0.1:5000/
```

### 6. Using the Application

#### Tweet Generator
1. Navigate to http://127.0.0.1:5000/
2. Click on "Tweet Generator" tab
3. Enter a prompt (e.g., "Write a tweet about our new AI product")
4. Click "Generate" and view the AI-generated tweets with predictions

#### Deepfake Detector
1. Navigate to http://127.0.0.1:5000/
2. Click on "Deepfake Detector" tab
3. Upload a facial image (PNG, JPG, etc.)
4. Click "Analyze Image"
5. View the detection results with confidence scores

**Note:** On first use, the deepfake detection model (~350MB) will be automatically downloaded from HuggingFace.

**For detailed usage examples, see [DEEPFAKE_DETECTION.md](DEEPFAKE_DETECTION.md)**

---

## 🔬 Deepfake Detection Model

The deepfake detector is based on the research paper:
**[Unlocking the Hidden Potential of CLIP in Generalizable Deepfake Detection](https://arxiv.org/abs/2503.19683)**
by Andrii Yermakov, Jan Cech, and Jiri Matas (2025)

### Key Features:
- Uses CLIP's ViT-L/14 visual encoder
- Trained on FaceForensics++ dataset
- Generalizes well across multiple deepfake datasets
- Parameter-efficient fine-tuning (PEFT) with LN-tuning
- Competitive performance with state-of-the-art methods

### Model Citation:
```bibtex
@article{yermakov-2025-deepfake-detection,
    title={Unlocking the Hidden Potential of CLIP in Generalizable Deepfake Detection}, 
    author={Andrii Yermakov and Jan Cech and Jiri Matas},
    year={2025},
    eprint={2503.19683},
    archivePrefix={arXiv},
    primaryClass={cs.CV},
    url={https://arxiv.org/abs/2503.19683}, 
}
```

---


## 🧾 License

This project is open-source and available under the **MIT License**.

---

## ✨ Author

**Manvita Ch.**  
👩‍💻 Passionate about AI, NLP, and creative applications of LLMs.  
💬 Building innovative tools that connect creativity with technology.
