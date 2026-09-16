# Decision Log

## Architecture Choices
- **TF-IDF + LogisticRegression**: LogisticRegression was chosen to replace Naive Bayes because it produces better-calibrated confidence scores, which are strictly required for our low-confidence escalation routing rules.
- **Taxonomy Configuration**: The 8-intent taxonomy was externalized to `configs/intent_taxonomy.yaml`. This ensures routing and escalation rules can be updated without modifying core Python logic, preventing drift between API and UI.
- **Explainable Escalation Rules**: Escalations are handled via transparent Regex rules (e.g., detecting terms like "fraud", "stolen", "hack"). This was chosen over a black-box LLM to ensure deterministic safety flags for critical support paths.
- **Historical Evidence Lookup**: We implemented a local-only similarity check against `sample.csv`. This avoids exposing sensitive data to external APIs while satisfying the evidence-retrieval requirement.
- **Fallback Responses**: Deterministic, template-based safe responses are used. The system intentionally avoids claiming a refund or cancellation was processed since it lacks real Amazon CRM integration.

## Known Limitations
- **Dataset Limitations**: The model is trained on a tiny 93-row `sample.csv` snippet of TWCS data. 
- **Weak Supervision Leakage**: Because true human intent labels are absent, the model trains on pseudo-labels derived from heuristics. Consequently, evaluating it against the same data yields artificially perfect metrics.
- **Golden Set Absence**: An independent 250-example `golden_set.csv` was not found in the local repository. Evaluation defaults to in-sample diagnostics with strong warnings.
- **Production Status**: This is an offline prototype, not connected to Amazon systems.
