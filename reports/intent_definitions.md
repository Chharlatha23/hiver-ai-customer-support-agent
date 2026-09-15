# Hiver AI Customer Support Agent

## Intent Definitions for AmazonHelp

This document details the discovered customer-support intents based on keyword/heuristic classification of inbound customer messages in the AmazonHelp dataset.

### Methodology & Limitations
- **Classification Rules**: Intent assignment uses deterministic regular expressions tested against normalized customer messages.
- **Single-Label**: Messages are assigned EXACTLY ONE intent based on a strict priority order (highest risk/specificity first).
- **Limitations**: This is a deterministic regex/keyword baseline, NOT a true unsupervised machine-learning or embedding-based model. Future improvements should incorporate semantic embeddings for improved clustering.

### Intent Taxonomy

| Intent | Definition | Inclusion | Exclusion |
|--------|------------|-----------|-----------|
| Missing or Lost Package | Customer reports that a package was marked delivered but isn't there, or is lost in transit. | Mentions of stolen, missing, or unreceived packages, or explicitly asking 'where is my order/parcel'. | Packages that are just delayed (see Delivery/Shipping). |
| Wrong Item Received | Customer received a delivery, but it contains the wrong item. | Mentions of wrong, incorrect, or different items specifically. | Missing items from an otherwise correct order. Generic 'incorrect' (e.g. incorrect address) is excluded. |
| Damaged or Defective Item | Customer received an item but it is damaged, broken, or defective. | Mentions of physical damage or items not functioning. | Wrong items that are in good condition. Generic 'not working' is excluded to avoid app/tracking confusion. |
| Returns, Refunds & Cancellations | Requests or issues regarding returning items, receiving refunds, billing issues, or cancelling orders. | Mentions of returning, refunding, overcharging, or order cancellation. | General missing item complaints if refund isn't mentioned. |
| Payment & Billing | Issues regarding payment methods, unexpected charges, or billing. | Mentions of charges, payments, cards, banks, or fees. | Refunds (handled by Returns, Refunds & Cancellations). |
| Delivery & Shipping Delays | General inquiries about shipping status, delivery dates, tracking, or delays. | Mentions of tracking, delivery status, or delayed shipping. | Packages confirmed stolen or lost. |
| Orders & General Order Issues | General order inquiries not covered by missing, wrong, or damaged item rules. | Mentions of ordering, purchasing, or buying. | Specific order issues like missing/damaged items. |
| Account & Security | Issues regarding account access, security, or unauthorized activity. | Mentions of passwords, locked accounts, hacks, logins, or fraud. | Payment issues not explicitly tied to account hacks. |
| Prime & Subscriptions | Inquiries or issues related to Amazon Prime memberships. | Mentions of Prime, membership fees, or subscription renewals. | Digital content playback (handled by Digital Services). |
| Digital Services & Media | Issues with Amazon's digital media services. | Mentions of Video, Music, Kindle, Audible, or streaming. | Physical media (DVDs/CDs) unless explicitly related to a digital copy. |
| Seller & Marketplace Issues | Issues specifically calling out third-party sellers on the marketplace. | Mentions of third-party sellers, vendors, or storefronts. | General order complaints where the seller isn't explicitly mentioned. |
| App & Website Technical Issues | Technical glitches experienced on the Amazon app or website. | Mentions of app crashes, website glitches, or loading errors. | Generic mentions of using the app/website without reporting an error. |
| Customer Service Complaint | Feedback or complaints regarding a previous customer service interaction. | Mentions of unhelpful reps, long hold times, or terrible service. | Positive feedback or neutral mentions of customer service. |
| Other/Unclear | Messages that do not explicitly match any of the prioritized intent heuristics. | Fails to match any predefined regex rules. | Matches any predefined rule. |

