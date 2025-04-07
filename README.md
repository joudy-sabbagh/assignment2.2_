# Translation API

This project sets up a Flask-based translation service using a pre-trained Hugging Face model: `Helsinki-NLP/opus-mt-en-fr`.

At this stage, the project loads the model and verifies it can generate a basic translation.

The model takes English text as input and translates it to French.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate

 
2. Install the dependencies:

```bash
pip install -r requirements.txt

 
3. Run the test script to load the model and print a sample translation:

```bash
python main.py

 
Note: The first time you run this, it will download the model and tokenizer from Hugging Face. This may take a few minutes.

