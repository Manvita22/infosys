from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from create_tweets import create_tweet
from constants import twitterClient

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


if __name__ == "__main__":
    flask_app.run(debug=True)
