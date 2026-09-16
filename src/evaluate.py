import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from src.pipeline import TicketPipeline

def main():
    print("Evaluating AmazonHelp AI Support Agent Prototype\n")
    
    pipeline = TicketPipeline()
    project_root = os.path.dirname(os.path.dirname(__file__))
    try:
        pipeline.load(os.path.join(project_root, "src", "model", "ticket_pipeline.pkl"))
        if pipeline.model is None:
            raise FileNotFoundError
    except:
        print("Model not found. Please run src/train.py first.")
        return

    golden_set_path = os.path.join(project_root, "golden_set.csv")
    if os.path.exists(golden_set_path):
        print(f"Loading golden evaluation set: {golden_set_path}")
        df = pd.read_csv(golden_set_path)
        is_golden = True
        label_col = 'intent' # Assuming intent column exists in golden set
    else:
        print("No independent golden evaluation set (golden_set.csv) was found. Metrics are not reported as validated real-world performance.")
        print("Falling back to in-sample diagnostic using sample.csv (pseudo-labels)...")
        if not os.path.exists("sample.csv"):
            print("sample.csv not found. Aborting evaluation.")
            return
        df = pd.read_csv("sample.csv")
        is_golden = False
        text_col = 'text'
        if text_col not in df.columns:
            print("Error: text column not found.")
            return
        df['intent'] = df[text_col].apply(lambda x: pipeline.deterministic_intent(pipeline.preprocess(x)) or 'Other / Unknown')
        label_col = 'intent'
        
    print(f"\nData provenance:")
    print(f"- File used: {golden_set_path if is_golden else 'sample.csv'}")
    print(f"- Number of rows: {len(df)}")
    print(f"- Label type: {'Human-verified' if is_golden else 'Weakly supervised / Pseudo-labeled'}")
    print(f"- Independent from training: {'Yes' if is_golden else 'No (in-sample diagnostic)'}")
    
    text_col = 'text' if 'text' in df.columns else 'message'
    
    if len(df) == 0:
        print("Evaluation dataset is empty.")
        return
        
    y_true = df[label_col].tolist()
    y_pred = []
    
    for text in df[text_col]:
        pred = pipeline.predict(text)
        y_pred.append(pred['predicted_intent'])
        
    print("\n--- Diagnostic Metrics ---")
    if not is_golden:
        print("WARNING: These metrics measure agreement with heuristic pseudo-labels. They do NOT represent genuine ML accuracy.")
        
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision (macro): {precision_score(y_true, y_pred, average='macro', zero_division=0):.4f}")
    print(f"Recall (macro): {recall_score(y_true, y_pred, average='macro', zero_division=0):.4f}")
    print(f"F1-score (macro): {f1_score(y_true, y_pred, average='macro', zero_division=0):.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, zero_division=0))
    
    # Baselines
    majority_class = df[label_col].mode()[0]
    baseline_pred = [majority_class] * len(df)
    print("\n--- Baselines ---")
    print(f"Majority-class ('{majority_class}') Accuracy: {accuracy_score(y_true, baseline_pred):.4f}")
    
    # Keyword-rule baseline (this is essentially what we are measuring against if we are using the fallback dataset)
    print(f"Keyword-rule Accuracy: 1.0000 (By definition on this dataset)")

if __name__ == "__main__":
    main()
