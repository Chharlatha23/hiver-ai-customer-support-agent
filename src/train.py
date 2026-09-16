import os
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.pipeline import TicketPipeline

def main():
    project_root = os.path.dirname(os.path.dirname(__file__))
    print("Loading dataset...")
    df = pd.read_csv(os.path.join(project_root, "sample.csv"))
    
    text_col = 'text'
    if text_col not in df.columns:
        print("Error: text column not found.")
        return

    # Bootstrap labels using deterministic rules since sample.csv has no intent column
    pipeline = TicketPipeline()
    print("Bootstrapping labels with weak supervision/pseudo-labels...")
    df['intent'] = df[text_col].apply(lambda x: pipeline.deterministic_intent(pipeline.preprocess(x)) or 'Other / Unknown')
    
    label_col = 'intent'
    
    print(f"Dataset size: {len(df)}")
    print("Label distribution (Note: These are pseudo-labels, not manually verified human labels):")
    print(df[label_col].value_counts())
    
    X = df[text_col].apply(pipeline.preprocess)
    y = df[label_col]
    
    print("Training TF-IDF + LogisticRegression model...")
    model = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ('clf', LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced'))
    ])
    
    model.fit(X, y)
    
    pipeline.model = model
    
    model_dir = os.path.join(project_root, "src", "model")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "ticket_pipeline.pkl")
    pipeline.save(model_path)
    
    print(f"Training completion successful.")
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()
