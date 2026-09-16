# Final Research Report — AmazonHelp AI Support Agent

**Selected brand:** @AmazonHelp | **Dataset:** Customer Support on Twitter (TWCS)

## 1. Executive Summary
This project builds and evaluates an AI-assisted customer-support agent prototype for AmazonHelp conversations.
Given a customer message, the system predicts an intent, retrieves historical resolution guidance, drafts a safe response, and decides whether to auto-handle the case or escalate it to a human. The implementation combines a TF-IDF and Logistic Regression classifier, deterministic safety rules, an evidence retrieval layer, and a deterministic fallback template system. Streamlit provides an interactive dashboard, and FastAPI provides a REST endpoint.
Because the available dataset is heavily restricted, the result is a reproducible, strictly offline prototype for defensive ticket triage, rather than an autonomous production system.

## 2. Problem Framing and Dataset
For customer support, good performance requires more than classification accuracy. The agent must identify messy informal messages, provide useful evidence-grounded replies, avoid unsupported promises, automate only sufficiently safe cases, escalate sensitive or uncertain cases, and explain every escalation.
The TWCS dataset contains noisy customer-support conversations. AmazonHelp was selected to cover delivery, account, payment, and general support inquiries. 
**Dataset Limitation:** The prototype currently relies on a tiny 93-row snippet (`sample.csv`). Because true labels were absent, weak supervision rules were used to bootstrap training labels from recurring words and patterns. This saves time but introduces extreme label noise. 

## 3. System Architecture
The workflow is: `message` → `preprocessing` → `intent prediction` → `safety and routing checks` → `historical evidence lookup` → `reply generation` → `final routing output`. 
The Streamlit UI and FastAPI endpoints both call this exact same core Python workflow to ensure logic parity.

## 4. Model and Core Functionality
### 4.1 Intent Classification
The classifier uses TF-IDF features with Logistic Regression and balanced class weights. TF-IDF is fast and interpretable for short text, while Logistic Regression provides calibrated probabilities strictly needed for confidence-based routing. The taxonomy contains eight intents defined in YAML, heavily factoring in `Other / Unknown`.

### 4.2 Grounded Reply Generation
The predicted intent queries a local historical resolution store (`sample.csv`). To guarantee safety without live Amazon API integrations, deterministic templates provide controlled, risk-free fallbacks for the user rather than fabricating refunds.

### 4.3 Escalation and Routing
- The prototype escalates low-confidence predictions below a confidence threshold of **0.40**.
- Explicit escalation requests and unknown intents are safely routed to human departments.
- Sensitive phrases such as requests for a manager, lawyers, stolen items, or account hacks trigger deterministic safety overrides regardless of model confidence.
- The output payload exposes `escalation_reason`, `priority`, and `routing_department`.

### 4.4 Dashboard, API, and Deployment
The Streamlit dashboard allows an operator to enter a message and inspect intent, confidence, priority, department, escalation reason, generated reply, and evidence matches. FastAPI exposes `POST /predict` for programmatic use. Local execution commands:
```bash
python -m pip install -r requirements.txt
streamlit run app.py
uvicorn api:app --reload
```
This report describes local deployment and testing. It must not be interpreted as a cloud production deployment.

## 5. Evaluation Strategy
The evaluation uses accuracy, precision, recall, and F1 macro metrics. Two baselines are included: a trivial majority-class predictor and a keyword-rule predictor.
**No independent human-validated golden evaluation dataset was available.** Reported metrics are diagnostic measurements based on the available sample and pseudo-labeling heuristics. They should not be interpreted as production accuracy or evidence of real-world generalization. 
Because no independent test set exists, the `evaluate.py` script gracefully degrades to an in-sample diagnostic run. 

## 6. Results and the Misleading Headline Number
The most important analytical finding is that high overall accuracy in this prototype is entirely misleading. 
The keyword baseline score of **1.0000** perfectly reflects the overlap between the heuristic rules and the pseudo-label generation; the model is simply memorizing the rules used to label it. 
Furthermore, the dataset is heavily imbalanced: approximately 85 of the 93 rows belong to `Other/Unknown`. Consequently, the majority-class baseline of **0.9140** mainly reflects this severe class imbalance. Rare-intent performance is consequently unreliable.

## 7. Failure Analysis
| Failure mode | Likely cause | Improvement |
|---|---|---|
| Ambiguous or short messages | Insufficient context | Clarifying question or escalation |
| Over-indexing on `Other / Unknown` | Extreme class imbalance (85/93 rows) | Targeted data collection and sampling |
| Rare intents missed | Sparse lexical features | Transitioning to dense embeddings (e.g., SentenceTransformers) |
| Multi-intent messages | Single-label taxonomy constraint | Multi-label or hierarchical classification |

## 8. What Was Intentionally Not Built
- Live Twitter/X integration.
- Real Amazon order-management CRM access.
- Automatic processing of real refunds, cancellations, or account changes.
- Expensive or rate-limited LLM API integrations.
- Production databases or live scraping pipelines.

## 9. One-Week Improvement Plan
- **Acquire a Golden Set**: Source and hand-label a 250-example evaluation set independent of the training heuristics.
- **Dataset Expansion**: Expand the training snippet far beyond 93 rows to mitigate the severe `Other / Unknown` class imbalance.
- **Semantic Retrieval**: Replace hardcoded, token-overlap evidence retrieval with a searchable semantic vector store (FAISS/Chroma).
- **Tune Thresholds**: Tune the 0.40 escalation threshold using rigorous false-positive and false-negative cost analysis once a golden set is available.

## 10. Technical Decision Log
The repository contains documented decisions in `DECISION_LOG.md`: Logistic Regression over Naive Bayes for probability calibration; 0.40 escalation threshold; deterministic safety overrides; segregated intent taxonomy via YAML; and local-only historical evidence.

## 11. Reproducibility Checklist
- `README.md` contains setup, training, and usage instructions with offline prototype disclaimers.
- `app.py` provides the dashboard and `api.py` provides the backend REST API.
- `configs/intent_taxonomy.yaml` contains routing configuration and escalation patterns.
- `src/` contains the ML pipeline, training loop, and evaluation logic.
- `test_cases.py` functions as an automated PyTest suite.
- No API keys, `.env` files, `.pkl` binaries, or cache directories are committed to version control.

**Conclusion**
The AmazonHelp AI Support Agent demonstrates a defensive workflow for assisted customer support: intent classification, safety-aware escalation, priority and department routing, interactive testing, and programmatic access. The project prioritizes transparency regarding its dataset limitations and highlights exactly what must be improved before any autonomous production use.
