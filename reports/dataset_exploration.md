# Dataset Exploration Report

- **Rows**: 2811774
- **Columns**: tweet_id, author_id, inbound, created_at, text, response_tweet_id, in_response_to_tweet_id, conversation_id
- **Missing Values**: {'tweet_id': 0, 'author_id': 0, 'inbound': 0, 'created_at': 0, 'text': 0, 'response_tweet_id': 1040629, 'in_response_to_tweet_id': 794335, 'conversation_id': 0}
- **Duplicate Tweet IDs**: 0
- **Date Range**: 2008-05-08 20:13:59 to 2017-12-03 23:14:01
- **Inbound Messages**: 1537843 (54.7%)
- **Outbound Messages**: 1273931 (45.3%)
- **Unique Authors**: 702777
- **Root Tweets**: 798197
- **Orphan/Incomplete Tweets**: 3862

## Conversation Reconstruction Approach
Root tweets were identified by tracing back the `in_response_to_tweet_id` until a tweet with no parent or a parent not in the dataset was found. The ID of this root tweet serves as the `conversation_id`. This groups messages by root and does not explicitly model branch structure.

## Limitations
- Missing tweets in the dataset create orphans and break conversations into multiple smaller threads.
- `response_tweet_id` is useful for forward traversal but we only needed backward traversal to find the root.

## Reproducibility
`python src/01_dataset_exploration.py --input twcs/twcs.csv`
