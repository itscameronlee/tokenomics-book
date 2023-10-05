# **Tokenomics for Builders: The Comprehensive Practitioner’s Guide to Token Design**

by [MattyTokenomics](https://www.notion.so/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b?pvs=21) with special thanks to [The Stacks Foundation](https://www.notion.so/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b?pvs=21) and [additional contributors](https://www.notion.so/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b?pvs=21)

## Disclaimer

*This document and all resources, threads, models, and materials linked to within are for informational purposes only. None of this document’s contents, nor the contents linked to within, should be construed as legal advice, or financial advice, technical advice, investment advice, or representations in any way regarding any legal, technical, financial, or investment matters by the author. The author is not a lawyer or financial advisor in any jurisdiction, and highly encourages readers to engage with registered professionals to ensure compliance with any and all relevant laws and regulations.*

## Press & Awards for **Tokenomics for Builders**

- [**CryptoDaily - Unlocking The Secrets To Successful Tokenomics**](https://cryptodaily.co.uk/2023/09/unlocking-the-secrets-to-successful-tokenomics-an-interview-with-matty-token-economics)
- [**HackerNoon - Tokenomics: What Developers Should Know Before Launching a Token**](https://hackernoon.com/tokenomics-what-developers-should-know-before-launching-a-token)
- [**1st Place Smoothie Awards**](https://smoothie.so/product/content/tokenomics-for-builders/9ej1n1el)

!https://smoothie-awards.s3.us-west-1.amazonaws.com/projects/icons/a08dced8-658c-49e3-a83c-c09e541c979b.png

## Table of Contents

💡 **This open source guide is divided into two parts.**

- Part One: fundamental concepts and history every builder should know
- Part Two: a step-by-step process to design and optimize your token

# Introduction

## Foreword

Let’s face it - most tokens are useless money grabs.

But that doesn’t negate the fact that tokens enable new possibilities for distributing ownership, aligning incentives in complex systems, bootstrapping network effects, and building credibly neutral, censorship-resistant protocols that can compete in the free market against more centralized tools.

And it doesn’t mean launching a well-designed token is impossible.

This open source guide is for teams that are considering launching a token and want to do it the right way. It covers all the concepts, tools, and frameworks builders and developers need to know, it’s not a textbook to become a tokenomics professional (if that’s what you’re looking for [this reading list](https://twitter.com/mattyTokenomics/status/1662117802315255808?s=20) is a good complement to this guide).

The guide and the accompanying Tokenomics Design Canvas have been used by more than 50 teams across multiple Web3 startup programs, received praise from founders backed by Tier 1 investors such as Placeholder, and been featured in publications including [CryptoDaily](https://cryptodaily.co.uk/2023/09/unlocking-the-secrets-to-successful-tokenomics-an-interview-with-matty-token-economics) and [HackerNoon](https://hackernoon.com/tokenomics-what-developers-should-know-before-launching-a-token).

I began compiling the guide after speaking with teams that had just graduated from a Web3 accelerator. Each team was dealing with the same challenges:

- Struggling to formalize their assumptions and token incentive mechanisms
- Researching the same industry best practices for vesting, allocation, and emissions
- Compiling the same models and spreadsheets
- Wondering how to even begin the token design process

It was clear to me they needed guidance to tokenomics from a builders’ perspective.

All the teams had great products, which was a necessary start. No amount of token burns, emission rate reductions, and other supply-side manipulations can save a token that ultimately has zero use cases, zero benefits, and zero demand.

But even with a great product, tokens are not easy to get right. The long-term success of blockchain products requires a system - an economy - in which participants act on their own selfish interests, yet the aggregate result of their individual behaviors is an equilibrium that improves the stability, longevity, and user experience of the product. And all without a centralized party actively coordinating user behavior.

Easier said than done.

As tokenomics deals partially with human behavior, it is as much a soft science (psychology, sociology, economics) and applied science (engineering), as it is a hard science (math, physics).

Unlike the hard sciences, soft sciences rarely deal with *correct* and *incorrect* absolutes, only tradeoffs that are *better* or *worse* at optimizing for a given objective in a given context. For this reason, it is impossible to lay out precise mathematical formulas to arrive at “correct” token designs.

By the same measure, no single person can be an expert in every aspect of tokenomics - as a builder, you should be deeply skeptical of anyone who claims that they are, or that all the relevant concepts can be quickly mastered.

This guide collects and builds on the established best thinking and practices from field experts and empirical analysis, and is meant to walk you through starting from scratch to completing a first draft of your full token design.

Good luck.

## Provide Feedback or Content

Community help and expertise in improving this guide are welcome. If you find something you think is unclear, incomplete, or which can be improved please [get in touch](https://www.notion.so/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b?pvs=21).

If you’d like to help but aren’t sure how to get involved, see the [Requested Additions & Edits](https://www.notion.so/Tokenomics-for-Builders-The-Comprehensive-Practitioner-s-Guide-to-Token-b5154feba117415cafd67678355e317b?pvs=21) appendix for areas of this guide that could benefit from further content and development.

## Acknowledgments

Special thanks to [The Stacks Foundation](https://stacks.org/) for contributing to making this guide possible. Additional thanks to:

- [ygg_anderson](https://twitter.com/ygg_anderson), steward at [Token Engineering Commons](https://tecommons.org/)
- [Florian Strauf](https://twitter.com/ffstrauf), founder at [Tokenomics DAO](https://tokenomicsdao.xyz/)
- [Maximillian Gusche](https://twitter.com/guccikudo), core contributor at [Tokenomics DAO](https://tokenomicsdao.xyz/)
- Katherine Webb, tokenomics analyst at [Animoca Brands](https://www.animocabrands.com/)
- [Jeff](https://twitter.com/jefftoshi), founder at [Mechanism](https://www.mechanism.so/)
- [Albert Liang](https://twitter.com/btc_albert), founder at [Bitcoin Startup Lab](https://btcstartuplab.com/)
- Early test readers at Tokenomics DAO and Token Engineering Commons:
    - Marco Germanier-Torrado
    - [Please DM me how you would like me to cite you in this section if I have forgotten to include you!]


# 1.1 Why does Tokenomics Matter?

You’re a blockchain developer or founder (or aspire to be one). Maybe you already have a problem in mind you want to solve. Maybe you’ve already designed a great solution to the problem that people will love.

Why then should you worry about tokenomics?

Because, the decisions you make (or fail to make) on your tokenomics will impact nearly every aspect of what you’re working on, including:

- Regulatory and legal risks
- Ownership and governance
- User experience
- Frictions and barriers to adoption
- Retention, engagement, and usage
- Rate of growth
- Value created for your users
- Value captured by your project
- Value accrued to your token (*not the same thing as creating or capturing value!*)
- Exploit, abuse, and attack vectors
- Longevity and resiliency
- User acquisition strategy
- And more…

We’ll cover all these topics in this guide. But for the purposes of explaining *why* tokenomics is so important, we can group its major impacts into three key areas:

1. **Directing User Behavior**
2. **Bootstrapping Network Effects**
3. **Enabling User Ownership**

# Directing User Behavior

In a traditional tech product, the centralized party which owns or controls the technology has full reign over what users can and can not do, as well as who is allowed, and who isn’t allowed, to use it.

If Facebook, Uber, Twitter, Airbnb, or Uber don’t like what a user is doing, they can explicitly ban them, shadow-ban them, migrate them to different product versions, or restrict them from accessing certain features - all without the user’s consent, or even the user’s knowledge.

In the transparent world of blockchain, with on-chain data and open source, verifiable smart contracts, users have visibility and control. Projects can of course be forked to make changes to an existing product, but even then, the decision about which fork to adopt is ultimately up to users.

As a crypto builder, tokenomics matter because you can not force your users to do much of anything, nor prevent them from doing what they want to do:

- Bitcoin can not *force* miners to secure the network, nor can it *prevent* a miner from attempting a >50% attack
- Curve can not *force* users to keep liquidity in the protocol, nor can it *prevent* liquidity providers from dumping liquidity rewards as soon as possible
- Decentralized stablecoins like RAI or LUSD can not **force** the free market to maintain the peg, nor can they **prevent** traders from trying to manipulate the price

> 💡 This is one reason why many governments feel threatened by blockchain technology. The state has a monopoly on force - for example, since abandoning the gold standard, the only thing backing the US Dollar is the threat of violence from the military and judicial system. But if the world migrates to protocols where no one can *force* anyone else to do something against their will, the state’s force becomes irrelevant, and their control begins to erode.

So, if you can’t **force** users to behave how you want them to, what can you do? You can *direct* user behavior by creating the right incentives:

- Bitcoin can not **force** miners to add hash power to the network, but it directs them to do so by **incentiviz**i**ng** them with block rewards and network transaction fees
- Curve can not *force* users to provide liquidity, but it directs them to do so by **incentivizing** them with CRV token rewards (which represent rights to governance control and a share of protocol revenues from trading fees)
- RAI or LUSD can not **force** users to maintain the peg, but they direct them to do so by **incentivizing** them to sell when above target price and buy when below target price

Without proper incentives to reward desired behavior and deter undesired behavior, Bitcoin would not be secure from >50% attacks, Curve would struggle to retain liquidity, and decentralized stablecoins like RAI or LUSD would not maintain their peg.

When we’re talking about tokenomics, we’re fundamentally talking about incentives that can make or break your product.

While this may **sound** straightforward - “it’s just about incentives, that’s simple enough” - getting incentives right can be deceptively tricky. And the difficult thing about building blockchain products and balancing these incentives is that there’s very little room for error - it’s much easier for a centralized solution to recover from a misstep, since they can force changes on users, than a less centralized one which can not.

https://twitter.com/jessewldn/status/1683805696297406465?s=20

Rewarding desired user behaviors, without introducing negative or unforeseen side effects, is much easier said that done, and warped incentives have been directly responsible for some of the biggest failures in crypto history:

- Steemit, which reached a market cap of $2bn at its peak, was the largest early attempt at a blockchain social media platform. It tried to [incentivize content *quality* but inadvertently incentivized content *quantity*](https://arxiv.org/pdf/1904.07310.pdf). The inevitable result was high quantities of low-quality spam content that slowly killed organic usage of the product.
- Terra’s Anchor protocol, which at its peak held $14bn in deposits in Terra USD (UST), incentivized Terra ecosystem users to mint more UST and deposit it to earn a 19.5% yield, while not balancing this with a commensurate incentive to borrow UST. Unsurprisingly, this resulted in a gap between the protocol’s liabilities (outgoing yield obligations paid to UST depositors) and its assets (incoming interest earnings earned from UST borrowers). Such a deficit is unsustainable in the long term, which [made UST a ticking time bomb for a bank run](https://www.coindesk.com/markets/2022/05/09/investors-flee-terras-anchor-as-ust-stablecoin-repeatedly-loses-1-peg/) that would take down Anchor, UST, and LUNA. Those who understood the incentives at play [foresaw the meltdown many months in advance](https://twitter.com/FreddieRaynolds/status/1526060401569550339?s=20).
- DeFi exchange Mango Markets suffered a [$114m market exploit not cause by a bug or hack](https://www.coindesk.com/tech/2022/10/20/defi-exchange-mangos-114m-exploit-was-market-manipulation-not-a-hack-ex-fbi-special-agent-says/), but because the protocol unintentionally [incentivized manipulation of oracle prices](https://twitter.com/joshua_j_lim/status/1579987648546246658?s=20) (though the [exploiter himself put it slightly differently](https://twitter.com/avi_eisen/status/1581326199682265088)). A positive expected value for attacking the protocol created a perverse incentive to do so, and though the [exploiter was eventually arrested](https://www.coindesk.com/policy/2022/12/27/mango-markets-exploiter-eisenberg-arrested-in-puerto-rico/), the protocol was left insolvent.
- NFT marketplace LooksRare, which reached a peak market cap of more than $1bn was once at least [the 3rd largest marketplace by trading volume](https://dune.com/sealaunch/NFT?Select+Timeframe_ef4aff=720+days&Select+Date+Granularity_e0aaf0=week), tries to incentivize user adoption by rewarding trading activity. As a side effect though, Looksrare rewards users to generate “fake volume” by [wash trading](https://blog.chainalysis.com/reports/2022-crypto-crime-report-preview-nft-wash-trading-money-laundering/) back and forth with themselves. An estimated [95% of LooksRare’s volume is wash trading](https://beincrypto.com/95-trading-volume-looksrare-linked-wash-trading/), and even when they ranked 3rd by trading volumes, they ranked 6th by number of unique users as a result.

Despite working products and zealous communities for products like Steemit, Terra, and others, flawed incentives, created by flawed tokenomics, meant they were doomed from the start.

>💡 Even the strongest products, concepts, or communities can collapse due to poor tokenomics which incentive users to engage in value-destructive, rather than value-adding, behaviors - just look at [Steemit](https://arxiv.org/pdf/1904.07310.pdf), [Iron/Titan](https://www.cnbc.com/2021/06/24/why-titan-crypto-crash-that-burned-mark-cuban-may-not-signal-similar-bitcoin-plunge.html#:~:text=%E2%80%9CThe%20iron%20model%20was%20deeply%20flawed%20from%20a%20tokenomics%20perspective%2C%E2%80%9D%20said%20Mati%20Greenspan%2C%20portfolio%20manager%20and%20Quantum%20Economics%20founder), [Luna/UST](https://twitter.com/FreddieRaynolds/status/1463394348326961153?s=20&t=H795L7JXL0rXclDz8YY2HA), or Mango Markets.


Designing well-balanced incentives is complex, and it’s especially difficult to do without a systematic approach that includes quantitative modeling and stochastic simulations.

Part Two of this guide will cover practical frameworks for incentive mechanism design and introduce tools like the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21) to help builders lay out their tokenomics with a systematic approach.

For now though, keep in mind that as a blockchain builder, tokenomics matter because they are your toolset for directing user behavior.

Not only to get users to do what you want them to do, but just as importantly, to avoid them doing what you *don’t* want them to do.

# Bootstrapping Network Effects

Let’s set blockchain aside for a moment. Think of Uber. Airbnb. YouTube. What do they have in common?

They’re all two-sided marketplaces:

- Uber pairs *riders* with *drivers*
- Airbnb coordinates *hosts* and *travelers*
- YouTube helps *viewers* find content *creators*

Like all two-sided marketplaces, they each faced the “bootstrapping problem” or “cold start problem” when they launched. It’s a “chicken and egg” situation - which came first?

- Uber is only useful to **riders** if there are already lots of **drivers** available on the app.
- But… Uber is only useful to **drivers** if there are lots of **riders** already requesting rides.

So, if you just started Uber and want to grow the company:

**To get drivers on the app you need existing riders on the app, but…**

**To get riders on the app, you need existing drivers on the app, but…**

**(repeat)**

The bootstrapping problem affects **every** marketplace business. And it’s a big problem for any new product because it makes it difficult to compete with existing big players.

To see why let’s visualize how valuable Uber is to users in aggregate (network value) compared to the total number of users in the network (size of the network):

[Source*:* [The Network Effects Bible](https://www.nfx.com/post/network-effects-bible)](https://www.nfx.com/_next/image?url=https%3A%2F%2Fcontent.nfx.com%2Fwp-content%2Fuploads%2F2019%2F07%2FCritical-Mass.png&w=3840&q=75)

Source*:* [The Network Effects Bible](https://www.nfx.com/post/network-effects-bible)

Notice that network value drastically increases per unit of size beyond the point of critical mass. Once Uber amasses enough drivers and riders, each new rider and driver not only inherits a high amount of existing value in the network but also adds significant marginal value.

New entrants trying to compete start at the very left of the chart. Uber’s network already has (much) more value, and to make matters worse, Uber’s value grows at a faster rate for each new user acquired.

This network effect makes it extremely difficult and expensive for new competitors to gain market share once a handful of large companies have already reached critical mass.

As a result, tech-powered industries [tend to exhibit *winner-take-all*](https://www.london.edu/think/nine-reasons-why-tech-markets-are-winner-take-all) or *winner-take-most* dynamics:

- Amazon and Shopify dominate e-commerce
- Facebook and TikTok dominate social media
- Google dominates web search
- Airbnb dominates hosting
- Uber dominates ride sharing

None of these are blockchain products though, so why should you care?

Because network effects also apply to blockchain products. In fact, nearly every blockchain product is an **n-sided** marketplace business model - even centralized products like Binance.

| Product | Number of Sides | Parties Involved |
| --- | --- | --- |
| Binance | 2 | - Buyers - Sellers |
| Curve | 3 | - Liquidity Providers - Liquidity Takers (traders) - Protocols incentivizing their token’s liquidity |
| Bored Ape Yacht Club | 2 | - Artists (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3963881) - Collectors |
| Axie Infinity | 2 | - Players with more money than time - Players with more time than money |

Network effects are not a theoretical concept that only shows up in MBA courses or VC blog posts. We can observe the quantified impact of Binance’s network effect with our own eyes.

![Source*:* [Kaiko Research: April 4, 2022](https://blog.kaiko.com/tether-market-liquidity-shows-strong-improvement-9a02afd613a1)](https://miro.medium.com/max/1400/0*SLuqXnnuWKy9Bb15.png)

Source*:* [Kaiko Research: April 4, 2022](https://blog.kaiko.com/tether-market-liquidity-shows-strong-improvement-9a02afd613a1)

In the above graphic, the younger and smaller exchanges have higher slippage costs than Binance. Network effects are so powerful because they become a self-reinforcing cycle:

*More liquidity means lower slippage…*

**Lower slippage means more traders placing trades…**

*More trading activity means more fees and/or spreads to earn…*

*More fees and/or spreads to earn means more liquidity is attracted…*

*(repeat)*
 

Not only do network effects also apply to blockchain products, they’re an even **bigger** piece of defensibility for blockchain products vs traditional tech products. Consider the below example of starting a competitor to Uber, vs starting a competitor to Uniswap.

**Create a Web2 Uber Competitor**

- Compete to hire developers to build comparable software from scratch
- Compete to acquire enough user data to train your algorithms to be as effective
- Compete with Uber’s brand affinity and user loyalty
- Compete with Uber’s network effect (they offer each rider more drivers and each driver more riders)

**Create a Uniswap Competitor**

- Copy Uniswap’s open source smart contract code
- Copy Uniswap users’ usage data from the blockchain
- Compete with Uniswap’s brand affinity and user loyalty
- Compete with Uniswap’s network effect (they have more liquidity and thus lower trading costs)

Like most non-blockchain tech companies, Uber can rely on its [proprietary technology](https://briefer.com/books/zero#:~:text=The%20first%20is%20proprietary%20technology.%20This%20means%20that%20your%20company%20owns%20a%20technology%2C%20that%27s%20difficult%20or%20even%20impossible%20to%20replicate.) and [user data](https://www.nfx.com/post/network-effects-manual#data-network-effects) to defend against competitors - in addition to its brand loyalty and network effects.

On the other hand, Uniswap’s network effect is its *only* advantage other than brand loyalty.

![Source: **[Aggregators in Web2 vs Web3](https://messari.io/report/aggregators-in-web2-vs-web3?utm_source=twitter_messaricrypto&utm_medium=organic_social&utm_campaign=aggregators_in_web3)**](https://cdn.sanity.io/images/2bt0j8lu/production/71bb7bb18e43ea7e5ebb5da8f7cbadf73c051a0e-1600x900.png?w=900&fit=max&auto=format&dpr=3)

Source: **[Aggregators in Web2 vs Web3](https://messari.io/report/aggregators-in-web2-vs-web3?utm_source=twitter_messaricrypto&utm_medium=organic_social&utm_campaign=aggregators_in_web3)**

The above Messari chart depicts this dynamic. Imagine you’re building a Web2 aggregator, you need to fight tooth and nail to get your competitors’ proprietary data. But a Web3 aggregator can read the publicly available data right from the blockchain.

It’s easier to start the Web3 aggregator, and it’s harder to profit, for this very reason - it’s easy for new competitors to come in after you. How much, and how long, your protocol can profit will largely be a function of its network effects.

>💡 Blockchain network effects are not necessarily *stronger* than in Web2 ([there is some evidence to the opposite](https://breadcrumb.vc/crypto-nfts-network-effects-in-web3-7689cf8f0439)), but because smart contracts and on-chain user data can be easily copied, network effects become a relatively more *important* part of defensibility.

Users familiar with the history of the 2020 DeFi Summer may recall the real-life launch story of a Uniswap competitor called SushiSwap. SushiSwap copied Uniswap’s open source software and attempted to counter Uniswap’s network effects with a “vampire attack”.

As we’ll cover more in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21), the launch of the SUSHI token, and Uniswap’s response with the launch of the UNI token, demonstrate how tokenomics plays a vital role in building and defending network effects.

To get a better sense of how tokens can help overcome this problem, consider the below chart of Filecoin’s network utility, split into 3 stages: building network capacity, scaling up, and reaching maturity/defensibility.

![Source: **[Filecoin Tokenomics Explained](https://academy.shrimpy.io/post/filecoin-tokenomics-explained)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5f27b61f-bcb0-442a-95e3-bd258aea2bd6/Untitled.png)

Source: **[Filecoin Tokenomics Explained](https://academy.shrimpy.io/post/filecoin-tokenomics-explained)**

As we’ve discussed, the problem is that at the left side of the chart, when Filecoin is first launching, network utility is effectively zero - there is no reason for new supply-side users or new demand-side users to join.

This above chart of Filecoin’s network utility is essentially the “traditional network effect” portion of the chart below. Tokens come in as the green line, smoothing out total network utility so that even when Filecoin first launches, there is a draw for users to adopt the network.

[Source*:* [The Web3 Playbook: Using Token Incentives to Bootstrap New Networks](https://twitter.com/cdixon/status/1444072365822857219?s=20&t=cBEs2jtFd6iTKpWOQvxofQ)](https://pbs.twimg.com/media/FApbdHkVUAITw7C?format=png&name=small)

Source*:* [The Web3 Playbook: Using Token Incentives to Bootstrap New Networks](https://twitter.com/cdixon/status/1444072365822857219?s=20&t=cBEs2jtFd6iTKpWOQvxofQ)

Conversely, launching a decentralized product without a token can make it very difficult to overcome the bootstrapping effect. For example, the decentralized messaging protocol Nostr, relies on people to run servers, called relays, to pass around the messages and content end-users send and create. Running a server has costs, meaning that supply-side users are incurring expenses even before there is a sufficient number of demand-side users willing to compensate relays in order to use the service.

https://twitter.com/matteopelleg/status/1675236495266045952?s=20

Unless Nostr can find a way to attract enough demand-side users to properly compensate for relays, it will have to rely on people running relays at a financial loss for purely altruistic reasons, which makes it hard to scale.

By design, Nostr is token agnostic - it is not a blockchain product itself, but it’s still encountering the same bootstrapping problem virtually all blockchain products face.

Had it taken a different approach, a token could have been one possible means for Nostr to subsidize relays and attract demand-side users. But this would only be a sustainable solution if those demand-side users are willing to pay relays to use Nostr and continue to use Nostr after the rewards end.

If your product can’t stand on its own, and users don’t use it for any reason other than earning token rewards, then such rewards will attract the wrong kind of users.

Network effects kick in once a product unlocks a *large enough value* to each user. That is correlated to, but not identical to, having a large number of users. Attracting **value add** users is important:

- An Uber driver who only provides rides when surge pricing hits 4x does not add as much value to Uber’s network as a driver who provides rides as their full-time job.
- Play-to-earn game Axie Infinity’s highly inflationary tokenomics helped amass millions of daily active players. But unlike the value-add players of games like WoW, EVE Online, CS:GO, or Dota 2, most Axie Infinity players weren’t playing the game for enjoyment. Token rewards accelerated the adoption curve by amassing a high number of profit-motivated “value-extracting” users. The result? A drop of [>50% in daily active players and a crash of >95% in the price of AXS](https://afkgaming.com/esports/news/axie-infinity-active-user-count-drops-to-below-1m-for-the-first-time-in-8-months) from their respective peaks.
- Maker DAO’s MKR tokenomics aligned MKR holders with the success and adoption of DAI, which helped amass a small but dedicated audience committed to being vocal and loyal users of DAI (the right kind of users), years before DAI itself was even launched.

- Despite building network capacity with FIL emissions, Filecoin has yet to find meaningful demand, with only 5%-10% of the network capacity being utilized. Additional demand-side users are relatively much more valuable to the network than additional supply - at least for the time being.

>⚠️ While tokenomics **can** help overcome the bootstrapping problem, when done poorly, such as handing out tokens to reward **any** network activity instead of rewarding value add activities, tokens can actually be net destructive to network value and growth. We’ll discuss more on this topic, the pros and cons of a token, and how to tell when a product may be ready to launch a token in [Chapter 1.4](https://www.notion.so/1-4-Does-Every-Project-Need-a-Token-79f30dc5e5d34fcca18b7fbcfff3792f?pvs=21).

For now, keep in mind that tokenomics can play a crucial role in building network effects, and if you want to maximize your chances to be resilient to competitors and succeed in the long run, maximizing network effects is key.

The right tokenomics can help you reach critical mass. The wrong tokenomics can lead to collapse.

# **Enabling User Ownership**

Traditional tech products begin their life cycles by creating value for users, in many cases even offering their services for free initially. Over time, however, they begin to monetize their service, extracting value from users of the product and distributing that value to private shareholders.

While this model has worked reasonably well for fueling the growth of our economy and technological progress, it does have its downsides:

- The interests of private shareholders do not always necessarily align with the interests of the users of the product itself. Users inherently get some utility from the product (otherwise they would not use it), whereas shareholders seek to extract monetary value from the product (otherwise they would not invest). When these two objectives are in conflict, both parties suffer, as well as the product itself.
- New products have to separately raise capital and then use that capital to fund acquiring users. This has been the [VC model for the past decade or more,](https://techcrunch.com/2018/10/31/social-capitals-chamath-palihapitiya-says-we-need-to-return-to-the-roots-of-venture-investing/) with investors like [Peter Thiel preaching to give money away for free](https://www.abilitygrowth.com/blog/what-i-learned-from-paypals-peter-thiel) to scale faster than the competition, and startups raising large amounts of VC capital to fund operating at a deficit for extended periods of time while acquiring users to reach the point of critical mass.

At the same time, the earliest users of products, who are often some of the most vocal advocates for the product, and responsible for its success and growth, do not benefit from the financial upsides (unless they invest in the company separately).

This is inefficient - raising money from VCs in exchange for ownership and spending that money on acquiring users. Why not ‘cut out the middleman’ so to speak, and give users ownership directly? This is not as radical as it might sound - even Web2 tech companies have already begun to explore doing so.

>💡 The ultimate promise of tokens is enabling distributed ownership: not shareholder owned, not employee owned, user owned.

Early AirBnB hosts were pivotal to the ultimate success and growth of the product - and hosts today continue to be. They would make for great owners of AirBnB, something AirBnB is well aware of. In fact, the company has previously asked the SEC [how they can give shares to hosts](https://www.cbsnews.com/news/airbnb-wants-to-give-shares-in-its-business-to-hosts) - current regulations only permit giving shares to employees and investors, not users. Thanks Gary.

As a new primitive of digital ownership, tokens enable new forms of community-owned networks, products, and organizations. In this context, **network users and contributors**, not third-party private shareholders, are the beneficiaries of the product’s monetization.

![Source: [Deep Dive on Decentralization](https://youtu.be/rW8GrxQYPbI?t=153)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3490a47-9983-4e8a-82c9-b8eeb263ade3/Screen_Shot_2022-07-25_at_2.49.40_PM.png)

Source: [Deep Dive on Decentralization](https://youtu.be/rW8GrxQYPbI?t=153)

Blockchain products (the orange line above) can have business models that are much more cooperative with their communities in the long run than traditional, privately owned businesses (blue line above).

In these traditional companies, the roles of users, owners, and company executives are distinct roles held by different people. The average user is virtually never also an owner or executive that has input into decision-making. By contrast, blockchain enables users to own, govern, and contribute to products and organizations in ways not otherwise feasible.

Regulatory hurdles impose a real-world constraint to “token-based ownership” that builders must respect. Due to a lack of regulatory clarity, almost all existing tokens are lossy approximations of user ownership, but their differences in tokenomics still matter. Some tokens are far better approximations of user ownership than others, while remaining to be compliant with the laws of their relevant jurisdictions. It all comes down to how the token has been designed, the specifics of their tokenomics.

Trent McConaghy, the founder of the [Ocean Protocol](https://oceanprotocol.com/), originally expressed how tokens enabled new forms of decentralized ownership in his “Web3 Sustainability Loop”.

![Source: [The Web3 Sustainability Loop](https://blog.oceanprotocol.com/the-web3-sustainability-loop-b2a4097a36e)](https://miro.medium.com/max/1400/1*43iAeAJGzWMbRIkgD7Av0A.png)

Source: [The Web3 Sustainability Loop](https://blog.oceanprotocol.com/the-web3-sustainability-loop-b2a4097a36e)

> **At its heart is a loop, designed for “snowball effect” growth of the ecosystem. The Workers (center) do *work* to help grow the Web3 Project Ecosystem (right). Apps and services generate revenue, using the Web3 project’s tools. A non-extractive fraction of that revenue is looped back (arrow looping from right to left) as Network revenue to the Web3 community.**
**Source: [The Web3 Sustainability Loop](https://blog.oceanprotocol.com/the-web3-sustainability-loop-b2a4097a36e)**
> 

Trent arguably too narrowly defined a few components, such as the “Workers” at the center of the network, as well as the “Buy & Burn” and “Governance Token” mechanisms, but the core concepts remain.

“Buy & Burn” can be extended to any value accrual mechanism. “Governance Token” is likewise probably a bit too restrictive, as even non-governance tokens such as LQTY can align incentives to grow the protocol’s adoption. And “Workers” can be extended to contributors in a general sense, including users. All users that participate in a network add value to that network. Every rider using Uber adds value to drivers, and every driver available adds value to riders.

This represents a fundamental evolution from Web2 tech products, which are typically privately owned “winner take all” cases, to user ownership where every user can share ownership of the winner.

> **One of the most important implications of the [Web3] loop is the possibility of winner-take-all ecosystems comprising winners-share-all participants.
Source: [Unbundling the unbundlers - The end of winner-takes-all](https://platforms.substack.com/p/unbundling-the-unbundlers-the-end?s=w)**

Just ask yourself - are you more likely to remain an engaged user of a product that simply starts charging you a fee one day, or one where you could own part of the success for being an early user and/or have a voice in steering the product in the direction you want to see?

The choice is obvious. That’s the importance of tokenomics.

>⚠️ Since ponzi schemes are always early user owned (early users literally own the cash flows from later users), some of the very best and very worst tokens have user ownership in common. Do not fall into the trap of designing a ponzi scheme in an attempt to optimize for user ownership.

While decentralized governance is not without its problems (from whale takeovers to low engagement, to the possibility of misaligned incentives), token based ownership is a strict necessity for truly decentralized use cases such as network states, DAOs, and user owned protocols.

# Chapter Summary

- Tokenomics is vital to blockchain builders because:
    - It’s one of the most powerful tools to direct user behaviors
    - It plays a crucial role in overcoming the “cold start problem” to reaching critical mass
    - It sustains community engagement
- Blockchain product users can not be explicitly forced to do something, or prevented from doing it - they must be incentivized to do it or avoid doing it
- Even the best products, concepts, or communities can be ruined by poor tokenomics that result in warped incentives - just look at [Steemit](https://arxiv.org/pdf/1904.07310.pdf), [Iron/Titan](https://www.cnbc.com/2021/06/24/why-titan-crypto-crash-that-burned-mark-cuban-may-not-signal-similar-bitcoin-plunge.html#:~:text=%E2%80%9CThe%20iron%20model%20was%20deeply%20flawed%20from%20a%20tokenomics%20perspective%2C%E2%80%9D%20said%20Mati%20Greenspan%2C%20portfolio%20manager%20and%20Quantum%20Economics%20founder) or [Luna/UST](https://twitter.com/FreddieRaynolds/status/1463394348326961153?s=20&t=H795L7JXL0rXclDz8YY2HA)
- Network effects are built by reaching a critical mass before competitors
- Not every blockchain product has strong network effects, and blockchain product network effects are not necessarily *stronger* than in Web2 ([there is some evidence to the opposite](https://breadcrumb.vc/crypto-nfts-network-effects-in-web3-7689cf8f0439)), but because smart contracts and on-chain user data can be easily copied, network effects become even more *important* to defensibility
- The ultimate promise of tokens is enabling distributed ownership: not shareholder owned, not employee owned, user owned

# Additional Resources

- Blog, [The Network Effects Bible](https://www.nfx.com/post/network-effects-bible)
- Blog, [The Dynamics of Network Effects](https://a16z.com/2018/12/13/network-effects-dynamics-in-practice/)
- Blog, [Two Powerful Mental Models: Network Effects and Critical Mass](https://a16z.com/2016/03/07/network-effects_critical-mass/)
- Blog, [Nine Reasons Why Tech Markets Are Winner-Take-All](https://www.london.edu/think/nine-reasons-why-tech-markets-are-winner-take-all)
- Slide Deck, [Web3 Builders Playbook](https://drive.google.com/file/d/1iq5MaMgwgiAU0nCxrv30D-s8wl5S59la/view?usp=sharing)
- Blog, [Protocols As Minimally Extractive Coordinators](https://www.placeholder.vc/blog/2019/10/6/protocols-as-minimally-extractive-coordinators)
- Book Summary, [‘Zero to One’](https://briefer.com/books/zero)
- Blog, [What is Cryptocurrency Game Theory: A Basic introduction](https://blockgeeks.com/guides/cryptocurrency-game-theory/)
- Paper, [Incentivized Blockchain-based Social Media Platforms: A Case Study of Steemit](https://arxiv.org/pdf/1904.07310.pdf)
- Twitter Spaces, [How to grow a DeFi protocol](https://twitter.com/Blockworks_/status/1671621347578105858?s=20)

# 1.2 What is Tokenomics?

Tokenomics can be a loaded term - it’s easier to answer what it *isn’t*, rather than what it is.

![download (2).png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e7e9f2ac-4416-47ac-bf21-c7c9da345f4d/download_(2).png)

Tokenomics is **not a** token’s…

- Max supply
- Pie chart with 10%-20% allocated to the team
- Emissions schedule
- Buyback and burns
- Whitepaper
- Staking yield
- Utility

These are all elements **related to a protocol's tokenomics, but tokenomics is a much more holistic concept. Here are two helpful definitions:

> “[Tokenomics] includes everything about the mechanics of how the asset works, as well as the psychological or behavioral forces that could affect its value long term.”
> 
> 
> Source: [Tokenomics 101](https://every.to/almanack/tokenomics-101)
> 

> Tokenomics is a term that captures a token’s economics. It describes the factors that impact a token’s use and value, including but not limited to the token’s creation and distribution, supply and demand, incentive mechanisms, and token burn schedules.
Source: [What Is Tokenomics and Why Does It Matter?](https://academy.binance.com/en/articles/what-is-tokenomics-and-why-does-it-matter)
> 

Often when founders, protocols, and white papers discuss tokenomics, they almost exclusively discuss **supply-side** aspects: max supply, emissions rate, allocation, vesting periods, etc.

Why? Because, unlike **demand**, every aspect of *supply* is entirely under the founding team’s control (at least until launch). But this lazy approach, focusing on only one aspect of tokenomics, leads to poor outcomes - no amount of supply manipulation can make a useless token into a useful one.

https://twitter.com/DermanCapital/status/1550261330740903936?s=20

# Holistic Tokenomics

In order to move beyond a narrow view of “supply side tokenomics”, let’s consider the entire context of a blockchain network.

Every network contains four components:

- **Ledger of transactions** and data (i.e. chain history)
- **Set of methods** to alter the data structure (i.e. transactions types and smart contracts)
- **Consensus protocol** to validate transaction legitimacy (i.e. PoW, PoS, etc)
- **Community of agents** participating in the network (i.e. users, validators, nodes, miners, etc)
    
    Source: [On Engineering Economic Systems](https://medium.com/block-science/on-engineering-economic-systems-1cff055d3a5f)
    

In this context, tokenomics are specifically designed rules and parameters by which the **set of methods** operate in order to incentivize the **community of agents** to reach **consensus** and perform other actions that will add new entries to the **ledger of transactions.**

Part of Bitcoin’s tokenomics is to reward a miner each time a block is mined. This block reward is called a [coinbase](https://www.javatpoint.com/coinbase-transaction), not to be confused with Coinbase with a capital ‘C’, the centralized exchange.

The coinbase (one method in our **set of methods**), follows rules and parameters set in Bitcoin’s emissions schedule to incentivize **agents** (miners) to secure the network and maintain **consensus** about the **ledger of transactions**.

Part of Curve’s tokenomics is to reward liquidity providers with pool fees. Each time an **agent** (trader) calls the ‘TokenExchange’ **method** to place a trade, it follows coded rules and parameters to charge a specific fee and allocate some portion of that fee to incentivize a different set of **agents** (liquidity providers) to provide liquidity, with all these actions settling to the **ledger of transactions.**

Tokenomics always involves some element of incentivizing an agent to take (or abstain from) a certain behavior. For this reason, tokenomics is perhaps best viewed as user behavior engineering.

<aside>
💡 **Tokenomics is the set of monetary and non-monetary (governance) rules a protocol employs to incentivize user coordination towards a specific goal, even when individual users hold uncorrelated or conflicting goals.**

</aside>

In this light, it’s clear tokenomics is about much more than supply policies. In fact, [some people disagree with using the term “tokenomics” itself](https://a16zcrypto.com/posts/article/beyond-tokenomics-tokenology/), purporting that the term is responsible for fixating on economic-related concepts like monetary policy (supply), and does not emphasize the holistic nature of the field strongly enough.

While I relate to these concerns, I think introducing yet another term is unlikely to be the best solution.

# Economics vs Tokenomics

Criticism of the term aside, the word tokenomics obviously comes from a combination of “token” and “economics”. But there are key differences between classic economics and tokenomics.

- To a policymaker (like a central bank), economics is the practice of optimizing for a goal, given scarce resources and the means by which those resources are produced, distributed, consumed, and traded. Common goals that policymakers optimize for include increasing total production (GDP), decreasing unemployment, or targeting a given rate of inflation.
- To blockchain protocols, tokenomics is the practice of designing digital resources (or digital representations of offline resources), and the means by which they are produced, distributed, consumed, and traded, given a desired goal. Common goals founders optimize for include maximizing network security/decentralization, increasing total network value, or maintaining a price target (for wrapped tokens, stablecoins, and tokenized assets).

<aside>
💡 In economics, policymakers optimize for an intended goal and inherit existing rules and constraints.

In tokenomics, protocols begin with an intended goal and design the rules and constraints to achieve that goal.

</aside>

**Economics**

*Given there is a finite amount of gold in the world, we can optimize for stable purchasing power by backing dollars with gold.*

**Tokenomics**

*Given we want a monetary supply that does not lose purchasing power, we can set the maximum supply to 21mm and make it costly to produce.*

While many concepts and approaches from classic economics carry over to tokenomics - not all of them do, especially within the context of gaming (see the section on Games & Play to Earn in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21) for more specifics if you are building a game).

# Start With Solving a Problem

As a blockchain builder, it’s important to remember that your token is not the same thing as your product - and, just like traditional products, you need to solve a real user problem.

No one uses Web2 products that don’t solve a problem.

No one remains a long-term user of a blockchain product that doesn’t solve a problem - nor will they use or hold that product’s token.

Below is an excerpt from a real conversation I had with an aspiring builder. Though it’s just one specific example, I can assure you it’s part of a common trend of similar conversations that happen much too often. All personally identifying details have been redacted.

> **Founder**: [I'm working on a] quiz dApp that let users answer questions. after answering a certain number of questions correctly they get rewarded with our fungible token. [we’ll] develop a dex where they will be able to swap the fungible token for other tokens that will be available in the dex

**Me:** So you’ll incentivize users to take quizzes and answer questions correctly by rewarding them with your token? What gives value to the token? Why will people want to earn it by taking quizzes? Why will other people want to buy it from the quiz takers who have earned it?

**Founder:** we are thinking of rewarding users with the token, then when they want to swap the token we take a fee from the swap

**Me**: Hmm. That doesn't make much sense imo. The purpose and value of the token has virtually nothing to do with the usage of the quiz platform. It seems like you might as well be building a DEX at that point.

**Founder:** so what's your advice on building the revenue and value?

**Me**: Well that’s the million-dollar question. Blockchain products are not fundamentally different than Web2 in the sense that you still need to build something people want to use badly enough that they are willing to pay to use it. And to do that requires solving a problem. It all comes back to the basics: a) what problem are you solving? b) who has this problem? c) how much (if anything) would they be willing to pay to solve this problem?

**Founder**: we didn't think of problems, we just thought it will be nice to bring education into the ecosystem
> 

This founder made the classic mistake of falling in love with the technology or solution, instead of a user’s problem. As a former technical founder myself, it’s a mistake I can relate to all too well - we’re engineers, and building new tech is fun.

And there is absolutely nothing wrong with releasing a piece of *software* that doesn’t explicitly solve a problem if you’re doing it as a learning project or an experiment.

But releasing a transferrable **token** (especially one designed to capture fees and incentivize user behavior) for a software product that does not solve a problem is **never** a good idea.

Why? Because even if you give 100% of the token supply away for free or do a “fair launch”, you may still be taking on legal and regulatory risks and will create a community that blames you personally if the token falls in price (yes, even if you give it away for free, as we’ll see in [Chapter 1.4](https://www.notion.so/1-4-Does-Every-Project-Need-a-Token-79f30dc5e5d34fcca18b7fbcfff3792f?pvs=21)).

And all for no or very limited benefit, because the product doesn’t solve a problem in the first place. The risk-reward to launching a main-net token purely as an experiment usually doesn’t make much sense.

You don’t want to end up like many play-to-earn games, riding a temporary boost from a token until it [inevitably crashes and users leave](https://restofworld.org/2022/axie-infinity-hack/), since they were only using the product to earn the token, and once the token is worthless, there’s no reason to stay.

https://twitter.com/Jason/status/1667581126393880578?s=20

Even Bitcoin itself had to solve a problem(s):

- Problem: the US dollar has lost more than 96% of its purchasing power since the creation of the Federal Reserve in 1913
- Problem: electronic money held in banks can be frozen, stolen, or seized if the government decides it doesn’t like what you’re saying or doing or if the bank collapses
- Problem: peer-to-peer and cross-border payments are slow, expensive, and entirely at the mercy of 3rd party for-profit corporations and government entities

Plenty of people disagree about whether Bitcoin is the **best** or **only** solution to these problems, but almost everyone agrees that Bitcoin is at least one option people have for these problems.

Coins and tokens, even Bitcoin itself, do not have value simply because they exist - they have value because they solve a problem.

# Product Before Token

Once you have a problem to solve, you still need an actual solution to that problem (i.e. a product).

Your token is generally **not** the same thing as your product:

- Your product is what you’re building to solve user problems.
- Your token is a digital representation of some resource or relationship within your product. It enables or improves a core feature of your product.

Obviously, some exceptions apply to this rule. If you’re building a centralized stablecoin like USDC (i.e. literally tokenizing US dollars sitting in a custodial bank account) your product is largely synonymous with your token. The token is the thing that lets those dollars be used on-chain.

Even with USDC though, there are aspects of the product that are not the on-chain token itself, such as how the actual fiat-USD which backs the token is secured, how redemptions work, what the reserves are composed of (checking account deposits, treasury bills, money market funds and more are all considered cash equivalents), and how reserves are audited.

Even in the case of tokenized assets, one could argue that the token is still not the product. And this is much more clearly the case in almost every situation besides tokenized assets:

- Uniswap vs UNI token

Uniswap existed as a protocol for nearly two years before launching the UNI token, proof that the UNI token doesn’t *need* to exist in order for traders and liquidity providers to get value from Uniswap’s product.

But UNI, despite some clear problems with its tokenomics around value capture and accrual, makes the product even better by increasing liquidity (resulting in lower slippage costs for users). UNI only launched when it did as a [response to SushiSwap’s vampire attack](https://twitter.com/markjeffrey/status/1306449680025358337) - the product was already solving user problems before the token came into being.
- Maker DAO vs MKR token

Maker DAO could have conceivably launched decentralized borrowing/lending without its MKR token by releasing smart contracts for using CDPs (collateralized debt positions) to mint DAI. No MKR token is required to publish a smart contract, post ETH collateral to a smart contract vault, or mint an ERC-20 token (DAI). MKR isn’t even strictly needed for decentralized governance of the protocol, in theory, ETH could be used for governance votes.

Strictly speaking, the core product, CDP vaults, does not **need** the MKR token to exist. That said, MKR makes Maker DAO’s decentralized CDP product much stronger by helping to [overcome bootstrapping challenges](https://www.reddit.com/r/MakerDAO/comments/5oyr28/maker_ico_and_polychain/), improving protocol resiliency (via [recapitalizing the protocol in extreme market events](https://cointelegraph.com/news/the-makerdao-auction-is-happening-heres-what-to-expect)), and increasing community engagement through ‘skin-in-the-game’ signaling, distributed ownership, governance involvement, and deflationary rewards.
- Chainlink vs LINK token

Chainlink uses LINK to reward oracles with fees for their services, and for oracles to post collateral that can be slashed, incentivizing them to be truthful. Yet a liquid stable coin like DAI, or even ETH itself, could conceivably fill the same role: oracles post DAI collateral, users of oracles pay fees in DAI, and oracles are rewarded with a share of those DAI user fees.

A decentralized oracle network using DAI or ETH instead of LINK would still be solving a user problem and be a valuable product. But LINK makes this product even stronger by reducing external dependencies (such as DAI de-pegging risk) and [simplifying pricing](https://www.reddit.com/r/Chainlink/comments/acqdmb/comment/edatc6z/).
- Ethereum Virtual Machine (EVM) vs ETH token

Decentralized computing has existed since at least 2000, with the launch of [Folding@home](https://en.wikipedia.org/wiki/Folding@home) for distributed protein folding. This predates Ethereum by nearly fifteen years. The Ethereum Virtual Machine *could* have been designed as a Folding@home style protocol without the ETH token.

Yet ETH allows for generalizing decentralized computing to more use cases by rewarding participants for validating, executing, and securing computations on the EVM that would otherwise be the target of profit motivated attacks.
- Bitcoin network vs BTC coin

The Bitcoin network is one of the largest, most decentralized networks in existence, responsible for securing the finality of BTC transactions and settlements. For years, people considered the Bitcoin network as only valuable due to processing settlement of BTC transactions, drawing little to no distinction between the Bitcoin network as a product and BTC as a coin itself.

But with the flurry of Ordinals and BRC-20 activity in 2023, as well as smart contract L2s for Bitcoin such as Stacks and sidechains such as RSK, more builders and users are beginning to see the Bitcoin network as a product that offers secure settlement finality for **any** use case, including but not limited to BTC transactions.

The point is **not** that UNI, MKR, LINK, or ETH tokens shouldn’t exist or that they don’t serve any purpose. The point is…

<aside>
💡 Solving a problem with a great product, or at least a great product *concept*, comes first, before the token and tokenomics, not the other way around.

</aside>

Too many builders think launching a token will solve all their problems, and then work backward from designing their token launch towards how their product must work, and what user problem it claims to solve.

This is akin to first setting a goal to raise VC funding, and then working backward to design a cool new technology product so you can raise money.

It **can** work, but it never gives you the best chance of success. It’s the wrong approach.

# Good Tokenomics are Not Sufficient

We’ll talk a lot more specifically about what makes tokenomics good or bad in the next chapter.

For now, remember that good tokenomics can make a good product great, and bad tokenomics can destroy even the best products.

Even so, you still want to worry first and foremost about solving a real problem with a good product, and **then** worry about getting your tokenomics right.

Why? Because emitting tokens can help acquire, retain, engage, and coordinate users - but only if users care about the token in the first place.

https://twitter.com/mrjasonchoi/status/1550463269009182721?s=20&t=frKVMgyMCsDd0DnzXURlZA

As Cobie so eloquently pointed out in his seminal blog post on staking rewards, at the end of the day earning more tokens is meaningless if there is no product behind it giving that token some economic, social, or utility value.

> “Simply paying users for not selling, payment received in the same asset that they are not selling, seems like pretty late-stage in the games of ponzi creation.”
- Cobie, [ApeCoin & the death of staking](https://cobie.substack.com/p/apecoin-and-the-death-of-staking)
> 

Curve’s often copied “vote escrowed” tokenomics mechanism, which we’ll discuss in later chapters, certainly helps with retaining existing users by keeping them actively engaged with the protocol and in competition with each other. But ultimately, CRV tokens are in demand in the first place because Curve has users that pay to use the product in order to solve a problem.

This is why you need to worry about problems and product first. You can’t just look at Curve’s tokenomics, and slap their vote escrow mechanism on a useless product and expect Curve’s rate of user growth.

Even if your product works well, tokenomics that work for Curve don’t necessarily work for every protocol, because Curve is not the same product as other protocols. Focus on the problem and product first, and then optimize for the tokenomics that work best for that specific product.

In nearly all cases, the product *could* exist without a token, but a token can not exist in the long run without a product.

# How Tokenomics Influences Your Product

While your token is not the same thing as your product, the tokenomics design you choose will heavily impact your product.

This is a double-edged sword. Good tokenomics can help growth, bad tokenomics can kill it - and tokenomics influence nearly every aspect of your product:

- Userbase
    - Adoption
    - Retention
    - Behavior & Engagement
- Risks
    - Exploits & Attack Vectors
    - Legal & Regulatory
- Financial Outcomes
    - Product Revenues
    - Token Holder Rewards
    

## Userbase

### Adoption

Token emissions are not a cash expense paid by a protocol, and thus not truly comparable to a “customer acquisition cost” (CAC). The reason for this is simple - the issuer of the tokens doesn’t have to pay an expense to emit these tokens.

If the tokens represent a share of ownership or rights to protocol revenues such as CRV or GMX, then token emissions are comparable to equity dilution, but are still not a cash or monetary expense in the same way PayPal gave new users $10 in cash or Deliveroo may give $5 off first orders. The latter two cases are both expenses that the company directly pays for from its cash balance.

https://twitter.com/aeyakovenko/status/1509668273339527186

Comparing token emissions to CAC then is admittedly flawed, but can still yield rough insights. In traditional companies, it’s well known that CAC can not exceed Customer Lifetime Value (CLV) indefinitely. If you pay $10 for each customer, but they only yield $6 profit, you’re losing $4 for each new customer you get, and will soon go bankrupt unless you increase CLV and/or decrease CAC.

In theory, a blockchain protocol can mint its tokens forever to fund CAC. In practice, doing so forever at rates much higher than actual use and demand for the token is not sustainable, because unless meaningful utility value and/or revenues are generated, the token will eventually become worthless. A worthless token makes it impossible in practical terms to continue paying for CAC in token form - we’re essentially describing an inflationary death spiral.

Comparing CAC to CLV is one common way to look at the health of a growing startup. We can make a similar comparison of protocol revenues vs token emissions to get a rough idea of how much organic usage a protocol has.

The more organic users that are paying to use the product, the more revenues compared to emissions we’d expect to see, on average. Conversely, low revenues compared to high emissions is one signal that the protocol may be unhealthy - that users are only there as “mercenary capital” to farm rewards, and will abandon the protocol as soon as emissions decline.

https://twitter.com/masonnystrom/status/1575152260950085632?s=20

Who you reward with tokens, and what you reward them for, are critical design choices that will influence how quickly users adopt your product, and which type of users adopt your product.

The industry norm for token emissions has evolved from ICO public sales, in which it was common that 100% of the token supply was released upfront in a single token generation event (TGE), to the modern standards of emissions for rewarding liquidity and other actions.

Builders need to think carefully about how to reward organic users instead of mercenary capital. One relatively simple yet effective tactic can be capping a maximum rate of rewards.

While protocols sometimes boast about 100% or greater reward rates, all else equal this represents high inflation, attracts the wrong type of user, and is overkill for attracting more organic users.

Users who like your product anyway would probably be just as happy to try the product with a 15% reward compared to a 100% reward, whereas users who only care about rewards, will only be drawn to the 100% reward.

Part of the challenge unique to blockchain is the difficulty in “first-time customer” offers or referral codes. In Web2, it is much simpler to identify individual users (by email, phone number, address, credit card, etc.) to prevent one user from creating multiple new accounts.

However for blockchain products, while exceptions apply, it is generally not possible to ensure one individual user is not controlling multiple wallet addresses (Sybil attack). If incentivized with extra rewards, users can and will create multiple addresses to pretend to be first-time users or to use their own referral codes.

<aside>
💡 New users need to be attracted by the same rewards available to existing users, and builders need to think carefully about which behaviors to reward and which types of users they are really attracting.

</aside>

### Retention

Arguably the most infamous example of user retention for a blockchain product was Uniswap’s launch of the UNI token. At the time, Uniswap’s liquidity providers were leaving the platform for SushiSwap, with platform TVL down by nearly 70%. SushiSwap’s TVL initially exceeded Uniswap’s, before seeming to begin to stabilize at an equal size to Uniswap’s.

https://pbs.twimg.com/media/EktHAyEXIAEXV7_?format=png&name=medium

The launch of the UNI token was able to immediately turn the tide back in Uniswap’s favor however, and it has [sustained a considerably larger user base and trade volume](https://dune.com/broderickbonelli/Uniswap-vs-Sushiswap) than SushiSwap for years.

This shouldn’t be taken by builders to mean that issuing a token automatically helps with user retention. Tokens that are highly inflationary relative to protocol growth, subject to death spirals, or have no legitimate utility value or demand, can not retain users for the long term, and make things worse.

For example, STEPN rewards users with tokens, but with [annual inflation rates of 31,000%](https://twitter.com/PhABCD/status/1528757519312625667?s=20), tokens with [dubious utility](https://twitter.com/m2e_chris/status/1556848124282519553?s=20), and [death-spiral tokenomics](https://twitter.com/jellulu_fish/status/1577479378522738688?s=20), STEPN saw an 80% decline in daily active users and a >99% crash in the price of its in-game GST token.

https://twitter.com/MessariCrypto/status/1567880627399131136?s=20

Issuing tokens is not an easy button for user retention. If supply and demand are not properly balanced, users will eventually leave, whether because the token price crashes due to hyperinflation, or because when emissions reduce there is no more good reason to stick around.

### Behavior & Engagement

We’ve already discussed how tokenomics is a powerful tool for directing behaviors.

Simple in concept, but obviously there’s a lot more complexity involved, and the same tokenomics used in different types of products can result in radically different outcomes.

First, consider AMM protocols like Uniswap or Curve. Both aim to reduce user slippage costs by increasing liquidity, and both incentivize liquidity by rewarding liquidity providers.

Simple enough. Maybe this tokenomics stuff isn’t so hard after all!

Before you run off and launch a token, there’s an important wrinkle to keep in mind: rewarding *low frequency* vs *high frequency* interactions:

**Low Frequency Interactions**

Behaviors like providing liquidity, adding TVL to a yield aggregator, or staking tokens in a validator node require a relatively **low frequency** of engagement.

Users have to manually initiate providing liquidity, but then their liquidity continues adding value to the system as long as they leave it there, no further actions are needed, until they manually choose to submit a transaction to withdraw.

The users do not need to remain actively engaged, yet the protocol still benefits the entire time from their **low-frequency** engagements.

**High Frequency Interactions**

What about user behaviors that require a **high frequency** of engagement, such as actively participating in governance votes, creating content, or actively curating lists? Suddenly, it becomes much more difficult to avoid side effects or exploits. Cautionary tales for failed **high frequency** engagement mechanisms abound:

- Posting and curating content, such as social media, is an example of a **high frequency** engagement. Steemit attempted to reward frequent engagement, and ensure quality by rewarding curation but ended up [incentivizing botting and high quantities of low quality content](https://arxiv.org/pdf/1904.07310.pdf).
- DAOs, even those as popular as Bankless DAO, consistently [struggle to meet the required minimum level of votes](https://forum.bankless.community/t/gse-and-quorum-the-daos-options-to-repair-governance-processes/2861) (quorum). Amusingly, the proposal adding a new quorum requirement to Bankless DAO itself did not reach quorum!

Ideally, DAO members do their research, make informed decisions, and actively participate in every proposal. Yet blindly rewarding the act of voting would simply incentivize low-quality proposal spam and uninformed voting in order to earn rewards.

How to better encourage **high frequency** participation in DAOs remains [an open question that enthusiasts are still experimenting with](https://twitter.com/thegrifft/status/1595110675244011521?s=20).
- Token Curated Registries (TCR), for example, an on-chain curated list of the “best restaurants in New York” is another concept that requires high levels of user engagement, but remains quite [difficult to properly incentivize](https://blog.coinfund.io/curate-this-token-curated-registries-that-dont-work-d76370b77150).
- Community engagement is another difficult area to reward. While reputation tokens can play a role, particularly in strongly knit communities where social signaling is highly valued, but in many cases, users don’t necessarily care about earning social clout (reputation) without at least the possibility of future monetary rewards. Many builders have assumed that if reputation tokens also have a monetary value (i.e. can be sold), then reputation becomes more valuable, improving community engagement. In practice though, when reputation itself can be purchased, this can [undermine the value of reputation and social signaling in the community](https://future.com/reputation-based-systems/), resulting in less cohesion and engagement.
- Play-to-earn games such as Axie Infinity want their players to remain loyal players, but rewarding in-game actions incentives activities that may harm the playing experience for legitimate players, such as [bots taking over the game](https://twitter.com/LevanKvirkvelia/status/1564290386138464256) and excessive inflation of in-game currencies. This can quickly spiral out of control because as more bots show up, the game experience becomes worse for players, leading to fewer players who might actually spend money on the game (in-game items, skins, extra lives, etc) whereas bots do not spend money, thus the fundamentals of the game’s economy further deteriorates.

It takes a bit more creativity, careful design, experimentation, and simulation to balance rewards and find the right incentives for **high frequency** engagement. Here are a few examples of mechanisms that, while not perfect, are a step in the right direction for **high frequency** engagements:

- Sam Williams, the founder of Arweave, mentions the example of a [scooter-sharing company in his lecture on mechanism design](https://youtu.be/gCFlGLbI_kE?t=493). Ideally, the scooter company wants users to return the scooters they use each day to their starting locations so that they are in the ideal areas for the morning commute. One mechanism for a decentralized approach would be to offer discounted, or even negative cost (ie pay users), rides that begin where most trips end, and end where most trips begin - thus redistributing scooters to where they are most needed.
- Curve’s “vote escrowed” mechanism introduces a time-based decay in voting power. Users that want to maximize their voting power need to consistently “renew” their voting power, which can translate into more consistent engagement overall - something most DAOs struggle with. It should be noted too though that even in Curve’s case, this mechanism resulted in an unforeseen side effect, with protocols like Convex aggregating locked CRV tokens and essentially tokenizing “maximum vote locked” CRV tokens as their own Convex tokens.
- Maker DAO incentives frequent governance engagement by aligning the economic interests of MKR holders with the success or failure of DAI’s collateralization and adoption. Even then, a [30% turnout rate represents a ‘high turnout’ vote for MKR](https://blockworks.co/news/makerdao-votes-against-a-more-streamlined-leadership) - there’s room for further improvement.

<aside>
💡 It’s relatively easier to design mechanisms for incentivizing behaviors that require a *low frequency* of engagement, such as providing liquidity or mining. It is much more difficult to design mechanisms that incentivize user behaviors that require a **high frequency** of engagement (such as) without creating potential exploits and abuses. Even then, all incentives come with tradeoffs, and it's important to think through and simulate the possible side effects beforehand.

</aside>

## Risks

### Exploits & Attack Vectors

No matter what you’re building, your tokenomics represent one of the most significant sources of risk to your product.

Don’t make the mistake of thinking that smart contract audits cover the risks that your product contains exploits or attack vectors.

> **In code security you look [at] how a smart contract does what it is supposed to do. Economic security is different, you are more interested in how a smart contract is interacting with other smart contracts.
- Tarun Chitra, [Understanding Code & Economic Security](https://verum.capital/codeeconomicsecurity/)**
> 

Many exploits have occurred not because of hacks or bugs - but because of poorly designed tokenomics. The code functioned exactly as it was designed to, but it was designed to do the wrong thing in the first place.

We’ve already discussed the case of Mango Markets, but it’s far for the only example. In fact, a similar [attack attempted by the very same exploiter nearly brought down Aave](https://twitter.com/ArkhamIntel/status/1595041038824923136?s=20) - making Aave’s design choices about risk controls and other aspects of economic security vital to the protocol’s survival.

This is part of the reason why DeFi protocols like Aave work with the rise of platforms like [Gauntlet](https://gauntlet.network/) and [Chaos Labs](https://chaoslabs.xyz/). Together these platforms provide economic risk simulations and optimizations to protocols including Aave, Maker, Compound, Chainlink, SushiSwap, Balancer, Uniswap, dYdX, Avalanche, and many more.

Meanwhile, in the Web3 gaming space, GUI-based simulation tool [Machinations offers a “Verified by Machinations Seal” auditing service](https://machinations.io/web3/) that verifies a "balanced, sustainable and unexploitable economy”.

https://twitter.com/omeragoldberg/status/1628041614084956160?s=20

Other large-scale collapses due to tokenomics vulnerabilities (not hacks or bugs) that we’ve already discussed include stablecoins like [UST](https://twitter.com/FreddieRaynolds/status/1526060401569550339?s=20), play-to-earn games like Axie Infinity or [STEPN](https://defivader.medium.com/why-stepns-collapse-is-inevitable-5259a6584a98), social media platforms like Steemit, and [potentially even Bitcoin itself](https://www.cs.princeton.edu/~arvindn/publications/mining_CCS.pdf) depending on who you ask (we’ll discuss at the debate over how Bitcoin can be secured once block rewards end in a later chapter).

As the ecosystem matures, economic security audits will soon be just as prevalent as smart contract audits. Tokenomics designs that introduce complexities such as multiple interdependent tokens, collateral, borrowing, oracles, explicit feedback mechanisms, and/or variable token emission rates are at an especially high risk of economic security exploits.

https://twitter.com/brianmcmichael/status/1626625784499650560?s=20

We’ll discuss tools, frameworks, and approaches for how to evaluate and quantify risks, as well as how to model and optimize your tokenomics, in Part Two of this guide ([2.6 Modeling & Optimization](https://www.notion.so/2-6-Modeling-Optimization-bcaab2f1ee2c4cceb6371ce29d3e1827?pvs=21)). For now, it’s important to recognize that such economic risk auditing is not something you can ignore as a builders, it’s already a well-established industry best practice, especially for novel, complex, or high-risk designs:

- In preparation for Ethereum’s transition to proof-of-stake, the Ethereum Robust Incentives Group and Ethereum ESP (Ecosystem Support Program) funded and conducted intensive [simulation modeling](https://github.com/CADLabs/ethereum-economic-model) of Ethereum’s proof-of-stake merge. This was in addition to extensive analysis and review of the [economic incentive model for proof-of-stake](https://drive.google.com/file/d/1pwt-EdnjhDLc_Mi2ydHus0_Cm14rs1Aq/view), and similar auditing work has been conducted to analyze key improvement proposals such as [EIP-1159](https://arxiv.org/pdf/2012.00854.pdf).
- When Stacks, a smart contact L2 for Bitcoin, launched their novel consensus mechanism to secure the chain to Bitcoin, they engaged firms such as the [Prysm Group](https://www.prysmgroup.io/) for an economic model audit to stress test the incentives mechanisms and assumptions inherent in the design.
- Status, one of the earliest projects in the Ethereum ecosystem, collaborated with BlockScience to model, simulate, and test [economics models for decentralized file storage](https://github.com/status-im/storage-econ-model/tree/master) in order to research launching such a product.
- Liquity, developers of the LUSD stablecoin, conducted and [published extensive economic modeling and simulation](https://docs.liquity.org/documentation/resources) before launch, including a summary of financial modeling analysis by an independent third party.
- ALEX, a DeFi protocol, published the concept of a [Collateral Rebalancing Pool](https://docs.alexgo.io/whitepaper/dive-into-collateral-rebalancing-pool) (CDP) to enable borrowing without risk of margin calls, complete with Monte Carlo simulation results. This concept is very similar to the one Curve introduced a year later, called [Lending-Liquidating AMM Algorithm](https://github.com/curvefi/curve-stablecoin/blob/master/doc/curve-stablecoin.pdf) (LLAMMA).

Just as smart contract risk can be minimized but never fully eliminated, the risk of economic vulnerabilities can never be fully eliminated. But given that your tokenomics is just as large a source of exploit risk as your smart contracts code, builders need to follow industry best practices to minimize risks.

Not publishing any modeling results or findings before launching a token is a tell-tale sign of an amateur project that is putting its users and token holders at needless risk.

Feeling overwhelmed? Good. Launching a token is not something to be taken lightly. But don’t worry. If launching a token is right for your particular situation, Part Two of this guide covers a step-by-step process builders can follow to optimize their tokenomics and maximize economic security.

<aside>
💡 Poorly designed tokenomics create economic risks that smart contracts audits are not designed to catch - they are not errors in code, but errors in incentive structures that can result in everything from a poor user experience (e.g. spam on Steemit) to total protocol collapse (e.g. Terra, Iron Finance, Mango Markets).

</aside>

### Legal & Regulatory

Perhaps the biggest source of risk of all for blockchain builders and protocols is regulatory risk. 

And tokenomics is arguably the single most important factor when it comes to the degree of regulatory risk you are exposed to.

Regardless of your personal opinions about the SEC, CFTC, IRS, IMF, or any other regulatory bodies, builders need to take regulations seriously as a matter of cold, hard pragmatism.

For example, no matter your personal view on XRP as a token, the fact remains that elements of its tokenomics, such as its emissions and issuance, drew the attention of the SEC, resulting in their [action against Ripple](https://www.sec.gov/news/press-release/2020-338), and XRP’s [loss of trading status on many centralized exchanges as a result](https://markets.businessinsider.com/currencies/news/xrp-delisted-ripple-sec-complaint-coinbase-crypto-okcoin-trading-platform-2020-12-1029926814).

More recent actions by the SEC against [LBRY](https://www.coindesk.com/policy/2022/11/07/lbry-sold-tokens-as-securities-federal-judge-rules/), [Kraken](https://www.coindesk.com/policy/2023/02/09/us-securities-and-exchange-commission-sues-kraken-over-crypto-staking-services/), Coinbase, and others it argues [made unregistered securities offerings](https://decrypt.co/105693/sec-coinbase-lists-nine-crypto-tokens-securities), plus the [arrest of a developer guilty of nothing but contributing to Tornado Cash’s open source code](https://www.coindesk.com/layer2/2022/08/12/an-alleged-tornado-cash-developer-was-arrested-are-you-next/) demonstrate that XRP was not a one-time event.

Unfortunately, whether the SEC is in the right or the wrong largely doesn’t matter. Unless you’re willing to spend years of your life and millions of dollars in court cases against the SEC, you need to take these recent events seriously.

https://twitter.com/LBRYcom/status/1620467454391771144?s=20

https://twitter.com/LBRYcom/status/1622997686898106368?s=20

[T](https://home.treasury.gov/news/press-releases/jy0916)he subsequent [censorship of addresses associated with Tornado Cash transactions](https://tokenist.com/tornado-cashs-usdc-frozen-as-stablecoin-censorship-fears-grow/), questions remain about whether [regulators can effectively censor transactions on the Ethereum network](https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored/) (the latest percent of OFAC compliant validators is [tracked here](https://www.mevwatch.info/)), or even if the [SEC will deem Ethereum itself to be a security](https://www.forbes.com/sites/mariagraciasantillanalinares/2022/06/27/sec-chairman-gary-gensler-implies-that-ether-is-a-security-and-falls-under-his-jurisdiction/?sh=7f39996d7775), despite Gary Gensler’s repeated personal comments ([here](https://youtube.com/shorts/9wf0uanzHEE) and [here](https://www.youtube.com/watch?v=ZPy9QbY6D9w)) prior to becoming SEC chair that Ethereum is not a security.

To date, while chair of SEC, Gary Gensler has only definitively stated that [one cryptocurrency is not a security - Bitcoin](https://www.coindesk.com/layer2/2022/06/28/secs-gensler-reiterates-bitcoin-alone-is-a-commodity-is-he-right/) (despite his own comments before serving as chair that least three others are not securities).

While possible to reduce doubt by “playing ball”, doing so is costly and time-consuming, and the benefits of doing so are still unknown. Only a handful of tokens have actually gone through the process of registering sales with the SEC:

- Stacks, a smart contract L2 for Bitcoin, [registered its ICO as a securities offering with the SEC](https://decrypt.co/9076/blockstack-nets-23-million-historic-sec-qualified-token-sale-ico)
- INX, a trading platform, became the [“first SEC registered token IPO”](https://news.bitcoin.com/inx-becomes-the-first-sec-registered-ipo-to-accept-crypto/)
- Note that a number of coins have raised via Reg-D offerings (almost all VC token sales are by this route) - but these type offerings mostly exclude non-accredited investors and are explicitly **exempt** from needing to register with the SEC

Modern builders must recognize that the market has changed drastically since just a few years ago. Just because a protocol used a certain tokenomics design before, and has not yet been sued, does **not** mean that design is free of legal or regulatory risks.

For example, just because Curve pays revenues to token holders, and Binance does buybacks and burns, does not mean you can do so without any risk.

[Chapter 2.7 Legal Opinion](https://www.notion.so/2-7-Legal-Opinion-Structure-94f04489ede3424fbc66e358fa5f317c?pvs=21) of this guide covers some **potential** best practices for legal concerns for informational and educational purposes only - builders should take these risks seriously and **always** consult a legal professional before launching a token.

<aside>
💡 Regulation is only becoming *more* important, not less, to blockchain builders. Not taking regulation seriously can be a death blow to your protocol, waste years of life, drain millions of your dollars, and possibly send you to prison. Tokenomics aspects like emissions, value accrual, and utility all play a big role in the degree of legal risk protocols take on.

</aside>

## Financial Outcomes

*This section on financial outcomes covers the financial and economic implications your tokenomics have on your protocol and token holders. This section does not assert anything regarding the legal or regulatory viability of any of the token value accrual mechanisms mentioned. As a reminder, none of the contents in this guide represent legal advice. Always consult a legal professional before launching a token.*

### Product Revenues

For the vast majority of blockchain products and protocols, success is ultimately defined in terms of revenues. Metrics like users, TVL, and trade volume are proxies for revenue. And high growth rates in these proxies are considered favorable because they indicate the possibility of **future** revenues, not because they are end goals themselves.

Remember that solving a problem with a good product always comes first and foremost - if no one will pay to use your product, then your revenues will always be zero, no matter your tokenomics.

That said, if we compare two otherwise equivalent products, tokenomics become the most important determinant of your blockchain product’s revenues because they directly impact user adoption, usage, and retention.

Note that your product **creating** value for users and your product **capturing** value as revenue are two different things.

Uniswap has created quite a lot of value for its users - it enables liquidity providers to earn trading fees, and traders to make trades at lower costs and without relying on a custodial, centralized exchange. That’s very valuable to both liquidity providers and traders alike - it’s value the Uniswap product has **created** for users.

However, to date, Uniswap itself has not *captured* any of the value it has created. Uniswap does not collect any fees from users of its service.

To help make this distinction between **created** value and **captured** value more concrete, let’s consider an example:

> Imagine you have $1,000 USDC and want to buy Ethereum. For simplicity, imagine making the trade on a centralized exchange would be free, but you don’t want the additional custodial risks, signup process, withdraw delays, and KYC burdens of a centralized exchange. Imagine you’re willing to pay $10 in fees to avoid all these hassles.

By offering you a liquid, decentralized exchange, Uniswap has **created** $10 of value for you, since how much you value all the benefits of a DEX over a CEX.

If the Uniswap treasury charges you $3 to make the trade, then using Uniswap is still a net positive value to you of $7.

$10 of value is **created**, you keep $7 of that value, and Uniswap’s treasury **captures** $3 of value.

In reality, Uniswap does not currently collect any fees, so even though it **creates** value, Uniswap itself **captures** no value.
> 

Savvy reads will note that the fact that the Uniswap protocol does not **capture** value is a problem - but the *protocol* not earning any revenue is a separate topic from the UNI **token** itself not accruing any value - we’ll discuss that in the next section.

Now that Uniswap is trying to turn on fees, they’re facing more pushback than if perhaps they had been collecting a fee to begin with. (Curve also technically launched with no fees, but turned on fees less than a month after launching, whereas Uniswap waited several years).

https://twitter.com/mhonkasalo/status/1552994507838349313?s=20&t=bDpjYZ5oxZ5blaAgTwA1AA

As a builder, you need to keep both value **creation** and value **capture** in mind - and the regulatory concerns that might come with certain value capture approaches.

A short, promotional period of no fees is one thing (Curve), but sustained periods of no fees that get users accustomed to zero fees may mean it’s harder to turn a fee on after the fact than to have one on the begin with. As such, it may be wise to find a legally compliant way for your protocol to **capture** value as soon as possible.

<aside>
💡 Just because your product *creates* value does not necessarily mean it *captures* any of that value - it depends on your business model and tokenomics.

</aside>

### Token Holder Rewards

Once your product has *created* value, and *captured* a portion of that created value, your tokenomics become even more relevant. How the value captured by your protocol benefits token holders is entirely determined by your tokenomics.

Given our discussion of Uniswap above, you may already be asking yourself “if the Uniswap product does not **capture** any value (does not earn any revenue) why does the UNI token itself have any value?”

All current UNI holders are relying on the possibility that Uniswap will eventually start **capturing** value, and that this [value will **accrue** to the token via mechanisms as future cash flows](https://gov.uniswap.org/t/uniswap-objective-function/21005), such as revenue distributions or buybacks.

While it may be beneficial to have value **capture** from day one to avoid Uniswap’s problem of facing user pushback to later turning fees on, value **accrual** to your token does not necessarily need to happen immediately.

For example, even though Curve **captured** fees extremely shortly after launching, those fees were simply held by the protocol - the token did not **accrue** this value via any direct means (other than the promise of a governance vote approving access to those funds). It wasn’t until about a year after creating and capturing value that Curve began [distributing protocol revenues to token holders](https://www.coindesk.com/markets/2020/09/19/stablecoin-dex-curve-will-kick-off-a-dividend-on-its-crv-token-today/), thus directly accruing value to the token.

Every builder and protocol faces a paradox when it comes to value accrual. Optimizing for token price (so called ”number go up”) at the expense of security, utility, and long-term sustainability ironically makes your protocol more volatile and susceptible to crashes and exploits.

At the same time, the unfortunate reality is that token price is the simplest and most transparent vanity metric by which people will judge your entire product. The best protocols find a balance by optimizing for tokenomics that minimizes volatility and provides sustainable means to attract, retain, and incentivize users.

https://twitter.com/Flynnjamm/status/1310268817138884608?s=20

But until the market further matures, projects with ponzi scheme tokenomics (ponzinomics) that optimize for short-term pump-and-dumps will still occasionally make headlines - especially on the way back down as they collapse. Stronger industry standards for tokenomics best practices among builders like yourselves can play a big role in reducing the harm these scam projects cause to the industry.

<aside>
💡 Once you have a product that **creates** user value, it may be beneficial to **capture** value as early as possible - even if that value does not **accrue** to the token. This may avoid the problems Uniswap is facing trying to add fees later on. Curve **captured** value starting early on, but the token didn’t **accrue** any of that value until a year later. Today, Curve and CRV token holders earn protocol revenues, while UNI token holders still don’t…

</aside>

# Chapter Summary

- Tokenomics is the set of economic and non-economic (governance) rules a protocol employs to incentivize user coordination towards a specific goal, even when individual users hold uncorrelated or conflicting goals
- While many of the concepts and approaches from traditional economics carry over to tokenomics - not all of them do, especially within the context of gaming (discussed further in the  [Games & Play to Earn in Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21))
- Your tokenomics is not the same thing as your product. In nearly all cases, the product *could* exist without the token, but the token can not exist (sustainably) without the product
- Great products, or great product concepts at the very least, come first, before the token and tokenomics, not the other way around. In the cases of Uniswap, Maker DAO and Chainlink, their tokenomics make an already good product even stronger
- Enabling user ownership is an extremely powerful advantage of Web3 models for user retention - one that [Web2 companies are trying to emulate](https://finance.yahoo.com/news/ouch-airbnb-hosts-missed-email-193020536.html)
- It’s relatively easier to design mechanisms for incentivizing behaviors that require a *low frequency* of engagement, such as providing liquidity or mining. It is much more difficult to design mechanisms that incentivize user behaviors that require a **high frequency** of engagement (such as) without creating potential exploits and abuses. Even then, all incentives come with tradeoffs, and it’s important to think through and simulate the potential side effects beforehand.
- Poorly designed tokenomics create economic risks that smart contracts audits are not designed to catch - they are not errors in code, but errors in incentive structures that can result in everything from poor user experience (ex. Solana’s downtime or Steemit’s spam content) to total protocol collapse (ex. Terra, Iron Finance, Mango).
- Regulation is only becoming *more* important, not less, to blockchain builders, with the [SEC clamping down on Coinbase](https://www.sec.gov/news/press-release/2022-127) and by extension accusing at least [9 tokens of making unregistered securities offerings](https://decrypt.co/105693/sec-coinbase-lists-nine-crypto-tokens-securities), as well as the recent [sanctioning of specific Tornado Cash](https://home.treasury.gov/news/press-releases/jy0916) (a currency mixing service), the subsequent [censorship of addresses associated with Tornado Cash transactions](https://tokenist.com/tornado-cashs-usdc-frozen-as-stablecoin-censorship-fears-grow/), and even the [arrest of a developer in the Netherlands who contributed to Tornado Cash’s open source code](https://www.coindesk.com/layer2/2022/08/12/an-alleged-tornado-cash-developer-was-arrested-are-you-next/).
- Just because your product *creates* value does not necessarily mean it *captures* any of that value - it depends on your business model and tokenomics
- It’s possible to *capture* value (product/protocol revenues) without any of that value *accruing* to the token or token holders. For example, for the first year, Curve captured protocol revenues but did not direct revenues to token holders in any way

# Additional Resources

- Blog, [Understanding Token Economics (Tokenomics 101)](https://anatha.io/blog/understanding-token-economics-tokenomics-101)
- Article, [What is Tokenomics and Why is it Important?](https://www.coindesk.com/learn/what-is-tokenomics-and-why-is-it-important/)
- Paper, [Mechanism Design and Blockchains](https://arxiv.org/pdf/2005.02390.pdf)
- YouTube, [Demand Side Tokenomics](https://www.youtube.com/watch?v=I_4QbbZJjsA)
- Article, [To Infinity and Back: Inside Axie’s Disastrous Year](https://restofworld.org/2022/axie-infinity-hack/)
- Blog, [Token-Curated Registries 1.0](https://medium.com/@ilovebagels/token-curated-registries-1-0-61a232f8dac7](https://medium.com/@ilovebagels/token-curated-registries-1-0-61a232f8dac7)
- Blog, [TCR Design Flaws: Why Blockchain Needs Reputation](https://blog.relevant.community/tcr-design-flaws-why-blockchain-needs-reputation-c5771d97b210)
- Blog, [Subjective vs. Objective TCRs](https://medium.com/coinmonks/subjective-vs-objective-tcrs-a21f5d848553)
- Blog, [DAO Voting Mechanisms Explained](https://limechain.tech/blog/dao-voting-mechanisms-explained-2022-guide/)
- Blog, [What is the Difference Between Creating and Capturing Value?](http://theventurecfo.com/blog/2015/01/23/what-is-the-difference-between-creating-and-capturing-value)
- Blog, [Tokens are Products](https://variant.fund/articles/tokens-are-products/) (a good article, though the title is misleading)
- Blog, [ETH is Not Ultrasound Money](https://joncharbonneau.substack.com/p/eth-is-not-ultrasound-money-part)

# 1.3 The Good, The Bad, and The Ugly

As discussed so far, tokens help with directing user behaviors, bootstrapping network effects, and enabling user ownership - but they do not replace the need for a solid product that solves a real user problem.

- A good product does not automatically mean any tokenomics you pick will work. Bad tokenomics will kill even the best products or concepts.
*Good Product + Bad Tokenomics = Bad Outcome
(ex. STEEM or UST)*
- Good tokenomics will not save a bad product if no one wants to use it.
*Bad Product + Good Tokenomics = Bad Outcome
(ex. Buggy, low liquidity CEX that copies BNB’s tokenomics)*
- And both a bad product and bad tokenomics is (not surprisingly) bad.
*Bad Product + Bad Tokenomics = Bad Outcome
(ex. Celcius’ CEL token)*
- You need good tokenomics and a good product.
Good Product + Good Tokenomics = Game Changes
*(ex. BTC, ETH, LQTY, GMX, MKR, CRV - note this is not an endorsement or recommendation to buy or invest in any of these tokens or their associated protocols)*

# Good vs Bad: Web3 Uber Tokenomics Examples

Imagine a fictional Web3 competitor to Uber with a native token, UBR. Imagine the product itself is functioning well and already has riders and drivers using it.

Let’s consider a couple of possible tokenomics designs for this fictional UBR token by using a simplified version of the **Incentives Mechanism Framework** from the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21). We’ll cover the full canvas step by step in Part Two of this guide.

**UBR Tokenomics - Alternative A**

**Simplified version of Incentives Mechanism Framework from the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)**

| (A) Role | (B) Desired Behaviors | (C) Frictions to Desired Behaviors | (F) Incentive Mechanisms |
| --- | --- | --- | --- |
| Riders | Book rides | Costs money, faster or cheaper alternatives | To make rides cheaper: riders earn 10% of their spending as “ride-to-earn” UBR rewards. |
| Drivers | Provide rides | Providing rides requires time and money | To make drivers more likely to offer rides, drivers get paid by riders in UBR, and earn 10% extra “drive-to-earn” UBR rewards. |

What is likely to happen with Alternative A UBR tokenomics?

As riders book rides and drivers provide rides, the circulating supply of UBR will dramatically increase. Some drivers may even create bots or multiple fake rider wallets to book fake rides with themselves to earn the “ride-to-earn” and “drive-to-earn” UBR rewards.

At least some drivers will begin selling the UBR they earn for USD since they need to pay their bills for gas and car insurance in USD, not in UBR.

As drivers sell UBR and the supply continues to increase, the value of the UBR token comes under pressure - creating a death spiral. The more the UBR price declines, the more UBR tokens drivers have to sell in order to pay the same USD bill. This feedback loop leads to the UBR token price collapsing.

No drivers want to be reimbursed in UBR anymore, since it’s worthless, and with no available drivers, there is no value for riders to use the product.

The product dies.

Now let’s look at the same exact product, but with the tokenomics below, in Alternative B.

**UBR Tokenomics - Alternative B**

**Simplified version of Incentives Mechanism Framework from the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)**

| (A) Role | (B) Desired Behaviors | (C) Frictions to Desired Behaviors | (F) Incentive Mechanisms |
| --- | --- | --- | --- |
| Riders | Book rides | Costs money, faster or cheaper alternatives | Riders can pay drivers in DAI (stablecoin) or get a discount if paying in UBR tokens. In either case, the protocol’s fee (X% of payment, where X% is less than Web2 Uber’s fee) must be paid in UBR tokens. The protocol’s fee is burned each transaction. |
| Drivers | Provide rides | Providing rides requires time and money | Give driver’s a bigger cut of rider’s payment (i.e. UBR protocol fee is < Web2 Uber’s fee), drivers can keep even bigger cut by locking up UBR. |

What is likely to happen with this tokenomics design?

While not all riders will pay in UBR, some will. As they pay for rides in UBR in order to get a discount, some UBR tokens are burned, reducing the total and circulating supply of UBR.

While not all drivers will lock up UBR to pay a lower protocol fee, some will. As they lock UBR, the total circulating supply of UBR further decreases.
If we assume that the value of a given ride stays constant in USD, i.e. it always costs $20 to drive from Point A to Point B, as platform usage grows, the number of total and circulating UBR tokens decreases, and all else equal the value of each UBR token increases in USD terms.

As UBR appreciates, it draws more attention from both drivers and riders, causing more usage…

<aside>
💡 Comparing Alternative A to Alternative B, we see that otherwise *identical* products can have drastically different outcomes based on the tokenomics decisions they make.

</aside>

# The Good: “Win-Win-Win”

Good tokenomics meet three key criteria:

- Reward contributors
- Improve the product
- Benefit holders

In other words, good tokenomics are “win-win-win”.

## Reward Contributors

Rewarding project contributors helps the network further develop and aligns incentives with users.

Everything in moderation as they say - more rewards for contributors is not always best, and there are limits to contributor rewards beyond which they cease being healthy for the protocol.

<aside>
💡 While it’s obvious too much supply going to contributors can be detrimental, a so-called “fair launch” where contributors get too *little* of the supply, can be just as bad.

</aside>

Yearn Finance (YFI) is a project largely responsible for starting the modern definition on “fair launches”, with zero pre-mine, zero investor allocation, zero pre-sale, and zero team allocation.

Bitcoin did this first of course, but the term “fair launch” was not really used to describe Bitcoin until other tokens came along, creating an “unfair” vs “fair” distinction. YFI was one of the first high profile tokens to demonstrate that other tokens, not just Bitcoin, could have a “fair launch”.

Yearn Finance’s creator, Andre Cronje, said at the time:

> …**we have released YFI, a completely valueless 0 supply token. We reiterate, it has 0 financial value. There is no pre-mine, there is no sale, no you cannot buy it, no, it won’t be on Uniswap, no, there won’t be an auction. We don’t have any of it… And just because we feel we didn’t stress it enough, 0 value. Don’t buy it. Earn it.
- Andre Cronje,** [Why YFI Are Not Investment Contracts](https://lexnode.substack.com/p/why-yfi-are-not-investment-contracts#:~:text=we%20have%20released%20YFI%2C%20a%20completely%20valueless%200%20supply%20token.%20We%20reiterate%2C%20it%20has%200%20financial%20value.%20There%20is%20no%20pre%2Dmine%2C%20there%20is%20no%20sale%2C%20no%20you%20cannot%20buy%20it%2C%20no%2C%20it%20won%E2%80%99t%20be%20on%20uniswap%2C%20no%2C%20there%20won%E2%80%99t%20be%20an%20auction.%20We%20don%E2%80%99t%20have%20any%20of%20it)
> 

Even as “fair launches” go, this is about as fair as you can get. Yet Andre came to regret this “fair launch” decision:

> **When I decided to distribute YFI 100% [for free] it was because I believed it would allow me to exit to the community. However, I am still blamed if the price goes down, I am still constantly plagued by “when next release”, “when update”, etc messages. I still have all the responsibility and expectations, except I have 0 of the reward or upside. Don’t do this, I was an idiot.
- Andre Cronje,** [Building in defi sucks (part 2)](https://andrecronje.medium.com/building-in-defi-sucks-part-2-75df9ee7871b)
> 

In [Chapter 2.5 Supply Policy](https://www.notion.so/2-5-Supply-Policy-ff3f8ab217b143278c3e8fd0c03ac137?pvs=21), we’ll dig into specifics for industry standards for supply allocated to the team, vesting, etc. Those details are “simple” since they’re just parameters.

The more important thing to keep in mind is that rewarding contributors is a key piece of win-win-win tokenomics because it aligns the success of contributors with the success of users and the protocol itself.

Tokens that **only** exist to reward contributors and early insiders (ponzinomics), do not maximize long-term protocol success, as they’re missing the other core elements of win-win-win tokenomics.

## Improve the Product

Good tokenomics also improve the product by making it better, faster, cheaper, or more accessible:

- UNI, CRV, GMX - more liquidity, lower slippage
- MKR, LQTY  - more community engagement and adoption
- LINK, RPL - more stability and simplicity

As discussed in the previous chapter, one could reasonably argue that none of these tokens strictly **need** to exist - but they each improve their respective products.

<aside>
💡 How the token improves the product is a key distinction between good tokenomics and bad tokenomics. When the token does not make the product better in a clear way (other than raising money), it’s a strong sign that the token has not been well designed.

</aside>

As a builder, it can be helpful to first ask yourself, “how would this product work without a token.” If there are no tradeoffs or sacrifices to the product that you’d have to make to remove the token, that’s a good sign launching a token may not be the right choice (we’ll look at a framework for making this decision in the next chapter).

Conversely, the presence of a token should unlock, enable, or coordinate a benefit that would not otherwise arise.

> **A good design should solve collective action problems, organizing and incentivizing its participants to provide services collectively that could not be generated from individual behavior… Consider the simple example of staking. Without a reward system, no participant would want to secure the network… But with a reward system (typically emissions or fees paid to "stakers"), that decision-making changes. Participants stake for reasons that are *individually rational*, but — in the aggregate — they provide benefits that are enjoyed by all.
Source:** [Token Design for Serious People](https://jumpcrypto.com/token-design-for-serious-people/)
> 

While it’s possible to have at least some form of distributed computing without a token, Ethereum’s tokenomics improve the core distributed computing product, capable of extending the EVM to use cases for economic contracts that could not otherwise be processed in a secure manner.

Similarly, the tokenomics of decentralized governance communities such as Maker DAO and Curve improve their respective products by increasing community engagement and incentives alignment.

Tokens in each of these cases improve the product. While the product generally **can** exist without a token, it is a stronger product because the token exists.

## Benefit Holders

The final criterion for win-win-win tokenomics is that tokens must also benefit holders - the token can’t simply extract value from holders as a fundraising mechanism (ponzinomics). The benefit to holders does not necessarily need to be monetary though, it can be utility benefit or social benefit as well.

It’s common for builders to assume that if their product or token gets enough usage, token holders will automatically benefit. In reality, this simply isn’t the case.

<aside>
⚠️ Teams naively assume their token will automatically act as a store of value or a medium of exchange, and appreciate in value just because their product gains users. This is a telltale sign of an amateur team.

</aside>

When speaking to builders who make this mistake, it seems to be due to the fact that they naively assume their token will inherently be valuable as a store of value or medium of exchange, simply by virtue of its existence.

Oftentimes their reasoning is along the lines of: “Well Bitcoin is a store of value, isn’t it? So our token will be too.”

> **Bitcoin confused people. It made some believe that a functional cryptocurrency will be valuable just by virtue of being out there… The Bitcoin example is a really bad model for others. It induces the perception that all you need to do is create a currency and people will do the rest… It is not to be matched by copycats.
Source: Alex Bulkin, [Cryptoeconomics Is Hard](https://blog.coinfund.io/cryptoeconomics-is-hard-ad401b2428b9)**
> 

This is problematic because they design tokenomics models that **rely** on these assumptions.

But both assumptions (medium-of-exchange and store-of-value) are virtually always wrong.

> **What this all serves to show is that relying purely on the medium-of-exchange argument to support a token value, while attractive because of its seeming ability to print money out of thin air, is ultimately quite brittle. Protocol tokens using this model may well be sustained for some time due to irrationality and temporary equilibria where the implicit cost of holding the token is zero, but it is a kind of model which always has an unavoidable risk of collapsing at any time.
Source: Vitalik Buterin, [On Medium-of-Exchange Token Valuations](https://vitalik.ca/general/2017/10/17/moe.html)**
> 

> **[Becoming a store of value] is by far the most difficult to achieve as it’s not a function of a specific design mechanic, but rather a question of broader technical viability and market acceptance… There are only a handful of projects even attempting to fulfill this vision today. Although money has strong network effects, it’s not clear how strong those effects are, or how much the market will demand viable competition to mitigate macro-level risk associated with a single mega currency.**
**Source: Kyle Samani, [Understanding Token Velocity](https://multicoin.capital/2017/12/08/understanding-token-velocity/)**
> 

To briefly illustrate why you can’t assume more users automatically benefits token holders, let’s return to our simple UBR token example.

Imagine I want to book a ride and pay in UBR tokens. To do so, I buy 10 UBR tokens with USD, and pay my driver those 10 UBR for the ride. All else equal, my purchase of UBR leads to a higher UBR price per dollar.

But… if the UBR driver sells those 10 UBR tokens for USD immediately after receiving them, this effectively nets out my purchase. All else equal, the price increase in UBR tokens is exactly canceled out.

Even if millions of rides are being paid for in UBR, if riders just buy UBR tokens when they need to spend them, and drivers sell those UBR tokens the moment they receive them, the price does not change - in fact, the UBR token is effectively worthless, as it is in effect nothing but a conduit for making a USD payment but with additional frictions in the way.

This “speed of how quickly UBR token changes hands” is what is known in economics as the **[velocity of money](https://www.investopedia.com/terms/v/velocity.asp). The velocity of money can be expressed as a number, defined as the number of times a monetary unit changes hands over a single year.

In our case above, since riders and drivers are constantly swapping UBR tokens, the average number of times each UBR token changes hands per year will be extremely high. For each ride, tokens are changing hands 3 times:

1. The rider buys the UBR token with USD
2. The rider transfers the UBR token to the driver to pay for the ride
3. The driver sells the UBR token for USD

But what if we imagine that we decrease the velocity and that drivers hold on to some, or all, of the UBR tokens they receive in payment? In our simplified example, the riders’ purchases of UBR are not entirely offset by driver sales of UBR, and the token price goes up.

This is why so many builders overly focus on supply side aspects of tokenomics. Staking, locking, slashing, escrowing, and more are all techniques employed by a variety of protocols to essentially force a reduction in the velocity of money by slowing down how many times tokens can be sold in a given period.

But a lower velocity isn’t necessarily good in every situation, as we’ll discuss further in depth in Part Two of this guide in [Chapter 2.5 Supply Policy](https://www.notion.so/2-5-Supply-Policy-ff3f8ab217b143278c3e8fd0c03ac137?pvs=21).

For now, keep in mind that you can’t just assume token holders will be benefitted - a more explicit mechanism needs to explicitly be part of your design process.

In a bull market, you may get away with worse tokenomics, but you don’t want a death spiral to kick in when a bear market arrives and suddenly token velocity increases because people don’t want to hold your poorly designed token.

https://twitter.com/mrjasonchoi/status/1550463296662188032?s=20&t=loP-e5CvO6FX8XlyGV_x7g

Let’s look at some real-world examples of similar products that have different mechanisms for benefiting token holders:

- UNI: Uniswap does not capture platform revenue, no revenues accrue to token holders
- CRV: Curve distributes protocol revenues to holders, and uses a novel “vote escrow” mechanism to incentivize lower token velocity
- GMX: Also distributed protocol revenues to holders, but also uses “multiplier points” and “escrowed emissions” to reduce token velocity and disincentivize mercenary capital

While Curve, GMX, and Uniswap are all roughly similar products, their tokenomics are drastically different. Tokens that benefit holders, all else equal, stand a better chance to win out in the long run.

As a final note on benefitting token holders, you need to be aware that certain mechanisms, such as Curve or GMX protocol revenue distributions, may carry significant regulatory risk. You should always speak to a legal professional **before** launching your token.

## Example of Good Tokenomics

Remember, there is no one “correct” or “best” set of tokenomics. To help cement what good tokenomics can look like in real-world situations, see the example below of the complete **Incentives Mechanism Framework** from the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

**Maker DAO’s **Tokenomics**

**Incentives Mechanism Framework from the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)**

| (A) Role | (B) Desired Behaviors | (C) Frictions to Desired Behaviors | (D) Undesired Behaviors | (E) Motivations for Undesired Behaviors | (F) Incentive Mechanisms | (G) Disincentive Mechanisms | (H) Mechanism Conflicts | (I) Possible Resolutions & Open Questions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Borrowers | Post collateral to mint DAI, help maintain the DAI peg to $1 | Capital intensive, pay a stability fee to mint DAI, don’t have any default reason to keep DAI at $1 | Incur bad debt, mint no DAI, manipulate DAI price | Lower quality debt is less capital intensive, minting less DAI can save on stability fees | Provide minters of DAI with many different use cases for putting their DAI to work to earn a positive net yield, encouraging more minting of DAI | Liquidate vaults if the collateral gets too low, encouraging healthy collateral balances.

Reduce cost of borrowing when DAI is >$1 (increasing supply, decreasing price) and visa versa when <$1 | Value of use cases and available investments for DAI must be equal to or greater than borrowing costs, otherwise no one will mint DAI | Partner with other DeFi protocols for lending DAI |
| Arbitragers | Help maintain the DAI peg by selling DAI when >$1 and buying DAI when <$1 | Risks of capital loss, trading costs | Manipulate prices | Profit | Deeply liquid trading pools of DAI vs other stablecoins create strong controls that ensure DAI remains overcollateralized even in black swan events, and consistently use interest rate mechanics to build confidence peg will return to give arbitragers more confidence in returns | Increasing liquidity and the number of competitive arbitragers makes manipulating prices for profit riskier |  |  |
| DAO members (MKR holders) | Remain actively engaged, work to protect, improve, and grow the protocol | Time intensive | Propose harmful governance actions | Profit | Distribute the protocols fees it earns from interest (ie charging borrowing costs) to MKR holders, encouraging them to protect and grow the protocol | If the protocol becomes undercollateralized, dilute existing MKR holders to recapitalize the protocol, encouraging MKR holders to not set too aggressive/risky collateral requirements |  |  |

# The Bad and The Ugly: Types of Ponzinomics

We’ve already briefly discussed value creation, and how even good tokenomics can not save a product that fundamentally does not create value for users.

Unfortunately, it’s all too common that builders try to compensate for a useless product by designing tokenomics that give the product an illusion of creating value.

One of the biggest warning signs that you are falling into this design trap is if you’re optimizing your tokenomics for ridiculously high APYs or similar marketing gimmicks. Such high APYs are not sustainable for a simple reason - they must be fueled by inflationary token emissions.

All else equal, a 1,000% APY from token emissions is the same thing as a 1,000% nominal **inflation** rate. Suddenly that APR doesn’t sound so appealing, does it?

The [relationship from real world Cosmos ecosystem data is not 1:1](https://lookerstudio.google.com/reporting/a9479025-42eb-4161-a941-336a683a20e5/page/c7pAD), but the overall point stands.

Even **if** the APY is being funded by a legitimate growth in protocol revenues, there is only so long that even the fastest-growing products in the world can sustain that rate of growth. Sooner or later (usually sooner), the growth rate drastically slows down - that high of an APY is not sustainable.

It’s a mistake to try and design to provide flashy APYs, even if your competitors are doing so, because when a downturn comes they will collapse - and if you’re trying to match them on APY, your protocol will collapse as well.

A bear market doesn’t change the fact that a good product legitimately creates value. But it will expose any product that hasn’t been creating value, and instead has been using unsustainable tokenomics to merely **transfer** value.

> “**Tokenomics should channel value towards those who create that value, prioritizing value *distribution* (aligned with value creation) towards high-utility groups over value *transfer* between participants.”
Source:** [Token Design for Serious People](https://jumpcrypto.com/token-design-for-serious-people/)
> 

A skeptic could argue that if tokens are meant to benefit holders and reward early adopters to overcome the bootstrapping problem, then all forms of tokenomics are meant to **transfer** wealth. But this is not a strong argument.

Consider the CRV token. Yes, all else equal the longer you’ve been using Curve, the more CRV tokens you will have accumulated and the more protocol revenues you can earn. But the fundamental product itself, the AMM, **creates** user value and earns revenue. The longer you have been providing liquidity to Curve, the more you have been responsible for helping to create that value - the more right you have to earn a **distribution** of that **created** value.

This is fundamentally different than the **transfer** of value from a new user to an old user. New users use Curve because they want to trade and doing so has value - so they pay a fee to do so. This fee is then distributed to parties roughly in line with their level of historical contribution to the value created by Curve as a product**.**

Is it perfect? No.

Is the value distributed **exactly** in proportion to the value created? No.

But is it fundamentally different from ponzinomic value **transfer** models? Yes.

To see why, consider the stark contrast of tokenomics in which news users’ economic activity is directly **transfer**r**ed** to existing users, and the product does not create any value, people only use it in the hopes that future users’ economic activity will be directly **transferred** to them.

When it first launched, Olympus DAO heavily advertised unsustainably high APYs that were a product of directly taking incoming capital from new users and distributing the economic rights to that capital (in the form of distributing new OHM tokens backed by the treasury) to existing users.

At first, this value **transfer** design appeared to work well - but it only works while more and more capital is coming in and the token price continues to go up. When the inevitable happened, and growth slowed, a death spiral kicked in. The end result left the vast majority of users badly burned, with OHM’s market cap dropping more than 95% from its peak.

The product did not create any value - the entire product was essentially just a fundraising mechanism for an investment fund that paid most incoming funds out to early investors and retained some for insiders (via a clever mechanism that ensured only the team’s share was protected from dilution).

https://twitter.com/cyounessi1/status/1483594696622489600?s=20

After the initial pump wore off, it experienced a pump-and-dump crash exactly as expected given its design. Yes, some people made lots of money from OHM, but many, many more people lost money. It’s generally not a successful strategy to burn the vast majority of your users.

We’ll discuss “protocol owned liquidity” and OHM’s unique tokenomics and history further in depth in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21).

OHM has since drastically pivoted, completely changing its marketing, tokenomics, and product features, entirely abandoning the ponzinomic staking yield.

Ironically, whereas their original pitch was around OHM’s strength due to owning its own liquidity (protocol owned liquidity), their [more recent pivots specifically boast about **reducing** protocol owned liquidity](https://twitter.com/OlympusDAO/status/1671964440458305538?s=20). And their about-face does not change the fact that its original iteration was purely a ponzi fundraising mechanism that burned many more people than it ever benefited, because all it did was directly **transfer** wealth from new token buyers to existing token buyers.

https://twitter.com/MimirSolutions/status/1486122927850405889?s=20

While these tokenomics may not meet the **textbook** definition of a ponzi scheme, they are very clearly not sustainable - even OHM itself would have to agree since they abandoned the tokenomics model in question.

<aside>
💡 Just like traditional tech products, blockchain products must **create** value, not just a token that **transfers** it from new users to existing users, to enjoy long-term success.

</aside>

Designs that are fragile to price volatility are no better than tokenomics which rely on “number go up”. For instance, UST didn’t require LUNA price to always go up. Things would never have melted down if LUNA prices had permanently stayed constant relative to the outstanding amount of UST.

But this is of course not how the world works - things are always changing, and growing net liabilities as adoption grew, plus natural volatility in LUNA price, combined with the protocol’s lack of liquidation mechanism, made UST exceptionally fragile to LUNA price volatility.

https://twitter.com/terra_money/status/1396780954006429698?s=20

Relying on collateral is not inherently bad practice. For algorithmic stablecoins like DAI, RAI, and LUSD, or lending markets like Aave, it's necessary.

Yet relying on collateral **always** introduces new risks, and systems with collateral must build resilience via safety measures, risk controls, and backstops necessary for the system can handle the natural price volatility of the collateral assets. We’ll cover a framework to help builders do just this in Part Two of this guide.

For instance, Maker DAO’s DAI uses systems such as multiple forms of collateral, conservative levels of over-collateralization, a [battle-tested process for recapitalization if necessary in black swan events](https://cointelegraph.com/news/the-makerdao-auction-is-happening-heres-what-to-expect), and flexible parameters that can be adjusted to maintain the peg in a variety of conditions (instead of being hardcoded like in UST’s case).

# The Future: Skin-In-The-Game

Designing sustainable tokenomics that are win-win-win and maximize a protocol’s chances of long-term success is not easy.

In the previous chapter, we saw this chart demonstrating how among popular DeFi protocols, only Maker DAO manages to generate revenues in excess of their token emissions (an imperfect proxy for CAC).

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7e7f994e-cd0f-4bc2-a6dd-c4a15cce7ca7/Untitled.png)

Though they have more recently made some questionable decisions that introduce centralization risks into a stablecoin that is ostensibly decentralized (discussed further in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21)), Maker DAO has historically been a great example of tokenomics done well.

So what makes Maker DAO different? What has it done well when so many other protocols have yet to strike a better balance?

- Maker DAO’s product, the DAI stablecoin, **creates** value by solving a user problem: crypto is too volatile for some use cases
- The protocol has a clear value **capture** mechanism
- The MKR token has a clear value **accrual** mechanism
- Maker DAO has a strong, governance-empowered community
- MKR token holders have skin in the game - they take on the risk of dilution if the protocol becomes undercollateralized and in return for benefitting from protocol revenues

Unlike protocols where users “stake” their tokens to earn rewards without taking on any risk or providing any value in doing so, MKR holders are aligned with the protocol’s long-term success.

As this requires more commitment and engagement, it may contribute to a psychologically higher switching cost when users consider leaving the Marker community by selling their MKR tokens.

Loss aversion is a well-known psychological bias, in which investors care nearly twice as much about a loss as they do about an equally sized gain. In other words, the pain of losing something is psychologically about twice as powerful as the pleasure of gaining something of equal value.

In the context of MKR, since holders are part of one of the most well-known communities in blockchain, and actively sharing in the revenues generated by the protocol, the potential loss of those benefits is a strong psychological motivator against dumping MKR tokens.

Contrast this with liquidity farming staking rewards for example, where users can chase yield with no skin in the game of the protocol itself, and constantly switch back and forth to whichever platform is currently offering the best yield at the time with very little switching cost.

Compared to Maker, such a protocol would need to constantly “reacquire” their users, contributing to higher CAC.

https://twitter.com/RyanWatkins_/status/1323318971635015681?s=20&t=6jvfMQDYwSY9P0Vy4lXd5w

Remember, most products don’t strictly **need** a token. Some of the most popular and successful tokenomics models in recent years though have given token holders “skin in the game” or enabled other more direct forms of user ownership.

User ownership, like all ownership, is a centralizing force if the alternative is a protocol with no governance, no ownership, and immutable code, like Bitcoin.

https://twitter.com/GwartyGwart/status/1677764817128673280

But decentralization is a spectrum - there is no such thing as “purely decentralized”, and it’s up to builders what they’re optimizing for maximum decentralization, user ownership, or something else entirely.

Curve, GMX, and Olympus DAO are also examples of protocols that, like MKR, attempted to design their tokenomics such that holders have skin in the game:

- CRV’s vote escrow mechanism means that the longer you commit to holding CRV the more influence you have on governance votes including directing liquidity rewards.
- GMX’s emissions rewards are distributed in an illiquid form that prevents immediate dumping, meaning mercenary capital behavior has a substantially different risk-reward profile than on other platforms and ensuring that the users who care about earning rewards are the types of users that are willing to make longer-term commitments.
- OHM’s [8,000% APYs](https://milesperday.com/2022/02/how-i-lost-85-staking-olympus-ohm-crypto-coins/) and heavy marketing of its [“dangerously oversimplified” (3,3) game theory meme](https://www.youtube.com/watch?v=lL13Puz-oSE&t=512s) attempted to align token holders with the protocol by trying to bribe them to stake their tokens forever and never sell. While in theory **some** small part of OHM token holders’ value was aligned with the success of OHM as a protocol and its treasury, in practice any returns generated by the treasury itself were dwarfed by the inflationary staking APY. This meant that instead of being aligned with the protocol’s success, holders were actually aligned with doing whatever it took to attract ever-increasing amounts of short-term speculator capital ([even when these holders knew the model was an unsustainable ponzi](https://twitter.com/FreddieRaynolds/status/1445284106783367171?s=20)). As expected, it then crashed 95% and [attracted hundreds of millions of dollars in lawsuits](https://www.businessinsider.com/olympusdao-founder-zeus-real-name-lawsuit-says-2022-8?r=US&IR=T).

It’s no easy feat to replicate the success of protocols like Maker, Curve, and GMX, but builders would be wise to draw some clear takeaways. Designing sustainable win-win-win tokenomics that benefit holders, improve the product, and reward contributors fosters an engaged community with skin in the game maximizes your protocol’s chances of long-term success.

# Chapter Summary

- A good product does not mean you automatically have good tokenomics
- A successful product does not mean your token price automatically goes up
- Good tokenomics are win-win-win
    - The builders win (note ”fair launches” are not necessarily best)
    - The product wins
    - The holders win
- Bad tokenomics designs can be recognized from their unsustainable claims, untested assumptions, misaligned incentives for user behavior vs desired user behavior, reliance on “price go up”, or reliance on **transferring** the economic activity of new users directly to old users instead of *creating* value and *distributing* that value
- Be especially wary about your token mechanisms when designing products that involve collateral assets and/or oracles
- While builders may be wary of chasing users off with tokenomics that ask holders to take on risks, designs that offer holders both benefits and put their skin in the game may actually lead to the best results

# Additional Resources

- Blog, [Token Design for Serious People](https://jumpcrypto.com/token-design-for-serious-people/)
- Blog, [What Are Good Tokenomics](https://blog.polkastarter.com/what-are-good-tokenomics/)
- Blog, [How To Design Tokenomics For Your Cryptocurrency: The Basics Of Creating Your Token](https://maxya.mp/how-to-design-tokenomics-for-your-cryptocurrency-the-basics-of-creating-your-token)
- Blog, [Designing Token Economies](https://www.notboring.co/p/designing-token-economies?s=r)
- YouTube, [Sam Williams: Mechanism Design 101](https://youtu.be/gCFlGLbI_kE)
- YouTube, [Token Design: Mental Models, Capabilities, and Emerging Design Spaces](https://www.youtube.com/watch?v=GOkxDvq_8zQ)
- YouTube, [Algorithmic Game Theory (Lecture 2: Mechanism Design Basics)](https://www.youtube.com/watch?v=z1QZqYuiGa8&ab_channel=TimRoughgardenLectures)
- YouTube, [Olympus DAO case study](https://youtu.be/lL13Puz-oSE?t=469)
- Blog, [Why STEPN’s Collapse Is Inevitable](https://defivader.medium.com/why-stepns-collapse-is-inevitable-5259a6584a98)
- Blog, [Creating a Sustainable Token-Based Economy](https://medium.com/the-interchain-foundation/creating-a-sustainable-token-based-economy-98b46d20796b)
- Blog (Archived), [Entrepreneurs who use Utility Tokens to reduce CAC (Customer Acquisition Cost) will create the most valuable Security Tokens](https://web.archive.org/web/20230201195247/https://dailyfintech.com/2019/04/13/entrepreneurs-who-use-utility-tokens-to-reduce-cac-customer-acquisition-cost-will-create-the-most-valuable-security-tokens/)

# 1.4 Does Every Project Need a Token?

To get right to the question posed by this chapter’s title… No. Not every project **needs** a token.

And even products that can launch a token with win-win-win tokenomics (discussed in the last chapter), do not necessarily need to launch a token **right now**.

This is especially true because if you plan ahead, you can always launch a token later, but it’s difficult to gracefully “unlaunch” a token.

<aside>
💡 Not every project needs a token. And not every project that has a legitimate reason for a token necessarily needs a token right now. But every project with a token needs the right tokenomics.

</aside>

While some products that launched tokens in have effectively “unlaunched” by buying tokens back from investors (for example, [Modum.io did so with their 2017 ICO issued MOD token](https://www.trustsquare.ch/investor-relations), doing so wastes time, incurs legal expenses, and may leave your product with significant reputational damage.

In this chapter, we’ll explore some Pros and Cons of launching a token, and cover a simple framework to evaluate whether launching a token may or may not be the right choice for your project and whether you are ready to do so.

# Token Pros

## User Acquisition & Retention

We’ve already discussed in [p](https://www.notion.so/1-1-Why-does-Tokenomics-Matter-64e59b8103c643d89ddeea6b5348a97e?pvs=21)revious chapters how, when done well, tokenomics can help attract and retain users.

The difficult part is to reward the **right** behaviors that will attract loyal, long-term users, and ensure the protocol is able to eventually generate sufficient utility value and/or revenues to make token emissions less inflationary.

Highly inflationary token emissions are not sustainable for the long term - eventually, the token price will crash, making it worthless for the purpose of acquiring or retaining users.

Readers should refer back to earlier chapters for further details.

## Community Ownership

Launching a token enables new forms of decentralized governance and community ownership that would otherwise be impossible, or at least impractical, to achieve.

<aside>
💡 Even builders in the Bitcoin ecosystem, who once held the opinion that tokens are never useful, are beginning to realize that tokens allow for aligning incentives in way that makes it possible to build credibly neutral, censorship-resistant protocols and apps that can compete in a free market against more centralized tools.

</aside>

This is incredibly difficult to do without tokens.

https://twitter.com/EdanYago/status/1679830151549399041?s=20

More explicitly tokens can enable unique community governance models like Maker DAO and Nouns DAO. We’ll discuss DAOs and governance much more in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21), and the specific risks of governance tokens in [Chapter 1.5](https://www.notion.so/1-5-Types-of-Tokens-1e1f4f7120144ec4a83baa1dee9b3e7e?pvs=21), but keep in mind that community ownership and control can take many more forms than the default approach: “1 token, 1 vote, more than 50% wins”.

Decentralized governance and community ownership does not necessarily require a tradeable or transferable token. In some cases, it can be possible, if not preferable, to use a non-transferable, “soulbound” reputation token for governance to reduce (but not eliminate) the threat of governance attacks.

While community ownership has the potential to improve network engagement, security, and resiliency, decentralized governance can also be a major headache, akin to running a public company and introducing cases where uninformed decision makers are voting on complex decisions that require high context to make an informed vote.

https://twitter.com/TokenBrice/status/1567552522809753604?s=20

Protocols like Liquity have purposefully avoided community governance by design, opting for an immutable protocol. Their native LQTY token is not a governance token but still aids in overcoming the bootstrapping problem by distributing protocol revenues, thus incentivizing holders to grow the network. It achieves **community ownership** without requiring **community governance**.

## Fundraising

**This section is not an endorsement for launching a token as an unregistered security offering. It does not represent legal or financial advice. Always consult your own legal representation before launching a token.**

Raising money via a token can certainly make it easier to raise more capital and/or at better valuations. That said, launching a token, especially one that is sold to raise money, **always** carries regulatory considerations.

That is not to say every fundraise carries the same risks. It is possible to raise investment that is registered, or which is exempt from registration, with the SEC. For example, Bitcoin L2 Stacks conducted an ICO via a [registered offering with the SEC](https://decrypt.co/9076/blockstack-nets-23-million-historic-sec-qualified-token-sale-ico).

Tokens can avoid regulatory uncertainty by explicitly launching as financial securities (Security Tokens, which we’ll discuss in the next chapter), but it is not necessarily required to launch a Security Token in order to raise money via a token.

Structured as Reg-D offerings, agreements such as Simple Agreement for Future Tokens (SAFT) or token warrants *may* allow for raising from accredited and/or institutional investors with a token in a compliant fashion without necessarily being a Security Token Offering.

“The SAFT Project” [offers a template SAFT](https://saftproject.com/) that builders who are fundraising may find helpful and Legal Nodes offers further [information about token warrants](https://legalnodes.com/template/token-warrant) as well as this [template token warrant](https://docs.google.com/document/d/1F4H11jLPFt1s0fs9rfxImemKIU1kxViX/edit?usp=sharing&ouid=113048252102766915163&rtpof=true&sd=true) - but this is not legal advice and you should always consult your own legal counsel to see if these templates are applicable to your situation. 

Note that since the [XRP vs SEC court case ruling in July 2023](https://www.reuters.com/legal/us-judge-says-sec-lawsuit-vs-ripple-labs-can-proceed-trial-some-claims-2023-07-13), judge Analisa Torres’ ruling that sales of XRP to institutional investors represented a securities offering has been frequently misunderstood. The ruling does not mean that selling tokens to VCs inherently violates securities law, or that doing so makes the token itself a security. In both Web2 and Web3, it is common practice to raise money from securities offerings to VCs **without** registering with the SEC via a [Reg-D offering](https://carta.com/blog/regulation-d/). These offerings are *exempt* from the usual requirements to register securities offerings with the SEC, as long as certain criteria are met.

Reg-D exists to help streamline economic activity. Imagine if every time a Web2 startup wanted to raise a Seed round they had to register with the SEC like an IPO, and wait for qualification. It’d be incredibly hard, expensive, and slow for new companies to raise money and build new tech.

Of course, the findings of the XRP case can change if the case is appealed or be called into question if other courts disagree in similar cases - but even if so, that won’t change Reg-D itself.

https://twitter.com/Orlando_btc/status/1679596100079190016?s=20

For companies that raise money via both equity (traditional shares) and via tokens, there is not yet an industry standard for how these relate. It’s largely up to the company and its investors whether equity investors are automatically granted pro-rata share tokens, are granted the right to buy tokens at a particular price (token warrant), are granted a [MFN clause](https://capbase.com/most-favored-nation-mfn-clause-in-startup-investing-what-it-is-and-how-it-works/) for any future token sales, or have no special rights to any future token sales.

Based on conversations with VCs, accelerators, incubators, and angel investors with hundreds of aggregate crypto investments, the majority expressed they **prefer** to invest in token form, or at least with the option of a token.

Why? Because tokens can offer more liquidity than traditional equity shares, even after accounting for vesting schedules. Additionally, many investors expressed that they see higher returns in their token investments vs traditional equity. Whether justified or not, tokens tended to carry valuation premiums to traditional shares of companies with comparable fundamentals.

You can find plenty of examples of products only raising via equity or only raising via a token sale, though it is increasingly becoming commonplace to raise via equity (typically a SAFE for early rounds) combined with a token warrant.

Here are a few examples from real deal flow (all identifying details redacted):

- “raising a $2M SAFE at a $15M pre-money valuation with a 1:1 token warrant”
- “raising $1M at a $12M post-money valuation with 1:1 token warrants”
- “raising a SAFE at a $10M post-money valuation cap (w/ token warrant at 1.00 : 0.75, or implied $13.3M FDV)”
- “raising $12M at $100M post-money (+ token warrant at $225M FDV cap)”
- “$2M SAFE (w/ 1:1 token warrants) at a $20M post-money cap”

<aside>
⚠️ Builders should beware of launching a token purely to raise capital though. If your product or pitch is not convincing enough on its own, slapping a token on as an afterthought is rarely a wise approach. The founders I’ve spoken with who privately admit their token’s entire purpose is to raise money are rarely able to raise VC funding anyway - so it’s less helpful than many first-time founders assume.

</aside>

Even if tacking on a token is what makes the difference and allows you to raise funds, launching a token solely for the purpose of fundraising means builders have to reverse engineer a justification for the token’s existence in the first place.

As you can imagine, this typically results in extremely fragile tokenomics with needless complexity, multiple tokens, and/or lazy, pump-and-dump designs such as ponzinomic transfers of wealth directly from later token buyers to earlier token holders.

## Multichain Support

A native token can sometimes make your users’ experience simpler when your product bridges multiple chains. For example, Chainlink, which provides oracle data to many different chains, uses LINK instead of requiring users to pay fees in multiple different gas tokens.

It’s becoming easier than ever to deploy a token on multiple chains, with a plethora of infrastructure solutions such as Layer Zero offering solutions, that while not risk-free, do not have the same custodial risks of wrapped assets or risks of traditional bridges.

Depending on your use case, and the chains your community uses, supporting your token across multiple chains and/or rollups may require implementing custom bridges that create additional complications and security risks.

## New Types of Business Models & Products

Lastly, a token can enable new business models, products, and user experiences that are not feasible without a token. We talked about this in previous chapters, when we discussed how tokens can align crucial incentives. 

For example, it’d be impossible to securely extend the use case of distributed computing to cover economic transactions as well without the proper security derived by economic incentives (ie the ETH token for the Ethereum network).

However, it’s important to be honest with yourself about this benefit. Most protocols that have a token don’t have win-win-win tokenomics. And very few protocols strictly **need** a token.

It’s possible you don’t **need** a token, but that a token would make your product better. But it’s important to keep yourself honest and remember what makes for good tokenomics (win-win-win).

Otherwise, it’s all too easy to fall into the trap of assuming you need a token and that you need it right now. Rushing to launch a hastily designed token can do a lot more harm to your product and community than waiting to launch a better-designed token when you’re ready.

# Token Cons

## Reputation Risk

One of the most obvious downsides of launching a token can be skepticism about the token and the team’s motivations.

Good products that launch a token run the risk of being seen as a scam or using the community as “exit liquidity”, and this is especially true if the tokenomics are not well designed, not transparent, are not win-win-win, or the timing is not right.

The best way to protect against this risk is to follow best practices for tokenomics design which we cover in Part Two of this guide and to be honest with yourself about your motivations. Launching a token purely for raising money or for short-term objectives rarely works out well in the long run.

## Legal & Regulatory Risks

An increasingly large risk to any token launch is the risk of falling afoul of regulators. Regardless of your personal feelings about Ripple, LBRY, Binance, Coinbase, or the SEC, the fact remains that even if you eventually win a legal case with regulators, you can first waste millions of dollars, get delisted from exchanges, and get bombarded on both sides by investigations and upset community members.

Is the lack of regulatory clarity reasonable or fair? No.

But is it a real risk you need to take seriously? Sadly, yes.

Even with the recent development in the Ripple case, the battle is not over. Just ask protocols like LBRY - even if you eventually come out on top, when you tangle with regulators, it’s almost always at best a Pyrrhic victory.

 

https://twitter.com/LBRYcom/status/1510005363604660225?s=20

When in doubt, the best way to protect against this risk is to not launch a token until you have regulatory clarity due to a change in your circumstances or in the law.

The second best way to protect against this risk is to consult with knowledgeable legal professionals about the specifics of your tokenomics design.

<aside>
💡 If you have a legitimate use case for a token, and want the benefits offering a token can have on fundraising without taking on the regulatory risk, you may consider offering VC investors a token warrant. A token warrant generally specifies that you are under no obligation to launch a token, but that if you do, warrants holders have certain rights to purchase the token. You should always check with a legal professional before doing this, but it may be a way to limit risks, avoid the obligation to launch a token before you’re ready, and still retain some of the benefits that launching a token offers.

</aside>

We’ll cover a bit of some legal resources in [Chapter 2.7 Legal Opinion](https://www.notion.so/2-7-Legal-Opinion-Structure-94f04489ede3424fbc66e358fa5f317c?pvs=21) that may help point you in the right direction. However, as a reminder, this guide is not legal advice and the author is not a legal professional.

## Distracts from Core Product

One of the biggest oversights founders make is not realizing how much of their time and resources will be consumed by their token.

> **We would have to elaborate a plan to develop and release those [tokens] safely, without any exploit or unintentional backdoor. And give some to the investors. All of this of course was totally unnecessary to make a [DEX]. A bit like companies going public, we would simulate having purchasable shares that way, the crypto was our shares, even thought we were not even a legally registered company. Which was a job as of itself, and a bit on the grey legal line.
- Anicet Nougaret, [A postmortem: My experience as a DeFi startup Co-Founder](https://anicetnougaret.fr/blog/farswap-xp)**
> 

<aside>
⚠️ Once your token is live, it’s not a matter of **if** it will be a resource drain, but a question of **how much** of a drain it will be.

</aside>

It’s not a quick fix to problems with your product, and in fact, it can make those problems get even more attention and less time to fix. This can mean the product itself, the thing that ostensibly uses the token and benefits from the token, directly suffers because of the token.

> **Development takes time, much longer than even you, as a developer, think it will… But now, add hundreds (sometimes thousands) of people shouting on telegram, discord, and twitter “when will it be released?”, “why hasn’t it been released?”, “give us an update!”, and often, significantly more hostile messages.
- Andre Cronje, [Building in defi sucks (part 2)](https://andrecronje.medium.com/building-in-defi-sucks-part-2-75df9ee7871b)**
> 

The only way to protect against this risk is to not launch a token until you’re ready to operate in full public view. Even if a token is the right choice, it may not be the right choice right away if you aren’t ready to balance the core product with the hours of distraction the token will cause.

## User Friction

If users are required to first acquire, earn, or purchase your token in order to use your product or join your community, this can actually add friction to onboarding more users, and result in the product growing slower than without a token.

To return to the Web3 Uber example discussed in previous chapters, imagine instead of being able to pay in USD and use UBR tokens to get a discount, all users **must** pay with UBR tokens.

You’ve just made it much more difficult and added a few more steps for people who don’t already have a crypto wallet or who don’t already have enough UBR tokens to use your product.

A lot of people who would otherwise use the service, and maybe eventually become holders and users of UBR tokens, will never even try the service.

This might be alright if your product or community already has high usage. If the app has already reached critical mass, adding some friction might not cause many users to leave because using the product is still highly valuable, and worth the trouble.

Imagine what you’d do if one friend says to you, “Hey, download this new messaging app so we can chat.” Will you really download a new app just to chat with them? Probably not. Downloading the app is a friction point that prevented you from joining as a new user.

But if most or all of your friends are already on the app, you’re much more likely to download it. The benefit (network effect) that the app has, overcomes the friction.

## Churn Users & Crash Your Usage

In [Chapter 1.1](https://www.notion.so/1-1-Why-does-Tokenomics-Matter-64e59b8103c643d89ddeea6b5348a97e?pvs=21), we mentioned how one of the potential benefits of tokens is to overcome the bootstrapping or cold start problem that marketplaces have.

In that chapter, we looked at cases where this was done reasonably well, such as Maker DAO, as well as cases where this was done poorly, such as Axie Infinity and STEPN.

Bringing in new users is a necessary step to overcoming the bootstrapping problem and building a network effect. The problem is, while tokens can bring in new users, if your product itself is not ready or capable of *retaining* those users, this can actually be net destructive by fueling a spike of new users, who then quickly churn, resulting in fewer users than if you had grown at a more sustainable pace in the first place.

!https://assets.super.so/1fb1238b-00a4-4bef-98fc-3b1212a3a63d/images/75a1f0a3-bbbc-474a-bed8-18a8843a5e37/1*Q1rBOUC3tarrEaqwiLKH6Q.png?w=1500&f=webp

<aside>
⚠️ Converting users earlier doesn’t automatically lead to user retention or increase the total addressable market. If you accelerate user conversion but can’t sustainably retain them, you aren’t actually approaching critical mass for network effects. Instead, you’re increasing user churn and increasing the chances of a death spiral.

</aside>

While tokens can help reach critical mass, those users must be retained to have a lasting impact. Many builders take this for granted, and overlook the devil in the details:

- AMMs like Uniswap and Curve are generally viewed as clear examples of where a token helped overcome the bootstrapping problem in aggregate. But when looking closer at specific pools, [experiments with token incentive programs have shown mixed results](https://medium.com/gauntlet-networks/uniswap-liquidity-mining-analysis-14c739c54a9d) for kickstarting higher TVL and fees that persist after the program ends.
- Infrastructure plays like Filecoin and Helium have largely been successful at bootstrapping **supply-side** users. But Filecoin has a large excess storage capacity ([active deals have tended to be only 5%-10% of network capacity](https://dashboard.starboard.ventures/capacity-services)) and Helium is still [struggling to onboard paying demand-side users](https://blockworks.co/news/where-is-the-revenue-helium-investors-inquire). Network effects can only be reached with a critical mass of both supply-side and demand-side users.

These examples underscore just how important it is to get token incentives right, and how difficult it can be when you look beneath the surface.

In theory, tokens can help acquire users. In practice it’s not that simple - the tokenomics have to balance supply (emissions) with demand (use cases, utility, value accrual, etc).

## Increases Complexity & Risks

The final considerable drawback to launching a token is that doing so may vastly increase your liabilities to hacks and exploits.

> **Some exploit occurs? You are 100% to blame and need to refund or figure out ways to make them whole again.
- Andre Cronje, [Building in defi sucks (part 2)](https://andrecronje.medium.com/building-in-defi-sucks-part-2-75df9ee7871b)**
> 

Don’t make the mistake of assuming something as simple as a smart contract audit removes this risk either. Introducing your own token not only increases the risks of hacks but also of economic exploits.

For example, neither the collapse of UST nor the recent Mango exploit were explicitly caused by hacks - they were exploits taking advantage of economic vulnerabilities.

Protecting against these risks is not as a matter of getting a smart contracts audit, though in [Chapter 2.6](https://www.notion.so/2-6-Modeling-Optimization-bcaab2f1ee2c4cceb6371ce29d3e1827?pvs=21) we’ll look at the **Economic Security Framework** to help catch and mitigate these risks.

# Token Checklist

This checklist helps builders determine whether it may be appropriate to launch a token and if so, when the right time may be to do so.

## Do You Ever Need a Token?

You probably don’t ever need a token if you don’t meet the below criteria:

- At least one of:
    - [ ]  The product intends to be either fully decentralized, permissionless, or community-owned/operated
    - [ ]  The token benefits the product itself (ex. product will be faster, simpler, less expensive, more secure, etc. than possible without a token)
    - [ ]  The token will be a native form of gas or currency to a chain, or it represents or tracks a value pegged to an off-chain or on-chain asset (ex. stablecoins, carbon credits, etc.)
- And, at least one of:
    - [ ]  The token is used for reputation (not transferable, no explicit monetary value)
    - [ ]  The token has legitimate use cases and utility for holders (providing liquidity, staking to earn more of the same token, and price speculation trading are not legitimate utilities)
    - [ ]  The token can financially reward holders via buybacks, revenue distributions, or similar mechanisms funded by paying users of the protocol, not ponzi transfers of wealth
    (you **must** be conscious of legal/regulatory aspects if this is the option you’re relying on - speak to your legal representation)

## Is Now the Right Time to Launch a Token?

Even if you need a token at some point, you probably aren’t ready to launch one until you meet these additional criteria:

- Launching the token now is will materially help with at least one of:
    - [ ]  Attracting new users you are able to retain (you have product market fit)
    - [ ]  Retaining existing users (even when emissions decline)
    - [ ]  Protecting from competitors (defending against a vampire attack)
    - [ ]  Enabling significant community control and governance (not decentralization theater)
- At least one of:
    - [ ]  The core team is prepared to operate a “public company”
    - [ ]  The core team is ready to fully abdicate responsibility to token holders, and token holders are ready to take full control  of day-to-day governance and operations
    - [ ]  There is no “core team” to begin with, or all of the contracts have been deployed and are non-upgradeable and immutable (i.e. Bitcoin or Liquity)
- At least one of:
    - [ ]  The product has achieved “[sufficient decentralization](https://variant.fund/articles/sufficient-decentralization/)” (legal risks may still apply)
    - [ ]  You will not be selling tokens to non-accredited US investors (there may still be regulatory implications for tokens given away for free)
    - [ ]  You have registered your token offering sale with the SEC or the relevant regulator for your jurisdiction such as the MAS in Singapore
- And:
    - [ ]  Your token launch plan has been reviewed by a knowledgeable legal professional

# Chapter Summary

- Launching a token has both pros and cons, builders need to carefully weigh them, as once launched, it’s very difficult to gracefully “unlaunch” a token - doing so almost always wastes time and damages reputation
- Pros: easier fundraising, benefit user acquisition, enable community ownership, support multichain, and enable new products
- Cons: reputation risk/damage, legal risks, distracts resources from core product, create additional complexities and economic exploit risks that smart contract audits are not designed to catch
- The simple framework at the end of the chapter can help to quickly evaluate if a token is right for your product, and if **now** is the right time

# Additional Resources

- Blog, [Does Your Product Need a Token?](https://outlierventures.io/does-your-product-need-a-token/)
- Blog, [Are Tokens Good for Bootstrapping Growth?](https://designingtokenomics.com/the-complete-tokenomics-course-primer/articles/are-tokens-good-for-bootstrapping-network-effects)
- Blog, [Should Product-Market Fit Come Before Tokens?](https://blog.oceanprotocol.com/should-product-market-fit-come-before-tokens-6c542a75c8dc)
- Blog, [When to Launch a Token](https://variant.fund/articles/when-to-launch-token/)
- YouTube, [Token Design: Mental Models, Capabilities, and Emerging Design Spaces](https://youtu.be/GOkxDvq_8zQ?t=370)
- Blog, [Sufficient Decentralization: A Playbook for Web3 Builders and Lawyers](https://variant.fund/articles/sufficient-decentralization/)
- Blog, [Progressive Decentralization: A Playbook for Building Crypto Applications](https://jessewalden.com/progressive-decentralization-a-playbook-for-building-crypto-applications/)
- Blog, [Decentralization for Web3 Builders: Principles, Models, How To](https://future.com/web3-decentralization-models-framework-principles-how-to/#section--2)
- Blog, [5 Lessons from a Failed Token Sale](https://medium.com/snips-ai/5-lessons-from-a-failed-token-sale-410e47a66647)

# 1.5 Types of Tokens

First and foremost, builders need to understand that no universally accepted, formal classification system for tokens exists.

How individual tokens are classified will differ depending on who you ask, including varying between regulatory jurisdictions. The majority of jurisdictions have not ruled definitively on specific tokens, but many have provided much more comprehensive guidance than the United States, particularly Switzerland and Singapore.

These definitions help provide **some** degree of objectivity to token-type classifications, and are useful for builders to be familiar with, especially since so many crypto projects have foundations or other legal entities in Switzerland or Singapore.

Yet even in Switzerland and Singapore, how a particular token may be classified remains a subjective question. Complicating the matter is the fact that most tokens possess a mix of characteristics that make them difficult to classify.

For example, Curve’s CRV token is used in governance, earns stakers a portion of protocol revenues, and has utility for protocols that wish to direct incentives to their token’s liquidity pool.

Does that make CRV a governance token, a stakeholder token, or a utility token?

Binance’s BNB token is used access certain priority features, use the trading service with a discount, and holders expect to benefit when trading activity increases due to a buyback-and-burn mechanism.

Does that make BNB a utility token, a payment token, or a stakeholder token?

There is no universal answer to these questions.

But drawing distinctions between types of tokens according to their objectives is helpful for builders - you want to be intentional about which type of token you are launching.

Knowing which kind of token you’re launching, and which kind is appropriate for your objectives, is an important part of good token design.

# Token Types: Regulatory Guidelines

*Just as with all other content in this guide, the below content is not legal advice. It is presented purely for informational purposes about how different jurisdictions may classify tokens. Do not rely on this information for making legal decisions, even if you are launching a token in one of the jurisdictions mentioned below. Always consult a registered legal professional to ensure compliance with any and all relevant laws and regulations.*

## Switzerland

Guidance issued by the Swiss Financial Market Supervisory Authority (FINMA) distinguishes three types of tokens, and outlines specific evaluation criteria used in determining the case for each token.

### Token Types

- **Payment tokens**
Tokens intended to be used, now or in the future, as a means of payment for acquiring goods or services or as a means of money or value transfer. They are not considered securities. FINMA specifies three criteria for determining whether a token fits the definition of a payment token:
    - Must be created and issued by a non-financial intermediary
    - Must be freely transferable between wallet addresses
    - Must be used primarily as a means of payment

- **Utility tokens**
Used to access a digital application or service provided by blockchain infrastructure such as a dApp. Depending on their form, they are comparable to vouchers or points that can be redeemed for contractually owed services. They are not considered to be securities if they do not confer any ownership rights. FINMA specifies three criteria for determining whether a token fits the definition of a utility token:
    - Must be created and issued by a non-financial intermediary
    - Must be freely transferable between wallet addresses
    - Must have a clear utility, such as providing access to a platform or service, and are primarily used for this specific purpose

- **Asset tokens**
Represent an ownership interest in an underlying asset. This includes tokens that represent a share in future company earnings or similar claims to future cash flows, as well as tokenized real-world assets. They are considered to be securities and are therefore subject to securities laws. FINMA specifies three criteria for determining whether a token fits the definition of a security token:
    - Represent an ownership interest in an underlying asset
    - Are offered to the public
    - Are sold with the expectation of profit

<aside>
💡 Though FINMA guidance distinguishes between payment tokens, utility tokens, and assets tokens, it explicitly mentions these classes are **not mutually exclusive**.

</aside>

In practice, this means it is entirely possible for FINMA to view a token as both a payment token and an asset token. In such a case, despite also being a payment token, as an asset token it would be subject to securities law.

### Evaluation Criteria

FINMA has also stated that it will consider all of the below factors when determining which type is applicable.

- **Economic function:** The economic function of the token, such as whether it is primarily used as a medium of exchange, store of value, unit of account, give access to a service or platform, etc
- **Underlying asset:** The underlying asset that the token is linked to, if any
- **Transferability:** The transferability of the token, such as whether it is freely transferrable, only transferrable to whitelisted addresses, soulbound, etc
- **Maturity:** The maturity or expiration date of the token, if any
- **Risks:** The risks associated with the token including whether the degree of risk and the nature of risks the token is exposed to

## Singapore

The Monetary Authority of Singapore (MAS) has also published classification guidance quite similar to Switzerland’s.

### Token Types

- **Digital Payment Tokens (DPTs)**
Tokens used as a medium of exchange, a unit of account, or a store of value that are not associated with an underlying asset or security.
- **Utility Tokens**
Tokens that give holders access to a particular service or platform, or are used to purchase goods or service on a particular platform. These tokens may be associated with an underlying asset or security, but the value of the token must not be derived solely from the value of the underlying asset or security.

- **Security Tokens
T**okens that represent ownership interest, right to ownership interest, or an option to acquire an interest, in a company or other asset. As their name implies, security tokens are regulated by securities laws, must be issued in accordance with the securities laws of Singapore, and are subject to the same regulatory requirements as other securities.

### Evaluation Criteria

The MAS has specified they use the following three criteria to determine the type of token:

1. **Purpose:** The purpose of the token. For example, is it used as a means of payment, to provide access to a platform or service, or to represent an ownership interest in an underlying asset?
2. **Rights:** The rights that the token gives to the holder. For example, does it give the holder the right to vote on corporate matters, to receive dividends, or to redeem the token for goods or services?
3. **Distribution:** The way in which the token is distributed. For example, is it sold to the public or is it only available to a select group of investors?

## Other Jurisdictions

While two of the most popular jurisdictions for builders, Switzerland and Singapore are far from the only jurisdictions to issue similar guidance.

Japan (FSA), Canada (CSA), Hong Kong (SFC), South Korea (FSC), Estonia (EFSA), the United Kingdom (FSA), and other countries have issued guidance that *generally* draw some form of distinction between payment tokens, utility tokens, and security/asset tokens.

While there are of course differences between jurisdictions, unlike the actions of regulators in the United States, most jurisdictions are similar in acknowledging types of tokens other than securities tokens.

That said, there are no known cases of final, definitive rulings on the classification of any particular token - with the potential exception of LBRY, KIN (Kik), and TON (Telegram) being found by United States courts to be security tokens. While the SEC has made similar allegations against a number of other tokens, including XRP, to date the courts have yet to find the tokens themselves are securities, even though **sales of the token** may be, in certain circumstances, a securities offering.

Further muddying the waters is the fact that even the jurisdictions with relatively sophisticated guidance still have blind spots. 

For example, a non-transferrable (soulbond) reputation token is very clearly not a security token since it can’t be bought for speculation, sold for a profit, or traded for any price. Yet it also does not neatly fit into the Swiss definition of a utility token or payment token since it is not “freely transferable between wallet addresses”.

Thus, the industry is left to draw unofficial classifications. While not recognized by a legal jurisdiction, they remain common industry terminology, and useful for builders to understand so they can be intentional about what they are designing, and the relevant strengths, weaknesses, and limitations of their token.

## A Note on Security Tokens

Security Tokens, issued via Security Token Offerings, are tokens which elect to follow all securities laws including but not limited to KYC/AML measures, in order to have regularity clarity.

In jurisdictions like Singapore and Switzerland, these tokens fit relatively clearly into the Security Token or Asset Token designations based on regulator guidance.

Yet even in the United States, which has issued virtually no blockchain specific guidance whatsoever, Security Token Offerings can be a compliant path for token issuance simply because these tokens and their initial sales offerings follow all existing regulations as if they were a traditional security, not a blockchain token.

By their very nature, Security Tokens can not be censorship resistant and decentralized in the same way tokens controlled by immutable code can be.

But that does not necessarily mean Security Tokens have no appropriate use cases. For example, Security Tokens may ultimately be the only viable path for RWA blockchain products, since RWA product **always** have centralized points of failure that can be censored and shutdown by regulators, and thus need to be in full compliance.

Infrastructure platforms such as [Fireblocks](https://www.fireblocks.com/platforms/tokenization/), and [1X](https://tokenist.com/private-securities-exchange-1x-launches-in-singapore-with-4-1-million-worth-of-security-tokens-listed) in Singapore, offer infrastructure to support compliant tokenization and issuance of Security Tokens, and have helped facilitate offerings for tokenized bonds, REITs, preferred stock, and more.

# Token Types: Unofficial Industry Definitions

*Any of the below token types may be found to be a security by a regulatory body. Do not rely on the below token classifications as legal advice, they are for informational purposes only. Always consult a registered legal professional to ensure compliance with any and all relevant laws and regulations.*

<aside>
💡 While some of the classifications listed below, such as medium of exchange tokens, are virtually always fungible **tokens in practice, the below classifications are not strictly limited to fungible tokens. Distinguishing between fungible tokens or non-fungible tokens (NFTs) is largely orthogonal to the below classifications.

</aside>

 

## Reputation Tokens

Reputation tokens track the social credibility of a community member within a given community. By their very nature, these tokens are not fungible across communities. For example, while a person may be very credible in a legal community as a talented lawyer, that does not necessarily give them credibility in a community of musicians.

Reputation tokens do not necessarily have to fungible **within** a community either - reputation could be represented by NFTs, similar to different roles in a Discord server. In fact, these tokens may not be transferrable at all (soulbound tokens). While this has obvious downsides, since some form of originating logic or party must govern how reputation is initially assigned, and if or how it can be earned, it also protects against vote-buying or other attacks that can occur when reputation is for sale.

![**Source: [Reputation vs Tokens](https://medium.com/daostack/reputation-vs-tokens-6d7642c7a538)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/85deda6f-e668-4883-ae3a-8aaea705b7e3/Untitled.png)

**Source: [Reputation vs Tokens](https://medium.com/daostack/reputation-vs-tokens-6d7642c7a538)**

Depending on how they are implemented, reputation tokens may be very similar in function to governance tokens, and one could argue that a theoretical soulbound governance token would in essence be a reputation token.

## Store of Value Tokens

Store of value tokens primarily exist to retain or increase their purchasing power over time - something which is much easier said than done. In other words, these tokens represent properties consistent with gold or real estate in that they are “hard assets” that tend to offer protection from inflation.

> **[Store of value] is by far the most difficult to achieve as it’s not a function of a specific design mechanic, but rather a question of broader technical viability and market acceptance.**
**Source: [Understanding Token Velocity](https://multicoin.capital/2017/12/08/understanding-token-velocity/)**
> 

The reality is that almost no coins or tokens have much large scale credible market acceptance as a store of value of inflation hedge other than BTC or ETH. Even then, both have hotly debated counterpoints from **within** their own communities - namely that BTC can’t maintain its security in the future without [eventually increasing supply above 21mm](https://thebitcoinmanual.com/articles/btc-tail-emissions-debate/), and that ETH, despite its claims, is [not ultrasound money](https://joncharbonneau.substack.com/p/eth-is-not-ultrasound-money-part).

If even BTC and ETH have been unable to establish clear market acceptance as a store of value, you can see why builders are naive to assume that their token will inherently act as a store of value.

> **99 percent of tokens won’t ever satisfy the store of value pre-requisites… You’ll also notice that usage as a medium of exchange and dAppp functionality is not listed as a prerequisite. There are two diametrically opposed tradeoffs… Base layer trustlessness is a necessary condition for a reserve store of value and layer-one transactions and feature richness are not. Without trustlessness, blockchains start to act [more] like… our current inflationary monetary system than a reserve store of value.
Source: [Making Sense of Crypto Asset Valuation Insanity](https://www.coindesk.com/markets/2018/03/11/making-sense-of-crypto-asset-valuation-insanity/#:~:text=Most%20assets%20won%27t%20become%20a%20reserve%20store%20of%20value)**
> 

## Medium of Exchange Tokens

Medium of exchange and store of value are often confused - for example physical gold and real estate are generally considered stores of value, but you do not pay for everyday purchases with nuggets of gold or deeds to property.

One of the factors that confuses builders is that this distinction breaks down on the blockchain, where everything is digital - it’s just as easy to use digital gold to make a payment as it is to use digital dollars.

As discussed in Chapter 1.3, amateur builders often fall into the trap of thinking their token will be treated as a medium of exchange. They assume their token will have an inherent value to people as a form of payment. Yet this is not realistic - it would require a large network preferring to do business in your token instead of using traditional fiat currencies, tokenized gold, stablecoins, BTC, or ETH.

For better or worse, stablecoins have largely proven themselves to be the preferred medium of exchange tokens on the blockchain, as evidenced by both their growth of total crypto market cap, and their share of trading activity. It would be hard for a token that is not a stablecoin to compete directly against stablecoins at the very use case they excel at - serving as a medium of exchange.

![**Source: [Record stablecoin market share points to crypto upside: JPMorgan](https://cointelegraph.com/news/record-stablecoin-market-share-points-to-crypto-upside-jpmorgan)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67c0ed9e-4274-4347-95c5-cb5209ed7e8c/Untitled.png)

**Source: [Record stablecoin market share points to crypto upside: JPMorgan](https://cointelegraph.com/news/record-stablecoin-market-share-points-to-crypto-upside-jpmorgan)**

![**Source: [The State of Stablecoins](https://research.kaiko.com/insights/the-state-of-stablecoins)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1ffe9849-4c1c-413b-8b12-d2f95c5798e8/Untitled.png)

**Source: [The State of Stablecoins](https://research.kaiko.com/insights/the-state-of-stablecoins)**

The dominance of stablecoins as **the** crypto industry’s preferred medium of exchange holds true even when comparing to Bitcoin itself (which, was in Satoshi’s own words, was designed to be "a peer-to-peer electronic cash system”).

If even Bitcoin itself serves less of a medium of exchange role than stablecoins, then you can see how wildly uninformed it is for builders to assume their token will serve a medium of exchange role.

https://x.com/nic__carter/status/1701521505300189415?s=20

It is therefore generally unwise to launch a non-stablecoin token meant to function as a medium of exchange unless within a very specific economy, such as an in-game currency in a gaming economy.

Ironically, even if a token were able to become a **general** medium of exchange, the more it is used as a medium of exchange, the more its velocity of money increases, and all else equal, the less valuable the token becomes.

This is at the heart of the inherent conflict between being a “store of value” and a “medium of exchange”, and amateur builders not only convince themselves their token will automatically function as one of these roles (already extremely difficult), they naively assume their token will function as both!

> **In the case of pure cryptocurrencies like bitcoin, store-of-value use (“hodling”) and medium-of-exchange use (“buying coffees”) are naturally in conflict, as the store-of-value prizes security much more than the medium-of-exchange use case, which more strongly values usability.
Source: Vitalik Buterin, [Notes on Blockchain Governance](https://vitalik.ca/general/2017/12/17/voting.html)**
> 

## Stakeholder Tokens

Stakeholder tokens align the interest of token holders and the protocol by making the holders stakeholders in the protocol’s success and/or its failures (skin in the game). This does not necessarily mean a stakeholder token must carry with it governance rights.

For instance, Liquity’s LQTY token is not a governance token, but distributes protocol revenues to holders, giving them a stake in the success and adoption of LUSD.

Examples of stakeholder tokens which do happen to carry governance rights include MKR, CRV, GMX, and many more.

While stakeholder tokens may represent more legal or regulatory risk due to the explicit alignment of incentives, builders should not conflate **stakeholders** with **shareholders**.

For better or worse, one can have a stake in a product’s outcome without necessarily possessing everything that it means to be a shareholder such as voting rights and legal claims.

An employee at a company is a **stakeholder**, as their salary depends on the ongoing operations of the company, even if they do not own any equity or have voting rights in the company.

Of course, regulators may not see it that way for any given token, and may choose to view popular stakeholder tokens such as MKR, CRV, GMX, YFI, LQTY, HEGIC, and others as securities. Builders should take note that it is likely they may draw more regulatory risk for a stakeholder token.

Why then do products take that extra risk? One reason is that unlike assuming a token will function as a medium of exchange or store of value, genuinely aligning holder interests is a much stronger driver of value. Relatively informal attempts to classify tokens and assess their various performances have yielded weak evidence to support this - though the analysis makes no claims to statistical significance.

![Performance of tokens based on their classification. The analysis uses the term “productive” tokens to describe stakeholder tokens
Source: [What's the Best Token Model?](https://www.notion.so/1-3-The-Good-The-Bad-and-The-Ugly-3dfc31a65d33497394e3a4965ed90e4b?pvs=21)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5f11eebd-b327-4172-9439-99a216486885/Untitled.png)

Performance of tokens based on their classification. The analysis uses the term “productive” tokens to describe stakeholder tokens
Source: [What's the Best Token Model?](https://www.notion.so/1-3-The-Good-The-Bad-and-The-Ugly-3dfc31a65d33497394e3a4965ed90e4b?pvs=21)

As the industry matures, it is likely that stakeholder tokens continue to outperform and become more popular. Stakeholder tokens require making holders into stakeholders of the product, which means aligning incentives via value accrual mechanisms to the token. We’ll discuss these mechanisms much more in Part Two of this guide, and builders who are designing stakeholder tokens will want to spend extra time refining their value accrual mechanisms and working with registered legal professionals to assess any regulatory risks.

## Stable and Pegged Tokens

This category includes tokenized assets, such as carbon credits, real estate, US dollars (stablecoins), or other assets that seek to retain a stable price without explicitly being pegged to a reference asset, such as RAI.

These are a rather unique type of token in that their first and foremost concern is an explicit mechanism that ties their market traded price to the target price, or price of the asset, that they track. Without this explicit mechanism, there is no reason for price to deviate from what the builder intends, and the security and utility of the token is only as strong as this mechanism.

For example, imagine a stablecoin that cannot be redeemed by anyone for $1 worth of collateral or actual USD. Such a coin would struggle to actually maintain peg, since there is no market force incentivized by arbitrage profit to sell the token when above peg or buy the token when it is below peg.

This is precisely what played out for [DAI before Maker DAO added the Price Stability Module](https://www.coindesk.com/tech/2020/09/11/no-other-option-but-more-collateral-the-short-and-long-term-fixes-for-dais-broken-peg/) (PSM) as a workaround, which in essence helped DAI retain its peg by providing 1:1 liquidity for DAI:USDC. Since USDC is directly redeemable for $1, DAI effectively “inherited” this redeemability from USDC via the PSM.

<aside>
💡 It’s extremely difficult to retain a strict peg without the option to redeem the token for the underlying pegged asset, no matter how liquid or illiquid that asset may be.

</aside>

For example, [PAXG represents tokenized gold](https://paxos.com/paxgold/), and is redeemable for physical gold. [Lofty.ai tokenizes real estate](https://www.lofty.ai/), and token holders can vote via governance to list the entire property for sale (as a normal non-blockchain property sale), thus redeeming their tokens for the market value in cash. This redeemability ensures that the market value for the token should not trade materially below the market value of the property.

Conversely, UST was not, strictly speaking, ever redeemable for 1 USD - it was simply redeemable for $1 worth of LUNA. When the total market cap of UST exceeded the total market cap of LUNA, it became impossible to redeem every UST for $1 worth of LUNA. In aggregate, UST was no longer redeemable, which created the death spiral bank run to redeem UST while still possible.

Redeemability establishes and maintains a peg, and losing redeemability can cause catastrophic depegs. Though it is the most explicit and strongest peg mechanism, it is not the **only** peg mechanism. Builders planning on launching a stable or pegged token must think very carefully about the incentive mechanisms at play, and how the market is explicitly incentivized to safely and consistently keep the token price at the target price.

We’ll discuss stablecoins further in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21).

## Governance Tokens

Governance tokens have been arguably the single most common type of token. In concept, governance tokens grant holders and ability to control the protocol, to vote on key decisions, parameters, and features that influence the protocol.

In practice, there is usually a wide gulf between how much control governance token holders can exert in theory, and how much they can exert in practice. This was perhaps most famously highlighted when [Arbitrum’s governance vote on the allocation of approximately $1bn was not approved](https://cointelegraph.com/news/arbitrum-s-first-governance-proposal-sparks-controversy-with-1b-at-stake), only for Arbitrum to reveal that at least some of the funds had already been spent.

One potential reason governance tokens have become so popular is the perception that they may represent a relatively benign token approach for legal and regulatory risk. A governance token is given away freely to users instead of sold to them for investment, and which does not provide any direct financial rewards from the protocol may or may not be a less risky token - but it certainly is a less useful and valuable one. Governance *alone* does not make a token valuable.

https://twitter.com/VitalikButerin/status/1597570120456769536?s=20

And while governance is often conflated with user ownership, the two are different concepts, both in TradFi analogs, as well as in blockchain products. For example, DAI and LUSD are both stablecoin products with a native token, MKR and LQTY respectively. Both native tokens have value accrual mechanisms to reward holders from the protocol’s revenues. Yet while MKR is also a governance token, LQTY is not - the Liquity protocol is immutable and not governed by anyone.

https://twitter.com/AriDavidPaul/status/1597571226008178689?s=20

In addition to being conflated with ownership, governance is often made out to be a strict necessity for any decentralized product or protocol. Once again, counter examples such as BTC and LQTY show this is not the case.

Community governance **can** be helpful - but it is not always so beneficial. Governance token [holders are not necessarily protected from being rugged](https://twitter.com/spreekaway/status/1682390046824091648) simply by funds being controlled by community governance.

And governance does not necessarily make your product stronger or more resilient. When the stability of the system depends on key parameters and the values of these parameters are set by governance, instead of ossified design choices or market equilibriums, the system assumes that governance voters will be rational, informed, and active participants. The problem is, most average users of complex DeFi products do not possess the knowledge required to properly run risk management of such products. The recent “CRV debt contagion” threat created by over-leveraging across some of the most popular governance-run DeFi lending protocols is an excellent example of governance jeopardizing the product, rather than benefitting it.

https://twitter.com/euler_mab/status/1687055214736457728?s=20

The reality is that governance tokens *always* **open your product to at least some risk of abuse, exploit, or sabotage. This is especially true when governance tokens are tradeable, since anyone with deep enough pockets can acquire the required number of tokens to steal funds or otherwise harm the project. While in theory, this would require purchasing 50% or more of total supply, in reality since the turnout for most governance voting is so low it would require drastically less than 50% of total supply.

In fact, one study of on-chain data found typical voter turnout at 10% or less, meaning that a malicious party would only need to control a tiny portion of the total supply to do damage.

![“Governance participation rates. Each point corresponds to an improvement proposal’s voting round.”
**Source:** **[Decentralised Finance's Unregulated Governance: Minority Rule in the Digital Wild West](https://www.researchgate.net/publication/358506121_Decentralised_Finance%27s_Unregulated_Governance_Minority_Rule_in_the_Digital_Wild_West)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87ba33d0-db08-4b12-9694-2d370121483d/Untitled.png)

“Governance participation rates. Each point corresponds to an improvement proposal’s voting round.”
**Source:** **[Decentralised Finance's Unregulated Governance: Minority Rule in the Digital Wild West](https://www.researchgate.net/publication/358506121_Decentralised_Finance%27s_Unregulated_Governance_Minority_Rule_in_the_Digital_Wild_West)**

Attacks may not always be profit motivated - a deep pocketed sovereign state could use a governance token as a weapon to censor or sabotage if need be (though there are likely more cost efficient options available to such entities).

These attacks are not just hypothetical. Multiple “governance takeover” exploits have occurred:

https://twitter.com/thegrifft/status/1683579165902077956

https://twitter.com/samczsun/status/1660012956632104960

https://twitter.com/MessariCrypto/status/1550497033991385088?s=20

https://twitter.com/Dogetoshi/status/1622088935336824833?s=20

Covenants, quorum, quadratic voting, whitelisted voting, soulbound governance tokens, and other measures can help to mitigate these risks - but they can not eliminate them.

Governance itself is a large topic, and getting into every aspect of governance is beyond the scope of this guide, though we’ll discuss DAOs and governance mechanisms much more in [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21).

That being said…

<aside>
💡 Builders should keep in mind that while potentially beneficial, governance tokens create additional room for abuses, exploits, and malicious ‘governance takeovers’, in addition to handing potential control of crucial aspects of the product to users who sometimes have drastically less domain expertise.

Despite common perception, community governance is not required to build decentralized or user owned products, and it is not always a net positive. User governance is often adopted simple because builders that it is a way, or the only way, to avoid certain regulatory risks - but this is certainly not always the case.

User governance is a subjective political decision or design objective - not a technical requirement, and often not a regulatory requirement either. Before launching a token or user governance, speak to registered legal professional.

</aside>

## Utility Tokens

Utility tokens are tokens which have a specific use case, generally within the context of a specific application or network. For example:

- ETH tokens have utility as they are required to pay gas fees in order to use the Ethereum blockchain.
- FIL tokens have utility as they are required to post as collateral to begin earning from storage deals as a storage collateral.
- BNB tokens have utility because they can optionally be used to pay discounted fees, and access other product features such as the launchpad.
- MKR tokens arguably have no utility beyond their role as a stakeholder and governance token, and anyone can use MakerDAO CDPs to mint DAI without MKR tokens.

Whether having utility makes a given token a utility token or not is subjective. Remember that these classifications of tokens are not formal, and are not mutually exclusive. The more formal distinctions issued by jurisdictions such as Singapore and Switzerland are also not mutually exclusive.

It’s entirely possible that a regulatory, or any other party, chooses to define a token that has utility as some other type of token, or as both a utility token and another type of token.

Thus, while builders have often tended to act as if launching a token with **any** degree of utility provides some regulatory cover by allowing them to call the token a utility token, this is largely a myth. Imparting utility into a token as an after thought does not necessarily reduce regulatory risk.

Nor is it likely to improve your product’s user experience. For instance, you may have immediately noticed from the Filecoin, Binance, and Maker examples above, there is often an inherent conflict between a token’s utility and its friction to user adoption.

At one extreme, largely any product could add token gating as a utility. This is a very strong form of utility - the token is literally the only way to use the product if users are required to pay with the native token or hold a certain number of tokens in order to use the product. But it also creates a great deal of friction to user adoption. Instead of just being able to use your product, users have to first deal with acquiring your token.

In a middle ground, the token **can** be used, perhaps to unlock additional features or get preferential pricing, but is not strictly required to use the product. This is slightly weaker utility, but drastically less friction.

And at the other extreme, users don’t have any need at all for the token in order to use the product (though they may still want to become stakeholders or hold tokens for reasons other than utility). Tokens have no direct utility, though friction isn’t much less than the middle ground approach.

<aside>
💡 While more token utility is a good thing in isolation, increased utility can often come at the expense of increase user frictions, and builders need to careful consider how these can be balanced to maximize long term success.

</aside>

### Common Types of Utility

The below list cover some of the most common forms of token utility, though it is not necessarily exhaustive:

- **Usage Fees**
Tokens provide utility in that they are required to **pay for** a product or service such as gas fees, an in-game currency, or product credits.
- **Access Rights (i.e. token gating)**
Tokens have utility in that they are either required to *access* an app or service at all (all-or-none), or they are required to access tiered, premium, or add-on features. This can include both access required to either *use* a product or service, or access required to **provide** a product of service (i.e. FIL for storage providers or LINK for oracle providers).

- **Discounts**
Tokens have an economic utility due to providing a discount to purchase a good or use a service. This discount could be one-time, akin to a redeemable coupon or loyalty reward. In this case, tokens are spent or burned to incur the discount, such as spending BNB tokens for reduced trading fees.

Or the discount can be perpetual, akin to a reward class or loyalty tier. In this case, purchases do not spend or burned, but instead grant a given discount for holding a certain number of tokens.
- **Social Participation**
The token possesses a social signaling utility, identifying the holder’s status, affiliation, or membership with a particular group. This is generally, though not always, a weaker form of utility as it is highly subjective.

Generally speaking, NFTs may be better suited than fungible tokens to social utility. Fungible tokens **can** retain a social utility, especially in cases where token balances are a proxy for reputation, but tradeable tokens generally do not preserve a reputation bearing property, since if reputation can be purchased, it loses at least part of its meaning.
- **Economic Participation**
The token provides economic utility, such as a share of protocol revenues or compensation for taking on risks (such as insurance coverage).

This category overlaps with aspects of stakeholder tokens - it can be thought of as the utility that stakeholder tokens can provide. That does not mean this is not legitimate utility and a use case for holding the token, but this type of utility could incur additional regulatory risk - always speak with a registered lawyer before launching a token.
- **Governance Participation**
Governance can carry a political or philosophical utility, as some people may place a value on participating in the direction and outcomes of the product and community.

This should not be mistaken for an economic value however, as mentioned earlier, empirically very little economic value is generally assigned purely to voting rights. For this reason, this is a weaker form of utility similar to social utility.

In general, builders tend to vastly overestimate the utility of governance participation, and in cases of governance tokens with high premiums to the economic value accrued to the tokens (such as UNI), this premium is best attributed to speculation on accruing future economic value (i.e. Uniswap fee switch), not governance participation for the sake of governance.

### Common Utility Misconceptions

In addition the above list of utilities, let’s set the record straight about a few token properties that builders often incorrectly label as utility:

- **Price Speculation**
The ability to trade a token and speculate on its future price is not a form of utility. Price volatility is a property every non-soulbound token and on-chain or off-chain asset in the world possesses inherently - it is not a feature of capability, it is a side effect.

The mere presence of price volatility and ability to speculate adds no value to the product or token.

- **Collateral for Loans**
The ability to borrow against a token is also not a form of utility, feature, or capability. It is an inherent property of **any** asset with a non-zero value, and if an asset has zero value, then it can’t be used as collateral anyway!

Holding a token or asset purely for the purpose of borrowing against it does not make that asset useful, unless it posses some additional utility or benefits unrelated to serving as collateral.
- **Staking Funded by Net Inflation**
Staking a token purely to earn more rewards denominated in that same token is also not a utility. This mechanism serves no purpose other than to attempt to dissuade holders from selling their tokens, but the act of minting more tokens can not create value or reward holders in aggregate.

Staking rewards paid funded by product revenues (i.e. buyback and distribute tokens), or paid directly in product revenues, make the token an appreciating or yield generating asset, which has economic utility. But, on it’s own, earning more of the same token that otherwise does nothing is not a legitimate use case or justification to own that token.
    
    > **These “staking” mechanisms (that do not do anything at all except pay users more coins for staking) are giving away equity for nothing except to reduce potential sellers’ liquidity… If we are being truly honest about this proposal, what it really means is “lets pay existing holders for not selling while the founder/investor/contributor unlocks happen, and also so we can fake some utility before any is actually built”… Getting more supply onto the market, bribing users to not sell, or providing “fake utility” are not credible goals for a staking program.
    Source: [ApeCoin & the death of staking](https://cobie.substack.com/p/apecoin-and-the-death-of-staking)**
    > 

# Chapter Summary

- Regulatory bodies in Switzerland and Singapore have similar guidance on token classes for payment, utility and securities/assets, though these classes are not mutually exclusive
- Unofficial industry classifications of tokens do not assume tokens are necessarily fungible tokens rather than non-fungible tokens, many cases, such as reputation, governance, pegged, and more can make use of NFTs or FTs
- It is generally unwise to launch a non-stablecoin token meant to function as a medium of exchange (unless within a very specific economy, such as an in-game currency)
- It’s extremely difficult to retain a strict peg without the option to redeem the token for the underlying pegged asset, no matter how liquid or illiquid that asset may be
- Governance tokens create additional room for abuses, exploits, and malicious ‘governance takeovers’, in addition to handing potential control of crucial aspects of the product to users who sometimes have drastically less domain expertise
- Community governance is not required to build decentralized or user owned products, it is a subjective political decision or design objective - not a technical requirement, and often not a regulatory requirement either - always speak to a registered legal professional before launching a token

# Additional Resources

- Blog, [Designing Internet-Native Economies: A Guide to Crypto Tokens](https://a16zcrypto.com/posts/article/a-taxonomy-of-tokens-distinctions-with-a-difference/)
- Blog, [New Models for Utility Tokens](https://multicoin.capital/2018/02/13/new-models-utility-tokens/)
- Blog, [Thoughts on Tokens](https://news.earn.com/thoughts-on-tokens-436109aabcbe)
- Blog, [[Social] Status as a Service](https://www.eugenewei.com/blog/2019/2/19/status-as-a-service)
- Blog, [DAO governance attacks, and how to avoid them](https://a16zcrypto.com/posts/article/dao-governance-attacks-and-how-to-avoid-them/)
- Blog, [On-Chain Vote Buying and the Rise of Dark DAOs](https://hackingdistributed.com/2018/07/02/on-chain-vote-buying/)
- Blog, [Designing Governance Tokens](https://variant.fund/articles/designing-governance-tokens/)
- Blog, [Governance Minimization](https://www.paradigm.xyz/2020/10/870#what-governance-minimization-is-not)
- Paper, [RAI Whitepaper - Governance Minimization Guide](https://docs.reflexer.finance/ungovernance/governance-minimization-guide)
- Blog, [Moving beyond coin voting governance](https://vitalik.ca/general/2021/08/16/voting3.html)
- Blog, [Endgame: Proof of Governance](https://dba.mirror.xyz/UTPfxWe65dYrUu_RJX-5VkAJypFRyw3AZh6m0dRXYZk)
- Paper, [FINMA (Switzerland): Guidelines for enquiries regarding the regulatory framework for initial coin offerings (ICOs)](https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/1bewilligung/fintech/wegleitung-ico.pdf?sc_lang=en&hash=83EE49D77DA54DD079F314D9EDCBDC3D)
- Paper, [MAS (Singapore): Guide to Digital Token Offerings](https://www.mas.gov.sg/regulation/guidelines/a-guide-to-digital-token-offerings)
- Paper, [Security Token Offerings - The Shape of Regulation Across Asia-Pacific](https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2020/11/security-token-offerings-regulation-across-apac-pacific.pdf)
- Paper, [HomebaseDAO Whitepaper -Security Token Offerings](https://docs.homebasedao.io/whitepaper/security-token-offerings)
- Slides, [Crypto Token Economy Design for Disruptive BM](https://site.ieee.org/bcsummitkorea-2018/files/2018/06/D1_SKT_Crypto-Token-Economy-Design-for-Disruptive-BM_Jongseung-Kim.pdf)
- Blog, [TCR Design Flaws: Why Blockchain Needs Reputation](https://blog.relevant.community/tcr-design-flaws-why-blockchain-needs-reputation-c5771d97b210)
- Blog, [A Novel Framework for Reputation-Based Systems](https://future.com/reputation-based-systems/)
- Paper, [Tokenomics and blockchain tokens: A design-oriented morphological framework](https://www.sciencedirect.com/science/article/pii/S2096720922000094#sec7)

# 1.6 A Must-Know History of Tokenomics

# Introduction

Every few years, a new wave of blockchain experiments and innovations find their way to market.

![crypto history to date.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2217fb9c-d83c-417b-9ced-d60765618301/crypto_history_to_date.jpeg)

Sometimes these usher in new bull markets. Sometimes they are quick speculative bubbles that don’t last. And sometimes, albeit very rarely, they change the game forever.

In this chapter, we’ll explore the history of tokenomics that every blockchain founder should know. 

<aside>
💡 Learn your history. Borrow what worked. Avoid what didn’t.

</aside>

> **Those who cannot remember the past are condemned to repeat it.
- George Santayan**
> 

> **Good artists copy; great artists steal.
- Pablo Picaso**
> 

# Proof-of-Work Mining, Jan 2009

It all began with Bitcoin mining rewards - the first-ever case of aligning incentives via blockchain. Distributing block rewards to miners incentivizes hash power to join the network, leading to more network security, creating more network value, enticing more hash power… and so on.

Yet even Bitcoin’s relatively simple incentives model is not free from internal debate and controversy. It remains an open question what will happen to Bitcoin once block rewards expire (or become vanishingly small), and the only source of revenue for miners becomes transaction fees.

https://twitter.com/Justin_Bons/status/1628117102119862273?s=20

Even Bitcoin core developers disagree on what Bitcoin will need to do, if anything, to mitigate this problem. Tail emissions are one potential solution, but sacrifice the “21 million” narrative. High miner fees are another theoretical solution, but if Bitcoin remains “digital gold” with no additional use cases built on top of it, it is hard to see how sufficient activity will materialize (a problem the lighting network does not directly address since transactions on the lightning network do not pay gas fees to Bitcoin miners except when channels are opened or closed).

Another interesting possibility is for Bitcoin L2s to use Bitcoin as the core settlement layer for extended use cases that require general smart contracts logic and global state knowledge. Fees and block rewards on these L2s could inherently act as an extension of block rewards for Bitcoin miners without changing Bitcoin’s code or total supply.

Whichever argument you personally side with, the future of Bitcoin remains one of the most significant open questions about incentives and economic security in all of blockchain.

**Additional Resources**

- Paper, [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoinwhitepaper.co/)
- Paper, [On the Instability of Bitcoin Without the Block Reward](https://www.cs.princeton.edu/~arvindn/publications/mining_CCS.pdf)
- Blog, [Surprisingly, Tail Emission Is Not Inflationary](https://petertodd.org/2022/surprisingly-tail-emission-is-not-inflationary)
- Paper, [Stacks: A Bitcoin Layer for Smart Contracts](https://stx.is/nakamoto)
- Blog, [What Will Happen After All Bitcoin Are Mined?](https://river.com/learn/what-will-happen-after-all-bitcoin-mined/)
- Thread, [Monero Tail Emissions Announcement](https://twitter.com/monero/status/1521841252429451265?s=20&t=JE9Xsz2kwRNZhFfklI-8JQ)
- Blog, [The Bitcoin Tail Emissions Debate](https://thebitcoinmanual.com/articles/btc-tail-emissions-debate/)
- Blog, [Understanding Bitcoin’s Fee-Based Security](https://braiins.com/blog/bitcoin-fees-security-threats)

# Proof-of-Stake Consensus, Aug 2012

Proof-of-Stake consensus has existed as an alternative to Proof-of-Work long, long before “The Merge” (Ethereum 2.0), beginning with the launch of [Peercoin](https://en.wikipedia.org/wiki/Peercoin) in 2012.

Obviously economic risks and exploit vectors differ in PoS vs PoW, though the (intended) incentives remain roughly the same - reward the act of securing the network in order to promote greater network security. While PoW security is a direct product of hash power, which itself is an indirect product of economic incentives, PoS security is a direct function of the cost it would take to acquire a sufficient stake to gain control of the network relative to the potential benefit of a malicious attack.

Though staking was originally introduced in the context of a consensus mechanism (PoS), the term “staking” has since become more generalized to simply mean “locking up tokens” even when doing so does not provide any specific value or purpose. This form of non-Proof-of-Stake rewards are discussed later in this chapter in “Staking Rewards (Non-PoS)”, and we’ll also discuss the specifics of “The Merge” later this chapter as well.

**Additional Resources**

- YouTube, [A Tale of Two Protocol Designs](https://www.youtube.com/watch?v=Fk7Tc99orS0&list=PLa_a2TnKITJ9YiVWcfJ7TDjTvYL4TXBIQ&index=4) (PoW vs PoS)
- Paper, [Staking Pools on Blockchains](https://arxiv.org/pdf/2203.05838.pdf)
- Paper, [PPCoin: Peer-to-Peer Crypto-Currency with Proof-of-Stake](https://whitepaperdatabase.com/peercoin-ppc-whitepaper/)

# Initial Coin Offerings (ICOs), Jul 2013

Contrary to popular opinion, Ethereum was **not** the very first ICO. The first ICO was Mastercoin (now called Omni), though the terminology “ICO” did not exist at the time.

Mastercoin’s ICO was a month-long raise in July 2013 during which anyone could send bitcoin to the Mastercoin Exodus Bitcoin address to fund the development of the protocol. The sale raised about 5,120 bitcoin, which was worth approximately $500,000 at the time.

While Mastercoin (now Omni) has not gained adoption, it set the precedent for fundraising, and Ethereum followed suit with its ICO in 2014. Eventually, this led to the ICO craze of 2017 and 2018, during which more than [$28bn was raised](https://elementus.io/token-sales-history).

Many of these offerings would be unthinkable by modern standards - with teams raising tens or hundreds of millions with nothing but a website and whitepaper, selling 100% of the token supply all at once upfront, no vesting period for core team members, and nothing to prevent the team from immediately abandoning the project and keeping the treasury for themselves.

It’s no wonder that a report by [E&Y on 2017 ICOs](https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/news/2018/10/ey-ico-research-web-oct-17-2018.pdf) found 86% of projects were below their ICO price just a year later, with 30% having collapsed to virtually zero, and a 66% loss if an investor had invested in a general index of 2017 ICOs. The Top 10 2017 ICOs were responsible for a whopping “99% of the net gain” for investors.

A separate analysis of ICO data found that as much as [80% of ICOs were scams](https://web.archive.org/web/20180716094634/https://medium.com/satis-group/ico-quality-development-trading-e4fef28df04f).

While the industry still needs to mature, it has changed a lot since 2014 - 2017. The first wave of retail investors learned painful lessons, institutional adoption has grown, and regulators have begun watching with more scrutiny.

ICOs are no longer commonplace and have given way to private sales, VC rounds, NFT sales, and IEOs, though it is [possible to conduct a regulatory-compliant ICO](https://cointelegraph.com/news/us-sec-approves-blockstack-token-offering-under-regulation-a).

<aside>
⚠️ As a builder, keep in mind that any tokenomics models inspired by projects that launched in ICOs (especially 2018 or earlier) will likely need significant changes to be viable by modern standards for incentive alignment, value capture, value accrual, vesting, allocation, emissions, compliance, and more.

</aside>

**Additional Resources**

- Paper, [MasterCoin - A Second-Generation Protocol on the Bitcoin Blockchain for Creating and Trading New Currencies](https://github.com/bitsblocks/mastercoin-whitepaper/blob/master/index.md)
- Paper, [Digital Tulips? Returns to Investors in Initial Coin Offerings](https://deliverypdf.ssrn.com/delivery.php?ID=742110126119070020107067104097029127062041020052054087069122090029067090031112107088102031125025020116062125088070092120118088057017017032053110084073119124003102009061056073029104010080099112074005013087096021087124121030099021082105030102127123103&EXT=pdf&INDEX=TRUE)
- Dashboard, [Token Sales History](https://www.elementus.io/token-sales-history)

# Airdops, Mar 2014

The first ever known instance of an airdrop was Auroracoin - a cryptocurrency launched in early 2014 in Iceland. The developers used Iceland’s national ID database to distribute 50% of the total supply to population for free.

Airdrops later spiked in popularity during the ICO craze as a way to grab attention, and were often used to reward recipients for marketing and hyping tokens ahead of the sale. Part of the popularity of airdrops can also be attributed to builders at the time mistakenly believing that tokens given away for free carried no regulatory risk, unlike tokens that were sold - but this is not necessarily the case.

The SEC can and has come after projects for aidropping tokens when those airdrops are essentially rewards for work or services provided, such as marketing services.

https://twitter.com/Orlando_btc/status/1575462407245385730?s=20

Following the 2017/2018 ICO frenzy, airdrops for large portions of the token supply have fallen out of favor.

This is partially to do with evolutions in market standards for token allocations and distribution - what once would have been distributed via airdrop is now often used for reward emissions, such as rewarding staking, liquidity, TVL, or product usage.

But it’s also due to the fact that analyses of airdrops have repeatedly shown that they largely do not achieve their stated goals of decentralizing token distribution or attracting initial users. In reality, airdrops are largely simply farmed and then dumped, so tokens end up in the hands of a few concentrated parties anyway, and recipients are often not converted into users that remain active following the airdrop (low retention).

![Source: [blur_dumping](https://dune.com/queries/2006659/3320624)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/516384b3-a714-40c7-a207-5c6a1391607a/blur_aridrop.png)

Source: [blur_dumping](https://dune.com/queries/2006659/3320624)

Much of the inefficiency of airdrops is the fact that they are relatively easy to game or exploit. Sybil attacks are too easy to perform - and have virtually no opportunity cost to exploring the aidrop.

https://twitter.com/Auri_0x/status/1584469757931057153?s=20

<aside>
💡 We’ll discuss potential solutions and creative ways to mitigate the risks of airdrops, to make them more efficient when we discuss Supply Policy in Chapter 2.5

</aside>

**Additional Resources**

- Wiki, [Auroracoin](https://en.wikipedia.org/wiki/Auroracoin)
- Dashboadrd, [UNI Airdroppers - Where are they Now?](https://dune.com/jhackworth/uniswap-airdroppers)
- Dashboard, [Messari: Airdrops](https://dune.com/messari/Messari:-Airdrops)
- Dashboard, [Understanding the Impact of Airdrops on NFT Marketplace Performance](https://dune.com/jhackworth/olxb)
- Paper, [Airdrops: “Free” Tokens Are Not Free From Regulatory Compliance](https://repository.law.miami.edu/cgi/viewcontent.cgi?article=1360&context=umblr)
- Blog, [We need to rethink Airdrops next cycle…](https://medium.com/hashed-official/we-need-to-rethink-airdrops-next-cycle-730706f963a7)
- Blog, [What Crypto Founders Can Learn from Blur’s Token Airdrop](https://archive.ph/Bnvnu)

# Computations, not (Just) Currencies, Aug 2014

While Bitcoin revolutionized **currency**, the original Ethereum whitepaper by Vitalik Buterin envisioned generalized Bitcoin’s state transition mechanism to enable generalized applications and computation - a world computer.

Early experiments on Bitcoin such as Mastercoin’s “colored coins” explored minting new currencies, but Vitalik envisioned extending blockchain’s value proposition beyond simply being technology for a monetary currency unit, medium of exchange, and/or store of value.

https://twitter.com/LogarithmicRex/status/1545593124839374848?s=20

Ethereum’s original tokenomics were strikingly similar to Bitcoin’s (both PoW, both rewarding miners with fees and block rewards) with one notable exception - Ethereum has never had a maximum supply, even prior to The Merge and EIP-1559. The closest ETH has ever come to having a maximum supply was an EIP Vitalik posted on April 1st, 2018- make of that what you will.

**Additional Resources**

- Paper, [Ethereum: A Next-Generation Smart Contract and Decentralized Application Platform](https://ethereum.org/669c9e2e2027310b6b3cdce6e1c52962/Ethereum_Whitepaper_-_Buterin_2014.pdf)
- EIP (Closed), [Meta: cap total ether supply at ~120 million](https://github.com/ethereum/EIPs/issues/960)

# Stablecoins, Oct 2014

The first stablecoin to ever be issued was not DAI or USDC, in fact, it wasn’t even issued on Ethereum. “Realcoin” issued the stablecoins in existence on the Bitcoin blockchain via Mastercoin (Omni) in late 2014, before rebranding to what it’s now known as today: Tether.

Nine years later in 2023, Tether announced it was ending support of USDT on Bitcoin (via Omni), citing a lack of demand. But on chains such as Ethereum, stablecoins Tether and other stablecoins have exploded in popularity and market cap during that time.

Each USDT, and later centralized stablecoins such as UDSC, are (in theory) backed by fiat USD and directly redeemable at a 1:1 ratio for actual USD. In reality, there is a wide range of holdings that actually back centralized, redeemable stablecoins, and doubts have been raised about the lack of audits or quality of assets held by some tokens.

For instance, Tether has been historically backed by a relatively large portion of [commercial paper](https://www.investopedia.com/terms/c/commercialpaper.asp) - a highly liquid, relatively low risk form of short term debt. While in **most** market conditions these assets retain their value, the risk of default does exist, meaning this commercial paper could become worthless in the event of bankruptcy. A financial crisis, such as in 2018, could result in widespread defaults on commercial paper meaning that while Tether is fully backed in theory by USD, in practice the truth is a bit more complicated.

![Source: [Crypto Boom Poses New Challenges to Financial Stability](https://www.imf.org/en/Blogs/Articles/2021/10/01/blog-gfsr-ch2-crypto-boom-poses-new-challenges-to-financial-stability)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75ef9aa5-f0ae-4417-b57c-3e090646899c/Untitled.png)

Source: [Crypto Boom Poses New Challenges to Financial Stability](https://www.imf.org/en/Blogs/Articles/2021/10/01/blog-gfsr-ch2-crypto-boom-poses-new-challenges-to-financial-stability)

While Tether was the first stablecoin, MakerDAO’s DAI was the first attempt at a decentralized stablecoin that is not actually backed by Fiat USD, but backed by other collateral assets.

DAI was later followed by algorithmic stablecoins, including the now infamous IRON and UST Terra stablecoins, which attempted to push the envelope even further by offering undercollateralized stablecoins - a dubious concept as history has shown.

The issue is that overcollateralized stables, whether collateralized by fiat such as USDC or collateralized by crypto such as DAI or LUSD, have enough collateral such that a bank run can not exhaust all the existing collateral.

Exceptions do apply when collateral prices collapse so quickly that liquidations can not happen at prices above the value of the assets backed by collateral - this occurred once before for MKR on March 12th 2020, resulting in auctioning MKR tokens to re-collateralize the protocol.

On the other hand, partially collateralized stables are always exposed to bank runs because a bank run can exhaust all collateral, leaving some holders with tokens that are not backed by, or redeemable for, anything of value. This is exacerbated by collateral prices collapsing very quickly - while neither approach is risk free, partially collateralized stables are still more fragile in these circumstances.

> **Partially collateralized stablecoins have repeatedly failed over and over. They cannot solve the fundamental problem of bank runs when the peg is under pressure.
- Nik Kunkel, former head of backend services for MakerDAO**
> 

Though modern stablecoins vary significantly across a number of factors including redemption mechanisms, interest rates, and other design parameters, two primary aspects can be used to distinguish between fundamentally different kinds of stablecoins:

- How do they retain their peg or target price?
- How are they backed to prevent and/or recover from bank runs?

**Classifying Popular Stablecoins (Not an Exhaustive List)**

| Stablecoin | How It Retains Peg or Target | How It’s Backed | Market cap |
| --- | --- | --- | --- |
| USDT | Redeemable for $1 fiat USD | Fully collateralized by fiat cash equivalents | $83.5bn |
| USDC | Redeemable for $1 fiat USD | Fully collateralized by fiat cash equivalents | $26.2bn |
| DAI | Liquidity pool with USDC (PSM) | Over collateralized by cryptoassets | $4.0bn |
| BUSD | Redeemable for $1 fiat USD | Fully collateralized by fiat cash equivalents | $3.4bn |
| FRAX | Algorithmically adjusted supply | Partially collateralized by USDC, moving to fully collateralized by liquid staked collateral  | $800mm |
| LUSD | Redeemable for $1 of collateral | Over collateralized by ETH | $300mm |
| MIM | Redeemable for $1 of collateral | Over collateralized by cryptoassets | $54mm |
| AMPL | Algorithmically adjusted supply | Non-collateralized, algorithmic rebases | $25mm |
| RAI | Redeemable for algorithmically adjusted rate of collateral | Over collateralized by ETH | $7mm |
| UST Terra | Mint and burn collateral asset | Partially collateralized by LUNA | - |

The list above also includes more recent experiments such as RAI and AMPL which do not attempt to peg to one dollar, but instead track a given target price. Unlike, AMPL, which unsustainably requires an ever increasing marketcap to achieve its purpose of tracking inflation, RAI’s mechanism has its downsides, but is sustainable. (We’ll talk about AMPL more later this chapter in the context of rebase tokens).

<aside>
💡 While RAI is still a small and experimental project that may fail, every builder should be familiar with it due to its simplicity in using feedback mechanisms as incentives to maintain a stable price.

</aside>

It remains exceptionally difficult to retain a stable peg at large scale without a redemption mechanism. DAI itself struggled to maintain its peg and only stabilized after introducing the ‘Price Stability Module’, essentially a liquidity pool for DAI<>USDC, effectively inheriting USDC’s redemption mechanism at the cost of relying on a centralized stablecoin. DAI’s large dependence on USDC has called its degree of decentralization into serious question.

In fact, Maker’s founder has even recently voiced the concern that Maker has “no choice but to prepare for free float DAI” (i.e. abandon the peg).

> **Attempts to guarantee a peg to 1 USD without having access to USD linked RWA collateral only ends in even worse misery and disaster, such as the Terra collapse. So our only choice is to prepare and do everything we possibly can to make it a transition [to a floating price].
- Rune Christensen, [The Path of Compliance and the Path of Decentralization: Why Maker Has No Choice but to Prepare to Free Float Dai](https://forum.makerdao.com/t/the-path-of-compliance-and-the-path-of-decentralization-why-maker-has-no-choice-but-to-prepare-to-free-float-dai/17466)**
> 

The strongest peg mechanism (by far) is redemption - because it creates profitable pure arbitrage opportunities whenever the market price differs from the peg.

The struggle to create a stablecoin that achieves decentralization, price stability (keeps it peg), and capital efficiency (i.e. doesn’t need to be over collateralized), is known as The Stablecoin Trilemma. Stablecoins can optimize any two of the three features (any side of the triangle below), but unlocking all three aspects remains an elusive target.

![Source: [The Stablecoin Trilemma](https://stablecoins.wtf/resources/the-stablecoin-trillema)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91521f47-54b9-4534-abff-dca3922ffd76/Untitled.png)

Source: [The Stablecoin Trilemma](https://stablecoins.wtf/resources/the-stablecoin-trillema)

**Additional Resources**

- Blog, [Two Thought Experiments to Evaluate Automated Stablecoins](https://vitalik.ca/general/2022/05/25/stable.html)
- Report, [Reflexer Finance(RAI): Non-pegged Overcollateral Decentralized Stablecoin](https://mintventures.fund/reflexer-finance-rai-non-pegged-over-collateral-decentralized-stablecoin.pdf)
- YouTube, [RAI: The First Stablecoin](https://www.youtube.com/watch?v=wyr297JjEGY)
- Blog, [The Stablecoin Trilemma: Price Stability, Capital Efficiency, and Decentralization](https://stablecoins.wtf/resources/the-stablecoin-trillema)
- Website, [USDC: Latest Independent Accountant Report](https://www.circle.com/en/transparency)
- Website, [Tether: Latest Independent Accountant Report](https://tether.to/en/transparency/#reports)
- Blog, [Governance Poll: Accelerate the [MakerDAO] Peg Stability Module Launch](https://blog.makerdao.com/governance-polls-november-23-2020/)
- Blog, [Reserve’s Analysis of the MakerDAO Protocol](https://blog.reserve.org/our-analysis-of-the-makerdao-protocol-4a9872c1a824)
- Blog, [The End of a Stablecoin — The Case of NuBits](https://blog.reserve.org/the-end-of-a-stablecoin-the-case-of-nubits-dd1f0fb427a9)
- Blog, [The Market Collapse of March 12-13, 2020: How It Impacted MakerDAO](https://blog.makerdao.com/the-market-collapse-of-march-12-2020-how-it-impacted-makerdao/)
- Article, [After the Collapse of Terra's UST, What's Next for Algorithmic Stablecoins?](https://decrypt.co/100104/after-collapse-terra-ust-next-algorithmic-stablecoins)
- Article, [Iron Finance Bank Run Stings Investors — A Lesson for All Stablecoins?](https://cointelegraph.com/news/iron-finance-bank-run-stings-investors-a-lesson-for-all-stablecoins)
- Blog, [Stablecoins, Stability, and Financial Inclusion](https://a16zcrypto.com/posts/article/stablecoins-stability-and-financial-inclusion/)
- Blog, [On Price Stability of Liquity](https://www.liquity.org/blog/on-price-stability-of-liquity)
- Paper, [While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins](https://arxiv.org/abs/2004.01304)
- Blog, [The Rise of MakerDAO: A Personal Journey](https://unchainedcrypto.com/the-rise-of-makerdao-a-personal-journey/)
- Blog, [Zero to One Billion Dai: Five Years of Growth for MakerDAO](https://blog.makerdao.com/zero-to-one-billion-dai-five-years-of-growth-for-makerdao/)

# Web3 Games & Play to Earn, 2015

Before Axie Infinity and even before CryptoKitties, even before the first game on Ethereum at all, the first example of a game on the blockchain was Spells of Genesis in early 2015, a trading card game that issued cards as tokens on the Bitcoin blockchain using the Counterparty protocol.

The first game on Ethereum arrived in October 2015, when the game Etheria launched only three months after Ethereum itself.

> **Ξtheria is a virtual world in which players can own tiles, farm them for blocks, and build things. The entire state of the world is held in and all player actions are made through the decentralized, trustless Ethereum blockchain.
Source: [What is Etheria?](https://etheria.world/whatis.html)**
> 

Since then, blockchain games have (intermittently) exploded in popularity, with CryptoKitties growing large enough to cause significant network congestion in 2017 and Axie Infinity reaching a high of 2.7mm daily active users in 2021.

But there’s an important distinction between early games like Etheria and CryptoKitties, and “play-to-earn” games like Axie Infinity. While players could still ‘earn’ by selling rare collectibles in Etheria and CryptoKitties they were not “play-to-earn” in the way Axie Infinity popularized, with payers directly earning fungible tokens to play the game.

Early experiments with this “play-to-earn” mechanic help explain why games like Axie Infinity rose so quickly, and why it then lost more than 50% of active players and the AXS token fell more than 95% of its value.

The reason is relatively simple: players came to earn token emissions, emissions grew as more players arrived, eventually player growth slowed but emissions continued, the excess supply put downward pressure on token price reducing the value of players rewards, and more players left since rewards declined (and they weren’t playing the game for fun).

A death spiral ensued: as more players left due to falling token prices and liquidated their tokens, the price fell further, leading more players leaving… and so on.

https://twitter.com/VaderResearch/status/1513804131374272517?s=20

While the cause of Axie Infinty’s collapse is relatively simply to understand, the solution to attracting players while avoiding this type of outcome is less straightforward.

Entire books can and have been written on the topic of gaming and game economies alone, but the core challenge for builders remains how to balance supply and demand over time, and build sustainable in-game economies that can survive fluctuations in the number of players.

Yet these aspects are in fundamental conflict with the inherent desires of gamers:

> **Economic progression vs sustainability:** The player goal of economic progression is at odds with the developer goal of economic sustainability.

**Content reward (i.e. loot drops) vs trading:** The player goal of experiencing rare loot drops is at odds with the player goal of tradability.

**Primary revenue vs secondary trading monetisation:** The developer goal of selling content to players is at odds with the player goal of trading content with each other.

**Economic sustainability vs free player experience:** The developer goal of preserving economic sustainability is at odds with the developer goal of creating a positive player experience.

Source: [Unavoidable Cursed Design Problems in Web3 Economies: Challenges and Mitigations](https://web3games.substack.com/p/unavoidable-cursed-design-problems)
> 

Using a token that serves as both an in-game asset, and a token that enables user ownership or value accrual is incredibly difficult to achieve. Set aside blockchain for a moment, and consider how difficult it is to even manage an well balanced in-game economy even for a large scale game without a token.

![Source: [EVE Online Monthly Economic Report - July 2023](https://www.eveonline.com/news/view/monthly-economic-report-july-2023)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/915985f2-8124-43da-b30f-165dc056d48a/Untitled.png)

Source: [EVE Online Monthly Economic Report - July 2023](https://www.eveonline.com/news/view/monthly-economic-report-july-2023)

As you can begin to see from the above report from EVE Online’s in-game currency ISK, designing a well balanced in-game currency is hard enough. (Designing Web2 game economies are essentially an exercise in tokenomics without the blockchain). Adding on the additional complexities of a fungible Web3 token on top of that is often not worth the extra effort.

Credible voices in the industry have raised legitimate doubts about whether fungible tokens make sense at all for most games.

https://twitter.com/VaderResearch/status/1661684724832534530?s=20

Rather than launching fungible tokens, a more viable path for Web3 games may be to lean into building games that people enjoy playing, and monetizing customizable NFTs and skins or resources that unlock new experiences or enable new levels of gameplay. Collectible NFTs can also be ways to monetize special experiences and content outside of the game itself, as [“53% of time with game content is spent NOT playing the game, but engaging with it in other ways”](https://twitter.com/0xKepler/status/1623051489030840327).

Trading card games like Skyweaver achieve this form on monetization well - with cards represented by NFTs that serve both a utility in the game, and as a social collectible, much in the same way physical cards are monetized in games such as Magic the Gathering.

Crossover partnerships between development studios can enable NFTs that unlock benefits across multiple games, creating even more value and utility, similar to the wide variety of crossover IP skins available in games like Fortnite.

> **By rewarding players with NFTs instead of FTs, games can move the player focus from monetary rewards to in-game utility… NFTs resemble resources while FTs act like currencies. Resources have a value in themselves, while currencies are the bridges between resources. Therefore, games tend to have more resources than currencies.
Source: [A Road forward for Web3 Gaming](https://medium.com/@0xKepler/a-road-forward-for-web3-gaming-e70d82dd19e3)**
> 

https://twitter.com/sal_coin/status/1575969323339890703?s=20

Instead of charging players to play, or paying them to do so, building a fun game with a robust in-game economy that naturally encourages trading between players offers another monetization option.

![“Constantly releasing newly purchasable content/assets would no longer be the only way to monetize a successful game—collecting royalties from a high velocity economy might just do that. This may end up beneficial for both the studios and the players.”
Source: [Crypto Gaming: A Most Practical Thesis](https://medium.com/collab-currency/crypto-gaming-a-most-practical-thesis-ec4f55f53408)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5ff5b1a-dd62-4b26-b04a-f89c7ef3e0c2/Untitled.png)

“Constantly releasing newly purchasable content/assets would no longer be the only way to monetize a successful game—collecting royalties from a high velocity economy might just do that. This may end up beneficial for both the studios and the players.”
Source: [Crypto Gaming: A Most Practical Thesis](https://medium.com/collab-currency/crypto-gaming-a-most-practical-thesis-ec4f55f53408)

It’s no coincidence that the single largest sink for EVE Online’s in-game currency, ISK, is transaction taxes. This can potentially translate well to Web3 games when users are trading in non-native monetary units such as ETH or stablecoins, as the taxes represent direct revenue, or if players are trading with in-game currency that is minted at a cost, as the taxes create a need to continually replenish the currency over time.

But this still leaves the challenge of how to attract users to overcome the bootstrapping problem that affects multiplayer games in particular (i.e. the game is no fun if no one else is playing it). The common failure pattern across early attempts to attract players via play-to-earn rewards has been to distribute rewards to all players regardless of their value contributed to the game (quantity of players vs quality) and to accelerate rewards as the player base grows instead of reign in inflation as critical mass is reached. Both of these factors create ideal conditions for hyperinflationary death spirals to develop.

> **The primary issue with play-to-earn as currently implemented is the efficiency of value distribution, in the sense of aligned rewards over total rewards. Broadly, the ideal mechanism to reward early community builders would reward only actions that make the game more enjoyable for all, only when they are needed to build critical mass, and only for ongoing contributions.
Source: [Token Design for Serious People](https://jumpcrypto.com/writing/token-design-for-serious-people/)**
> 

One thing seems relatively certain, particularly with the rise of more sophisticated AI agents: play-to-earn mechanisms like Axie Infinity are not the likely future for Web3 gaming. Rewards will simply be farmed by bots and mercenaries, who won’t continue playing or spend anything on game content once rewards dry up.

Web3 games will have to find other ways to attract and monetize players. At the end of the day, just as good tokenomics can’t save a bad product, they can’t save a game that no one wants to play either.

https://twitter.com/DangerWillRobin/status/1628957681712001024?s=20

**Additional Resources**

- Book, [Virtual Economies: Design and Analysis](https://www.amazon.com/Virtual-Economies-Design-Analysis-Information/dp/0262535068)
- Blog, [Solutions and challenges in building sustainable play-and-earn economies](https://web3games.substack.com/p/solutions-and-challenges-in-building)
- Blog, [Opportunities and challenges of using blockchain in games (2023)](https://web3games.substack.com/p/opportunities-and-challenges-of-using)
- **Thread, [“I can already trade CS:GO skins on Steam, what's the point of NFTs in GAMING?”](https://twitter.com/VaderResearch/status/1621116674727632896)**
- Blog, [Axie Infinity Economy Proposal](https://defivader.medium.com/axie-infinity-economy-proposal-5b040086d65e)
- Article, [How To Build A Smart Game Economy](https://techcrunch.com/2015/08/05/how-to-build-a-smart-game-economy)
- Thread, [“P2E economics should learn from EM economies, not DeFi”](https://twitter.com/DermanCapital/status/1531794747265785858?s=20)
- Thread, [“Why Play to Earn Games Crash?”](https://twitter.com/VaderResearch/status/1513804131374272517)
- Blog, [Why STEPN’s Collapse Is Inevitable?](https://defivader.medium.com/why-stepns-collapse-is-inevitable-5259a6584a98)
- YouTube, [Lessons Learned from Building Pegaxy](https://www.youtube.com/watch?v=rA19ym02cmU)
- Website, [EVE Online Monthly Economic Reports](https://www.eveonline.com/news/t/monthly-economic-reports)
- Book, [Empires of EVE: A History of the Great Wars of EVE Online](https://www.amazon.com/Empires-EVE-History-Great-Online/dp/0990972402)
- Article, [To infinity and back: Inside Axie’s disastrous year](https://restofworld.org/2022/axie-infinity-hack/)
- Blog, [Crypto Gaming: A Most Practical Thesis](https://medium.com/collab-currency/crypto-gaming-a-most-practical-thesis-ec4f55f53408)
- Article, [Workers in the Global South are making a living playing the blockchain game Axie Infinity](https://restofworld.org/2021/axie-infinity/)
- Blog, [Metanomics — Building The Economy Of The Metaverse](https://medium.com/@theo/metanomics-building-the-economy-of-the-metaverse-4b7b73f60c9f)
- Blog, [A Road forward for Web3 Gaming: 5 Theses on incorporating crypto into games](https://medium.com/@0xKepler/a-road-forward-for-web3-gaming-e70d82dd19e3)
- Blog, [Unavoidable cursed design problems in web3 economies: challenges and mitigations](https://web3games.substack.com/p/unavoidable-cursed-design-problems)
- Slides, [The Analysis of Economic System in Axie Infinity](https://drive.google.com/file/d/1g4RN-dQpd0y3UJOQD6M4uC5AVkLwdv0B/view)
- Thread, [Web3 Gaming Manifesto - The History of Gaming and its Web3 Future](https://twitter.com/sal_coin/status/1575969083492810772)
- Book, [Game Mechanics: Advanced Game Design](https://www.amazon.com/Game-Mechanics-Advanced-Design-Voices-ebook/dp/B008CG8E8Y)
- Book (Free), [Engineering Emergence: Applied Theory for Game Design](https://dare.uva.nl/search?identifier=40b1a42a-4291-48a3-80a1-c85dfe927f50)
- Book, [Advanced Game Design: A Systems Approach](https://www.amazon.com/Advanced-Game-Design-Systems-Approach-ebook/dp/B076YD21JW)

# NFTs, 2015

While early experiments with Colored Coins on Bitcoin laid some of the foundations for NFTs, the earliest cases of NFTs on Bitcoin and Ethereum both arrived in 2015, and both in the context of representing non-fungible in-game assets for the trading card game Spells of Genesis and virtual world game Etheria.

The fact that Spells of Genesis predates Etheria means that contrary to popular opinion, NFTs were actually first created on Bitcoin - and they didn’t end with Spells of Genesis trading cards. Rare Pepes on Bitcoin became popular in 2016, and also used the Counterparty protocol to issue the tokens on Bitcoin (Counterparty was an early protocol that aimed to be a layer on top of Bitcoin to make it compatible with Solidity smart contracts).

https://twitter.com/muneeb/status/1552987191302918144?s=20&t=v2T1RQCDQdcOxn-2D5iMKw

In 2017, NFT projects like CryptoPunks, and of course CryptoKitties, went a long way to cementing NFTs as a useful alternative to fungible tokens.

It’s no coincidence that NFTs, from the very beginning, often appear in a gaming context, and any NFT builders can draw inferences from how NFTs are used in games - a context where they arguably have much more utility when compared to the average non-gaming related NFT project.

Purely from a revenue-maximizing perspective, it’s rational behavior that NFT artists have launched multiple collections often even before fulfilling any of the “roadmap” or “utility” promised for earlier collections.

![Source: [NFTs and a thousand true fans](https://a16zcrypto.com/posts/article/nfts-thousand-true-fans/)](https://future.com/wp-content/uploads/2021/05/Screen-Shot-2021-02-27-at-12.56.46-PM-1536x321-1.png)

Source: [NFTs and a thousand true fans](https://a16zcrypto.com/posts/article/nfts-thousand-true-fans/)

But, the constant issuing of additional collections extracts lots of value from the community while typically adding very little value or utility. This is especially true when NFT collections issue a **fungible** token, such as ApeCoin. Fungible tokens carry much less social signaling and collectible value, meaning that launching a fungible token attempts to offer economic value to holders usually before there is any, setting the price up to dump, and removing, rather than reinforcing, community momentum.

Instead, NFT collections considering launching a fungible token would likely be much better off initially launching the fungible token as soulbound reputation token, used for accessing events, social status, and buying merch or merch discounts, but not for price speculation. Then, at a later point when the community thinks there is organic demand for the token and it would be beneficial to make it tradeable, they can vote by governance to do so.

This approach requires a bit more planning, but may actually **reduce** the regulatory concerns of launching a fungible token since it is not tradeable. This is not legal advice however, and you should always speak to a registered lawyer before launching a token.

If NFT collections and projects are to succeed, they can not remain what too many early experiments have been - file references to pixel images that have no other purpose, utility, or use case other than a speculative value.

This isn’t to say collectibles are not a legitimate use case, and that they do not carry social signal and subjective value for collectors, but how many NFT collections are actually being collected for the subjective value to holders vs hoping the floor price goes up? Very few.

https://twitter.com/chriscantino/status/1553509599440867328?s=20

It’s a shame so many projects lack value, because NFTs as a concept have tremendous potential for enabling unique use cases like improving the efficiency of ownership tracking and secondary market trading for non-fungible assets or experiences like tickets, memberships, and real world assets.

https://twitter.com/cdixon/status/1440026989038034949?s=20

https://twitter.com/john_ennis_btc/status/1688603227745378304?s=20

NFTs have additional promising roles to play in Play-to-Earn games, as previously discussed, as well as potentially in improving DAO membership engagement and governance participation (as we’ll later discuss).

**Additional Resources**

- Curation, [NFT Canon](https://a16zcrypto.com/posts/article/nft-canon/)
- Blog, [The History of Non-Fungible Tokens (NFTs)](https://medium.com/@Andrew.Steinwold/the-history-of-non-fungible-tokens-nfts-f362ca57ae10)
- Article, [The Year of the NFT: How an Emerging Medium Went Mainstream in 2021](https://www.artnews.com/list/art-news/artists/2021-year-of-the-nft-1234614022/cryptopunks-the-og-nfts/)
- Thread, [“Lessons From Growing Collections to Floor Price of 40 ETH”](https://twitter.com/chriscantino/status/1553509596412538880?s=20)
- Thread, [“Most NFT distribution models today are broken”](https://twitter.com/0xPrismatic/status/1567186402961494016?s=20)
- Thread, [“Seven types of NFTs”](https://twitter.com/cdixon/status/1469734078425485317?s=20)
- Blog, [The art of using NFT memberships](https://rechargepayments.com/blog/nfts-and-access-memberships/)
- Thread, [“Decline of NFT Royalties”](https://twitter.com/punk9059/status/1586085941390635008?s=20)
- Thread, “[Blur vs OpenSea Royalties Enforcement Battle](https://twitter.com/pandajackson42/status/1620081518575235073?s=20)”
- Article, [No Non-Fungible Tokens, No Entry: How NFT Social Clubs Work](https://www.coindesk.com/learn/no-non-fungible-tokens-no-entry-how-nft-social-clubs-work/)
- Podcast, [All about NFTs](https://future.com/podcasts/nfts-explainer/)

# Real World Assets, Jan 2016

In early 2016, Digix (DGX) become one of the first cases of a blockchain token representing a real world asset. 1 DGX tokens represented physical gold held in a vault in Singapore, and was redeemable for that gold, effectively putting gold as a real world asset onchain.

Other early experiments include the Propy, which in 2017 conducted the first blockchain-based real estate sale with a smart contract facilitated purchase of an apartment in Ukraine.

Builders in the RWA space need to recognize that blockchain solutions do not, and can not, achieve the same level of decentralization and censorship resistance as purely onchain products. Even if clear regulation existed for onchain RWA (in most jurisdiction it does not), RWA are by their very nature as physical, tangible objects always capable of being stolen, controlled, captured, confiscated, censored, or destroyed by governments or other third parties in ways that is simply not possible for onchain assets.

For example, the Singaporean or Ukrainian governments could not shut down DGX or Propy tokens on Ethereum, but if they had decided DGX or Propy were a criminal organizations, they could have confiscated all the gold or real estate ostensibly represented by those tokens.

Similarly, private parties that enter agreements with RWA products can default on their commitments, and unlike smart contracts, which can always be enforced, enforcing offchain agreements and contracts is not quick, cheap, or even guaranteed.

https://twitter.com/DeFi_Cheetah/status/1682396178581958658?s=20

While some purists argue this means RWA has no place in onchain transactions and decentralized finance, that is likely too extreme. There are benefits that blockchain offers beyond censorship resistance, such as quick and efficient transactions for changes of ownership, as well as transparent, unbiased, and immutable record keeping of those transactions.

![Source: [Tokenized Real-World Assets (RWAs): Scaling DeFi to a Global Level](https://blog.chain.link/tokenized-real-world-assets/)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/816748da-4bd3-4b63-9ad3-2886d4b67ab3/Untitled.png)

Source: [Tokenized Real-World Assets (RWAs): Scaling DeFi to a Global Level](https://blog.chain.link/tokenized-real-world-assets/)

These are the benefits builders of RWA products should lean into. They should go after use cases where censorship resistance is relatively less important, and efficiency gains are relatively more important, such as enabling cheaper, more accessible liquidity for assets that are typically illiquid and expensive to divest, like real estate.

> **Physical crackdown against crypto can occur with no advance notice, and with no possibility of recovery even for legitimate, innocent users. This violates two core assumption that we used to understand RWA risk, making the authoritarian threat a lot more serious… 
- Rune Christensen, [The Path of Compliance and the Path of Decentralization: Why Maker Has No Choice but to Prepare to Free Float Dai](https://forum.makerdao.com/t/the-path-of-compliance-and-the-path-of-decentralization-why-maker-has-no-choice-but-to-prepare-to-free-float-dai/17466)**
> 

Builders who make claims about decentralization and censorship resistance for their RWA product are largely putting on decentralization theater. The onchain governance, onchain treasury management, and onchain operations of an RWA product can be decentralized, and offchain operations can be **automated**, but the product’s bank accounts, legal entities, offchain assets, offchain contracts, physical property, and bridges between onchain and offchain assets will always inherently be centralized points of failure, even if existing regulations change.

Given this reality that RWA protocols will **always** have centralized points of failure, for an RWA protocol to minimize the risk of being arbitrarily shut down at any moment will require full compliance with very aspect of existing regulations, including but not limited to securities laws, anti-money laundering laws, and tax compliance.

One example of an approach that *may* allow for builders to tokenize RWA in a compliant manner in the United States is via the approach Homebase DAO uses to tokenize real estate. In this case, each asset is owned by an entity such as an LLC or SPV, tokenize ownership of that entity, and issue the tokens via a Reg-D or Reg-A offering. This potentially allows for both accredited and non-accredited investors to purchase and trade the tokens, though certain limitations, such as potentially no trades for the first year after token issuance, may apply. This is not legal advice though, and you should always speak to a registered professional before issuing a token.

The above approach does require KYC and has other limitations that a centralized investment product would have, but that most DeFi products do not have. Yet such is the nature of RWA blockchain products that want to avoid being shut down out of the blue.

**Additional Resources**

- Forum, [MakerDAO: The Endgame Plan](https://forum.makerdao.com/t/the-endgame-plan-parts-1-2/15456)
- Paper, [Tokenizing Real-World Assets - Towards a Regulated and Stable Token-Driven Economy](https://thetokenizer.io/wp-content/uploads/2019/06/Informational-Paper-by-The-Tokenizer-prepared-for-Maker.pdf)
- Paper, [Digix’s Whitepaper: The Gold Standard in Crypto­Assets](https://www.weusecoins.com/assets/pdf/library/Digix%20Whitepaper%20-%20The%20Gold%20Standard%20in%20Crypto%20Assets.pdf)
- Blog, [Tokenized Real-World Assets (RWAs): Scaling DeFi to a Global Level](https://blog.chain.link/tokenized-real-world-assets/)
- Blog, [Real Estate 3.0 – The Ownership Revolution](https://www.nfx.com/post/real-estate-3-proptech-the-ownership-revolution)
- Thread, [Introducing the Physical Backed Token (PBT)](https://twitter.com/Azuki/status/1582057921516474368)
- Blog, [Roofstock onChain Sells First Real Estate NFT Purchased with USDC through On-Chain Home Financing](https://www.circle.com/en/pressroom/roofstock-onchain-sells-first-real-estate-nft-purchased-with-usdc-through-on-chain-home-financing)
- Twitter Spaces, [NFT house sells for $175k: Q&A w/ @roofstock, @originprotocol & Wyre](https://twitter.com/Rusty_Bill/status/1582730053703860224?s=20)
- Paper, [Homebase DAO Whitepaper: Security Token Offerings](https://docs.homebasedao.io/whitepaper/security-token-offerings)

# DAOs & Governance, Apr 2016

MakerDAO and “The DAO” were the first two projects to popularize DAOs. MakerDAO can trace its roots back to a [2015 Reddit post](https://www.reddit.com/r/ethereum/comments/30f98i/introducing_edollar_the_ultimate_stablecoin_built/) by Rune Christensen, and conducted its first private token sales in late 2015, but did not officially launch until 2017.

The DAO, a decentralized VC fund, launched a public crowdsale in April 2016, raising $150mm in ETH over the course of 28 days Unfortunately, the smart contract handling the sale contained a bug - allowing an exploiter to steal approximately 15% of the total circulating suppy of ETH at the time.

Proposals to freeze the stolen ETH eventually led to what is arguably the single most controversial decision ever made in blockchain’s history: to rollback the Ethereum blockchain’s state to undo the result of the hack.

Despite attempts and threats by the exploiter to bribe Ethereum miners to not support any new forks, a hard fork was proposed, splitting the chain based on those that supported rolling back, and those that did not, whether for monetary or ideological reasons.

That original Ethereum chain, with the 15% of tokens owned by the attacker is what is now known as Ethereum Classic.

It is unfortunate, if not ironic, that one of the earliest popular examples of a DAO has set a legacy of relatively centralized control and interference. Yet despite the controversy surrounding one of the earliest DAOs, the number of DAOs has obviously drastically increased since then.

While DAOs vary in the specifics of their operations, objectives, and structures, all DAOs deal with three common aspects:

1. Structure & Legal Entity
2. Governance
3. Treasury Management & Allocation

 

**1. DAO Structure & Legal Entity**

<aside>
💡 Builders looking for resources on how to structure their entity as a DAO should refer to Chapter 2.7 on Legal Opinion & Structure.

</aside>

**2. DAO Governance**

<aside>
💡 We’ve discussed the risks introduced by community governance in the context of governance tokens in Chapter 1.5. In general, builders overestimate the importance of community governance, underestimate its risks, conflate decentralization with user governance, and incorrectly assume that governance is the only way to reduce certain regulatory risks.

As products like Liquity demonstrate, it is entirely possible to retain decentralization, and even user ownership, without requiring governance.

</aside>

User governance is a subjective design objective and/or political decision, not a technical requirement or a requirement to be decentralized. If you are insistent on having user governance, whether for political or philosophical goals, or in the rare cases in which a registered legal professional has confirmed that user governance is advisable to reduce risk, it’s important to consider the current state of governance, what is broken, and how it can be improved.

While the events of “The DAO” were unfortunate, it is more unfortunate that even today, most DAOs remain decentralized-in-name-only (DINOs).

That harsh reality is that participation rates in many of the most popular DAOs are extremely low, while concentrations of voting power are extremely high.

> **In both [Uniswap and Compound] governance systems less than 10% of total tokens (or
15% of circulating tokens) participate in votes on proposals. Hence, already 7.5% of circulating tokens would have sufficed to win an average vote in the past…

[The number of addresses required for >50% voting power] reveal an extreme centralization in all three governance systems: In the case of Compound, only 8 delegates can dictate any governance action using their majority. For Uniswap this number is 11, for ENS it is 18.
Source: [Analyzing Voting Power in Decentralized Governance: Who controls DAOs?](https://arxiv.org/pdf/2204.01176.pdf)**
> 

Compensating governance participation to counter low engagement is a solution in theory, but in practice it can introduce even more room for abuse and exploits by warping incentives…

https://twitter.com/0xfrisson/status/1689032382169616384?s=20

… and by encouraging “governance farming”, i.e. spamming meaningless governance proposals in order to then participate in votes to earn governance compensation. This is far from a theoretical concern, in fact, a large bulk of existing DAO proposals are **already** meaningless spam.

https://twitter.com/DrNickA/status/1692077818169966932?s=20

Worse still, at least one analysis has found that low governance involvement does not seem to be related to a DAOs size, larger DAOs with more at stake don’t see more governance involvement, nor do smaller DAOs with theoretically smaller, more passionate communities. The frequency of proposals to engage with also seems to have little impact, suggesting this isn’t just a matter of governance votes being either too time-consuming or too infrequent to remember.

> **Regression shows us that there’s no relationship between size of the DAO (by treasury AUM) and participation rate. This means that small DAOs and large DAOs don’t really see a difference in participation rate. Nor was there a relationship between the total number of proposals and the participation rate (i.e., just because there are more proposals doesn’t mean that people will participate in them more, below).
Source: [The Dao Governance Conundrum Part II](https://medium.com/@fydetreasury/the-dao-governance-conundrum-part-ii-e375c240b76a)**
> 

Even when users do participate, the vast majority of governance is done off-chain, meaning there is some centralized middleman between the decision making process itself, and the on-chain fulfillment or execution of that decision.

![Source: [Governor Note: Evolving On-Chain Governance With Element Council](https://messari.io/report/governor-note-evolving-on-chain-governance-with-element-council)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/44c8ec8e-5f8a-4b18-a690-fdd0a11b4170/Untitled.png)

Source: [Governor Note: Evolving On-Chain Governance With Element Council](https://messari.io/report/governor-note-evolving-on-chain-governance-with-element-council)

The standard “1 token, 1 vote, more than 50% majority wins the vote” form of governance is far from the only form it can take, but is still commonly used, despite its flaws.

Quadratic voting, and other methods that essentially underweight large whale addresses quickly encounter issues of Sybil resistance. Reducing large whales’ vote weight in proportion to an equivalent number of tokens split across many smaller voters doesn’t work if the whale can freely transfer those governance tokens to other wallets, and wallets are not tied to any identity, reputation, or whitelist system. The whale can simply split their tokens across multiple wallets to **appear** like many small voters, and achieve the same final weight of their vote. The only real cost in such a scenario (without other Sybil countermeasures) would be the gas fees to transfer the governance tokens to multiple wallets.

Associating voting power with an identity, such as a connected social media account or a non-transferrable or illiquid NFT, can more effectively prevent Sybil attacks, since unlike a fungible token, whales can’t split an identity or NFT across multiple wallets.

> **In early stages of community building, illiquid tokens with some status attached seem to do best at retaining members. If you look at engaged or successful communities like Mirror or CryptoPunks, tokens have either 1) high barriers to entry 2) or have been fairly illiquid for most of their history. On the contrary most fungible tokens tend to be 1) low barrier to entry especially in the early days 2) and fairly liquid. Make sure to take that into account when leveraging tokens to recruit community members.
Source: [Growing A Tokenized Community](https://club.mirror.xyz/hUCOZNvJ7uQI7DXOAmz3Rr-yt82o9gTiJx5T5srD5tc)**
> 

And in fact, there is at least some weak evidence supporting that an approach to DAO membership oriented around NFTs, rather than fungible tokens, may improve governance participation, as Nouns DAO typically see much higher participation than the average DAO.

![Source: [Nouns — Hyperscaling a Brand & Treasury From Zero](https://members.delphidigital.io/reports/nouns-hyperscaling-a-brand-treasury-from-zero#key-takeaways)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c534236c-67cb-4dae-8274-20a63150b582/Untitled.png)

Source: [Nouns — Hyperscaling a Brand & Treasury From Zero](https://members.delphidigital.io/reports/nouns-hyperscaling-a-brand-treasury-from-zero#key-takeaways)

Rushing to launch a *fungible token* for a DAO is usually not as beneficial as most builders think it will be. In fact, it can be outright counterproductive, for all the reasons we discussed in [Chapter 1.4](https://www.notion.so/1-4-Does-Every-Project-Need-a-Token-79f30dc5e5d34fcca18b7fbcfff3792f?pvs=21) about the risks and downsides to launching a token.

https://twitter.com/mrjasonchoi/status/1550463281671708675?s=20

https://twitter.com/CDTEliot/status/1481374373281878016?s=20

Why are most governance programs so bad? One (large) contributing factor is that they inherently ask largely uninterested and/or uninformed people, without high degrees of context, to make high context decisions.

> **The delegates don't know enough to make good decisions on most of these things. They either don't vote (again, leaving the decisions to those who "show up") or make them based on minimal or unrelated information (e.g. who their friends are). It's an inefficient waste of time.
Source: [A Call for DAO Minimalism in Protocol Governance - ENS DAO as a Case Study](https://twitter.com/BrantlyMillegan/status/1669764751021203457?s=20)**
> 

Potential solutions for governance, [as proposed by Vitalik](https://vitalik.ca/general/2021/08/16/voting3.html), include:

1. Limited governance
2. Non-coin-driven governance
3. Skin in the game (i.e. make voters individually, and not just collectively, responsible for their decisions)

Of course, forgoing governance altogether remains another option, as does reputation-based governance or elected representative-based governance that transparently strikes a balance between centralization and decentralization, instead of claiming to optimize for decentralization while failing to achieve it in practice.

While a deep dive into every possible approach to governance is beyond this guide, the below table summarizes many of the most significant and popular governance mechanisms. Please note the list is not exhaustive, and mechanisms are not mutually exclusive - governance processes can and often do combine multiple of the below mechanisms.

**Summary of Governance Mechanisms**

| Mechanism | Description | Pros | Cons | Examples |
| --- | --- | --- | --- | --- |
| 1 Token, 1 Vote | Voters allocate tokens across one or more candidates, each token corresponds to one vote, | Simple to understand and implement | Plutocratic: whales have dominating influence and exposed to governance attacks by well funded parties | Most DAOs and DeFi protocols |
| Quorum Voting | For the result of a vote to be considered valid, a minimum number of votes or voters must participate. | Helps eliminate some governance attacks where a small minority hijacks a vote while most voters are unaware or unable to respond | If the quorum threshold is set too high, can paralyze decision making | Most DAOs and DeFi protocols |
| Quadratic Voting | Voters allocate tokens across one or more candidates, but for any given candidate, that voter’s number of votes is equal the square root of the number of tokens they allocate. | Relatively simple way to balance voting power of a few large voters vs many smaller voters (in theory) | Can easily be gamed by whales splitting tokens across multiple wallets, thus requires Sybil resistance for full impact. Complex to implement and understand | Gitcoin, Radicle |
| Pairwise Voting | Voters evaluate each head-to-head pair of candidates, and select their preferred candidate in each pairing. Votes can be weighted by tokens or not. The final result is determined by which candidate performs the best in head-to-head matches (this is not necessarily the same outcome as which performs best when all are candidates are considered simultaneously). | Captures more nuanced voter preferences, helps avoid voters settling for the “lesser of two evils” and avoid two similar choices diluting each other’s support | Winner may not have the popular vote, more time-consuming for voters as the number of candidates increases. Complex to implement and understand | Colony Network |
| Stake-Weighted Voting | Voters allocate tokens across one or more candidates, locking up tokens or incurring some opportunity cost or skin-in-the-game stake to do so. The weight of a voters’ tokens increases as the cost they incur to vote (stake) increases. | Reflects long-term preferences of voters, discourage short-term mercenary behavior | Depending on the cost function, potential for older/earlier users (and/or whales) to dominate the vote | Curve |
| Conviction Voting | Voters allocate tokens across one or more candidates by locking/bonding tokens to support a given candidate, with voting weight accruing over time as the tokens remain locked/bonded to that candidate. | Improves governance coordination by signaling user preferences over time, discourages short-term mercenary behavior | Older/earlier voters or candidates can have outsized influences | 1Hive, Commons Stack, MetaCartel |
| Ranked Choice Voting | Voters directly rank candidates in order of preference. If no candidate has a majority, the least support candidate is eliminated, with candidates re-ranked per voters indicated rankings excluding that candidate. This is repeated until one candidate has a majority. | Results in better compromises and maximization of overall voter preferences, helps avoid voters settling for the “lesser of two evils” and avoid two similar choices diluting each other’s support | More complex to interpret and less straightforward to weight by token balances | Not common in blockchain, used in some US state elections |
| Commit-Reveal | Voters submit their votes for candidates without that vote being revealed. Once all votes are submitted, votes are revealed. | Helps maintain voting integrity by making vote buying and other manipulation more difficult due to imperfect information ahead of results | Can be more complex to implement in way that is trustless and does increase burden on voters to first vote and then return to unseal votes, in certain cases may lead to less voter engagement | Gnosis prediction markets |
| Liquid Democracy | Voters can either directly vote on a given proposal or delegate their votes by default to another voter who in turn can either vote or further delegate those votes. | Increases governance participation and more informed voter decisions, combines benefits of direct and representative democracy | Delegation can lead to centralization, and delegates may act against the interests of their delegators | Democracy Earth, Giveth, Aargon |
| Holographic Consensus | A subset of voters stake tokens to back candidates they believe will win, if the candidates reach a certain threshold, they are escalated to the larger, full audience of voters. If these candidates lose or do not pass, early supporters lose their stake, if they do pass, early supporters are rewarded.
 | More scalable governance, and more informed, better engaged voters by incentivizing involvement at the earliest stages of proposals | Significantly increases governance complexity, financial incentives can warp governance decisions, introduce conflicts of interest, and be prohibitive for some voters | Genesis DAO, Prime DAO |

Griff Green, who helped launch The DAO, led a counterattack against the black hat hacker who drained its treasury, and has continued to work on DAOs and governance ever since, has conceived of, or experimented with, just about every governance mechanism you can imagine. In addition to the above table, you can hear Griff discuss a wide variety of mechanisms below.

https://twitter.com/thegrifft/status/1595110675244011521?s=20

**3. DAO Treasury Management**

**Please note, as with the other contents of this guide, this section is not financial, investment, or accounting advice. Always consult with a registered professional and do your own research.**

Optimizing DAO treasury management warrants its own full guide - in essence, it’s a very similar challenge to what sovereign wealth funds, pensions funds, endowment funds, and trusts try to accomplish: invest current assets so that future liabilities are met or exceeded by future investment proceeds.

There’s a reason institutional money managers exist that help such funds manage their investments and risk, and there’s a reason the crypto equivalent of treasury and risk management protocols such as Gauntlet and Fireblocks have also grown in popularity: investing to match liabilities decades into the future is much easier said than done.

According to Delphi Digital, most DAOs are overweight their own native token. As a result, they can be caught by surprise when a bear market arrives, and their treasury, which appeared to be exceptionally well funded, crashes 90% because it is composed entirely of the protocol’s own highly volatile token.

![Source: [A New Mental Model for Defi Treasuries](https://uncommoncore.co/a-new-mental-model-for-defi-treasuries/)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c12b5949-54f2-412e-b4d1-1386e35f1b1b/Screen_Shot_2022-10-21_at_2.28.37_PM.png)

Source: [A New Mental Model for Defi Treasuries](https://uncommoncore.co/a-new-mental-model-for-defi-treasuries/)

Hedging during a bull market by converting portions of the treasury into other uncorrelated assets such as BTC, ETH, stablecoins, and high quality, yield generating altcoins diversifies the treasury. Generally speaking, diversification of any portfolio is **much more appropriate than over-concentrating in one asset and hoping for the best.

This issue is exacerbated when DAO treasury management is combined with community governance, such that the treasury is being allocated by decision makers with much shorter term individual investment horizons than the DAO’s, and without a professional level understanding of fundamentals like risk management and modern portfolio theory.

> **I have extremely little faith that coin-voting communities of retail investors will vote for the best medium-term outcomes, and in fact will more likely vote for damaging medium-term outcomes. I read something today that said Sushi treasury went from $1bn to $30m in a year. I don’t know if that is exaggerated, or fictional, but think this will be a common story of many failed DAOs in time.
Source: [ApeCoin & the death of staking](https://cobie.substack.com/p/apecoin-and-the-death-of-staking)**
> 

Conversely, selling other treasury assets to buy back the DAO’s own native token, if the price has fallen so much that it represents the best risk adjusted returns available, can also be appropriate, depending on the situation.

> **DAOs should discount native tokens from their treasury immediately – they are the crypto equivalent to authorized but unissued stock… DAO treasuries need to survive the next bear market… Build a treasury that will last you 2-4 years even if the entire market collapses by 90% and stays there for some time.
Source: [A New Mental Model for Defi Treasuries](https://uncommoncore.co/a-new-mental-model-for-defi-treasuries/)**
> 

While planning for **years** in advance may sound difficult, that’s how long bear markets can last, and if your DAO plans to be around for the long term, that's what your treasury management approach ultimately needs to be doing.

![Source: [Treasury Management: A Guide to Navigating Downturns](https://a16zcrypto.com/posts/article/treasury-management-guide/)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/54a57eb8-9023-4601-b4f3-b00ec0913184/Untitled.png)

Source: [Treasury Management: A Guide to Navigating Downturns](https://a16zcrypto.com/posts/article/treasury-management-guide/)

**Additional Resources**

- Curation, [DAOs, A Canon](https://a16zcrypto.com/posts/article/dao-canon/)
- Blog, [Treasury Management: A Guide to Navigating Downturns](https://a16zcrypto.com/posts/article/treasury-management-guide/)
- Blog, [DAO Voting Mechanisms Explained](https://limechain.tech/blog/dao-voting-mechanisms-explained-2022-guide/)
- Blog, [Blockchain Governance: Programming Our Future](https://medium.com/@FEhrsam/blockchain-governance-programming-our-future-c3bfe30f2d74)
- Blog, [Growing A Tokenized Community](https://club.mirror.xyz/hUCOZNvJ7uQI7DXOAmz3Rr-yt82o9gTiJx5T5srD5tc)
- Blog, [Moving beyond coin voting governance](https://vitalik.ca/general/2021/08/16/voting3.html)
- Blog, [Endgame: Proof of Governance](https://dba.mirror.xyz/UTPfxWe65dYrUu_RJX-5VkAJypFRyw3AZh6m0dRXYZk)
- Blog, [Governance Minimization](https://www.paradigm.xyz/2020/10/870#what-governance-minimization-is-not)
- Paper, [RAI Whitepaper - Governance Minimization Guide](https://docs.reflexer.finance/ungovernance/governance-minimization-guide)
- Blog, [DAO Voting Mechanisms Explained](https://limechain.tech/blog/dao-voting-mechanisms-explained/)
- Blog, [Popular Voting Mechanisms Used by DAOs](https://www.peaka.com/blog/web3-dao-voting-mechanisms/)
- Blog, [DAO Voting Mechanisms and Systems: A Deep Dive](https://blog.xdao.app/unleashing-the-power-of-dao-voting-a-deep-dive-into-dao-voting-mechanisms-and-systems-4d4ece7aed36)
- Blog, [Voting Options in DAOs](https://medium.com/daostack/voting-options-in-daos-b86e5c69a3e3)
- Blog, [Conviction Voting: A Novel Continuous Decision Making Alternative to Governance](https://blog.giveth.io/conviction-voting-a-novel-continuous-decision-making-alternative-to-governance-aa746cfb9475)
- Blog, [A Taxonomy of Voting Methods](https://blog.aragon.org/a-taxonomy-of-voting-methods/)
- Paper, [Analyzing Voting Power in Decentralized Governance: Who controls DAOs?](https://arxiv.org/pdf/2204.01176.pdf)
- Paper, [Understanding Blockchain Governance: Analyzing Decentralized Voting to Amend DeFi Smart Contracts](https://arxiv.org/pdf/2305.17655.pdf)
- Paper, [Unpacking How Decentralized Autonomous Organizations (DAOs) Work in Practice](https://arxiv.org/abs/2304.09822)
- Paper, [Decentralized Capital Allocation via Budgeting Boxes](https://uploads-ssl.webflow.com/61840fafb9a4c433c1470856/639b50ee30b729cb016806c1_BudgetingBoxes.pdf)
- Blog, [A New Mental Model for DeFi Treasuries](https://uncommoncore.co/a-new-mental-model-for-defi-treasuries/)
- Article, [The impact and rise of DAOs in the legal industry](https://cointelegraph.com/learn/daos-impact-in-legal-industry)
- Thread, [DAOs are broken](https://twitter.com/0xsydney/status/1674285151478751232)
- Thread, [“Top DAO tools everyone needs to know”](https://twitter.com/JRossTreacher/status/1586538388248621056)
- Blog, [Anatomy of an Alleged DAO Scam](https://www.karlstack.com/p/anatomy-of-an-alleged-dao-scam?s=w)
- YouTube, [The Evolution of Decentralized Governance](https://www.youtube.com/watch?v=igyYHRf0-aw)
- YouTube, [Bringing Decentralized Governance to Tech Platforms](https://www.youtube.com/watch?v=CWaGciMkDWA)
- Youtube, [Voting, Security, and Governance in Blockchains and Cryptonetworks](https://www.youtube.com/watch?v=Lx9sVfNvpXw)
- Blog, [Lightspeed Democracy: What Web3 Organizations Can Learn From the History of Governance](https://a16zcrypto.com/posts/article/lightspeed-democracy-what-web3-organizations-can-learn-from-the-history-of-governance/)
- Thread, [A Call for DAO Minimalism in Protocol Governance - ENS DAO as a Case Study](https://twitter.com/BrantlyMillegan/status/1669764751021203457)
- Blog, [Governance FAQ](https://a16zcrypto.com/posts/article/governance-faq/)
- Blog, [Paying People to Participate in Governance](https://a16zcrypto.com/posts/article/paying-people-to-participate-in-governance/)
- Blog, [Nouns — Hyperscaling a Brand & Treasury From Zero](https://members.delphidigital.io/reports/nouns-hyperscaling-a-brand-treasury-from-zero#key-takeaways)
- Blog, [Little-Known Facts About MakerDAO](https://blog.makerdao.com/little-known-facts-about-makerdao)
- Paper, [When Bidders Are DAOs](https://arxiv.org/pdf/2306.17099.pdf)
- Curation, [The Token Curated Registry Reading List](https://medium.com/@tokencuratedregistry/the-token-curated-registry-whitepaper-bd2fb29299d6)

# Decentralized Social Media, Jul 2016

Steemit, the first large blockchain based social media platform launched in July 2016 with plans of eventually taking on giants such as Tumblr and YouTube.

The platform used a complex two token model, STEEM and SBD, to reward content in an attempt to incentivize high quality content creation and community curation of quality content.

As you might expect - this resulted in a large amount of botting and spamming of low quality content to earn rewards.

Using token emissions to bootstrap social media adoption without introducing ample room for exploits and Sybil attacks largely remains an unsolved problem to this day. Modern decentralized social media attempts are either blockchain adjacent, rather than explicitly blockchain based (e.x.  [Nostr](https://nostr.com/), [AT Protocol/BlueSky](https://blueskyweb.xyz/), [Mastodon](https://mastodon.social/explore)), or focused more on organic activity, exclusivity via token gating, and native integrations with wallets for social interaction ([Status.im](https://status.im/), [Farcaster](https://www.farcaster.xyz/), [Lens Protocol](https://www.lens.xyz/), [Orb](https://orb.ac/)).

In additional to the technical challenges of a widely distributed social media platform, the relevant economic incentives pose additional challenges. A purely peer-to-peer approach introduces a large number of challenges, including how to ensure a consistent experience or store history - who pays for the storage? And a client to node/relay/server/host based approach simply modifies the question without answering it - why will people pay the costs to continually run the required hardware?

The economic incentives must come from somewhere - either via existing network effects (such as facilitating economic activities that communities already conduct) or from users explicitly paying for services.

It’s no secret that Web2 social media is not actually free - you pay by selling your data. To scale, Web3 social media can not be free either.

**Additional Resources**

- Blog, [A Self-Authenticating Social Protocol](https://blueskyweb.org/blog/3-6-2022-a-self-authenticating-social-protocol)
- GitLab, [Decentralized Social Media Ecosystem Overview](https://gitlab.com/bluesky-community1/decentralized-ecosystem/-/blob/master/README.md)
- Blog, [Sufficient Decentralization for Social Networks](https://www.varunsrinivasan.com/2022/01/11/sufficient-decentralization-for-social-networks)
- Thread, [Banned from Mastodon](https://twitter.com/LefterisJP/status/1593934653114785793?s=20)
- Article, [FBI Seizure of Mastodon Server Data is a Wakeup Call to Fediverse Users and Hosts to Protect their Users](https://www.eff.org/deeplinks/2023/07/fbi-seizure-mastodon-server-wakeup-call-fediverse-users-and-hosts-protect-their)
- Paper, [Incentivized Blockchain-based Social Media Platforms: A Case Study of Steemit](https://arxiv.org/pdf/1904.07310.pdf)

# Decentralized Borrowing & Lending, May 2017

A project known as ETHLend launched an ICO in May 2017 to develop a decentralized lending application on the Ethereum blockchain.

Later in 2018, that project rebranded to its current name: Aave.

The trustless nature of smart contracts makes blockchain fit for purpose for overcollateralized lending. In traditional collateralized lending, such as mortgages or car loans, recovering the collateral asset when a borrower defaults on their loan can be expensive, time consuming, and get tied up for years in legal challenges in order to enforce the original contract. Enforceability is not typically a problem smart contracts have.

Yet for the same reasons, **undercollateralized** lending (e.x. personal loans, credit card debt, student loans) is not as well fit to blockchain lending. Enforcing the contract is no longer a matter of code, so undercollateralized lending, even when agreed to onchain, inherently becomes exposed to all the same kinds of complications and risks that come with RWA.

<aside>
💡 Introducing collateral and/or borrowing lending **always** creates a risk of bad debt, if not for the entire treasury, then at the very least for lenders using the product. Builders should be intimately familiar with these risks and best practices to mitigate them.

</aside>

Risks created when collateral, borrowing, or lending, is introduced can include:

- Oracle risk: if liquidations or minting new loans are dependent on an oracle price, a bug in oracle prices can enable minting much more debt than risk controls “should” allow.
- Market manipulation risk: when liquidations or minting new loans are dependent on recent market prices (whether via an oracle or via direct observation of an onchain AMM), short term temporary spikes or crashes in price can be manipulated to cause cascading liquidations or inflate collateral to mint excess debt.
- Price and correlation risk: prices move, and markets are volatile - the possibility of collateral assets dropping significantly and rapidly in price always exists. This risk can be **mitigated** with **diversification, but these benefits tend to decline exactly when they are most needed because correlations between assets generally increase during market crashes.
- Black swan events (”unknown unknowns”): the most difficult thing about risk is that its impossible to fully anticipate. Builders should be aware of the limitations of common concepts such as liquidity, risk premiums, and market cap for evaluating the expected value of collateral in a liquidation scenario. What may hold true in most cases is not guaranteed to always hold true.

**Additional Resources**

- Paper, [Increased Correlation in Bear Markets](https://www.researchgate.net/publication/235351979_Increased_Correlation_in_Bear_Markets)
- Aave Forum, [Blameless Post Mortem: Curve - Aug 8, 2023](https://governance.aave.com/t/blameless-post-mortem-curve-aug-8-2023/14386)
- Blog, [Fully Diluted Value is a Misleading Concept](https://www.ar.ca/blog/fully-diluted-value-is-a-misleading-concept)
- Thread, [“Low Float, High FDV”](https://twitter.com/jonwu_/status/1590883261164638208)
- Blog, [Which one should you use? Arithmetic or geometric mean TWAP](https://delphilabs.medium.com/which-one-should-you-use-arithmetic-or-geometric-mean-twap-ded01532bf49)

# Bonding Curves, Jun 2017

The concept of bonding curves were initially popularized by v1 Bancor, which launched June 2017. At its simplest, the concept of a bonding curve is a fixed mathematical curve that governs a tokens price.

For instance, on a linear bonding curve with a slope of 1, the first token to be purchased might cost $1, the second $2, the third $3, etc. If ten tokens are purchased in total, $55 would have been used to purchase those tokens. Selling tokens back to the bonding curve smart contract works the same way in reverse. Assuming the current supply is ten, selling one token would be for $10, the next for $9, etc.

![Source: [An introduction to bonding curves, shapes and use cases](https://medium.com/linum-labs/intro-to-bonding-curves-and-shapes-bf326bc4e11a)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dce2f0c0-576b-4fb0-aa90-4379e92cdc28/Untitled.png)

Source: [An introduction to bonding curves, shapes and use cases](https://medium.com/linum-labs/intro-to-bonding-curves-and-shapes-bf326bc4e11a)

Bonding curves allowed for new (though arguably not very practical) models of token issuance and token faucets.

Imagine a utility token that is burned on use. As the token is used, the price per token increases along the bonding curve, but the total supply of available (unburned tokens) shrinks in relation to the total supply of all tokens (including burned), resulting in a portion of the protocol treasury that can never be redeemed - protocol revenues that have been captured.

Or imagine a token that has one curve for buying the token from the treasury and another, lower curve for selling the token back to the treasury - the spread between the curves again essentially represents protocol revenues.

https://twitter.com/DrNickA/status/1689934620618330113?s=20

In practice, however, bonding curves have a glaring weakness and are not commonly used outside very specific contexts. In fact, their greatest strength - a formulaic relationship of price and supply - is also their greatest weakness. A token with a price driven by market forces or incentives is relevant for a much wider range of use cases. Furthermore, in order to truly make a bonding curve two-way (i.e. users can buy or sell from the curve), any curve used by a product for token issuance requires that treasury to retain a significant portion to rebuy tokens along the curve - the funds in the treasury can’t actually be used.

<aside>
💡 Arguably the most important significant aspect of bonding curves’ legacy is that they were an early predecessor of AMMs. One could even make the argument that AMMs are a type of bonding curve that allows for token prices to be a function of market dynamics, even though the price at any given point in time is “predetermined” (by the AMM’s curve).

</aside>

**Additional Resources**

- Blog, [Tokens 2.0: Curved Token Bonding in Curation Markets](https://medium.com/@simondlr/tokens-2-0-curved-token-bonding-in-curation-markets-1764a2e0bee5)
- Blog, [Bancor’s Smart Tokens vs Token Bonding Curves](https://medium.com/@simondlr/bancors-smart-tokens-vs-token-bonding-curves-a4f0cdfd3388)
- Blog, [Bancor: The History of DeFi’s Founding Fathers](https://www.thetie.io/insights/research/bancor-history/)
- Blog, [Bonding Curves Explained](https://yos.io/2018/11/10/bonding-curves/)
- Blog, [An introduction to bonding curves, shapes and use cases](https://medium.com/linum-labs/intro-to-bonding-curves-and-shapes-bf326bc4e11a)
- Blog, [How to Make Bonding Curves for Continuous Token Models](https://blog.relevant.community/how-to-make-bonding-curves-for-continuous-token-models-3784653f8b17)
- Blog, [Token Bonding Curves](https://medium.com/aventus/token-bonding-curves-683b8b309c18)
- Blog, [Swarm and its “Bzzaar” Bonding Curve](https://medium.com/ethereum-swarm/swarm-and-its-bzzaar-bonding-curve-ac2fa9889914)

# Multichain & Bridges, 2017

With the plethora of alternate L1 chains launching ICOs in 2017, including EOS, Tezos, and NEO/AntShares, came the need to bridge tokens between these blockchains which do not natively communicate with each other.

It’s difficult to pin down the exact first instance of a bridge across chains. Early projects operating in the space of enabling crosschain, multichain, and/or bridges included Blocknet in 2014, Polkadot and Cosmos around 2016, and Wanchain in 2017.

Today, the number of available bridges in each ecosystem has grown considerably.

![Source: [What are Cross-Chain Bridges?](https://www.alchemy.com/overviews/cross-chain-bridges)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf25b1a0-ba39-47d4-9409-c276c61dc38d/Untitled.png)

Source: [What are Cross-Chain Bridges?](https://www.alchemy.com/overviews/cross-chain-bridges)

This is despite the fact that bridges remain one of the most vulnerable areas of all of crypto, with bridge hacks, bugs, and exploits representing some of the largest exploits in DeFi, and overall blockchain, history.

https://twitter.com/koeppelmann/status/1684133540101758976?s=20

The reason for this is pretty simple: bridges often hold a large number of tokens that are essentially locked on one chain (the bridge out chain) in order to back the token on the other chain (bridge in the chain) in a 1:1 manner so that the tokens can be bridged back at any time.

This creates a very large target for attackers and a very large risk for developers to avoid bugs or lose access keys.

https://twitter.com/haydenzadams/status/1685711436494811136?s=20

Despite the growth in the number, importance, and security threats of bridges, a formal classification system for different types of bridges has yet to emerge. One potential reason for this is that while bridges can share a common approach - often very subtle differences in implementation can have large implications on realized security risks and trust assumptions.

Bridges suffer from their own trilemma, stating that only two of three core aspects can be achieved between being trustless, generalizable, and extensible.

![Source: **[The Interoperability Trilemma](https://blog.connext.network/the-interoperability-trilemma-657c2cf69f17)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32da6ee5-3b6e-4ca9-9ec3-6d1de23b69a8/Untitled.png)

Source: **[The Interoperability Trilemma](https://blog.connext.network/the-interoperability-trilemma-657c2cf69f17)**

<aside>
💡 Loosely speaking bridges can be fit into the below informal categorizations - though as mentioned before, differences in implementation, and thus considerable differences in security implications and attack vectors, exist even within the same category of bridge.

</aside>

1. **Centralized Custodial Bridges**

These bridges rely on a centralized custodian that controls a wallet. To bridge in, users send tokens to this centralized wallet, and once the custodian has confirmed ownership of the tokens on Chain A, they send tokens on Chain B to the user.

While simple and scalable, this approach suffers from the obvious drawback of reliance on a centralized entity that can be hacked, lose access to the wallet, censor users, block users, or even steal from users.

2. **Vault Bridges**

Instead of sending tokens to a centralized custodian, vault bridges have users send tokens to either a smart contract or a multi-sig wallet. This smart contract or multi-sig wallet acts as a vault, holding the tokens sent to it.

When tokens are received on Chain A, the tokens are “locked” (held) in the vault, and tokens on Chain B are released to the user. To bridge back, the user sends tokens to the corresponding vault on Chain B, locking tokens on Chain B, and unlocking tokens on Chain A.

3. **Mint & Burn Bridges**

These bridges operate very similarly to Vault Bridges. Users that want to bridge send tokens on Chain A to a smart contract or multi-sig wallet. But instead of corresponding tokens on Chain B being **unlocked** by a vault, new tokens on Chain B are actually minted by a smart contract.

To reverse the process and bridge back to Chain A, a user burns the tokens on Chain B with the smart contract, and then the tokens on Chain A are unlocked and released for the user to reclaim.

Depending on the bridge, it’s possible that tokens are minted and burned on Chain A as well, not locked in a vault. For example, to bridge to Chain B, users burn tokens with the bridge smart contract on Chain A, and mint tokens on Chain B (instead of locking up tokens on Chain A in a smart contract or multi-sig wallet).

4. **Cross-Chain Liquidity Pools / Swaps**

In this situation, users effectively sell the token on Chain A and simultaneously buy the corresponding token on Chain B, facilitated by a liquidity pool (which can have varying degrees of decentralization depending on the bridge in question).

For this to enable bridging the same token from one chain to another effectively requires some portion of the token supply to already exist on both chains, or already have been bridged via some other method to both chains.

Hash Time-Locked Contracts or Atomic Swaps can be viewed as a special type of Cross-Chain Swap that uses cryptography and time locks to trustlessly enable two users to swap or trade assets across chains. The nature of the swap ensures that either both users receive the ability to claim the tokens they should receive, or neither do - it does not require trusting the other party involved, or using any centralized custodian.

5. **Collateralized Bridges / Non-Custodial Wrapped Assets**

This type of “bridge” is essentially a non-custodial wrapped, or even synthetic, asset which is backed by collateral.

For example, tBTC represents Bitcoin “bridged” to Ethereum. A user who has native Bitcoin and wants to “bridge” Bitcoin to Ethereum without using wBTC which relies on a centralized custodian can send BTC on the Bitcoin blockchain to an wallet controlled by a number of “keepers”. The “keepers” that control this wallet, have posted ETH collateral on the Ethereum network that ensures they act honestly by minting a corresponding number of tBTC on a 1:1 basis for BTC, and for redeeming tBTC for BTC on a 1:1 basis.

If they do not, their collateral is slashed, and is used to compensate the affected bridge user. This doesn’t *guarantee* an exact 1:1 redemption in the case of misbehavior, but it makes misbehavior unprofitable for the keepers, and helps ensure users’ losses are minimized, if not eliminated, if misbehavior does occur.

**Additional Resources**

- Reddit (Vitalik), [“optimistic about a *multi-chain,* pessimistic about *cross-chain”*](https://old.reddit.com/r/ethereum/comments/rwojtk/ama_we_are_the_efs_research_team_pt_7_07_january/hrngyk8/)
- Forum, [L2Bridge Risk Framework](https://gov.l2beat.com/t/l2bridge-risk-framework/31)
- Blog, [What are Cross-Chain Bridges?](https://www.alchemy.com/overviews/cross-chain-bridges)
- Blog, [What Are Blockchain Bridges And How Can We Classify Them?](https://blog.li.fi/what-are-blockchain-bridges-and-how-can-we-classify-them-560dc6ec05fa)
- Thread, [Multi-Chain, Cross-Chain, and Omnichain - The Ultimate Guide](https://twitter.com/ernestxavier_/status/1677295292545134598)
- Blog, [The Interoperability Trilemma](https://blog.connext.network/the-interoperability-trilemma-657c2cf69f17)
- Blog, [What are Blockchain Bridges? A Complete Guide](https://www.chainport.io/knowledge-base/what-are-blockchain-bridges-and-how-do-they-work)
- Thread, [“Tokenomics in a Crosschain World”](https://twitter.com/0xWangarian/status/1391680711128621056?s=20)
- YouTube, [Daniel Lumi - Next Gen Cross-Chain Bridges & How All Bridges Still Suck](https://www.youtube.com/watch?v=EAkOHyWPI4o)
- YouTube, [Mastering Cross-Chain Bridges](https://www.youtube.com/watch?v=T6cRqriIBNk)

# Synthetic Assets, Feb 2018

Synthetix, originally known as Haven, launched its ICO in February 2018, becoming the earliest platforms to popularize synthetic assets.

Synthetic assets can be as simple as peer-to-peer agreements, such as “Party A will pay Party B the difference between the current price of gold when this agreement is signed, and the price of gold 30 days after this agreement is signed”.

The issue with such peer-to-peer deals is that it involves counterparty risk and is very illiquid, as entering a trade requires finding someone willing to take the opposite side of the exact trade you want to make.

Prior to the popularity of AMMs, which did not arrive until later in 2018, Synthetix solved these issues by using a shared collateralization based system that enabled traders to mint synthetic tokens that tracked prices of assets using a price oracle. The considerable downside of this shared pool was that a given trader’s profit and loss was not purely a function of their own trades - it shared in some of the impact of other trader’s positions. 

This later evolved to a more generalized AMM-like liquidity pool against which traders can mint synthetic positions. Profit and loss on each synthetic position isolated to that position, and tracked by price oracles. The profit or loss is realized from the liquidity pool providers when traders close their position and burn the synthetic tokens - liquidity providers essentially make the exact opposite of traders’ aggregate profit or loss (before accounting for fees).

Because of this, it becomes important for the protocol to manage risk - if traders use all the AMM liquidity pool to go long Bitcoin, and Bitcoin increases in price, the protocol can essentially become insolvent, unable to realize the unrealized profits on synthetic positions.

Alternatively, as long as an equal notional size of long and short synthetic positions are currently open, the pool can not lose money because it has no net exposure - it can only benefit from fees.

<aside>
💡 Incentive mechanisms designed to limit net exposure and balance risks, such as increasing fees for trades that increase an imbalance in exposure, play an important role in protecting synthetic asset protocols like Synthetix from insolvency.

</aside>

**Additional Resources**

- Article, [Synthetix suffers oracle attack, more than 37 million synthetic ether exposed](https://www.theblock.co/linked/28748/synthetix-suffers-oracle-attack-potentially-looting-37-million-synthetic-ether)
- Blog, [Debt Hedging Refresher for SNX Stakers](https://blog.synthetix.io/debt-hedging-refresher-for-snx-stakers/)

# Automated Market Makers (AMM), Nov 2018

While precursors to modern AMMs such as Kyber and Bancor existed earlier, the first case of an AMM as we now think of them arrived with Uniswap v1 in November of 2018.While the AMM has gone through several evolutions, first from constant sum to constant product, and then from two-sided liquidity to concentrated single-sided liquidity, the core concept has been largely responsible for the growth of DeFi in recent years.

The original premise was exceptionally simple, instead of a limit order book where buyers and sellers post bids and offers, liquidity providers post both tokens into a pool, and the price per token is simply governed by the ratio of tokens in the pool.

In an ETH/USDC AMM, if I buy ETH, I am selling USDC (adding more USDC tokens to the pool) and buying ETH (removing ETH tokens from the pool), thus increasing the ratio of USDC tokens per ETH token, and thus increasing the price of 1 ETH token in USDC terms.

![Source: [Uniswap v3 Explained – All You Need to Know](https://mvpworkshop.co/blog/uniswap-v3-explained-all-you-need-to-know/)](https://mvpworkshop.co/wp-content/uploads/2021/04/constant_product_curve-1-1024x526.png)

Source: [Uniswap v3 Explained – All You Need to Know](https://mvpworkshop.co/blog/uniswap-v3-explained-all-you-need-to-know/)

Curve’s further evolution of the AMM curve model was also beautifully simplistic yet powerful. In pools of highly stable or correlated assets, such as a pool of two stablecoins like USDC/DAI, traders should be able to trade lots of volume without impacting price much.

In other words, the slope of the curve should be relatively constant. This could be achieved simply by making the curve essentially the weighted average of a constant product pricing curve `x*y` and a constant sum pricing curve `x+y`, and to have the weight assigned to the constant sum portion dynamically change at different ratios of tokens in the pool so that the slope can stay relatively constant except when the ratio of tokens in the pool reaches either extreme.

![Source: [A Stablecoin Exchange](https://alvarofeito.com/articles/curve/#A-stablecoin-exchange)](https://miro.medium.com/v2/resize:fit:1280/1*V_hTefKgifN2eGmxVC_SkA.gif)

Source: [A Stablecoin Exchange](https://alvarofeito.com/articles/curve/#A-stablecoin-exchange)

![Source: [A Stablecoin Exchange](https://alvarofeito.com/articles/curve/#A-stablecoin-exchange)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5ce4d56b-b581-4e0c-98ae-950f1d43fbbd/Untitled.png)

Source: [A Stablecoin Exchange](https://alvarofeito.com/articles/curve/#A-stablecoin-exchange)

AMMs are not without their drawbacks, however, as liquidity providers are exposed to IL (Impermanent Loss), or alternatively LVR (Loss Versus Rebalancing).

IL essentially focuses on the “opportunity cost” incurred when prices change drastically because the liquidity provider would have a higher overall portfolio value had they not been providing liquidity in this scenario.

LVR is related to the hotly debated view that liquidity providers are victims of “toxic flow” and “markouts” - concepts from TradFi market making. Decentralized AMMs are generally slower to respond to price changes (the price can only update each block) than centralized exchanges (the price can update in a few microseconds). As a result, “new” prices are available on CEXs before AMMs, creating an opportunity to arbitrage between the CEX and the AMM.

For example, if the price on a CEX increases before the AMM can update, an arbitrager can buy from the old, lower price on an AMM, and sell at the new, higher price on the CEX, capturing the difference as an immediate profit.

AMM liquidity providers are “victims” of this arbitrage since they could have otherwise been market markets on a CEX order book and sold at the new high price, or chosen to increase the prices at which they are willing to sell based on the new market information.

If one were to assume liquidity providers’ token balances changed the same way they change as trades in an AMM occur, but assume that liquidity providers were able to buy/sell tokens at the prices on the CEX at the time, rather than the price in the AMM, then we could compare the realized price that liquidity providers in an AMM got vs this theoretical “rebalancing strategy” price.

LVR is defined as the difference between the two - representing how much value liquidity providers are theoretically missing out on compared to if they were executing the same trades on a CEX.

The debate about whether AMM liquidity provision is fairly compensated, or will inherently **always** be victim to LVR, and thus is not a desirable activity, is still an ongoing debate in DeFi.

On one side, researchers such as [Alex Nezlobin](https://twitter.com/0x94305) argue that AMM liquidity providers are making massive theoretical losses in LVR and markouts.

https://twitter.com/0x94305/status/1671929875878547456?s=20

On the other side, researchers and builders like [Guillame Lambert](https://twitter.com/guil_lambert) argue that LP providers are compensated for taking on risks in a similar way to selling options, and that liquidity providers don’t care about underperforming hypothetical benchmarks or that they could theoretically make better returns by being active market makers or arbitragers - they care about the passive income they are earning in practice.

https://twitter.com/guil_lambert/status/1687791021206503424?s=20

**Additional Resources**

- Twitter Spaces, [LVR Reduction: The Biggest Open Problem in DeFi (Part One)](https://twitter.com/specialmech/status/1688623676415991808?s=20)
- Twitter Spaces, [LVR Reduction: The Biggest Open Problem in DeFi (Part Two)](https://twitter.com/i/spaces/1OwxWwNkdBVxQ?s=20)
- Spreadsheet, [Uniswap v3 Impermanent Loss Calculator](https://twitter.com/phtevenstrong/status/1583599046685790208?s=20) (backup [link](https://docs.google.com/spreadsheets/d/1FQ-iPRvIMfJowWMtb1cSbfc-KoxcepXw2yOa067_vjY/edit?usp=sharing))
- Paper, [Decentralised Finance and Automated Market Making: Execution and Speculation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4144743)
- Blog, [Understanding StableSwap (Curve)](https://miguelmota.com/blog/understanding-stableswap-curve/)
- Blog, [A Stablecoin Exchange](https://alvarofeito.com/articles/curve/#A-stablecoin-exchange)
- Blog, [Back to the Basics: Uniswap, Balancer, Curve](https://medium.com/@kinaumov/back-to-the-basics-uniswap-balancer-curve-e930c3ad9046)
- Blog, [Project Insight: Uniswap - A Pioneer in the Decentralized AMM Space](https://www.bsc.news/post/uniswap-project-insight-a-pioneer-in-the-decentralised-amm-space)
- Blog, [Calculating the Expected Value of the Impermanent Loss in Uniswap](https://lambert-guillaume.medium.com/an-analysis-of-the-expected-value-of-the-impermanent-loss-in-uniswap-bfbfebbefed2)
- Thread, [“Order Flow Toxicity”](https://twitter.com/Bob_Baxley/status/1588886801363898368?s=20)
- Thread, [“GMX Price Oracles to Prevent LVR/Arbitrage”](https://twitter.com/thiccythot_/status/1602298869282381824)
- Blog, [On Path Independence](https://vitalik.ca/general/2017/06/22/marketmakers.html)
- Blog, [Uniswap v3 Explained – All You Need to Know](https://mvpworkshop.co/blog/uniswap-v3-explained-all-you-need-to-know/)
- Thread, [“Avellaneda and Stoikov Market Making Formula”](https://twitter.com/cole0x/status/1581023044511813632)
- Blog, [Usage of Markout to Calculate LP Profitability in Uniswap V3](https://crocswap.medium.com/usage-of-markout-to-calculate-lp-profitability-in-uniswap-v3-e32773b1a88e)
- Blog, [DeFi Deep Dive: Uniswap Part 2](https://web.archive.org/web/20230128073034/https://medium.com/friktion-research/defi-deep-dive-uniswap-part-2-8be77a859f47)
- Blog, [LVR: Quantifying the Cost of Providing Liquidity to Automated Market Makers](https://a16zcrypto.com/posts/article/lvr-quantifying-the-cost-of-providing-liquidity-to-automated-market-makers/)
- Paper, [Automated Market Making and Loss-Versus-Rebalancing](https://moallemi.com/ciamac/papers/lvr-2022.pdf)

# IEOs & IDOs,  Jan 2019

After the ICO craze in 2017 and 2018, the SEC began cracking down on high profile ICOs by companies such as Telegram and Kik. Furthermore, the success of all these ICOs meant lots of more tokens to trade at a time that predated DeFi, meaning that centralized exchanges were hubs of attention, users, and liquidity.

The option to conduct an offering with a centralized exchange made sense to builders and retail, in theory at least. Builders would benefit from the centralized exchanges’ internal regulatory compliance resources, KYC workflows, and existing large audiences, while retail would (in theory) get access to more curated projects than in ICOs.

Binance Launchpad conducted its first IEO (Initial Exchange Offering) in January 2019 for BitTorrent. The sale itself was a success, and BTT tokens sold out in. a few minutes.

As DeFi and DEXs have grown, central exchanges have become somewhat less important, and now tokens also conduct IDOs (Initial DEX Offering). IDOs, due to the permissionless nature of DeFi, blend some of the benefits of ICOs (not gated) with IEOs (pre-existing community).

While ICOs may be out of favor, modern builders should lean into the advantages of IEOs and IDOs, while being mindful of regulations. Where possible, these types of offerings can be helpful because builders can benefit from the existing user bases the CEX or DEX has, instead of spending marketing resources to build awareness and liquidity from scratch.

Regardless, builders should always speak to a registered legal professional before launching a token or token sale, no matter what form the token sale takes.

**Additional Resources**

- Blog, [Binance Launchpad: New Projects Coming Soon](https://www.binance.com/en/blog/launchpad/binance-launchpad-new-projects-coming-soon-287512671268392960)

# Insurance, May 2019

Nexus Mutual launched in May 2019, offering the crypto world a form of insurance against smart contract exploits called “smart contract cover”.

The concept is similar enough to traditional insurance companies in theory: charge users a recurring cost and use this cost to fund an insurance pool that is used to handle payouts for legitimate claims.

Preventing claim fraud quickly becomes a primary concern, as insurance policyholders have a strong incentive to submit claims, whereas the insurance issuer (underwriter) has a strong incentive to deny claims even when they are legitimate.

Nexus Mutual leverages economic incentives which give token holders skin in the game and encourages them to act honestly when it comes to reviewing claims by rewarding voting with consensus and slashing voting against consensus.

Additionally, managing protocol-level exposure also becomes a major concern. Risks are notoriously difficult to correctly price in insurance, as insurance largely deals with rare, but costly, “black swan” events. Not charging a sufficient premium in order to cover payouts can result in the protocol becoming insolvent and/or claim holders not being fully paid out on legitimate claims.

Today, Nexus Mutual is far from the only insurance provider in the space, but they contributed greatly to thinking on modeling, governance, incentives, and tokenomics for insurance protocols.

**Additional Resources**

- Blog, [We’ve launched! (Nexus Mutual)](https://medium.com/nexus-mutual/weve-launched-2bc8ba1049f2)
- Blog, [Nexus Mutual Launch — How our digital cooperative works](https://medium.com/nexus-mutual/nexus-mutual-launch-how-our-digital-cooperative-will-work-711822c2931d)
- Whitepaper, [Unslashed Finance - Examples and Case Studies](https://documentation.unslashed.finance/mission-cover-all-crypto-risks/examples-and-case-studies)

# Liquidity Mining & Yield Farming, Jul 2019

In July 2019, synthetic asset protocol Synthetix (formerly Haven) launched what may be the first documented case of a liquidity incentives program for a trading pair with their Synthtic asset sETH and ETH or Uniswap.

> **Today we are extremely excited to announce an experiment we will be running for the next four weeks to test whether protocol level incentives lead to a deep liquidity pool for the sETH/ETH pair on Uniswap.
Source: [Uniswap sETH Pool Liquidity Incentives](https://blog.synthetix.io/uniswap-seth-pool-incentives/)**
> 

Today the concepts of reward emissions, liquidity incentives, yield farming, and liquidity farming, are commonplace, but it’s easy to forget that these only arose within the past few years. You will not find any allocation pie charts from 2017/2018 ICOs mentioning a portion of tokens reserved for staking or liquidity rewards.

While Synthetix may have been the first case of liquidity rewards, Compound generalized the experiment to not just rewarding liquidity, but rewarding any context-specific desired behavior. In Compound’s case, that meant distributing COMP tokens to lenders and borrowers in 2020. The so called “DeFi Summer” of 2020 shortly followed, cementing incentive rewards, and yield farming behavior, as the new norm.

In extreme cases, like PancakeSwap (CAKE), token emissions completely replaced any “pre-mine” or pre-sale token allocations to investors or team members.

> **What does the PancakeSwap team get?
No pre-mine
No overzealous pie chart with the word “team” on it…**
> 
> 
> **It may be that in the future, the community decides to reward us (The PancakeSwap team) with CAKE tokens (via vote) as a thank you for providing value to the CAKE token holders, delivering on our promises, etc..**
> 
> **Source: [PancakeSwap — The Flippening.](https://medium.com/pancakeswap/pancakeswap-the-flippening-13bea39921b7#:~:text=What%20does%20the%20PancakeSwap%20team%20get%3F)**
> 

Builders should be wary of falling into the trap of assuming that these “fair launches” are always a preferable method of distribution. Even fair launches have their risks and downsides, as discussed in [Chapter 1.3](https://www.notion.so/1-3-The-Good-The-Bad-and-The-Ugly-3dfc31a65d33497394e3a4965ed90e4b?pvs=21). 

Yield farming is enabled by incentives emissions/rewards, which is really just a generalization of what others like Steemit had been doing even earlier, by rewarded users for creating and curating content.

And as seen in Steemit’s case, where rewards created warped incentives, these rewards do not always provide a net positive or sustainable benefit.

For example, on NFT marketplace Looksrare, as much as 95% of trading activity is thought to be wash trading that is only taking place to earn and dump token rewards paid to traders.

While encouraging sufficient liquidity can be helpful, especially in the modern days of AMM where passive liquidity provision is so dominant, builders should ensure they are thinking carefully about **how much** they are rewarded certain behaviors, including liquidity, and **which** behaviors are really worth rewarding. Using incentives to kickstart network value that persists after the incentives cease is much easier said than done.

We’ll get into these topics in much more detail, and with frameworks to aid decision-making, in Part Two.

**Additional Resources**

- Blog, [Uniswap Liquidity Mining Analysis](https://medium.com/gauntlet-networks/uniswap-liquidity-mining-analysis-14c739c54a9d)
- Article, [LooksRare - The NFT token everyone is looking at](https://bravenewcoin.com/insights/looksrare-token-news)
- Article, [95% of Trading Volume on LooksRare Linked to Wash Trading](https://beincrypto.com/95-trading-volume-looksrare-linked-wash-trading/)
- Blog, [Incentives structures](https://cobie.substack.com/p/incentives-structures)
- Article, [Yield farming: An investing strategy involving staking or lending crypto assets to generate returns](https://www.businessinsider.com/personal-finance/yield-farming)
- Blog, [The Fairest Launch Ever](https://medium.com/pancakeswap/the-fairest-launch-ever-5b246644ba2a#:~:text=To%20make%20the%20launch%20of%20PancakeSwap%20as%20fair%20as%20possible%20for%20market%20participants%2C%20this%20burn%20mechanism%20prevents%20the%20dev%20team%20from%20obtaining%20many%20CAKE%20tokens%3A%20the%20burn%20effectively%20makes%20the%20development%20team%20own%200%20CAKE)
- Blog, [PancakeSwap — The Flippening](https://medium.com/pancakeswap/pancakeswap-the-flippening-13bea39921b7#:~:text=What%20does%20the%20PancakeSwap%20team%20get%3F)

# Rebase Tokens, Jul 2019

Rebase tokens introduced a novel concept of a token whose token supply can change. With rebase tokens, balances held in user wallets can be altered, minting new tokens or burning existing tokens to alter the total supply, and each user’s number of tokens, though without necessarily altering the **percentage** of total tokens each user owns.

Ampleforth (AMPL) launched in 2019, as the first well-known case of a rebase token. AMPL uses this mechanism to algorithmically adjust its total supply so that, if you assume the project’s market cap holds constant, reducing the supply results in an increased price per token, and increasing the supply results in a decreased price per token.

This rebasing mechanism is used by AMPL to keep the price per token at a level that tracks an inflation-adjusted dollar - you can think of AMPL as an “inflation-proof stablecoin” that is pegged to the purchasing power of a US Dollar in 2019, not pegged to the **current** value of a US Dollar, which will be lower if inflation since 2019 has been positive.

For instance, let’s imagine that the United States inflation rate is 10% a year, and look at how buying and holding $100 worth of actual Fiat currency (cash), AMPL tokens, or a stablecoin would work out in theory.

**AMPL as an Inflation Hedge (Figures are Illustrative, Not Economic Forecasts or Predictions)**

| Year | Annual Inflation Rate | 2019 Base Purchasing Power of a $100 Bill | Number of Dollars Required to Match $100 2019 Base Purchasing Power | AMPL Target Value | 2019 Base Purchasing Power of 100 AMPL Tokens | USDC Target Value | 2019 Base Purchasing Power of 100 USDC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| End of 2019 | 10% | $100.00 | $100.00 | $1.00 | $100.00 | $1.00 | $100.00 |
| End of 2020 | 10% | $90.91 | $110.00 | $1.10 | $100.00 | $1.00 | $90.91 |
| End of 2021 | 10% | $82.64 | $121.00 | $1.21 | $100.00 | $1.00 | $82.64 |
| End of 2022 | 10% | $75.13 | $133.10 | $1.33 | $100.00 | $1.00 | $75.13 |
| End of 2023 | 10% | $68.30 | $146.41 | $1.46 | $100.00 | $1.00 | $68.30 |
| End of 2024 | 10% | $62.09 | $161.05 | $1.61 | $100.00 | $1.00 | $62.09 |
| End of 2025 | 10% | $56.45 | $177.16 | $1.77 | $100.00 | $1.00 | $56.45 |

By the end of 2025, US Dollars themselves have lost nearly 50% of their purchasing power in 2019 terms, as have stablecoins, since they track US Dollars on a 1:1 basis. But, if AMPL’s rebase mechanic is able to ensure it tracks its target value, then the value of 100 AMPL tokens retains its purchasing power in 2019 terms.

This sounds great in concept - but there’s a glaring flaw to AMPL’s stated use case as an inflation hedge.

It’s true that if the rebase mechanism ensures AMPL tracks its target value, then *100 AMPL tokens* will have retained their purchasing power. But the catch is the very same rebase mechanism that is ensuring AMPL tracks its target value is doing so **by changing the number of tokens each wallet owns.** All else equal, since the rebase mechanism is reducing supply in order to increase AMPL price, holders that started with 100 tokens would expect to have **fewer** than 100 tokens, and thus still lose purchasing power!

![Source: [The Truth about Rebase Tokens](https://web.archive.org/web/20220106151642/https://medium.com/@PAPADAO/the-truth-about-rebase-tokens-a7dc8d518cd4)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c9fe0a09-9670-4f0b-8abb-b7f2013d4867/Untitled.png)

Source: [The Truth about Rebase Tokens](https://web.archive.org/web/20220106151642/https://medium.com/@PAPADAO/the-truth-about-rebase-tokens-a7dc8d518cd4)

In other words, while supply and price per token can be influenced by the rebase mechanism, market cap can not. Reducing supply does increase price if you hold market cap constant, but it doesn’t **increase** the market cap itself.

It doesn’t matter to each user if the *price per AMPL token* tracks inflation*,* what matters is that the **value of their total AMPL position** tracks inflation.

In practice, this means that AMPL requires an ever-growing amount of incoming capital because it requires an ever-increasing **market cap** (not price per token) in order to effectively preserve the holder’s purchasing power against inflation. This reliance on a continually increasing market cap is something most if not all rebase tokens suffer from, making them unsustainable at large scale and vulnerability to similar risks to those that UST was exposed to before collapsing.

The **price per token** may continue to increase or track its target price, even if the protocol’s market cap collapses, but the **value of each user’s holdings** would not.

Due to these inherent limitations, rebase tokens, similar to bonding curves, are an intriguing mechanism that builders should be familiar with, and which may be useful in very specific contexts where they are fit for purpose, but which not often used in practice.

Case in point - today AMPL’s market cap sits around $30mm. Its adoption has fallen more than 95% from its all-time high of a $688mm market cap, and the price per token trades outside its target range for weeks at a time.

**Additional Resources**

- Blog (Archived), [The Truth about Rebase Tokens](https://web.archive.org/web/20220106151642/https://medium.com/@PAPADAO/the-truth-about-rebase-tokens-a7dc8d518cd4)
- Blog, [Rebase! The Implications of Supply Smoothing](https://www.publish0x.com/block-enthusiast-an-exploration-of-things/rebase-the-implications-of-supply-smoothing-xropreg)
- Thread, [“why Ampleforth (AMPL) is the biggest facepalm in crypto history”](https://twitter.com/samkazemian/status/1287705804875825154)
- Dashboard, [AMPL Rebase Dashboard](https://www.ampleforth.org/dashboard/)

 

# Proof of Physical Work (PoPW) & Decentralized Infrastructure, Jul 2019

Proof of Work blockchains or decentralized file storage protocols like Sia can be viewed as the earliest example of decentralized infrastructure, but it wasn’t until later arrivals like Helium in July 2019 that use cases for specialized physical infrastructure beyond file storage or proof of work.

https://twitter.com/Old_Samster/status/1555620023003013122?s=20

Helium has so far been a textbook example of using token emissions to bootstrap the supply side, building a global network of IoT devices and hotspot owners.

But as we discussed in earlier chapters, overcoming the bootstrapping problem requires acquiring users on both the demand and supply side. If there is no demand, even the best tokenomics can not save the product.

One of the biggest challenges with token rewards for the demand side is Sybil attacks. Rewards supply can be more objectively verified, a node either is running or it isn’t. But if rewards are distributed to demand, for **used** capacity, then an incentive is created to use fake activity to earn rewards.

This dynamic is why NFT marketplaces that pay people to place trades, like LooksRare, see so much wash trading, and why protocols like Filecoin have such low capacity utilization rates - they can more effectively incentivize supply capacity than demand.

It’s also a large part of why Filecoin launched Filecoin Plus, allowing for curating specific demand side participants, which cuts down on Sybil attacks, allowing for more effectively incentivizing and onboarding demand. It’s no surprise Filecoin’s active deals are almost entirely composed of Filecoin Plus activity.

<aside>
💡 The lessons for builders here are that effectively incentivizing demand side requires taking Sybil resistance measures, and that validating the existence of user demand is important before heavily investing in building out cavity with supply side incentives.

</aside>

**Additional Resources**

- Article, [Crypto Darling Helium Promised A ‘People’s Network.’ Instead, Its Executives Got Rich](https://www.forbes.com/sites/sarahemerson/2022/09/23/helium-crypto-tokens-peoples-network/?sh=2d8335973166)
- Article, [Embattled Helium is attempting a second act as a crypto-powered mobile network](https://fortune.com/crypto/2022/09/27/embattled-helium-attempting-crypto-powered-mobile-network/)
- Dashboard, [Starboard Ventures’ Filecoin Dashboard](https://dashboard.starboard.ventures/dashboard)

# Staking Rewards (Non-PoS), 2019

The term “staking rewards” originally was only used in the context of Proof-of-Stake consensus mechanisms, where users locked up tokens to participate in consensus, and earned staking rewards for doing so.

Yet somewhere along the way and with the rise of DeFi, the term “staking” became watered down to describe **any** case where users lock up tokens, even when this mechanic is entirely unnecessary and unrelated to the actual functioning of the product itself.

This isn’t to say that locking up tokens for reasons other than Proof-of-Stake consensus can never be useful or should not be rewarded. Locking up collateral as a Chainlink oracle, depositing DAI to earn the savings rates, or SushiSwap’s vampire attack to reward staking of Uniswap LP tokens are all examples of cases where locking up tokens had a specific benefit to the protocol.

Yet as the term staking became more general, staking itself rose in popularity simply as a cheap means to try to prevent tokens from being sold. If holders are receiving a yield to stake, and maybe even locked in while doing so without the option to unstake, they may be less likely, or even unable to, sell tokens.

> **Simply paying users for not selling, payment received in the same asset that they are not selling, seems like pretty late-stage in the games of ponzi creation… We should’ve protested the repurposing of the term “staking” from being a reward for work in a consensus mechanism, with risk of losing collateral, into this current “idk just lock it off market to receive more coins risk-free lol” but it’s probably too late for that now.
Source: [ApeCoin & the death of staking](https://cobie.substack.com/p/apecoin-and-the-death-of-staking)**
> 

On its own though, this is of course not a sustainable mechanism, because if a token has no usage, value, utility, or purpose other than it can be staked to earn more of that very token, staking only delays the inevitable dump of tokens and crash in token price.

<aside>
💡 Before adding staking, builders should ask themselves if there is a specific benefit locking up tokens brings to the product in terms of align incentives, skin in the game, improved security, etc, or if they are simply just trying to find reasons for holders not to sell.

</aside>

**Additional Resources**

- Blog, [ApeCoin & the death of staking](https://cobie.substack.com/p/apecoin-and-the-death-of-staking)
- Blog, [Why the Dai Savings Rate is a Game-Changer for the DeFi Ecosystem, and Beyond](https://blog.makerdao.com/why-the-dai-savings-rate-is-a-game-changer-for-the-defi-ecosystem-and-beyond/)

# The Curve Wars, Aug 2020

Curve’s CRV token was launched in August 2020, as a means to add additional incentives to liquidity providers on the platform. Curve’s success in attracting liquidity resulted in project competing to farm the yields CRV token distributions offers (such as Yearn Finance’s yCRV vault to automatically yield farm), and led to projects with their own native tokens to try to increase liquidity being provided for their own tokens by directing Curve emissions.

The Curve Wars had begun.

Yield farming and liquidity mining quickly became the dominant narratives of “DeFi Summer”, with yields, strategies, and players changing every day.

Much of Curve’s rise to fame is attributed to its tokenomics mechanism for **vote escrowed** Curve. Holders of CRV tokens lock up tokens by staking them for up to 4 years, in return for veCRV tokens - the longer the stake, the more veCRV.

These veCRV tokens are used in weekly “gauge weight” which determine how much each liquidity pool is incentivized. Pools with more weight receive greater rewards, and thus can expect to see more liquidity, all else equal.

![Source: **[CRV wars: understanding the race to accumulate power to influence Curve Finance protocol](https://tokenbrice.xyz/crv-wars/)**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3abfa26f-1255-4889-8e46-eed55475c177/Untitled.png)

Source: **[CRV wars: understanding the race to accumulate power to influence Curve Finance protocol](https://tokenbrice.xyz/crv-wars/)**

It was not long before an entire ecosystem sprang up around farming CRV rewards, and entirely new projects were created to aggregate veCRV voting power (Convex), since the more concentrated one’s voting power, the more influence over directly rewards they they have.

Given the popularity of veCRV it’s easy to understand why the vote escrow mechanism has subsequently been copied by many projects as a way to try to lock up supply to reduce selling pressure.

But, despite being frequently copied, Curve’s vote escrow mechanism is not without its flaws and inefficiencies.

https://twitter.com/Gabe_PZ/status/1570120713432080386?s=20

Better value alignment would involve aligning rewards with value created for the protocol. For example, perhaps veCRV voters are slashed if they vote for pools which generate a lot less fees than emissions, and/or earn extra emissions when the pools they vote for earn more fees than emissions. This would encourage directing rewards, and thus liqudity, to the most value add activities for the protocol.

<aside>
💡 Builders must remember that Curve itself launched a valuable product that created value for users - an AMM with considerable lower slippage costs when trading correlated or stable asset pairs. One cannot replicate the success of veCRV by taking the “ve” portion (the vote escrow mechanism) and slapping it on any token or product that creates no value. Vote escrow mechanisms that are not ultimately supported by demand and value accrual are ultimately unsustainable.

</aside>

Though veCRV holders receive protocol revenue distributions, it remains possible that even veCRV itself will prove to be unsustainable if emissions are disproportionate to protocol revenues in the long term.

**Additional Resources**

- Dashboard, [veCRV](https://dune.com/banteg/misc)
- Blog, [Bribing veCRV gauges 101](https://andrecronje.medium.com/bribing-vecrv-gauges-101-8f6e4506bb62)
- Blog, [CRV wars: understanding the race to accumulate power to influence Curve Finance protocol (Part One)](https://tokenbrice.xyz/crv-wars/)
- Blog, [Advanced CRV warfare: analysis of protocols built on top of Curve and Convex (Part Two)](https://tokenbrice.xyz/crv-wars-l2/)
- Blog, [The Curve Wars Explained: When DeFi Becomes Aggressive](https://dappradar.com/blog/the-curve-wars-explained-when-defi-becomes-aggressive)
- Article, [Curve's "vote locking" feature boosts CRV rewards by up to 2.5x](https://decrypt.co/38923/curves-vote-locking-feature-boosts-crv-rewards-by-up-to-2-5x)
- Blog, [Tokenomics is back (thanks to CRV)](https://doseofdefi.substack.com/p/tokenomics-is-back-thanks-to-crv?s=r)
- Thread, [CRV, veCRV, and the Curve Wars](https://twitter.com/puntium/status/1503859941039558659?s=20&t=v2T1RQCDQdcOxn-2D5iMKw)
- Blog, [Tokenomics Musings: ve tokens and alternatives](https://mirror.xyz/0x1e35A719f1d68da02DEf39Bde510c9cc4efDC84B/qe5TdeXrnT8OuuQobQN7kZLhsnQQb92ypSuKyznBlsc)
- Blog, [What’s veTokenomics? Analysis of 20 veToken Ecosystem Protocols](https://medium.com/@Ignas_defi_research/whats-vetokenomics-analysis-of-20-vetoken-ecosystem-protocols-7714ad56dc3e)
- Blog, [The Pillars of Tokenomics & The ve Token Model](https://captainbtc.substack.com/p/the-pillars-of-tokenomics-and-the?s=r)
- Article, [Governance of DeFi Giant Curve in Flux as Smaller Convex Exerts Control](https://thedefiant.io/curve-convex-governance-crv-control)
- Blog, [What Is Convex Finance (CVX)? A Powerful DeFi Yield Farming Platform Explained](https://academy.shrimpy.io/post/what-is-convex-finance-cvx-a-powerful-defi-yield-farming-platform-explained#:~:text=Convex)

# Vampire Attacks, Sep 2020

In early September 2020, SushiSwap launched an attack to draw users away from Uniswap to their protocol, in an ingenious counter attack to their competitor’s network effects.

SushiSwap offered rewards to Uniswap users who brought Uniswap LP tokens over to SushiSwap and staked them there, allowing SushiSwap to redeem these LP tokens for the underlying tokens in Uniswap AMM pools, and move them over the SushiSwap’s own AMM pools.

In effect, SushiSwap bribed users to convert their Uniswap LP into SushiSwap LP by redistributing tokens as bribes - though the user experience to do so was even smoother, as it was as simple as staking Uniswap LP to earn rewards.

The attack had an immediate effect on TVL, with SushiSwap actually exceeding Uniswap’s TVL.

![Source: [Messari](https://twitter.com/MessariCrypto/status/1318229445581430798)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25ea6d93-cbde-4a49-91a1-2dbd7d982f3c/Untitled.png)

Source: [Messari](https://twitter.com/MessariCrypto/status/1318229445581430798)

SushiSwap’s success was short lived however, partially due to Uniswap’s response by launching their own token. Regardless, even after most TVL returned to Uniswap, TVL on SushiSwap remained considerably higher than it had been before the vampire attack had been launched.

<aside>
💡 Vampire attacks remain a clever go to market strategy, particular as a potential counter to an existing competitors established network effect. One can think of vampire attacks as a form of “adversarial airdrop”, that not only attracts new users, but directly draws users away from a particular competitor. To have a sustained effect, a vampire attack must be paired with a strong product and well designed tokenomics that make it worthwhile for users to stick around not just immediately dump the token and return to the competitor.

</aside>

SushiSwap is far from the only example of a vampire attack. LooksRare conducted a similar attack on OpenSea when it first launched as well, by airdropping LOOKS to addresses that had spent more than 3 ETH on OpenSea in the second half of 2021.

Once a competitor has a well established network effect, it is extremely difficult to overcome without an drastically better product. Vampire attacks won’t lead to users moving to an equivalent product, but they can lead to users giving your product a shot that they otherwise wouldn’t.

**Additional Resources**

- Blog, [Vampire attacks: A theory (and thread) on 'blood sucking' platform competition](https://a16zcrypto.com/posts/article/vampire-attacks-competition/)
- Paper, [A Simple Theory of Vampire Attacks](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4377561)
- Blog, [The Vampire Attack Phenomenon: A Closer Look](https://gbirioluwaseun.medium.com/the-vampire-attack-phenomenon-a-closer-look-a429442c48ea)
- Blog, [Vampire Attacks - ‘I vant to drain your liquidity’](https://avark.agency/learn/article/vampire-attacks-i-vant-to-drain-your-liquidity/)
- Article, [A Guide and Short History of SushiSwap](https://beincrypto.com/a-guide-and-short-history-of-sushiswap/)
- Blog, [SUSHI Token Economics: The Impact of Inflation](https://insights.glassnode.com/sushi-token-economics-impact-of-inflation/)
- Article, [‘Overvalued’ SUSHI Dumps 80% Ahead of Platform Migration](https://beincrypto.com/overvalued-sushi-dumps-80-ahead-platform-migration/)
- Article, [Another NFT marketplace launches ‘vampire attack’ against OpenSea](https://forkast.news/headlines/nft-marketplace-vampire-attack-opensea/)

# MEV, 2020

MEV (Miner Extractable Value) arises from the fact that miners (or validators on PoS) chose the order of transactions within blocks. In essence, MEV is the value that can be created based on the order, such as by placing one’s own frontrunning trade in front of a large buy order transaction.

![Source: [Inevitable Ethereum: MEV Example](https://inevitableeth.com/home/concepts/mev/example)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de2eb34e-775d-4454-be01-b1da3d5b75fb/Untitled.png)

Source: [Inevitable Ethereum: MEV Example](https://inevitableeth.com/home/concepts/mev/example)

MEV thus existed the moment the first rudimentary DEXs came into being, or even earlier. It’s possible miners put their own transactions into quick to sell out ICOs ahead of other transactions. That said, it wasn’t until later that it became such a big deal, because the DeFi Summer of 2020 brought more on-chain uses cases, applications, and most importantly of all lots of more capital.

The rise of AMMs handling large amounts of trading flows meant that MEV became a very profitable business.

While not **all** types of MEV are harmful, popular forms of MEV like sandwich attacks and frontrunning leeches value from users in a way that would be considered illegal market manipulation in traditional finance, and has contributed to concerns over Ethereum’s censorship resistance due to most MEV-boost relays censoring transactions to be compliant with OFAC.

While not directly an artifact of MEV itself, since validators which run MEV-boost can increase staking returns by selling blockspace to MEV searchers, validators have an incentive to use MEV-boost, meaning that Ethereum’s level of centralization converges towards to level of centralization of MEV-boost relays.

Proposals to “solve” MEV largely break down into four schools of thought.

![Source: [The Four Quadrants of MEV Protection](https://bennyattar.substack.com/p/mev)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3c09f578-b9a3-4552-9b86-7776d41b4bac/Untitled.png)

Source: [The Four Quadrants of MEV Protection](https://bennyattar.substack.com/p/mev)

**Additional Resources**

- Blog, [What is MEV Boost?](https://www.alchemy.com/overviews/mev-boost)
- Blog, [Time, slots, and the ordering of events in Ethereum Proof-of-Stake](https://www.paradigm.xyz/2023/04/mev-boost-ethereum-consensus)
- Blog, [How our team makes millions in crypto risk-free](https://deepfivalue.substack.com/p/how-our-team-makes-millions-in-crypto)
- Thread, “[MEV, relays, blockbuilding, Flashbots, Ethereum](https://twitter.com/JackNiewold/status/1582118436838133760)”
- Thread, [“Can crypto actually *improve* online trust via MEV auctions?”](https://twitter.com/tarunchitra/status/1620162562489819143?s=20)
- Forum, [MEV-SGX: A sealed bid MEV auction design](https://ethresear.ch/t/mev-sgx-a-sealed-bid-mev-auction-design/9677)
- Paper, [High-Frequency Trading on Decentralized On-Chain Exchanges](https://arxiv.org/abs/2009.14021)
- Blog, [The Four Quadrants of MEV Protection](https://bennyattar.substack.com/p/mev)

# Protocol Owned Liquidity (Olympus DAO), Apr 2021

Olympus DAO launched in April 2021, with a unique model that ultimately drew quite a lot of attention, with a market cap that peaked at $4.36bn before collapsing more than 95%, leaving most people involved badly burned.

Olympus’ main selling point was its extremely high APY, which was fueled by a rebase mechanic that minted new OHM tokens and distributed them to stakers when new investors purchase OHM tokens to fund the treasury - essentially transferring the economic value of claims to treasury assets directly from new incoming investors into the hands of earlier investors.

You’d be right to say that sounds relatively ponzinomic, and it certainly fails the basic ponzinomic sniff test.

https://twitter.com/AlanaDLevin/status/1551905122971795456?s=20

So how and why was Olympus able to rise to such success? While earlier instances of rebase tokens existed, OHM introduced the concept of protocol owned liquidity, as well as a highly influential marketing campaign centered on game theory to advertise the extremely high yields from its ponzinomic staking mechanism.

At the time, protocols were competing for liquidity for their native tokens (Curve Wars), but bribing or incentivizing LPs to provide liquidity is temporary. Those LPs are, as rational actors, seeking to maximize their own returns, and so as the incentives slow down, the liquidity leaves - essentially the liquidity is only **rented** instead of **owned**.

Olympus DAO introduced the concept of buying their own LP tokens, for example ETH/OHM Uniswap LP tokens, so that the treasury owns its own liquidity. In practice this meant liquidity providers sold LP tokens to the OHM treasury in exchange for OHM tokens at a discount to market prices.

Owning their own liquidity was advertised as a way to ensure long term liquidity for OHM, in addition to representing a theoretical revenue source, since LP tokens earn trading fees.

Once again, this mechanic too should set off ponzinomic warning flags, as it’s entirely self referential, as earning fees for OHM token liquidity only occurs if OHM tokens are being traded - thus, OHM is still a function of price speculation, rather than organic revenue and value creation.

> **Accrual of LP fees from $OHM trading does not count [as value generation], as that is again simply shuffling around money between participants entering and exiting a closed system… 
Source: [A correct model of Olympus DAO](https://milkyeggs.com/crypto/a-correct-model-of-olympus-dao/)**
> 

This is not to say that all protocol owned liquidity is inherently unsustainable.

<aside>
💡 Protocol owned liquidity can be sustainable as a **value accrual** mechanism (e.x. Maker DAO buyback and LP), but it is not a replacement for a value creation mechanism, and can not be sustainable without being funded by underlying value creation.

</aside>

While OHM advertised a use case as intending to become a “decentralized reserve currency”, this activity alone does not create economic value other than the returns generated by investing the treasury assets (investment fund revenues). Furthermore, it’s questionable whether it’s even logical for an ERC-20 token can even theoretically become a form of money, as this would seem to require the base layer token itself being a better form of money that supersedes the ERC-20 tokens dependent on its security budget.

https://twitter.com/cyounessi1/status/1483594686531055625?s=20

With a questionable use case, and no protocol revenues other than investing treasury assets, which any investment fund or treasury could provide without protocol owned liquidity or a rebase powered, staking mechanism, we are still left with the question of how OHM became so popular at the same time as it was receiving widespread criticisms of its model. (The original quoted Tweet below was published at the very height of OHM’s success in November 2021).

https://twitter.com/crypto_notte/status/1480642777780207616?s=20

What Olympus DAO did best was marketing, centering their efforts around the “(3,3)” game theory inspired meme. According to this simplified game theory payoff structure, if every stakes and never sells, the price will keep appreciating forever, leaving everyone involved with a positive **unrealized** collective gain while tokens remained locked up and illiquid.

> **Collective losses can hide in illiquidity until they get realized.
**Source: [Of Smoke and Mirrors.. Part I](https://medium.com/@game_theorizing/of-smoke-and-mirrors-part-1-117c1f92e186)**
> 

Even if we take the game theory at face value, this conclusion ignores the fact that in repeated games, ideal strategies can be radically different than the dominant strategy assuming a single round is played.

<aside>
💡 For example in prisoner’s dilemma, when the game is only played once, the ideal strategy is to rat on your fellow prisoner, resulting in both prisoners betraying each other. But this is not the ideal strategy in empirical studies and simulations of **repeated games.** When the game is repeated, the best performing strategies become combinations of the “grim” or “spiteful” strategy, and the “tit-for-tat” strategy.

</aside>

In the grim/spiteful strategy, a prisoner remains loyal to their opponent **until they are betrayed** by their opponent, after which they betray their opponent every round for the *entire remainder of the game*. In the tit-for-tat strategy, a prisoner does what their opponent did last round. I.e. they are loyal if their opponent was loyal last round, and they betray them if their opponent betrayed them in the last round.

Simulations show that these behaviors become the ideal player behaviors that emerge when the game is repeated.

> **We note that [the best performing strategies] are almost all mixtures of two basic strategies: *tit_for_tat* and *spiteful*. This suggests that *tit_for_tat* is not severe enough, that *spiteful* is a little too much severe and that finding ways to build hybrids of these two strategies is certainly what gives the best and most robust results.
Source: [New Winning Strategies for the Iterated Prisoner's Dilemma](https://www.jasss.org/20/4/12.html#7.10)**
> 

This is worth noting because staking OHM, like most activities in the real world, is not a game that is played once. The game is played repeatedly, each day, each block, when participants have to decide to begin staking, continue staking, or stop staking (to name just a few of their options).

In a repeated game environment, the better performing strategy can change from mutually staking OHM to always dumping any earned OHM once other OHM holders first begin to sell tokens (grim/spiteful strategy), or dumping only when others sell (tit-for-tat strategy).

Empirically this aligns with what actually occurred, as selling pressure compounded as a self-reinforcing behavior.

If we step back and critically examine OHM’s game theory payoff structure, the red flags get bigger. The (3,3) staking payoff is obviously a gross oversimplification that ignores the marginal utility of money, and assumes participants value **unrealized** gains as perfectly identical to **realized** gains.

In the words of FreddieRaynolds, who publicly called the collapse of LUNA/UST at least six months in advance:

https://twitter.com/FreddieRaynolds/status/1439656351110680577?s=20

By definition, if no one ever sells, price can never go down, and everyone can make theoretical, unrealized gains forever - but for each dollar of unrealized gains a holder makes, the marginal utility of the next dollar of unrealized gains shrinks. The payoff structure (which is entirely subjective in the first place) quite literally changes, it is no longer (3,3) to stake, it becomes (<3,<3). (**The similarity of that notation in appearance to “(** ❤️,❤️**)” is one of life’s beautiful ironies).**

At the same time, the payoff of selling, in order to **realize** some or all of the unrealized gains, increases, as in reality, **realized** gains have a far greater value and utility than **unrealized** gains. This is arguably exaggerated even further by irrational biases, as [data demonstrates that traders have a psychological bias to close winning positions early](https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/areinvestorsreluctant.pdf) (i.e. people tend to close positions with unrealized **gains** much sooner than positions with unrealized **losses**).

In the context’s of OHM’s payoff structure, both these factors would contribute to selling become a higher and higher subjective payoff relative to staking as the game continues and as holders accrue **unrealized** gains.

Thus, the simplistic view of the (3,3) payoff structure as a constant and objective representation of preferences is deeply misleading.

> **(3,3) is simply and transparently gibberish… This statement implies that the act of purchasing and staking $OHM is positive-sum. However, buying, staking, and selling $OHM are essentially all “rearrangements” of money within a closed system. In the absence of positive value generation (*e.g.,* legitimate business activity), it is *a priori* impossible for all participants to experience a (3, 3, …, 3) outcome, for the simple reason that shuffling money around in a closed system without any productive activity cannot create positive value…

Note that in the situation where all participants buy and stake and nobody sells, everyone can have arbitrarily large paper gains; however, it is impossible for all participants to realize gains at the maximal price and the amount of money flowing out must necessarily be strictly limited by the amount of money which flowed in…
Source: [A correct model of Olympus DAO](https://milkyeggs.com/crypto/a-correct-model-of-olympus-dao/)**
> 

As an (obvious) result, it was inevitable that a large portion of stakers eventually began to sell, at which point the speculative FOMO began to unwind, creating a self reinforcing cycle as **unrealized** gains evaporated and staking APYs declined. A death spiral.

This occurred even though the token was ostensibly backed by the treasury for a value of 1 DAI, because OHM’s market cap was extremely undercollateralized by the treasury - a product of encouraging speculative behavior to farm the unsustainable staking rewards APY.

https://twitter.com/norswap/status/1498358053317459969?s=20&t=3yfFqntFdYb-twTHzzvbfw

Ironically, OHM’s rebase powered staking yield mechanism was entirely unrelated to, and unnecessary for, designing a token with a stable value, or for designing a treasury reserve that distributes proceeds from treasury investments.

The staking mechanism was purely a ponzinomic fundraising mechanism - entirely orthogonal to operations, value creation, and OHM’s stated purpose. Thus in essence, in its original formulation, OHM was an investment fund that used a ponzi to raise its initial assets under management. As the former head of risk at MakerDAO puts it:

https://twitter.com/cyounessi1/status/1483594693615226880?s=20

At best, OHM was an interesting case of unintentionally misleading marketing, built on a flawed understanding of the practical limitations of game theory, combined with hyperinflationary tokenomics that fueled unsustainable APYs for drawing further marketing attention.

At worst, OHM was designed to intentionally mislead retail investors and transfer wealth from retail to the treasury and early insiders.

> **In prioritizing value transfer (from long-term and passive participants to short-term and extractive ones) over value creation, [OHM’s staking] mechanism weakened the long-term foundations of the protocol.”
Source: [Token Design for Serious People](https://jumpcrypto.com/token-design-for-serious-people/)**
> 

It is unfortunate that protocol owned liquidity may always carry the ugly legacy of OHM, because POL is as brilliantly simple as a protocol itself providing liquidity in an AMM. This can be done as a value accrual mechanism (buyback tokens with protocol revenues to provide LP, or provide single sided LP with protocol revenues). Or it can be done in lieu of a one-time token sale event, as putting tokens in a liquidity pool essentially functions as an ongoing token sale.

As for Olympus DAO itself, its clear the original mechanisms were not sustainable or productive - and in fact OHM has since abandoned the staking mechanism, demonstrating they now acknowledge it was not sustainable. The existing treasury only creates value in so far as it is invested for **superior risk adjusted returns** than other potential investments - otherwise Olympus DAO has no marginal purpose or value contribution.

If you define success as raising a large treasury from unsuspecting retail with misleading marketing, wildly unsustainable APYs, and a predatory fundraising mechanism totally unnecessary for building the stated objective, then OHM was a success.

However if you think destroying your reputation with most of your user base and collapsing more than 95% in market cap just to bootstrap an initial treasury is not a viable long-term growth strategy, then OHM is a cautionary tale, not a success case.

https://twitter.com/CarlKVogel/status/1487512145420029953?s=20

**Additional Resources**

- Blog, [The (3, 3) Gods’Father](https://medium.com/@game_theorizing/of-smoke-and-mirrors-part-2-the-godsfather-cd24ff7476da)
- Blog, [Olympus Has Fallen: A Postmortem on the (3,3) Experiment](https://medium.com/@juicyarbol/olympus-has-fallen-a-postmortem-on-the-3-3-experiment-87c316791612)
- Blog (Archived), [The Truth about Rebase Tokens](https://web.archive.org/web/20220106151642/https://medium.com/@PAPADAO/the-truth-about-rebase-tokens-a7dc8d518cd4)
- Blog, [Diminishing marginal utility of income and wealth](https://www.economicshelp.org/blog/12309/concepts/diminishing-marginal-utility-of-income-and-wealth/)
- Thread, [“why we stopped working on Olympus before launch”](https://twitter.com/MimirSolutions/status/1486121940913905670?s=20)
- Thread, [“what I've learned about Olympus since I publicly skewered them for running a ponzi”](https://twitter.com/cyounessi1/status/1483594676145954818?s=20)
- Blog, [Olympus DAO from Primary Sources](https://norswap.com/olympus/)
- Thread, [“economic analysis of OlympusDAO”](https://twitter.com/norswap/status/1498358036733194243?s=20)
- Paper, [New Winning Strategies for the Iterated Prisoner's Dilemma](https://www.jasss.org/20/4/12.html#7.10)
- Slides, [Infinitely Repeated Games](http://www.econ.uiuc.edu/~hrtdmrt2/Teaching/GT_2015_19/L12.pdf)
- Paper, [Are Investors Reluctant to Realize Their Losses?](https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/areinvestorsreluctant.pdf)
- Paper, [The Disposition to Sell Winners too Early and Ride Losers too Long](https://www.researchgate.net/publication/313248569_The_Disposition_to_Sell_Winners_too_Early_and_Ride_Losers_too_Long)
- YouTube, [Tokenomics Skills #8: Game Theory (Olympus DAO case study)](https://www.youtube.com/watch?v=lL13Puz-oSE&t=512s)
- YouTube, [Tokenomics / Ponzinomics case study: Olympus DAO](https://www.youtube.com/watch?v=eW6G6JxiOMc)
- YouTube, [OlympusDAO OHM Crash](https://www.youtube.com/watch?v=uY9YCbnletc&t=920s)
- Article, [Olympus DAO is under fire after price drop and liquidations](https://thedefiant.io/olympus-under-fire)

# L2 Rollups, Aug 2021

While Polygon (originally known as the Matic Network, hence their token MATIC) launched in 2017 as a sidechain, Arbitrum was the fist Ethereum Layer 2 rollup to launch. Arbitrum arrived in August 2021, follower shortly after by Optimism in December 2021.

Both Arbitrum and Optimism are optimistic rollups, meaning that transactions are “optimistically assumed” to be valid until proven otherwise. In practice, this means that in order to bridge out, a window of time has to be reserved within which transactions can be cancelled.

Whereas in Layer 1s, miners product blocks and order transactions within blocks, on Layer 2s, sequencers order transactions and post rollups to the L1.

https://twitter.com/jarrodWattsDev/status/1689851728571547648

zkRollups on the other hand, unlike optimistic rollups, require verifiable proofs to be posted in order to produce blocks. This eliminates the need for reserving a window of time to bridge back to the L1, but comes at a higher cost, since producing and verifying proofs is computationally expensive.

In reality, L2 sequencers remain centralized, though most L2s at least claim to be working on moving towards using decentralized sequencers. Technical and economic challenges remain with aligning incentives and ensuring security without sacrificing the intended benefits of the L2 in the first place.

**Additional Resources**

- Article, [Arbitrum vs. Optimism: What’s the Difference Between These Ethereum Rollups?](https://www.makeuseof.com/arbitrum-vs-optimism-whats-the-difference/)
- Article, [Ethereum's Layer 2: The Story So Far And What To Expect Next](https://hackernoon.com/ethereums-layer-2-the-story-so-far-and-what-to-expect-next-kn41342c)
- Forum, [L2Bridge Risk Framework](https://gov.l2beat.com/t/l2bridge-risk-framework/31)
- YouTube, [Making sense of rollup economics](https://www.youtube.com/watch?v=BmQnb7TN3Ho)
- Blog, [Rollups-as-a-Service Are Going To Zero](https://www.neelsomani.com/blog/rollups-as-a-service-are-going-to-zero.php)
- Blog, [Zero-knowledge Proofs, the future of privacy friendly digital products](https://uxplanet.org/zkproof-4509f8c83959)
- Forum, [How can I explain a Zero Knowledge Proof with minimal mathematics](https://math.stackexchange.com/questions/1505402/how-can-i-explain-a-zero-knowledge-proof-with-minimal-mathematics)

# Escrowed Rewards (GMX), Jan 2022

Not to be mistaken for Curve’s **vote escrow** mechanism, in which CRV tokens are **staked** to create *vote escrowed* tokens as veCRV, GMX rewards that are distributed to GMX stakers are made in an **escrowed** form as esGMX - meaning they are not initially tradeable or transferrable.

Escrowed esGMX tokens can be converted over time time into liquid GMX tokens, essentially a vesting or “unescrowing” process that requires locking up GMX tokens with esGMX tokens to do so.

This mechanic introduces several benefits by reducing the utility and value of staking rewards distributed to *mercenary capital*, while preserving the value that is distributed to long term users, better aligning the distribution of rewards to the types of users and behaviors that create value for GMX.

GMX also uses another mechanic, Multiplier Points, which accrue when GMX tokens are staked in proportion to the number of staked tokens. MP themselves then earn staking rewards, thus creating a compounding effect that rewards consistent, sustained staking since MPs are proportionally burned when GMX is unstaked.

Unlike veCRV, which encourages users to constantly re-lock in order to preserve voting power which would otherwise decay, GMX’s MP mechanic creates an opportunity cost to stop staking once a user has already been doing so, since unstaking would burn MPs and reduce the rate at which that user can earn future rewards.

While GMX’s escrowed rewards (esGMX) and compounding staking rewards (Multiplier Points) may sound quite ponzinomic, these mechanics are not inherently unsustainable. To be clear, they can absolutely be unsustainable when staking rewards are paid out of thin air or when rewards are excessively inflationary.

That said, when the aggregate reward pool is capped to a manageable level of tail emissions inflation, or the rewards are entirely sourced from distributing protocol revenues, this means that even with compounding MPs, the protocol’s overall emissions are not unsustainably forever increasing. Instead, stakers of MPs are earning a larger **proportional share** of rewards.

<aside>
💡 GMX and CRV remain two of the most influential projects to modern tokenomics. Builders should familiarize themselves with both models.

</aside>

**Additional Resources**

- Whitepaper, [GMX - Rewards](https://gmxio.gitbook.io/gmx/rewards)
- Blog, [Trustless Governance and Value Accrual](https://mirror.xyz/jaypowcrypto.eth/6c3BhMRzzet3NUFocMSQuj5zZ8CTwDud5c6CzFH-zEg)
- Blog, [Tokenomics Musings: ve tokens and alternatives](https://mirror.xyz/0x1e35A719f1d68da02DEf39Bde510c9cc4efDC84B/qe5TdeXrnT8OuuQobQN7kZLhsnQQb92ypSuKyznBlsc)

# Ethereum PoW vs PoS (”The Merge”), Sep 2022

It’s hard to understate just how significant of a milestone the transition of Ethereum from Proof-of-Work to Proof-of-Stake on September 15th 2022 was. This remains true whether you think moving to PoS was a good idea or not. For example proponents would say the energy savings of PoS over PoW are a vital step forward, whereas opponents recognize that moving to PoS was a significant factor in anti-Bitcoin rhetoric ramping up under the guise of environmentalism.

Criticisms of the move to PoS mainly center on the increased degree of validator centralization, exposing the Ethereum chain to the threat of censorship by validators in certain jurisdictions, or influenced by restrictive jurisdictions. These validators would theoretically censor transactions by excluding them for blocks they propose.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/56fa9d25-08dd-4f7a-98ee-b836f10b2731/Untitled.png)

MEV-boost is an optional service validators can use to increase their APR by outsourcing block production to the highest bidders. These bidders are in turn bidding to produce blocks because if they product the block they can order transactions in the block, and capture any MEV.

After the merge, the percentage of OFAC compliant blocks reached as high as nearly 80%, and though it’s come down considerably since then, it’s still hovering around 50% of all blocks.

This has since raised questions in the community about how to potential respond to or treat validators that are knowingly censoring certain transactions.

https://twitter.com/koeppelmann/status/1582035980206239752?s=20

As a result, Ethereum’s future as a credibly decentralized, censorship resistant base layer is, no pun intended, at stake.

https://twitter.com/specialmech/status/1691178038640492544?s=20

**Additional Resources**

- YouTube, [Ethereum's Proof of Stake consensus explained](https://www.youtube.com/watch?v=5gfNUVmX3Es&list=PLa_a2TnKITJ9YiVWcfJ7TDjTvYL4TXBIQ&index=6)
- Dashboard, [MEV Watch](https://www.mevwatch.info/)
- Blog, [Ethereum Reorgs After The Merge](https://www.paradigm.xyz/2021/07/ethereum-reorgs-after-the-merge)
- Article, [Has Proof of Stake Made Ethereum More Centralized?](https://decrypt.co/111485/has-proof-of-stake-made-ethereum-more-centralized)
- Blog, [Base Layer Neutrality: Sanctions and Censorship Implications for Blockchain Infrastructure](https://www.paradigm.xyz/2022/09/base-layer-neutrality#user-content-fn-1)
- Paper, [Ethereum 2.0 Economic Review](https://drive.google.com/file/d/1pwt-EdnjhDLc_Mi2ydHus0_Cm14rs1Aq/view?usp=sharing)
- Paper, [Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559](https://arxiv.org/pdf/2012.00854.pdf)
- Paper, [Weighted Voting on the Blockchain: Improving Consensus in Proof of Stake Protocols](https://arxiv.org/pdf/1903.04213.pdf)
- Thread, [“Is PoS more decentralised and censorship resistant than ETH PoW”](https://twitter.com/_Checkmatey_/status/1560399107189006336?s=20&t=v2T1RQCDQdcOxn-2D5iMKw)

# Credit Scoring, 2022

On-chain credit scoring offers a potential means to unlock use cases for undercollateralized lending, or “buy-now-pay-later” (BNPL) solutions, by serving a similar role to credit scores used in traditional finance for assessing whether a consumer is likely to repay a mortgage, car loan, credit card, or other debt.

This is useful at an institutional scale for undercollateralized lending protocols like Maple Finance to assess a borrower’s health, where Sybil resistance is typically ensured by institutional borrowers being whitelisted and vetted before getting access to the market.

But it seems less likely that these solutions will make a large difference in retail undercollateralized use cases which lack Sybil resistance. It’s relatively cheap and simple for a user to create multiple addresses, invest some time making them appear to be low risk, and then simply taking out credit and defaulting on it.

The quest for the ‘decentralized Klarna’ thus seems misled. Unless lending uses KYC or other centralized means to ensure Sybil resistance and introduce other means of potential debt recovering, defaults can’t be prevented without requiring collateral posted in a smart contract.

But if buyers already have the collateral to post why not just use it to pay now? The BNPL use case quickly collapses to a subset of those covered by overcollateralized lending markets.

**Additional Resources**

- Thread, [“Credit Scores for DeFi”](https://twitter.com/juliangay/status/1547662040788914176?s=20)
- Blog, [Secured and Unsecured Lending](https://medium.com/credora/secured-and-unsecured-lending-3e1e10d03499)

# Decentralized Options, 2022

Call and put options allow investors to express asymmetric bets, and earn a sustainable source of yield (selling covered options is sustainable, though not by any means risk-free).

Options and other complex derivatives have additional complexities that do not exist for outright positions. Creating a synthetic long position is simple enough to accomplish with an AMM to provide liquidity for the other side of the trade and a price oracle.

But when a price oracle for the option itself does not exist, which is often the case since options have varying strike prices and dates of expiration, pricing an option becomes subjective. For a protocol to provide options requires some pricing assumptions beyond the scope of this guide (such as volatility skew and creating a volatility surface).

But advancements in decentralized options are being made, from [Atomic Finance](https://atomic.finance/) using DLCs for trustless Bitcoin options, to underwriting pools like [Hegic](https://www.hegic.co/), to protocols working on turning liquidity provider positions in Uniswap AMMs into options.

The later protocols, which are still in development, leverage the fact that providing liquidity is *akin* to selling an option, thus by trading and manipulating LP positions, in particular one-sided liquidity positions using Uniswap v3, option payoff structures for calls, puts, and complex strategies can be approximated.

![“**Left**: Deploying liquidity above the current spot price creates a range order which converts ETH to DAI as the price moves between the Lower and Upper ticks. **Right**: Deploying liquidity to a narrow, single-tick range creates a “covered call-like” payoff where the ETH is sold immediately as the spot price crosses the strike.”
Source: [Uniswap V3 LP Tokens as Perpetual Put and Call Options](https://lambert-guillaume.medium.com/uniswap-v3-lp-tokens-as-perpetual-put-and-call-options-5b66219db827)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fb475baa-a961-4c7d-a3dc-270c9ac65ac7/Untitled.png)

“**Left**: Deploying liquidity above the current spot price creates a range order which converts ETH to DAI as the price moves between the Lower and Upper ticks. **Right**: Deploying liquidity to a narrow, single-tick range creates a “covered call-like” payoff where the ETH is sold immediately as the spot price crosses the strike.”
Source: [Uniswap V3 LP Tokens as Perpetual Put and Call Options](https://lambert-guillaume.medium.com/uniswap-v3-lp-tokens-as-perpetual-put-and-call-options-5b66219db827)

A liquid DeFi options market would enable new sustainable sources of yield and hedging for treasuries and DeFi apps.

**Additional Resources**

- Blog, [Uniswap V3 LP Tokens as Perpetual Put and Call Options](https://lambert-guillaume.medium.com/uniswap-v3-lp-tokens-as-perpetual-put-and-call-options-5b66219db827)
- Blog, [Perpetual Options for DeFi](https://medium.com/numoen/perpetual-options-for-defi-821351c0a24f)
- Blog, [Calculating Implied Volatility from Uniswap V2 & V3](https://medium.com/gammaswap-labs/calculating-implied-volatility-from-uniswap-v2-v3-e466e49d60e0)
- Spaces, [The future of AMMs](https://twitter.com/MaxResnick1/status/1597458507892396033?s=20)
- Thread, [“Shorting Impermanent Loss”](https://twitter.com/Slappjakke/status/1620436830494625793?s=20)

# Bitcoin Ordinals, Jan 2023

Just as the crypto world seemed to have written Bitcoin off as digital gold, building on Bitcoin saw a renaissance in 2023 with the introduction of Ordinals, enabled by the Taproot upgrade rolled out the year before.

Ordinals, created by Bitcoin core developer [Casey Rodarmor](https://twitter.com/rodarmor), enable “NFTs” on Bitcoin, but just as with NFTs on Ethereum, Ordinals on Bitcoin are capable of extending Bitcoin to many more use cases than profile pictures and images.

https://twitter.com/ChainLeftist/status/1624085853076172810?s=20

Ordinals have also been used to enable **fungible tokens** to be issued on Bitcoin as well, via the BRC-20 protocol created by [anonymous developer “domo”](https://twitter.com/domodata). Though these early fungible tokens rely on additional security assumptions beyond vanilla Bitcoin transactions, work to improve and further decentralize these early experiments is ongoing.

Funds like [Bitcoin Startup Lab](https://btcstartuplab.com/) and [BTC Frontier Fund](https://twitter.com/BTCFrontierFund) are enabling the next wave of developers to build solutions on Bitcoin with tools such as Ordinals, L2s, and DLCs.

**Additional Resources:**

- Blog, [Ordinal Theory](https://rodarmor.com/blog/ordinal-theory/)
- Blog, [Inscribing Mainnet](https://rodarmor.com/blog/inscribing-mainnet/)
- Thread, ["Cursed Inscriptions”](https://twitter.com/LeonidasNFT/status/1665437076450336768?s=20)

# Proof of Humanity, Jul 2023

Sybil resistance has come up multiple times in this guide and Proof of Humanity is catch of term for different approaches to allow for users to prove they represent a unique individual, instead of a bot or a collection of wallets all controlled by the same person.

In essence, centralized KYC measures are a simplistic form of Proof of Humanity, though the holy grail obviously remains doing so while still retaining privacy.

https://twitter.com/blockworksres/status/1692210426661228978?s=20

In July 2023, Worldcoin became the most widely known, and most controversial, widespread attempt at a proof of Humanity protocol, but it is far from the only project working on solving this problem. Popular projects include:

- [Worldcoin](https://twitter.com/worldcoin)
- [Proof of Humanity](https://twitter.com/proofofhumanity)
- [BrightID](https://twitter.com/BrightIDProject)
- [Governor_DAO](https://twitter.com/Governor_DAO)

Until is is solved, Sybil attacks will remain a legitimate security risk to many blockchain products, and builders always need to take them into consideration when designing their product and token.

**Additional Resources**

- Article, [DeFi Sybil attack created $7.5B fake TVL on Solana from ‘anon’ developers](https://cryptoslate.com/defi-sybil-attack-created-7-5b-fake-tvl-on-solana-from-anon-developers/)
- Blog, [What do I think about biometric proof of personhood?](https://vitalik.ca/general/2023/07/24/biometric.html)
- Twitter Spaces, [GDAO 2yr Anniversary: State of the Union](https://twitter.com/Governor_DAO/status/1579237742357016578?s=20)

# 2.0 General Principles & Mistakes to Avoid

<aside>
⚠️ If you’ve skipped ahead to Part Two of this guide. You may want to consider quickly checking out the [**Token Checklist** in Chapter 1.4](https://www.notion.so/1-4-Does-Every-Project-Need-a-Token-79f30dc5e5d34fcca18b7fbcfff3792f?pvs=21) to help you evaluate whether launching a token may be right for you, and whether you may be ready or not to do so.

</aside>

>💡 Part Two has a companion YouTube playlist produced in partnership with the Stacks Foundation that covers every step required to complete the first draft of your tokenomics. https://youtu.be/F0H7K0F1L2o


# The Overall Process

At a high level, *launching* a token involves five steps. Note these deal only with the token itself. Designing and building the product itself is an entirely different conversation.

These five steps for the token can each be broken down into a multitude of substeps and tasks - this guide is primarily concerned with the first of these steps, **designing** your token (including internal tests and optimization of your design).

The remaining steps, including things like smart contract audits, are just as important but are outside the scope of this guide.

## 5 Step Process to Launch a Token

1. **Tokenomics Design**
2. Economic Security Testing (”Tokenomics Audit”)
3. Smart Contract Development
4. Smart Contract Audit
5. Token Launch Event

As mentioned, this guide covers the first steps above **Tokenomics Design**, which breaks down into its own seven step process.

## The *Tokenomics Design* Process

1. Objectives & Requirements
2. Value Accrual
3. Lifecycle Patterns
4. Incentive Mechanisms
5. Supply Policy
6. Modeling & Optimization
7. Legal Opinion & Structure

Part Two of this guide covers each of these seven steps in its own chapter, including frameworks, templates, and/or models for you to work from as you go.

Before delving into the process itself though, we’ll first cover some valuable best practices to keep in mind throughout the process, as well as top mistakes to avoid as you design your tokenomics.

# General Principles & Best Practices

## Use Comps

“Comps” is not a reference to the COMP token - it’s short for **comparables.**

Looking at products similar to the one you are building (comps), is key to making informed strategy decisions.

Suppose you wanted to understand how to build an electric car company, you would look at companies like Tesla and Rivian to understand what *comparable* companies are doing - both what they are doing well, and what mistakes they’ve made along the way.

Or imagine you wanted to understand what a company similar to Tesla and Rivian would be worth. A reasonable place to start would be to look at how much revenue those companies are generating, and how much their market caps are compared to revenue, yielding a “valuation multiple”. Take an expected revenue, multiplied by that valuation multiple, and you have a “fair market estimation” market cap.

The DeFi equivalent would be to look at a valuation metric like [MarketCap/TVL](https://defillama.com/) in order to roughly understand the relative “overvaluation” or “undervaluation” of protocols. It’s important to note that there is no single “right” metric, and even in DeFi, simply using MarketCap/TVL is not very useful when comparing different types of platforms that earn revenues in fundamentally different ways. For instance, AMMs tend to make fees from trading volume, whereas a yield aggregator makes fees from TVL yield.

Using comps is not just for valuing products and companies - it allows you to stand on the shoulders of giants, and to learn from mistakes that others have already made. Comps are always helpful for making tokenomics and protocol design decisions.

## Innovate in the Right Areas

Like any young technology, blockchain has only just scratched the surface of its full potential use cases. You want to be innovative and stand out when it comes to creating new:

- Use cases and utility
- Sustainable incentive mechanisms
- Governance models
- Technology and architecture
- Value **creation** and value **capture** mechanisms

Yet it’s just as important to be careful about **not** standing out in the wrong areas.

Doing so can increase the risk of drawing the ire of regulators, scaring off potential users, harming your token holders, and/or making it harder to raise funding.

You may want to err on the side of caution, and avoid standing out (follow industry best practices by looking at comps) when it comes to:

- Legal and regulatory structures
- Value **accrual** to token holders
- Profit sharing
- Token allocation splits
- Token vesting periods

For example, if the market standard is to allocate roughly 15% of tokens to the core team which vests over several years, but you allocate 50% of your tokens to the core team that vests in 3 months, you can expect that all else equal, people will be a lot more skeptical of your product’s long-term outlook.

This can translate into less adoption, less loyal users, and less capital to build with.

If you were deciding between using two otherwise similar products, but one had a very abnormal token allocation, which would you be more likely to use?

We’ll cover the market best practices for token supply (allocation, emissions, vesting, etc) in detail in [Chapter 2.5](https://www.notion.so/2-5-Supply-Policy-ff3f8ab217b143278c3e8fd0c03ac137?pvs=21).

## Minimize Volatility

It’s tempting to optimize for increasing your token price, especially when the token’s price is the single most transparent metric by which your entire project will be judged:

> **“Your value is only as good as your token, token go up? You built an amazing protocol, its the future of finance, blah blah. Token goes down? You are a scammer, fake project, bad coder, blah blah.”
- Andre Cronje, [Building in defi sucks (part 2)](https://andrecronje.medium.com/building-in-defi-sucks-part-2-75df9ee7871b#:~:text=Your%20value%20is%20only%20as%20good%20as%20your%20token%2C%20token%20go%20up%3F%20You%20built%20an%20amazing%20protocol%2C%20its%20the%20future%20of%20finance%2C%20blah%20blah.%20Token%20goes%20down%3F%20You%20are%20a%20scammer%2C%20fake%20project%2C%20bad%20coder%2C%20blah%20blah)**
> 

However, optimizing for increasing your token price sacrifices the actual health and sustainable growth of the protocol itself - ironically resulting in a lower token price in the long run.

Instead of optimizing for increasing token price, builders should optimize for being resilient to market crashes, slowdowns in product usage, and malicious attacks - they should minimize volatility.

When your protocol has resilient tokenomics, your product and token can not only survive adverse conditions but also retain their fundamental values through these conditions while competitors entirely explode.

For example, UST’s tokenomics optimized for increasing the market cap of UST above everything else, paying a heavily advertised 20% APY no matter what. As a result, its tokenomics had no mechanism to deal with the LUNA dropping in value below a critical threshold.

UST blindly relied on each LUNA token to always exceed a certain value, and as the amount of issued UST grew and grew, this required value increased - meaning the protocol became less and less resilient, and more and more volatile, the larger it grew.

https://web.archive.org/web/20220322205103/https://twitter.com/0xHamz/status/1506372692005593090

Olympus DAO (OHM) is another example of optimizing for market cap growth above everything else. In its original form (they have since abandoned the unsustainable ponzinomic yield model), the tokenomics required a constant stream of more and more capital entering the system.

When capital inevitably begins to leave, the expected outcome as a death spiral, [according to the very same game theory principles](https://www.jasss.org/20/4/12.html#7.10) OHM mentions as a strength in its white paper! And a death spiral is exactly what played out, with market cap collapsing more than 95%.

Ironically, optimizing for higher prices often directly leads to the opposite outcome. Optimizing for healthy fundamentals, sustainable growth, sound incentives, and minimizing volatility is much more likely to lead to success.

# The 9 Biggest Tokenomics Mistakes to Avoid

## 1. Not Knowing Why You Need a Token

The most common mistake is not knowing why or how a token will actually benefit your product and your users.

These builders are often interested in launching a token purely to raise money, and then have to try work backward to create a need for the token. Just as you wouldn’t start a company “in order to be an entrepreneur”, launching a token “to have a token” is not the right approach.

Both crypto and traditional business models alike start with solving a problem and creating something useful that people want or need.

## 2. Not Planning Ahead

The second mistake is almost the inverse of the first - whereas in the first mistake, builders have a token but no product, the second mistake is to have a product that isn’t designed for a token, and then launch a token after the fact.

Case in point - Uniswap is still struggling to activate the “fee switch”, and until they do, the UNI token is purely a governance token with dubious value or purpose except as speculation that UNI will capture fees in the future. Part of this may have been due to the fact that the launch of UNI was largely rushed in order to defend against the SushiSwap vampire attack.

Uniswap could have still launched their product first and their token later - doing so remains a common tactic for many crypto products. However, when doing so, it’s important to plan ahead of time for how the token fits into and benefits the product, even if have no plans to actually launch the token yet.

We’ll discuss Uniswap’s situation and token value accrual more in [Chapter 2.2](https://www.notion.so/2-2-Value-Accrual-8d82061356a8422b9f39e8271c4e3b8a?pvs=21).

## 3. Not Knowing What Type of Token You’re Issuing

Another common mistake is not knowing what type of token you’re launching.

This increases your legal risk since you don’t know how your token will likely fit into existing regulatory frameworks that specify specific token types.

Just as bad, if you don’t explicitly know what type of token you’re launching, it’s easy to fool yourself into excusing a poorly designed token that has no utility by assuming that your token will be used as a medium of exchange (currency) or a store of value (ie Bitcoin, gold).

> **“99 percent of tokens won’t ever satisfy the store of value pre-requisites.”
-** Brendan Bernstein, [Making Sense of Crypto Asset Valuation Insanity](https://www.coindesk.com/markets/2018/03/11/making-sense-of-crypto-asset-valuation-insanity/#:~:text=Most%20assets%20won%27t%20become%20a%20reserve%20store%20of%20value)
> 

In reality, for the vast, vast majority of builders your token will never become a store of value or general medium of exchange, and assuming it will, or using a design that requires it to, is delusional wishful thinking.

Ironically, even if your token was used as a medium of exchange, its velocity of money would increase, thus making the token itself less valuable!

Along the same lines, if you’re introducing a utility token, make sure it has actual utility. Taking a useless token and adding staking to earn more of the same token does not give it utility.

## 4. Relying on Always Increasing Prices

Builders that optimize for “number go up technology”  will find that all the growth that seemed to come while the price was rising will just as quickly evaporate once the price declines. Builders cannot rely on prices always going up - tokenomics that do are schemes, not products.

https://twitter.com/mrjasonchoi/status/1550463271475392512?s=20&t=cbtnwbTkfytpFCz4y_gFJA

Volatility and random events are part of life. The world is far more complex than a simplistic 3x3 game theory payoffs matrix.

People sell tokens for all sorts of rational and irrational reasons, and each unit of value does not have identical worth to everyone - risks and rewards are subjective. Users can be incentivized, but can never be forced to do something or prevented from trying it even, if they “shouldn’t” or if it's irrational to do so.

> **In general, the crypto space needs to move away from the attitude that it's okay to achieve safety by relying on endless growth. It's certainly not acceptable to maintain that attitude by saying that "the fiat world works in the same way", because the fiat world is not attempting to offer anyone returns that go up much faster than the regular economy, outside of isolated cases that certainly should be criticized with the same ferocity.
- Vitalik Buterin, [Two Thought Experiments to Evaluate Automated Stablecoins](https://vitalik.ca/general/2022/05/25/stable.html)**
> 

If your tokenomics cannot handle anyone ever selling, user activity sometimes shrinking instead of constantly growing, or your token price sometimes falling, your product will not survive.

## 5. Underestimating Collateral Risks

Using collateral is sometimes unavoidable. For example, enabling users to mint DAI requires them to post collateral, otherwise people would spam minting DAI, with no repercussion for doing so.

DAI would soon have no value and have no chance of functioning as a stablecoin.

Yet collateral **always** means risk. Looking at surface level assumptions of price, market cap, and market liquidity and depth can be extremely misleading when assessing these risks.

Market cap structurally overestimates the value of collateral when the value of that collateral is most important - when people start selling it.

Just because you can sell 1 ETH for $2,000 does not mean you can instantly sell 1 million ETH all for $2,000 each. Obviously, if you tried to do so, the price would decline, and your average price would be lower than $2,000.

But when you rely on market cap for collateral value, you’re making an even less realistic assumption - you’re assuming you could sell every single ETH in existence for $2,000 each!

Another hidden risk is that market downturns are also the time when markets generally become less liquid, slippage increases, spreads widen, order books thin out, and asset correlation increases. All this means that if you look at **current** liquidity as an expectation of liquidity for when you need to liquidate collateral, you are almost certainly overestimating what liquidity will actually look like when you’re trying to sell.

<aside>
💡 Builders too often overestimate the value, liquidity, and diversification of collateral assets, and underestimate their correlation to the overall market because they make assumptions based on normal market conditions, not based on conditions during market downturns.

</aside>

## 6. Assuming Product Usage Means Token Demand

It’s common to assume the more a product is used, the more demand for the token they’ll be - however this is not necessarily the case and is heavily dependent on tokenomics.

Devoid of clear **value capture** and **value accrual** there is no often no fundamental reason more usage translates into **sustainable** higher prices.

> **You might expect cryptoassets to gain value with adoption, but this equation suggests the opposite. At scale, cryptoassets will likely achieve hyper efficiency that reduces the price.
Source: Mike Sall, [Valuing Cryptoassets from the Ground Up](https://medium.com/@sall/valuing-cryptoassets-from-the-ground-up-441ad5a9ff03)**
> 

> **We often hear investors put too much stake on the relationship between adoption and cryptocurrency price. In truth, you have to look at economics very closely in order to understand whether such a relationship even exists. Developers of decentralized networks often don’t evaluate these dynamics correctly and inadvertently represent to their investors the expectations that are simply not true.
Source: Alex Bulkin, [Cryptoeconomics Is Hard Part 2](https://blog.coinfund.io/cryptoeconomics-is-hard-part-2-4d522cb3d3a4)**
> 

We discussed an example in [Chapter 1.3](https://www.notion.so/1-3-The-Good-The-Bad-and-The-Ugly-3dfc31a65d33497394e3a4965ed90e4b?pvs=21) to demonstrate why, with the fictional UBR token for a Web3 Uber product:

- A rider buys 10 UBR tokens with dollars and pays the driver those 10 UBR. The rider’s purchase of UBR, in isolation, is net positive demand and increases the price of UBR.
- But… if the UBR tokens have no utility to the driver, and they sell the 10 UBR tokens for dollars immediately upon receiving them (for instance, in order to pay for gasoline which is priced in dollars), then all else equal, the demand and price increase for UBR is exactly canceled out.
- Thus… more rides do not create net demand for the UBR token.

Assuming product usage translates to token demand is not realistic - it depends on the tokenomics, especially on the utility, value capture, and value accrual mechanisms.

## 7. Only Focusing on Token Supply

When you hear people discussing tokenomics, they almost always discuss these aspects:

- Allocation
- Emission schedule
- Inflation rate
- Burns
- Total number of tokens
- Tokens in circulation

These are all **supply** aspects, and supply is only one piece of the puzzle:

- Scarcity alone is not enough.
Your childhood artwork is scarce. Yet chances are they’re not selling for much these days, even as NFTs.
- Reducing inflation is not enough.
Less of something that is useless is still useless.
- Removing sell pressure is not enough.
People are catching on that [staking for no reason other than to prevent selling](https://cobie.substack.com/p/apecoin-and-the-death-of-staking) is a cheap gimmick that is [not the same thing as earning interest](https://www.reddit.com/r/CryptoCurrency/comments/pgqz03/please_stop_treating_staking_and_getting_interest/), despite being framed as an APY.

If people never acquire your token, because it’s useless other than staking it, then reducing sell pressure doesn’t matter!

- More deflation is not always a good thing.
Deflationary pressures that are not properly balanced can paralyze economic activity since people begin to hoard the token instead of using it for its intended purpose. The benefits of deflation are often overestimated, a topic we’ll revisit in [Chapter 2.5](https://www.notion.so/2-5-Supply-Policy-ff3f8ab217b143278c3e8fd0c03ac137?pvs=21) on Supply Policy

> **“If you’re thinking about rewards or token allocations, instead of agents or how to preserve alignment among the participants in your system, you’re probably not thinking about a protocol, you’re thinking about that token, and that token is not the protocol. The token shouldn’t be the goal, it should be just a tool.”**
**- Eddy Lazzarin,** [Token Design: Mental Models, Capabilities, and Emerging Design Spaces](https://www.youtube.com/watch?v=GOkxDvq_8zQ)
> 

As a builder, you need to be thinking about token **demand, use cases, incentive mechanisms, and value drivers just as much, if not even more, than supply.

## 8. Not Modeling & Stress Testing

Incentives are tough to get right, and even if the overall system is sound in design, it is a virtual impossibility that you happen to pick the optimal parameters that plug into that design out of thin air. This is true even when guided by frameworks like game theory.

Yet many builders simply don’t where to start when it comes to optimizing parameters and stress testing their design. It’s intimidating, and difficult to know **what** to model, let alone **how** to model it to test their assumptions.

https://twitter.com/TendermintTimmy/status/1674770677599961089?s=20

As a result, teams end up with arbitrary emissions schedules, undetected death spirals, hidden assumptions that suddenly pop up in bear markets, overlooked critical thresholds that need to be guarded, hard-coded parameters that need to be dynamic, unrealistic expectations of risks, and a poor understanding of what to tweak to optimize the design.

Every serious builder knows they need to audit their smart contracts. While it’s important to have code that does what it’s supposed to do… ensuring the code is supposed to do the right thing in the first place is even more important.

<aside>
⚠️ Beware of builders who dismiss modeling as useless - this is a telltale mark of either an amateur launching an untested protocol, or a scammer who doesn’t want their community to understand what the modeling shows.

</aside>

Methods that are everyday practice in TradFi and system engineering, such as Monte Carlo random walks, boundary testing, and scenario analysis, would have helped identify the degree and severity of the unseen risks Luna, Celsius, Mango, and others were taking.

If they had taken risk management seriously things would have turned out very differently.

## 9. Ignoring Regulatory Risks

People go to jail for ignoring regulatory risk - sometimes justifiably so, sometimes not. Take it seriously.

> **“Binance does BNB buyback and burns, so we can definitively do buybacks too, no problem.”
- Ignorant Builders**
> 

You are not Binance. Get a legal opinion!

Just because someone else uses a certain tokenomics model and hasn’t (yet) been sued or arrested doesn’t mean the same applies to you. Life’s not fair.

With the recent crackdowns on Tornado Cash, including the arrest of a developer guilty of the ‘crime’ of committing code to an open source project, it’s more important than ever to take this seriously. As a brief reminder - this guide is not legal advice.

# Chapter Summary

- Learn from comparable products (especially their mistakes)
- Innovate in the right ways, and don’t stand out in areas that will spook token holders, users, or regulators
- Focus on more than just token prices and token supply
- Model, test, iterate, keep asking “why”, and don’t ignore regulations!
- Luckily, you can avoid all the top mistakes by following this guide’s tokenomics design process…

# Additional Resources

- Blog, [Token Design for Serious People](https://jumpcrypto.com/token-design-for-serious-people/)
- YouTube, [Token Design: Mental Models, Capabilities, and Emerging Design Spaces](https://www.youtube.com/watch?v=GOkxDvq_8zQ)
- YouTube, [ETHDenver: Demand-Side Tokenomics](https://www.youtube.com/watch?v=I_4QbbZJjsA)
- Twitter Spaces, [Circular & Sustainable Economies](https://twitter.com/joincommonwlth/status/1675406452343595009?s=20)
- Twitter Spaces, [Tokenomics Design Strategy](https://twitter.com/robindavidji/status/1603486612457148416?s=20)
- YouTube, [EthCC[6] Paris - Token Engineering Track](https://youtube.com/playlist?list=PL-GxJch-YeZf8bRpNGddYu9bpqCo6p2sD)

# Video Tutorial

# 2.1 Objectives & Requirements

# Introduction

The first step in designing win-win-win tokenomics is to identify your high-level objectives and requirements.

Every design process is an iterative process. You may complete a step before realizing you’ve got to go back and tweak a few things.

That’s actually a good thing. That’s what making improvements looks like.

To start, you’ll need to complete the [“Step 1: Objectives & Requirements” in the **Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

As you complete the worksheet, keep in mind that tokenomics starts with solving a problem ([Chapter 1.2](https://www.notion.so/1-2-What-is-Tokenomics-3a6dacd60eaf41ab95d832f60d7a8bef?pvs=21)). If your product doesn’t solve a key user problem, or no one would use your product unless they can make money from your token, it’s a good sign you may need to take a step back and reevaluate your plans. Exceptions apply, but generally speaking, your token is not your product.

Additionally, recall that good tokenomics are win-win-win ([Chapter 1.3](https://www.notion.so/2-1-Objectives-Requirements-a9139538d7054a1f95f07ea901e356fe?pvs=21)), improving the product and benefiting both holders and contributors. If you don’t hit those three criteria, or if there’s no legitimate use case or utility for your token other than raising funds, that’s another good sign to pause and reflect - especially if you’re planning a token sale to retail investors.

Staking an otherwise useless token to earn more of that useless token is not valuable to holders. Price speculation, fundraising, providing liquidity, and staking are not legitimate token utilities.

Remember that not every project needs a token, and there are pros and cons to launching a token that you should carefully weigh before deciding to do so ([Chapter 1.4](https://www.notion.so/1-4-Does-Every-Project-Need-a-Token-79f30dc5e5d34fcca18b7fbcfff3792f?pvs=21)). The [*Token Checklist*](https://www.notion.so/1-4-Does-Every-Project-Need-a-Token-79f30dc5e5d34fcca18b7fbcfff3792f?pvs=21) at the end of that chapter can help you decide in a more structured way if a token is right for you.

# Primary Tool: Tokenomics Design Canvas (TDC)

<aside>
💡 Complete “Step 1: Objectives & Requirements” of the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)

You can find an example of the canvas and download a [printable version to complete by hand on Canva](https://www.canva.com/design/DAFDTNKsIJs/8Ky9EoJJI7p98qKLIu2XNw/view) (please note to use it as a template you must be logged in to Canva).

</aside>

# Video Tutorial

# 2.2 Value Accrual

# Introduction

It’s now time to think about your token’s value accrual and complete [“Step 2: Value Accrual” in the Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).

This is a crucial step, as how value accrues to your token can be largely affected by even seemingly small differences in your tokenomics.

Something as simple as switching from charging **sellers** a commission to sell their NFT to charging **buyers** a fee to purchase the NFT can make a large difference:

- Charging **sellers** means that supply is less likely to use that marketplace, and naturally buyers will look to go to marketplaces with the most available supply.
- Charging **buyers** on the other hand means sellers can use the marketplace for free, and thus will be more likely to list their supply there, in turn bringing more buyers, in turn resulting in higher overall fees than charging the same transaction fees to sellers.

https://twitter.com/beeple/status/1581351398259597312?s=20&t=ENl5ytcXgAE__Z4gt9YNRQ

There are three relevant core concepts that are often confused, and it’s important to understand the differences between Value Creation, Value Capture, and Value Accrual, and how each relates to your product and token.

# Value Creation

Imagine it’s late 2018 - you have some ETH and some LINK tokens.

You’d like to keep both, but earn a yield on your tokens at the same time (this pre-dates The Merge and the ability to stake ETH for validator rewards).

In theory, you could earn a yield by market making on the order book of a centralized exchange - but doing so requires constant and sophisticated management of your bid and offer sizes, spread, skew, inventory, etc.

Along comes a new product called Uniswap, an AMM (Automated Market Maker), allowing you to deposit equal values of your ETH and LINK to automatically provide liquidity and earn a portion of trading fees. All without the custodial risk of a centralized exchange, of the prohibitive barriers to active market making.

Uniswap has **created** value for you as a liquidity provider.

Or, as we discussed in Chapter 1.2, imagine you have $1,000 of USDC you want to sell to buy ETH but want to avoid the hassles, delays, and risks of trading on a centralized exchange. Uniswap offers you a way to sell your USDC to buy ETH that avoids these downsides.

Uniswap has **created** value for you as a trader.

The product has **created** value, but the question remains - did Uniswap **capture** any of that value for its own treasury?

# Value Capture

A product can’t *capture* value if it hasn’t **created** any in the first place. For example, if both liquidity providers and traders would prefer a centralized exchange over a DEX, then Uniswap hasn’t created any value for anyone, so it won’t have any users, and thus won’t have any value to capture.

<aside>
💡 It’s impossible to **capture** value without **creating** value first. But it’s all too easy to **create** value and not **capture** any of it.

</aside>

Uniswap is the biggest example of this - though it’s a useful product that creates value for users, all fees by traders are earned by liquidity providers, the Uniswap treasury does not capture any value.

Builders too often make an assumption that value creation has an inherent casual relationship with value capture - it does not.

> **A business creates X Dollars and captures Y% of $X.**
> 
> 
> **X and Y are Independent Variables.
> 
> X and Y have nothing to do with each other. They are not interrelated at all.
> Source: [Why Value Capture is the Most Important Business Idea You Haven’t Read Enough About](https://medium.com/evergreen-business-weekly/why-value-capture-is-the-most-important-business-idea-you-haven-t-read-enough-about-c035c657d091)**
> 

In 2016, the “[Fat Protocol Thesis](https://www.usv.com/writing/2016/08/fat-protocols/)” postulated that value would primarily be captured by underlying blockchains rather than the products and dApps built on them. But we are now in an era where top dApps and DeFi products generate more in revenues (value captured) than popular alternate chains and rollups such as BSC, Arbitrum, Optimism, Solana, Avalanche, and Polygon.

![Products and protocols sorted by 30d revenues (i.e. value captured).
Source: [DefiLlama](https://defillama.com/fees)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/988bd8c5-3212-4e40-86bd-825bacfda46b/Untitled.png)

Products and protocols sorted by 30d revenues (i.e. value captured).
Source: [DefiLlama](https://defillama.com/fees)

Notice Uniswap’s conspicuous absence from the rankings above - when sorted by **fees paid by users** instead of by **revenues**, Uniswap would rank 4th.

Other DeFi products, including competitor AMMs, **capture** more value than Uniswap - in some cases despite having materially lower usage, such as PancakeSwap. This is not some unknown phenomenon - this is directly due to their different models and tokenomics.

![Source: [Bankless, Which DeFi Protocols are Profitable](https://newsletter.banklesshq.com/p/which-defi-protocols-are-profitable)](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4830ab74-d391-4ac6-91ec-ccb9621f5ade_1194x623.png)

Source: [Bankless, Which DeFi Protocols are Profitable](https://newsletter.banklesshq.com/p/which-defi-protocols-are-profitable)

Uniswap is still struggling with the so-called “fee switch” problem - the debate over starting to direct some of the trading fees to the treasury to **capture** value as revenue.

Why has this been such a contentious debate? Largely because liquidity providers have gotten used to keeping 100% of the fees themselves and don’t want to give up a share of their fees to the treasury. Design choices made about Uniswap’s tokenomics have backed it into a corner that will be tough to get out of.

https://twitter.com/mhonkasalo/status/1552994507838349313?s=20&t=RgD9S0j-Pa9u1-Npu-vbwQ

https://twitter.com/BarryFried1/status/1553051635609485313?s=20&t=v2T1RQCDQdcOxn-2D5iMKw

https://twitter.com/mjayceee/status/1673394954834419712?s=20

Even though Uniswap has **created** tremendous value for users, it has yet to **capture** any of that value for itself.

# Value Accrual

Just because a product **captures** value does not mean that value **accrues** to the token. In Uniswap’s case, because the treasury does not capture any value, there is no value to accrue to the UNI token.

But even worse, several large products do not **accrue** value to their tokens despite **capturing** value. dydX is one such example, much to the ire of token holders.

https://twitter.com/jdorman81/status/1617966345282551808?s=20

Other leading tokens do accrue value - CRV, GMX, MKR, BNB, LQTY, and MPL, to name a few.

Binance’s BNB token is perhaps the most well-known example of a token with value accrual - and in fact, it uses multiple mechanisms including buying back tokens with protocol revenue, and allowing users to pay discounted trading fees in BNB which imbues the token with an inherent “floor” value.

You might be asking yourself then, if tokens like UNI and dYdX don’t accrue value, why do they have any value at all? Why do people buy them or care about earning them?

The answer is largely speculation and narrative - speculation that the tokens will, at some point, begin to accrue value.

> **There are two ways you can make money. One is through driving the narrative, even when there is a lack of protocol fees or usage. Meme tokens are a version of this, taken to the extreme. The other is building a dApp that generates fees and commands a reasonable multiple… Both, require an incredible amount of work.**
> 
> 
> **The best founders we have seen can drive both narratives and platform usage. Having only one is generally a recipe for disaster.**
> 
> **- [Value Accrual: Should Protocols Make Money?](https://www.decentralised.co/p/value-accrual)**
> 

But speculation and narrative can only take a project so far for so long - it isn’t sustainable. Builders can’t just assume that at some point more product usage will begin to automatically translate into the token accruing value. How, or if it does, is up to your tokenomics design choices.

To be clear, directly distributing product revenues is not the only form of value accrual - and it’s not even possible in many cases.

For example, L1s do not directly “earn revenues” or “capture fees” in the same way a dApp does. Value accrual in these cases often involves dynamically rebalancing supply and demand such that increased usage explicitly is converted into value accrual - which is very different from builders just assuming this will happen on its own.

# Value Accrual Blueprints

This section compiles some of the most popular value accrual mechanisms that products use - it is not necessarily exhaustive, new mechanisms can be created, though builders should be wary of new mechanisms that seem to good to be true. Accrued value can not exceed captured value, just as captured value can not exceed created value.

Any mechanism that seems to accrue more value than it creates in total (i.e. ponzinomic flows that **transfer** value instead of creating it) is a red flag.

Builders should also remember that just because an existing product uses a specific mechanism does not necessarily mean it is legal or prudent to do so in your use case or jurisdiction.

Token value accrual can be an especially critical topic from a regulatory point of view. Always get a legal opinion from a registered professional before launching a token.

It’s generally a good idea to experiment with designs using different approaches to arrive at the value accrual mechanism that makes the most sense for your situation. This often requires at least some quick spreadsheet calculations and high-level modeling to see, given some basic assumptions, how each might impact your product.

You may need to return to this step after doing more advanced simulations in later steps.

That’s OK. What’s important is that you are intentional about a value accrual mechanism up front, because as you progress with your token’s design, subsequent steps such as your token’s incentives, sinks, and faucets will be at least partially dependent on the value accrual mechanism.

## Fee Distributions

With fee distributions, revenues are directly distributed on a pro-rata basis to token holders or to staked tokens in order to reward those with skin-in-the-game.

<aside>
💡 CRV, GXM, LQTY, and MPL are each examples of tokens that do this in some form, and when done properly, fee distributions can be done in a decentralized, non-custodial, and gas-efficient manner.

</aside>

For example,  CRV distributes a portion of fees to veCRV holders (CRV stakers) once a week, every Sunday at 12:00 UTC, and uses batching in order to minimize gas fees.

While fee distributions do directly impact the token price, they create a token that pays a real yield - i.e. not just more of the product’s native token. This yield has knock-on effects on token demand, and thus its price. For instance, if investments with similar risks pay a 10% yield, and a token is currently distributing an 12% yield from fee distributions of recurring revenue (i.e. an actual, sustainable source of yield), that implies that there may be more demand for the token in the future as people would prefer to earn a 12% yield vs a 10% yield for the same level of risk.

While the yield accrues value to the token, and can impact price, fee distributions do not directly show up in the token price or as a history of appreciation in the token price in the same way token buybacks would for example. That’s because fee distributions are not directly a source of token demand or buying pressure, and do not reduce token supply.

For instance, imagine Token A and Token B are two otherwise identical tokens with identical revenues. Token A uses revenues for fee distributions, while Token B uses revenues for buybacks.

All else equal we would expect Token B to have a higher price per token, and more consistent appreciation in the token price, even if total returns to holders of Token A and Token B are identical. That’s because 100% of Token B’s returns are from price appreciation, whereas Token’s A returns are “split” across yield earned and price appreciation.

In an industry where a token’s price and price history are the most transparent and first metrics used to judge a project, tokens that pay fee distributions instead of methods like buybacks may be at a disadvantage - irrational as it may be.

Fee distributions may also be less desirable to holders for tax reasons, since fee distributions may be considered taxable as ordinary income at the time they are paid out. Conversely, appreciation in token price would only be taxable when tokens are sold, and potentially at lower “long terms capital gains” tax rates. This is not accounting or tax advice though, and you should speak to a registered professional for relevant advice.

## Buyback and Burn

Revenues earned by the product are used to repurchase tokens from the open market, and then some or all of these tokens are burned.

Modern AMMs allow for this process to be fully decentralized and non-custodial. To do so, the product’s smart contract collects fees and has a publicly callable contract which will place a trade to buyback the native token from an existing AMM pool and burn them.

Since all token holders have an incentive to trigger the contract to buyback from the pool, and the contract can be called by any token holder, it's inevitable that the contract is called from time to time to buyback tokens and burn them.

In practice, certain limitations may be desirable to avoid abuse, such as a maximum cap on the number of tokens repurchased per day, or throttling how often the public contract can be called - but these too are part of the contract itself, removing the need for any centralized entity to take custody or oversee the process.

The benefit here is two-fold:

- The greater the revenues, the more buying pressure there is in the short term, accruing immediate value to the token
- The greater the revenues, the more tokens are burned, thus the more supply is reduced, making tokens increasingly sparse

The downsides are that buyback and burns reward dead wallets, and if done indiscriminately, can be buying back tokens at peak speculation prices. A reasonable modification may be to buyback dips in the token price, essentially helping to establish a price floor - which makes a bigger impact on prices when it matters most (in downturns) and be a more efficient spend of the funds, especially if buybacks are telegraphed and can be front run, which would mean buying back tokens at short-term highs.

Either way, critics of buyback and burns are correct in that it essentially destroys funds that could be reinvested into growth. Once a product is mature, such that it generates large, stable revenues but not growing quickly, buybacks can be the optimal approach.

But while revenue is growing at a faster rate than the rate of return earned by buybacks, it is value destructive to buyback and burn instead of reinvest in growth, which brings us to…

## Buyback and Build

As the name implies, this is an alternative to Buyback and Burn, where revenues are still used to buy tokens from the open market, but instead of burning them, these native tokens are returned to the treasury to be used in future incentive programs such as development grants and staking rewards.

<aside>
💡 The end result is similar to Buyback and Burn when the tokens are paid out as staking rewards - the token price still increases from buying demand, and rewards provide a yield.

</aside>

In the “worst case” scenario, where 100% of the tokens paid as yield are sold by recipients, Buyback and Build essentially becomes a revenue distribution to token holders:

- Fictional product AlphaFi uses 1,000 USDC of revenue to buyback ABC tokens from the USDC:ABC pool (selling USDC to buy ABC), and distributes the ABC as staking rewards to token holders
- 100% of ABC tokens paid out as staking rewards are dumped by holders back into the USDC:ABC pool (selling ABC to buy USDC)
- The end result is the price of ABC token is USDC returns to approximately the same price before the buyback, and ABC stakers end up with approximately 1,000 USDC tokens

The Buyback and Build model was [first popularized by Yearn Finance in YIP-56](https://gov.yearn.finance/t/yip-56-buyback-and-build/8929) which itself was inspired by Joel Monegro’s blog post “[Stop Burning Tokens – Buyback And Make Instead](https://www.placeholder.vc/blog/2020/9/17/stop-burning-tokens-buyback-and-make-instead)”.

## Buyback and LP

Another buyback option is to buyback the native token, pair them with a non-native asset that revenue is earned in, such as the chain’s gas asset or a stablecoin, and deposit in a liquidity pool.

[Marker DAO recently moved to this approach](https://forum.makerdao.com/t/introduction-of-smart-burn-engine-and-initial-parameters/21201) instead of buybacks and burns, though they use the term “smart burn” which is somewhat misleading as tokens are not actually burned, but deposited as liquidity.

Instead of burning or redistributing the repurchased tokens, the treasury retains ownership of this liquidity, making this approach a form of “protocol owned liquidity”, a term that can carry a negative connotation because OHM popularized the phrase along with its “(3,3)” ponzinomics. It’s worth noting though that ponzinomis and protocol owned liquidity do not need to go hand in hand.

If the token is purchased from a sustainable, recurring revenue source (e.x. Maker repurchases MKR from DAI revenue), then there is nothing unhealthy about buyback and LP style treasury owned liquidity. The problem arises when purchases are funded by unsustainable value **transfer** mechanisms that enter a death spiral without an ever increasing amount of incoming capital.

The immediate effects of buyback and LP is very similar to buyback and burn, as the buyback adds net demand pressure, and tokens are removed from “active” supply (i.e. non-treasury owned supply) instead of being distributed to wallets that may sell them (like in buyback and build).

The tokens don’t cease to exist though, they can still be purchased from the liquidity pool, so the circulating supply does not change. This means that in the longer term, buyback and LP is not as deflationary as buyback and burn. That said, by increasing liquidity, the price volatility of the token is dampened, as future buys or sells with have less market impact.

<aside>
💡 All else equal, buyback and burn optimizes more for price increase at the expense of more volatile prices, whereas buyback and LP optimizes for reducing volatility, at the potential expense of less token appreciation.

</aside>

An additional modification to this approach would be to directly use product revenues to provide single-sided liquidity below the current price. This has the benefit of further dampening sell pressure, while not dampening buy pressure, and avoiding the inefficiency of the treasury buying back tokens from their own liquidity. But the relative downside of single-side liquidity is that no net buy pressure is exerted on the token.

A 50% blend of buyback and burn and 50% buyback to single-side LP seems like a dominant strategy vs 100% of revenues routed to buyback to double-side LP. But ultimately, each product can blend these mechanisms though, routing portions of revenue to each, in order to optimize for their specific objectives.

## Work Tokens

Kyle Samani’s explanation below sums up Work Tokens’ mechanism very well. Value accrues to the token as product usage increases due to the particular mechanism - not just because of a general assumption usage always translates into token demand.

> **In the work token model, a service provider stakes (AKA bonding) the native token of the network to earn the right to perform work for the network. For services which are commodities such as… Filecoin (distributed file storage), [and] Livepeer (distributed video encoding)… the probability that a given service provider is awarded the next job is proportional to the number of tokens staked as a fraction of total tokens staked by all service providers.

As demand for the service grows, more revenue will flow to service providers. Given a fixed supply of tokens, service providers will rationally pay more per token for the right to earn part of a growing cash flow stream.
Source: Klye Samani, [New Models for Utility Tokens](https://multicoin.capital/2018/02/13/new-models-utility-tokens/)**
> 

The advantage here is that increased usage of the product pretty directly fuels demand for the token, without the product itself even needing to charge a fee that would otherwise reduce profits available to service providers.

The disadvantage is that requiring service providers to first acquire and stake large amounts of your token becomes an upfront investment that creates friction to adoption and may be a centralizing force by introducing a barrier to entry.

## Burn and Mint

This approach uses a utility token that is burned in order to use or pay for the service - a token that is burned on use. Such a token is inherently deflationary, with the rate of deflation directly tied to the amount of usage of the product.

This might sound ideal at first, but builders often overestimate the benefits of deflation, something we’ll discuss more in depth in [Chapter 2.5](https://www.notion.so/2-5-Supply-Policy-ff3f8ab217b143278c3e8fd0c03ac137?pvs=21) when we address Supply Policy.

To balance this, such that users can acquire new tokens to spend, and to modulate the rate of deflation, new tokens are minted as well at a rate meant to stabilize usage of the product.

The advantage here is that the supply of the token decreases over time, but the disadvantage is that this alone does not create demand for the token, and it creates the danger of destabilizing product growth.

If the token becomes too deflationary, such that users would rather hold their token for speculative reasons rather than use the token, paradoxically user activity dries up. Yes, this would mean the rate of deflation would then decrease, but it creates volatile swings in product usage.

This is part of the beauty of EIP-1559 in Ethereum. Most people only focus on the fact that EIP-1559 can make ETH deflationary, but the real benefit is that it **balances** deflation with inflation so as not to stifle product usage.

Modern ETH is burn and mint. Gas fees are burned, while rewards paid to validators are minted. Both deflation and inflation are happening at once - and which force wins is a function of product usage.

<aside>
💡 The significance is that ETH benefits from some of the value accrual benefits of deflation - but as deflationary pressure gets too out of hand, such that people start purely holding ETH instead of using it, the rate of deflation decreases directly in-line with this reduced usage, even flipping to net inflation, removing the incentive to not use the network. Thus, burn and mint stabilizes value accrual deflation and product usage.

</aside>

## Fee Discounts

Discounts can come in two forms:

- One time discount
- Perpetual discount

For a one time discount, the most well known example is BNB. Traders using Binance can optionally pay the fee for the trade in BNB token. Those tokens are used in the process, meaning they’re a one time discount.

If the same trader wants a discount on the next trade, they need to go acquire more BNB if they don’t have enough left over.

A perpetual discount is different - instead of spending tokens once for a discount, token holders get a higher percentage discount the more tokens they hold or stake.

For example, Binance could have structured BNB such that if you hold 10 BNB or more you get a 10% discount, 20 BNB or more 20% discount and so on, up to some maximum discount amount.

The advantage of this approach is that since users can save money by using or holding your token, it essentially always has a “floor price” of being worth at least the amount of discount it provides. This also encourages users that anticipate using the product in the future to acquire more of the token upfront, thus increasing demand for the token.

The downside is that relative to other value accrual mechanisms, discounting can be a relatively weak mechanism since the value it provides is only a fraction of the total fee owed. But discounts are relatively simple to combine with other value accrual mechanisms (BNB combines discounts with buyback and burn), and having multiple mechanisms often helps to reinforce each other.

# A Note on Regulatory Compliance

*The below section, like all contents in this guide, is not legal advice. You should always discuss every aspect of your tokenomics with a registered legal professional to ensure your design, including your value accrual mechanism, abides by any and all relevant laws and regulations.*

It’s no secret though that value accrual mechanisms are one area that can introduce risk by inadvertently causing your token to be classified as a security, or viewed as such by regulators - even if they’re wrong in doing so.

<aside>
💡 Some crypto lawyers have said that a best practice **may** be to capture value to the treasury as soon as the product launches, and to allow for the future possibility of accruing value to the token, but not to have any mechanism initially in place, nor to advertise, market, hint, or promise that any such mechanism will be put into place.

</aside>

Then, at a later date when the product is sufficiently decentralized, a decentralized governance vote can elect to start accruing value to token holders.

This path *may* have less risk of falling afoul of regulators compared to if the token had been accruing value from day one. Speak to your own professional legal representation.

# Primary Tool: Tokenomics Design Canvas (TDC)

<aside>
💡 Complete “Step 2: Value Accrual” of the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)

You can find an example of the canvas and download a [printable version to complete by hand on Canva](https://www.canva.com/design/DAFDTNKsIJs/8Ky9EoJJI7p98qKLIu2XNw/view) (please note to use it as a template you must be logged in to Canva).

</aside>

# Video Tutorial

https://youtu.be/F0H7K0F1L2o

# 2.3 Lifecycle Patterns

# Introduction

Now that you have a rough idea of the aspects that influence how a token moves through your ecosystem over its lifecycle, it’s time to complete [”Step 3: Lifecycle Patterns” in the Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).

There are four stages of a token’s lifecycle:

1. Creation
2. Transfers
3. Usage
4. Destruction

# Token Creation

As discussed in the paper [Tokenomics and Blockchain Tokens: A Design-Oriented Morphological Framework](https://www.sciencedirect.com/science/article/pii/S2096720922000094#bib23), some of the most common ways tokens are created include:

## Time Scheduled Based Emissions

Most commonly, mining, farming, or staking rewards emitted at a certain rate per day/week/month. The rate does not vary based on user activity, and each user typically earns tokens based on their pro-rata share of activity within a given period.

For example if more tokens are staked, more tokens are not emitted. The total size of the pie (total emissions) is not determined by staking activity, but each users’ slice of that pie is depends on their personal staking and total staking activity.\

## Metric or KPI based emissions

Emissions, rewards, or unlocks that occur when certain key metrics are hit, such as a certain level of TVL. The emissions rate thus responds to user activity in some manner. Though this method has historically been less common than time based emissions, [“productivity linked” variable emissions have been discussed in theory](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4071089), as well as appear in practice for some of the largest protocols by market cap.

For example, the [majority of Filecoin tokens earmarked for emissions are dependent on network storage capacity](https://filecoin.io/blog/filecoin-circulating-supply/), while a portion also emits based on a pre-scheduled rate. Time based and metric based emissions can be blended to achieve the benefits of both.

## Airdrops

Despite the attention airdrops get, they’re essentially a specific type of either time based emissions (occurs at time zero - when the protocol launches), or metric based emissions (occurs based on how many people interact with the protocol and complete certain tasks).

Recurring airdrops are no exception - they will either recur based on a time schedule, or based on certain KPIs being hit.

## Minted by Users

This can be a one time token mint event, either based on a whitelist or a first-come-first-serve “fair launch”, or it can be a recurring part of the protocol for users to continually mint and burn tokens.

An example of the former are NFT mints, BRC-20 mints, and “fair launches”. An example of the latter is DAI, the supply of DAI is constantly in flux, with users able to mint DAI from collateralized vaults, and to burn DAI to unlock collateral as they wish.

## Minted by Protocol

Tokens can also be minted by the protocol itself based on particular logic, or by a governance vote. Note this is different than spending tokens which already exist but which are held by the treasury, this is actually minting new tokens by the protocol, increasing the total supply.

For example, if the Maker protocol becomes undercollateralized (the total value of circulating DAI exceeds the total value of vault collateral), the protocol mints and auctions off new MKR tokens in order to raise enough funds to recollateralize the protocol - [this occurred in March 2020](https://blog.makerdao.com/mkr-debt-auction-announcement-and-details/).

Another example are rebase tokens, such as AMPL, where logic governing the number of tokens is built into the protocol’s contracts. The protocol [dynamically creates additional AMPL tokens as needed](https://documentingampl.medium.com/technical-guide-to-ampl-for-beginners-be19f0fa97ca), increasing the total supply if and when the price of each AMPL token exceeds the target price.

In other cases, [governance votes could approve a “token split”](https://quickswap-layer2.medium.com/you-voted-for-a-token-split-should-quickswap-split-quick-by-1-100-or-1-1000-11ef37ba6b66), which would increase the total supply of tokens and reduce the price per token, but without diluting existing token holders, and without any direct impact to the total market cap - the token equivalent of a stock split. Or governance votes could approve minting new tokens in order to fund new incentive programs such as liquidity rewards.

## Sales & Pre-Mine Distributions

Tokens granted to the treasury, ecosystem fund, team, advisors, or sold to private investors is a common large source of all tokens created, though, depending on who you ask, it is quite controversial.

“Fair launch” purists generally look down on projects with any level of pre-mined tokens, despite the fact that projects with a “fair launch” can still be outright scams and/or manipulated by insiders who acquire a significant portion of tokens at virtually no cost anyway.

Most modern projects allocate roughly 50% of tokens to the treasury, team, advisors, and investors, and while these tokens typically are locked and vest over a number of years, they are still essentially created, and part of the total supply, before users can publicly acquire or earn tokens, hence the name “pre-mine”.

Chances are at least some of your tokens will be created in sales or pre-mine distributions, but sending on your use case, a larger or smaller allocation to this type of token creation may make sense - we’ll cover specific percentages and market standards in Chapter 2.5.

# Token Transfers

Not every token should be transferrable - in some cases allowing it to be tradeable and transferrable weakens the entire purpose of the token.

For example, tokens that track users’ community reputation can become meaningless if they can be bought and sold - separating reputation from liquidity via two token model is one proposed solution.

https://twitter.com/cdixon/status/1446991369025646592?s=20

<aside>
💡 Think carefully about tokens used for reputation, governance, security, community status, permission levels, or membership. Making them tradeable or purchasable has both benefits and drawbacks.

</aside>

Consider Twitter’s “blue check mark” debacle. Once anyone could purchase a blue check mark, it immediately lost its social signal value and lead to widespread impersonation, [lower quality feeds](https://twitter.com/mcuban/status/1590551499972935680?s=20&t=SvG7z0ZErk8y1SlsmmyiZA), and a material loss in ad revenue from large companies that had “legacy” blue check marks.

The need to add different types of more exclusive, higher priced check marks, such as the gold “official organization” check mark, shows exactly how the blue check mark was cheapened, and no longer sufficiently served its original role, once it was for sale.

# Token Usage

If the only use cases for your token are price speculation, providing liquidity, or staking to earn more of the same token, it’s time to reconsider launching a token.

When thinking about token usage, think about the use cases and utilities you’re designing for, as well as *unexpected* ways in which your token might be used.

For example, Curve’s CRV token was expected to be locked as veCRV - but since pooling more veCRV together meant more voting power over the distribution of economic rewards, this unexpectedly gave rise to institutional level “CRV pools” via an entirely new protocol and token: Convex and the CVX token. This can be a source of centralization risk, as well as a type of user behavior (different user persona).

Considering how your token might be used in both desired and undesired ways will be key to designing incentives in the next step of the design process.

# Token Destruction

Tokens do not need to be permanent - they can be burned or even expire. Destroying tokens is often used as a value accrual mechanism (buyback and burn) - but that’s not the only valid reason to do so.

It can also be a crucial part of a protocol’s operations, such as AMPL rebases, slashing collateral of bad ETH validators or LINK oracles, or burning DAI when debts are paid back. The protocol could not correctly operate without destroying tokens in particular situations.

Tokens may even have an expiry date. For example users mint veCRV tokens by locking up CRV, and these veCRV tokens decay (expire) linearly over the lock period.

# Primary Tool: Tokenomics Design Canvas (TDC)

<aside>
💡 Complete “Step 3: Value Lifecycle Patterns” of the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)

You can find an example of the canvas and download a [printable version to complete by hand on Canva](https://www.canva.com/design/DAFDTNKsIJs/8Ky9EoJJI7p98qKLIu2XNw/view) (please note to use it as a template you must be logged in to Canva).

</aside>

# Video Tutorial

# 2.4 Incentive Mechanisms

# Introduction

As discussed in Part One, tokenomics is your best tool for coordinating user behaviors.

This is achieved through carefully balanced incentives - both rewarding desired behaviors, and punishing (or at least not rewarding) undesired behaviors. While obvious at a high level, the specifics of well-balanced incentives are quite nuanced and require not only a sound qualitative design but also the right quantitative parameters to achieve equilibrium in practice.

In other words, it’s one thing to say “Miners should be rewarded”, but it’s an entirely different thing to answer “This is how **much** miners should be rewarded”.

Coordinating user behavior comes down to answering these basic questions then:

- Who do you reward
- What do you reward them for doing (or for not doing)
- How much do you reward them to do it (or not do it)

CoinMarketCap and CoinGecko are littered with failed projects where builders fell into the trap of being lazy, and only answering these questions at a surface level.

In complex systems, conflicting or misaligned incentives, and the exploit vectors they create, are hard to identify at first glance, and without explicitly thinking through (and then modeling in later steps) the incentives in your tokenomics, you are blindly assuming the incentives will just happen to work out.

To illustrate how difficult this is, consider that despite being one of the best businessmen of his generation, even Jeff Bezos has stumbled in the past to balance incentives.

https://twitter.com/SahilBloom/status/1434847325990555652?s=20&t=_mgrCldd95TRkNupopIi2g

The best way to protect against inadvertent misaligned incentives is to explicitly identify all incentives, and systematically ensure those incentives are aligned. To do so, complete “[Step 4: “Incentive Mechanisms” in the Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).

It pays to be rigorous on this step - even if it feels a bit like you are repeating some of the work done earlier, that is intentional. Even billionaires get this step wrong, and not only will your incentives make or break your token, but they can also be hard or practically impossible to change after the fact, even if you get everything else about your design right!

As you complete it, you’ll identify exactly which quantifiable factors and parameters you need to stress-test, optimize, and balance. Finding the ideal specific quantified settings for them can only come from quantified modeling, which comes later in [t](https://www.notion.so/2-6-Modeling-Optimization-bcaab2f1ee2c4cceb6371ce29d3e1827?pvs=21)he process, in [Chapter 2.6](https://www.notion.so/2-6-Modeling-Optimization-bcaab2f1ee2c4cceb6371ce29d3e1827?pvs=21).

As you design your incentives, keep these warning signs and tips in mind.

# Incentive Warning Signs Checklist

Your tokenomics are at a high risk of systemic failure, and you need to be extra vigilant, if:

- Your incentives rely on one or more of:
    - [ ]  Native token price constantly increasing
        - Play-to-earn games like Sky Maxis, STPEN, and game theory inspired “(3,3)” incentives depend on token price never falling - and all had large meltdowns
    - [ ]  A collateral asset not collapsing in value
        - UST & LUNA had incentives that relied on LUNA’s value, with no mitigations in place
        - DAI & MKR have incentives that partially rely on collateral backing DAI but with multiple other incentives to mitigate this and cover situations where collateral value collapses
    - [ ]  Transferring value rather than supporting the creation of value
        - CRV incentivizes liquidity by sharing a portion of fees paid by traders to use a service. This deeper liquidity **creates** more value for all traders (lower slippage).
        - OHM incentivized staking by rewarding earlier investors with additional tokes when later investors buy in. This **transferred** the economic value directly from new users to earlier users without creating any tangible, non-speculative value.
    - [ ]  Data from 3rd party oracles
        - This is not always avoidable, but it’s important to minimize reliance on uncontrolled variables wherever possible
        - For example, oracles that relied on data from [CoinMarketCap reported heavily inflated prices during a bug](https://www.nasdaq.com/articles/coinmarketcap-suffers-a-seeming-hack-falsely-driving-crypto-prices-to-tens-of-billions), resulting in some DeFi protocols treating collateral assets as being worth thousands of times their actual value. This created exploits for users to borrow against these inflated values, as they could then default and walk away with a large profit.
- Or, your incentives would result in one or more of:
    - [ ]  A temporary, unsustainable burst of buying pressure (a pump, setting up an inevitable dump)
        - Many tokens launch with a relatively small initial supply and advertise high staking APYs, leading  to an initial rush to purchase tokens when the supply is small, only for supply to then dramatically increase immediately afterward (due to the high staking APY - keep in mind a high staking APY also means a high inflation rate, all else equal)
        - Traders on Binance are incentivized to buy BNB to pay discounted trading fees. The more trading activity, the more BNB is used, thus BNB is (at least partially) sustainably driven by long-term usage fundamentals for a product with real utility, rather than purely driven by short-term speculation
    - [ ]  An increase in the volatility or token price or product usage
        - UST’s fragility and asymmetric risks with LUNA price exacerbated volatility in the price of LUNA, rather than dampening this risk
        - Looksrare’s trading rewards incentivize spamming fake product usage (wash trading), so much so that as much as [87% of its usage is wash trading](https://decrypt.co/91510/looksrare-has-reportedly-generated-8b-ethereum-nft-wash-trading) that extracts net value from the protocol (wash traders earn rewards worth more than the fees the protocol collects from their usage, and then dump their token rewards). Thus, product usage is highly fragile and sensitive to trading rewards,.
        - Conversely, Ethereum’s EIP-1559 dampens/stabilizes downturns in product usage caused by hoarding tokens to benefit from deflation, as the platform becomes more inflationary, encouraging more use. At the same time, high levels of use and spike in gas due to congestion create relatively more deflation, encouraging holding rather than immediate use, which reduces/stabilizes network congestion.
- Or, your product has one or more of these “death spiral” characteristics:
    - [ ]  Your product’s ability to function depends on your native token price
    - [ ]  Your contracts can mint tokens (creating a potential abuse)
    - [ ]  Mints or burns of your protocol token can be anticipated (front-running abuse)
    - [ ]  Your token can be shorted on a liquid marketplace
    
    Source: [Checklist for Destruction: The Turbo Death Spiral, Part 1](https://medium.com/@0xRez/the-turbo-death-spiral-part-1-checklist-for-destruction-e024f19215f8)
    

If you find yourself mentally checking off one or more of the boxes above, that doesn’t necessarily mean your product or incentives are broken or can not work - but it does mean you need to consider your design and risk management very carefully.

# Incentive Design Tips

## Make Incentives Tangible

To be most effective, incentives (disincentives) should be as tangible as possible. The less directly users are affected, or the longer it takes to affect them, the weaker the incentive becomes.

Even when asking users to commit to long-term actions, such as locking up CRV for up to four years at a time, the benefits are still tangible and are at least partially realized right away - users get a higher weight of veCRV tokens immediately, and all the associated benefits, including revenue distribution.  

Conversely, tokens that solely exist as governance tokens offer relatively weak incentives - on their own, there’s not much tangible benefit to being able to govern a protocol.

https://twitter.com/VitalikButerin/status/1597570120456769536?s=20

MKR holders have incentives beyond pure governance, as they have an economic incentive to grow the adoption of Marker DAO’s stable coin DAI in a sustainable way. MKR’s value accrual mechanism benefits when more DAI is issued, but MKR is diluted if the protocol becomes undercollateralized due to poor risk management.

This is certainly more tangible than if MKR lacked any economic incentives, though as economic incentives go, they’re not the most tangible. For example, a bad actor ETH validator feels the sting of being slashed almost immediately - yet if MKR holders are bad stewards of the protocol, it might take years for the realized costs to play out.

In this light, it’s perhaps not so surprising that Maker DAO has made some controversial and questionable decisions in more recent years. Backing the majority of DAI with the centralized stablecoin USDC via the [Peg Stability Module](https://blog.makerdao.com/governance-polls-november-23-2020/) helped to secure the DAI peg, but undoes much of the value proposition for DAI in the first place - a **decentralized** stablecoin.

DAI’s reliance on centralized USDC has already created problems internally, with Maker’s founder Rune Christensen even proposing to [convert USDC collateral to ETH collateral when Circle froze USDC balances after the Tornado Cash ban](https://www.coindailynews.io/2022/08/13/makerdao-to-convert-usdc-into-eth-ahead-of-ethereum-merge-community-reacts/). 

Why would MKR holders introduce these additional custodial and censorship risks to DAI, when they’re incentivized to sustainably grow its adoption?

One contributing factor is that the disincentive of taking a loss when the protocol becomes undercollateralized is simply not very tangible - [people have an irrational psychological bias to underestimate systemic risk](https://nicholasbarberis.github.io/ch18_6.pdf).

Time will tell how this will play out for Maker and DAI.

Curve’s gauge weights represent another, arguably more egregious example. veCRV holders are effectively incentivized to purely maximize their immediate profit from emissions rewards. While there is theoretically an incentive to not harm the protocol in order to continue to earn rewards for the long term, this incentive is extremely intangible.

One potential approach to make this incentive to protect the overall long term adoption of the protocol much more tangible would be to give gauge weight voters skin in the game.

> **Give veCRV voters risk exposure to the pools they endorse with incentives. Meaning, when you vote for a pool in the gauge, you must escrow your veCRV to back the value of that pool’s stable assets. If the value of an LP token drops by too much, you are liquidated and the LPs protected.
Source: [All for One, or One for All? Where incentive alignment is lacking in DeFi tokenomics and some ideas to improve](https://medium.com/@kirkhutchison/all-for-one-or-one-for-all-bdc88cf36323)**
> 

While this mechanic is not perfect, it would certainly result in veCRV voters being more intentional about their behavior in directing rewards.

## Make Incentives Simple to Understand

Incentive mechanisms are complex - but even if there’s a lot of complexity involved, incentives should be simple for users to understand the key takeaways.

You don’t need to understand every in and out of Ethereum’s consensus mechanism to know that it hurts to be slashed for going offline.

The reality is that the vast majority of your users are not going to want to know every single detail of the inner mechanisms of your product.  But they all want to be able to quickly know the key takeaways.

GMX’s escrowed rewards mechanism is relatively complex - there are staked tokens, escrowed tokens, multiplier points, conversion ratios, etc. Users who want to crunch all the numbers can do so with the documentation and calculators GMX provides - but much more importantly, the key takeaways of the mechanism are simple to understand and quick to explain.

The longer you stake, the more your rate of reward compounds.

Despite deeply problematic tokenomics and a flawed description of the game theory involved ([staking is not the dominant strategy in a continuously repeated game](https://www.jasss.org/20/4/12.html#7.10)), OHM drew huge attention in part because of simple messaging that made it easy for momentum to build: “If everyone stakes, everyone wins”.

Of course, this wasn’t a realistic representation of the incentives at play. But the truth doesn’t quite have the same ring to it: “If everyone stakes everyone temporarily wins on paper until someone starts to sell to realize their profits, at which point the optimal strategy is to also sell as soon as possible.”

<aside>
💡 The point is **absolutely not** to oversimply things to lie to your users. The point is that when even complex incentives have simple key takeaways, they can be incredibly powerful - for good or for bad.

</aside>

Taking shortcuts with your incentives and how you market them can work for a bit, but it can’t lead to long-term success. As founders like Do Kwon have learned the hard way, misrepresenting your incentives can end with a warrant for your arrest.

## Abuse Your Incentives

Most importantly, you **must** try to break, abuse, and exploit your incentives before finalizing your design and launching.

When designing a new incentive, ask yourself: “What could go wrong? How could I abuse this to make a profit, or to sabotage things if I wanted it to fail?”

For example, in the earlier Amazon example, ask yourself: “What would I do, as a manager at Amazon, if I got paid a bonus every time I fired someone?”

The obvious answer is that you’d fire more people.

And how do you get more people to fire (without sacrificing your department's other KPIs you’re rewarded on)?

You hire incompetent people just to fire them.

<aside>
💡 It’s not enough that your incentives work in the absence of malicious actors - the whole value of well-designed incentives is that they are impervious to malicious actors.

</aside>

Malicious actors aren’t always profit-motivated. 

If your incentives allow for performing an undesired action for free - sooner or later some jerk is going to come along and spam that undesired action all day long, not because it helps them to do so, but because it doesn’t hurt them to do so.

This is another reason why designing incentives is so difficult - there’s always going to be someone smarter than you out there (whether human or AI), and the more complicated your incentives are, the easier it’s going to be for them to find an exploit that you overlooked.

Thus, the implications when it comes to designing your incentives are twofold:

- Keep things simple where possible - simpler systems are easier to test and harder for cracks to go overlooked before launch. Bitcoin is a prime example. Though it has a much more restrictive language and is capable of fewer use cases than fully expressive smart contracts, its proponents see this as a security feature, not a bug.
- Modeling and simulations are critical - no matter how simple your incentives may be, modeling is the best tool builders have to stress test and abuse their incentive mechanisms. Teams that have no risk management and scenario analysis modeling will struggle to raise investment and be at higher risk of launching with critical vulnerabilities.

## Optimize Your Incentives

As discussed in [Chapter 1.2](https://www.notion.so/1-2-What-is-Tokenomics-3a6dacd60eaf41ab95d832f60d7a8bef?pvs=21), builders need to think carefully not just about **who** and **what** they reward or incentivize, but also **how much** they do so.

Excessive rewards that are misaligned with the value created is wasteful and creates short-term distortions that can increase price volatility, attract the wrong type of user base, and actually reduce long-term adoption of the product.

A classic example is protocols maximizing the rate of return for their reward emissions to try to attract users at all costs. As a result, emissions end up much higher than is necessary to attract most users, resulting in more mercenary capital behavior, and higher rates of inflation without much benefit.

[Source: [Incentive Spend: Elasticity and Optimization](https://medium.com/gauntlet-networks/incentive-spend-elasticity-and-optimization-18aa7f608d3d)](https://miro.medium.com/v2/resize:fit:720/0*kmRpqZaQWorrXIO3)

Source: [Incentive Spend: Elasticity and Optimization](https://medium.com/gauntlet-networks/incentive-spend-elasticity-and-optimization-18aa7f608d3d)

As indicated in the chart, above or below a certain range incentives become relatively inefficient at attracting the next marginal user.

For example, very few people care about doubling a 1% yield to a 2% yield. This doubles the incentives the product must distribute but doesn’t make much of a difference. Doubling a 10% to 20% yield, however, is likely to draw much more attention, despite representing the same degree of increase in paid incentives. Beyond a certain point though, indifference returns - doubling a 25% yield to a 50% yield isn’t going to attract many users that weren’t already drawn in by the already quite high 25% yield in the first place.

> **A robust tokenomic model [has] the ability to compensate individuals proportional to the value created (and destroyed)… Aligned compensation incentivizes risk — or cost-bearing commitments and other forms of longer-term investment. Conversely, non-aligned compensation encourages mercenary capital which often preserves maximum freedom to exit… Design mechanisms that do not align compensation tend to destroy long-term value, especially when interacting with feedback loops. For instance, giving artificially high rewards to holders of an NFT collection may kick off a speculative run that reverses brutally once the rewards are exhausted — possibly destroying the perceived value of the collection.
Source: [Token Design for Serious People](https://jumpcrypto.com/writing/token-design-for-serious-people/)**
> 

<aside>
💡 Creating the right incentives means optimizing **how much** to reward or punish certain behaviors. Even if you reward the right users for the right actions, rewarding them too little will not have the intended effect, and rewarding them excessively can actually distort the incentives and change user behaviors to be more short-term focused.

</aside>

The best way to balance incentives is to first map them out qualitatively and balance them from a first principles and game theory approach, as you will do at the end of this chapter, and then use experimentation and modeling to quantitatively stress-test assumptions and optimize for your particular objectives, as we will cover in Chapter 2.6.

# Common Forms of Incentives and Disincentives

There are many ways to incentivize or disincentivize user behavior. Builders should consider how each of them might be a fit for their use case, as well as any legal and regulatory implications for their situation.

Some of the most common incentivizes or disincentivizes include:

- Granting or revoking access or inclusion
- Applying a discount or charging a premium
- Rewarding in kind (more of the same currency) or slashing collateral
- Rewarding in a reference currency (such as a non-native token-denominated share of protocol revenues) or confiscating accrued rewards
- Increasing expected value of holdings or diluting share of holdings
- Increasing or decreasing social reputation
- Increasing or reducing barrier-to-entry costs or taxes
- Ensuring positive or negative expected value

# Additional Resources

Incentives mechanisms, and modeling in the next chapter, are arguably the two most important aspects of your tokenomics and the design process.

The below resources are some of the best materials you will find for builders who wish to take an even deeper dive into more advanced incentive and mechanism design concepts.

- Ethereum 2.0 Economic Review
    - Blog, [An Analysis of Ethereum’s Proof of Stake Incentive Model](https://tomborgers.medium.com/ethereum-2-0-economic-review-1fc4a9b8c2d9)
    - Paper, https://drive.google.com/file/d/1pwt-EdnjhDLc_Mi2ydHus0_Cm14rs1Aq/view
    - Spreadsheet Model, https://docs.google.com/spreadsheets/d/1y18MoYSBLlHZ-ueN9m0a-JpC6tYjqDtpISJ6_WdicdE
- Paper, [How Can Incentive Mechanisms and Blockchain Benefit with Each Other?](https://dl.acm.org/doi/10.1145/3539604)
- Paper, [Mechanism Design Approaches to Blockchain Consensus](https://www.nber.org/system/files/working_papers/w30189/w30189.pdf)
- Paper, [A Survey of Behavioral Finance](https://nicholasbarberis.github.io/ch18_6.pdf)
- Blog, [DeFi Economic Model: Four Incentive Models from Value Flow Perspective](https://mirror.xyz/0x70562F91075eea0f87728733b4bbe00F7e779788/g9-n9JAAxw1-j-m-qJj221a6YLmRhUQz_yJgluJaSkE)
- Blog, [Intro to AMM Incentives](https://www.gauntlet.xyz/resources/intro-to-amm-incentives)
- Blog, [Incentives structures](https://cobie.substack.com/p/incentives-structures)
- Forum, [Uniswap Incentive Design Analysis](https://gov.uniswap.org/t/uniswap-incentive-design-analysis/21662)
- Forum, [Gauntlet <> Compound Incentive Optimization](https://www.comp.xyz/t/gauntlet-compound-incentive-optimization/4267)
- Slides, [Long term Growth Strategies Using Token Incentives](https://drive.google.com/file/d/16aRLylh1DlVL4t_6T3s7vUEYnyzIcNdz/view)
- YouTube, [Transaction Fee Mechanism Design for the Ethereum Blockchain](https://www.youtube.com/watch?v=dtNHdilXKyo)
- YouTube, [Cryptoeconomics, Token Design, and Incentives in DeFi](https://www.youtube.com/watch?v=_LjYvQGfxOk)
- YouTube, [DeFi Incentives - Running Your Protocol Like a Business](https://youtu.be/Sdoz1sOQ-Hw)
- Twitter Spaces, [How to grow a DeFi protocol](https://twitter.com/Blockworks_/status/1671621347578105858?s=20)
- Twitter Spaces, [Building an Optimal Incentives Program](https://twitter.com/0xKofi/status/1643292763578851330)
- Twitter Spaces, [Mechanism Design Deep Dive](https://twitter.com/Blockworks_/status/1689743043287506944?s=20)
- Book, [Twenty Lectures on Algorithmic Game Theory](https://www.amazon.com/dp/131662479X)
- YouTube, [Twenty Lectures on Algorithmic Game Theory](https://www.youtube.com/playlist?list=PLEGCF-WLh2RJBqmxvZ0_ie-mleCFhi2N4)
- YouTube, [Transaction Gas Fees Economics: Keynote from Vitalik Buterin (Ethereum Foundation) at Ethereum Meetup 2018](https://www.youtube.com/watch?v=7vuTtvshR34&t=2s)

# Primary Tool: Tokenomics Design Canvas (TDC)

<aside>
💡 Complete “Step 4: Incentive Mechanisms” of the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)

You can find an example of the canvas and download a [printable version to complete by hand on Canva](https://www.canva.com/design/DAFDTNKsIJs/8Ky9EoJJI7p98qKLIu2XNw/view) (please note to use it as a template you must be logged in to Canva).

</aside>

# Video Tutorial

https://youtu.be/9LpaeVXbJBI

# 2.5 Supply Policy

# Introduction

We’re now at the step most people think of when they hear the word tokenomics: supply policy. To complete this step, you’ll customize the [Tokenomics Modeling Template featured in “Step 5: Supply Policy” of the Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21). To help you do so, let’s discuss token supply from a **data-driven** lens.

There have been a number of quantitative reports, including analysis of thousands of tokens and years of data conducted specifically to create this guide, on how to optimize aspects like max supply, emissions rates, vesting, etc. - we’ll look at all the data in this chapter so you as a builder can make an informed decision.

Before getting carried away, it’s worth noting the relative importance of the topics in this chapter.

Builders *think* inflation matters, and of course, egregious hyperinflation does matter (Sky Mavis, STEPN, etc), but if you’re doing reasonable things, which you’ll know by using comps and by modeling and simulating your designs in the next chapter, the impact of inflation is generally overrated.

<aside>
💡 Separate analyses conducted by different parties on different data sets and with different methodologies have both found that changes to token supply at most explain about 5% of price changes on a month-to-month or shorter time frame, even after controlling for overall market conditions. In other words, the remaining 95%+ of token price performance is explained by token specific factors other than emissions, such as incentive mechanisms, use cases, utility, value capture, value accrual, supply sinks, random events, etc.

</aside>

While emissions certainly can be optimized, builders should recognize that the benefits of taking emissions are much smaller than believed.

It’s important to get other aspects of your tokenomics right, and then optimize your emissions within the constraints the rest of your design creates - doing it in reverse (optimizing emissions first and then fitting the rest of the design to those emissions constraints) doesn’t make sense, and isn’t supported by the data.

# Common Token Supply Misconceptions

## Minimizing Circulating Supply is Always Better

Fueled by an overblown fear of inflation - builders only think about *too much* token supply being in circulation. Yet you should worry about the exact opposite when you first launch a token - having *too little* supply available at launch.

That’s because when your token first launches is generally:

- At or close to maximum hype surrounding the project and token
- The lowest circulating supply the token will ever have

The combination of these factors can result in a large amount of FOMO buying, resulting in an unsustainable pump in price that immediately crashes once token emissions kick in - since that level of concentrated buying demand per unit of available supply simply can not be maintained as hype decreases and/or supply increases.

<aside>
💡 When launching a token, consult with your legal team to evaluate whether you can use a price discovery mechanism, such as a Dutch Auction, in order to avoid severe imbalances in the initial token demand and supply causing a pump-and-dump.

</aside>

Liquidity crunches create high price volatility and pump-and-dump price patterns that can often leave a project’s adoption and community engagement worse off than where it started. Too many sinks can mean too little liquidity, which means your price is more fragile to crash, and by the time those sinks unlock, people will be looking to also dump the token.

https://twitter.com/_portersmith/status/1483218927480094720?s=20&t=TVpnQFqHnxsFMJJhIt5jPg

Rather than aiming to lock up supply for the sake of having as low a supply as possible, the aim should be to balance user demand with available liquid supply. One solution is to reward stakers of LP tokens (liquidity providers) more than stakers of your token.

<aside>
💡 By rewarding LP token stakers with a higher weight in staking rewards than default stakers of your token, you incentivize sufficient liquidity relative to staking. Ideally, this is dynamic - route a larger share of rewards to staked LP tokens the greater the ratio of default staked tokens to staked LP tokens, in order to incentivize liquidity when it’s most needed.

</aside>

Finally, having clear, transparent communication of valuation metrics helps users avoid short-term speculation and instead fosters sustainable community engagement.

For instance, if you were launching a competitor to AAVE, you could feature AAVE’s MarketCap/TVL (and other competitors) as well as your own token’s MarketCap/TVL on your front end or Discord.

If AAVE’s MarketCap/TVL valuation metric is 0.18, and your token is currently trading at a MarketCap/TVL of 0.20, that’s important for your community to know, and would be a good indication that your token may not be ideal to buy at this time (preventing FOMO pump-and-dumps). Conversely if that metric falls below AAVE’s, the transparency helps highlight that now may be a good time to buy, supporting price when it’s most needed.

These approaches - price discovery mechanisms at launch, incentivizing liquidity more highly relative to staking, and transparent pricing relative to comps - helps prevents your tokens from getting unsustainable run up into a pump-and-dump, maintain sufficient liquidity, and support the token if it’s been oversold and is relatively cheap.

## Higher Rewards are Always Better

Another mistake builders make that wastes their gunpowder is assuming that when it comes to staking rewards, or other similar yields distributed in their native token, higher is always better.

But why?

A **stable** 15% yield is already exceptionally high - enough to attract most people’s attention, especially if it's stable and sustainable.

Increasing that yield to 30% or 100% is overkill - you’re getting less bang for your buck, attracting the wrong type of user, and needlessly increasing your inflation rate.

https://twitter.com/Flynnjamm/status/1625714284192755712?s=20

Emissions rates that emit a fixed number of tokens no matter what are needlessly inflationary. If only 25% of tokens are staked, what would otherwise be a 10% yield becomes a 40% yield.

Instead of emitting the 40% yield, it likely makes more sense to cap the maximum yield at something like 15%, and directly the excess tokens either to a treasury or burn address.

Similarly, if your product relies on attracting both **supply side** users (e.x. liquidity providers) and **demand side** users (e.x. traders), you don’t want to waste excess rewards where they’re not needed.

For example, if you have much more supply side (overcapacity), than demand, but continue to reward the supply side at the same rate, you’re wasting your gunpowder for no benefit. Reducing rewards to the supply side to increase rewards to the demand side would result in more overall user activity, without increasing emissions - or even with reducing overall emissions.

<aside>
💡 Rewards should be dynamic based on user behavior to target a **maximum cap** yield distributed and a balance between supply users and demand users. Rewards above the cap, or to the user type you have an excess of, create more inflation for little benefit.

</aside>

There’s nothing unsustainable about a maximum cap - it’s the opposite, it improves sustainability. The same is not true of minimum floors. Guaranteeing a minimum yield can not be sustained long-term without hyperinflation ensuing because any shortfall not covered by organic protocol revenues must come from minting tokens and the token number of tokens required to distribute compounds over time.

## More Deflation is Always Better

It might shock you to hear- but more deflation is not always necessarily a good thing.

There are a few reasons this is the case:

### Deflation Can Reduce Economic Activity

Let’s return to our earlier UBR token example. Suppose that UBR tokens are being burned for each ride taken, and a decent portion of riders and drivers are holding UBR instead of immediately selling them.

Given dApp usage stays stable, the deflation in UBR means the token will appreciate in price. As a result, more riders hold a larger portion of their UBR tokens, trusting that the price will continue to appreciate - they’d rather pay in USD rather than use UBR since they expect UBR to be worth more in the future.

As you might see, this becomes a feedback loop.

<aside>
💡 Excessive deflation leads to higher token prices, which leads to hoarding instead of using the token (less economic activity), which means less available supply, which leads to higher prices, and so on. Usage of the dApp declines. The fundamentals supporting the token become less healthy.

</aside>

This is part of the strength of Ethereum’s EIP-1159 - if usage decreases, the rate of deflation decreases, providing a counteracting mechanism to the reinforcing deflationary feedback loop that can kick in.

The threat of a deflationary feedback loop is not just theoretical, historical case studies from macroeconomics include Japan’s “lost decade” as well as the Great Depression in the United States:

- [Understanding the Costs of Deflation in the Japanese Context](https://www.imf.org/external/pubs/ft/wp/2003/wp03215.pdf)
- [Japan's Bubble, Deflation, and Long-term Stagnation](https://www.esri.cao.go.jp/en/esri/archive/e_rnote/e_rnote20/e-rnote019.pdf)
- [The Great Depression](https://www.federalreservehistory.org/essays/great-depression)

### Deflation Can Limit Your Resources

Recall that one of the largest benefits of tokenomics is to coordinate user behavior via incentives. In this light, your token is your “gunpowder” available to fuel these incentives.

Modern Ethereum is an example of still having **gross** inflation (minting validator rewards) while still being **net** deflationary (burning more gas fees than tokens mined). This is incredibly powerful because it enables deflation while retaining the benefits of aligning incentives necessary for validators to secure the chain.

One of the [largest open debates regarding Bitcoin is its emission schedule](https://thebitcoinmanual.com/articles/btc-tail-emissions-debate/) - that the halving of block rewards every 4 years, and eventually end to block rewards, means that unless something drastically changes, there will be dwindling incentives for miners to secure the chain.

In other words, Bitcoin is facing a worrying position of spending all its “gunpowder” crucial to aligning incentives, before establishing an organic fee market that could sustain the security budget on its own.

https://twitter.com/Justin_Bons/status/1628117104040747011?s=20

If maxis have their way, it’s hard to see how this could ever happen: anti-ordinals, anti-BRC20s, anti-tokens issued on Bitcoin L2s or sidechains such as Stacks or RSK… where does the demand for block space come from if not from securing additional assets and use cases to Bitcoin?

Ironically, the Lightning Network, the most adopted Bitcoin layer to date, and the only one supported by maxis, is intended to **reduce** fees (though to be fair it may serve to increase fees as a second-order term with higher overall adoption).

<aside>
💡 Builders shouldn’t optimize for deflation at the expense of the incentive mechanisms crucial to their product. While you should aim for sustainability, rushing to be deflationary before finding organic demand is a great way to kill your product early.

</aside>

### Deflation Is Not A Use Case or Utility

Because of the focus of Bitcoin on a max supply, and Ethereum’s new deflation “sound money” narrative, it’s understandable why builders sometimes mistake deflation as a core use case or utility.

It’s not. If deflation alone were a solid use case, then tokens like the BOMB token should be even more successful than Bitcoin.

https://twitter.com/BombToken/status/1147658121885757442?s=20

The BOMB token took deflation to the extreme - deflation as a use case. Ironically, despite the token’s single goal of appreciating in value, [BOMB is down more than 99% since its all-time high](https://www.coingecko.com/en/coins/bomb).

(A lot of coins, including BTC and ETH, have at some point dropped by as much as 90% from their highs, so you might be thinking -99% is not that much worse than -90%. But the human brain isn’t great at making sense of negative percentages approaching a total loss of -100%. In reality, its much worse: a -99% return is equivalent to losing 90% twice in a row. You need a return of 10x to recover your money after -90%; after -99% you need 100x.)

A similar gimmick is tokens that boast a high number of tokens burned - especially when right after minting. Other than the memes, there is no difference between a token that has a max supply of 10 million and one that starts with 100 million, mints 95 million to the treasury, and burns 90 million of them after minting. These are marketing gimmicks, not use cases or utilities.

Deflation is another tool in the tokenomics toolset, not a goal to optimize for at the expense of everything else.

# Token Supply Best Practices

## Maximum Supply

Builders, and the community in general, are often guilty of knee-jerk reactions to assume that having a maximum supply is always better than a token with no cap.

In practice, tokens with a max supply eventually become deflationary, due to no new supply while tokens are lost or burned, whereas tokens with an unlimited supply are typically inflationary and are not deterministically deflationary.

This is often the basis for arguments supporting why a max supply cap is better than no max supply, but there are plenty of counterpoints to suggest that isn’t always the case:

- Macroeconomics suggests there may be [asymmetric dangers to deflation](https://deliverypdf.ssrn.com/delivery.php?ID=815017127117092119001112086107068023031027086039084088067035097122104009030058057006099084057042064083076084054076000092124076116085062012125080117029023000008124000012123122012085111005006001100005000077022091127101&EXT=pdf&INDEX=TRUE) compared to low rates of inflation
- Two of Bitcoin’s closest “competitors” have no max supply
    - Ethereum has never had a max supply (even though one was proposed before The Merge)
    - Monero has tail emissions to incentive ongoing PoW mining
- A constant rate of annual inflation (tail emissions), is [not inherently inflationary](https://petertodd.org/2022/surprisingly-tail-emission-is-not-inflationary) - given a Bitcoin core dev wrote this argument, it’s worth paying attention
- The Nouns DAO model (1 NFT minted per day) technically has an unlimited supply, but the inflation rate approaches zero over time, making it similar in effect to a capped supply model

Regardless, builders still obsess and agonize over max supply!

You want to tailor your answer to your use case - the truth is there is no one universally best choice between uncapped or capped, and if capped, how many tokens to cap it at.

That said, we can dive deeper into the data for insights into what may **generally** work for most builders.

### Capped vs Uncapped Total Supply

There are some uses where a max supply simply is not relevant.

For example, if you are issuing any type of tokenized asset (ex. carbon credits), pegged asset, wrapped asset, or user-minted asset against collateral (including stablecoins), the supply should be uncapped. New carbon credits can always be created. More collateral can be deposited to mint more assets. What gives these tokens their value isn’t scarcity, it’s their peg mechanism ensuring they are backed 1:1 by the asset they represent or have a claim to.

If those use cases don’t apply to you, you should still base your decision on your use case - does your use case require tail emissions? Then use uncapped.

Analysis comparing the performance of uncapped vs capped supply tokens by TaschaLabs found conflicting results - uncapped tokens outperformed in 2022 (bear market) but underperformed in 2021 (bull market).

https://twitter.com/TaschaLabs/status/1601974064247369728?s=20&t=9hhqvHycFg41ljX68sYFpw

Yet this study alone, while suggestive, is not terribly convincing due to its short time frame and lack of statistical significance tests.

### Historical Returns Analysis

To follow up, using data from CoinGecko and CoinMarketCap, I ran an analysis of the Top 1,000 tokens by market cap each month for the past 5 years, excluding stablecoins and wrapped assets.

Due to the changing nature of the tokens (tokens cycle in and out of the Top 1,000), and the long time frame spanning bull and bear markets, it would be relatively meaningless to compare raw price performances - the figures could be easily skewed by random noise in the month-to-month data. Thus, each token’s monthly performance was normalized by that month’s market cap-weighted market return. This yields each token’s excess monthly return above/below the total market of the Top 1,000 tokens for the month in question.

**Excess Returns by Max Supply Type*
*Top 1,000 by Market Cap, Monthly, June 2018 - June 2023**

| Max Supply | Mean Relative Monthly Return | Median Relative Monthly Return | Stdev of Relative Monthly Returns (Not Annualized) |
| --- | --- | --- | --- |
| No Cap | -1.36% | -4.2% | 26.2% |
| Capped | -2.7% | -6.0% | 37.6% |

**Not all results are statistically significant. See notes below.**

The results found that uncapped tokens (no max supply) did perform better than capped tokens, but this difference was not statistically significant, even at a *p* of 0.10. 

However, using [Levene's test](https://en.wikipedia.org/wiki/Levene's_test) to assess differences in variance indicated a statistical difference at a **p** of 0.05, suggesting that tokens with a capped supply exhibit a more narrow range of performances.

Repeating the analysis for the Top 100 monthly yields nothing of statistical significance for relative returns, but does also find significance for lower variance for uncapped tokens.

### Over/Under Representation Analysis

Another alterative way to look at the data is to check the relative representation of each type of token in the Top 100 projects vs Top 101 - 1,000 projects by market cap.

For instance, if 50% of Top 100 projects are uncapped, but only 10% of Top 101 - 1,000 projects are uncapped, then uncapped tokens are 40% “overrepresented” in the Top 100 - a weak suggestion that there may be a bias for uncapped tokens to perform better and achieve higher market caps.

**Top 100 vs Top 101 - 1,000 by Max Supply Type, June 2023**

| Token Price Bucket | Excess Representation in Top 100 |
| --- | --- |
| No Cap | +15.9% |
| Capped | -15.9% |

Once again, we have another data point in favor of uncapped supply tokens - they are overrepresented in the Top 100 project by a statistically significant degree.

Overall, the data does not indicate a statistically significant clear winner - though there is some evidence in support of uncapped tokens. While this may seem like a non-result, given conventional wisdom is often that “capped supply is always better”, it’s noteworthy that the data does not support this hypothesis.

<aside>
💡 Builders should not only consider designs with a max supply based on conventional wisdom - it is not supported by data. Instead, they should evaluate both uncapped and capped supply approaches and select whichever is a better fit for the use case.

</aside>

### Optimizing Capped Maximum Supply

If you’ve decided to operate with a capped maximum supply model, the next logical question is: “What should the max supply be?”

The answer, which you may not like, is that it doesn’t really matter all that much - other than playing on psychological biases the number is entirely arbitrary.

There’s no fundamental reason Bitcoin **must** have been set to 21 million max supply when it first launched. It could have just as easily been 2.1 million, or 210 million, or 137.4 trillion. The specific number doesn’t matter - what matters to people is that now that it’s been set at 21 million, it stays at 21 million.

The biggest factor influenced by the max supply of tokens you chose is what your token price will be at a given market cap.

**Price per Token given a Circulating Supply (y-axis), and Market Cap (x-axis)**

|  | $1mm | $5m | $10mm | $50mm | $100mm | $500mm | $1bn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1,000,000 | $1.0000 | $5.0000 | $10.0000 | $50.0000 | $100.0000 | $500.0000 | $1,000.0000 |
| 10,000,000 | $0.1000 | $0.5000 | $1.0000 | $5.0000 | $10.0000 | $50.0000 | $100.0000 |
| 100,000,000 | $0.0100 | $0.0500 | $0.1000 | $0.5000 | $1.0000 | $5.0000 | $10.0000 |
| 1,000,000,000 | $0.0010 | $0.0050 | $0.0100 | $0.0500 | $0.1000 | $0.5000 | $1.0000 |
| 10,000,000,000 | $0.0001 | $0.0005 | $0.0010 | $0.0050 | $0.0100 | $0.0500 | $0.1000 |

While the price per token should not matter to **rational** market actors - there is evidence from behavioral finance studies that stock market investors display several biases based on the price per share.

The price per share, like the price per token, is entirely arbitrary and alone tells a rational investor nothing about the relative value of the company, its recent performance, or its expected future performance… and yet:

- Stocks tend to materially outperform following stock splits (decreasing price per share and increasing number of shares, while keeping market cap and dilution constant). In a 1:10 split, if you own 1 share at $100/share before the split, you own 10 shares at $10/share afterward - $100 still buys the same percentage of the company in both cases. This overperformance following splits is possibly due to investors’ irrational preference for the lower-priced shares.
**Source: [What do Stock Splits Really Signal?](https://www.researchgate.net/publication/227406318_What_do_Stock_Splits_Really_Signal)**
- At least some investors display an irrational bias towards lower-priced shares on the belief for greater potential percentage gains. This is of course irrational, holding liquidity constant, it takes just as many dollars of net buying pressure to double a $100mm market cap company’s share price whether its share price is $0.01 per share or $1,000 per share. Nevertheless, at least a certain type of investor would irrationally feel the $0.01 has larger potential gains.
**Source: [The Conceptual and Empirical Relationship Between Gambling, Investing, and Speculation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5370364/)**
- Various studies in consumer marketing have found a “left-digit anchoring” bias. For instance, buyers irrationally perceive $9.99 to be a materially better deal than $10.00. It’s quite possible a similar anchoring bias exists in financial markets, though no behavioral finance studies have yet to explicitly confirm or reject this.
**Source: [The Left-Digit Bias: When and Why Are Consumers Penny Wise and Pound Foolish?](https://journals.sagepub.com/doi/full/10.1177/0022243720932532)**

While these biases generally suggest “the lower the token price the better”, it logically follows there is some lower bound to this benefit. For example, if consumers value the lefthand most digit most, there is likely a much bigger psychological difference between a token price of $.01 and $1.00 than there is between $0.000001 and $0.0001, even though in both cases the second price is 100x the first price. If people need to pause and carefully count leading zeros, the price is probably beyond the optimal point for any “lower price” bias.

But we don’t need to just assume these biases play out with token and crypto asset prices - we can dig into the data to check for evidence of preferences for certain token prices.

### Historical Returns Analysis

Using the same approach described earlier to arrive at each token’s excess monthly returns, we can then group each token into price ranges according to its price per token at the time.

Sliced this way, the same token may change buckets over the course of the data analyzed - the purpose is not to analyze the returns of tokens that **started** in a certain price range, the purpose is to analyze whether certain price ranges consistently perform better or worse, benefitting from an irrational bias for certain prices per token.

**Excess Returns by Token Price Bucket*
*Top 1,000 by Market Cap, Monthly, June 2018 - June 2023**

| Token Price Bucket | Mean Relative Monthly Return | Median Relative Monthly Return | Stdev of Relative Monthly Returns (Not Annualized) |
| --- | --- | --- | --- |
| <$0.01 | -3.4% | -6.7% | 38.4% |
| ≥$1.00 − <$10.00 | -2.8% | -5.8% | 36.5% |
| $0.01 − <$0.10 | -2.6% | -5.9% | 37.9% |
| ≥$0.10 − <$1.00 | -2.5% | -6.1% | 37.4% |
| ≥$100.00 | -2.0% | -2.7% | 26.6% |
| ≥$10.00 − <$100.00 | -1.5% | -5.4% | 33.0% |

**Most results are not statistically significant see description below.
**If you’re wondering how every bucket is negative, this indicates that in every bucket, an equal-weighted index of tokens in that bucket generally underperforms a market cap-weighted index of all tokens.*

Interestingly, these findings seem to reject the “lower price is better” hypothesis. Even at a *p* of 0.10, there was only one statistically significant difference in head-to-head comparisons of each price bucket.

The $<0.01 price bucket has statistically significantly worse (*p*=0.0496) returns than the ≥$10.00 - <$100.00 price bucket.

Tokens <$0.01 also had a statistically significant higher variance of relative monthly returns than ≥$1.00 − <$10.00, ≥$100.00, and ≥$10.00 − <$100.00 buckets, suggesting a consistently wider range of performance relative to the market.

The implication for builders is to avoid selecting max supply such that your expected token price is <$0.01. Beyond this point, the data suggests tokens significantly underperform and potentially experience more volatility.

This is perhaps because they are psychologically perceived as high-risk, or perhaps drowned out by a large number of low-quality coins that try to use a low token price as a gimmick.

Repeating the analysis for the Top 100 monthly tokens yields nothing statistically significant about better or worse returns for each bucket.

### Over/Under Representation Analysis

Another alternative way to look at the data is to check the relative representation of each token bucket in the Top 100 projects vs Top 101 - 1,000 projects by market cap.

If prices of tokens are randomly distributed, a given price bucket should have a similar percentage of each segment of projects.

But if a given price bucket is overrepresented in the Top 100, this may be a weak indication that token prices in that bucket benefit from a subjective bias, leading them to be higher in the market cap rankings.

Conversely, an underrepresentation is a weak indication of a bias against that token price bucket.

For instance, if 20% of Top 100 projects have a price of ≥$1.00 - <$10.00, but only 5% of Top 101- 1,000 are in that bucket, it is 15% overrepresented in the Top 100 - a weak suggestion investors have a psychological bias for that price range.

**Top 100 vs Top 101 - 1,000 by Price Bucket, June 2023**

| Token Price Bucket | Excess Representation in Top 100 |
| --- | --- |
| ≥$0.10 − <$1.00 | -12.2% |
| $0.01 − <$0.10 | -1.0% |
| ≥$1.00 − <$10.00 | +1.8% |
| <$0.01 | +2.0% |
| ≥$100.00 | +3.7% |
| ≥$10.00 − <$100.00 | +5.7% |

**Most results are not statistically significant see the description below*

While this approach seems less damning of tokens <$0.01, there was no statistical significance to this price bucket’s performance. Some buckets did have statistically significant results:

- ≥$0.10 − <$1.00 is statistically significantly underrepresented (*p*=0.012) in Top 100 projects
- ≥$10.00 − <$100.00 is statistically significantly overrepresented (*p*=0.013) in Top 100 projects
- ≥$100.00 is statistically significantly overrepresented (*p*=0.032) in Top 100 projects

<aside>
💡 While both approaches have their limitations and flaws, both suggest there is **some** evidence for a psychological investor bias that benefits tokens in the price range of $10.00 up to $100.00, and that there may be a bias harming tokens with a price below $0.01. While the expected benefits are minor, builders can select a max supply in order to target this range of price per token (1mm to 10mm for most projects).

</aside>

## Emissions Rate

Now that you’ve made data driven decisions on whether to have a max supply or not, and if so what that max supply will be, it’s time to think about your emissions.

Analysis of the Top 1,000 tokens by market cap each month for the past 5 years, excluding stablecoins and wrapped assets, shows the relationship between each token’s latest 1 month, 3 month, and 6 month changes in circulating supply and the latest month’s excess returns above/below the performance of the market.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/527e04dc-2825-49ff-a248-8f46c8c189ea/Untitled.png)

Most builders might be surprised to find there is virtually no consistent relationship between token emissions rates and monthly excess returns.

<aside>
💡 This does not mean that inflation does not matter at all - for example when LUNA underwent hyperinflation due to the meltdown of UST, the price was immediately and heavily impacted. Hyperinflation still matters, but overall supply changes are nowhere near as impactful as many builders believe.

</aside>

Even when we slice the data in the below additional ways, the explanation power (coefficient of determination) of recent inflation rates on monthly excess returns never exceeds about 0.05:

- Only uncapped supply tokens
- Only capped supply tokens
- Capped supply tokens with circulating supply of:
    - 0% to 20% max supply
    - 20% to 40% max supply
    - 40% to 60% max supply
    - 60% to 80% max supply
    - 80% to 100% max supply
- All of the above but only the window of annualized inflation rates of >0% to 100%
- All of the above on the Top 100 tokens each month instead of the Top 1,000

Inflation does not become a meaningful predictor in any of these cases. Here is a relatively cherry-picked slice of uncapped tokens with greater than zero-emission rates, but less than an annualized 100% emission rate.

While the slope is negative, the significance of the impact is effectively zero.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d3fa1efa-1558-4f4f-a32b-00cfd33bf9a5/Untitled.png)

These findings are corroborated by a [separate analysis of 5,000 token unlock events by 6th Man Ventures](https://6thman.ventures/writing/we-analyzed-5000-token-unlocks-this-is-what-we-found/). Rather than monthly price changes, this analysis focused on shorter-term price changes, ranging from 3 to 15 days around the unlock event.

In this analysis, the coefficient of determination of various different slices of the data never exceeded 0.06, meaning that only 6% of even short-term price movements are explained by specific token unlock events that increase supply. (Note there is a [bug in their original report](https://github.com/6th-Man-Ventures/token-vesting/pull/1) resulting in reporting Pearson’s correlation coefficient values as if they were coefficient of determination values - in other words, each `r^2` in the report is actually `r`.)

Hyperinflation will still kill your momentum and credibility, but even after controlling for overall market fluctuations, actual rates of supply change only explain a tiny fraction of price performance on a month-to-month or shorter time frame. Your token is much more impacted by other aspects: utility, incentive mechanisms, supply sinks, use cases, value accrual, etc.

### Improving on Linear Emissions

So what are builders to do then when it comes to their emission curve? While the data itself does not have much definitive to say, we can at least draw some logical inference about how to optimize emissions curves beyond the vanilla linear emissions schedule.

In particular “S”-shaped curves as in the picture below (sigmoid curve), arguably make for better emissions schedules than linear schedules.

![Cumulative linear emissions curve over 5 years compared to an optimized sigmoid curve.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ce83ea96-3f90-4bd9-b3ea-ef4aa88d5439/Linear_vs_Sigmoid_Cumulative_Emissions.png)

Cumulative linear emissions curve over 5 years compared to an optimized sigmoid curve.

Inflation (dilution) rates are biased to be highest when a token first launches because the existing supply is at its lowest-ever levels. Most projects, including those that make use of linear emissions schedules, have their highest rates of inflation when they first launch, creating the optimal conditions for a price dump, and turning the project into a pump-and-dump.

![Monthly annualized rates of inflation for a linear emissions curve over 5 years compared to an optimized sigmoid curve.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/96498614-8dbd-423f-8db4-ffb187871484/Linear_vs_Sigmoid_Annualized_Inflation_Rate.png)

Monthly annualized rates of inflation for a linear emissions curve over 5 years compared to an optimized sigmoid curve.

An optimized sigmoid curve reduces inflation when the project is most susceptible to pump-and-dumps, effectively smoothing the **rate** of inflation more evenly over the total schedule.

<aside>
💡 Whereas linear emissions smooth the **absolute amount** of tokens emitted over the total schedule, a sigmoid curve smooths the **inflation rate** at which tokens are emitted over the total schedule.

</aside>

Of course, a curve can’t emit fewer tokens than an equal-length linear curve without at some point also emitting more tokens than the linear curve.

That is indeed what is happening in the curve picture above, with the month-over-month emissions of tokens for the sigmoid curve exceeding the linear one from about Year 1 -  Year 3 out of the 5 year emissions schedule.

But not only is this likely an acceptable cost for getting the lower rates of inflation when the project first launches - it might also actually be itself another strength of sigmoid curve emissions.

6th Man Ventures’ analysis mentioned earlier found (weak) evidence to conclude that tokens with most of their supply already emitted (vested), experience less volatility and potentially outperform tokens that still have yet to emit the majority of tokens.

![Monthly emissions as a percent of total supply for a linear emissions curve over 5 years compared to an optimized sigmoid curve.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/05207248-5cb3-436c-8150-f9f707d274c7/Linear_vs_Sigmoid_Monthly_Pct_of_Cumulative_Emissions.png)

Monthly emissions as a percent of total supply for a linear emissions curve over 5 years compared to an optimized sigmoid curve.

A sigmoid curve allows for both reducing upfront inflation when a project first launches, but still reaching 50% cumulative emissions earlier than a linear curve.

For example, the sigmoid curve depicted in the above charts has drastically lower inflation when the project first launches, and yet reaches 50% cumulative emissions 6 months before linear, without drastically exceeding the monthly increase under a linear schedule.

Furthermore, the sigmoid curve’s inflation rate peaks right around the two-year mark - when most projects are either hitting their full stride and can tolerate (or even benefit from) moderately higher inflation, or have bigger problems than moderately higher inflation anyway.

https://twitter.com/verumcapital/status/1633456943728668674

Verum Capital found some weak evidence to support a “sweet spot” at 40%-60% of cumulative emissions (see thread above). If true, this would also suggest this sigmoid curve’s inflation rates peak during the period of cumulative emissions when the market is best suited to absorbing relatively higher emission rates.

### Improving on Time-Based Emissions

Most emissions, including the ones we’ve spoken about so far, are time-based emissions. Whether per block, per day, per week, or per month emissions occur as time passes.

This is fine enough when a protocol is growing, but when growth slows it means that dilution continues unabated, possibly when the protocol can least tolerate it.

An alternative is KPI or “productivity linked” emissions - emissions don’t occur as a function of time (although of course there is a realized rate of emissions per time) but as a function of performance.

The benefits of these emissions include:

- Better aligned the team, users, and investor incentives to grow the protocol
- Enables emissions that are **net nondilutive** per valuation metrics (e.x. the number of tokens per TVL does not increase as a function of emissions)
- Reduces dilution when likely most important to do so, during bear markets or natural slower periods of growth

The primary potential drawback is that if users are primarily driven by emissions, a slowdown in emissions when a slowdown in growth occurs can worsen the effects of the slowdown. Some ways to mitigate this downside include:

- Blending KPI emissions with time-based emission
- Governance votes that can approve temporary time-based emissions programs to kickstart or reignite adoption
- Designing a sound product and tokenomics in the first place, so that user demand is organic, not artificial usage motivated only by emissions

While KPI based emissions have yet to see common adoption, they have been explored [both in theory](https://deliverypdf.ssrn.com/delivery.php?ID=056112118000090002126101117010081122118082063037061028081121125073113004086006090066101022100000122017012004104109072122086122061072021040019082115122028070064074098060085038119101001009071071069082095107124094080110024089101004085070000120100000017013&EXT=pdf&INDEX=TRUE) and in practice in a few notable cases such as Filecoin, which blends time-based and network capacity KPI based FIL emissions.

[Clip Finance](https://twitter.com/ClipFinance), a soon-to-launch yield aggregator protocol ties their emissions to the protocol hitting TVL milestones, thus rewarding users for protocol growth, ensuring emissions are not net dilutive relative to fundamental adoption, aligning incentives for users and the team, and incentivizing all parties involved to participate in increasing adoption.

https://twitter.com/IdeaMikk/status/1682035795040043015?s=20

And more recently, [Outlier Ventures coined the phrase “Adoption Adjusted Vesting” (AAV)](https://outlierventures.io/article/adoption-adjusted-vesting/) to describe token issuance as a function of KPIs.

<aside>
💡 The data suggests optimizing emissions is not about minimizing inflation at all costs, as many builders assume, but about balancing supply and demand, creating and maintaining the right incentives, rewarding value-add user behavior, creating the appropriate distribution of holders, and stabilizing the protocol, which all depend on your specific use case. There is no such thing as “the best emissions curve”, though there are best practices and improvements over linear time-based models to consider.

</aside>

## Allocation

Data for allocations is much more sparse than for emissions, which makes it difficult to conduct analysis on the optimal allocations. That said, even if data was readily available, the portion of total tokens allocated to investors, team, advisors, etc would likely not be a reliable indicator of project success except for obviously egregious cases where the token crashed due to obvious misuse in allocation to the team and early insiders.

<aside>
💡 For a data-driven approach to allocation, we should look at what is typical for projects and generally best practice. The industry standard allocations below have been compiled from additional custom analysis and additional sources listed at the end of this chapter.

</aside>

Builders should be aware that are very few market standards for terminology, or for enforcing that tokens are [actually used in the manner they are earmarked](https://twitter.com/0xedenau/status/1642502145839890432?s=20). What one project might call “staking rewards” and list as a separate category, another project might lump into “community rewards” without any greater granularity.

Thus, these standards serve as a starting place to customize - though builders should generally have a good reason for material differences.

### Industry Standards

| Industry Standards | Vesting Length | Vesting Cliff | Vesting Delay | Vesting Type | Vesting Frequency |
| --- | --- | --- | --- | --- | --- |
| Team | 5+ years | N/A | 1-2 years | Sigmoid | Continuous |
| Advisors | 3+ years | N/A | 1 year | Sigmoid | Continuous |
| Investors | 2+ years | N/A | 1 year | Sigmoid | Continuous |
- **Team**
*Core team and project contributors*
Typical 15% ; Range 15% - 20%
- **Advisors**
*Advisors and partners*
Typical 5% ; Range 3% - 6%
- **Investors**
*Private investors, angels, and VCs*
Typical 15%; Range 10% - 20%
- **Treasury**
**Tokens generally held in a smart contract to be allocated at the discretion of the team and/or governance votes for development, partnerships, marketing, or other measures**
Typical 20%; Range 15 - 30%
- **Community Rewards**
**Staking, liquidity, or other rewards to the community, either according to an emissions schedule or ad-hoc at the discretion of the team and/or governance votes**
Typical 40%; Range 20% - 50%
- **Airdrop**
**Issued to users/testers, community members, and/or a competitor’s users (vampire attack)**
Typical 5%; Range 5% - 10%

![Modern industry-standard token allocations](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df08f10c-e2eb-42af-af02-52596da96ee9/allocation_piechart.png)

Modern industry-standard token allocations

## Vesting

Vesting is essentially a sub-set of emissions in general, but it is complex enough that it deserves its own discussion, especially since builders have to make decisions on things like cliff lengths and total vesting periods for tokens allocated to the team, investors, advisors - which generally represents a significant portion of the total supply.

### Current Norms

The below table describes what is currently the industry standard practice for vesting, though builders should note that in the case of vesting industry standards are not necessarily the same thing as best practices.

**Current Norms (Not Necessarily Best Practices)**

| Industry Standards | Vesting Length | Vesting Cliff | Vesting Delay | Vesting Type | Vesting Frequency |
| --- | --- | --- | --- | --- | --- |
| Team | 2-3+ years | 1 year | N/A | Linear | Monthly |
| Advisors | 1+ years | 0.5 - 1 year | N/A | Linear | Monthly |
| Investors | 1.5+ years | 0.5 - 1 year | N/A | Linear | Monthly |

Builders who wish to optimize their vesting should consider the below additional optimizations, which aim to minimize the negative impacts of vesting unlocks, better align incentives, and optimize vesting within the context of optimizing overall emissions.

### Additional Optimization

There are several detailed analyses of vesting data we can draw inferences from. Unfortunately, arguably the two most detailed reports contradict each other in some of their findings:

- “[The Optimal Token Vesting Schedule](https://lstephanian.mirror.xyz/Vdaepc7jyIHa3ma8Eg9C_IVIo1knVv9A36iYd6OD4Zg)” by Pantera Capital suggests:
    - Fewer, larger unlocks that are spaced out longer are better
    - 6-month cliffs are better than 1-year cliffs (shorter is better)
    - A short total vesting length is better than longer vesting
- Yet “[We Analyzed 5000 Token Unlocks – This is What We Found](https://6thman.ventures/writing/we-analyzed-5000-token-unlocks-this-is-what-we-found/)” by 6th Man Ventures suggests:
    - Smaller (<1% total supply), more frequent unlocks are better
    - Avoid cliffs, use a delayed start vesting instead of a cliff
    - Tokens with the majority of their total supply emitted/vested outperform tokens with the majority still unreleased

How are builders to reconcile these findings?

- First and foremost - keep in mind that neither report’s findings make any claims about being statistically significant - usually indicator findings are **not** significant. Explanatory power that is quantified in the reports is extremely weak - an entirely plausible reason the reports seem to contradict each other is that both are mostly random noise!
- Both reports suggest that tokens should aim to emit a cumulative majority of their total supply sooner rather than later. We discussed the benefits of doing this earlier, in the context of sigmoid emissions curves vs linear emission curves.
- The first report seems to give mixed signals around the size of unlocks - it mentions larger unlocks have less negative impact, but does not get into the data on this point, and separately makes the claims that shorter cliffs (smaller unlocks) perform better than longer cliffs (larger unlocks), and that gradual linear unlocks perform better than more discrete unlocks (which all else equal would be larger than continuous linear unlocks).
This inconsistency, combined with better-quantified results from other analyses, likely indicates that more continuous, smaller unlocks are more desirable. This would also be consistent with data from traditional finance and economics - sharp jumps in supply are likely undesirable, although an important exception to this may be KPI-based emissions/vesting as we previously discussed.
- Both reports seem to agree directionally at least that shorter cliffs are better. But builders should not mistake “shorter cliffs” for “short total vesting”. As the 6th Man Ventures report points out, vesting can simply start later - avoiding the lumpiness of a cliff in unlocks, while still maintaining a vesting period that aligns incentives.
A reasonably long vesting period is healthy when it aligns the incentives of the team with the token, and several industry professionals have made strong arguments and calls in support of materially longer standard vesting periods for the team of [7+ years](https://defivader.medium.com/token-vesting-period-proposal-f88cf9ebe833) or even as long as [10 years.](https://beincrypto.com/web3-founders-should-look-to-longer-vesting-schedules-binance-labs-ken-li-ethdenver/)

<aside>
💡 Summarizing quantitative analyses on vesting suggests several modifications to existing best practices. Evidence suggests these changes *may* contribute to less overall price volatility, and less negative short-term price action around token unlock events.

</aside>

**Best Practices (Optimized Vesting)**

| Industry Standards | Vesting Length | Vesting Cliff | Vesting Delay | Vesting Type | Vesting Frequency |
| --- | --- | --- | --- | --- | --- |
| Team | 5+ years | N/A | 1-2 years | Sigmoid | Continuous |
| Advisors | 3+ years | N/A | 1 year | Sigmoid | Continuous |
| Investors | 2+ years | N/A | 1 year | Sigmoid | Continuous |

## Airdrops

It’s generally known that indiscriminate airdrops are a relatively cheap but ineffective way of increasing the distribution of token holders.

https://twitter.com/jphackworth42/status/1575124337086156801?s=20

They can still have a place in supply policy and can be effective if well-targeted, but since it is relatively low-cost to run a Sybil attack and control multiple wallets in order to earn substantial airdrop rewards, abuse is to be expected.

If you’re launching an airdrop put yourself in the shoes of a malicious attacker and try to abuse your airdrop - similar to when designing your token incentives. How might you skirt what the distribution rules are attempting to reward? Approaching it from this angle will help maximize the airdrops’ lasting effects - though there is no way to eliminate abuse entirely.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec49390b-cf74-4a2b-8345-ff066cf9325d/Untitled.png)

One specific strategy to mitigate mercenary airdrop farming is to make airdrops a continual, multistep event, instead of a single one-distribution. While this does allow for filtering out recipients who immediately dumped the token so they do not receive additional rewards, it also effectively turns airdrops into a pseudo-staking rewards mechanism, where only wallets that have not sold continue to earn rewards.

This means that if not planned carefully, sequential airdrops can essentially just “kick the can down the road” and make the token dump by mercenary farmers even larger and all at once when airdrops rewards finally end or start to decline.

https://twitter.com/spencecoin/status/1532180927291346945?s=20

A similar end goal could be achieved via only airdropping tokens to wallets that agree to receive airdrops in the form of tokens that are locked for a period of time, say for one year. The challenge is that there is no opportunity cost with airdropped tokens - even if you only give airdrop eligibility to wallets that opt-in to receive rewards locked for one year, it’s still “free money”. From the perspective of the airdrop recipient, they still don’t lose or risk anything even if the token price declines during the year since the airdrop, because they wouldn’t have received **anything** if they had not opted into the “locked airdrop” in the first place.

The easiest and more direct way to impose an opportunity cost is to **sell** tokens instead of airdrop them - but this is not always feasible for regulatory reasons (speak to a lawyer) nor is it necessary as effective for awareness, marketing, and widespread token distribution.

https://twitter.com/ljin18/status/1625881752815259653?s=20

Creative solutions could be tiers of airdrops - recipients opt into various durations and all airdropped tokens are distributed as locked tokens, with those who opt for a longer time frame earning more tokens.

When possible, increasing Sybil resistance by increasing the cost of a Sybil attack could also be effective. Depending on your use case, requiring recipients to link a paid Twitter account or something similar would drastically increase the cost and difficulty to conduct a widespread Sybil attack. While this approach is not a good fit for privacy-heavy use cases, it could work for use cases such as Web3 games where users already connect social accounts, emails, Discords, or other offchain sources of identity.

Another option that would preserve privacy and instill an opportunity cost to airdrops could be to partner with an existing token, such as a project building in the same ecosystem, and require airdrop recipients to lock up that project’s token to be eligible for your airdrop. This imposes an opportunity cost, reducing the potential for abuse, while also allowing to leverage an existing community for awareness - one of the primary goals for an airdrop. The same strategy could even be deployed in a more adversarial “vampire attack” approach - require wallets that are already existing users of a competitor to lock up that competitor’s token in your smart contract in order to be eligible for your airdrop. Maybe the contract even sells or burns those competitor tokens if recipients dump their airdrop rewards within a certain amount of time from receiving your token. Whether cooperative or adversarial, this strategy may have legal or regulatory implications, and this is not legal advice. Always speak to a lawyer before marketing, selling, or distributing your token.

<aside>
💡 Builders should ensure they have realistic expectations for their airdrop - data from comps suggest that the majority of tokens are dumped within short order. If you’re including an airdrop, this makes other aspects of your supply policy we’ve discussed, like ensuring sufficient liquidity incentives and balancing early emissions rates, all the more important.

</aside>

## Token Sinks

Token sinks is a term for any mechanism, feature, or use case that reduces the [velocity](https://en.wikipedia.org/wiki/Velocity_of_money) of a token - you can them of them as “absorbing” token supply, like a sink filling up with water.

Some popular examples of sinks include:

- Bitcoin: the expectation of store of value against an inflating Fiat money supply serves as a social/psychological sink for BTC, as holders are happy not spending, using, or selling their coins (thus reducing velocity)
- Ethereum: staking to run a validator serves as a sink for ETH
- Chainlink: requiring oracles to post collateral that can be slashed both serves as a means to incentivize honest oracles, and as a sink for LINK tokens
- Filecoin: posting collateral in order to provide storage space and to take on deals, as well as token rewards being locked up for newer providers, creates a sink for FIL
- Curve: staking tokens as ‘veCRV’ form in order to direct rewards to different liquidity pools and earn protocol revenue distributions is a sink for CRV
- GMX: escrowed ‘esGMX’ staking rewards (rewards that must be gradually unlocked by pairing with GMX tokens), creates a sink for GMX tokens

In particular, Curve’s “vote escrow” staking model and GMX’s escrowed rewards are two of the most popular, and often imitated, token sink mechanics in recent years. See [Chapter 1.6](https://www.notion.so/1-6-A-Must-Know-History-of-Tokenomics-562de02145a64a9aa529425db7b3339d?pvs=21) for a brief discussion of each.

Not all sinks are necessarily healthy or sustainable - adding sinks to an otherwise useless token only delays the inevitable crash, it does not add any value to the token itself. For example, adding staking rewards to a token that does absolutely nothing does create a sink for the token, but it doesn’t create any new demand, utility, use case, or value for the token itself. All it does is **temporarily** reduce velocity and circulating supply. This is why…

<aside>
💡 Contrary to how it’s usually presented in white papers, staking is not a use case or token utility - it’s a **supply** mechanism.

The obvious exceptions are staking that performs a role, such as in Proof-of-Stake consensus, or staking that insures or collateralizes a protocol as a last measure in emergencies.

</aside>

It’s important to remember that even the strongest sinks only *temporarily* reduce velocity and circulating supply. In fact, what behaves like a sink in the short term can often lead to completely opposite outcomes in the long run.

https://twitter.com/VaderResearch/status/1512736643094093824?s=20

For example, OHM’s ponzinomic (3,3) token sink, which encouraged existing holders to not sell by paying them a yield directly funded by incoming investments was never sustainable and required ever-increasing capital inflows to maintain.

<aside>
💡 A general rule of thumb about healthy sinks vs ponzi sinks is that if the sink rewards holders with a greater share of revenues/value created by the product, the sink is generally healthy. But if the sink pays a yield to holders directly funded by new money flowing into the sink, the sink is almost always an unhealthy, unsustainable ponzi that will collapse the moment growth slows down.

</aside>

This is why token sinks alone are not sufficient. They can serve useful to improving security (e.x. collateral), aligning incentives (e.x. stake to earn protocol revenues), and achieving other legitimate benefits, but token sinks can not, and do not, replace the need for **demand** for the token, which comes from use cases and utility, not from locking up supply in a sink.

(Technically the one exception to this is if the token itself is a form of money, but as discussed in [Chapter 1.5](https://www.notion.so/1-5-Types-of-Tokens-1e1f4f7120144ec4a83baa1dee9b3e7e?pvs=21), this is almost always a mistake for builders to attempt).

While models like Curve’s “vote escrow” sink are popular, there is no “correct” or “best” sink.

Builders should consider a wide range of sinks used by comps, as well as consider designs for new innovations, and find what is best suited to their use case.

When it comes to sinks, real-world on-chain data from comps is a builders’ best friend, especially as we get into the next step of the design process: modeling and optimization. Builders should use comps not just for inspiration, but to validate what a realistic impact a token sink is expected to be.

For example, one of the most successful token sinks of all time is Curve’s veCRV - entire protocols (Convex) have been built on the premise of locking CRV tokens in this sink and tokenizing that share (in essence a type of liquid staking derivatives).

Yet even then, CRV has [around 40% of total issued CRV staked](https://classic.curve.fi/usecrv). If your designs or modeling assume that when you add a vote escrow mechanism it will absorb more than 40% of the total supply - you’re likely going to have some rude surprises when you launch.

As we’ll see next chapter, no one can predict the future, but that doesn’t mean you should blindly stumble ahead without validating assumptions and managing risks.

# Additional Resources

- Blog, [We Analyzed 5000 Token Unlocks – This is What We Found](https://6thman.ventures/writing/we-analyzed-5000-token-unlocks-this-is-what-we-found/)
- Blog, [Optimizing Your Token Distribution](https://lstephanian.mirror.xyz/kB9Jz_5joqbY0ePO8rU1NNDKhiqvzU6OWyYsbSA-Kcc)
- Blog, [The Optimal Token Vesting Schedule](https://lstephanian.mirror.xyz/Vdaepc7jyIHa3ma8Eg9C_IVIo1knVv9A36iYd6OD4Zg)
- Blog, [Token Vesting and Allocations Industry Benchmarks](https://www.liquifi.finance/post/token-vesting-and-allocation-benchmarks)
- Dashboard, [Moonfire Tokenomics Explorer](https://tokenomics.moonfire.com/)
- Dashboard, [Uniswap Post-Airdrop Analysis](https://dune.com/jhackworth/uniswap-airdroppers)
- Paper, [The Three Tokenomics Problems and a Productivity-Linked Tokenomics Design](https://deliverypdf.ssrn.com/delivery.php?ID=056112118000090002126101117010081122118082063037061028081121125073113004086006090066101022100000122017012004104109072122086122061072021040019082115122028070064074098060085038119101001009071071069082095107124094080110024089101004085070000120100000017013&EXT=pdf&INDEX=TRUE)
- Blog, [Adoption Adjusted Vesting](https://outlierventures.io/article/adoption-adjusted-vesting/)
- Blog, [Why Web3 Founders Should Focus On Longer Vesting Schedules](https://beincrypto.com/web3-founders-should-look-to-longer-vesting-schedules-binance-labs-ken-li-ethdenver/)
- Blog, [Token Vesting Period Proposal](https://defivader.medium.com/token-vesting-period-proposal-f88cf9ebe833)
- Blog, [The Comprehensive Guide to Token Compensation](https://www.liquifi.finance/post/the-comprehensive-guide-to-token-compensation)
- Blog, [On Tokenomics Series Part I - The Game of Supply and Demand: The Supply](https://threesigma.xyz/blog/on-tokenomics-supply-and-demand-part1)
- Blog, [On Tokenomics Series Part II - The Game of Supply and Demand: The Demand](https://threesigma.xyz/blog/on-tokenomics-supply-and-demand-part-ii)

# Primary Tool: Tokenomics Modeling Template

<aside>
💡 Complete “Step 5: Supply Policy” of the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)** by filling out the “Supply (Allocation & Emissions)” tab of the [**Tokenomics Modeling Template**](https://docs.google.com/spreadsheets/d/13uc39fMqLb1RKvcGk9s_whwZXgkftfaFLcgPkJpG9YI/edit?usp=sharing). You can save an editable copy of the template by clicking **File > Make a Copy**.

The template is **pre-populated with best practices for optimized allocations, emissions, and vesting periods** based on multiple quantitative analyses described in full in the corresponding chapter of the Tokenomics for Builders guide.

As you fill out the spreadsheet, the charts on the “Supply Charts” tab will update automatically. Additionally, you can use the “Curve Calculator” tab to quickly compare the effect of different parameters for non-linear (sigmoid) curves.

https://docs.google.com/spreadsheets/d/13uc39fMqLb1RKvcGk9s_whwZXgkftfaFLcgPkJpG9YI/edit?usp=sharing

</aside>

# Video Tutorial

# 2.6 Modeling & Optimization

# Introduction

Why is modeling useful?

The most common answer you’ll hear is: “Modeling is useful for predicting token price.”

Wrong. Wrong on two fronts.

https://twitter.com/MehdiFarooq2/status/1673968770048720896?s=20

First, modeling goes well beyond prices. The design choices you make as a builder can, and should, be tested ahead of time in simulations and scenario analysis modeling.

Modeling can be used to make informed decisions about emission rates, system architecture, parameter settings, risk controls, balanced incentives, and much, much more:

- What should the parameters for Maker DAO’s collateral pools be to maximize DAI adoption?
- How should liquidity be distributed along the curve in Curve’s stablecoin pool?
- How many ETH should be required as collateral to run a node in proof-of-stake Ethereum?
- Will increasing or decreasing emissions lead to more organic product usage for Looksrare?
- What is the most effective feedback mechanism architecture for RAI to maintain a stable price?
- What is the ideal fee for Uniswap to adopt if they turn on the ‘fee-switch’?
- What rate of redemptions can UST/LUNA handle before becoming unstable, and how likely is this to occur based on observed variances in redemptions?
- What degree of risk is Mango Markets exposed to by allowing traders to use positions as collateral for leverage, and how can these risks best be mitigated?
- How often can storage providers be required to create zero-knowledge proofs while still remaining profitable, and what are the implications for required token incentives?
- How many new miners would be expected to secure the chain if block rewards are changed?
- Under what market and network conditions would an attack on the protocol be profitable, and how can the protocol minimize its probability of occurrence?

To answer all these questions in a data-driven way requires modeling.

Optimizing your protocol requires modeling - and that can lead to a higher token price. But predicting a token price, on its own, will not do anything to optimize your protocol.

The second reason “Modeling is useful for predicting token price” is wrong, is that it assumes modeling is useful for predicting the future.

This belief about modeling is a telltale sign of an amateur builder. Acting on this misled belief, these builders either think they can predict the future, and thus put blind confidence in an overly simplistic model, or they think predicting the future is impossible, so they don’t do any modeling at all.

<aside>
💡 What beginners fail to understand, is that modeling is not useful for **predicting outcomes**, it’s useful for **analyzing risks.** In other words, modeling is not about understanding what **will** happen, it’s about understanding what **can** happen and the **relative probabilities** of various outcomes.

</aside>

In other words, modeling is not about understanding what **will** happen, it’s about understanding what **can** happen and the **relative probabilities** of different outcomes.

Modeling allows designers to quantify risks, identify key assumptions, and optimize system design to strike the best risk-to-reward balance for their use case and avoid catastrophic events before they happen.

## Example: Mango Markets

A simple example from crypto is the $114 million Mango Markets exploit. This was not a hack - it was an *economic exploit* only possible due to a lack of risk controls which could have been easily flagged by modeling.

Put simply, the exploiter intentionally manipulated the oracle price of an illiquid asset in order to borrow against its inflated value and then default on the loan. As a result, the protocol was left with bad debt, drained of users’ deposited collateral.

![Source: [Coindesk](https://www.coindesk.com/tech/2022/10/20/defi-exchange-mangos-114m-exploit-was-market-manipulation-not-a-hack-ex-fbi-special-agent-says/)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/07c06d77-a268-41af-a0f8-34578cdd99eb/Untitled.png)

Source: [Coindesk](https://www.coindesk.com/tech/2022/10/20/defi-exchange-mangos-114m-exploit-was-market-manipulation-not-a-hack-ex-fbi-special-agent-says/)

It would be impossible to **predict** that in the future that particular asset would hit an inflated price and cause the protocol to go bankrupt - but that’s not the point of modeling.

The point of modeling is to run scenario analyses to check what **can** happen.

For example, random walks with sufficient volatility, or even simple boundary analysis - setting prices to suddenly move to approach infinity, or approach zero, would demonstrate that short term, temporary spikes in prices allow for borrowing dangerously high amounts against open positions.

Modeling shows abuse **can** happen. It does not predict when, where, or the exact specifics of how it **will** happen.

While Mango Markets is a good example on the importance of modeling, it can be difficult to grasp the underlying concepts when we just look at a high-level example.

So let's use another simple example to actually quantify the specifics.

## Example: Betting Optimization

It’s the World Cup finals. Oddsmakers are putting a 1.25-to-1 payout on Argentina to win the match - we’ll assume bets are inclusive of all overtime and penalties, so there’s no such thing as a draw.

In other words, a $1.00 bet on Argentina would return $1.25 gross ($0.25 net profit) if Argentina wins, and $1.00 net loss if Argentina loses.

Imagine your friend is an expert statistician, and let’s assume for sake of example he knows the “true odds” - he says the true odds favor Argentina to win.

Assuming you trust your friend, should you bet on Argentina?

A beginner might say yes. But the real answer is it depends.

In our example, betting on Argentina has a $1.00 loss if they actually lose, but only a net $0.25 profit if they do indeed win. The oddsmakers are effectively saying Argentina has an 80% chance of wining the game (thus implying a 20% chance for France to win, implying a 5-to-1 payout).

Imagine the **true odds**, which your friend knows, are that Argentina has a 60% chance of winning the game. In this case, you actually shouldn’t bet on them.

To be clear, 60% if still a majority - a beginner would be correct that Argentina is **expected to win the game on average**, but the expert knows that is not what matters. Even though Argentina is “predicted” to win the game, betting on them is the wrong bet.

The beginner bets on Argentina because ”Argentina is expected to win”

- 60% chance of a $0.25 net profit
- 40% chance of a $1.00 net loss
- Expected profit: -$0.25 (-25%)

The professional bets on France because “it optimizes the betting system based on risks”

- 40% chance of a $4.00 net profit
- 60% chance of a $1.00 net loss
- Expected profit: $1.00 (100%)

In the long-run, the professional makes a profit, while the beginner will eventually lose all their money. But for a given bet, sometimes the beginner will win and the professional will lose due to randomness (risk) - that’s life.

No one can predict the future and no one can design a system with zero risks. Nevertheless, your job as a builder is to use modeling to understand and quantify these risks, in order to optimize your approach, and not end up like the beginner in our example.

<aside>
💡 Optimizing complex systems isn’t about predicting what will happen or is most likely to happen, it’s about understanding the **relative probabilities** of a full spectrum of outcomes, and the **relative costs and benefits** of those outcomes, in order to be able assess how design choices minimize risks or maximize chances for a given outcome.

</aside>

# Modeling Approaches

A deep dive into modeling techniques is beyond the scope of this guide - entire books have been written on each subtopic of this chapter alone.

But builders should be familiar with the general concepts so they can ensure they work with the right tools, team members, and/or advisors to do the degree of risk management appropriate for their use case.

Builders which don’t do any kind of risk analysis are essentially blindly guessing that their design will work exactly as planned in every possible future and that there are no hard-to-anticipate risks lingering in the system.

As we’ve time and time again, that’s not a very wise approach.

## Deterministic

When most people think of modeling, their first thought is spreadsheets.

Excel. Google Sheets. Rows. Cells. Formulas. That’s modeling, right?

That’s *one kind* of modeling, but that’s not all there is to it.

This kind of modeling is very useful, especially for quick drafts, simple thought exercises, less complex systems, one subcomponent of a larger system, systems with less randomness or uncontrollable variables, less mission-critical use cases, and for creating interactive calculators that are more friendly for non-technical team members and users.

You can do very powerful things with spreadsheets, such as replicate a model of ETH 2.0’s economics (we’ll see multiple versions of such a model later this chapter). This could be appropriate for high level scenario analysis for ETH’s rates of issuance, burn, net inflation to optimize network configurations for validator incentives.

But a spreadsheet would likely not be well suited for a simulation of Ethereum’s consensus mechanism itself, where subtle actions by individual validators, and complex interactions between them, create outcomes that are highly contextually dependent and nuanced.

These kind of models are less useful when it requires analyzing systems with multiple moving pieces that recursively influence each other, or analyzing the relative probabilities of a large or open ended range of possibilities.

For instance, if you’re designing a system like Maker’s CDP vaults, the risk of the protocol becoming undercollateralized depends on:

- How much debt users have minted (borrowed) in their vaults
- Which collateral assets users have deposited into vaults
- How much and how quickly do the collateral assets fall in price
- How correlated are the price moves in all these different collateral assets are
- How much additional collateral do users deposit and how quickly do they do so
- How much debt users payback and how quickly they do so
- How quickly vaults can be liquidated and at what costs and slippage
- The system parameters for liquidation ratio and liquidation penalty

As you can see, things quickly get complex.

Does this mean it’s **impossible** or **useless** to model CDP vaults?

No - in fact it means the exact opposite. The more complex a system the harder it is for a human designer to know how their design will function in various situations and conditions. 

<aside>
💡 The more complex a system, the more important modeling becomes.

</aside>

It just means that spreadsheet modeling is likely not the best approach in this case. One reason for this so many relevant factors are not in the designers’s (or anyone’s) control. For example, price changes of collateral assets are a random process that no one can directly control or reliably predict.

This brings us to our dilemma. Quantifying the risks to the protocol is a necessary step to optimize its design and parameters. Yet to do so, we need to account for complex simulations of inherent randomness that will influence the system.

A simple spreadsheet with one field for each of these factors, for example a cell for “how much did collateral assets fall”, clearly **can not** achieve this - it does not represent any randomness or path dependency over time.

> In mathematics, computer science and physics, a **deterministic** system is a system in which no randomness is involved in the development of future states of the system. A deterministic model will thus always produce the same output from a given starting condition or initial state.
**Source: [Wikipedia](https://en.wikipedia.org/wiki/Deterministic_system)
> 

We can change the inputs to the cells, but each time we use the same inputs and “run” the model, we get the same output - it is a deterministic model.

Deterministic models are very powerful tools - but they are generally not the right tool for conducting robust risk analysis.

## Stochastic

This brings us to stochastic modeling.

> "Stochastic" means being or having a random variable. A **stochastic** model is a tool for estimating probability distributions of potential outcomes by allowing for random variation in one or more inputs over time. The random variation is usually based on fluctuations observed in historical data for a selected period using standard time-series techniques. Distributions of potential outcomes are derived from a large number of simulations (stochastic projections) which reflect the random variation in the input(s). Its application initially started in physics. It is now being applied in engineering, life sciences, social sciences, and finance.
Source: [Wikipedia](https://en.wikipedia.org/wiki/Stochastic_modelling_(insurance))
> 

A common method used in stochastic modeling is Monte Carlo simulations. In simple terms, Monte Carlo simulations generate simulated paths of how a variable like asset price, product usage, network growth, interest rates, or system load will play out over time.

To ensure even unlikely events are included, tens of thousands of simulations (or more) are generated. You can think of each of these paths as a potential universe that **may** or **may not** play out in the future. The point is not to predict which universe will occur, or what will actually happen, but to quantify the relative probabilities of different outcomes, and be able to assess what would happen to your system at each step along these thousands of possible futures.

<aside>
💡 For example, imagine there’s a 50% chance a coin lands on heads or tails, and you will go bankrupt if the coin lands on 10 tails in a row. A Monte Carlo simulation isn’t needed for this simple case, but you could use one to understand and quantify your risk.

While this example may seem trivial, replace the “coin” with “UST”, and replace “if 10 tails in a row you go bankrupt” with “if 10% price drop or more the protocol collapses”, and you can begin to see why Monte Carlo simulations are so useful.

</aside>

Stochastic modeling allows builders to identify unlikely but catastrophic systemic risks ahead of time, and to accordingly optimize their systems in an empirical way.

This is exactly why it’s a giant red flag when builders don’t have any modeling **before** launching their token, or perhaps worse, when they publish “[dangerously oversimplified](https://youtu.be/lL13Puz-oSE?t=512)” analyses that do not reflect the randomness, path dependency, and emergent characteristics of a repeatedly run complex system.

## Agent Based

Most models, both stochastic and deterministic, are conducted in an “aggregated” manner. For instance, in the Maker CDP model, we could look at the **average** or **total** vault collateral. The **average** or **total** amount of outstanding DAI liabilities.

Many times this is perfectly acceptable. For instance if we care about **in aggregate** does the Maker protocol become undercollateralized, then total collateral and total liabilities is ultimately what matters. It doesn’t really what what happens to one specific user because even if their vault is undercollateralized, as long as other vaults have sufficient net collateral balances to cover the discrepancy, those vaults can be liquidated.

But some granularity is inherently lost in this approach. Just because an average user has a certain collateralization ratio doesn’t mean every user does. Some users will inherently have more risk, and get liquidated before the average user does, and this could trigger other users next in line to get liquidated early in order to cover any collateralization shortfalls.

That user experience of getting liquidated early to protect the protocol doesn’t matter for the health of the protocol in that moment - but it likely would matter to those users in question and potentially influence their future individual behavior.

<aside>
💡 Agent based models attempt to capture these individual aspects by modeling each unique agent (user) in the system, and analyzing the results to the overall system that occur, as well as observing and discovering individual user behaviors that the designers may not have anticipated.

</aside>

Agent based modeling can be either deterministic, stochastic, or a combination of both.

For example, imagine a simple two-agent simulation of “rock, paper, scissors”. A deterministic approach would be to hardcode each agent’s behavior such as “always play what your opponent played last round”. No matter how many times the model is run, the exact same series of events will play out.

A stochastic approach would be to involved elements of randomness in the gameplay, such as setting one agent to “pick a random choice every round”, or even have one or more agent’s behavior driven by a [Deep Reinforcement Learning](https://www.tensorflow.org/agents/tutorials/0_intro_rl) algorithm - essentially a type of AI that would learn to play the game better and better and make its own optimal decisions.

What does this simple example have to do with crypto? Replace “rock, paper, scissors” with “stake, hodl, sell”, or “tell-the-truth, lie, abstain” for block validation.

## Pros and Cons

Each of the three approaches we’ve discussed has its relative strengths and weaknesses.

**Pros and Cons of each Modeling Approach**

| Approach | Pros | Cons |
| --- | --- | --- |
| Deterministic | Simple to implement and interpret, fast to run | Does not account for uncertainty, randomness, or recursive interactions |
| Stochastic | Provides distribution of scenarios rather than single estimate, incorporates uncertainty, can capture complex interactions | More difficult to implement and interpret, computationally expensive |
| Agent Based | Can capture emergent system properties and user behaviors, can handle highly complex cases | Most difficult to design, implement, and interpret, very computationally expensive, highly domain specific and  |

Which approach makes sense for your use case depends on the granularity level of analysis you need, and the degree of risk management you need - for example, an L1 consensus mechanism or protocol with collateral need to be extremely confident about its risk management, whereas a clone of Uniswap v2 does not need to be as extreme.

That said, there isn’t necessarily only one way of doing things - any of the approaches can be applied to any use case, just be aware that in some cases a certain approach might not be rigorous enough, where another approach would be overkill.

**Examples of Each Modeling Approach in Various Use Cases**

| Use Case | Deterministic | Stochastic | Agent Based |
| --- | --- | --- | --- |
| Leverage Trading DEX: Evaluate protocol collateral risk | Boundary analysis of prices approaching zero and infinity, scenario analysis or historical market crashes | Random walks of price changes, simulate aggregate net trader positions to quantify tail risks | Individual trader agents place trades according to their individual risk tolerance parameters, are liquidated one-by-one, can be trained (RL) to maximize profit in order to discover profitable exploits of the system |
| NFT Marketplace: Optimize emissions to minimize wash trading, and maximize organic trading | Analyze historical data to evaluate potential responses to emission changes, | Simulate a range of possible trader behaviors under different emission levels, use the distribution of outcomes to maximize risk-reward | Individual trader agents act according to their own utility functions, simulate complex marketplace dynamics created by their interactions |
| Proof of Stake Layer 1: Evaluate security of the consensus mechanism | High level analysis of expected value payoffs for honest and malicious strategies under conditions that fit general assumptions | Simulate random participant behavior and network conditions and asses the distribution of security metrics under those conditions | Individual validator agents act according to provided profile type, assess network security as higher percentages of agents are assigned “malicious” type, use RL to discover adaptive attacker strategies |

These are of course not the only use cases that are applicable to each of these approaches, but this should give you a good idea of the kinds of things you can use each approach to do.

# Modeling Best Practices

Modeling can be intimidating for many builders. Try to stick to these best practices, and you’ll have a massive head start when it comes to validating and optimizing your product.

## Treat Modeling as an Optimization Function

An optimization function seeks to minimize or maximize a specific variable or measure. Too many builders dive into modeling without really understanding what it is they are even trying to accomplish.

Remember that you’re not trying to predict the future, but generally you are trying to minimize some kind of risk, maximize adoption, or optimize for some “sweet spot” in various factors (i.e. most adoption per unit of risk).

<aside>
💡 There is no such thing as **“the **best approach” or “the best tokenomics” for every situation. Every design decision is a tradeoff, and the right design for your context depends on **what** you are optimizing, maximizing, or minimizing.

</aside>

In order to approach modeling in a productive way, go back to the “**Incentives Mechanisms**” sheet you completed in the **[Tokenomics Design Canvas**.](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21) What open questions remain? What assumptions need to be tested and validated?

The “**Economic Security Framework**” framework (which you’ll be asked to complete at the end of this chapter) helps to further specify which parameters you need to optimize or risks you need to minimize.

Once you have the specifics or what to actually measure and optimize for in mind - now go and model them.

## Use Real World Data

No matter which approaches to modeling you’re taking, deterministic, stochastic, or agent based, all of them can benefit from basing your inputs and assumptions in real world data.

https://twitter.com/mrjasonchoi/status/1550463304513925120?s=20&t=v2T1RQCDQdcOxn-2D5iMKw

Your deterministic models’ inputs should be realistic based on those of comparable projects.

Your stochastic models’ degree of randomness and volatility should be realistic based on the fluctuations in data for comparable projects.

Your agent based models’ agent behaviors and motivations should be realistic based on the behaviors of users of comparable projects, and the proportion of different user types such as speculative mercenary capital vs organic users vs bull market users vs bear market users, etc.

Your models will almost always be more useful when incorporating real world data wherever possible. But this doesn’t mean you should run analysis that only considers “normal” real world situations, which brings us to…

## Conduct Scenario and Boundary Analysis

While real world data is useful, certain risks, such as tail risks (black swan events), do not always show up in historical data because they happen so infrequently.

You can and should incorporate real world data as much as possible - but you should always run analysis that is more conservative, and considers real world data from specific scenarios.

For example, you may run your stochastic model assuming a volatility rate observed during a bear market, compared to a flat market, compared to a bull market. You may even further exaggerate the parameters to be worse than the worst bear market even seen to date.

You should also feed in “artificial” boundary data - essentially asking: “What would happen if this parameter/input approached its highest or lowest possible value?”

This type of boundary analysis is simple but effective for detecting risks that have gone overlooked because the situations necessary for them to appear happen very rarely.

The results will describe situations that are very unlikely to occur, but which **can** occur, which is the entire benefit of modeling in the first place. You get a chance to fix and optimize things before they matter because once live, it’s only a matter of time until a rare event inevitably occurs - you don’t want the entire product to collapse when it does due to an oversight.

## Find Unvalidated Assumptions

If you’re making use of an oracle - how do you know that oracle is correct? Does your system assume the oracle is right 100% of the time?

What happens if you model out a scenario where the oracle has a bug and is wrong? Do you have risk controls in place? Does your product explode? Did your system inherently **assume** the oracle will never have a bug?

https://twitter.com/SBF_FTX/status/1580170218789253123?s=20

*Of all the people who could have a great thread on risk controls, it of course has to be SBF (trust me, I get the irony). I do not defend SBF in any way, but the above thread is a fantastic read.*

If you’re making use of collateral, how do you know that collateral is worth what you think it’s worth at any given moment in time? What happens if you model out a scenario where the collateral price has a flash crash or a sudden spike up before immediately crashing back down? Did your system inherently *assume* the market is never irrational, never illiquid, and never capable of being manipulated - even for a split second?

Lending markets like AAVE put themselves at considerable risk of bad debt due to overlending against CRV collateral, to the point where nearly 50% of the circulating supply of CRV was being used as collateral for various loans. AAVE was inherently assuming that the CRV collateral could be liquidated at current prices, but liquidating 50% of the circulating supply at once would easily break that assumption. While [AAVE v3 has risk controls about the maximum amount of collateral to accept in a given token](https://governance.aave.com/t/gauntlet-methodologies-borrow-and-supply-cap/11487), v2 does not - another example of invalidated assumptions putting the protocol at risk.

Subtle differences in how risk controls and parameters are calculated can make a large difference in the level of mitigation they provide. For example, a trailing **average** of collateral asset prices is likely a more reliable indicator of price than the spot price at any given period in time. But the **arithmetic mean** is more easily manipulated to the upside by a single outlier, whereas **[geometric means](https://www.investopedia.com/ask/answers/06/geometricmean.asp)** are less sensitive in this case (see the table below).

| Time | Raw Prices | 5min Arithmetic Mean | 5min Cumulative Geometric Mean | Arithmetic v.s. Geometric Difference |
| --- | --- | --- | --- | --- |
| 12:00 | $20.00 | - | - | - |
| 12:01 | $20.00 | - | - | - |
| 12:02 | $20.00 | - | - | - |
| 12:03 | $20.00 | - | - | - |
| 12:04 | $20.00 | $20.00 | $20.00 | 0.0% |
| 12:05 | $80.00 | $32.00 | $26.39 | 21.3% |
| 12:06 | $20.00 | $32.00 | $26.39 | 21.3% |
| 12:07 | $20.00 | $32.00 | $26.39 | 21.3% |
| 12:08 | $20.00 | $32.00 | $26.39 | 21.3% |
| 12:09 | $20.00 | $32.00 | $26.39 | 21.3% |
| 12:10 | $20.00 | $20.00 | $20.00 | 0.0% |

Both the **arithmetic mean** and the **geometric mean** are widely accepted forms of calculating an **average** of a series of numbers, such as trailing prices over the past N minutes, hours, or days, but which you choose can have a direct impact on how easy it is to manipulate the assumptions your model is built on. In the simple example above, a single temporary spike in price increases the trailing arithmetic mean by more than 20% than it increases the trailing geometric mean.

If this were prices of a collateral asset that users can borrow against, using the arithmetic mean makes it easier for attackers to manipulate collateral values higher, and then borrow more debt.

What’s the best way to find the subtle quirks in the parameters and risk controls you select? Modeling and simulations - both with real world data, and with boundary analysis and “sanity checks” (i.e. ‘what if the oracle temporarily glitches the number of decimal places and price jumps one-million times higher for ten minutes?’).

https://twitter.com/danrobinson/status/1455237045568348163?s=20

## Iterate, Don’t be A Perfectionist

By definition, all models are imperfect approximations of more complex systems. Models do not need to be **perfect** in order to be *useful.* It’s easy to say something can’t be perfectly modeled - but that isn’t a reason to not model it.

> “All models are wrong, but some are useful.”
- George E. P. Box
> 

This is particularly true for your first draft. In general, a sound approach to modeling is to:

1. Start with a simple deterministic model (based on real-world data) to identify which assumptions and parameters need to be tested with a greater degree of granularity.
2. Iterate on the model, and advance to a stochastic model as necessary.
3. Recognize that optimization is a continual process - for protocols run by decentralized governance, it continues even after launch. There’s no such thing as perfect - even Bitcoin and Ethereum make tradeoffs.

# A Note on Valuation Models

As we’ve seen in this chapter, modeling is **not** about forecasting price - it’s about risk management.

In order to launch their product, builders often have to raise money though, which may mean pitching angels, VCs, or other investors - and investors generally want to see projections.

Institutional investors like VCs know the standard “5-year charts” in pitch decks almost never play out - because they’re not reliable predictions. In fact, they’re really just one outcome cherry-picked from a scenario analysis.

So why do investors ask for them?

Because it shows you’ve done the work, that you know who your competitors are, what inputs into the business model matter, what drives value, and how to capture and accrue that value.

At the (frequent) request of builders, here is a short overview of various approaches to token valuation.

## MV = PQ

This approach is borrowed from classic economics, and assumes that your token essentially serves as the monetary supply within your product’s “economy”.

While once a popular approach, it has generally fallen out of favor due to valid critiques of its methodology, and the fact that empirically it does not tend to hold true. When you [observe realized token velocity](https://dune.com/queries/2059936) and solve for an expected price, the market price is often several orders of magnitude different than what it “should” be if the market were valuing the token based on `MV=PQ`.

For an example of this approach, see [Cryptoasset Valuations by Chris Burniske](https://medium.com/@cburniske/cryptoasset-valuations-ac83479ffca7).

For further critique, see [MV=P…Que? Love and Circularity in the Time of Crypto](https://medium.com/@AustereCapital/mv-p-que-love-and-circularity-in-the-time-of-crypto-1626c8ac297f).

## Discounted Cash Flows

In traditional finance, a common valuation approach for investments is to analyze future cash flows (scenario analysis) and then [discount the future cash flows](https://www.investopedia.com/terms/d/dcf.asp) to a lump sum present value.

This too, is not generally a very practical approach for tokens, where future cash flows may not even exist (for example ETH does not “earn revenue” and yet clearly has a market value) or may be exceptionally far into the future, and the question of which interest rate to use for discounting is highly subjective.

It certainly **can** be applied to tokens…

![Sample Discounted Cash Flow (DCF) valuation approach…](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91dbd8e5-170d-4f3f-832e-3330572880ee/Untitled.png)

Sample Discounted Cash Flow (DCF) valuation approach…

![…and corresponding scenario analysis.
Source: [Curve Finance Valuation Report](https://messari.io/report/curve-finance-valuation-report?)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cafb9771-a0df-42ec-b52d-2808ab8d8646/Untitled.png)

…and corresponding scenario analysis.
Source: [Curve Finance Valuation Report](https://messari.io/report/curve-finance-valuation-report?)

But even in traditional finance, this method is not generally the first choice for valuing an investment with comps that already have a market-traded price, and which often don’t pay a meaningful yield.

In fact, the Messari DCF example above essentially gets around some of the challenges of DCF by just assuming at the end of 5 years a comp-based multiplier is applied to its cash flows.

This brings us to…

## Relative Valuation (Market Comps)

This approach is one of the most general and flexible, as well as one of the easiest to interpret. It makes use of the “cheat” that we don’t need to answer the question of valuation from scratch when the free market has already done most of the work for us.

In other words, all we need to do is figure out the valuation **relative** to similar projects that already have a market-determined valuation.

In TradFi this is typically done within a given industry, to ensure comps are similar, and based on specific valuation metric(s) such Price-to-Earnings or Price-to-Sales.

The equivalent for tokens would be to look at the tokens of similar projects with similar use cases and look at valuation metrics like Market Cap / TVL, MarketCap / Fees, non-native-token yield, MarketCap / Daily Active Addresses, etc.

This approach’s simplicity and flexibility mean it can be used even for cases where other approaches are difficult to fit, such as L1 valuations.

https://twitter.com/Artemis__xyz/status/1574422232666963972?s=20

![Relative valuation approach to CRV using Price-to-Sales (P/S) as the valuation metric.
Source: [Curve Finance Valuation Report](https://messari.io/report/curve-finance-valuation-report?)](https://cdn.sanity.io/images/2bt0j8lu/production/8d8a774ecf2317e913510bf6a49f8fe5977ee761-900x511.png?w=900&fit=max&auto=format&dpr=3)

Relative valuation approach to CRV using Price-to-Sales (P/S) as the valuation metric.
Source: [Curve Finance Valuation Report](https://messari.io/report/curve-finance-valuation-report?)

The wrinkle is which comps you pick - the market has already justified those project’s prices, but the comps need to be justified as being the most similar to your product. Sometimes those comps can even be the project’s own history to demonstrate whether a project is potentially over or undervalued a current valuation metric, versus the historical average level of that valuation metric. For example:

> **MKR still trades at the low of its multiple range (10x P/E). This compares to 20x P/E that MKR used to trade at during the buyback and burn era.
Source: [MKR: Burn Baby Burn](https://ouroborosresearch.substack.com/p/mkr-burn-baby-burn)**
> 

And you can very easily layer in additional modifiers to this approach as well.

For example, perhaps projects that use “veCRV” style tokenomics trade at an average 10% premium relative to their respective peers - that becomes another factor to layer in to adjust for Curve’s most direct comps not having that mechanism.

# Real-World Example Models

Below is a list of curated models with various approaches, and built with various tools including spreadsheets, Python using custom notebooks or existing [simulation libraries like radCAD](https://github.com/CADLabs/radCAD), and even “drag and drop” GUI based tool [Machinations.io](http://machination.io/).

If you know of a public or open-source working model that should be added to this list, please get in touch.

## Ethereum 2.0

### Deterministic

https://docs.google.com/spreadsheets/d/1UlxKC98STwN-AoonytC-qOscZ_99fAMpMvB6EfGGe9E/edit#gid=0

https://docs.google.com/spreadsheets/d/1y18MoYSBLlHZ-ueN9m0a-JpC6tYjqDtpISJ6_WdicdE/edit#gid=769350728

### Stochastic

https://github.com/CADLabs/ethereum-economic-model

## Liquity (LUSD)

[Google Colaboratory](https://colab.research.google.com/drive/1AyhFfE_EKCcMO6HeG04Se3hbraTxODWU)

**Liquity Macroeconomic Model - Theory & Results**

## AMM

[Complete Example Token Side AMM](https://machinations.io/community/matthew.16/complete-example-token-side-amm-bb3823fae99011ec8c2902f943517e50/)

## Filecoin

### Deterministic

[Google Colaboratory](https://colab.research.google.com/drive/1qaLM2Fm27kQ07jIGBPdkdoTvo9-YAAtq?usp=sharing)

**Filecoin Economy Forecaster**

https://github.com/protocol/filecoin-mecha-twin

### Agent Based

https://github.com/protocol/filecoin-agent-twin

## Outlier Ventures - General Token Model

Outlier Ventures has graciously agreed to include their deterministic spreadsheet token model  and their stochastic model via radCAD integration in this open source guide, but has the following requests for those making use of the model.

<aside>
⚠️ “**Quantitative Token Model (QTM) - Access**

**Important Notes - MUST READ**

- The tool is located in a Google Drive directory. It can only be used with Google Sheets and not as a desktop version -> A local download is therefore not recommended.
- You are allowed to work with the tool and extend it with respect to your needs as you wish. The tool is free to use.
- **All we ask in return is that you must not remove nor change the Information tab of the sheet and the relation to Outlier Ventures -> Also don't remove the OV banner and logo on the individual tabs!”**
</aside>

### Deterministic

**To access the latest version of the Quantitative Token Model (QTM) Spreadsheet:**

1. Request access to the tool via this link:
https://drive.google.com/drive/folders/1mKZVGR5_qsrbP9mVkMddLrB791NPeOHP?usp=share_link
2. Create a copy of the QTM version with file name:
"YOUR_NAME_Quantitative_Token_Model_Vx.xx" in your personal Google Drive directory
3. Open it from your own directory and start working with it

**If the latest version is unavailable, an earlier version is available here:**

https://docs.google.com/spreadsheets/d/1uhtTgkTSYYtyOUOcklY-5Zl1uiEjhfAnCiKj5zXmNds/edit?usp=sharing

https://docs.google.com/spreadsheets/d/1zh465cWXWwzZxH1BHIL24K-RMT8qxHL33t4S7vlxfg8/edit?usp=sharing

### Stochastic

https://github.com/OutlierVentures/QTM-Interface

# Additional Resources

- Blog, [How We Simulated and Subsequently Abandoned the Mythx Token](https://atchai.com/blog/2018-12-31-simulation-mythx-token-ethereum/)
- Blog, [Simulating Token Economies: Motivations and Insights](https://6thman.ventures/writing/simulating-token-economies-motivations-and-insights/)
- Blog, [Modeling the Filecoin Economy — Part 2](https://medium.com/cryptoeconlab/modeling-the-filecoin-economy-part-2-9388a6e26fb9)
- Paper, [Ethereum 2.0 Economic Review](https://drive.google.com/file/d/1pwt-EdnjhDLc_Mi2ydHus0_Cm14rs1Aq/view?usp=sharing)
- Blog, [Checklist for Destruction: The Turbo Death Spiral, Part 1](https://medium.com/@0xRez/the-turbo-death-spiral-part-1-checklist-for-destruction-e024f19215f8)
- Blog, [The Media Has A Probability Problem](https://fivethirtyeight.com/features/the-media-has-a-probability-problem/)
- Blog, [Why You Should Care About the Nate Silver vs. Nassim Taleb Twitter War](https://towardsdatascience.com/why-you-should-care-about-the-nate-silver-vs-nassim-taleb-twitter-war-a581dce1f5fc)
- Blog, [On Price Stability of Liquity](https://www.liquity.org/blog/on-price-stability-of-liquity)
- Blog, [Which one should you use? Arithmetic or geometric mean TWAP](https://delphilabs.medium.com/which-one-should-you-use-arithmetic-or-geometric-mean-twap-ded01532bf49)
- Paper, [While Stability Lasts: A Stochastic Model of Non-Custodial Stablecoins](https://arxiv.org/abs/2004.01304)
- Forum, [Blameless Post Mortem: Curve - Aug 8, 2023](https://governance.aave.com/t/blameless-post-mortem-curve-aug-8-2023/14386)
- Thread, [“Low Float, High FDV”](https://twitter.com/jonwu_/status/1590883261164638208)
- Blog, [Fully Diluted Value is a Misleading Concept](https://www.ar.ca/blog/fully-diluted-value-is-a-misleading-concept)
- Thread, [Modeling CRV & CVX Subsidies](https://twitter.com/Riley_gmi/status/1531259688104251392?s=20)
- Paper, [A Framework for DAO Token Valuation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4309744)
- Paper, [Tokenomics: Dynamic Adoption and Valuation](https://academic.oup.com/rfs/article/34/3/1105/5891182)
- Blog, [On Verifying Token-Based Systems](https://blog.oceanprotocol.com/on-verifying-token-based-systems-c33eca757ecf)
- Paper, [Measuring Inflation within Virtual Economies using Deep Reinforcement
Learning](https://www.scitepress.org/Papers/2021/103928/103928.pdf)
- YouTube, [Token Engineering Hard Skills - with Machinations.io](https://www.youtube.com/watch?v=DNGvEWzGEQM)
- Blog, [How to Model with TokenSPICE EVM Agent Simulation](https://medium.com/tokenspice/how-to-model-with-tokenspice-evm-agent-simulation-2b2ef8cfe9c9)
- Github, [Mesa: Agent-based modeling in Python 3+](https://github.com/projectmesa/mesa)
- YouTube, [Reinforcement Learning with Python](https://www.youtube.com/playlist?list=PLgNJO2hghbmjlE6cuKMws2ejC54BTAaWV)

# Primary Tool: Modeling Tools & Tokenomics Design Canvas (TDC)

<aside>
 💡 Complete “Step 6: Economic Security Framework” of the **[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21).**

[Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21)

Having completed the **Incentive Mechanism Framework** and **Economic Security Frameworks** you should have a good idea of the specific questions, assumptions, parameters, and risks you need to stress test and quantify.

To do so, make use of one of the following recommended modeling tools below:

- See the “Sample Market Comps” and “Sample Scenario Analysis” tabs of the [**Tokenomics Modeling Template**](https://docs.google.com/spreadsheets/d/13uc39fMqLb1RKvcGk9s_whwZXgkftfaFLcgPkJpG9YI/edit?usp=sharing). You can save an editable copy of the template by clicking **File > Make a Copy**.
- For generating random paths and conducting stochastic analysis in Python, see the “Brownian Motion Generator” repository on GitHub
    
    https://github.com/mattyTokenomics/brownian-motion-simulations
    
- Other Tools:
    - [Machinations.io](http://Machinations.io) - GUI Based ‘Drag and Drop’ Modeling
    - [radCAD](https://github.com/CADLabs/radCAD) - lightweight but powerful framework for deterministic, stochastic, and/or agent-based simulations in Python
    - [TokenSPICE](https://github.com/tokenspice/tokenspice) - agent-based simulations of tokenized ecosystems with EVM in-the-loop, in Python and Solidity
</aside>

# Video

https://youtu.be/PA3Rr1bfIgg

# 2.7 Legal Opinion & Structure

# Introduction

Now that you’ve completed every other step in the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21), it’s time to engage with a registered legal professional (if you haven’t already). You need to do so **before** you launch your token.

While some jurisdictions have published frameworks that explicitly distinguish between utility tokens and security tokens, this far from the case for every jurisdiction.

In fact the SEC has taking legal action against protocols like LBRY, that did not not even conduct an ICO token sale.

> The argument a digital asset is not a security because it has “utility” is a favorite argument of critics of the SEC’s enforcement actions against issuers of digital assets. Unfortunately, the “utility” argument appears to be of little merit when the digital asset is offered and sold to raise capital.
Source: [Canary in the LBRY, Federal Judge Grants SEC’s Motion, Rules Digital Asset is a Security](https://www.nelsonmullins.com/idea_exchange/blogs/investigations/sec/canary-in-the-lbry)
> 

But securities law is not the only legal aspect you need to consider. Other relevant aspects include, but are not necessarily limited to:

- Project Corporate Structure
    - Ecosystem Foundation Entity
    - Token Seller Entity
    - Development Entity
    - DAO Legal Entity
- Taxes
    - Project Taxes
    - Personal Taxes
- Banking
    - Money Transmission Compliance
    - KYC/AML Compliance

This guide is not legal advice, and I am not a lawyer - it would be irresponsible for this chapter to be a summary of legal resources in my own words or based on my own opinions.

Thus, this chapter includes a curated list of relevant resources that cite legal professionals in their own words.

Keep in mind, even if a lawyer shoots down your initial design, you can work with them to iterate, repeating the steps in the [Tokenomics Design Canvas](https://www.notion.so/Tokenomics-Design-Canvas-9b15bbd593504e9cbb91f82f95f75ca9?pvs=21) until you have something that works fro everyone, including your legal representation.

*If you are a legal professional and would like to contribute to this chapter, please get in touch.*

# Top 5 Legal ‘Rules of the Road’

**This list is directly quoted from Miles Jennings. Read [his original thread here](https://twitter.com/milesjennings/status/1550541473443000321?s=20).*

1. “Don’t sell tokens to U.S. persons for fundraising purposes.”
2. “Even if you aren’t selling tokens, don’t ever market/hype them as an investment opportunity.”
3. “Don’t prioritize/emphasize secondary market liquidity or listings.”
4. “Decentralization matters… so build a final product before you launch a token”
5. “Communication matters… both public as well as private”

# Overall Guide: Legal Structuring for Token Sales

This brief guide by lawyer Clarence Guo succinctly covers many of the questions builders have when it comes to the practicalities of launching a token:

https://drive.google.com/file/d/1gnzmPRHbod6gOBMI14aDElqoV9-XHGDz/view

(**If the above preview does not render [you can also find it here](https://drive.google.com/file/d/1gnzmPRHbod6gOBMI14aDElqoV9-XHGDz/view))*

Here are some **direct quote** highlights from the guide above:

<aside>
💡 Over the past 5 years, the most common structure which the market has settled on is a tripartite structure as follows:

- (a) Offshore Foundation / Trust (Foundation)
- (b) Offshore private company (100% owned by Foundation) (Token Seller)
- (c) Standalone onshore private company, with no shareholding link to Foundation (Development Entity)
</aside>

<aside>
⚠️ Wyoming "LLC DAO" is bad. Forces you into LLC structure where token holders are shareholders (security). Similar, Delaware LLC DAO also legally requires formal registration of all "members". Creates additional link to US regulatory regime when there may be none to begin with.

</aside>

<aside>
⚠️ Burning, buyback are common, yet very risky features. Flagged by various regulators around the world.

"Staking" needs to be considered very carefully. Does it result in some useful work being performed for the benefit of the protocol, or are there active elements? If not, token may be a passive investment (securities).

Focus on utility features of token. Value accrual should be wholly incidental, and not the main aim of the tokenomics.

</aside>

# Legal & Regulatory Resources

## General

- a16z, YouTube: [Regulation 101](https://www.youtube.com/watch?v=SEobUfVYLw0)
- a16z, YouTube: [Token Securities Framework and Launching a Network](https://www.youtube.com/watch?v=CrrcGiyPglI)
- LBRY Contact Info

https://twitter.com/LBRYcom/status/1617978599101042688?s=20

## DAO and Corporate Structure

- Legal Nodes, Blog: [Choosing a Legal Wrapper for Your DAO, A Playbook](https://drive.google.com/file/d/1yaSCAVvZrLdKcs68w2OkffR4dE9lTXJR/view?usp=sharing)
- a16z, Blog: [DAO Entity Features & Entity Selection](https://a16z.com/2022/05/23/dao-legal-frameworks-entity-features-selection/)
- a16z, Paper: [A Legal Framework for Decentralized Autonomous Organizations](https://a16zcrypto.com/wp-content/uploads/2022/06/dao-legal-framework-part-1.pdf)
- a16z, Paper: [A Legal Framework for Decentralized Autonomous Organizations Part II: Entity Selection Framework](https://a16zcrypto.com/wp-content/uploads/2022/06/dao-legal-framework-part-2.pdf)
- Delphi Labs, Blog: [Assimilating the BORG: A New Framework for CryptoLaw Entities](https://delphilabs.medium.com/assimilating-the-borg-a-new-cryptolegal-framework-for-dao-adjacent-entities-569e54a43f83)

## Decentralization

- Variant Fund, Blog: [Sufficient Decentralization: A Playbook for web3 Builders and Lawyers](https://variant.fund/articles/sufficient-decentralization/)
- Jesse Walden, Blog: [Progressive Decentralization: A Playbook for Building Crypto Applications](https://jessewalden.com/progressive-decentralization-a-playbook-for-building-crypto-applications/)
- a16z, Blog: [Decentralization for Web3 Builders: Principles, Models, How](https://future.com/web3-decentralization-models-framework-principles-how-to)
- a16z, Paper: [Principles & Models of Web3 Decentralization](https://a16z.com/wp-content/uploads/2022/04/principles-and-models-of-decentralization_miles-jennings_a16zcrypto.pdf)

## Blockchain Lawyer Accounts to Follow

A list of blockchain lawyers that share relevant informational content:
[**https://twitter.com/i/lists/1676566547953770496**](https://twitter.com/i/lists/1676566547953770496?s=20)

# Primary Tool: Securities Law Framework

<aside>
💡 Crypto Rating Council’s Securities Law Framework is a framework for evaluating your token from a securities law point of view.

Completing the framework does not replace the need to get your own legal representation, but it can make your conversations with lawyers much more productive, saving you time and money.

Access the framework, including a completed example framework for ETH, here:
https://www.cryptoratingcouncil.com/the-framework

</aside>

# Video Tutorial

# Appendices

## About the Author

[Matty](https://twitter.com/mattyTokenomics) is the Token Economics Lead at [Status.im](https://twitter.com/ethstatus), one of the earliest projects to launch on Ethereum, and [Logos](https://twitter.com/Logos_state), a Status initiative building the trust-minimized, corruption-resistant infrastructure that is key to creating network states.

Previously, he served as a tokenomics research resident for the [Stacks Foundation](https://twitter.com/Stacks), a smart contract L2 for Bitcoin and Top 50 project by market cap. He is also a former Techstars founder, and former algorithmic investment engineer at Bridgewater Associates, the world’s largest hedge fund by AUM.

He has more than a decade of experience designing, simulating, and optimizing economic models, and has contributed to community governance proposals, identified economic security flaws, modeled consensus mechanism changes, and helped improve the tokenomics for projects including L1/L2 chains and dApps on Ethereum, Polygon, Solana, Binance, and Stacks.

He mentors founders at the [BTC Frontier Fund](https://twitter.com/BTCFrontierFund) and the [Bitcoin Startup Lab](https://twitter.com/btcstartuplab) and is an angel investor in [EigenLayer](https://twitter.com/eigenlayer), [ChainPatrol](https://twitter.com/ChainPatrol), [Intmax](https://twitter.com/intmaxIO), [Delegate](https://twitter.com/delegatecash), [Anoma](https://twitter.com/anoma), [NeoSwap AI](https://twitter.com/neoswap_ai), and [Clip Finance](https://twitter.com/ClipFinance) among others.

Find more of his work and contact him at https://linktr.ee/tokenomics

## About the Stacks Foundation

[The Stacks Foundation](https://stacks.org/) is a Delaware Nonprofit Foundation that works “to ensure the [Stacks] community has the space and mechanisms available to self-organize, share information, and make decisions.” The Stacks Foundation helped make this open source guide possible.

Stacks (formerly “Blockstack”) is a Bitcoin layer-2 for smart contracts, enabling apps and digital assets that are secured by the Bitcoin L1 chain. To attack Stacks’ history, e.g., to alter any transaction more than about a day old, an attacker needs to do a deep reorg of Bitcoin itself.

The STX token is the gas token for the Stacks smart contract L2, enables decentralized programmable BTC (sBTC), and pays “stackers” a native BTC yield as an organic product of its consensus mechanism. It was launched in a first-of-its-kind [SEC-qualified ICO in 2019](https://www.coindesk.com/markets/2019/09/10/blockstacks-regulated-token-offerings-raise-23-million/), before subsequently reaching sufficient decentralization to [no longer file as a security with the SEC in 2021](https://decrypt.co/69980/hiro-formerly-blockstack-says-its-stx-token-from-security-to-utility-token).

Learn More:

- “[Stacks: A Bitcoin Layer for Smart Contracts](https://stacks-network.github.io/stacks/stacks.pdf)”
- “[sBTC: Design of a Trustless Two-way Peg for Bitcoin](https://stacks-network.github.io/stacks/sbtc.html)**”**
- “[Bitcoin: Beyond the Base Layer](https://drive.google.com/file/d/1sPyr6W6qJENwR8H8P4mJn8SdnUOtdUBn/view)” by [The Block Research](https://www.theblockresearch.com/)

## Requested Additions & Edits

If you like to assist with any of the below, please [get in touch](https://linktr.ee/tokenomics):

- Graphics designers who can help adapt more “marketable” graphic versions of the [Tokenomics Design Canvas](https://www.notion.so/9b15bbd593504e9cbb91f82f95f75ca9?pvs=21) and other frameworks
- Ecosystem specific resources for raising capital and token launchpads for future chapter, “2.8 Prepare for Launch”
- radCAD and/or reinforcement learning Python developers who want to collaborate in building an intelligent agent based tokenomics modeling engine
- Subject matter experts who want to contribute to a specific sub-topic
- Publishers interested in releasing this material in other forms

## The Tokenomics Design Canvas

## Additional Resources

### Tokenomics Reading List

[Matty on Twitter](https://twitter.com/mattyTokenomics/status/1662117802315255808?s=20)

### Tokenomics Accounts to Follow

[**https://twitter.com/i/lists/1601969991989006337**](https://twitter.com/i/lists/1601969991989006337?s=20)

### Blockchain Lawyer Accounts to Follow

[**https://twitter.com/i/lists/1676566547953770496**](https://twitter.com/i/lists/1676566547953770496?s=20)

### Research Reports

- **[Messari Research](https://messari.io/research)**
- [**Prime Rating**](https://www.prime.xyz/rating-defi)
- [**CryptoEQ**](https://www.cryptoeq.io/dashboard)
- [**Tokenomics Hub**](https://www.tokenomicshub.xyz/)

### Communities

- [**Tokenomics DAO**](https://tokenomicsdao.xyz/)
- [**Token Engineering Commons**](https://tecommons.org/)

### Podcasts

- [**Bell Curve**](https://open.spotify.com/show/3uMWirMj2hc7IQYEUeBTyT?si=22ecdf0b5048433b)
- [**Tokenomics DAO Podcast**](https://open.spotify.com/show/7lQuGyYzKilKINYQ9cKJ6H?si=4663945b2ce0416e)

### YouTube Playlists

- [**Tokenomics Crash Course**](https://youtube.com/playlist?list=PLa_a2TnKITJ9YiVWcfJ7TDjTvYL4TXBIQ)
- [**Foundations of Blockchains**](https://www.youtube.com/playlist?list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA)
- [**a16z Crypto Startup School**](https://www.youtube.com/playlist?list=PLK9Lwn4_TfLS3I9huJjd-k_FeMKiTkAff)
- [**a16z Crypto Summer Research Seminars**](https://www.youtube.com/watch?v=VLWPl7PsPDQ&list=PLjQ9HCQMu_8yPGgfvsscHgt1w1KJkx8BN)
- [**TokenEngineering in Practice**](https://www.youtube.com/playlist?list=PL-GxJch-YeZebmmq77mrwLr-XYxFwaCw5)
- [**Game Theory 101**](https://www.youtube.com/playlist?list=PL76B0EB6DDFC42D02)

### Additional Resource Collections

- [**The Daily Ape - Tokenomics**](https://www.notion.so/458683e63ab34f4b8a0ed442946883d8?pvs=21)
- [**Token Economics Resource List**](https://docs.google.com/spreadsheets/d/1_py70Ic2u91VILJWCA7AMOXVZmmTv-zGo-LPr3PhDvM/edit#gid=0)
