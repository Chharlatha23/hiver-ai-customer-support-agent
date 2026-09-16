# AmazonHelp AI Support Agent

## Objective
Build a functional defensive customer-support prototype that accepts a customer-support message, classifies the intent, predicts priority, routes the ticket to the appropriate support team, and safely handles edge cases (like escalations for sensitive words or low-confidence predictions).

## Dataset Description
This prototype uses a tiny snippet (`sample.csv`) of the Customer Support on Twitter (TWCS) dataset. The dataset is small (93 rows) and heavily imbalanced, with approximately 85 rows belonging to Other/Unknown. Rare-intent performance is unreliable. 

**No independent human-validated golden evaluation dataset was available. Reported metrics are diagnostic measurements based on the available sample and pseudo-labeling heuristics. They should not be interpreted as production accuracy or evidence of real-world generalization.**

## Architecture & Preprocessing
- **Preprocessing**: Cleans input strings, strips duplicate spaces, and extracts explicit entity tokens (e.g. `ORD12345`).
- **Model**: TF-IDF Vectorizer paired with `LogisticRegression`.
- **Taxonomy**: 8 specific intents loaded from `configs/intent_taxonomy.yaml`.
- **Priority Logic**: Inherited from the YAML taxonomy, with Regex overrides for urgent terms (e.g., "emergency", "stolen" -> Critical).
- **Routing Logic**: Directly mapped from intent categories to specific departments.
- **Escalation Logic**: The prototype escalates low-confidence predictions below a confidence threshold of 0.40, and also triggers for sensitive keywords (fraud, hack, lawyer, manager).
- **Evidence Retrieval**: A token-overlap algorithm matches the incoming message against local `sample.csv` rows.

## Usage Instructions

### 1. API Service (FastAPI)
```bash
python -m pip install -r requirements.txt
uvicorn api:app --reload --port 8000
```
- Health Check: `http://localhost:8000/health`
- Predict Endpoint: `POST http://localhost:8000/predict` (send JSON: `{"ticket": "my message"}`)

### 2. Dashboard UI (Streamlit)
```bash
streamlit run app.py --server.port 8501
```
The browser will automatically open the dashboard at `http://localhost:8501`.

### 3. Training & Evaluation
```bash
python -m src.train
python -m src.evaluate
```
*Note: The keyword baseline score of 1.0000 in evaluation may reflect overlap between the heuristic rules and pseudo-label generation. The majority-class baseline of 0.9140 mainly reflects class imbalance.*

### 4. Tests
```bash
python test_cases.py
```

## Limitations & Future Improvements
- **Limitations**: The model is heavily biased toward the "Other / Unknown" intent. It operates as a strict prototype. It does not possess production accuracy, live Amazon-service integration, or real-world generalization. 
- **Future Improvements**: Acquire a significantly larger, human-validated dataset. Upgrade historical retrieval to use semantic embeddings rather than local keyword matching.
