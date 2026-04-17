from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/decide", methods=["POST"])
def decide():
    data = request.json
    energy = data.get("energy", "medium")
    time_available = data.get("time", "30 minutes")
    ingredients = data.get("ingredients", "anything")
    mood = data.get("mood", "no preference")

    prompt = f"""
    You are a decisive meal recommender. Your job is to eliminate decision fatigue.
    Give ONE specific meal recommendation. No alternatives. No "or you could...".
    Just one answer with a 2 sentence reason.

    User context:
    - Energy level: {energy}
    - Time available: {time_available}
    - Ingredients/cuisine mood: {ingredients}
    - Current mood: {mood}

    Respond in this exact format:
    MEAL: [meal name]
    REASON: [2 sentences max explaining why this fits
        TIME: [how long it takes]
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content
    lines = text.strip().split("\n")
    result = {}
    for line in lines:
        if line.startswith("MEAL:"):
            result["meal"] = line.replace("MEAL:", "").strip()
        elif line.startswith("REASON:"):
            result["reason"] = line.replace("REASON:", "").strip()
        elif line.startswith("TIME:"):
            result["time"] = line.replace("TIME:", "").strip()

    return jsonify(result)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})

if __name__ == "__main__":
    app.run(debug=False)