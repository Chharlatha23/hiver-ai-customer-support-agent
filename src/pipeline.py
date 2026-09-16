import os
import re
import joblib
import pandas as pd
import yaml
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class TicketPipeline:
    def __init__(self):
        self.model = None
        self.taxonomy = []
        self.taxonomy_dict = {}
        self.historical_data = None
        project_root = os.path.dirname(os.path.dirname(__file__))
        self.load_taxonomy(os.path.join(project_root, "configs", "intent_taxonomy.yaml"))
        self.load_historical_data(os.path.join(project_root, "sample.csv"))

    def load_taxonomy(self, path: str):
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = yaml.safe_load(f)
                self.taxonomy = data.get('intents', [])
                for intent in self.taxonomy:
                    self.taxonomy_dict[intent['display_name']] = intent
        else:
            # Basic fallback if no taxonomy
            self.taxonomy_dict = {}

    def load_historical_data(self, path: str):
        if os.path.exists(path):
            try:
                self.historical_data = pd.read_csv(path)
            except:
                self.historical_data = None

    def preprocess(self, text: str) -> str:
        if not text or not text.strip():
            return ""
        text = text.lower()
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def extract_entities(self, text: str) -> dict:
        order_id = re.search(r'\bORD\d+\b', text, flags=re.IGNORECASE)
        ticket_id = re.search(r'\bTKT\d+\b', text, flags=re.IGNORECASE)
        email = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
        phone = re.search(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
        return {
            "order_id": order_id.group(0).upper() if order_id else None,
            "ticket_id": ticket_id.group(0).upper() if ticket_id else None,
            "email": email.group(0) if email else None,
            "phone": phone.group(0) if phone else None
        }

    def get_intent_config(self, intent_name: str):
        return self.taxonomy_dict.get(intent_name, {
            'display_name': intent_name,
            'default_priority': 'Medium',
            'routing_department': 'General Support',
            'safe_response': "Thank you for reaching out to AmazonHelp. A customer support representative will review your message and get back to you shortly.",
            'escalation_rules': []
        })

    def determine_priority(self, intent_config: dict, text: str) -> str:
        base_priority = intent_config.get('default_priority', 'Medium')
        urgent_pattern = r'\b(urgent|asap|emergency|immediately|stolen|fraud|hack)\b'
        if re.search(urgent_pattern, text.lower()):
            return 'Critical'
        return base_priority

    def determine_routing(self, intent_config: dict) -> str:
        return intent_config.get('routing_department', 'General Support')

    def check_escalation(self, intent_config: dict, text: str, confidence: float):
        # Escalate on low confidence
        if confidence < 0.4:
            return True, "Low confidence prediction requires human review", "low_confidence"
            
        rules = intent_config.get('escalation_rules', [])
        for rule in rules:
            if re.search(rule['pattern'], text.lower()):
                return True, rule['reason'], "rule_match"
                
        global_escalation = r'\b(human|agent|manager|supervisor|lawyer|sue|threat)\b'
        if re.search(global_escalation, text.lower()):
            return True, "Explicit request for human or global escalation phrase detected", "global_rule"
            
        return False, None, None

    def lookup_historical_evidence(self, text: str):
        if self.historical_data is None or 'text' not in self.historical_data.columns:
            return [], 0
            
        # Very simple keyword match for mock retrieval
        words = set(text.lower().split())
        if not words:
            return [], 0
            
        matches = []
        for idx, row in self.historical_data.iterrows():
            if pd.isna(row.get('text')):
                continue
            hist_words = set(str(row['text']).lower().split())
            overlap = len(words.intersection(hist_words))
            if overlap >= 3:
                matches.append({
                    "text": str(row['text']),
                    "tweet_id": str(row.get('tweet_id', 'unknown'))
                })
                if len(matches) >= 3:
                    break
        return matches, len(matches)

    def generate_response(self, intent_config: dict, entities: dict, should_escalate: bool) -> str:
        base = intent_config.get('safe_response', "Thank you for reaching out.")
        if entities.get('order_id') and "order details" in base:
            base = base.replace("provide your order details", f"verify order {entities['order_id']}")
            
        if should_escalate and "escalating" not in base.lower():
            base += " I have also flagged this ticket for priority review by a human representative."
            
        return base

    def deterministic_intent(self, text: str):
        # Use taxonomy keywords if available
        if self.taxonomy:
            for intent in self.taxonomy:
                keywords = intent.get('keywords', [])
                if keywords:
                    pattern = r'\b(' + '|'.join(keywords) + r')\b'
                    if re.search(pattern, text):
                        return intent['display_name']
        return None

    def predict(self, ticket_text: str) -> dict:
        processed_text = self.preprocess(ticket_text)
        is_fallback = False
        
        if not processed_text:
            return {
                "message": ticket_text,
                "cleaned_text": "",
                "predicted_intent": "Other / Unknown",
                "intent_display_name": "Other / Unknown",
                "confidence": 0.0,
                "priority": "Low",
                "routing_department": "General Support",
                "should_escalate": False,
                "escalation_reason": None,
                "escalation_type": None,
                "entities": {},
                "historical_evidence": [],
                "evidence_count": 0,
                "generated_response": "Please provide a valid support ticket description.",
                "model": "tfidf_logistic_regression",
                "is_fallback": True
            }

        entities = self.extract_entities(ticket_text)
        intent = None
        confidence = 0.0
        
        if self.model:
            try:
                intent = self.model.predict([processed_text])[0]
                proba = self.model.predict_proba([processed_text])[0]
                confidence = float(max(proba))
            except:
                pass

        if not intent or confidence < 0.3:
            # Fallback to rules if ML fails or is very uncertain
            rule_intent = self.deterministic_intent(processed_text)
            if rule_intent:
                intent = rule_intent
                confidence = 1.0
                is_fallback = True
            else:
                intent = "Other / Unknown"
                confidence = 0.0
                is_fallback = True

        intent_config = self.get_intent_config(intent)
        
        priority = self.determine_priority(intent_config, processed_text)
        routing = self.determine_routing(intent_config)
        should_escalate, esc_reason, esc_type = self.check_escalation(intent_config, processed_text, confidence)
        
        evidence, evidence_count = self.lookup_historical_evidence(processed_text)
        
        response = self.generate_response(intent_config, entities, should_escalate)
        
        return {
            "message": ticket_text,
            "cleaned_text": processed_text,
            "predicted_intent": intent,
            "intent_display_name": intent_config.get('display_name', intent),
            "confidence": confidence,
            "priority": priority,
            "routing_department": routing,
            "should_escalate": should_escalate,
            "escalation_reason": esc_reason,
            "escalation_type": esc_type,
            "entities": entities,
            "historical_evidence": evidence,
            "evidence_count": evidence_count,
            "generated_response": response,
            "model": "tfidf_logistic_regression",
            "is_fallback": is_fallback
        }

    def save(self, path: str):
        joblib.dump(self.model, path)

    def load(self, path: str):
        try:
            self.model = joblib.load(path)
        except Exception:
            self.model = None
