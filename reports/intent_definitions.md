# Intent Definitions for AmazonHelp

This document details the discovered customer-support intents based on keyword/heuristic classification of inbound customer messages in the AmazonHelp dataset.

## Methodology & Limitations
- **Classification Rules**: Intent assignment uses deterministic regular expressions tested against normalized customer messages.
- **Single-Label**: Messages are assigned EXACTLY ONE intent based on a strict priority order (highest risk/specificity first). For example, a message mentioning both a 'hacked account' and 'refund' is classified as Account/Security.
- **Customer Messages Only**: AmazonHelp outbound replies are strictly excluded from these counts and examples.
- **Ambiguity/Overlap**: Keywords like 'cancel' might apply to 'Returns & Refunds' or 'Prime Subscriptions'. Context-free keyword matching is a proxy and not ground-truth annotation.

## 1. Account & Security
- **Definition**: Issues regarding account access, security, or unauthorized activity.
- **Inclusion Criteria**: Mentions of passwords, locked accounts, hacks, logins, or fraud. (Regex: `\b(password|lock(ed)?|hack(ed)?|login|log in|account|unauthorized|fraud)\b`)
- **Exclusion Criteria**: Payment issues not explicitly tied to account hacks.
- **Frequency**: 7647 messages (3.76%)
- **Representative Examples**:
  - `@AmazonHelp Thanks, have filled in a contact form. Is there any way to freeze the account in the meantime? I have the 'rogue' address.` (Conv: 1082229)
  - `@AmazonHelp hello really need your help my account ha been locked!!` (Conv: 1222617)
  - `@AmazonHelp How will the account specialist contact me?` (Conv: 932290)
  - `@AmazonHelp I cancelled Prime membership and have been expecting a credit to my account since. Please advise where I can follow up on the progress. It’s been past 5 working days already` (Conv: 2317931)
  - `@AmazonHelp This link need user login. My account is blocked, and need help to solve this.` (Conv: 363984)

## 2. Amazon Prime & Subscriptions
- **Definition**: Inquiries or issues related to Amazon Prime services and digital subscriptions.
- **Inclusion Criteria**: Mentions of Prime, membership fees, Prime Video, or Music. (Regex: `\b(prime|subscript(ion)?|member(ship)?|(prime|amazon) video|amazon music)\b`)
- **Exclusion Criteria**: Standard physical deliveries unless explicitly referencing Prime delays. Excludes generic mentions of 'video' (e.g., 'I took a video of the damage').
- **Frequency**: 14314 messages (7.03%)
- **Representative Examples**:
  - `@116618 - I got charged for a tv episode that is included with prime. How can I dispute this?` (Conv: 1246885)
  - `@AmazonHelp I feel like Amazon is not trying to keep non-prime customers. They want to force you to sign for Amazon Prime or wait a month for items.` (Conv: 1919765)
  - `@AmazonHelp @302018 Please add support for prime video for India on @127972. It can’t be that hard surely! Maybe someone needs to flip a switch somewhere :)` (Conv: 761836)
  - `@AmazonHelp If the Amazon website let me sign up for Prime with a card that has no money on it, will the membership be cancelled if 1/2` (Conv: 1095892)
  - `@115821 With the huge failure today driver around the corner and doesn't deliver my package now it's delayed, that's not PRIME. #FAIL` (Conv: 2807308)

## 3. Returns, Refunds & Cancellations
- **Definition**: Requests or issues regarding returning items, receiving refunds, billing issues, or cancelling orders.
- **Inclusion Criteria**: Mentions of returning, refunding, overcharging, or order cancellation. (Regex: `\b(return(ing|ed)?|refund(ed)?|money back|charge(d)? twice|cancel(led|ing|lation)?)\b`)
- **Exclusion Criteria**: General missing item complaints if refund isn't mentioned.
- **Frequency**: 12233 messages (6.01%)
- **Representative Examples**:
  - `@AmazonHelp CS rep then told me I have to pay for a second one again before u can despatch it. Now awaiting 2 refunds and hope system dont cancel again` (Conv: 740418)
  - `@AmazonHelp Return item(408-3942370-6997921) was picked up on 05/10 by BlueDart .Howver,its not reflecting in my order history and also refund pending.` (Conv: 183011)
  - `@AmazonHelp I will be heartbroken if Xenoblade Chronicles 2 does not arrive tomorrow. There are other items lost, overdue, and cancelled in my history. My customer email is iain at [twitter username].com.` (Conv: 65754)
  - `@AmazonHelp Anyways i need to be refunded by tomorrow evening or Tuesday i will go to consumer court with my lawyer and i have enough profs to prove` (Conv: 1608379)
  - `@AmazonHelp No options was just given a refund and told its out of stock....hence why we had preordered!!` (Conv: 2780525)

## 4. Missing or Lost Package
- **Definition**: Customer reports that a package was marked delivered but isn't there, or is lost in transit.
- **Inclusion Criteria**: Mentions of stolen, missing, or unreceived packages, or explicitly asking 'where is my order/parcel'. (Regex: `\b(missing|stolen|didn\'t receive|never arriv(ed|ing)|not receiv(ed|ing)|lost|where is (my|the) (order|package|parcel|item|delivery))\b`)
- **Exclusion Criteria**: Packages that are just delayed (see Delivery/Shipping).
- **Frequency**: 3490 messages (1.71%)
- **Representative Examples**:
  - `@AmazonHelp ... and I see I've been charged for everything, despite not receiving it. Crossing my fingers that I'll get the delivery only one day late!` (Conv: 2985480)
  - `It would be SUPER helpful if @115821 drivers stopped leaving my packages in strange places in the rain. Four times now they've been lost or ruined. Hasn't happened until recently. What's going on?! @AmazonHelp` (Conv: 2376132)
  - `lost the invoice of Moto G4+ purchased from amazon with imei number __credit_card__ @8850 @23773 @951 @115821 @115850` (Conv: 1445391)
  - `@AmazonHelp Where is my order details in that its just your courier service details not even the name of product is visible let alone order number` (Conv: 841262)
  - `How about a ‘where IS my package?’ button @AmazonHelp? £40 lost. 😡 https://t.co/SS9iH4oZFI` (Conv: 24559)

## 5. Item Condition (Damaged/Defective)
- **Definition**: Customer received an item but it is damaged, broken, or defective.
- **Inclusion Criteria**: Mentions of physical damage or items not functioning. (Regex: `\b(damag(e|ed)|broken|defect(ive)?|destroy(ed)?|scratch(ed)?|shatter(ed)?)\b`)
- **Exclusion Criteria**: Wrong items that are in good condition. Generic 'not working' is excluded to avoid app/tracking confusion.
- **Frequency**: 1686 messages (0.83%)
- **Representative Examples**:
  - `@115830 I ordered something from you and it's arrived damaged. I'm not sure who to contact, when I tried to leave a review with photos it wouldn't let me. U would like someone to contact me regarding this issue please` (Conv: 644804)
  - `@AmazonHelp 2nd time in a row I've received damaged/leaking groceries. I'm fed up! Why sell groceries if you can't deliver properly?? 😡😡` (Conv: 280203)
  - `@AmazonHelp Thanks for responding to my tweets. I'll definitely let you know my thoughts. I know that several of my friends who also collect amiibos have received them damaged from Amazon. Would like to possibly help the problem here.` (Conv: 2307127)
  - `@AmazonHelp Need resolution for someone to pickup broken delivery and not resolution to leave feedback. I want that broken item outta house` (Conv: 974002)
  - `Dear @115821 - AMZL sucks. Fix your broken self delivery service. Carriers should have the same basic mail knowledge as typical carriers.` (Conv: 2052271)

## 6. Wrong Item Received
- **Definition**: Customer received a delivery, but it contains the wrong item.
- **Inclusion Criteria**: Mentions of wrong, incorrect, or different items specifically. (Regex: `\b(wrong (item|order|product|book|dvd|cd)|incorrect (item|order|product)|not what i ordered|different item|sent the wrong)\b`)
- **Exclusion Criteria**: Missing items from an otherwise correct order. Generic 'incorrect' (e.g. incorrect address) is excluded.
- **Frequency**: 256 messages (0.13%)
- **Representative Examples**:
  - `@AmazonHelp That is the correct listing for the correct show. It might just be the incorrect product image for the one I sent you.` (Conv: 377730)
  - `@115850 Sending me a wrong product again and again. https://t.co/QObhKEzWnN` (Conv: 1385727)
  - `AMAZON SHIPPED THE WRONG ORDER AGAIN. SUPPOSED TO SEND ME THE RIGHT ONE. JUST GOT HOME AND THE WEONG ITEM WAS DELIVERED AGAIN @AmazonHelp` (Conv: 1408285)
  - `Just ordered 16 @15890 on Amazon, and they only sent 15 and they sent the wrong flavors. Never buying from a thrid party again` (Conv: 398691)
  - `@AmazonHelp Received wrong product for 5th time for the same order` (Conv: 1494754)

## 7. Delivery & Shipping Delays
- **Definition**: General inquiries about shipping status, delivery dates, tracking, or delays.
- **Inclusion Criteria**: Mentions of tracking, delivery status, or delayed shipping. (Regex: `\b(deliver(y|ed|ing)?|ship(ping|ped|ment)?|track(ing)?|arriv(e|ing|ed)?|delay(ed)?)\b`)
- **Exclusion Criteria**: Packages confirmed stolen or lost.
- **Frequency**: 30055 messages (14.76%)
- **Representative Examples**:
  - `@115821 worst delivery experience with Amazon, no importance of customer n it's time` (Conv: 285588)
  - `Waited in all day for my @115830 delivery which was due to be delivered before 8pm. Nothing. 🖒` (Conv: 166409)
  - `@AmazonHelp Should get rid of this...'Out for delivery  On its way to ...... US'. It's not out for delivery to the customer that day. That's confusing.` (Conv: 1537545)
  - `@AmazonHelp And then they told it will be delivered by today and if I am calling since morning he is telling it will be delivered by night` (Conv: 279914)
  - `@AmazonHelp I have not seen any reasons. I have only seen the 'arriving' date being pushed back each time I look.` (Conv: 295831)

## 8. App & Website Technical Issues
- **Definition**: Technical glitches experienced on the Amazon app or website.
- **Inclusion Criteria**: Mentions of app crashes, website glitches, or loading errors. (Regex: `\b(app (crash(ed)?|glitch(es)?|error|bug|won\'t open)|website (crash(ed)?|glitch(es)?|error|down|bug)|(site|page) (is )?down|won\'t load|loading error)\b`)
- **Exclusion Criteria**: Generic mentions of using the app/website without reporting an error.
- **Frequency**: 36 messages (0.02%)
- **Representative Examples**:
  - `@AmazonHelp Our home screen won't load` (Conv: 1221776)
  - `@AmazonHelp What is with the website?  Graphics won't load.  Can't see the pictures to buy merchandise.` (Conv: 1265711)
  - `Amazon India site down? @115850` (Conv: 2793112)
  - `@117634 I'm about to have a tantrum. My app won't open a book that I desperately need to read. It's doing that circle constantly going round and round. It's taunting me.` (Conv: 2584191)
  - `@AmazonHelp No thanks @AmazonHelp. Just reporting the website error to you guys. I don't need help and/or savings on the book. I'd recommend filing a trouble ticket for ASIN B00543720Y.  --Batman` (Conv: 1721643)

## 9. Customer Service Complaint
- **Definition**: Feedback or complaints regarding a previous customer service interaction.
- **Inclusion Criteria**: Mentions of unhelpful reps, long hold times, or terrible service. (Regex: `\b((bad|terrible|horrible|worst|useless|unhelpful) (customer )?service|rude (agent|rep|representative)|on hold for|hung up on)\b`)
- **Exclusion Criteria**: Positive feedback or neutral mentions of customer service.
- **Frequency**: 725 messages (0.36%)
- **Representative Examples**:
  - `@AmazonHelp Worst service ever. Had to yell to get a manager otherwise would have filled out the same form that I already provided twice` (Conv: 320599)
  - `@115850 is making fool of his customers selling products @ high prices. False promises and bad service. @118702 @17256 @AmazonHelp @11852 @4030 @14281` (Conv: 394929)
  - `@115821 Your customer service is the worst I've ever seen. Been on hold for over an hour. It's clear the representative has no idea what she's doing or what step to take next with my issue. Get it together.` (Conv: 596807)
  - `@AmazonHelp I have changed my mind about ever ordering from amazon again. So many problems w/ them the past 7 months. Bad customer service` (Conv: 1129900)
  - `@AmazonHelp Sooo, you're just going to once again ignore the question at hand? Thanks for continuing to provide horrible customer service!` (Conv: 2295511)

## 10. Other/Unclear
- **Definition**: Messages that do not explicitly match any of the prioritized intent heuristics.
- **Inclusion Criteria**: Fails to match any predefined regex rules.
- **Exclusion Criteria**: Matches any predefined rule.
- **Frequency**: 133156 messages (65.4%)
- **Representative Examples**:
  - `@116935 hey guys I’ve been having issues, my music keeps glitching` (Conv: 258819)
  - `Amazon care &amp;third party ("SHOPODEALZ")bt they can't solved this prob &amp; alwys neglect n prob.its rediculous things tht r happened @115850 @123644` (Conv: 71917)
  - `@AmazonHelp Amazon México :(` (Conv: 122743)
  - `@AmazonHelp Maybe fill my housemates bed with them so he thinks It's a waterbed 😂😍` (Conv: 1263080)
  - `@242301 @AmazonHelp Just fed up of them ignoring the issue mate` (Conv: 528255)

