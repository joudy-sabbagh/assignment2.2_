# Translation API

This project sets up a Flask-based translation service using a pre-trained Hugging Face model: `Helsinki-NLP/opus-mt-en-fr`.
The model takes English text as input and translates it to French.

## Setup

1. Create and activate a virtual environment:

    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate it (Windows)
    venv\Scripts\activate
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the API:

    ```bash
    python main.py
    ```

4. Send a request to the translation endpoint:

    ```bash
    curl -X POST http://127.0.0.1:5000/translate ^
        -H "Content-Type: application/json" ^
        -d "{\"text\": \"Hello, how are you?\"}"
    ````

