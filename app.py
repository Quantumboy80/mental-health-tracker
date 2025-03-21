from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call API without CORS issues

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Parse JSON data from request
        data = request.get_json()
        
        if not data or "text" not in data:
            return jsonify({"error": "Invalid input. Please provide 'text' key in JSON."}), 400
        
        text = data["text"]
        
        # Perform sentiment analysis
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            emotion = "POSITIVE"
            recommendation = "Great! Keep engaging in positive habits!"
        elif sentiment < 0:
            emotion = "NEGATIVE"
            recommendation = "Try some relaxation techniques!"
        else:
            emotion = "NEUTRAL"
            recommendation = "Stay balanced and mindful!"

        return jsonify({
            "emotion": emotion,
            "score": sentiment,
            "recommendation": recommendation
        })

    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
