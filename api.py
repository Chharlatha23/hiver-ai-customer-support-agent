from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.pipeline import TicketPipeline

app = FastAPI(title="AmazonHelp Ticket Classification API")

import os
pipeline = TicketPipeline()
project_root = os.path.dirname(os.path.abspath(__file__))
try:
    pipeline.load(os.path.join(project_root, "src", "model", "ticket_pipeline.pkl"))
except:
    print("Warning: Could not load model. Operating in rule-based fallback mode.")

class TicketRequest(BaseModel):
    ticket: str

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "AmazonHelp AI Support API"
    }

@app.post("/predict")
def predict(req: TicketRequest):
    if not hasattr(req, 'ticket') or req.ticket is None or str(req.ticket).strip() == "":
        raise HTTPException(status_code=400, detail="Ticket text cannot be empty.")
    
    try:
        prediction = pipeline.predict(req.ticket)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error while processing the request.")
