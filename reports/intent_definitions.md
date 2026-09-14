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
- **Inclusion Criteria**: Mentions of Prime, membership fees, Prime Video, or Music. (Regex: `\b(prime|subscript(ion)?|member(ship)?|video|music)\b`)
- **Exclusion Criteria**: Standard physical deliveries unless explicitly referencing Prime delays.
- **Frequency**: 15031 messages (7.38%)
- **Representative Examples**:
  - `I don't know why @116316  Prime in Belgium isn't being carried out by @37596. @132988 isn't as fast (and not as good as Bpost).` (Conv: 2403888)
  - `.@120533 je n’en peux plus de ne pas recevoir mes colis en temps et en heure en étant Prime… Où est passée votre qualité de service? https://t.co/AHke4MPHqw` (Conv: 1093295)
  - `@AmazonHelp It has just been dispatched and is going to arrive tomorrow now. When you have guaranteed day of release and we have prime time delivery ?` (Conv: 1494253)
  - `Man...I love how the very first purchase I made AFTER my amazon prime renewed gets delayed somehow.  Meanwhile people ordered the same thing MONTHS after I did and it's on time for them.  Great business strategy.` (Conv: 2599700)
  - `@AmazonHelp Managing permissions on Advantage. I've sent in a video link to show the problem via my case log. Hopefully that helps.` (Conv: 2499199)

## 3. Returns, Refunds & Cancellations
- **Definition**: Requests or issues regarding returning items, receiving refunds, billing issues, or cancelling orders.
- **Inclusion Criteria**: Mentions of returning, refunding, overcharging, or order cancellation. (Regex: `\b(return(ing|ed)?|refund(ed)?|money back|charge(d)? twice|cancel(led|ing|lation)?)\b`)
- **Exclusion Criteria**: General missing item complaints if refund isn't mentioned.
- **Frequency**: 12213 messages (6.0%)
- **Representative Examples**:
  - `@AmazonHelp my constructive feedback on leap refund was not posted in amazon,   don't know why amazon try to protect their sellers??` (Conv: 851605)
  - `@AmazonHelp I was asked if I wanted a refund or replacement, I chose replacement but received an email saying you can’t replace.` (Conv: 529952)
  - `@AmazonHelp So, can you confirm, will I be able to Active the Trial at a later date or not if this is Cancelled currently?  Thanks!` (Conv: 145769)
  - `@AmazonHelp How do I return a damaged item from 3rd party seller?` (Conv: 2277875)
  - `@AmazonHelp Re-ordering the same monitor didn't go through (for some reason.) The customer rep that helped me offered a full refund so I can go ahead and reorder it. That's fine and dandy, but now this monitor's status is 1 in-stock and for 268.99. Which defeats the purpose of Black Friday.` (Conv: 560583)

## 4. Missing or Lost Package
- **Definition**: Customer reports that a package was marked delivered but isn't there, or is lost in transit.
- **Inclusion Criteria**: Mentions of stolen, missing, or unreceived packages. (Regex: `\b(missing|stolen|didn\'t receive|never arriv(ed|ing)|not receiv(ed|ing)|lost)\b`)
- **Exclusion Criteria**: Packages that are just delayed (see Delivery/Shipping).
- **Frequency**: 3293 messages (1.62%)
- **Representative Examples**:
  - `@AmazonHelp help! My partner ordered from you and still have not received - should have arrived on Wednesday` (Conv: 356692)
  - `@AmazonHelp Ordered 14-Oct, AmazonCC asked me to wait till 17-Oct then 24-Oct and now 26-Oct to work on escalation for not receiving product https://t.co/nfPd3U003j` (Conv: 1172163)
  - `@AmazonHelp Not received the email nothing @115850` (Conv: 1381161)
  - `@115821 You charged me twice. Your overseas rep lied BIG time. Now I have to dispute through Amazon Store card. My time is being stolen. Will be 4-5 calls to resolve. My big Christmas shopping not done and won't be through Amazon now or ever. Double charging everybody? Thieves!` (Conv: 481711)
  - `@AmazonHelp An "Add-On" item is missing from the package I picked up yesterday. The order was packed by Amazon. I can find no appropriate support details for contact to report this and get a replacement. Can you give me a link please?` (Conv: 481485)

## 5. Item Condition (Damaged/Defective)
- **Definition**: Customer received an item but it is damaged, broken, or defective.
- **Inclusion Criteria**: Mentions of physical damage or items not functioning. (Regex: `\b(damag(e|ed)|broken|defect(ive)?|destroy(ed)?|scratch(ed)?|shatter(ed)?|not working)\b`)
- **Exclusion Criteria**: Wrong items that are in good condition.
- **Frequency**: 2137 messages (1.05%)
- **Representative Examples**:
  - `@AmazonHelp Yes I have reported this to your support staff and they have directed me to send the pictures of the defective product via email` (Conv: 1141932)
  - `I can't place my order bcz issue is "amazon pay balance" after selection this mode, it is not working for further procedures .  I regularly tried to contact customer care executive but no response found 😡 plz help urgently...............................` (Conv: 2542905)
  - `Thanks to my @AmazonHelp delivery driver who called to ask if I was home, could barely speak English,asked to put the parcel in my outside letterbox,i advised if too big to put it in the porch.He couldn't understand&amp;left it  hanging out the letterbox!Parcel&amp;goods water damaged👎` (Conv: 2747237)
  - `@AmazonHelp 1. To get the TV installed was a nightmare. 2. Have been having issues with the TV not working - goes blank screen  frequently` (Conv: 227382)
  - `@115821 is your new biz plan converting new items to damaged ones so you can sell at discount/loss?` (Conv: 1828781)

## 6. Wrong Item Received
- **Definition**: Customer received a delivery, but it contains the wrong item.
- **Inclusion Criteria**: Mentions of wrong, incorrect, or different items. (Regex: `\b(wrong|incorrect|not what i ordered|different item)\b`)
- **Exclusion Criteria**: Missing items from an otherwise correct order.
- **Frequency**: 1933 messages (0.95%)
- **Representative Examples**:
  - `@AmazonHelp Did the same on the last wrong order... Got  I support yet...` (Conv: 2193238)
  - `@164818 @AmazonHelp last week @115830 sent me the wrong version of a game because they had increased the price after i'd bought it,. Good luck with this` (Conv: 206211)
  - `@115821  all the promo prices were incorrect in my shopping cart,what's up w/that? U need to credit me the difference,this is BS. What kind of scam are you running?#blackfriday` (Conv: 152144)
  - `@AmazonHelp Yes. But you've delivered there before including very recently. There's clearly something wrong with this order only or perhaps your courier` (Conv: 367403)
  - `@AmazonHelp They sent me to the wrong one - found it myself - if anyone else asks, its to the left of the entrance to Debenhams, ground floor, opposite The Gate!` (Conv: 2883293)

## 7. Delivery & Shipping Delays
- **Definition**: General inquiries about shipping status, delivery dates, tracking, or delays.
- **Inclusion Criteria**: Mentions of tracking, delivery status, or delayed shipping. (Regex: `\b(deliver(y|ed|ing)?|ship(ping|ped|ment)?|track(ing)?|arriv(e|ing|ed)?|delay(ed)?|where is my (order|package))\b`)
- **Exclusion Criteria**: Packages confirmed stolen or lost.
- **Frequency**: 29480 messages (14.48%)
- **Representative Examples**:
  - `@AmazonHelp Was my first issue with shipping. Obviously it was an inconvenience and frustrating. Will continue to shop. #primememberfor3+years` (Conv: 584573)
  - `@AmazonHelp It's always Amazon Logistics. Never reads the delivery instructions.` (Conv: 1693668)
  - `Pathetic delivery experience by @115850. Confirmed delivery without the delivery. Thanks for brilliant work. #thankyou` (Conv: 1765373)
  - `@AmazonHelp Hi can you DM me , I want a better idea of what time my delivery is` (Conv: 2104295)
  - `Expecting my #sirui #monopod and #ballhead to arrive today , thanks to @115850 #AmazonPrime` (Conv: 346728)

## 8. App & Website Technical Issues
- **Definition**: Technical glitches experienced on the Amazon app or website.
- **Inclusion Criteria**: Mentions of app crashes, website glitches, or loading errors. (Regex: `\b(app|website|site|glitch|error|load(ing)?|crash(ed)?|bug|won\'t open)\b`)
- **Exclusion Criteria**: Account login issues (see Account & Security).
- **Frequency**: 5043 messages (2.48%)
- **Representative Examples**:
  - `@AmazonHelp did the sonos play:1 promo end? I thought tomorrow was last day. Your site is not accepting the promo code. Please advise!` (Conv: 411881)
  - `@AmazonHelp Where is that on the website?` (Conv: 423980)
  - `@AmazonHelp Yeah. I’d still like to get my orders. I’m familiar with the customer service option in the app. There’s no excuse for these delays. https://t.co/WVtzxUoXx2` (Conv: 2570137)
  - `@AmazonHelp não pararia na alfândega pelas taxas e tudo mais?Queria comprar pelo site da amazon brasileira e não correr o risco de taxarem 200% do valor` (Conv: 1339871)
  - `@AmazonHelp hi, when will you list the Intel i7-8700k on the UK site? It’s supposed to release today.` (Conv: 235661)

## 9. Customer Service Complaint
- **Definition**: Feedback or complaints regarding a previous customer service interaction.
- **Inclusion Criteria**: Mentions of unhelpful reps, long hold times, or terrible service. (Regex: `\b(customer service|hold|agent|representative|rep\b|worst|terrible|horrible|unhelpful)\b`)
- **Exclusion Criteria**: General complaints about shipping without mentioning support staff.
- **Frequency**: 4582 messages (2.25%)
- **Representative Examples**:
  - `@AmazonHelp @115851 dear team you are https://t.co/csafCG5zeB guys world's best customer service company. I really appreciate ur work and honesty.tnx` (Conv: 644717)
  - `been 10 days. customer service keeps askin me to wait for 24 hours more.Amazon India's service is a joke. I've been having problems with every single time I use the service! Just coz you've almst monopolized the market doesn mean you get to treat customers like trash @115821` (Conv: 80761)
  - `@AmazonHelp @115850 worst service by you` (Conv: 311048)
  - `@115830 your service for me recently has been shocking. I have emailed you about this issue but don't buy a TV people is a total ballache! Customer service team are not helpful and don't know what's going on. #crapservice #BlackFriday #amazon #unhappy` (Conv: 2898872)
  - `@AmazonHelp Don't get any problems with @122232 or @115817 and there customer service is great too` (Conv: 229801)

## 10. Other/Unclear
- **Definition**: Messages that do not explicitly match any of the prioritized intent heuristics.
- **Inclusion Criteria**: Fails to match any predefined regex rules.
- **Exclusion Criteria**: Matches any predefined rule.
- **Frequency**: 122239 messages (60.04%)
- **Representative Examples**:
  - `@AmazonHelp No safe place set up as just a book and thought would fit in letterbox, but have checked bins just in case and nothing there` (Conv: 2470094)
  - `@AmazonHelp すみません、運送業者のサイトで確認したところ商品自体は受け取り店(コンビニ)に到着しているようなのですが、受け取り番号が発行されていないようです この場合はどうしたら良いのでしょうか?` (Conv: 215171)
  - `@AmazonHelp  https://t.co/I6uwqGCjGd` (Conv: 2725040)
  - `@115850 Why I wasted my time to go to service center when the same will be applicable automatically.` (Conv: 2296683)
  - `@AmazonHelp Thanks for checking the conversation, do help me by fulfilling the commitment done. #AwaitingResolution https://t.co/QsUNlq47l5` (Conv: 1055275)

