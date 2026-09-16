import streamlit as st
from src.pipeline import TicketPipeline

st.set_page_config(page_title="AmazonHelp AI Support Agent", layout="wide")

@st.cache_resource
def load_pipeline():
    import os
    pipeline = TicketPipeline()
    project_root = os.path.dirname(os.path.abspath(__file__))
    try:
        pipeline.load(os.path.join(project_root, "src", "model", "ticket_pipeline.pkl"))
    except Exception as e:
        st.error(f"Could not load ML model. Operating in fallback mode. Error: {e}")
    return pipeline

pipeline = load_pipeline()

st.title("AmazonHelp AI Support Agent")
st.write("This application classifies Amazon customer support messages, routes tickets, determines priority, checks escalation rules, and provides safe response templates.")
st.warning("⚠️ **DISCLAIMER:** This is a prototype for an AI support system and is not a live Amazon customer support application. It does not connect to actual Amazon services or process real orders, refunds, or cancellations.")

sample_tickets = [
    "My package is delayed and has not arrived. Order ID ORD12345",
    "I want to return the product and get a refund. ORD98765",
    "My payment failed but money was deducted. Possible fraud.",
    "My account was hacked and password changed.",
    "I want to speak with a human manager immediately!",
    "What are the specifications of this product?",
    "This is an unrelated or ambiguous message.",
    ""
]

selected_sample = st.selectbox("Select a sample message or write your own:", [""] + sample_tickets)

if "ticket_input" not in st.session_state:
    st.session_state.ticket_input = ""

if selected_sample:
    st.session_state.ticket_input = selected_sample

ticket = st.text_area("Customer Message", value=st.session_state.ticket_input, height=150)

col1, col2 = st.columns([1, 5])
with col1:
    classify_btn = st.button("Analyze Ticket", type="primary")
with col2:
    if st.button("Clear"):
        st.session_state.ticket_input = ""
        st.rerun()

if classify_btn:
    if not ticket.strip():
        st.error("Please enter a customer message.")
    else:
        with st.spinner("Analyzing..."):
            result = pipeline.predict(ticket)
            
            st.subheader("Classification & Routing")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Predicted Intent", result["intent_display_name"])
            c2.metric("Confidence", f"{result['confidence']:.2f}")
            c3.metric("Priority", result["priority"])
            c4.metric("Routing Dept", result["routing_department"])
            
            st.subheader("Escalation Status")
            if result["should_escalate"]:
                st.error(f"🚨 ESCALATION REQUIRED: {result['escalation_reason']}")
            else:
                st.success("✅ No automatic escalation required.")
                
            st.subheader("Extracted Entities")
            st.json(result["entities"])
            
            st.subheader("Historical Evidence Lookup")
            if result["evidence_count"] > 0:
                st.info(f"Found {result['evidence_count']} similar historical messages.")
                st.json(result["historical_evidence"])
            else:
                st.warning("No local historical match was found.")
            
            st.subheader("Generated Support Reply")
            st.info(result["generated_response"])
            
            with st.expander("Model & Pipeline Metadata"):
                st.write(f"**Pipeline Strategy**: {result['model']}")
                st.write(f"**Fallback Activated**: {result['is_fallback']}")
                st.json(result)
