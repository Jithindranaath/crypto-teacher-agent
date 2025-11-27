# Crypto Teacher Agent

Analyzes crypto data and explains it in simple, educational terms.

## Purpose
- Receives user question + live crypto data
- Analyzes the data
- Explains concepts clearly like a teacher
- Uses analogies and simple language

## Input
JSON with user question and crypto data:
```json
{
  "user_question": "What is Bitcoin?",
  "intent": "explain bitcoin",
  "crypto_data": {
    "bitcoin": {
      "price_data": {...},
      "details": {...}
    }
  }
}
```

## Output
Educational explanation using the live data provided.

## Run
```bash
pip install -r requirements.txt
python app.py
```

Runs on: `http://localhost:8002`

## Teaching Style
- Uses actual data values
- Explains in simple terms
- Provides analogies
- Engaging and conversational
