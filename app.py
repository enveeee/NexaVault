from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Mapping emojis to sentiment
emoji_sentiments = {
    "😀": "Positive", "😢": "Negative", "😡": "Negative",
    "😍": "Positive", "😂": "Positive", "😐": "Neutral"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")

    # Check for emojis in input
    for emoji, sentiment in emoji_sentiments.items():
        if emoji in text:
            return jsonify({"sentiment": sentiment})

    # Analyze text sentiment using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
