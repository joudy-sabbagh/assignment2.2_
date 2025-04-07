from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

# Load model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Translation API is running"}

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    # Get the input text
    text = data.get("text")
    if not text:
        return jsonify({"error": "Missing 'text' in request"}), 400

    # Translate
    inputs = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    output = tokenizer.decode(translated[0], skip_special_tokens=True)

    return jsonify({"translation": output})

if __name__ == "__main__":
    app.run(debug=True)
