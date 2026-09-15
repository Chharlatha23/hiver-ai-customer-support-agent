# Hiver AI Customer Support Agent

## Overview
This project builds an AI-powered customer support agent using historical Twitter customer-support conversations. The agent aims to assist and automate customer support responses based on a structured analysis of the Customer Support on Twitter (TWCS) dataset.

## Project Phases

### Phase 1: Dataset Exploration and Brand Selection
- Dataset exploration.
- Conversation reconstruction.
- Candidate brand comparison.
- AmazonHelp selection.

### Phase 2: Intent Discovery
- Customer message filtering.
- Intent taxonomy.
- Rule-based baseline classification.
- Intent distribution analysis.
- Representative examples.

### Future Phases
- Historical response retrieval.
- Similar-conversation search.
- Response drafting.
- Confidence scoring.
- Human escalation.
- Evaluation.

## Dataset Setup

The raw TWCS dataset must be downloaded separately and placed at the path expected by the scripts (`twcs/twcs.csv`), as documented in `data/README.md`. 
**Do not include the raw dataset in GitHub.**

## Installation

```bash
pip install -r requirements.txt
```
