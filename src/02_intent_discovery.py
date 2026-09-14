import argparse
import pandas as pd
import numpy as np
import os
import re
import importlib.util
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Discover customer intents for AmazonHelp.')
    parser.add_argument('--input', type=str, default='twcs/twcs.csv', help='Path to twcs.csv')
    parser.add_argument('--output_dir', type=str, default='reports', help='Directory for reports')
    return parser.parse_args()

def load_reconstruction_logic():
    # Dynamically import from 01_dataset_exploration.py without renaming the file
    script_path = os.path.join(os.path.dirname(__file__), '01_dataset_exploration.py')
    spec = importlib.util.spec_from_file_location("exploration", script_path)
    exploration = importlib.util.module_from_spec(spec)
    sys.modules["exploration"] = exploration
    spec.loader.exec_module(exploration)
    return exploration.reconstruct_conversations

# Intent Definitions & Heuristics
# Classification Priority matches the order of this list.
INTENT_RULES = [
    {
        "name": "Account & Security",
        "regex": r'\b(password|lock(ed)?|hack(ed)?|login|log in|account|unauthorized|fraud)\b',
        "definition": "Issues regarding account access, security, or unauthorized activity.",
        "inclusion": "Mentions of passwords, locked accounts, hacks, logins, or fraud.",
        "exclusion": "Payment issues not explicitly tied to account hacks."
    },
    {
        "name": "Amazon Prime & Subscriptions",
        "regex": r'\b(prime|subscript(ion)?|member(ship)?|video|music)\b',
        "definition": "Inquiries or issues related to Amazon Prime services and digital subscriptions.",
        "inclusion": "Mentions of Prime, membership fees, Prime Video, or Music.",
        "exclusion": "Standard physical deliveries unless explicitly referencing Prime delays."
    },
    {
        "name": "Returns, Refunds & Cancellations",
        "regex": r'\b(return(ing|ed)?|refund(ed)?|money back|charge(d)? twice|cancel(led|ing|lation)?)\b',
        "definition": "Requests or issues regarding returning items, receiving refunds, billing issues, or cancelling orders.",
        "inclusion": "Mentions of returning, refunding, overcharging, or order cancellation.",
        "exclusion": "General missing item complaints if refund isn't mentioned."
    },
    {
        "name": "Missing or Lost Package",
        "regex": r'\b(missing|stolen|didn\'t receive|never arriv(ed|ing)|not receiv(ed|ing)|lost)\b',
        "definition": "Customer reports that a package was marked delivered but isn't there, or is lost in transit.",
        "inclusion": "Mentions of stolen, missing, or unreceived packages.",
        "exclusion": "Packages that are just delayed (see Delivery/Shipping)."
    },
    {
        "name": "Item Condition (Damaged/Defective)",
        "regex": r'\b(damag(e|ed)|broken|defect(ive)?|destroy(ed)?|scratch(ed)?|shatter(ed)?|not working)\b',
        "definition": "Customer received an item but it is damaged, broken, or defective.",
        "inclusion": "Mentions of physical damage or items not functioning.",
        "exclusion": "Wrong items that are in good condition."
    },
    {
        "name": "Wrong Item Received",
        "regex": r'\b(wrong|incorrect|not what i ordered|different item)\b',
        "definition": "Customer received a delivery, but it contains the wrong item.",
        "inclusion": "Mentions of wrong, incorrect, or different items.",
        "exclusion": "Missing items from an otherwise correct order."
    },
    {
        "name": "Delivery & Shipping Delays",
        "regex": r'\b(deliver(y|ed|ing)?|ship(ping|ped|ment)?|track(ing)?|arriv(e|ing|ed)?|delay(ed)?|where is my (order|package))\b',
        "definition": "General inquiries about shipping status, delivery dates, tracking, or delays.",
        "inclusion": "Mentions of tracking, delivery status, or delayed shipping.",
        "exclusion": "Packages confirmed stolen or lost."
    },
    {
        "name": "App & Website Technical Issues",
        "regex": r'\b(app|website|site|glitch|error|load(ing)?|crash(ed)?|bug|won\'t open)\b',
        "definition": "Technical glitches experienced on the Amazon app or website.",
        "inclusion": "Mentions of app crashes, website glitches, or loading errors.",
        "exclusion": "Account login issues (see Account & Security)."
    },
    {
        "name": "Customer Service Complaint",
        "regex": r'\b(customer service|hold|agent|representative|rep\b|worst|terrible|horrible|unhelpful)\b',
        "definition": "Feedback or complaints regarding a previous customer service interaction.",
        "inclusion": "Mentions of unhelpful reps, long hold times, or terrible service.",
        "exclusion": "General complaints about shipping without mentioning support staff."
    }
]
# Fallback is "Other/Unclear"

def classify_intent(text):
    text_lower = str(text).lower()
    for rule in INTENT_RULES:
        if re.search(rule["regex"], text_lower):
            return rule["name"]
    return "Other/Unclear"

def main():
    args = parse_args()
    if not os.path.exists(args.input):
        print(f"Error: Dataset {args.input} not found.")
        return
        
    print("Loading dataset...")
    df = pd.read_csv(args.input, dtype={'tweet_id': str, 'in_response_to_tweet_id': str, 'author_id': str})
    
    # 1. Reconstruct conversations using Phase 1 logic
    reconstruct_conversations = load_reconstruction_logic()
    df = reconstruct_conversations(df)
    
    # 2. Filter AmazonHelp conversations
    print("Filtering AmazonHelp conversations...")
    amazon_convs = df[df['author_id'] == 'AmazonHelp']['conversation_id'].unique()
    amazon_df = df[df['conversation_id'].isin(amazon_convs)]
    
    # 3. Identify customer-authored inbound messages
    print("Isolating customer inbound messages...")
    customer_msgs = amazon_df[(amazon_df['inbound'] == True) & (amazon_df['author_id'] != 'AmazonHelp')].copy()
    total_customer_msgs = len(customer_msgs)
    print(f"Total AmazonHelp customer inbound messages: {total_customer_msgs}")
    
    # 4. Normalize text and apply single-label classification
    print("Classifying intents (this may take a minute)...")
    customer_msgs['normalized_text'] = customer_msgs['text'].str.lower()
    customer_msgs['intent'] = customer_msgs['normalized_text'].apply(classify_intent)
    
    # 5. Calculate distribution
    print("Calculating distribution...")
    dist = customer_msgs['intent'].value_counts().reset_index()
    dist.columns = ['intent', 'message_count']
    dist['percentage'] = (dist['message_count'] / total_customer_msgs * 100).round(2)
    dist['cumulative_count'] = dist['message_count'].cumsum()
    dist['total_customer_messages'] = total_customer_msgs
    
    os.makedirs(args.output_dir, exist_ok=True)
    dist.to_csv(os.path.join(args.output_dir, 'intent_distribution.csv'), index=False)
    
    # Verify sum
    assert dist['message_count'].sum() == total_customer_msgs, "Intent counts do not reconcile with total customer messages!"
    
    # 6. Sample 5 representative examples per intent
    print("Sampling examples...")
    np.random.seed(42) # fixed random seed
    examples = []
    
    intents = [rule['name'] for rule in INTENT_RULES] + ["Other/Unclear"]
    for intent in intents:
        subset = customer_msgs[customer_msgs['intent'] == intent]
        if len(subset) >= 5:
            sampled = subset.sample(5)
        else:
            sampled = subset
            
        for _, row in sampled.iterrows():
            examples.append({
                'intent': intent,
                'tweet_id': row['tweet_id'],
                'conversation_id': row['conversation_id'],
                'author_id': row['author_id'],
                'original_customer_message': row['text'],
                'normalized_message': row['normalized_text']
            })
            
    examples_df = pd.DataFrame(examples)
    examples_df.to_csv(os.path.join(args.output_dir, 'intent_examples.csv'), index=False)
    
    # 7. Write Definitions Report
    print("Writing definitions report...")
    report_path = os.path.join(args.output_dir, 'intent_definitions.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Intent Definitions for AmazonHelp\n\n")
        f.write("This document details the discovered customer-support intents based on keyword/heuristic classification of inbound customer messages in the AmazonHelp dataset.\n\n")
        
        f.write("## Methodology & Limitations\n")
        f.write("- **Classification Rules**: Intent assignment uses deterministic regular expressions tested against normalized customer messages.\n")
        f.write("- **Single-Label**: Messages are assigned EXACTLY ONE intent based on a strict priority order (highest risk/specificity first). For example, a message mentioning both a 'hacked account' and 'refund' is classified as Account/Security.\n")
        f.write("- **Customer Messages Only**: AmazonHelp outbound replies are strictly excluded from these counts and examples.\n")
        f.write("- **Ambiguity/Overlap**: Keywords like 'cancel' might apply to 'Returns & Refunds' or 'Prime Subscriptions'. Context-free keyword matching is a proxy and not ground-truth annotation.\n\n")
        
        priority = 1
        for rule in INTENT_RULES:
            intent_name = rule['name']
            stats = dist[dist['intent'] == intent_name]
            count = stats['message_count'].values[0] if not stats.empty else 0
            pct = stats['percentage'].values[0] if not stats.empty else 0.0
            
            f.write(f"## {priority}. {intent_name}\n")
            f.write(f"- **Definition**: {rule['definition']}\n")
            f.write(f"- **Inclusion Criteria**: {rule['inclusion']} (Regex: `{rule['regex']}`)\n")
            f.write(f"- **Exclusion Criteria**: {rule['exclusion']}\n")
            f.write(f"- **Frequency**: {count} messages ({pct}%)\n")
            f.write("- **Representative Examples**:\n")
            
            ex_subset = examples_df[examples_df['intent'] == intent_name]
            if not ex_subset.empty:
                for _, ex in ex_subset.iterrows():
                    # Replace newlines in text to prevent breaking markdown lists
                    clean_text = ex['original_customer_message'].replace('\n', ' ')
                    f.write(f"  - `{clean_text}` (Conv: {ex['conversation_id']})\n")
            else:
                f.write("  - *Not enough examples.*\n")
            f.write("\n")
            priority += 1
            
        # Add Other/Unclear
        stats = dist[dist['intent'] == 'Other/Unclear']
        count = stats['message_count'].values[0] if not stats.empty else 0
        pct = stats['percentage'].values[0] if not stats.empty else 0.0
        f.write(f"## {priority}. Other/Unclear\n")
        f.write("- **Definition**: Messages that do not explicitly match any of the prioritized intent heuristics.\n")
        f.write("- **Inclusion Criteria**: Fails to match any predefined regex rules.\n")
        f.write("- **Exclusion Criteria**: Matches any predefined rule.\n")
        f.write(f"- **Frequency**: {count} messages ({pct}%)\n")
        f.write("- **Representative Examples**:\n")
        ex_subset = examples_df[examples_df['intent'] == 'Other/Unclear']
        if not ex_subset.empty:
            for _, ex in ex_subset.iterrows():
                clean_text = ex['original_customer_message'].replace('\n', ' ')
                f.write(f"  - `{clean_text}` (Conv: {ex['conversation_id']})\n")
        else:
            f.write("  - *Not enough examples.*\n")
        f.write("\n")
        
    print("Done! Phase 2 reports successfully generated.")

if __name__ == "__main__":
    main()
