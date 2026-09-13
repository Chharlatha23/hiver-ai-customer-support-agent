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

## Selected Brand: AmazonHelp
**AmazonHelp** is the recommended brand for the AI customer support agent.

### Justification
- It has the highest number of usable pairs (153029), ensuring ample data for intent classification and historical-response retrieval.
- It maintains a large number of unique conversations (82556) and high unique customer count (73425), ensuring topic diversity.
- The presence of 51260 multi-turn conversations indicates deep, meaningful support interactions rather than purely automated or single-turn responses.

### Rejection Reasons for Other Candidates
- **AppleSupport**: Rejected despite having 105487 usable pairs because AmazonHelp offers a superior overall volume of multi-turn and diverse customer interactions.
- **Uber_Support**: Rejected despite having 55190 usable pairs because AmazonHelp offers a superior overall volume of multi-turn and diverse customer interactions.
- **SpotifyCares**: Rejected despite having 41383 usable pairs because AmazonHelp offers a superior overall volume of multi-turn and diverse customer interactions.
- **AmericanAir**: Rejected despite having 36418 usable pairs because AmazonHelp offers a superior overall volume of multi-turn and diverse customer interactions.

### Risks and Limitations
- **Account Authenticity**: The identity is inferred from naming patterns and high outbound support volume, but not verified via external official channels.
- **Data Drift/Context**: Tweets may reference external links or specific localized outages that an AI agent cannot dynamically resolve without active systems integration.

### Next Steps
Proceed to Phase 2: Filter the dataset exclusively for this brand, generate intent clusters, and prepare the grounded generation evaluation set.
