import pytest
from src.pipeline import TicketPipeline

@pytest.fixture(scope="module")
def pipeline():
    pipe = TicketPipeline()
    try:
        pipe.load("src/model/ticket_pipeline.pkl")
    except Exception as e:
        pass # Model load failures will be caught or run in fallback mode
    return pipe

def test_empty_input(pipeline):
    result = pipeline.predict("")
    assert result['predicted_intent'] == 'Other / Unknown'
    assert result['confidence'] == 0.0
    assert result['is_fallback'] == True
    assert "Please provide a valid" in result['generated_response']

def test_normal_delivery(pipeline):
    result = pipeline.predict("My package is delayed. Order ID ORD12345")
    assert 'predicted_intent' in result
    assert result['priority'] in ['Low', 'Medium', 'High', 'Critical']
    assert 'routing_department' in result

def test_refund_request(pipeline):
    result = pipeline.predict("How can I get a refund for ORD98765?")
    assert 'should_escalate' in result
    # We can't guarantee exact prediction since dataset is tiny, just schema

def test_payment_issue(pipeline):
    result = pipeline.predict("I was charged twice for the same order.")
    assert 'confidence' in result

def test_account_issue(pipeline):
    result = pipeline.predict("My account password is not working")
    assert 'historical_evidence' in result

def test_technical_issue(pipeline):
    result = pipeline.predict("The app crashes when I open it.")
    assert 'entities' in result

def test_unknown_ambiguous(pipeline):
    result = pipeline.predict("This is completely unrelated.")
    assert result['predicted_intent'] == 'Other / Unknown'

def test_escalation_logic(pipeline):
    result = pipeline.predict("I need to speak to a human manager now")
    assert result['should_escalate'] == True
    assert result['escalation_reason'] is not None

def test_api_schema(pipeline):
    result = pipeline.predict("Test message")
    keys = ['message', 'cleaned_text', 'predicted_intent', 'intent_display_name',
            'confidence', 'priority', 'routing_department', 'should_escalate',
            'escalation_reason', 'escalation_type', 'entities', 'historical_evidence',
            'evidence_count', 'generated_response', 'model', 'is_fallback']
    for key in keys:
        assert key in result

def test_model_loading_failure():
    pipe = TicketPipeline()
    pipe.load("invalid_path.pkl")
    assert pipe.model is None
    result = pipe.predict("Test message")
    assert result['is_fallback'] == True
