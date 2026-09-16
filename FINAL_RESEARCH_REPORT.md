# Final Research & Implementation Report

## 1. Problem Statement & Scope
This project prototypes an AI-assisted customer-support agent for AmazonHelp conversations. The system triages incoming messages, classifies them into an 8-intent taxonomy, determines priority and routing, triggers escalation for sensitive issues, and generates safe, deterministic support replies.

## 2. Dataset & Provenance
The model relies on the Customer Support on Twitter (TWCS) dataset. Currently, only a 93-row snippet (`sample.csv`) is present locally. The labels used for training are weak-supervision pseudo-labels derived from keyword heuristics, as no human-verified annotations exist in this dataset. The dataset is extremely small and heavily imbalanced, with approximately 85 of 93 rows belonging to Other/Unknown. Rare-intent performance is consequently unreliable.

## 3. System Architecture
- **Model Choice**: TF-IDF vectorization paired with Logistic Regression.
- **Intent Taxonomy**: 8 distinct intents (Delivery Delay, Refund Request, Payment Issue, Account Issue, Product or Order Problem, Order Cancellation, Customer Service Escalation, Other / Unknown).
- **Priority Logic**: Inherited from the YAML taxonomy, with Regex overrides for urgent terms (e.g., "emergency", "stolen" -> Critical).
- **Routing Logic**: Directly mapped from intent categories to specific departments (e.g., Payments and Refunds, Account Support).
- **Escalation Logic**: Deterministic rules triggered by sensitive keywords (fraud, hack, lawyer, manager). The prototype escalates low-confidence predictions below a confidence threshold of 0.40.
- **Historical Evidence**: A basic token-overlap algorithm matches the incoming message against local `sample.csv` rows.
- **Response Generation**: Safe templates that do not promise unauthorized actions or fabricate API interactions with Amazon.

## 4. Evaluation Methodology & Limitations
The `evaluate.py` script attempts to use a human-verified `golden_set.csv` for independent evaluation. Because it is absent, it gracefully falls back to an in-sample diagnostic run on the pseudo-labeled `sample.csv`. 

**No independent human-validated golden evaluation dataset was available. Reported metrics are diagnostic measurements based on the available sample and pseudo-labeling heuristics. They should not be interpreted as production accuracy or evidence of real-world generalization.**

- **Baselines**: The keyword baseline score of 1.0000 essentially reflects overlap between the heuristic rules and pseudo-label generation. The majority-class baseline of 0.9140 mainly reflects class imbalance.

## 5. Prototype Interfaces
- **FastAPI Backend**: Provides `/health` and `/predict` endpoints, robustly handling malformed inputs.
- **Streamlit Dashboard**: Provides a visual UI to demonstrate the complete workflow: predicting intents, highlighting escalation reasons, and retrieving historical evidence.

## 6. Ethical and Privacy Considerations
The system is explicitly designed as a local-only prototype. It does not invoke paid APIs, and no real customer accounts are manipulated. Safe response templates explicitly instruct users not to share passwords or sensitive credentials.
