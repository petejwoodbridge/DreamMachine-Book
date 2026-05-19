# Chapter 12

## Authenticity as the New Scarcity

In early 2026, a stop-motion animator who goes by *Tiny Grandma* on YouTube uploaded a short to her channel. It was a stop-motion piece — claymation, frame by frame, the kind of work that takes weeks to make a few seconds of. YouTube's AI-detection systems flagged it as AI-generated content and applied the platform's automated labelling. The video went viral, not because of the animation, but because the platform's automated system had wrongly flagged genuine human handcraft as synthetic.[^1]

The story of *Tiny Grandma* is the perfect inverse of the Tilly Norwood story we opened with in Chapter 1.

If Tilly Norwood was the moment a synthetic creation tried to enter the working creative economy as if it were human, *Tiny Grandma* was the moment a human creation was wrongly identified as synthetic by the very systems that were supposed to protect the public from synthetic content. Both moments tell you the same thing, from opposite directions: the *signal* of whether a piece of creative work was made by a human is now an economic, cultural and legal asset of the first order, and the infrastructure for reliably establishing that signal is one of the most underdeveloped parts of the current creative economy.

This is the chapter about *provenance.* About why the question "did a person make this?" has become — in eight months — the single most important question in creative AI policy, and about what the people, companies and institutions trying to answer it are doing about it.

### The death threats

In April 2026, [*Dream Machine* Issue 23](../Dream%20Machine%20MD/23.md) reported, with as little editorialising as I could manage, that **Tilly Norwood's creator Eline Van der Velden** had received death threats.[^2]

The threats were not, of course, justified by anything. Death threats never are. But the cultural reaction that produced them — the visceral, sustained hostility that built up around the *idea* of a synthetic actress through the autumn of 2025 and the spring of 2026 — was not random. It was a specific response to a specific kind of cultural transgression. *You came here pretending to be one of us. You took something that belongs to us.*

The death threats are the extreme tail of a much larger curve of audience response that has been quietly shaping the AI creative economy for these six months. The slop ceiling in Chapter 5 — the 44%-to-3% Deezer ratio — is the polite version of the same response. The vehement audience pushback against AI art in *Call of Duty: Black Ops 7* and *Anno 117* in November 2025 is another version. The viral reaction to *Spotify*'s AI music infiltrating Discover Weekly playlists, the public anger at *McDonald's Netherlands' AI* Christmas ad, the "*disturbing*" reception of *Valentino's* AI handbag campaign — every one of these episodes is the audience saying, in increasingly direct terms, *we know what is human-made, we want what is human-made, and we are paying attention to who is trying to slip us something else.*

This is the cultural pressure that *authenticity-as-scarcity* describes. It is not, as some of the more dismissive AI commentary has framed it, a romantic attachment to old craft. It is a *market signal.* The audience is allocating attention, money and trust on a basis that increasingly weights human authorship as a positive variable. I have come, in talks since the autumn, to call this the **Authenticity Premium** — the measurable excess of attention, willingness to pay, and cultural credit that audiences allocate to creative work whose human authorship can be verified. The Authenticity Premium is the *positive* side of the slop ceiling: the slop ceiling tells you what audiences *will not* engage with; the Authenticity Premium tells you what they *will pay extra for.* Both are market findings. Both are produced by the same underlying audience behaviour. The data is unambiguous. The strategic implication, for every working creative and every studio operating in this period, is also unambiguous.

The chess analogy I develop at length in [Chapter 15](15_Choosing_the_Future.md) sits underneath this. The Authenticity Premium is what it looks like when an audience, faced with an infinite supply of machine-optimal work, allocates its scarce attention to the *deliberately un-machine-like* move. The 88% of UK respondents who wanted licensing-in-all-cases were articulating the same preference at the policy layer. The 44%-to-3% Deezer ratio was the same preference at the listening layer. The Television Academy's "tools used to bring it to life" language was the same preference at the institutional layer. The Authenticity Premium is, at its core, the *commercial price* of the deliberately-human move — the move the engine, by construction, could not have made — and the audience's reliable willingness to pay it.

The question is what the *infrastructure* for honouring that signal looks like.

### Fingerprinting real media

I quoted Adam Mosseri — the head of Instagram — in Chapter 4 making the case that the platforms should focus on "fingerprinting real media" rather than chasing AI slop disclosure. The fuller version of his argument, made repeatedly across late 2025 and early 2026, was that the current approach to AI content moderation — trying to detect and label everything synthetic — is unwinnable.[^3] The volume is too high, the detection is too unreliable, and the labelling produces both false positives (Tiny Grandma) and false negatives (the AI hate-songs spreading across European Spotify charts in November 2025).[^4]

The alternative Mosseri and others have argued for is *the inverse:* instead of trying to catch what's synthetic, build infrastructure that can *prove what's human.* A capture-time fingerprint — a cryptographic signature embedded by the camera, the microphone, the editing software, the upload pipeline — that travels with the file through its entire life on the public web.

The technical infrastructure for this is, as of 2026, partially built. The **Content Authenticity Initiative**, an Adobe-led coalition of camera makers, software companies and news organisations, has been working on it since 2019. By late 2025, **C2PA** (Coalition for Content Provenance and Authenticity) standards were supported by most major camera manufacturers, most major editing platforms, and a growing number of social-media uploads pipelines. The standards are robust enough that a photo taken with a C2PA-enabled camera, edited in Photoshop with C2PA-aware tools, uploaded to a C2PA-supporting platform, can carry a verifiable chain-of-custody for its entire provenance, from sensor to viewer.

Underneath this is **Google's SynthID** — a watermarking system that Google has been deploying across its AI generation tools, including Veo and Lyria.[^5] In December 2025, the company announced that users could ask the Gemini app, *"Is this video made with AI?"*, and receive a reliable yes/no answer based on the SynthID watermark. By January 2026, this capability was available in the consumer Gemini product.[^6]

These technologies are not, on their own, sufficient. Watermarks can be stripped by determined adversaries. C2PA chains break when files pass through non-compliant tools. The reliability of any given piece of provenance metadata depends on the integrity of every link in its chain. The trust infrastructure is still — relative to the speed of the AI rollout — early.

But what these technologies are doing, collectively, is establishing the *category.* They are saying: the question *did a person make this?* is technically answerable, with high reliability, given the right tooling. The next decade of cultural and legal policy in the creative industries will be — in significant part — about who controls that tooling, who decides what it certifies, and what economic value it carries.

If you want to know where the next ten years of investment, policy and platform politics in creative AI is going, watch the provenance layer. The companies that win the provenance infrastructure will be — in a real sense — the companies that own the *signal of authenticity* that the audience increasingly demands.

### The trademark, the trust, the tax

The cultural pushback against synthetic content has produced, alongside the technical provenance infrastructure, a parallel set of *legal and contractual* defences that working creatives have begun deploying around their own work and identity.

**Taylor Swift** filed trademarks on her voice and image in early 2026, specifically citing AI deepfake concerns.[^7] **Matthew McConaughey** publicly drew the same line in January 2026.[^8] **Madonna and Will Smith** appeared in AI videos by Higgsfield in early 2026, the Madonna piece becoming a marquee example of how a major artist could *deliberately* deploy synthetic imagery as part of their own brand.[^9] **George Clooney**, in November 2025, gave Variety the working actor's read on the synthetic-star economy: *"It's been just like a writer creating characters. You fall in love with your characters when you're writing them. It's a wonderful process. It wasn't like I just made her in a second, and that was it. You know, it took a long time."*[^10] Clooney was making, in his particular way, the same argument that the slop ceiling makes empirically: cultural stardom is a *function of time and human relationship.* It is not a function of generation cost. **Jeremy Renner** threatened a "multi-millions" lawsuit against an AI documentary director he said had used his voice without permission.[^11]

Underneath the celebrity layer, the structural infrastructure was being built. The **ELVIS Act**, Tennessee's AI-impersonation law, had been used by the **Johnny Cash estate** to sue Coca-Cola over a tribute-act ad soundtrack.[^12] **New York** passed a law in December 2025 forcing advertisers to disclose when they were using AI avatars. The SAG-AFTRA statement on the law's passage captured the political theory underneath the moment: *"These protections are the direct result of artists, lawmakers and advocates coming together to confront the very real and immediate risks posed by unchecked AI use."*[^13] **Governments around the world** were considering bans on Grok's app over an AI sexual-image scandal that broke in early 2026.[^14] By **May 2026**, the **AI Disclosure Standard** had been launched at the **Cannes Film Festival** as an industry coordination point for production-side AI labelling.[^15] The **Academy of Motion Picture Arts and Sciences** had — in a quietly consequential rule update — set the line *"You must be human to win"* for its 2026 awards.[^16] The **Emmys** had set their own AI guidelines. The Television Academy's language was a model of how to write a policy that defends authorship without picking a fight with the toolchain: *"The Television Academy reserves the right to inquire about the use of AI in submissions. The core of our recognition remains centered on human storytelling, regardless of the tools used to bring it to life."*[^17] *Tools used to bring it to life* — not *tools that did the work.* The grammar matters. **SAG-AFTRA's** four-year contract — finalised by spring 2026 — included what the trade press informally called the **Tilly Tax**: a structured set of provisions for compensation, consent and residuals when AI replicas of human performers are used.[^18]

Each of these is, on its own, a marginal piece of policy. Stacked together, they describe a new economic landscape: one in which *human authorship and identity* have become legally protected categories of creative work, with specific procedural and economic mechanisms for asserting them, defending them and compensating their use.

The cultural shorthand for this — *authenticity as the new scarcity* — captures the supply-and-demand logic. The legal shorthand — *human-authored work as a protected class* — captures the policy logic. Both are the same thing seen from different angles.

### What sincerity looks like in 2026

I want to come back to a distinction I made in Chapter 4, because it has held up through the last six months better than almost any other framing in this book.

I argued that audiences distinguish, very quickly, between *sincere* synthetic work and *cynical* synthetic work — that the underlying technology is the same, but the fingerprint of human intent behind the work is visible to the audience at the speed of a swipe.

The data from the spring of 2026 supports this. *Marketing Week*'s analysis "You can't dismiss AI ads as slop when they're winning in testing"[^19] documented that AI-generated advertising creative could, in fact, win in standard creative-effectiveness tests — *when the work was made with care, on a brief that respected the audience, by a team that had taste.* The same publication's parallel coverage of the audience pushback against the McDonald's Netherlands ad, the Valentino handbag campaign and a dozen other "AI slop" launches, made the inverse point. The technology is neutral. The intent is not.

The strongest AI-authored creative work of the period this book covers has, almost without exception, *not* tried to hide that it was AI-authored. Andrii Daniels' bomb-shelter clip foregrounded its conditions of making.[^20] Hoyt Dwyer's animated short for AI FilmFest Japan was upfront about its medium.[^21] *Dear Upstairs Neighbors,* the Google DeepMind / Connie He collaboration that premiered at Sundance, was *about* the constraints and possibilities of its production pipeline.[^22] *Synthetic Sincerity*, Marc Isaacs' IDFA film, took the disclosure to the title of the piece.[^23] *Watch the Skies*, the AI-dubbed Swedish UFO feature, disclosed the dubbing process as part of its identity.[^24] *Lily,* the $1m AI Film Award-winning Tunisian short, was framed by its director and reviewers as a piece *about* the new toolchain.[^25]

The pattern, repeated across thirty or forty examples I have looked at carefully, is the same: *AI work that owns its synthetic nature, and that is made with human creative intent, finds an audience.* AI work that tries to pass as something it isn't gets the audience response that Tiny Grandma's stop-motion got *from the algorithm* — an immediate, automatic, suspicious flag.

This is, in market terms, a stable equilibrium. It is the market that the slop ceiling and the audience pushback have built. And it is, for working creatives, a manageable and even encouraging environment to operate in. The audience is not against AI. The audience is against being lied to.

### What disclosure should look like

I want to lay out — because I have been asked this in every Q&A I have done since starting the newsletter — what I think the *practical* shape of authenticity infrastructure should look like for working creatives in 2026.

It is four things, in increasing order of investment:

**One. Disclose, consistently.** If you use AI in any part of your work, say so. In your credits. On your website. In your contracts with clients. In the metadata of your files. The act of disclosure does, in my experience, not cost you anything with the audience — the audience that is going to reject AI work would reject it anyway, and the audience that is going to accept it is the audience that values you being straight with them. The cost of *getting caught* not disclosing, in this environment, is materially higher than the cost of disclosing.

**Two. Document, deliberately.** Keep logs. Keep notes. Keep prompt histories. If a piece of work you make this year ends up being legally or culturally contested in 2030 — and a non-trivial fraction of work made this year will be — your ability to *show your workings* will be the difference between defending the work and losing it. The Sundance literacy initiative's emphasis on *evidence of human authorship* is exactly right.[^26]

**Three. Watermark, where appropriate.** Use SynthID, C2PA, or the equivalent provenance layer that your toolchain supports. If your work doesn't yet support these standards, ask your tool vendors when they will. The market for tools that support provenance metadata is, in 2026, larger than the market for tools that don't.

**Four. Build the chain.** If you are running a studio or an agency, build the *internal* infrastructure for verifying and tracking the provenance of your work end-to-end. The cost of doing this in 2026 is moderate. The cost of *not* doing it in 2029, when a client asks for the chain-of-custody on a piece of work and you can't produce it, is going to be much higher.

These are not, on their own, business strategies. They are, in 2026, the *minimum hygiene* for operating a credible creative practice in the AI era. Treat them as you would treat health-and-safety on a film set. Do them as a default. Do them well. Then get on with the work.

### The provenance infrastructure, named: thirty-six pieces of the puzzle

I want to lay out a more complete map of the provenance infrastructure that is being built in 2025–26, because the technical-and-policy stack is more advanced than the public conversation has caught up with, and working creatives reading this book need to know what is actually in the field.

Stacking the moves I have referenced across this chapter and the rest of the book, the inventory is roughly this:

**Capture-time signing and provenance metadata:**

1. **C2PA / Content Credentials** (Adobe-led, with Microsoft, Sony, Nikon, Leica, BBC, Canon participation) — the cryptographic-signature standard for capture-and-edit-time provenance.
2. **Leica M11-P / M11-D** — first consumer cameras with C2PA at the firmware level (2023, expanded through 2025).
3. **Sony Alpha 1 II and Alpha 9 III firmware** — C2PA support across pro Alpha range.
4. **Nikon Z9 firmware** — C2PA support for the AP/Reuters wire-service workflow.
5. **Canon professional bodies** — Content Credentials integration through 2025 firmware cycle.
6. **iPhone Camera app** (selected models, 2025–26) — capture-time signature support.
7. **Adobe Photoshop, Premiere, Lightroom** — edit-time chain-of-custody preservation through Content Credentials toolchain.
8. **DaVinci Resolve, Final Cut Pro, Avid Media Composer** — partial C2PA support through 2025–26 update cycle.
9. **Capture One** — Content Credentials integration for the high-end commercial-photography workflow.

**Synthetic watermarking and detection:**

10. **Google DeepMind SynthID** — embedded watermark for Veo (video), Lyria (audio) and Imagen (image) outputs.
11. **SynthID Verification via Gemini app** — consumer-facing yes/no detection.
12. **Lyria 3 SynthID extension** — audio verification across the Google music-model family.
13. **YouTube AI Detection Tool** — automated content classification (the *Tiny Grandma* false-positive case demonstrating both its scope and its current accuracy ceiling).
14. **Deezer's AI-music detection pipeline** — identifies up to 75,000 AI-generated tracks per day at upload time.
15. **Spotify AI Transparency Beta** — voluntary creator disclosure surfaced in the consumer player UI.
16. **Beeble** — independent detection-and-watermarking infrastructure used by some news organisations.
17. **Cloudflare AI bot classification** — public-web-infrastructure-level tracking of AI crawlers and agents.
18. **Sony music-identification technology** — identifying source recordings inside AI-generated outputs at the catalogue level.

**Institutional and contractual disclosure:**

19. **Cannes AI Disclosure Standard** — industry-coordination production-side labelling standard for the festival circuit (launched May 2026).
20. **Sundance AI Literacy Initiative** — creator-training programme funded by Google's $2M commitment, training 100,000+ artists in foundational AI literacy and provenance practice.
21. **Academy of Motion Picture Arts and Sciences "you must be human to win" rule** — 2026 awards eligibility update.
22. **Television Academy AI guidelines** — "tools used to bring it to life" framing for Emmys submissions.
23. **SAG-AFTRA Tilly Tax provisions** — the consent, compensation and residuals framework for digital-replica use, included in the 2026 four-year contract.
24. **Equity (UK) strike ballot outcome** — 99% vote authorising industrial action over AI provisions.
25. **PRS for Music AI Survey 2026** — UK music-creator sentiment baseline informing collective-licensing negotiations.
26. **GEMA ruling against OpenAI** — first European-rights-society legal precedent on AI training compensation.
27. **The 88% UK consultation outcome** — political mandate for licensing-by-default.
28. **The *Stealing Our Work Is Not Innovation* declaration** — 800-creator cultural marker.
29. **Bandcamp's outright AI-music ban** — distribution-platform-level disclosure-by-exclusion.
30. **Swedish Top Chart AI ban** — chart-eligibility-level disclosure.
31. **San Diego Comic-Con AI art ban** — convention-level disclosure-by-exclusion.

**Legal infrastructure protecting human identity:**

32. **Tennessee ELVIS Act** — the most-cited state-level AI-impersonation statute, used by the Johnny Cash estate in the Coca-Cola tribute-act case.
33. **New York's December 2025 AI-avatar disclosure law** — requires advertisers to disclose AI-performer use.
34. **The Taylor Swift voice-and-image trademark filings** (early 2026) — celebrity-led use of trademark mechanism for identity protection.
35. **The Jeremy Renner unauthorised-voice lawsuit** — pending case testing voice-likeness protections.
36. **The pending EU AI Act enforcement** — training-data-transparency requirements coming into effect through 2026.

Each of these, on its own, is a marginal piece. Stacked together — capture-signing, watermarking, platform integration, festival rules, awards rules, union contracts, civil society declarations, legal protections — they describe a *coherent infrastructure project* that the creative industries are, in eight months, jointly constructing.

The project is, by any reasonable assessment of similar previous infrastructure builds, *substantially ahead of schedule*. The C2PA standards body was founded in 2021 and was, by mid-2026, deployed across most major commercial capture and edit tooling. SynthID went from research demo in 2023 to consumer-facing detection in Gemini by January 2026. The SAG-AFTRA digital-replica provisions went from a 2023 strike demand to a contractual reality in 2026. The 88% went from political abstraction to government statement of progress in twelve months.

The thing this rate of progress tells me is *not* that the work is done. The work is, in many places, half-done — there are gaps in adversarial robustness, in platform UI integration, in cross-jurisdictional enforcement, in coverage of the long tail of creator categories outside the major commercial industries. The work is also being done unevenly: the music industry has built more of the stack than the games industry, which has built more than the publishing industry, which has built more than the regional and minority-language creative ecosystems that the next decade will need to bring in.

But the *trajectory* of the work is unambiguous. The provenance stack is being built. The institutional disclosure infrastructure is being built. The legal protections are being built. The audience contract I describe in the next section is being written. Working creatives who position themselves on the *inside* of this build — using the tools, contributing to the standards, showing up at the consultations, advocating with the unions, deploying provenance metadata in their own work as a default — will have, by 2030, materially more leverage than working creatives who waited for someone else to finish the project for them.

### What this means for the audience

I want to close the chapter with a thought about what this whole structure means for *the audience*, because most of this book has — by design — been about the people who *make* creative work, and the audience is sitting on the other side of the screen the whole time.

What I think the slop ceiling, the provenance infrastructure, the disclosure norms and the legal protections are, *collectively*, building is a *new contract* between makers and audiences.

The old contract was straightforward. The maker made the thing. The audience watched, listened, played, read. The signal of authenticity was implicit — most creative work was, by default, made by humans because there was no other way to make it.

The new contract is, by necessity, *explicit*. The maker discloses what was made by whom and how. The audience gets to make an informed choice. The platform, the union, the law and the institution all support both sides of the transaction.

If we get this contract right, the AI era is not the end of human creative work. It is a *renegotiation* of the terms on which human and synthetic creative work coexist in the public sphere — with the audience, for the first time in a very long time, getting a real seat at the table.

If we get it wrong — if the disclosure infrastructure fails, if the provenance metadata is unreliable, if the platforms refuse to honour the audience's stated preferences, if the legal protections are not enforced — what we get is the world the *Dead Internet* chapter described. A web of synthetic content, made by no one in particular, for no one in particular, churning past an audience that has lost the ability to trust any of it.

The choice between those two outcomes is *not, in 2026, a technical question.* The technical infrastructure for both is, by spring 2026, broadly in place. The choice between them is a *political, institutional and cultural* one. It is about whether the people who set the rules — the platforms, the legislators, the institutions, the studios, the audience itself — collectively decide that *knowable human authorship* is a public good worth protecting.

I think, on the evidence of the last six months, that the choice is being made — slowly, contentiously, imperfectly, but recognisably — in the right direction. The 88%, the Sundance literacy turn, the Cannes Disclosure Standard, the Academy's rule update, the SAG-AFTRA contract, the C2PA standards, the SynthID rollout, the audience's own attention behaviour: these all point the same way.

The question for the rest of this book — Chapter 13 on the organisational restructuring, Chapter 14 on the labour-market reshuffle, and Chapter 15 on the political choice — is what happens to the *organisations*, the *labour market* and the *economy* of creative work when authenticity is the scarce good and the orchestrator is the new role. The implications for how teams are structured, how labour is paid and how creative careers are built are bigger than any single tool launch, and they are what the next three chapters are about.

[^1]: [*Dream Machine* Issue 29](../Dream%20Machine%20MD/29.md) reportage of Tiny Grandma stop-motion content being wrongly flagged as AI by YouTube's automated detection, May 2026.

[^2]: [*Dream Machine* Issue 23](../Dream%20Machine%20MD/23.md), April 2026, reporting death threats against Eline Van der Velden following Tilly Norwood's continuing public role.

[^3]: *Digital Music News*, "Instagram Chief Says We Should 'Fingerprint Real Media' Instead of Tracking and Disclosing AI Slop." <https://www.digitalmusicnews.com/2026/01/05/instagram-chief-ai-slop-comments/>. *WebProNews*, "Instagram Head Warns AI Images Erode Trust, Calls for Verification Standards." <https://www.webpronews.com/instagram-head-warns-ai-images-erode-trust-calls-for-verification-standards/>. [*Dream Machine* Issue 13](../Dream%20Machine%20MD/13.md).

[^4]: *Digital Music News*, "AI-Generated Far-Right Hate Songs Aren't Just a Problem in the US — Now They're Spreading Across Europe Too." <https://www.digitalmusicnews.com/2025/11/09/ai-generated-hate-songs-dutch-spotify-charts/>. [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md).

[^5]: Google DeepMind SynthID watermark roll-out across Veo, Lyria and Imagen products. *Dream Machine* Issues [11](../Dream%20Machine%20MD/11.md), [12](../Dream%20Machine%20MD/12.md).

[^6]: Google DeepMind, "Verify Google AI-generated videos in the Gemini app." <https://www.linkedin.com/posts/googledeepmind_verify-google-ai-generated-videos-in-the-activity-7407748300688478208-fJgW>. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md); broader coverage in *SmartBrief*, "Google's Gemini can now spot AI-generated videos." <https://newsletter.smartbrief.com/sharedSummary/index.jsp?briefId=40A39351-5419-4681-94DF-31A53480B698&issueId=58E986AD-821F-422E-9E34-3386E0E2272B&copyId=2DB8E453-8E83-416C-949B-44751F252A8D>. [*Dream Machine* Issue 13](../Dream%20Machine%20MD/13.md).

[^7]: *Dream Machine* Issues [23](../Dream%20Machine%20MD/23.md), [27](../Dream%20Machine%20MD/27.md) reportage on Taylor Swift's voice/image trademark filings.

[^8]: *Lawyer Monthly*, "Matthew McConaughey Draws a Line to Protect His Voice and Image From AI." <https://www.lawyer-monthly.com/2026/01/matthew-mcconaughey-protects-voice-image-ai/>. [*Dream Machine* Issue 15](../Dream%20Machine%20MD/15.md).

[^9]: *Adweek*, "Meet the $1.3 Billion Startup Behind Madonna and Will Smith's AI Video." <https://www.adweek.com/media/higgsfield-ai-marketing-startup/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^10]: Variety, "George Clooney Says AI Actors Will Face the 'Same Problem We Have' in Hollywood: 'Making a Star Is Not So Easy'." <https://variety.com/2025/scene/columns/george-clooney-ai-actors-movie-stars-1236579661/>. [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md).

[^11]: *Deadline*, "AI Documentary Director Insists Jeremy Renner Agreed To Narrate Movie As 'Hawkeye' Star Threatens 'Multi-Millions' Lawsuit." <https://deadline.com/2025/11/jeremy-renner-lawsuit-threat-ai-movie-1236611830/>. [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md).

[^12]: *Complete Music Update*, "Johnny Cash estate uses ELVIS Act to sue Coke over tribute act ad soundtrack." <https://completemusicupdate.com/johnny-cash-estate-uses-elvis-act-to-sue-coke-over-tribute-act-ad-soundtrack/>. [*Dream Machine* Issue 9](../Dream%20Machine%20MD/9.md).

[^13]: *The Verge*, "New York's new law forces advertisers to say when they're using AI avatars." <https://www.theverge.com/news/842848/new-york-law-ai-advertisements-sag-aftra-labor>. [*Dream Machine* Issue 11](../Dream%20Machine%20MD/11.md).

[^14]: *Fast Company*, "Governments around the world are considering bans on Grok's app over AI sexual image scandal." <https://www.fastcompany.com/91474131/governments-around-the-world-are-considering-bans-on-groks-app-over-ai-sexual-image-scandal>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^15]: Cannes AI Disclosure Standard, launched May 2026. [*Dream Machine* Issue 29](../Dream%20Machine%20MD/29.md).

[^16]: [*Dream Machine* Issue 28](../Dream%20Machine%20MD/28.md), May 2026, reporting on the Academy of Motion Picture Arts and Sciences' "You must be human to win" rule update.

[^17]: *The Hollywood Reporter*, "Emmys Set AI Guidance." <https://www.hollywoodreporter.com/tv/tv-news/emmys-ai-guidelines-2026-awards-1236468434/>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^18]: SAG-AFTRA negotiation timeline through *Dream Machine* Issues [7](../Dream%20Machine%20MD/7.md), [12](../Dream%20Machine%20MD/12.md), [15](../Dream%20Machine%20MD/15.md), [20](../Dream%20Machine%20MD/20.md), [26](../Dream%20Machine%20MD/26.md), [29](../Dream%20Machine%20MD/29.md).

[^19]: *Marketing Week*, "You can't dismiss AI ads as slop when they're winning in testing." <https://www.marketingweek.com/dismiss-ai-ads-winning-creative-effectiveness/>. *Dream Machine* Issues [8](../Dream%20Machine%20MD/8.md), [13](../Dream%20Machine%20MD/13.md).

[^20]: Variety, "AI Creator Behind Viral 'Deadpool,' 'Harry Potter' Christmas Clip Made His Film in a Ukrainian Bomb Shelter." *op. cit.* [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^21]: PR Newswire, "From Apple TV Creative to AI Filmmaker: Hoyt Dwyer's Animated Film To Compete at AI FilmFest Japan 2025." *op. cit.* [*Dream Machine* Issue 6](../Dream%20Machine%20MD/6.md).

[^22]: Google DeepMind, "Dear Upstairs Neighbors." <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/dear-upstairs-neighbors/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^23]: *The Hollywood Reporter*, "'Synthetic Sincerity' by Marc Isaacs." *op. cit.* [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^24]: Variety, "'Watch the Skies,' Swedish UFO Feature Film Dubbed Entirely With AI, Sets USA Distribution Deal." *op. cit.* [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^25]: *Broadcast Pro Middle East*, "Tunisian filmmaker wins $1 million AI Film Award for 'Lily'." *op. cit.* [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^26]: Sundance Institute AI Literacy Initiative emphasis on documentation: <https://www.sundance.org/blogs/centering-the-artist-why-were-launching-the-ai-literacy-initiative/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).
