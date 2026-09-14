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
- **Inclusion Criteria**: Mentions of physical damage or items not functioning. (Regex: `\b(damag(e|ed)|broken|defect(ive)?|destroy(ed)?|scratch(ed)?|shatter(ed)?|not working)\b`)
- **Exclusion Criteria**: Wrong items that are in good condition.
- **Frequency**: 2151 messages (1.06%)
- **Representative Examples**:
  - `Same day delivery not working then @115821` (Conv: 1297450)
  - `@117634 Any idea why wi fi stopped working on Kindle today? Wife's Kindle is not working too.` (Conv: 1190195)
  - `@115850 had ordered combo essential oil pack. One has broken seal,customer care number is getting disconnected automatically. Help here` (Conv: 2511193)
  - `@AmazonHelp By Amazon - you? If you can't help am I wasting my time? Like I am being asked to waste time/effort etc. sending you broken china pieces.` (Conv: 1338721)
  - `@AmazonHelp why do you not send books in protective packaging? I just received 3 books from you all scratched and with other damage -_-` (Conv: 1004387)

## 6. Wrong Item Received
- **Definition**: Customer received a delivery, but it contains the wrong item.
- **Inclusion Criteria**: Mentions of wrong, incorrect, or different items. (Regex: `\b(wrong|incorrect|not what i ordered|different item)\b`)
- **Exclusion Criteria**: Missing items from an otherwise correct order.
- **Frequency**: 1940 messages (0.95%)
- **Representative Examples**:
  - `@AmazonHelp Bugger, I did. Nothing conflicting in my post. U tell me what was wrong. @115821 stop hiring interns for SM and Digital` (Conv: 987369)
  - `@115821 can't get their shit together - Possible delay in delivery due to arrival at incorrect carrier facility - on my order for 8 days.` (Conv: 359202)
  - `Hey @115833 why does #Alexa get this wrong when #GoogleHome gets it right? I just asked for the temperature, not for the Iliad &amp; Odyssey https://t.co/EztkaJP6b4` (Conv: 871209)
  - `@AmazonHelp Order 204-8057426-5071528 issue with product being incorrect. Who do I speak to?` (Conv: 2432807)
  - `@AmazonHelp Yes it’s my details on the label and everything was ordered fulfilled by amazon. I’m thinking someone may have put the wrong label on the boxes like it was a mix up` (Conv: 2292092)

## 7. Delivery & Shipping Delays
- **Definition**: General inquiries about shipping status, delivery dates, tracking, or delays.
- **Inclusion Criteria**: Mentions of tracking, delivery status, or delayed shipping. (Regex: `\b(deliver(y|ed|ing)?|ship(ping|ped|ment)?|track(ing)?|arriv(e|ing|ed)?|delay(ed)?)\b`)
- **Exclusion Criteria**: Packages confirmed stolen or lost.
- **Frequency**: 29360 messages (14.42%)
- **Representative Examples**:
  - `@AmazonHelp ordered something same day delivery but it still hasn’t arrived. Is there a chance it could still come or will this be tomorrow?` (Conv: 2306226)
  - `@AmazonHelp No I did not, only saw it from the "track package"` (Conv: 2971861)
  - `Slow round of applause to @115830 who just delayed an advent calendar I ordered until the 6th December. 🤔` (Conv: 494116)
  - `@AmazonHelp I can actually do a new order now and would get it shipped faster than my pre-order in march.  Or just go to a store and get it.` (Conv: 2570904)
  - `@115851 can you make a software for creating product link for flat files.because relying on third party can delay us to update inventory. Happen with me today. #AmazonIndia  #ProudAmazonseller` (Conv: 2845566)

## 8. App & Website Technical Issues
- **Definition**: Technical glitches experienced on the Amazon app or website.
- **Inclusion Criteria**: Mentions of app crashes, website glitches, or loading errors. (Regex: `\b(app|website|site|glitch|error|load(ing)?|crash(ed)?|bug|won\'t open)\b`)
- **Exclusion Criteria**: Account login issues (see Account & Security).
- **Frequency**: 5150 messages (2.53%)
- **Representative Examples**:
  - `If anyone has the site for the @115821 customer service portal where they actually read the chat/emails, that would helpful info. Thanks and Happy Thanksgiving.` (Conv: 115883)
  - `@AmazonHelp Desde su centro de atencion al cliente ya han confirmado que no se ha producido ningún fraude.Una vez más su solucion es que tengo que pagar yo un error de ustedes.Muchas gracias por hacerme perder mi tiempo y mi dinero  #amazon #blackfriday #desastredeservicio` (Conv: 181233)
  - `@AmazonHelp Seems to be working now, without having cleared the cache. The issue was in both the app and the site, so caching wasn’t the issue. Thanks.` (Conv: 644009)
  - `@AmazonHelp no, the formatting is just gone. It's like i have low internet connection but every other site is working perfectly.` (Conv: 881095)
  - `@AmazonHelp its better weather i am going with another online website/store. Amazon takes 20 days in this process to get ready a product for DispatchWOW` (Conv: 985102)

## 9. Customer Service Complaint
- **Definition**: Feedback or complaints regarding a previous customer service interaction.
- **Inclusion Criteria**: Mentions of unhelpful reps, long hold times, or terrible service. (Regex: `\b(customer service|hold|agent|representative|rep\b|(worst|terrible|horrible|unhelpful) (customer )?service)\b`)
- **Exclusion Criteria**: General complaints about shipping without mentioning support staff.
- **Frequency**: 3734 messages (1.83%)
- **Representative Examples**:
  - `Customer service at its best. @115830 @AmazonHelp. 10 yrs a customer and never a bad experience. Kudos to the team. #satisfiedcustomer` (Conv: 1265724)
  - `Hey @AmazonHelp can I get some help with an order issue? I called customer service twice but they are having issues comprehending my problem` (Conv: 1245432)
  - `@AmazonHelp Just spoke with rep. He said I'd 2 call tomo b/w 9 n 5 but I'm at work all that time. He said he'd pass msg on...` (Conv: 1286726)
  - `@AmazonHelp and was asked if I wanted to give customer service a chance. I said yes and waited on hold to speak with someone. She was able to provide` (Conv: 357370)
  - `@AmazonHelp  @115850 your customer service executives are worst. I haven't received my cashback in 4 mnths despite several complaints. https://t.co/zNb85n3mtt` (Conv: 918252)

## 10. Other/Unclear
- **Definition**: Messages that do not explicitly match any of the prioritized intent heuristics.
- **Inclusion Criteria**: Fails to match any predefined regex rules.
- **Exclusion Criteria**: Matches any predefined rule.
- **Frequency**: 123579 messages (60.7%)
- **Representative Examples**:
  - `@AmazonHelp Pas encore Ma femme va le faire dans la foulée` (Conv: 1632494)
  - `@AmazonHelp Très bien merci je vais suivre cette procédure` (Conv: 529081)
  - `@115850  tell me what detail do you need? https://t.co/FhtRrOsU76` (Conv: 1655017)
  - `@AmazonHelp Thanks for the link. I submitted a couple order issues. Is there an easy way to do that online for orders that are late?` (Conv: 364025)
  - `@AmazonHelp わざわざ、リプありがとうございます🍀` (Conv: 660343)

