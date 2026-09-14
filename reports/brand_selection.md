# Brand Selection Report

## Selection Criteria
Candidates were ranked based on a balanced assessment of:
1. **Usable Pairs**: The absolute number of customer-question/support-answer pairs (inbound followed by brand outbound).
2. **Unique Conversations**: To ensure a wide variety of contexts.
3. **Multi-turn Conversations**: To support robust conversational context.
4. **Unique Customers**: A proxy for issue diversity and customer distribution.

## Candidate Comparison Table
| brand        |   total_messages |   inbound_customer |   outbound_support |   unique_customers |   unique_conversations |   multi_turn_convs |   avg_conv_length |   usable_pairs |   pair_ratio_pct |
|:-------------|-----------------:|-------------------:|-------------------:|-------------------:|-----------------------:|-------------------:|------------------:|---------------:|-----------------:|
| AmazonHelp   |           374042 |             203598 |             169840 |              73425 |                  82556 |              51260 |              4.53 |         153029 |            81.82 |
| AppleSupport |           238907 |             131764 |             106860 |              79517 |                  80717 |              28144 |              2.96 |         105487 |            88.31 |
| Uber_Support |           128550 |              72154 |              56270 |              39868 |                  41923 |              15088 |              3.07 |          55190 |            85.87 |
| SpotifyCares |            91889 |              48543 |              43265 |              28302 |                  28280 |              10500 |              3.25 |          41383 |            90.07 |
| AmericanAir  |            87584 |              50054 |              36764 |              23261 |                  26386 |              11577 |              3.32 |          36418 |            83.16 |

### Usable Pairs Definition and Limitations
`usable_pairs` is a conservative proxy consisting of an inbound customer message immediately followed by an outbound support message within the same reconstructed conversation. It does not guarantee that the outbound message is the direct response to that exact customer tweet.

**Limitations of this approach**:
- Consecutive customer messages can cause the earlier message to be excluded.
- Multiple support replies can cause some replies to be excluded.
- Chronological adjacency does not always prove direct reply intent.
- Actual `response_tweet_id` edges are not currently used for pair counting.

## Selected Brand: AmazonHelp
**AmazonHelp** is the recommended brand for the AI customer support agent.

### Account Identity
- `AmazonHelp` is the selected support account identifier.
- The account is inferred from dataset account naming and behavior.
- No external account-verification API was used.
- The project treats `AmazonHelp` as the operational brand label for subsequent phases.

### Justification
AmazonHelp is preferred based on a balanced evaluation:
- **Volume and Coverage**: Highest number of usable pairs (153029) and a strong pair ratio (81.82%). While the ranking is volume-dominated, the sheer scale ensures sufficient examples for all downstream tasks.
- **Diversity**: Largest pool of unique customers (73425) and unique conversations (82556), providing excellent diversity for intent discovery.
- **Depth**: 51,260 multi-turn conversations and an average conversation length of 4.53 implies deep, meaningful interactions rather than isolated automation, which is critical for historical-response retrieval.

### Rejection Reasons for Other Candidates
- **AppleSupport**: Rejected despite high pair ratios (88%) because it has half the multi-turn conversations of Amazon, limiting depth for retrieval.
- **Uber_Support, SpotifyCares, AmericanAir**: Rejected because their overall scale (total pairs and multi-turn conversations) is significantly smaller than AmazonHelp. While their interactions are high quality, AmazonHelp provides a vastly larger repository of varied conversational data to train and evaluate against.
- **Risks**: All candidates (including AmazonHelp) present risks of noisy or repetitive conversations (e.g., standard "DM us your order number" replies). AmazonHelp's massive unique customer count mitigates this risk better than the others.

### Next Steps
Proceed to Phase 2: Filter the dataset exclusively for this brand, generate intent clusters, and prepare the grounded generation evaluation set.
