# Brand Selection Report

## Selection Criteria
Candidates are primarily ranked by usable-pair count and then compared using:
- Conversation depth.
- Unique customers.
- Unique conversations.
- Pair ratio.
- Suitability for downstream tasks.

## Candidate Comparison Table
| brand        |   total_messages |   inbound_customer |   outbound_support |   unique_customers |   unique_conversations |   multi_turn_convs |   both_inbound_outbound_convs |   no_support_response_convs |   avg_conv_length |   median_conv_length |   usable_pairs |   pair_ratio_pct |
|:-------------|-----------------:|-------------------:|-------------------:|-------------------:|-----------------------:|-------------------:|------------------------------:|----------------------------:|------------------:|---------------------:|---------------:|-----------------:|
| AmazonHelp   |           374042 |             203598 |             169840 |              73425 |                  82556 |              51260 |                         82556 |                           0 |              4.53 |                    3 |         153028 |            81.82 |
| AppleSupport |           238907 |             131764 |             106860 |              79517 |                  80717 |              28144 |                         80717 |                           0 |              2.96 |                    2 |         105487 |            88.31 |
| Uber_Support |           128550 |              72154 |              56270 |              39868 |                  41923 |              15088 |                         41923 |                           0 |              3.07 |                    2 |          55189 |            85.86 |
| SpotifyCares |            91889 |              48543 |              43265 |              28302 |                  28280 |              10500 |                         28277 |                           0 |              3.25 |                    2 |          41383 |            90.07 |
| AmericanAir  |            87584 |              50054 |              36764 |              23261 |                  26386 |              11577 |                         26386 |                           0 |              3.32 |                    2 |          36418 |            83.16 |

### Usable Pairs Definition and Limitations
Usable pairs are chronological adjacent-message proxies, not exact response-linked pairs.
It consists of an inbound customer message immediately followed by an outbound support message within the same reconstructed conversation.

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
Usable-pair volume is the primary ranking criterion, followed by qualitative comparison:
AmazonHelp was selected because it provides a large and diverse customer-support dataset, the highest usable inbound/outbound message-pair volume among the evaluated candidates, and substantial multi-turn conversation coverage. Although AppleSupport has a slightly higher unique-customer count, AmazonHelp offers stronger conversation depth and usable-pair volume for building and evaluating a support agent.

### Rejection Reasons for Other Candidates
- **AppleSupport**: Rejected despite high pair ratios (88%) because it has half the multi-turn conversations of Amazon, limiting depth for retrieval.
- **Uber_Support, SpotifyCares, AmericanAir**: Rejected because their overall scale (total pairs and multi-turn conversations) is significantly smaller than AmazonHelp. While their interactions are high quality, AmazonHelp provides a vastly larger repository of varied conversational data to train and evaluate against.
- **Risks**: All candidates (including AmazonHelp) present risks of noisy or repetitive conversations (e.g., standard "DM us your order number" replies). AmazonHelp's massive unique customer count mitigates this risk better than the others.

### Next Steps
Proceed to Phase 2: Filter the dataset exclusively for this brand, generate intent clusters, and prepare the grounded generation evaluation set.
