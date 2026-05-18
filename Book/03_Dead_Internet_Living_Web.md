# Chapter 3

## Dead Internet, Living Web

On the morning of Wednesday 22 October 2025, I read three reports back to back at my desk, and by the time I was halfway through the third one I had stopped taking notes and just started staring at the screen.

The first was from Imperva, a security company that publishes an annual *Bad Bot Report*. The 2025 edition opened with a sentence I have quoted in talks at least a dozen times since: for the first time in a decade, automated traffic had overtaken human activity on the public web. Bots — not people — were now responsible for **51%** of all web traffic. Within that 51%, the category Imperva calls "bad bots" — scrapers, credential-stuffers, content thieves and fraud accounts — accounted for **37%** of the *whole* internet, on their own.[^1]

The second was from Cloudflare, whose engineers can see a significant share of global web traffic from inside their infrastructure. Cloudflare's own analysis, in a blog post titled *The crawl-to-click gap*, confirmed Imperva's picture and added a detail. Of the bot traffic Cloudflare could classify, roughly **80%** was attributable to *AI training crawlers* — GPTBot, ClaudeBot, Meta's scrapers, the new wave of agentic bots that performed autonomous tasks (1.7% of bot traffic at the time, but growing fast).[^2]

The third was a market projection from Grand View Research and a separate one from Gartner referenced in Europol's 2025 briefing. Both said, in slightly different language, the same thing: by 2030, between 90% and 99% of online content will be AI-generated or AI-assisted.[^3]

If you put the three reports together — and this is the thing I did on the morning of the 22nd, before I had decided what to write that week — what you got was a picture of an internet whose dominant activity was no longer humans publishing and reading. The dominant activity was *machines reading machines.* The web was being trained on a version of itself written by the systems it was training.

Five days later, the fourth issue of the *Dream Machine* newsletter went out with a headline I had been circling for weeks. It said: *Is the Internet Dead Yet?*[^4]

I want to spend this chapter on the answer.

### The synthetic mirror

The "Dead Internet Theory," for those who haven't met it, is a notion that has been knocking around the internet since at least 2021. In its original, slightly conspiratorial form, it claims that most of the web has been replaced by bots — that the people you talk to on social media are agents, that the comments on news articles are agents, that the cultural water you swim in is a synthetic medium pretending to be a human one.[^5]

In 2021, when it was first articulated, it was an interesting bit of folklore that didn't quite map onto reality. The bots existed; they just weren't, yet, doing most of the work. The cultural water was still mostly human.

By October 2025, the maths had quietly inverted. Half of the traffic was machines. A majority of *new published content* was machine-assisted, according to a separate 2025 analysis by Graphite that put the human-to-AI authoring split at roughly 50–50.[^6] The pages those machines were writing were being scraped by other machines to train *next year's* generation of writing machines.

A recursive system trained on its own outputs is called, in academic AI circles, *model collapse*. The fear, in the published literature on this, is straightforward: a system that learns from synthetic data loses touch with the real-world signal that made it useful in the first place, and starts producing increasingly homogenised, brittle, hallucination-prone outputs.[^7]

What the 2025 numbers said, when you sat with them, was that we were no longer talking about model collapse as a theoretical risk. We were talking about *web* collapse — a slow, quiet, structural drift in which the public commons of writing, image-making, video and music started to be made by, and for, the machines that read it. Humans were still there. We were no longer, by any meaningful metric, the *primary audience*.

### What the Dutch researchers found

In the second week of October, a team of researchers in the Netherlands ran an experiment that I think will end up being cited a lot more in the years to come than it was at the time.[^8]

They built a small, stripped-down social platform — no algorithms, no ranking, no advertising — and populated it with several hundred large-language-model-based AI agents. The agents had different "personalities," different starting interests, different opinions. The researchers' question was simple: in the absence of any algorithmic distortion, would the bots — when free to interact only with each other, with no human in the loop — converge on a healthy public conversation, or would they reproduce the pathologies we already see in human social media?

The answer, within hours, was the second. The agents fractured into warring tribes. A narrow elite captured the bulk of the attention. Extremist echo chambers flourished. The platform, with no humans on it at all, produced almost exactly the same dynamics that the human-plus-algorithm version of social media has produced for the last decade.

The conclusion the researchers reached — and the one I want to flag now, because it is going to recur in this book — was that the *architecture itself* is the problem. The toxicity wasn't, or wasn't only, in the humans. It was in the design of the system: how identity worked, how attention was allocated, how voices were amplified or suppressed. The bots reproduced it because they had been trained on the human web, and the human web has the same architecture.

This is the single most important thing I learned in the first two months of writing the newsletter. The optimistic AI take and the pessimistic AI take both assume the architecture stays the same. The optimist thinks the agents will use it better; the pessimist thinks they will use it worse. The Dutch experiment suggests that neither matters — the architecture *itself*, regardless of who or what is filling it, will produce the same pathologies.

If we want a different outcome from the AI era, we need different rails, not just different drivers.

### What survives

In the original Issue 4, I wrote that "authenticity and provenance become the new scarcity." I want to defend that line, six months on, because I think it is the part of the chapter that has held up best.

The simplest way to put it is this: when everything online can be faked, cloned or generated at near-zero cost, the most valuable signal is *proof that a person made something.* Not just an aesthetic preference. An economic one.

You can see this argument being made, all over the creative industries, by people who have nothing else in common. Adam Mosseri, the head of Instagram, said in early January 2026 that the platform should focus on "fingerprinting real media" rather than tracking and disclosing AI slop — that is, the policy should be to identify and amplify provably human-authored content rather than to play whack-a-mole with the synthetic stuff. His framing was telling: *"Everything that made creators matter — the ability to be real, to connect — is now accessible to anyone with the right tools."*[^9] The platform head was acknowledging, on the record, that the previous decade's content-creation moat had been completely flooded. The only remaining moat was *being a person you could verify was a person.*

Sundance Institute, launching its AI Literacy Initiative the same month, framed authentication and authorship as the central question filmmakers needed to negotiate to remain in control of their own work.[^10] Bandcamp, the indie music platform that has always carried more cultural weight than its commercial size implied, simply banned AI-generated music outright in early 2026.[^11] San Diego Comic-Con drew the same line for its 2026 art show, with rule language as flat as anything in the cultural sector: *"Material created by Artificial Intelligence (AI) either partially or wholly, is not allowed in the art show. If there are questions, the Art Show Coordinator will be the sole judge of acceptability."*[^12]

These are not, on their own, market signals — they are policy decisions. But they were being made, in early 2026, against a backdrop of audience behaviour that suggested something larger. Deezer reported in April 2026 that AI-generated music had risen to **44% of all daily uploads** — 75,000 tracks a day, more than 2 million a month — but that those tracks accounted for **between 1% and 3% of total streams.**[^13] The audience, given the choice, was choosing not to listen.

That ratio — call it 44 to 3, or 75,000 to listen-to-nothing, or whatever shorthand you prefer — is the most important number in this book, and I will come back to it in Chapter 4. The reason I introduce it here is that it is the empirical answer to the Dead Internet question. The web is not dead. The web is producing exponentially more *stuff* than it ever has, and the humans on it have started to develop antibodies. They are not engaging with the synthetic flood. They are, by their attention patterns, picking out the human signal.

### Synthetic sincerity

In November 2025, the filmmaker Marc Isaacs premiered a documentary at IDFA — the International Documentary Film Festival in Amsterdam — with a title I have not been able to get out of my head. The film was called *Synthetic Sincerity.* It was a hybrid piece, blending real footage with AI-generated characters, deliberately blurring the line between what was real and what wasn't, and asking — as its working premise — whether AI characters could be *taught* authenticity.[^14]

The film and its accompanying *Hollywood Reporter* interview ran the same week as a separate Variety piece titled *AI-Generated Images Threaten Future of Documentary as People 'Will Stop Believing Anything.'*[^15] The juxtaposition was almost too on the nose. One filmmaker trying to *expand* the territory of the synthetic, on the assumption that authenticity is a property that can be invested in fictional characters; another set of filmmakers arguing that the very ability to fake reality is hollowing out the cultural credibility of their entire form.

I am not going to take a side on the documentary question, because I don't think there is one yet. What I want to flag is that *Synthetic Sincerity* — the phrase, not the film — is a useful piece of vocabulary. It names a category. There is a kind of work, in this new ecology, that is *trying* to be authentic and openly synthetic at the same time. It is not pretending to be human. It is asking whether the qualities we used to attach to humans — emotional truth, lived experience, perspective — can be ported over to synthetic characters who are honest about what they are.

The verdict, six months in, is mixed. Some of the strongest creative work I have seen this year sits firmly in this space. Hoyt Dwyer's animated short — made by a former Apple TV creative, competing at the AI FilmFest Japan in late 2025 — does not pretend its characters are real, and is more honest about its medium than three quarters of the live-action features I watched the same year.[^16] Andrii Daniels' viral *Deadpool / Harry Potter* Christmas clip, which he made in a Ukrainian bomb shelter during an active war, has more sincerity in any single frame than most legacy-studio output, precisely because the conditions of its making are on the screen.[^17]

Some of the worst work I have seen this year sits in the same space too. McDonald's Netherlands' AI-driven Christmas ad — released in December 2025 and pulled within days after a public backlash — was an attempt at *synthetic sincerity* that read, almost universally, as cynicism wearing a Christmas jumper. The line that travelled fastest, as the ad's reception turned, came from a working creative director responding on social media: *"No actors, no camera team, no light, no sound, just probably one guy, alone in front of a computer battling with an AI prompt who steals the look and everything else from someone else."* That sentence — circulated on LinkedIn and X within an hour of the ad's launch — was the thing that did the cultural damage. The brand had to pull the spot.[^18] The Valentino "AI handbag" campaign, criticised by the BBC for being "disturbing," was the same.[^19] Coca-Cola's AI holiday ad — the second time the company had tried this — divided viewers along almost the same lines as the previous year.[^20]

The interesting pattern, when you line these up, is not whether AI is "good" or "bad" for the work. The interesting pattern is that audiences are very fast, and very precise, at distinguishing *sincere* synthetic work from *cynical* synthetic work. The technology is the same. The fingerprint of the human intent behind it is not. And the audience can feel the difference at the speed of a swipe.

### What the brain study said

In the middle of all this — and I want to acknowledge that it is harder evidence than the cultural commentary — an MIT Media Lab study made the rounds in the autumn of 2025, in which researchers measured the brain activity of subjects writing essays with and without generative AI assistance. The headline finding was that AI users showed measurably reduced brain activity over the course of the writing tasks compared to control subjects writing on their own.[^21]

The headline framing — *AI makes you stupid* — was unfair to the study, which was small, preliminary, and didn't claim anything as strong as that. But the underlying observation has been replicated in other domains. When the cognitive load of producing the first draft is offloaded to a generator, the cognitive engagement of the human in the loop measurably drops. The work gets produced. The person producing it engages with it less.

This is the quieter consequence of the Continuum chapter — the one that doesn't show up in any line item on a P&L sheet but that I think we are going to be wrestling with for years. If the right-hand side of the continuum is "machine agency," and we slide more and more functions of our creative work to that side, we are not just changing the *outputs.* We are changing the *people doing the work.* The thinking that produces the work happens, or doesn't, in the bodies of the people in the workflow. And brains, like muscles, atrophy with disuse.

This is not a reason to refuse the tools. It is a reason to be careful about *which functions* you offload, and to keep a deliberate, conscious habit of *exercising the cognitive work that defines your craft.* The Continuum doesn't just describe where the line sits today. It describes where you are willing to *let* your mind sit, every day, for the rest of your career.

### The architecture, again

I want to come back to the Dutch researchers' result one more time before I close this chapter, because I think it is the through-line.

The story we are mostly told, by toolmakers and platforms and the optimistic side of the industry press, is that the AI era is *a thing happening to* an otherwise functioning internet. The implication is that if we can get the AI part right — better tools, smarter agents, cleaner training data, better watermarking — then the internet itself will be fine.

I do not think this is true any more. I think what the bot statistics, the Dutch experiment, the model-collapse research, and the audience response to AI music collectively show, is that the architecture itself — the rails on which all this is running — was already broken, and that AI is just the load that has finally exposed how broken it was.

The Dead Internet, in this reading, is not a thing AI is doing to us. It is a thing the web's architecture was already drifting towards — attention-monopolised, identity-collapsed, provenance-blind, optimised for machine-readable metadata rather than human-meaningful work — and AI is the technology that has shown us the destination.

The *Living Web* — and this is where I find the actual reason for the rest of this book — is something that has to be deliberately built. It is the part of the internet where authorship is provable, where attribution is durable, where attention is allocated on something other than virality, where the architecture itself supports the kind of work that humans do well together. None of that comes for free. None of it is a side-effect of better AI models.

We have to make it. On purpose. In the next twelve months.

That is the project the rest of this book is about.

[^1]: Imperva, *2025 Bad Bot Report: How AI is Supercharging the Bot Threat*. <https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^2]: Cloudflare, "The crawl-to-click gap: Cloudflare data on AI bots, training, and referrals." <https://blog.cloudflare.com/crawlers-click-ai-bots-training/>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md). Later 2025 updates show training crawlers declining from ~90% to ~74% of AI bot activity as scraper bots rose to 24% and a new "agentic" category emerged at 1.7%; see Cloudflare, "A deeper look at AI crawlers: breaking down traffic by purpose and industry." <https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/>.

[^3]: Grand View Research, "Generative AI Content Creation Market Report." <https://www.grandviewresearch.com/industry-analysis/generative-ai-content-creation-market-report>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md) also cites Gartner and Europol forecasts of 90–99% AI-generated or AI-assisted online content by 2030.

[^4]: [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md), "Editor's Pick: Is the Internet Dead Yet?" 23 October 2025. <https://www.linkedin.com/pulse/dream-machine-creative-ai-news-insight-oct-25-issue-4-woodbridge-hzttc/>.

[^5]: Wikipedia, *Dead Internet Theory*. <https://en.wikipedia.org/wiki/Dead_Internet_theory>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^6]: Graphite, 2025 analysis of new web content by author type (human vs. AI vs. AI-assisted). Cited in [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^7]: For "model collapse" as a term of art, see Ilia Shumailov et al., "The Curse of Recursion: Training on Generated Data Makes Models Forget" (2024), and subsequent literature.

[^8]: Futurism, "Researchers built a social network with only AI agents — within hours it had collapsed into warring tribes." <https://futurism.com/social-network-ai-intervention-echo-chamber>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^9]: *Digital Music News*, "Instagram Chief Says We Should 'Fingerprint Real Media' Instead of Tracking and Disclosing AI Slop." <https://www.digitalmusicnews.com/2026/01/05/instagram-chief-ai-slop-comments/>. See also *WebProNews*, "Instagram Head Warns AI Images Erode Trust, Calls for Verification Standards." <https://www.webpronews.com/instagram-head-warns-ai-images-erode-trust-calls-for-verification-standards/>. [*Dream Machine* Issue 13](../Dream%20Machine%20MD/13.md).

[^10]: Sundance Institute, "Centering the Artist: Why We're Launching the AI Literacy Initiative." <https://www.sundance.org/blogs/centering-the-artist-why-were-launching-the-ai-literacy-initiative/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^11]: *Stereogum*, "Bandcamp bans AI music." <https://stereogum.com/2485199/bandcamp-bans-ai-music/news>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^12]: *CNET*, "San Diego Comic-Con Draws a Line: No AI Art Allowed at 2026 Event." <https://www.cnet.com/culture/san-diego-comic-con-bans-ai-art-for-2026-event/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^13]: Deezer, "AI-generated tracks now represent 44% of all new uploaded music," April 2026. <https://newsroom-deezer.com/2026/04/ai-generated-tracks-represent-44-of-new-uploaded-music/>. *Music Business Worldwide*, "75,000 AI-generated tracks now flood Deezer daily." <https://www.musicbusinessworldwide.com/75000-ai-generated-tracks-now-flood-deezer-daily-representing-44-of-all-new-music-uploaded-to-the-platform-says-streamer/>. *Dream Machine* Issues [7](../Dream%20Machine%20MD/7.md), [26](../Dream%20Machine%20MD/26.md), [27](../Dream%20Machine%20MD/27.md), [28](../Dream%20Machine%20MD/28.md).

[^14]: *The Hollywood Reporter*, "'Synthetic Sincerity' by Marc Isaacs Explores if AI Characters Can Be Taught Authenticity: IDFA." <https://www.hollywoodreporter.com/movies/movie-news/synthetic-sincerity-film-idfa-ai-authenticity-interview-1236426180/>. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^15]: Variety, "AI-Generated Images Threaten Future of Documentary as People 'Will Stop Believing Anything'." <https://variety.com/2025/film/festivals/ai-generated-images-threaten-future-of-documentary-1236583466/>. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^16]: PR Newswire, "From Apple TV Creative to AI Filmmaker: Hoyt Dwyer's Animated Film To Compete at AI FilmFest Japan 2025." <https://www.prnewswire.com/news-releases/from-apple-tv-creative-to-ai-filmmaker-hoyt-dwyers-animated-film-to-compete-at-ai-filmfest-japan-2025-302598064.html>. [*Dream Machine* Issue 6](../Dream%20Machine%20MD/6.md).

[^17]: Variety, "AI Creator Behind Viral 'Deadpool,' 'Harry Potter' Christmas Clip Made His Film in a Ukrainian Bomb Shelter." <https://variety.com/2026/digital/news/ai-video-deadpool-harry-potter-andrii-daniels-1236624632/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^18]: *Branding in Asia*, "'It's the Most Terrible Time of the Year' — McDonald's Netherlands' Wonderfully Chaotic, AI-Driven Christmas Film." <https://www.brandinginasia.com/its-the-most-terrible-time-of-the-year-mcdonalds-netherlands-wonderfully-chaotic-ai-driven-christmas-film/>. Pulled following backlash: *SiliconAngle*, "Not ready: McDonald's AI-generated ad taken down after public backlash." <https://siliconangle.com/2025/12/10/not-ready-mcdonalds-ai-generated-ad-taken-public-backlash/>. [*Dream Machine* Issue 11](../Dream%20Machine%20MD/11.md).

[^19]: BBC News, "Fashion house Valentino criticised over 'disturbing' AI handbag ads." <https://www.bbc.co.uk/news/articles/cwyvjyvn83go>. [*Dream Machine* Issue 10](../Dream%20Machine%20MD/10.md).

[^20]: *Adweek*, "Coca-Cola Uses AI to Rekindle the Magic of Its Holiday Ads." <https://www.adweek.com/creativity/coca-cola-uses-ai-to-rekindle-the-magic-of-its-holiday-ads/>. [*Dream Machine* Issue 6](../Dream%20Machine%20MD/6.md).

[^21]: *AI News*, "AI causes reduction in users' brain activity, MIT." <https://www.artificialintelligence-news.com/news/ai-causes-reduction-in-users-brain-activity-mit/>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).
