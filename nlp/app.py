from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
from langdetect import detect
import spacy

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "Positive 😊" if polarity > 0 else "Negative 😠" if polarity < 0 else "Neutral 😐"

    try:
        language = detect(text)
    except:
        language = "Unknown"

    summary = ' '.join(text.split('.')[:2]) + "..." if len(text.split('.')) > 2 else text
    corrected = str(blob.correct())
    keywords = list(set([word.lower_ for word in nlp(text) if word.is_alpha and not word.is_stop]))
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]

    return jsonify({
        'sentiment': sentiment,
        'language': language,
        'summary': summary,
        'corrected': corrected,
        'keywords': keywords,
        'entities': entities
    })

app.run(port=5000)
