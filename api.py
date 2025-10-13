from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from create_tweets import create_tweet
from constants import twitterClient
from deepfake_detector import get_detector
from PIL import Image
import io
import base64

flask_app = Flask(__name__, template_folder="templates")
CORS(flask_app)  # allow CORS for all domains


# -------------------------------
# Root route -> HTML page
# -------------------------------
@flask_app.route("/")
def index():
    return render_template("index.html")  # serve the HTML page


# -------------------------------
# Demo addition route
# -------------------------------
@flask_app.route("/add/<num1>/<num2>")
def add_numbers(num1, num2):
    sumNum = int(num1) + int(num2)
    return f"this method will add numbers {num1} and {num2} ==> {sumNum}"


# -------------------------------
# Tweet Generator API
# -------------------------------
@flask_app.route("/generate")
@cross_origin()
def generate_tweet():
    prompt = request.args.get("prompt")
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    tweet_creation_data = create_tweet(prompt)
    return jsonify(tweet_creation_data)


# -------------------------------
# Deepfake Detection API
# -------------------------------
@flask_app.route("/detect-deepfake", methods=["POST"])
@cross_origin()
def detect_deepfake():
    """
    Detect if an uploaded image is a deepfake.
    Expects: multipart/form-data with 'image' file
    Returns: JSON with detection results
    """
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    try:
        # Read image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Get detector and run detection
        detector = get_detector()
        result = detector.detect(image)
        
        return jsonify({
            "success": True,
            "result": result,
            "filename": file.filename
        })
    
    except Exception as e:
        return jsonify({
            "error": f"Detection failed: {str(e)}"
        }), 500


if __name__ == "__main__":
    flask_app.run(debug=True)
