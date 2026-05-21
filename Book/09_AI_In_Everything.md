# Chapter 9

## AI in Everything, Everywhere, All at Once

In late October 2025, at Adobe MAX, the company that has made the software almost everyone in the creative industries uses every day — Photoshop, Illustrator, Premiere, After Effects, InDesign — decided that the year-old marketing line *"AI is a feature in our tools"* had outlived its usefulness, and replaced it with a more honest one.

The new line was: **"AI in everything, everywhere, all at once."**[^1]

The reason I want to spend a chapter on that phrase is not because I love a slogan. The reason I want to spend a chapter on it is that I think it is, more than any other single piece of corporate positioning from the period this book covers, *literally* true. AI is in everything now. It is in every layer of the creative software stack. And the implications of that for working creatives — for the way we are trained, the way we are paid, the way we work with each other — are not yet, in the spring of 2026, fully understood.

This chapter is about the platform layer. About the companies that make the tools that the rest of the creative industries use to make the work. About how those companies have, in the past eight months, accepted that their business is no longer making *tools* but making *agents,* and about what that means for the rest of us.

### The Adobe MAX week

The Adobe MAX 2025 keynote — held in mid-October in Los Angeles, the week after OpenAI's DevDay, two weeks after Tilly Norwood — was unusual, by Adobe's standards, in how much it tried to land at once.

The headline products were Firefly Foundry, a service for companies to train their own custom generative models on their own visual identity;[^2] Firefly Image Model 5, the latest generation of the image generator that has, since 2023, been Adobe's primary public answer to Midjourney and Stable Diffusion;[^3] and an AI Assistant built directly into Adobe Express, the company's lower-barrier consumer creative tool.[^4]

Underneath the headlines was a much longer list of "Project" announcements — Adobe's research-preview format, the things that may or may not ship but that signal what the company is investing in. The list, looked at as a whole, is what convinced me, sitting at my desk in the North West watching the live stream, that something larger than a product launch was happening:

**Project Scene It**: image-to-3D and 3D-to-image technologies, with reference-image tagging for object preservation in 3D space.

**Project Surface Swap**: AI-powered material recognition, letting designers swap textures while preserving lighting, shading and perspective.

**Project Turn Style**: editing 2D objects as if they were 3D.

**Project Trace Erase**: removing objects *and* their shadows, reflections and environmental distortions in one operation.

**Project New Depths**: editing depth in an image as easily as adjusting brightness.

**Project Frame Forward**: applying changes across entire videos based on one annotated frame and a text prompt — "the precision of photo editing in video workflows."

**Project Motion Map**: bringing static vector graphics to life automatically.

**Project Sound Stager**: analysing a video's visuals, pacing and emotional tone, and automatically generating layered soundscapes.

**Project Clean Take**: AI correction of mispronunciations, voice isolation, noise removal and delivery refinement.

**Project Graph**: a node-based workflow editor, conceptually similar to ComfyUI, for chaining Adobe's tools and models into custom pipelines.[^5]

There is, in that list of ten projects, *every* layer of the post-production stack — image, video, 3D, audio, layout, workflow — being re-imagined as a generative or agentic operation. Not a tool with an AI feature stapled on. A *generative-first reimagining of the operation itself.*

The Adobe MAX week was, to put it plainly, Adobe's announcement that it was rebuilding its product from the inside.

### What "AI in everything" actually means

The reason I want to be careful with the Adobe-MAX framing is that, six months on, you can see how literally the company has executed against it.

In December 2025, Adobe announced that Photoshop, Express and Acrobat editing would be available *inside* ChatGPT — meaning the creative output was no longer happening inside Adobe's interface, but inside an AI agent's.[^6] In January 2026, the Premiere Object Mask tool — an AI-driven masking feature that automated one of the most laborious tasks in video editing — quietly became available to Premiere users.[^7] In late January, at Sundance, Adobe launched the *Adobe Film & TV Fund* and *Ignite Day*, with explicit support for filmmakers integrating AI into their workflows.[^8] In April 2026, at the **Adobe Summit**, the company introduced its **CX Enterprise** platform alongside NVIDIA — a stack of AI agents embedded across the entire content lifecycle from brief to delivery — under the framing "agentic creative intelligence is now."[^9]

The trajectory, in one sentence: Adobe in 2024 was a *creative tool company.* Adobe in 2026 is an *AI-agent platform company* that happens to also still ship Photoshop.

If you are wondering whether this transition has been smooth: it has not. The reception of the Adobe AI announcements among working creatives has been, in my own circles and the readers' WhatsApp group the *Dream Machine* community runs, sharply ambivalent. There is real appreciation for the productivity gains. There is real anxiety about the implications for craft, for licensing, for control, for the trajectory of the company's relationship with the creators who pay for it.

What no working creative I know thinks is that this transition is reversible. Once Photoshop has an AI assistant baked in, once Premiere has Object Mask, once After Effects has the AI-powered animation tools that landed in November 2025,[^10] the *next* version of every Adobe product is going to have *more* of this, not less. Adobe's *competitors* are, if anything, going faster. If Adobe slows down, somebody else lands the punch.

This is — I think this is the part that working creatives have to understand and internalise — *the new physics of the toolchain.* AI is not a feature that one tool company decided to ship. It is a structural property of the toolchain itself in 2026, and the question for anyone using that toolchain is not whether to integrate AI but *how to integrate it deliberately,* with eyes open, on terms that preserve the human craft underneath.

### The platform alliance

Adobe is not — and this is the more important observation — the only company doing this.

In March 2026, [*Dream Machine* Issue 21](../Dream%20Machine%20MD/21.md) led with what I have called, in talks since, the most consequential business announcement of the year: **Adobe + NVIDIA** entered a strategic partnership that explicitly framed creative AI as *enterprise infrastructure* rather than viral consumer tooling.[^11] The partnership covered next-generation Firefly models, agentic creative-and-marketing workflows, and production-pipeline integration. The language was telling: *precision and control* for creativity and marketing pipelines, alongside content, campaign and production speed.

The reason this is consequential — beyond the size of the two companies involved — is that it signals the *maturation* of the market. Adobe + NVIDIA is not a race-to-the-cool-demo deal. It is a *race-to-the-procurement-line* deal. The two companies are betting, jointly, that the next era of creative AI is going to be won by whoever ships the most reliable, most controllable, most legally-defensible production-grade tooling to the enterprise creative buyers — the studios, the agencies, the broadcasters, the brand teams.

The same week, **Google** and **NVIDIA** announced a parallel deal for cloud-based generative-AI infrastructure aimed at the same enterprise market.[^12] **Hugging Face** and **Google Cloud** announced a partnership in November 2025 covering open-source agentic development.[^13] **Meta** and **Hugging Face** launched **OpenEnv** in October 2025 to advance open-source agentic development.[^14] **Anthropic** signed a corporate-patronage deal with the **Blender Foundation** in May 2026.[^15] **Anthropic** also acquired into the **Slack** workplace-tooling ecosystem with Claude Apps in January 2026,[^16] and reached an ad-sales partnership with **Spotify** to put music recommendations inside Claude.[^17] In May 2026 **Splice** signed a "Responsible AI" deal with **ElevenLabs** covering sample-library training and consented voice synthesis;[^46] **Netflix** announced an agentic ad-tools roadmap whose internal framing — *"agentic AIs talking to each other"* — was an unusually candid description of where the advertising-orchestration layer is heading;[^47] and the AI-coworker startup **Viktor** raised $75M to embed an agentic colleague directly into Slack and Teams,[^48] reinforcing the pattern that the platform-layer agents are landing where the working creative already lives.

The advertising holding companies were moving at the same pace. **WPP** signed a $400m partnership with Google in October 2025.[^18] **WPP Open Pro**, a new edition of the agency's AI marketing platform, launched the same month with a framing that should be read carefully by anyone working in adland: *"While some companies hide their AI behind service teams or focus on just one part of the journey, WPP Open Pro is an integrated solution for campaign implementation, built to deliver outcomes, not just assets."*[^19] *Outcomes, not just assets.* That is the position of a holding company that has decided AI is not a feature — it is the entire reason a brand should buy from them in 2026. **WPP** then expanded its AI capabilities through a partnership with **Sightly** in November 2025.[^20] By April 2026, WPP was using Google Earth's AI tools to map consumer journeys at scale.[^21]

The pattern is unmistakable. The platform layer — the toolmakers, the infrastructure companies, the agencies, the cloud providers — has been quietly consolidating around a small number of strategic alliances that, taken together, are deciding the *rails* on which creative work will run for the next decade.

If you are a working creative reading this, you are probably already running some part of your workflow on rails laid by one of these alliances. By 2028, you will, almost certainly, be running *most* of your workflow on those rails — or on a deliberate, principled alternative that has chosen to opt out.

### Google I/O 2026: the second platform-layer moment

If Adobe MAX 2025 was the platform-layer announcement of the first half of this book, **Google I/O 2026** — held in the week this book went to press — was the announcement that closed it. The two events bookend the eight-month window the manuscript covers, and the symmetry of their framings is, on the platform-economics read, instructive.

The headline announcements were **Gemini Omni**, a unified multimodal model designed to work across text, image, audio, video and live interaction in a single workflow; **Antigravity**, Google's agentic coding and development environment; **Google Flow**, the agent-based workflow product that allows AI systems to take on multi-step creative and production tasks autonomously; **Gemini Spark**, the new developer toolkit aimed at building autonomous agents and AI-powered applications; and **Project Genie + Street View**, an integration that allows users to generate navigable simulations of real-world locations from the Street View map data — a topic I return to at length in [Chapter 8](08_Worlds_Not_Pictures.md).[^42] The keynote opened, deliberately, with a browser-based multiplayer demo called **Infinite Scaler** — thousands of players competing inside vertically generated levels created on the fly from player prompts — a piece of theatre that, like *Tilly Norwood* a year earlier, was less interesting for the product than for the framing it imposed on the event that followed: AI-generated worlds, live procedural experiences, mass participatory systems that evolve in real time.[^43] **SynthID**, Google's content-provenance watermarking technology, was announced as having marked over 100 billion items by May 2026, and as being extended to partner ecosystems including OpenAI, ElevenLabs and Kakao — a development I cover in detail in [Chapter 12](12_Authenticity_New_Scarcity.md).[^44]

The reason to draw the Adobe MAX / Google I/O parallel directly is that the *structural shape* of the two announcement weeks was identical. Both keynotes argued that AI was no longer a feature to be added to existing products; it was the *operating layer* into which the existing products would be re-built. Both keynotes pre-positioned the company's product roadmap around *agents* rather than tools. Both keynotes were aimed not at the consumer-keynote crowd but at the procurement teams of the enterprise creative buyers. The fact that the same framing arrived from the two largest creative-software and creative-platform companies in the world, eight months apart, in the same eight-month window, is the cleanest single confirmation I have that *the AI-in-everything thesis is the platform layer's settled commercial strategy* for the rest of the decade.

For working creatives, the operational implication is direct. The platform layer has decided. The question is no longer whether the creative software stack will be re-built around AI agents. It is which agents, on whose terms, with what provenance, on which commercial settlement.

### The new entrants

Underneath the platform giants, a separate layer of companies has been building the *consumer-facing AI creative tools* that, in some markets, are turning into bigger businesses faster than anyone expected.

**Higgsfield**, the AI video startup focused on social-media marketers, raised $80m at a $1.3bn valuation in January 2026.[^22] Three months later — in a stat that I have read repeatedly to check that I have not got it wrong — Higgsfield was reported to have earned $200m in nine months of operations.[^23] An AI-video startup, less than two years old, was running at a quarter-billion-dollar annual run-rate by the spring of 2026.

**Synthesia**, the U.K.-based AI-avatar platform, hit a $4bn valuation in January 2026 and let its employees cash in.[^24] In October 2025 it had reportedly *rejected* a $3bn acquisition offer from Adobe — choosing to remain independent.[^25]

**ElevenLabs**, the audio-AI company, was reported to have crossed $500m in annualised revenue by April 2026, raising from BlackRock, NVIDIA, Jamie Foxx and Eva Longoria.[^26]

**Runway** released Gen-4.5 in December 2025 and Gen-4.5 Image-to-Video in January 2026, then a "Workflows" product across all paid plans, then a Story Panels app, then a Characters API, then Apps for Advertising — and by spring 2026 was making the public case that AI could enable "50 indie films" instead of "one $100M blockbuster."[^27] In May 2026 the company opened a Tokyo office on a $40M commitment, marking its first material expansion into the Asia-Pacific creative-AI market.[^45]

**Krea**, **Freepik**, **Magnific**, **Heygen**, **Hedra**, **Cascadeur**, **Hunyuan**, **Kling**, **Suno**, **Udio**, **Mureka**, **Hitem3D**, **Meshy**, **Rodin** — the list of consumer-grade AI creative tools that crossed material commercial scale in this period is too long to fully enumerate, and the *Dream Machine* archive carries them week by week.[^28] The category that didn't exist in 2023 is now an industry with multiple unicorns, multiple billion-dollar valuations and meaningful real revenue.

**ComfyUI**, the open-source node-based workflow tool that has become a quiet standard for technical AI users, raised $17m in October 2025[^29] and hit a $500m valuation by May 2026.[^30] What the ComfyUI valuation tells you, more than any of the big-platform numbers, is that the market is also paying — at significant scale — for tools that give *creators control* over the AI process rather than abstracting it away.

### The free tier and the literacy tier

Two things happened in the consumer-platform layer that I think have been under-discussed and that matter a lot for what the next creative economy will look like.

The first is that the **base layer of AI capability went free**, in a meaningful sense, in the autumn of 2025. **Google** released its **Pomelli** marketing AI agent for free in October.[^31] **Google AI Studio**, **Opal** (the no-code AI mini-app builder), and the Project Genie prototype were all released as free or near-free tiers through early 2026.[^32] **Lovable** made its product free for teachers and students in classrooms.[^33] **Adobe Express's** AI Assistant arrived inside the free tier of Adobe's already-free consumer product.[^34] **Hugging Face** continued to expand its free hosting and open-source model distribution.[^35] **Krea**, **Freepik**, and many of the larger tool platforms kept generous free tiers as a customer-acquisition lever.

What this means, practically, is that the entry-level for AI-enabled creative work in 2026 is *near zero.* A teenager with a phone and a free Google account can, today, generate video, music, 3D objects and (with Project Genie) navigable interactive worlds at a quality bar that, two years ago, required a small production company to produce.

This is, in absolute terms, a democratisation. It is also — and this is the second thing — *creating a literacy gap* between the people who know how to use these tools well and the people who don't.

Adobe responded to this gap, in late 2025 and through 2026, by becoming — in addition to a software company — *a training organisation.* The Sundance partnership, with a $2M investment to teach 100,000 filmmakers AI skills.[^36] The Ignite Day, focused on emerging creators.[^37] The Adobe Film & TV Fund. The Adobe Express AI Assistant tutorials. Google made the same bet in parallel, putting $40bn into Anthropic in May 2026 in a deal widely interpreted as betting on the literacy and infrastructure layer of the next decade.[^38]

The UK government picked the same direction. In January 2026, the Department for Science, Innovation and Technology announced *Free AI training for all*, expanding a government-and-industry programme to provide 10 million UK workers with AI skills by 2030.[^39] The Department for Business and Trade research, reported in [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md), found that *neurodiverse workers* were 25% more satisfied with AI assistants — suggesting that AI's productivity benefits in certain workflows could "potentially help to level the playing field."[^40] The University of Wisconsin-Stout set AI-use as a baseline competency in its filmmaking course in January 2026.[^41]

What the consumer-platform companies and the policy-makers are, jointly, building is a *training infrastructure* for the new toolchain. The reason they are doing this is straightforward: a tool you cannot use is a tool you do not buy, and a worker who cannot use the new tool is a worker who eventually exits the workforce. Both incentives push in the direction of mass AI literacy as a public investment.

What I find encouraging about this — and I am genuinely encouraged, against the grain of much of the cultural commentary — is that the literacy push is being framed, both by Adobe at Sundance and by the UK government, as *creator empowerment* rather than worker replacement. The proposition is not *learn AI or be replaced by it.* The proposition is *learn AI to remain in the driver's seat of your own work.* That framing matters. It is the right framing. It is the only framing under which the AI-literacy push doesn't become a way of accelerating the very problems it is supposed to fix.

### The platform economics underneath the slogan

I want to spend a section on the *commercial* shape of the platform layer, because the "AI in everything" framing has economic implications that the keynotes have been careful not to name, and that working creatives buying platform access at scale need to understand.

The shape, simplified, is this. The dominant generative-AI platforms — OpenAI, Anthropic, Google DeepMind, Adobe, Runway, ElevenLabs and the rest — operate as *infrastructure-as-a-service* businesses on top of *capital-intensive* underlying compute. The marginal cost of producing one more generated image, song or video clip is, at the platform level, low. The fixed cost of the compute infrastructure required to produce *any* generated output at competitive quality is, at the platform level, very high — the data-centre build, the chip supply, the energy contract, the model-training spend.

This produces, structurally, a *natural-monopoly-tending* market. The platform with the largest compute base produces the lowest marginal cost per output, captures the largest user base, generates the largest revenue, and reinvests in a larger compute base. The flywheel is the standard cloud-services flywheel, accelerated by the AI-specific dynamics of training-data flywheels and user-feedback flywheels.

The 2025–26 financial telemetry, where the platform companies have disclosed it or been required to disclose it, supports the natural-monopoly read.

OpenAI was reported, through late 2025 and into 2026, to be operating at *significantly negative cash flow* at the unit-economics level despite its 800–900M weekly active users. The company's reported revenue, which crossed the $10 billion annual run-rate mark in late 2025, was — by every analyst breakdown I have seen — being substantially exceeded by infrastructure costs (data-centre lease, chip supply, energy, training compute). The Microsoft partnership at the financial level was, structurally, a *capital-supply* relationship rather than a *technology-licensing* one: Microsoft providing the compute capacity that OpenAI could not, by itself, finance.

Anthropic, in 2026, was reported to be operating with similar structural dynamics, with Google and Amazon as its capital-supply partners. The Anthropic Foundation patronage deal with the Blender Development Fund — announced in May 2026 and discussed in [Chapter 16](16_The_Tools.md) — is interesting precisely because it suggests Anthropic has, alongside the closed-platform business, *strategic interest* in supporting the open-source creative-AI infrastructure that the closed-platform model competes with. That kind of two-handed positioning is, in natural-monopoly markets, often the precursor to a *platform regulation* settlement.

Adobe, by contrast, operates with the most *defensible* business model in the creative-AI platform space, because it is selling AI as a feature of an existing subscription rather than as a per-use service. Firefly's contribution to Adobe's 2024 annual recurring revenue — 11% of new ARR, on the company's own published numbers — is being generated *without* the per-token unit-economics problem that OpenAI and Anthropic face, because Adobe is bundling the AI into the existing $54.99-a-month Creative Cloud all-apps subscription. The customer's behaviour change from no-AI to AI doesn't change the revenue line. It changes the *value capture* of the existing revenue line. This is, in business-school terms, the platform's *strongest* possible defensive position. It is also the reason Adobe's stock performed differently from the rest of the AI-platform cohort through 2025–26.

Runway, ElevenLabs and the AI-native specialist platforms operate with a per-use unit-economics structure that more closely resembles OpenAI's. The differentiation, where they have it, is in *workflow integration* — Runway's Workflows product, ElevenLabs' Flows canvas, the studio-tier features that lock professional users into per-platform tooling. The strategic question for each of these companies, in the next two years, is whether they can build defensible workflow lock-in before the natural-monopoly dynamic of the underlying foundation-model market consolidates the foundation-model layer down to two or three players.

The implications for working creatives buying platform access at scale, in 2026 and beyond:

*One,* the per-token / per-output prices working creatives are paying for AI tooling in 2026 are, on every analyst read I have seen, *materially subsidised by platform-company investor capital*. The unit economics underneath the prices are not, today, sustainable at the volumes the platforms are producing. The prices are, by structural inference, going *up* over the medium term as the platforms work toward unit-economic break-even. The working creative who builds a business model assuming today's per-token costs as a stable input is, on the platform-economics read, taking a bet that the platforms cannot win. *Pricing today is not pricing forever.* This is the part of the platform-dependency argument the *open-the-black-box* discussion in [Chapter 3](03_The_Human_AI_Agency_Continuum.md) most directly relies on.

*Two,* the *strategic-rent-extraction* potential of the eventual platform-monopoly position is the structural risk underneath the entire orchestrator economy I described in [Chapter 11](11_The_Orchestrator.md). If two foundation-model platforms dominate the underlying generative-AI capacity by 2030, and every working creative's production pipeline depends on access to one or both of them, the platforms will be in the position the cable companies were in by 2010 and the social-media platforms were in by 2015 — able to extract value from the working creators who depend on them at prices the creators have no real ability to negotiate. The Petrillo-template solution to this is *collective bargaining* by working creatives and their unions against the platform companies as a class. The early architecture of this — the Cannes Disclosure Standard, the SAG-AFTRA platform negotiations, the EU AI Act enforcement, the UK 88% — is in place. The substance of it is, in mid-2026, still mostly aspirational.

*Three,* the *open-source alternative* layer documented in [Chapter 16](16_The_Tools.md) is, on this structural read, *the working creative's principal long-term insurance policy* against platform-monopoly pricing. The 80% of YC and a16z startups now building on open-weight models — Hunyuan, Wan, Qwen, FLUX, DeepSeek, the various Mistral variants — is, in market-economics terms, *the credible-walk-to-alternative* that constrains the closed-platform companies' pricing power. The working creative who has familiarised themselves with open-weight tooling, even if they default to closed-platform tooling for most of their daily work, has a *strategic option* the working creative who has not has surrendered. The option is worth money. It is also, on the historical pattern, worth political leverage in the institutional negotiations that the next decade of platform-rule-writing will run on.

The "AI in everything" framing, in operational summary, *is the platform companies' commercial strategy described in marketing language*. The strategy is to make AI a default productivity feature of every creative workflow, on platform-controlled tooling, at prices that the platforms can adjust over time once the workflow lock-in is in place. The strategy is, on the historical pattern of every previous platform-economics moment, going to produce a settlement somewhere between *the most-extractive version of the strategy* and *the most-constrained version of the strategy*. The 88%, the SAG-AFTRA contract, the EU AI Act, the C2PA standards body, the open-source ecosystem, and the working-creative collective-bargaining infrastructure are the constraints. The platform companies' compute capital, distribution leverage, and product-design control are the extractive forces. The settlement will be wherever those forces balance.

### What we lost

I want to close this chapter with the harder question, because the "AI in everything" framing has a cost that the platform-company keynotes are not, on the whole, eager to discuss.

What we lost, in the transition to AI-in-everything tools, is *the deliberate friction of the old creative process.* The thing that made Photoshop, for many of its early users, a profound creative tool was not just what it could do. It was that it required you to know it. The interface was a discipline. The keyboard shortcuts were a vocabulary. The layers, the masks, the channels, the curves, the colour pickers — they were the language of a craft, and learning the language was part of becoming the craftsperson.

When the layer of mastery moves from the toolchain to the prompt, the *barrier* of mastery drops to near zero. That is the democratisation we have been promised, and it is real.

What goes with the barrier, though, is the *depth of relationship* between the maker and the tool. The Photoshop user of 2015 knew the tool the way a guitar player knows a guitar — with their hands, with their body, with a relationship built up over years of repeated, embodied practice. The prompt-driven AI tool user of 2026 has a different relationship. It is more like the relationship of a director to a department head: you describe the result, the department head executes, you adjust by giving notes.

The motion designer Doug McGinness, posting on LinkedIn about the new AI-augmented After Effects workflow in late 2025, summarised the current state of the tooling in a single, ruefully accurate line that became a small private meme inside my studio: *"export → prompt → pray → import."*[^10a] The line is funny because it's true. The current generation of AI-tooled creative work is, for a substantial portion of every day, an exercise in *committing to a black-box operation and accepting whatever comes back.* That is, structurally, a different kind of creative discipline than the deterministic-tool craft it is replacing.

Neither relationship is *better* than the other. They are different relationships, and they produce different kinds of practitioners. But the *transition* is real, and one of the consequences — which I have seen up close, watching young creatives come through the studio — is that the *cognitive engagement* with the medium is structurally less deep than it used to be. The maker is one further step removed from the material.

This is not, by itself, a tragedy. The cinema director is one step removed from the film stock and is still, recognisably, the author of the film. The composer is one step removed from the violin and is still, recognisably, the composer. The novelist who uses a word processor is one step removed from the page and is still, recognisably, a writer.

But it is a *change*, and it is one we are pretending not to notice. The new toolchain is not just faster than the old toolchain. It is also a different kind of relationship with the work, and the people who will be its best practitioners — the ones who will, in 2030 and 2035, be doing the AI-era equivalent of what Greg Lynn did with parametric architecture or what Bjork did with synthesisers — will be the people who *consciously cultivate* the depth of relationship that the toolchain no longer enforces.

The platform companies are not going to teach you to do this. They have no incentive to. They benefit from your dependency, not your mastery. The new toolchain is *frictionless,* and frictionless tools, however much we benefit from their efficiency, are not, on their own, going to produce the next generation of great creative work.

That work is going to come from the people who put the friction *back in,* deliberately, on their own terms — who treat the AI agent as a junior colleague rather than as an oracle, who insist on *understanding* what their tools are doing rather than just *using* them, and who maintain the cognitive engagement with the work that the tools have been designed to make optional.

In the next chapter, I want to talk about the people who are doing exactly that. The orchestrators.

[^1]: *Creative Boom*, "Adobe is putting AI in everything everywhere all at once." <https://www.creativeboom.com/news/adobe-is-putting-ai-in-everything-everywhere-all-at-once/>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md), "Editor's Pick," 31 October 2025.

[^2]: Adobe, "Adobe MAX 2025: Firefly Foundry." <https://news.adobe.com/news/2025/10/adobe-max-2025-firefly-foundry>.

[^3]: Adobe, "Adobe MAX 2025: Firefly." <https://news.adobe.com/news/2025/10/adobe-max-2025-firefly>.

[^4]: Adobe, "Adobe MAX 2025: Express AI Assistant." <https://news.adobe.com/news/2025/10/adobe-max-2025-express-ai-assistant>.

[^5]: *Wired*, "Adobe's 'Corrective AI' Can Change the Emotions of a Voice-Over" and accompanying Adobe Sneaks 2025 coverage. <https://www.wired.com/story/adobe-max-sneaks-2025-corrective-ai/>. Project list compiled from MAX keynote and [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md) coverage.

[^6]: *PYMNTS*, "Adobe Lets Users Design and Edit Using ChatGPT." <https://www.pymnts.com/artificial-intelligence-2/2025/adobe-lets-users-design-and-edit-using-chatgpt/>. Adobe blog: "Edit images, designs, and PDFs right inside ChatGPT." <https://blog.adobe.com/en/publish/2025/12/10/edit-photoshop-chatgpt>. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md).

[^7]: Adobe Premiere Object Mask tool: <https://www.linkedin.com/posts/robdewinter_ok-this-is-going-to-save-a-lot-of-time-in-ugcPost-7421617551690063872-yKmB>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^8]: Adobe blog, "Sundance Film Festival 2026: Creativity, Community & Power of Storytelling." <https://blog.adobe.com/en/publish/2026/01/20/sundance-film-festival-2026-creativity-community-power-storytelling>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^9]: Adobe Summit 2026, "agentic creative intelligence" keynote. [*Dream Machine* Issue 26](../Dream%20Machine%20MD/26.md).

[^10]: After Effects AI animation features through late 2025: [*Dream Machine* Issue 9](../Dream%20Machine%20MD/9.md), "AI video is finally animatable inside After Effects." <https://www.linkedin.com/posts/thisisdoug_ai-aivideo-animation-ugcPost-7399512745924067330-Aldk>.

[^10a]: Doug McGinness on LinkedIn, late 2025, in the same post. [*Dream Machine* Issue 9](../Dream%20Machine%20MD/9.md).

[^11]: [*Dream Machine* Issue 21](../Dream%20Machine%20MD/21.md), "Editor's Pick: Adobe and NVIDIA Just Raised the Stakes for Creative AI," 19 March 2026.

[^12]: NVIDIA + Google Cloud creative-AI infrastructure deal, March 2026. [*Dream Machine* Issue 21](../Dream%20Machine%20MD/21.md).

[^13]: Hugging Face and Google Cloud partnership announcement: <https://www.linkedin.com/posts/julienchaumond_i-am-super-excited-to-announce-that-hugging-activity-7396177403972276225-CuMM>. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^14]: *EdTech Innovation Hub*, "Meta and Hugging Face launch OpenEnv to advance open-source agentic development." <https://www.edtechinnovationhub.com/news/meta-and-hugging-face-launch-openenv-to-advance-open-source-agentic-development>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^15]: Anthropic / Blender Foundation patronage, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^16]: TechCrunch, "Anthropic launches interactive Claude apps, including Slack and other workplace tools." <https://techcrunch.com/2026/01/26/anthropic-launches-interactive-claude-apps-including-slack-and-other-workplace-tools/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^17]: Spotify–Anthropic integration, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^18]: *MarTech Series*, "WPP continues AI overhaul with $400-million Google partnership." <https://martechseries.com/predictive-ai/ai-platforms-machine-learning/google-and-spotify-alum-launch-epiminds-with-6-6m-to-build-marketing-teams-for-the-ai-era/>. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md).

[^19]: *Campaign Brief*, "WPP launches AI-powered marketing platform WPP Open Pro." <https://campaignbrief.com/wpp-launches-ai-powered-marketing-platform-wpp-open-pro/>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^20]: *Digiday*, "WPP expands AI capabilities to boost brand performance with Sightly partnership." <https://digiday.com/media-buying/agencies-continue-to-expand-ai-capabilities-to-boost-brand-performance/>. [*Dream Machine* Issue 6](../Dream%20Machine%20MD/6.md).

[^21]: WPP and Google Earth AI consumer-journey project, April 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^22]: *SiliconAngle*, "Higgsfield raises $80M on $1.3B valuation to scale AI video platform." <https://siliconangle.com/2026/01/15/higgsfield-raises-80m-1-3b-valuation-scale-ai-video-platform/>. [*Dream Machine* Issue 15](../Dream%20Machine%20MD/15.md).

[^23]: *36kr*, "AI Video Unicorn Higgsfield: Earns $200M in 9 Months by 'Serving' Social Media Marketers." <https://eu.36kr.com/en/p/3650517574312323>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^24]: TechCrunch, "Synthesia hits $4B valuation, lets employees cash in." <https://techcrunch.com/2026/01/26/synthesia-hits-4b-valuation-lets-employees-cash-in/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^25]: *Sifted*, "Synthesia rejects $3bn Adobe acquisition offer." <https://sifted.eu/articles/synthesia-acquisition-offer>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^26]: ElevenLabs $500m ARR reporting, April 2026. [*Dream Machine* Issue 25](../Dream%20Machine%20MD/25.md).

[^27]: Runway product cycle: Gen-4.5 (December 2025), Gen-4.5 Image-to-Video (January 2026), Workflows, Story Panels, Characters API, Apps for Advertising — *Dream Machine* Issues [10](../Dream%20Machine%20MD/10.md), [14](../Dream%20Machine%20MD/14.md), [15](../Dream%20Machine%20MD/15.md), [16](../Dream%20Machine%20MD/16.md), [20](../Dream%20Machine%20MD/20.md). Runway CEO on indie films vs. blockbusters: [*Dream Machine* Issue 26](../Dream%20Machine%20MD/26.md).

[^28]: For the running ledger of new creative-AI products through 2025–26, see *Dream Machine* Issues [1](../Dream%20Machine%20MD/1.md)–[30](../Dream%20Machine%20MD/30.md) archive.

[^29]: ComfyUI, "We raised $17 million to build an OS for Creative AI." <https://www.linkedin.com/posts/comfyui_we-raised-17-million-to-build-an-os-for-ugcPost-7373743341236236288-wkCc>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^30]: ComfyUI $500M valuation, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^31]: Google Pomelli launch: <https://x.com/GoogleLabs/status/1983204018567426312>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^32]: Google AI Studio app gallery: <https://x.com/GoogleAIStudio/status/1982121563785949255>. Google Labs Opal expansion: <https://blog.google/technology/google-labs/opal-expansion/>. Project Genie: <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/>. *Dream Machine* Issues [5](../Dream%20Machine%20MD/5.md), [17](../Dream%20Machine%20MD/17.md).

[^33]: Lovable for classrooms: <https://lovable.dev/classroom>. [*Dream Machine* Issue 11](../Dream%20Machine%20MD/11.md).

[^34]: Adobe Express AI Assistant: <https://news.adobe.com/news/2025/10/adobe-max-2025-express-ai-assistant>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^35]: Hugging Face platform expansion through 2025–26.

[^36]: Google blog, "Sundance Institute AI Education." <https://blog.google/company-news/outreach-and-initiatives/google-org/sundance-institute-ai-education/>. [*Dream Machine* Issue 15](../Dream%20Machine%20MD/15.md).

[^37]: Adobe Ignite Day at Sundance: *Adobe blog, Sundance Film Festival 2026.* <https://blog.adobe.com/en/publish/2026/01/20/sundance-film-festival-2026-creativity-community-power-storytelling>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^38]: Google's $40bn investment in Anthropic, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^39]: UK Government, "Free AI training for all." <https://www.gov.uk/government/news/free-ai-training-for-all-as-government-and-industry-programme-expands-to-provide-10-million-workers-with-key-ai-skills-by-2030>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^40]: *CNBC*, "People with ADHD, autism, dyslexia say AI agents are helping them succeed at work." <https://www.cnbc.com/2025/11/08/adhd-autism-dyslexia-jobs-careers-ai-agents-success.html>. [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md).

[^41]: University of Wisconsin-Stout, "AI Reshaping Industry: New UW-Stout Course Sets AI-Use as Baseline Competency in Filmmaking." <https://www.uwstout.edu/about-us/news-center/ai-reshaping-industry-new-uw-stout-course-sets-ai-use-baseline-competency-filmmaking>. [*Dream Machine* Issue 15](../Dream%20Machine%20MD/15.md).

[^42]: Google I/O 2026 announcement block: Gemini Omni <https://blog.google/technology/google-deepmind/gemini-omni/>, Antigravity <https://antigravity.google/>, Google Flow <https://flow.google/>, Gemini Spark <https://blog.google/technology/developers/gemini-spark/>, Project Genie + Street View <https://deepmind.google/discover/blog/project-genie-street-view/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md), "Editor's Pick — Google I/O 2026," 21 May 2026.

[^43]: Google Labs, "Infinite Scaler." <https://blog.google/technology/google-labs/infinite-scaler/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^44]: Google DeepMind, "SynthID — 100 billion watermarks, partner ecosystem." <https://deepmind.google/discover/blog/synthid-100-billion-watermarks-partners/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^45]: Runway, "Runway Japan." <https://runwayml.com/blog/runway-japan>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^46]: *Music Business Worldwide*, "Splice inks 'Responsible AI' deal with ElevenLabs." <https://www.musicbusinessworldwide.com/splice-elevenlabs-responsible-ai-deal/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^47]: *Adweek*, "Netflix ad tools could see 'agentic AIs talking to each other'." <https://www.adweek.com/media/netflix-ad-tools-agentic-ais-talking-to-each-other/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^48]: *Fortune*, "AI startup Viktor raises $75 million to put a virtual 'coworker' in Slack and Teams." <https://fortune.com/2026/05/19/ai-startup-viktor-75-million-virtual-coworker-slack-teams/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).
