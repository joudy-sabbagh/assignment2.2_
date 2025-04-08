from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# access the model through api call, generated read token to call model 
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr"
# retrive securily stored token
HF_TOKEN = os.getenv("HF_TOKEN")

# pass token in header when making request
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.route("/")
def home():
    return {"message": "Translation API is running"}

# THIS ROUTES TAKES INPUT TEXT IN ENGLISH AND RETURN IT'S TRANSLATION IN FRENCH
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "Missing 'text' in request"}), 400

    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        result = response.json()
    except requests.exceptions.JSONDecodeError:
        return jsonify({"error": "Hugging Face returned invalid JSON", "raw_response": response.text}), 500

    if response.status_code != 200:
        return jsonify({
            "error": "Hugging Face API error",
            "details": result
        }), 500

    try:
        translation = result[0]["translation_text"]
    except (KeyError, IndexError):
        return jsonify({"error": "Unexpected response format", "result": result}), 500

    return jsonify({"translation": translation})

if __name__ == "__main__":
    app.run(debug=True)
