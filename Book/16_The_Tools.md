# Chapter 16

## The Tools

I have, until this chapter, deliberately kept the *tools* out of the foreground. Thirteen chapters about creative AI without a chapter on the toolchain is, on the face of it, a strange editorial decision, and I want to begin by explaining it.

The reason is that I think the most common mistake people make about this period is to confuse *the tools* with *the transition*. Tools are the visible surface of the change — the thing the press cycle covers, the thing the platform companies want you to talk about, the thing that has a price and a logo and a launch date you can put on a slide. The transition is everything underneath: the economics, the labour, the audience contract, the law, the institutions, the rails. The tools change weekly. The transition is slower, deeper, and is what will still be true in 2030 when most of the tools in this chapter are obsolete.

The first sixteen chapters were about the transition. This chapter is about the tools.

I have written it last on purpose. Read in this order, the tools sit inside the architecture the book has been building — the Continuum, the Slop Ceiling, the four positions, the orchestrator role, the four principles. Read in any other order, they collapse back into the format the platform companies prefer: a tools-arms-race in which the only question is which model is best this week.

That format is, in 2026, the most reliable way to misunderstand what is happening.

A note on the date stamp. Everything in this chapter is current to May 2026. By the time you read it, some of these tools will have been bought, renamed, killed, surpassed or repositioned. The point is not that the specific tools matter. The point is the *shape* of the toolchain — what categories exist, what they do, who builds them, and how a working creative builds a coherent stack on top of them. The shape, in my experience, holds.

### How to think about the toolchain

Before the inventory, the frame.

I think the creative-AI toolchain in 2026 is best understood as a stack of seven layers, each with its own dominant players, its own pace of change, its own integration model. The layers, from foundation to consumer, are:

1. **Foundation models** — the large multimodal systems underneath everything else (OpenAI's GPT-class, Anthropic's Claude, Google's Gemini, Meta's Llama, the major Chinese open-source models). These are the raw capability layer. Almost no working creative uses them directly except via wrappers.

2. **Modality models** — specialist models for video (Sora, Veo, Runway Gen-4.5, Kling, Hunyuan, Wan), image (Firefly, Midjourney, FLUX, Imagen, SDXL/Stable Diffusion variants), audio (Suno, Udio, ElevenLabs, Mureka), 3D and world (Marble, Genie 3, WorldGen, UNI-1, Hunyuan 3D-PolyGen, ECHO). These are what most working creatives think of when they say "AI tools."

3. **Agent platforms** — systems that compose modality models and external tools into multi-step workflows (OpenAI's AgentKit, Anthropic's Claude apps and skills, Google's Project Genie, Heygen's Video Agent, Sony's 49-agent / 72-skill stack). The agent layer is where the "orchestrator economy" of Chapter 11 actually runs.

4. **Creative software with AI baked in** — the legacy creative suites that have been rebuilt as AI-first platforms (Adobe Creative Cloud, Autodesk, Foundry, Unreal Engine, Unity, DaVinci Resolve, Pro Tools, Logic Pro, Ableton). This is where most paid professional work still happens.

5. **AI-native creative apps** — new entrants whose product is a single-purpose AI workflow (Runway, Higgsfield, Krea, Freepik, Magnific, Synthesia, Heygen, Hedra, Cascadeur, Pika, Luma). Most working creatives use 4 to 10 of these in rotation.

6. **Open-source and workflow infrastructure** — the technical-creator layer that wires everything together (ComfyUI, Hugging Face, SuperSplat, OpenEnv, the open-source model ecosystem). This is where the most interesting innovation often happens first.

7. **Consumer surfaces** — the apps that put generative capability on every phone (the Sora app, CapCut/Dreamina with Seedance, the Gemini app, the various TikTok-style remix platforms). This is the layer the audience touches.

The mistake I see most often, both in the press cycle and in studios planning their internal AI roadmaps, is to optimise for layer 2 (modality models) without understanding that the actual leverage is in how you compose layers 2, 3, 4 and 6 into a coherent workflow. The tool that "wins" is rarely the tool with the best benchmark. It is the tool that integrates cleanly into the rest of your stack.

With that frame, the inventory.

### Video

The video layer changed faster than any other modality between October 2025 and May 2026, and is the one most likely to look different again by the time you read this. Treat the names as snapshots, not as a stable league table.

**Sora 2** (OpenAI) is the model that opened the period this book covers. Its September 2025 launch — physical realism, audio integration, multi-shot world-state persistence — is the moment Chapter 1 is about.[^1] The iOS app launched alongside it hit a million downloads in five days[^2] and is the consumer-facing edge of the AI video market. For professional production, Sora 2 is impressive on isolated single-clip generation and remains the model most cited in the mainstream press, but most working filmmakers I know use it less than its cultural prominence would suggest.

**Veo 3.1** (Google DeepMind), released in mid-October 2025, is the model the professional filmmaking community has, on average, gravitated toward — for narrative coherence, controllable camera composition, cinematic lighting vocabulary and sound integration.[^3] Sora 2 wins on raw physics in single clips; Veo 3.1 wins on the kind of sustained directorial control most actual production pipelines need.

**Runway Gen-4.5** (and Gen-4.5 Image-to-Video, the Workflows product, Story Panels, Characters API, Apps for Advertising) is the most-integrated commercial AI-video stack of the period.[^4] Runway has shipped product faster than any other AI video company in this market, and CEO Cristóbal Valenzuela's "fifty indie films instead of one $100M blockbuster" framing is the cleanest articulation I have seen of the case for AI as creative leverage rather than cost-cut.[^5]

**Kling** (Kuaishou), **Hunyuan Video** (Tencent), **Wan 2.5** (Alibaba), **Seedance 2.0** (ByteDance) — the Chinese-built models that, in aggregate, have rivalled or surpassed the U.S. labs on specific capabilities (motion physics, character consistency, render speed) at significantly lower cost.[^6] Hunyuan's open-source releases have been the single most important contribution to the wider open-source AI video ecosystem in this period.

**Pika 2.0**, **Higgsfield**, **Luma** (Dream Machine and UNI-1) round out the commercial layer. Each has carved a niche: Pika on iteration speed and creator workflow; Higgsfield on social-media marketing video at scale ($80M raised, $1.3B valuation, $200M revenue in nine months[^7]); Luma on the world-model bridge to spatial content.

**Heygen** ships Video Agent — a full scripting-to-assembly agent built around reference images.[^8] **Synthesia** holds the corporate AI-avatar market ($4B valuation, having reportedly rejected a $3B Adobe acquisition offer).[^9] **ElevenLabs** runs the dominant audio-AI layer underneath much of the new video work ($500m ARR by April 2026).[^10]

**Gemini Omni** (Google DeepMind), announced at Google I/O 2026, brings text, image, audio, video and live interaction into a single multimodal model — the first foundation-model release in this category that meaningfully unifies the modalities working creatives currently have to bridge across five different tools.[^42] **Beeple Canvas**, Mike Winkelmann's gen-AI compositor — launched May 2026 — is the first AI-native compositing application to ship from a working visual-effects artist's own studio, and is structurally distinct from the AI-features-bolted-onto-existing-compositors pattern in the legacy-software section below.[^43]

If I had to name a single video product that, in my experience, working creatives have settled on as a default in 2026, it would be Veo 3.1 for finished work and Runway for iteration and integration. Sora is the brand name the audience knows. The actual production pipelines run on the other two.

### Image

The image layer is more stable than video — the technology has matured, the differences between top models are narrower, and the dominant question has moved from "which model" to "which workflow."

**Adobe Firefly** (Image Model 5, plus Foundry for custom-trained corporate models, plus integration across Photoshop / Illustrator / Express / InDesign) is the default for any working creative who is also a Creative Cloud subscriber — which is, by Adobe's own numbers, 45% of Creative Cloud users actively using Firefly, 70% of those weekly, more than 22 billion assets generated by April 2025.[^11] The Firefly adoption curve is the single best evidence I have for the consumption-gap argument in Chapter 13.

**Midjourney** remains the aesthetic-leadership product in the category. Slower to ship, more opinionated about output style, dominant on Discord and X among the working AI-art community.

**FLUX** (Black Forest Labs) is the open-source and pro-creator favourite for fine control, having largely replaced Stable Diffusion XL as the open-weight default through 2025.

**Google Imagen** (and the *Nano Banana* fast-image variant integrated into Gemini, Photoshop and Unreal Engine via the various plugins) has become the most-integrated image model in the consumer toolchain, by virtue of Google's distribution. Nano Banana inside Photoshop and Nano Banana inside Unreal Engine were two of the more consequential cross-platform integrations of the period.[^12]

**Krea**, **Freepik**, **Magnific**, **Recraft** — the higher-control consumer / pro-creator products built on top of foundation image models. Each is competing on specific workflow advantages (real-time generation, upscaling, vector output, brand-consistency control).

The image workflow most commonly cited in my circle in mid-2026 is: a base generation in Firefly / Midjourney / FLUX, character-consistent variation in a controllable wrapper like Krea or Magnific, finishing inside Photoshop with the AI-assisted masking, generative-fill and object-removal tools that Adobe shipped through the autumn 2025 and spring 2026 update cycle.

### Music and audio

The music layer split into three categories during this period, and the split is, in my experience, more important than the specific products in each category.

**Generative music tools** that produce finished tracks from prompts — **Suno** (Studio launched late 2025[^13]), **Udio**, **Mureka** (with its Music Agent Studio, six specialised AI agents for songwriting, arrangement and production[^14]). These are the tools that produce most of the AI-music flood Chapter 5 describes. They are also, paradoxically, the tools most working musicians use the least directly — the consumer market for AI-generated finished tracks is large and growing, but professional musicians overwhelmingly use AI tools at a different layer.

**Production and post-production AI** — the tools that handle audio restoration, mixing, mastering and isolation. The 1,100-creator music survey discussed in [Appendix D](A4_Deep_Dive_Shadow_AI.md) found that 58% of professional producers used AI for audio restoration, 38% for mixing assistance, 33.9% for automated mastering. **iZotope Ozone 12**, **LANDR**, the Pro Tools and Logic Pro AI suites, **CleanvoiceAI** for podcast post — this is where the silent-adoption majority of the music industry lives.

**Voice and audio synthesis** — **ElevenLabs** is the dominant player, with $500m ARR, BlackRock / NVIDIA backing, and meaningful share across audiobook narration, dubbing, podcast synthesis and AI character voice work.[^15] The Cardiff band that found their music had been used to train an "AI artist" outperforming them on Spotify[^16] is one of the cautionary tales of this layer; the Andrii Daniels bomb-shelter clip[^17] is one of the success cases.

**Sound-effect foundation models** emerged as a new sub-category in May 2026. **Sony AI's Woosh** is the first foundation model explicitly trained for the professional sound-effects discipline — built for the people who design the sonic worlds behind games, film and interactive media, not for the consumer market.[^44] **Mirelo SFX 1.6** shipped the first sound-effects model that lets you *edit* a generated sound rather than only regenerate it — a structural shift in the discipline equivalent to the move from rendered images to layered Photoshop files.[^45] **Stable Audio 3.0** (Stability AI) shipped as an open-weight audio model family explicitly aimed at artistic experimentation.[^46] **Tamber**, the ethically-trained AI music suite I describe in [Chapter 6](06_The_88_Percent.md), shipped alongside a gestural-control interface that lets the musician steer the generation with arm movements.[^47] **Beatport's Track ID** rolled out as the real-time identification standard for the DJ market.[^48]

The deal flow underneath this layer is the second-fastest-changing in the toolchain. The Stability AI / Universal Music alliance, the Stability AI / Warner Music deal, the Splice / Universal partnership, the GEMA / OpenAI lawsuit, the Wixen / Meta lawsuit, the UMG / Anthropic $3B suit — these are the structural moves I would track if I were a working musician trying to plan a five-year toolchain.[^18]

### 3D, world models, spatial

The category that, more than any other, I think defines the next decade of creative work. Chapter 8 is the long-form argument; this section is the inventory.

**Marble** (World Labs, Fei-Fei Li's company) is the first commercial product I would put on a professional toolchain.[^19] Public release November 2025; Sony Pictures' use of it in virtual production reportedly running 40× faster than the legacy workflow.[^20] DreamLab has been in the beta since October 2025, and Marble is, today, the world-model product most integrated into a working pipeline I have used.

**Google DeepMind Genie 3** is the most ambitious research-grade world model, named by *Time* as one of the best inventions of 2025. Made publicly available to Google AI Ultra subscribers via Project Genie in January 2026.[^21]

**Meta WorldGen**, **Tencent HY World 1.5** (open-sourced December 2025, alongside the Hunyuan 3D Studio integration[^22]), **SpAItial ECHO**, **Stanford Wonderzoom**, **OpenArt Worlds**, **Luma UNI-1** (the most important *category* announcement of spring 2026, combining world generation with reasoning[^23]) — the rest of the world-model commercial layer.

The May 2026 world-model wave extended this layer further. **NVIDIA SANA-WM** is the first open-weight world model at meaningful scale (2.6B parameters), with 60-second video generation and explicit camera control.[^49] **Odyssey Starchild-1** is, by Odyssey's own framing, *"the first ever real-time multimodal world model"* — a system that doesn't just generate a world but simulates and reasons about it.[^50] **Odyssey Agora-1** is the multiplayer companion to Starchild, putting four players inside the same AI-generated world (built, in a small piece of provenance theatre, on the bones of a 1997 shooter).[^51] **Apple Headsup** is a research-grade 3D Gaussian head-reconstruction pipeline built for multi-view captures from consumer iPhones, extending the Vision-Pro-Personas Gaussian-splat thread into the open research layer.[^52]

Underneath this layer, the Gaussian-splatting infrastructure has matured into a stable workflow: **SuperSplat** (PlayCanvas) for editing, **Spark 2.0** for open-source streaming of 100-million-splat scenes to browsers, the SOG / WebP equivalent compression standard.[^24] Apple's confirmation that its Vision Pro Personas feature is powered by Gaussian splatting under the hood made it, by some margin, the most-deployed Gaussian-splat technology in consumer hardware as of late 2025.[^25]

For the 3D-asset and material side: **Hunyuan 3D-PolyGen 1.5** (Tencent's "art-grade" 3D generative model), **Hitem3D**, **Meshy**, **Rodin** — the rapidly-maturing 3D-asset generation layer that is being integrated, model-by-model, into Unreal Engine, Unity and Blender pipelines.

Ubisoft's open-sourcing of its **CHORD** PBR-material model in December 2025[^26], and the Blender Foundation's patronage deal with Anthropic announced in May 2026[^27], are two of the more strategically significant moves in this layer — both pushing the production-grade open-source tooling forward at a pace the commercial alternatives have struggled to match.

### Agent platforms and orchestration

The category I think most working creatives are still underestimating, six months after Chapter 3 argued it was the inflection point of the era.

**OpenAI AgentKit** (Agent Builder, ChatKit, connector registry, eval framework) launched October 2025 and is the developer-facing platform underneath most third-party agentic creative tools.[^28]

**Anthropic Claude apps** and the **Skills framework** — the system of named, reusable capabilities that Claude Code uses to coordinate multi-agent workflows. The Sony 49-agent / 72-skill game-development stack is built on this.[^29] In May 2026, **Google** released its own **official skills for AI agents** — a parallel, cross-vendor skills layer that lets Google-side agents do what Anthropic's Skills framework has been doing for Claude-side ones.[^53] The convergence of two named "skills" frameworks across the foundation-model vendors is, in my read, the first sign that the orchestration layer is settling on a shared vocabulary rather than continuing to fragment.

**Tencent Ardot**, the company's AI-native design-agent platform launched May 2026, is the most ambitious non-Western agent-platform launch of the period — an integrated environment in which generative design agents handle layout, asset generation, brand application and iteration as a single coordinated pipeline.[^54] In the same week, **Viktor** raised $75M to embed an agentic *coworker* directly into Slack and Microsoft Teams — i.e., the agentic layer landing not as a standalone product but as a colleague-shaped presence in the chat surface the working creative is already in all day, as discussed in [Chapter 9](09_AI_In_Everything.md).

**Heygen Video Agent** for end-to-end video assembly.[^30] **Adobe CX Enterprise** (announced at Adobe Summit 2026 with NVIDIA) for "agentic creative intelligence" across the full content lifecycle.[^31] **NVIDIA + Google Cloud** for the underlying creative-AI infrastructure most enterprise pipelines run on.[^32]

**ComfyUI** — the open-source node-based workflow editor — sits underneath much of the technical-creator community's agentic work. ComfyUI raised $17M in October 2025[^33] and hit a $500M valuation by May 2026[^34]; the platform has become the de facto OS for the open-source side of the creative-AI ecosystem. In May 2026 **Anthropic's Claude** was added as an official partner node inside ComfyUI, joining the existing Google, OpenAI and open-weight nodes — meaning the three frontier foundation models can now be orchestrated side-by-side inside the same open-source pipeline.[^55]

**Hugging Face**, **OpenEnv** (Meta / Hugging Face), the **Hugging Face / Google Cloud** partnership — the open-source agentic-development infrastructure.[^35]

For working creatives, the practical agent stack in 2026 is some combination of:

1. A foundation model (Claude / GPT / Gemini) for the orchestration brain.
2. A modality model layer (video, image, audio, 3D) doing the actual generation.
3. A workflow integration layer (ComfyUI for technical work, the in-app agent surfaces for less technical work).
4. A judgement layer (the human at the desk, doing what Chapter 11 calls *briefing, allocating, judging and integrating*).

The team I work with at DreamLab runs this stack in production every week. The agents that handle our daily work in May 2026 are, in aggregate, doing the labour of what would, two years ago, have been a team three to four times our size. The human team has not shrunk. We have just become substantially more leveraged.

### Legacy creative software, repositioned

The most under-reported strategic story of this period, in my view, has been the speed at which the legacy creative-software vendors have rebuilt their products as AI-agent platforms.

**Adobe** — I have written enough about Adobe in Chapter 9 that I will not repeat it here. The short version: Creative Cloud is, today, a stack of AI agents wearing a Photoshop / Premiere / After Effects / Illustrator / InDesign / Acrobat skin. The agents are inside the apps; the apps are inside ChatGPT; the apps are inside Adobe Express; the apps are inside the new CX Enterprise platform. The repositioning is complete.

**Unreal Engine** (Epic) — the games engine that has, through plugins, integrations and the Nano Banana / Gemini partnership, become a hybrid game-engine / virtual-production / AI-generation hub. The Unreal Engine 5 AI Assistant, announced at the end of 2025[^36], is one of the more consequential single-product launches of the period. The **ECABridge** connector, launched May 2026, is the most-cited Unreal-Engine MCP integration of the spring — providing the Model Context Protocol surface and a set of agentic capabilities Epic itself has not yet shipped to the launcher.[^56] In a separate but related move, an **Epic Games veteran** announced an AI-heavy *"Fully European"* game-engine project in the same week — the first plausibly-credible new entrant in the AAA game-engine market since the early 2010s, framed explicitly around AI as the core operating layer.[^57]

**Unity** — Unity's AI Open Beta (May 2026), an in-editor AI suite for the full games-development pipeline, alongside the company's AI Council formation in October 2025.[^37]

**Autodesk**, **Foundry**, **SideFX** — the VFX-pipeline vendors integrating generative AI into Maya, Nuke and Houdini at the speed the VFX industry's adoption curve (62% of Hollywood studios on automated compositing, 35% reduction in post-production timelines[^38]) demanded.

**Blender** — open-source 3D, now a recognised industry-grade tool, beneficiary of the Anthropic Foundation patronage deal.[^39]

**DaVinci Resolve** (Blackmagic), **Avid Media Composer**, **Pro Tools** — the editorial and audio post environments, all now shipping AI-augmented features that have become baseline expectations.

The thing to note is that the legacy software did not get displaced by the AI-native products. The legacy software *absorbed* the AI-native capability and kept the underlying user community. Adobe was supposed to lose to Midjourney in 2024; Adobe is, instead, the dominant generative-AI player by aggregate creator engagement in 2026. The platform companies bet on this absorption pattern, and that bet has, so far, paid off.

### Open source

The open-source ecosystem has, against the odds and against most VC predictions in 2024, held its ground through this period and is, in several categories, the leader rather than the follower.

**Hugging Face** — the operating system of open-source AI, expanding aggressively through 2025–26.

**ComfyUI** — already discussed.

**Open-source models from Tencent (Hunyuan)**, **Alibaba (Qwen, Wan)**, **DeepSeek**, **Meta (Llama)**, **Mistral**, **Stability AI** — collectively, the open-weight ecosystem that, by the spring of 2026, was being used by approximately 80% of startups pitching the Andreessen Horowitz fund.[^40] **NVIDIA's SANA-WM** (May 2026) extended this list to world-models for the first time at meaningful parameter scale.[^49]

**PhotoGIMP**, the open-source skin that takes GIMP and makes it look and feel exactly like Photoshop, became, in this period, a credible Photoshop alternative for working creatives who wanted to opt out of the Adobe subscription stack — the open-source equivalent of the *Tools I do not use* discipline in the section above.[^58]

**OpenEnv** (Meta / Hugging Face) for open-source agentic development. **Korin AI** (the Africa-trained, Africa-built model launched May 2026[^41]). **SuperSplat**, **Spark 2.0**, **PlayCanvas SOG**, **Blender** — the open-source spatial / 3D infrastructure layer.

If you are a working creative trying to build a long-term, defensible toolchain that does not depend on the unilateral pricing or policy decisions of a single platform company, the open-source ecosystem in 2026 is materially viable in a way it was not eighteen months ago. We have built significant parts of the DreamLab pipeline on top of it precisely for that reason.

### Tools I do not use, and why

I want to be specific, because lists of "best tools" without exclusions are not useful.

I do not use AI tools whose terms of service claim ownership over my output, or that train on user inputs without an opt-out. Multiple consumer-facing AI products in this period have shipped with terms that working creatives should read carefully before adopting.

I do not use AI tools whose training data provenance I cannot, in some material way, verify or trust. The growing infrastructure for *creative weight attribution*, watermarking and C2PA compliance is, in my view, the right side of the market to be on; tools that explicitly reject that infrastructure are tools that I have, increasingly, kept out of our production pipeline.

I do not use the AI products that have made the most noise in the consumer press cycle. The marketing-driven launches — the products whose first appearance is a viral demo and whose second appearance is a Series-A round — are, in my experience, the products most likely to have collapsed or pivoted by the time you need them in production six months later.

I do not, finally, use AI tools to produce work in the disciplines where my own craft is the value I am bringing to the client. The Continuum frame from Chapter 3 is, for me, a daily operational practice, not a theoretical model. The places I sit on the right edge of the line are deliberately chosen. The places I sit on the left are deliberately defended.

### The complete toolchain: a categorised reference

This section is a reference inventory, not a recommendation list. It catalogues every tool, model, platform, app, plugin, LoRA, workflow and service that *Dream Machine* tracked across its 29 issues, from October 2025 to May 2026. Some are dominant; some are niche; some have already been bought, renamed or discontinued by the time you read this. The point of the list is not "what to use." The point is *what existed*, in this period, in the creative-AI toolchain — so that the *shape* of the field is on the record.

A word on the list's grain. I have tried to err on the side of inclusion. Where a single company ships multiple closely-related products — Adobe's *Sneaks* portfolio, the Runway Gen-4.5 family, the Qwen-Edit LoRA series — I have grouped them under the parent entry but called out the constituent tools, because in this period each constituent shipped to working creatives separately and changed at its own cadence. Where a tool was a one-issue demo I could not later verify, I have still listed it; that the demo existed *at all* is part of the field's history. Where a tool's name conflicts with another (there are at least three things called "Wonder" in the period the book covers) I have annotated.

The list runs to roughly six hundred entries. Skim it. Use the categories. Come back to specific sections when you need them.

#### Foundation models / LLMs

- **ChatGPT / GPT-5 / GPT-5 Pro** (OpenAI) — the dominant consumer LLM and reference foundation model; 800–900M weekly active users; GPT-5 / GPT-5 Pro announced at DevDay 2025.
- **Claude / Claude Code / Claude Apps / Claude Skills** (Anthropic) — the writers' and developers' favoured second; strong long-context performance; the agentic coding environment that underlies Sony's 49-agent / 72-skill stack; Claude for Legal launched May 2026.
- **Gemini / Gemini 2.5 Flash / Gemini 3 / Gemini 3.1 Flash** (Google) — Google's multimodal LLM family; desktop users growing 155% YoY in 2025–26; Gemini 3.1 Flash TTS is the most controllable Google voice model as of spring 2026.
- **Llama** (Meta) — the dominant open-weight foundation model.
- **Mistral / Mistral Voxtral / Mistral Transcribe 2** — European open-source LLM; Voxtral is the next-generation speech-to-text family.
- **Qwen / Qwen 3.5-Omni** (Alibaba) — Chinese open-source LLM, image, video and audio variants; Omni is the multimodal family covering text, images, audio and video.
- **DeepSeek** — Chinese open-source LLM used heavily in agentic stacks.
- **Phi / Phi Mini** (Microsoft) — lightweight foundation models.
- **Lyria / Lyria 3 / Lyria 3 Pro** (Google DeepMind) — text-to-music foundation model family; Lyria 3 ships with SynthID watermarking and the Lyria Camera interactive demo.
- **Grok** (xAI) — xAI's LLM family, surfacing in the creative stack through Grok Imagine; voice cloning via the xAI API from May 2026.
- **Cohere Transcribe** — enterprise transcription model; 33 hours of audio in 12 minutes.
- **Microsoft VibeVoice** — open-source frontier voice AI model.

#### AI video models

- **Sora / Sora 2** (OpenAI) — the model that opened the period; physical realism, audio integration, multi-shot world-state persistence; iOS app hit 1M downloads in 5 days; Sora 2 Character Creation surfaced on fal in March 2026.
- **Veo 3 / Veo 3.1 / Veo 3.1 Ingredients to Video / Veo 3.1 Lite** (Google DeepMind) — the working filmmaker's preferred model for cinematic control; Ingredients to Video shipped to YouTube Shorts and YouTube Create; Veo 3.1 Lite is the lower-cost text- and image-to-video tier.
- **Runway Gen-4 / Gen-4.5 / Gen-4.5 Image-to-Video / Workflows / Story Panels / Characters API / Ad Concepter / Apps for Advertising** (Runway) — the most-integrated commercial AI-video stack; Story Panels generate three-panel storyboards from a single image; Characters API ships real-time intelligent avatars; the Vera Rubin-powered real-time model runs <100 ms latency.
- **Kling / Kling 2.5 Turbo / Kling O1 / Kling 2.6 / Kling 3.0 / Kling X-Dub / Kling Motion Control 3.0** (Kuaishou) — strong on physics and trajectory control; 3.0 adds multi-shot control, multilingual audio and 4K image generation; X-Dub is the context-rich visual dubbing variant.
- **Pika 2.0 / PikaStream 1.0** — iteration-speed-focused video generation; PikaStream brings AI agents into live video calls.
- **Luma Dream Machine / UNI-1 / UNI-1.1 / Ray3 Modify / Luma Dream Brief** — Luma's video, world-and-reasoning, and modification stack; UNI-1.1 ships with prompt enhancement and built-in research; Dream Brief is the $1M Cannes Lions competition.
- **Wan 2.2 / Wan 2.5 / Wan 2.6** (Alibaba Qwen) — camera-controlled video generation; 2.6 adds character reference and multishot capabilities.
- **Hunyuan Video / Hunyuan Image-to-Video** (Tencent) — open-source video model.
- **Seedance 2.0 / SeeDream 4 / SeeDream 4.5** (ByteDance) — image-to-video and finished-video models, integrated into CapCut / Dreamina and Freepik; per-second cost fell below $0.14 by March 2026.
- **Higgsfield / Higgsfield Sketch-to-Video / Higgsfield Popcorn / Higgsfield Relight / Higgsfield Shots / WAN Camera Control** — social-media-marketer video platform; $80M raised at $1.3B valuation, $200M revenue in nine months; Shots produces multiple storyboard images from a single shot.
- **LTX-2 / LTX-2.3 / LTX-2.3 Colorizer / LTX-HDR / LTX Studio / LTX-2 Audio-to-Video / LTX-2 Lip Sync / LTX-2 Real-Time** — open-source video generation with audio sync; LTX-2.3 is high-resolution, fast, cinematic with native lip-sync; LTX HDR (beta) ships HDR processing.
- **Odyssey 2** — real-time interactive video generation.
- **Vidi 2** (ByteDance) — multimodal video understanding and creation.
- **MotionStream** — real-time interactive video with mouse-based motion control.
- **Blockvid** — one-minute video with improved structure and visual consistency.
- **Video Rebirth** (Singapore) — studio-grade AI video platform; $50M raise.
- **LiveGS** — mobile Gaussian-splatting video.
- **Time-To-Move** — motion control for generated video.
- **Ovi / Ovi 1.1** (Character.AI) — open-source video with speech sync.
- **CraftStory** — image-to-video for long-form AI video with human "actors".
- **Decart Lucy 2.0** — realtime world-editing video model; 1080p at 30 fps.
- **Decart LSD v2** — real-time video-to-video with prompt-on-the-fly.
- **Xmax X1** — the first real-time interactive video model.
- **FastVideo** — 30-second 1080p generation at 4.5 s latency.
- **HiAR** (Tencent) — scalable long-video generation.
- **Alli AI** — system for creating and editing 8K video up to 60 seconds.
- **AERA AI TV** — automated storyboard generation, editing and serialized video production.
- **AnchorWeave** — world-consistent video generation with retrieved local spatial memories.
- **CubeComposer** — generates native 4K 360° video from standard perspective footage.
- **MatAnyone2** — high-fidelity video matting with finer detail.
- **VFace** — training-free video face-swapping for any diffusion model.
- **DreamActor M2.0** (fal) — drive characters from a single image + template video; multi-character supported.
- **ByteDance ALIVE** — unified audio-video generation.
- **Magnific Upscaler for Video / Magnific Precision v2 / Magnific Precision for Video** — upscaling and 4K detail enhancement, including dedicated video upscaling.
- **NetFlix VOID** — object removal from video with physics-interaction removal.
- **Ponder** — agentic video editor.
- **ArcReel** — multi-agent video generation from written stories.
- **Scope** — real-time interactive generative AI pipelines (LTX-2.3 real-time runs on Scope).
- **NotebookLM Cinematic Video Overviews** (Google) — video generation from notebooks.
- **Omnia** — AI-native browser video editor.
- **NVIDIA RTX Video Super Resolution** — upscaling node with ComfyUI integration.
- **Google M2SVid** — monocular-to-stereo video conversion.

#### AI image models / tools

- **Midjourney / Midjourney V8.1** — the aesthetic-leadership product; Discord/X-native; V8.1 ships native 2K HD rendering at 3× the speed and 3× the cost reduction.
- **FLUX / FLUX 2 / FLUX 2 Max / FLUX.2 [klein]** (Black Forest Labs) — open-weight, fine-control, the open-source default through 2025–26; klein is the 4B-parameter lightweight model.
- **Adobe Firefly / Firefly Image Model 5 / Firefly Foundry / Firefly Boards / Firefly Precision Flow** — Image Model 5, Foundry (custom corporate training), Firefly Boards (moodboards), Precision Flow (granular AI editing control, beta); 45% of Creative Cloud users active, 22B+ assets generated by April 2025.
- **Imagen 3 / Nano Banana / Nano Banana Pro / Nano Banana 2** (Google) — most-integrated image model in the consumer toolchain; Photoshop and Unreal Engine plugins; Nano Banana Pro ships professional capabilities at lightning speed.
- **Stable Diffusion / Stable Diffusion 3** (Stability AI) — the foundational open-source image model.
- **Krea / Krea AI / Krea 2 / Krea Realtime / Krea Realtime Edit / Krea Nodes / Krea LoRA Trainers** — real-time AI image generation, now open-source; Realtime Edit takes complex instructions in real time; the LoRA Trainers cover Qwen-2512 and Z-Image.
- **Qwen-Image-2512 / Qwen-Image-Edit-2511 / Qwen 2511 Time Travel / Qwen-Edit 2509** — the dominant open-source image-editing model family; constituent LoRAs (relighting, multi-angle, time-travel, AnyPose) discussed in the LoRAs section below.
- **ChatGPT Images / ChatGPT Images 2.0** — image generation integrated with Adobe Express, Photoshop and Acrobat; 2.0 ships thinking-level intelligence.
- **Grok Imagine / Grok Imagine API** (xAI) — image and video generation; the API bundles end-to-end creative workflows; reference-to-video and video extend added in March 2026.
- **Vision Banana** — unified model for image understanding and generation.
- **Freepik / Freepik Spaces / Freepik Speak / Freepik 3D Scenes** — design platform; Spaces is the real-time collaborative canvas; Speak is the lip-sync talking-video tool; 3D Scenes generates full environments from an image.
- **Recraft** — brand-focused AI design.
- **Weavy** — node-based AI creative platform; acquired by Figma.
- **Canva** — design platform with "Creative Operating System."
- **Civitai / Civision** — community-models and LoRAs platform; Civision is the free Civitai/Hugging-Face hybrid alternative.
- **Replicate** — model-hosting marketplace and API.
- **GFPGAN** — face restoration.
- **UpscalyAI / Upscayl / Topaz Gigapixel AI / Real-ESRGAN / Clarity Pro Upscaler** — upscaling tools; Clarity Pro reaches 10K.
- **PractiLight** — practical light control via diffusion.
- **PercHead** — 3D head reconstruction from single images.
- **Loveart AI** — layer separation and editable text (Live Editable Text, LET).
- **NVIDIA ChronoEdit** — temporal reasoning for image editing.
- **Beeble Switchlight 3 / Beeble Background Remover** — AI masking and relighting.
- **CanvAI** — turns rough sketches into polished AI art.
- **MakeComics / Make Comics** — generates custom comics with characters and storylines in seconds; from prompt to full comic book.
- **Seethrough** — illustration decomposition into layered PSD.
- **Best Face Swap (Flux 2 LoRA)** — specialised face-swap.
- **PixelSmile** — fine-grained facial-expression editing across 12 expressions.
- **Earth Cinema** — Chrome extension using Google Earth for cinematic images.
- **360Anything** — lifts any perspective image or video to a 360° panorama.

#### AI music / audio tools

- **Suno / Suno Studio / Suno 5.5** — the dominant prompt-to-track generative music platform; $250M raised at $2.45B valuation; Suno Studio is the "world's first generative audio workstation"; 5.5 adds Voices.
- **Udio** — prompt-to-music; partnered with Universal Music Group; indie-label licensing via Merlin.
- **Mureka / Music Agent Studio** — six specialised AI agents covering songwriting, arrangement and production.
- **ElevenLabs / ElevenLabs v3 / Scribe v2 Realtime / ElevenMusic / ElevenCreative / ElevenLabs Flows / ElevenAgents Expressive Mode / ElevenLabs Voice Changer** — the dominant voice/audio synthesis stack; $500M ARR; BlackRock + NVIDIA backed; Scribe v2 transcribes in 150 ms across 90+ languages; ElevenMusic is the discovery/creation/earning marketplace; Flows is the node-based creative canvas.
- **iZotope Ozone 12 / Stem EQ** — AI-assisted mixing and mastering.
- **LANDR** — AI mastering and distribution.
- **Riffusion** — spectrogram-based music generation.
- **Stable Audio 2.5** (Stability AI) — generative audio.
- **MusicGPT** — local music generation.
- **ACE Studio / ACE Studio 2.0 (TIMEDOMAIN) / ACE Studio Video-to-Music / ACE-Step 1.5 / ACE-Step 1.5 XL** — all-in-one AI music studio; video-to-music for visuals; ACE-Step generates full songs in under 10 seconds on <4 GB VRAM.
- **Music Lens** (Musixmatch) — catalog-intelligence agent.
- **Melosurf** — voice-controlled assistant for Ableton Live.
- **Songscription** — audio-to-notation transcription; $5M raise.
- **Groundhog Audio Pedal / Groundhog OnePedal** — AI guitar tone matching.
- **Spotify DJ / Spotify AI / Spotify AI Prompted Playlists / Spotify AI Transparency Beta / Personal Podcasts on Spotify** — playlist personalisation, voluntary AI disclosure beta, agent-created podcasts.
- **YouTube Music AI Hub** — AI music hosting and DJ features.
- **Epidemic Sound Studio** — AI music for video creators.
- **AIODE** — ethically-trained music creation DAW.
- **Overtune** — virtual music studio for Roblox.
- **Space DJ** (Google DeepMind) — interactive music exploration.
- **Minimax Music Generator** — song generation.
- **Roland AI Pedal** — concept for AI audio processing.
- **Roland + Sony CSL Melody Flip** — AI music tool.
- **BandLab Voice Cleaner / BandLab Palette** — background-noise removal; AI loop-matching.
- **Claimy** — missing-royalty recovery agent.
- **Fish Audio S1 / Fish Audio S2** — text-to-speech; S2 ships expressive TTS with emotional control (6× cheaper than ElevenLabs at S1).
- **Tempolor Guitars** (Quwan) — AI to make songs playable on guitar.
- **GEMIDI** — music playground powered by Gemini.
- **Lalal AI / Lalal AI plugin / Lalal AI API v1** — AI stem separation, music removal, voice changing; first stem-separation plugin native to a DAW.
- **StemDeck** — local stem separation; free, no upload required.
- **Mirelo** (Berlin) — automatic sound-effect generation for video.
- **PromptSep** — separates any sound by text description.
- **SAMAudio** (Meta) — Segment Anything for audio editing.
- **SonicLab SPATAI** — generative audio engine for immersive spatial production.
- **Apple Logic Pro AI** — synth player and personal music-theory expert; chord-progression generation.
- **Apple GarageBand** — consumer music creation.
- **Musicful AI** — music-video generation for AI-generated songs.
- **Latent Space Explorer** — interactive audio data visualiser using Stable Audio VAE.
- **Voicebox** — open-source local voice cloning from a 3-second audio clip.
- **Voice-Pro** — AI speech recognition / translation / transcription / multilingual dubbing.
- **PersonaPlex** (NVIDIA) — full-duplex model that listens and speaks simultaneously; open-source natural-sounding voice.
- **Phoenix-4** — advanced real-time human-rendering model with 10+ emotional states.
- **NVIDIA D-Rex** — photorealistic digital humans under any lighting.
- **Qwen3-TTS / VoiceDesign / VoiceClone** — text-to-speech with voice design and cloning.
- **Greysound** — self-engineering music-production studio.
- **TAC (Timestamped Audio Captioning)** — timestamped captions for audio and audiovisual content.
- **Insanely Fast Whisper** — 2.5 hours of audio transcribed in 98 seconds.
- **smol-audio** — local audio model notebooks and scripts.
- **AudioStream / Walzersymphonie** (Ars Electronica Futurelab) — AI composition system for classical music using Ricercar.
- **Ricercar** (Ars Electronica) — creative AI for artistic composition.
- **Krotos Video-to-Sound** — expanded platform for audio professionals (foley, sound design).
- **Jamu** — AI co-producer agent for Ableton Live.
- **Moises** — AI music platform; Charlie Puth as Chief Music Officer.
- **Music Mogul AI** — tour-booking automation.
- **Sonilo + Shutterstock** — video-to-music AI training deal.
- **Clearnote** — AI music-contract platform to end deal delays.
- **Sony music identification tech** — identify original music inside AI-generated songs.
- **Cactus Music** — artist-ops support.
- **Rebel Audio** — AI podcast startup.
- **ROLI Airwave & AI Music Coach** — hand-tracking (27 joints) with real-time AI piano practice coaching.
- **Sony AI ICASSP papers** — music understanding and generative audio research papers (April 2026).

#### 3D, world models and spatial

- **Marble / Marble 1.1 / WorldLabs API / RTFM** (World Labs / Fei-Fei Li) — first commercial generative world model; 40× faster than legacy VP workflow; 1.1 adds real-world location 3D reconstruction and restyling; the API generates persistent 3D worlds from text, images and video; RTFM is the real-time frame model.
- **Genie 3 / Project Genie** (Google DeepMind) — research-grade world model; *Time* Best Inventions 2025; rolled out to Google AI Ultra in January 2026.
- **WorldGen / WorldMirror** (Meta / Tencent) — interactive 3D world generation.
- **UNI-1 / UNI-1.1** (Luma) — world generation + reasoning combined; 1.1 adds prompt enhancement and built-in research.
- **Hunyuan 3D / Hunyuan 3D Studio / Hunyuan 3D-PolyGen 1.5 / HY3D 3.0 / HY-Motion 1.0** (Tencent) — art-grade 3D generative model family; PolyGen 1.5 is the art-grade text/image/sketch-to-3D model; HY-Motion 1.0 is text-to-3D human motion.
- **HY World 1.5 / HY-World 2.0 / WorldCompass / ShotVerse** (Tencent) — open-source real-time world-model frameworks; WorldCompass is the RL post-training framework; ShotVerse handles cinematic multi-shot camera control.
- **ECHO / Echo-2** (SpAItial) — spatial foundation model; Echo-2 adds world decomposition.
- **Wonderzoom** (Stanford) — multi-scale 3D world generation with infinite zoom.
- **Matrix-Game 3.0** (Skywork AI) — real-time interactive world model; 720p at 40 fps with long-horizon memory.
- **AMD Micro-World** — AMD's entry into world models.
- **LingBot-World** — free/open-source world model on Wan 2.2; real-time interaction at 16 fps.
- **Moonlake** — $28M-seeded world model platform now in beta for games and simulations.
- **NVIDIA Lyra 2.0** — explorable generative 3D worlds.
- **NVPanoptix-3D** (NVIDIA) — single-image 3D indoor-scene reconstruction.
- **Kimodo** (NVIDIA) — kinematic motion-diffusion model trained on 700 hours of mocap.
- **InSpatio-WorldFM** — open-source real-time generative frame model.
- **Code2Worlds** — workflow for generating 4D scenes with environmental/object generation and feedback refinement.
- **OpenArt Worlds** — 3D navigable environments from a single prompt.
- **Rodin / Hyper3D / Rodin Hyper 3D Gen 2** — high-precision 3D model generation.
- **Meshy / Meshy 6 / Meshy Image-to-3D** — 3D model generation; Meshy 6 ships natively inside ComfyUI; Image-to-3D generates poses.
- **Hitem3D** — high-resolution 3D generation.
- **Microsoft Trellis 2** — native compact structured latents for 3D.
- **ByteDance Seed3D 2.0** — 3D object generation from image or text.
- **Pixel3D** (Tencent) — 3D object generation.
- **Tripo 3.1** — 3D-asset creation; ComfyUI partner nodes.
- **PATINA** (fal) — image or text to full PBR material maps.
- **M-XR PBR Model** — 4K PBR material maps for 3D assets.
- **CHORD** (Ubisoft La Forge) — open-sourced end-to-end PBR-material generation.
- **Autodesk Wonder 3D** — generative AI tool creating editable 3D assets from text or images.
- **Autodesk Flow Studio Rigging** — AI rigging and neural layers.
- **AI4AnimationPy** (Meta) — pure-Python 3D character animation.
- **MocapAnything** (Huawei) — unified 3D motion capture for arbitrary skeletons from monocular video.
- **FreeMoCAP** — open-source markerless mocap from any camera.
- **MuJoCo** — physics engine for robotics and animation.
- **Mesh2Motion** — auto-assigns and exports 3D model animations.
- **One-to-All Animation** — alignment-free character animation and image pose transfer.
- **Cascadeur / Cascadeur AI Animation v2025.3** — AI animation tool for character movement; local interpolation.
- **Move AI** — motion capture.
- **MoCap / UE5 Motion** — camera-only motion capture.
- **SCAIL** — studio-grade character animation via in-context learning.
- **Vanast** — garment-transferred human animation from images.
- **CompHairHead** — one-shot 3D head avatars with deformable hair.
- **Reallusion Headshot 3** — digital-double creation.
- **MoRo** (Meta) — human motion recovery via masked modelling for occlusions.
- **Meta Sapiens 2** — pose estimation, body-part segmentation and surface normals.
- **NVIDIA Audio2Face / Audio2Face-3D** — facial animation from audio.
- **NVIDIA UniRelight** — shot relighting technology.
- **Apple SHARP / LiTo** — photorealistic 3D view synthesis from a single image in under a second; LiTo is the surface light-field tokenisation method.
- **Pixel3DMM** — screen-space single-image 3D face reconstruction.
- **VISTA4D** (Netflix + Eyeline) — live-action to navigable 4D point clouds.
- **SuperSplat / SuperSplat v2.16** (PlayCanvas) — free, open-source Gaussian-splat editor.
- **Spark 2.0** — open-source Gaussian-splat streaming framework; streamable LoD for WebGL2.
- **PlayCanvas SOG / SplatTransform v2.0.0** — WebP-equivalent compression for Gaussian splats; SplatTransform v2 ships automatic high-quality collisions for splats.
- **Cesium / CesiumJS / Cesium for Unreal** — geospatial 3D platform; Cesium agentic workflows let natural-language commands interact with 3D geospatial data; supports Gaussian splats natively.
- **SPAG-4D** — 360° photos to 3D Gaussian splat conversion.
- **Animated Gaussian Splats** (4DV.ai) — 4D Gaussian-splat animation.
- **Open3Dmap** — crowdsourced 3D mapping with Gaussian splats.
- **Hyperscape / Hyperscape Capture** (Meta) — Gaussian-splat capture on Quest.
- **Apple Vision Pro Personas** — Gaussian-splatting consumer feature.
- **Common Sense Machines** — converts 2D images into 3D digital assets (Google acquisition).
- **NVIDIA Omniverse Fixer** — rendering-artefact removal for Gaussians.
- **DecartAI / Decart LSD v2 / Decart Lucy 2.0** — real-time world transformation by voice; LSD v2 is real-time video-to-video; Lucy 2.0 is realtime world editing at 1080p/30fps.
- **VoxeloAI** — 3D creation for e-commerce.
- **Mosaic / Mosaic 3D** — 3D reconstruction.
- **Depth Anything 3** (ByteDance) — visual-space recovery from any view.
- **SAM 3 / SAM 3D / SAM 3.1** (Meta) — object detection and 3D segmentation; SAM 3.1 is 7× faster, tracking 128 objects on a single H100.
- **Seen2Scene** — realistic 3D scene completion with visibility-guided flow.
- **PixARMesh** — reconstructs full indoor scenes from a single photo into lightweight meshes.
- **Confidence-Based Mesh Extraction from 3D Gaussians** — algorithm for high-quality mesh extraction from Gaussian splats.
- **Rhizomatics Sword Tip Visualization System** — fencing tracking at 60 fps.
- **Mixar** — AI-native Blender-fork editor positioned as "Cursor for 3D artists".
- **Sprite Booth** — pixel-character animation tool (ComfyUI API required).
- **AutoSprite** — character-to-animated-sprite-sheet conversion.

#### Voice, avatar, digital human

- **Synthesia** — AI avatar platform; $4B valuation; rejected $3B Adobe offer.
- **Heygen / Heygen Video Agent / Heygen Motion Designer / LiveAvatar / Heygen Elements / Heygen CLI** — AI-avatar and end-to-end video generation; LiveAvatar is hyper-realistic real-time interactive; Elements builds scenes from reusable components; CLI ships videos from the command line.
- **Hedra / Hedra Audio Tags / Hedra Elements** — digital-human creation; Audio Tags assign precise emotions to audio.
- **Live Avatar** (Alibaba) — streaming real-time audio-driven avatar generation with infinite length.
- **Avatar Forcing** — real-time interactive head-avatar generation for natural conversation.
- **PersonaLive** — real-time expressive portrait animation.
- **Weclone** — digital avatar built from a user's chat history.
- **Particle6 / Tilly Norwood** — AI-performer studio and synthetic actress.
- **Xania Monet** — AI music artist; Billboard chart entries; $3M Hallwood Media deal.
- **Bleeding Verse** — AI band; Hallwood Media signing.
- **Sienna Rose** — anonymous AI artist with millions of Spotify streams.
- **Breaking Rust** — AI country artist; #1 country digital song sales.
- **Trilok** — Indian AI band.
- **Copresence / ConvAI / Inworld** — avatar and NPC-character technology for Unreal Engine, games and interactive media.
- **ROXi** — AI-generated TV presenters.
- **Facelooker** — interactive headshot generation.
- **FellinAI** — AI film director.
- **ego AI** — in-game character platform.
- **Character.AI** — play characters in your favourite books; Ovi open-source video with speech sync.

#### Agent platforms and orchestration

- **OpenAI AgentKit / Agent Builder / ChatKit / Connector Registry / Eval Framework** — the developer-facing agent platform underneath most third-party agentic creative tools.
- **Anthropic Claude Apps / Claude Skills / Claude Code / Claude Design / Claude for Legal / Anthropic Academy** — interactive Claude in workplace tools; the Skills framework powers Sony's 49-agent / 72-skill game-development stack; Claude Design ships prototypes/slides/one-pagers; Anthropic Academy is free Claude Code training.
- **Claude Code Game Studios** — 49-agent, 72-skill coordinated AI game-development team.
- **Gemini API Agents / Google Antigravity / Opal / Fabula / Google Stitch** (Google) — agentic capability surface across Google's stack; Antigravity is the agentic development platform; Opal is the no-code mini-app builder; Fabula is the interactive AI writing tool; Stitch generates mobile/web UI.
- **Heygen Video Agent** — end-to-end video-assembly agent.
- **Adobe CX Enterprise / GenStudio / Adobe Film & TV Fund / Adobe Ignite Day** — agentic creative intelligence across the full content lifecycle; GenStudio is the brand-intelligence system for personalised content at scale.
- **NVIDIA + Google Cloud / Avid + Google Cloud / Speechmatics in Adobe Premiere** — agentic-creative infrastructure partnerships; on-device speech-to-text inside Premiere.
- **n8n** — workflow automation with AI.
- **ComfyUI / ComfyUI Cloud / ComfyHub / ComfyUI App Mode / ComfyUI Simple Mode** — node-based AI workflow editor; $500M valuation by May 2026; App Mode turns workflows into shareable no-install apps; Simple Mode lowers the complexity threshold.
- **Replicate** — model marketplace.
- **Hugging Face** — open-source model hub and agentic platform; partnered with Google Cloud and Meta.
- **Meta OpenEnv** — open-source agentic-development environment.
- **fal / FAL MCP** — generative-model deployment marketplace; FAL MCP exposes 1,000+ generative models to Claude/Cursor.
- **Unity Official MCP / Unity MCP** — Unity Editor control via MCP protocol.
- **Blender MCP / Blender Buddy / OpenClaw + Blender MCP** — Claude-to-Blender control for 3D workflows.
- **VibeComfy** — open-source tools letting agents understand, build and run ComfyUI workflows with Claude.
- **MooshieUI** — beginner-friendly ComfyUI desktop frontend.
- **Lenny** (Maroofy) — AI agent for live-music event organisers.
- **AdsGency** — autonomous paid-marketing agent platform; $12M seed.
- **Invideo AI / Invideo AI Agent** — full video-ad generation from prompt; built on Gemini.
- **Pomelli** (Google Labs) — AI marketing agent for small business.
- **Inception Point AI** — podcast hosting with AI hosts (3,000+ episodes/week).
- **Slapshot** — AI camera tracking.
- **Photoroom** — AI photobooth.
- **Jabali.ai** — AI game-development platform (Sony-backed).
- **Fifth Door** — AI-powered game creation; $20M raise.
- **Atlas AI Agents** — game-production pipeline agents.
- **Ad Concepter** (Runway) — ad-concept exploration agent.
- **AE GPT** — AI assistant for After Effects (expressions, scripts).
- **Career-Ops** — AI job-search pipeline built with Claude Code.
- **Auto-Dream** (MyClawAI) — personal AI assistant wrapper.
- **Clicky** — AI screen-aware tutor/buddy interface.
- **MemPalace** — high-scoring AI memory system.
- **TikTok AI Agents for Ads** — TikTok's automated ad-creation agents.
- **Amazon Creative Agent** — agentic AI generating professional-quality ads.
- **Playad** — AI marketing agents for ad creative.
- **Moltbook** (Meta acquisition) — AI agent social network.

#### Legacy creative software, AI-augmented

- **Adobe Creative Cloud** — Photoshop, Premiere Pro, After Effects, Illustrator, Express, Acrobat, plus the Express AI Assistant, the Premiere Object Mask, the Photoshop generative-fill, selection and Rotate Object tools, the Photoshop AI Assistant public beta, and Illustrator Turntable.
- **Adobe Sneaks 2025–26** — Adobe's research-preview portfolio shown at MAX 2025 and Summit 2026:
  - **Project Scene It** — image-to-3D and 3D-to-image with object tagging.
  - **Project Surface Swap** — AI-powered texture recognition and swap.
  - **Project Turn Style** — edit and transform 2D objects as if they were 3D.
  - **Project Trace Erase** — removes objects, shadows, reflections and distortions.
  - **Project New Depths** — edit depth like brightness.
  - **Project Frame Forward** — apply changes across video from a single frame plus text.
  - **Project Motion Map** — bring static vector graphics to life.
  - **Project Sound Stager** — analyses video visuals and generates synchronised soundscapes.
  - **Project Clean Take** — corrects mispronunciations and isolates voices.
  - **Project Light Touch** — spatial lighting mode for relighting photos.
  - **Project Graph** — node-based workflow editor in the ComfyUI / Weavy lineage.
  - **Corrective AI** — changes the emotional register of voice-overs.
  - **Edit-by-Track** (Adobe Research) — generative video motion editing with 3D point tracks.
- **Adobe Acrobat** — AI converting PDFs into podcasts.
- **Unreal Engine 5 / UE5 AI Assistant / UE5 AI Motion Plugin / Unreal to Gaussian Splat / Prompt-to-Player** (Epic) — official AI assistant; camera-only motion capture; UE5 scene-to-splat conversion; Prompt-to-Player generates 3D characters and auto-rigs/animates them.
- **Unity / Unity AI Open Beta / Unity AI Council / Unity AI Tools Suite / Unity Prompt-a-Game** — in-editor AI suite for the full games pipeline; Prompt-a-Game demoed at GDC March 2026.
- **Autodesk Maya / Autodesk Flow Studio / Autodesk Wonder 3D / Autodesk Flow Studio Rigging** — motion capture, 3D animation, generative 3D and neural rigging.
- **Foundry / Nuke / Nano Banana × Nuke** — AI-augmented VFX; Weta FX / AWS collaboration; the Nuke node connecting Nano Banana through fal's API.
- **SideFX Houdini** — procedural modelling with AI integration.
- **Blender / Blender MCP / Blender Buddy** — open-source 3D; Anthropic Foundation patronage; MCP enables Claude control.
- **DaVinci Resolve** (Blackmagic) — colour and editorial with AI features.
- **Avid Media Composer / Avid + Google Cloud** — professional editorial; Pro Tools agentic AI in the Google Cloud partnership.
- **Pro Tools** — audio editorial with AI features; Claude integration in Ableton.
- **Logic Pro / Apple Logic Pro AI** — music production with AI; synth player and music-theory expert.
- **Ableton Live / Claude in Ableton / Jamu / Melosurf** — music production with Claude assistance, Jamu co-producer agent and Melosurf voice control.
- **GarageBand** — consumer music creation.
- **CapCut / Dreamina / Snapchat AI Clips in Lens Studio** (ByteDance / Snapchat) — mobile video editing with AI; Snapchat AI Clips in Lens Studio.
- **Final Cut Pro** — editorial with FX Factory plugins.
- **Keyframe** — AI models inside After Effects.
- **Tether** — AI animation inside After Effects.
- **Deep Pan** — animated stills in Premiere Pro.
- **FX Factory** — AI plugin suite for Premiere and Final Cut.
- **VEED Transitions** — AI transition generation.
- **Electric Sheep** — web-based projection mapping and AI visual orchestration.

#### AI-native creative studios and apps

- **Imaginae Studios** (Fremantle) — AI-native studio; *Art Awakens* project under Google AI Futures Fund.
- **Wonder Studios** — AI-native film studio; $12M raise; Wonder Film Festival.
- **Asteria** (Natasha Lyonne / Lightstorm / Topaz Video) — AI animated short *All Heart*; hybrid AI workflows with Topaz.
- **Promise** (Google-backed) — GenAI filmmaking and VFX for legacy media.
- **Obsidian Studio** (Imagine Entertainment / Ron Howard, Brian Grazer) — AI production partner.
- **Goldfinch enGEN3** — AI cinematic universe platform.
- **Chapter41** (Beta Film / Munich) — AI startup.
- **Kartel** (Kevin Reilly) — AI startup; ex-HBO leadership.
- **Holywater** (Fox Entertainment investment) — AI microdramas.
- **CenterStage** (David Boies / Zack Schiller) — interactive AI entertainment.
- **Superlunar + Eden Studios** — *Little Plastics* dystopian AI film.
- **Particle6** (Eline Van der Velden) — AI-performers studio.
- **Imago Pictures** — 3D + ComfyUI workflows.
- **LKDN AI Production** — node-based AI filmmaking.
- **Deep Fusion Films** (Cardiff) — AI documentary production; acquired by John Gore Studios.
- **Palo Creators** (MrBeast alumni) — AI for viral video creation.
- **Refik Anadol Studio Dataland** — first museum of AI art.
- **Animaj** — Google AI Futures Fund partner for kids' content.
- **Gossip Goblin** — AI filmmaking studio.
- **Critterz** (Vertigo + Federation) — AI-assisted animated-feature production.
- **Filmology Labs** — $250M studio for vertical micro-dramas and AI-driven media formats.
- **escapeAI** (John Gaeta) — streaming apps for AI-generated content across Roku, Fire TV, Samsung and LG.
- **Primordial Soup** (Darren Aronofsky) — AI production studio.
- **Toonstar** — AI animation house.
- **CinemersiveAbout Labs / Cinemersive Labs** — UK machine-learning and computer-vision company; acquired by Sony.
- **My SMASH Media** — AI film startup with Allison Gardner (ex-Glasgow Film Festival).
- **Framestore AI Platform / Framestore Futon** — ML and GenAI in the VFX pipeline.
- **Mito AI** — $4.5M-raised platform empowering video professionals.
- **Filmax DinoGames** — AI-driven 3D animated film project.
- **Abundantia Entertainment + InVideo** — AI film studio launched in India.
- **Luma Production Studio + Wonder Project** — feature collaboration.
- **Lionsgate Chief AI Officer (Kathleen Grace)** — first major-studio CAIO hire.
- **CreateAI** — AI animation production.
- **Netflix Ben Affleck AI Studio Acquisition** — AI filmmaking company acquisition.
- **Holywater** (Fox investment) — AI microdrama studio (also above).
- **DreamLab AI Collective** (the studio that produced this book) — AI-augmented creative practice across film, games and immersive.

#### Games-development AI

- **NitroGen** (NVIDIA + Stanford) — plays-any-game model trained on 40,000 hours across 1,000+ games.
- **SIMA 2** (Google DeepMind) — agent that plays, reasons and learns in 3D virtual worlds.
- **CHORD** (Ubisoft La Forge) — open-sourced end-to-end PBR material generation.
- **Ubisoft Teammates** — voice AI for in-game team communication.
- **YouTube Playables Builder** (Gemini 3) — text-to-game prompt-to-playable web app.
- **Roblox AI Tools / Roblox AI Assistant / Roblox Reality / Metain** — creator-facing AI for game development; Reality is Roblox's productised AI assistant; Metain is the prompt-to-Roblox-Studio interface.
- **Epic xAI Studio** — Elon-Musk-affiliated game-dev AI.
- **General Intuition** — spatial-reasoning research lab.
- **ReBlink ARBO** — AI-powered strategy battler.
- **Halo Studios** — AI woven into the production pipeline.
- **Dabgg** — AI gaming with interactive platform.
- **RosebudAI / Spawn / LudoAI** — vibe-coding games and interactive apps from prompts; Spawn is the "games made with words" community platform; LudoAI is the ideation and planning scaffold.
- **Verse8** — AI-driven game-creation platform.
- **Sett** — AI agents for game marketing.
- **Meta Horizon Studio AI Assistant** — Horizon Worlds creator AI.
- **Gambo** — vibe-coding game agent.
- **Project Motoko** (Razer) — AI-powered gaming headset.
- **Bethesda AI Toolset** — Todd Howard's game-dev AI integration.
- **StarBerry Games / Merge Mayor** — AI-all-in game studio.
- **Astrocade** — interactive entertainment platform; $56M Series B.
- **GameByte** — AI-powered game creation platform; $1M raise.
- **Studio Atelico Bobium Brawlers** — AI-based iOS game with pro-human approach.
- **Bitmagic** — AI-created version of classic Civilization.
- **Helika AI Publishing Engine** — AI publishing engine for game studios.
- **Xbox Game Studios "git gud" AI** — Xbox patent for AI tech that plays games for you.
- **Gaming Copilot** (Xbox) — console AI copilot.
- **NVIDIA DLSS 5** — gaming upscaling.
- **PS5 Pro PSSR** — PlayStation upscaling.
- **Gizmo** (Meta acquisition) — vibe-coding app for creating mini-games.
- **Voyage** (Latitude / AI Dungeon) — AI RPG platform.
- **DoomGen** — prompt-driven DOOM mod prototyping app.
- **Sony AI tools for PlayStation** — animation support, QA automation, asset generation and performance-capture-to-facial-models pipelines.
- **PROWL** (Odyssey) — RL agents for game-world model testing.
- **MagicDawn** (Tencent) — AI lighting tech.
- **ReActor** (Disney) — RL motion-transfer method.
- **Origin Lab** — game-world AI training data; $8M raise.
- **Daughter of the Inner Stars** — Unreal Engine 5 AI-driven game.
- **Genesis AI** — robot cooking and piano playing systems (demonstrating embodied agents).
- **Quilty** — AI platform for script development and assessment.

#### Marketing and advertising AI

- **WPP Open Pro** — agency-wide AI marketing platform.
- **Sightly** — AI advertising and brand performance.
- **Pomelli** (Google Labs) — small-business marketing agent.
- **AdCreative.ai** — mobile pro ad creation.
- **Epiminds** — AI marketing team builder.
- **Octave AI** — AI podcast/radio ad creation.
- **AdsGency** — autonomous paid-marketing agent.
- **Aimy** — AI TV advertising on the Comcast API.
- **Brand Networks** — AI television advertising.
- **Fullthrottle.ai** — automotive-focused DSP.
- **Channel 4 AI ads** — AI-driven TV-advertising tool for SMEs.
- **Sky Studio Challenge** — interactive AI ad creation via Starlink.
- **Google Demand Gen** — AI-powered image tools for the ad platform.
- **Amazon DSP** — AI one-stop-shop advertising infrastructure.
- **Amazon Creative Agent** — agentic ad creator.
- **Playad** — AI marketing agents.
- **Runway Ad Concepter App** — ad-concept and composition exploration.
- **TikTok AI Agents for Ads** — TikTok ad-creation agents.
- **Instagram Edits** — AI video generation for advertisers.

#### Open-source ecosystem and infrastructure

- **ComfyUI** — node-based AI workflow editor; the operating system of the open-source creative AI ecosystem; $17M raise (October 2025), $500M valuation (May 2026).
- **Hugging Face** — open-source model hub; partnerships with Google Cloud and Meta.
- **Meta OpenEnv** — open-source agentic-development environment.
- **PlayCanvas SOG / SplatTransform** — open Gaussian-splat compression and conversion.
- **Civitai / Civision** — community-models and LoRA platforms.
- **LoRA / PEFT / DiffSynth-Studio / Qwen-Image-i2L / Llama Factory / AI Toolkit / LTX-2 Trainer** — fine-tuning frameworks and training pipelines; DiffSynth turns a single image into a custom LoRA; Llama Factory enables zero-code fine-tuning of 100+ models; AI Toolkit covers LTX-2.3 fine-tuning; LTX-2 Trainer is the fal-hosted variant.
- **PyTorch / TensorFlow / Ollama / LLaMA.cpp / MuJoCo** — the open infrastructure layer.
- **Korin AI** — Africa-trained, Africa-built foundation model.
- **DecartAI** — real-time world transformation.
- **Replicate** — model hosting and API marketplace.
- **fal / FAL MCP** — generative-model API platform.
- **llmfit** — hardware scanner for local-model compatibility.
- **Open Vision Agents** — toolkit for building agents that watch, listen and understand video.
- **NotebookLM** — Google's research-and-content-generation surface; cinematic video overviews launched March 2026.
- **OpenAI Gym / Gym Retro / ARC** — research benchmarks (referenced in the games-AI literature).

#### ComfyUI ecosystem — nodes, extensions and workflows

- **Mesh2Motion** (ComfyUI) — mesh-to-motion conversion node.
- **NanoBanana Pro LoRA Dataset Generator** — creates training datasets for image-editing models in minutes.
- **ComfyUI Music Tools** — professional-grade music-processing node pack.
- **ComfyUI HY-Motion1 plugin** — Tencent HY-Motion implementation.
- **ComfyUI Audio Reactive Node Pack** (VisualFrisson) — spatial audio-reactive nodes.
- **ComfyUI-BlendPack** — nodes for video transitions.
- **KJNodes** — use audio as input for LTX-2 inside ComfyUI.
- **WhatDreamsCost ComfyUI Nodes** — LTX sequencer, keyframer.
- **Luminance Keyer Node** — luminance-based keying.
- **Camera Tracking & Body Pose tools (ComfyUI)** — work-in-progress camera and pose tracking.
- **Multiple Angle Camera Control Node** — multi-angle camera control.
- **FeedbackSampler** (Deforum-inspired) — iterative feedback sampling.
- **Day-to-Night with Qwen Edit LoRA** — day/night transformation workflow.
- **Sora 2 API Nodes** — Sora 2 access from ComfyUI.
- **QWEN-AI Compositing** — Qwen-driven compositing workflow.
- **Street View URL Parser** — Google Street View ingestion.
- **Minim** — ComfyUI model-linker extension.
- **Hunyuan 3D 3.0** (ComfyUI partner nodes) — HY3D 3.0 inside ComfyUI.
- **Kling 3.0 ComfyUI node** — Kling 3.0 partner node.
- **Kling Video 2.6 Motion Control** (ComfyUI) — Kling motion control inside ComfyUI.
- **Kling Motion Control 3.0** (ComfyUI) — the v3 motion control variant.
- **Seedance** (ComfyUI partner node) — Seedance inside ComfyUI.
- **LTX-2** (ComfyUI native support) — audio-video model natively supported.
- **LTX-2 ComfyUI Audio-to-Video** — audio-driven video inside ComfyUI.
- **ACE-Step 1.5** (ComfyUI) — full songs in under 10 seconds on <4 GB VRAM.
- **ElevenLabs ComfyUI Partner Nodes** — ElevenLabs inside ComfyUI.
- **Luma Uni-1 ComfyUI Partner Node** — Uni-1 inside ComfyUI.
- **Meshy 6** (ComfyUI native) — Meshy 6 inside ComfyUI.
- **Grok Imagine** (ComfyUI) — xAI image generation inside ComfyUI.
- **MatAnyone2** (ComfyUI) — high-fidelity video matting inside ComfyUI.
- **Tripo 3.1** (ComfyUI partner nodes) — Tripo 3.1 inside ComfyUI.
- **NVIDIA RTX Video Super Resolution Node** — RTX upscaling node.
- **Depth Anything Custom Node** — Depth Anything inside ComfyUI.
- **SAM 3 / SAM 3D ComfyUI integration** — Meta SAM 3 / 3D inside ComfyUI.
- **Sora 2 Full Loop Workflow** — end-to-end Sora 2 pipeline.
- **Krea Nodes** — Krea inside ComfyUI.
- **Gaussian Splats + Qwen Edit workflow** — explore 2D images and generate new camera views.
- **ComfyUI App Mode / ComfyHub** — turn workflows into shareable no-install apps.
- **ComfyUI Simple Mode** — share and iterate complex workflows more easily.
- **ComfyUI Cloud (private models)** — private model hosting inside ComfyUI Cloud.
- **ComfyUI Action Director** — interactive 3D viewport for ControlNet.
- **Complete Style Transfer Handbook (ComfyUI)** — style-transfer guide.
- **VibeComfy** — agents that understand, build and run ComfyUI workflows with Claude.
- **MooshieUI** — beginner-friendly ComfyUI desktop frontend.
- **Creative Control Using ComfyUI on NVIDIA RTX** — NVIDIA's official ComfyUI/RTX tutorial series.

#### LoRAs, fine-tuning and training

- **QwenEdit-2509 Light Transfer LoRA** — simple, powerful image relighting via reference.
- **Qwen-Edit Relighting LoRA** — atmospheric relighting control.
- **Qwen-Image-Edit-2511 Multiple Angles LoRA** — multi-angle perspective generation.
- **Qwen-Image-Edit-2511 AnyPose** — pose transfer from a reference image.
- **QwenEdit-2511 Anything2Real LoRA** — realistic-image transformation.
- **Qwen Edit LoRA Object Removal** — bounding-box-precision edits.
- **Qwen-Image-Edit 2511 Gaussian Splash 3D Camera Motion** — 3D Gaussian-splat motion control.
- **Qwen 2511 Time Travel Workflow** — temporal image effects.
- **NextScene (Qwen Image LoRA)** — cinematic image sequences with natural progression.
- **Best Face Swap (Flux 2 LoRA)** — specialised face-swap.
- **FLUX.2 [klein] LoRAs (fal)** — open-source: Outpaint, Zoom, Object Removal, Background Removal.
- **Krea AI LoRA Trainers** — train LoRAs for Qwen-2512 and Z-Image inside krea.ai.
- **LTX-2.3 Character LoRA Training (AI Toolkit)** — character LoRA training tutorial.
- **Gaussian Splats Repair LoRA** — Klein-9b LoRA for repairing 3D views and geometry.
- **LTX 2.3 Colorizer (LoRA)** — black-and-white footage colorisation.
- **Music Finetunes in ElevenCreative** — stylistically consistent vocal and instrument generation.

#### Provenance, watermarking and detection

- **C2PA** (Content Authenticity Initiative / Adobe-led) — cryptographic provenance metadata standard.
- **SynthID / SynthID Verification** (Google DeepMind) — synthetic-content watermark; deployed across Veo, Lyria and Imagen; verifiable inside Gemini.
- **YouTube AI Detection / YouTube AI Deepfake Detection** — automated AI-content detection; *Tiny Grandma* false-positive case study.
- **Deezer AI Music Detection** — identifies up to 75,000 fully AI-generated uploads per day.
- **Spotify AI Transparency Beta** — voluntary disclosure feature.
- **Beeble** — detection and watermarking tools.
- **Cloudflare AI Bot Classification** — public-web infrastructure tracking AI crawlers.
- **Human Provenance AI Disclosure Standard (Cannes)** — industry-coordination labelling standard.

#### Consumer surfaces and distribution platforms

- **Sora iOS app** (OpenAI) — TikTok-style AI video remix; 1M downloads in 5 days.
- **CapCut / Dreamina** (ByteDance) — consumer video editing + AI generation.
- **Gemini app** (Google) — Google's consumer AI surface.
- **ChatGPT app** (OpenAI) — mobile ChatGPT; Shazam integration.
- **Perplexity AI** — Samsung Smart TV AI assistant integration; consumer AI search.
- **Grok / Grok Imagine** — xAI consumer surfaces.
- **TikTok / Reels / Shorts** — AI-content distribution surfaces.
- **YouTube Shorts / YouTube Create** — destinations for Veo 3.1 Ingredients-to-Video.
- **Bandcamp** — banned AI music outright, January 2026.
- **Deezer** — published the 44%/3% data; built and licensed AI-music detection.
- **Spotify** — declined an AI-music filter; voluntary disclosure beta; *Personal Podcasts* agent feature.
- **YouTube Music** — labelling, the AI Detection Tool, viewership of AI content.
- **Steam** — AI-content labelling controversy; *Clair Obscur* Game of the Year stripping.
- **Sweden's Official Music Chart** — banned AI-generated entries.
- **San Diego Comic-Con** — banned AI art at the 2026 event.
- **Roblox** — creator-tools AI with continued controversy.
- **Fortnite** — Chapter 8 AI-art controversy; Disney partnership.
- **Netflix** — AI in production (de-aging, plates, retention engine, Ben Affleck studio acquisition).
- **Disney+** — user-generated AI content features.
- **Luna** (Amazon) — AI-powered Snoop Dogg game.

#### Studios, programmes, festivals and institutional infrastructure

- **Sundance AI Literacy Initiative** — Google-funded $2M creator-training programme; Sundance Collab learning, Story Forum, Ignite Day.
- **UCL / RCA / Brandtech Centre for Creative AI** — UK research hub.
- **AIMICI Training Program** — ScreenSkills-accredited AI training.
- **AI FilmFest Japan** — annual AI-film festival.
- **Dubai AI Film Award** — $1M prize won by Tunisia's *Lily*.
- **Cannes AI Disclosure Standard / Cannes Lions** — industry coordination for AI labelling; Luma Dream Brief $1M prize.
- **Future Vision Film Competition** — Google / XPRIZE / Range Media collaboration.
- **Runway AI Festival** — film and creative-discipline awards.
- **Wonder Film Festival** — AI-native film festival.
- **Academy of Motion Picture Arts and Sciences** — "you must be human to win" rule.
- **Television Academy / Emmys** — AI guidance for submissions.
- **SAG-AFTRA** — contract negotiations and the Tilly Tax.
- **Equity (UK)** — strike ballot; 99% vote in favour.
- **PRS for Music AI Survey 2026** — UK music-creator sentiment data.
- **GEMA** — German rights society; won against OpenAI.
- **Splice + UMG** — sample library; AI-music tools partnership.
- **Stability AI + Universal Music / Stability AI + Warner Music** — alliance and deal on the AI-music side.
- **Vizrt Viz One 8.1** — broadcast AI features.
- **Tesseract** — AI platform at MIPCOM.
- **Sphere + Google Cloud** — AI technology behind the *Wizard of Oz* experience.
- **Anthropic Joins Blender Development Fund** — patronage deal, May 2026.
- **Sony AI ICASSP papers** — music-understanding and generative-audio research, April 2026.
- **Google Flow Music + Believe Partnership** — AI music distribution partnership.

#### Techniques, methods and recurring workflows

- **Vibe Coding** — prompt-led creative prototyping, especially for games and interactive apps; Rosebud, Spawn, Gizmo, Gambo are the canonical surfaces.
- **Trajectory Control (ATI)** (Wan / Qwen) — control of video trajectories at frame and clip level.
- **Reference-to-Video** (Veo 3.1 + Gemini) — consistent character generation from a reference image.
- **Motion Control nodes / Time-To-Move** — frame- and segment-level motion controls in generated video.
- **Layer Separation & Live Editable Text (LET)** (Loveart) — extract and edit text and subjects from images as PSD layers.
- **Temporal Reasoning** (NVIDIA ChronoEdit) — physics-aware edits and world simulation.
- **Practical Light Control** (PractiLight) — foundational diffusion for relighting.
- **3D Gaussian Splatting** — the spatial backbone running through PlayCanvas SOG, Hyperscape, Apple Personas and the open-source splat ecosystem.
- **World Models** — recurring topic spanning Marble, Genie, HY-World, UNI-1, ECHO, Matrix-Game, LingBot-World, Moonlake.
- **Multi-Shot Consistency** — Kling 3.0, ShotVerse, Higgsfield Shots, Veo 3.1 — the multi-shot turn that defined the spring-2026 video pipeline.
- **Camera Control / Multi-Angle Generation** — WAN Camera Control, ShotVerse, ATI, Multiple Angle Camera Control Node.
- **Style Transfer (the ComfyUI handbook)** — the canonical workflow ladder for style transfer.
- **Audio-Reactive Generation** — Audio Reactive Node Pack and the Lalal-API / ACE-Step pipelines.
- **Real-Time Generation Pipelines** — Krea Realtime, MotionStream, Decart Lucy 2.0, Xmax X1, Phoenix-4, LTX-2.3 Real-Time on Scope; the *interactive-generation* category that emerged in Q1 2026.
- **Agentic Workflows / Multi-Agent Stacks** — Sony Game Studios (49 agents, 72 skills), Adobe CX Enterprise, OpenAI AgentKit, Heygen Video Agent, Claude Skills.
- **Provenance-First Capture** — C2PA + SynthID + on-device detection in Premiere and YouTube as the emerging *standard* of provenance-aware production.
- **Music Stem Separation as a primitive** — Lalal AI, StemDeck, BandLab — stem separation moving from end-product to upstream primitive.
- **MCP (Model Context Protocol) as the connective tissue** — Unity MCP, Blender MCP, fal MCP; the protocol the agentic creative ecosystem is converging on.
- **Brief-First, Generate-Second** — the workflow practice the book argues for in Chapter 11 (and Chapter 16's *toolchain in layers* section below).

This is the catalogue. By the time you read it, it will be incomplete — new tools have shipped, some on this list have been bought, renamed or killed. Treat it as a snapshot of one year of toolchain at the moment the toolchain became a stack rather than a list, and use it to orient yourself in whatever the state of play is when you pick the book up.

For a deeper analytical treatment of the adoption telemetry behind many of these tools — Firefly's 22B-asset growth curve, ChatGPT's 800–900M WAU figures, the Veo / Sora professional split, the GDC sentiment-vs-usage divergence — see [Appendix E: Dynamics of Generative AI Adoption](A5_Deep_Dive_Adoption_Dynamics.md).

### How to build a toolchain you can defend

The last thing I want to say in this chapter is something I have said in talks more often than anything else, because working creatives ask me this question, in some variant, every week.

*How do I decide what tools to use, in a market that is changing this fast, without burning my whole month re-learning interfaces?*

My short answer is: build the toolchain in *layers*, and accept that the layers move at different speeds.

The bottom layer — your foundation model, your modality stack, your agent platform — will change frequently. Treat it as ephemeral. Pick the best tools available *this quarter* and be ready to swap them next quarter.

The middle layer — your creative software (Adobe / Unreal / DaVinci / Pro Tools / Blender / Logic) — will change more slowly, and is the layer in which the AI capability will be progressively absorbed. Treat it as the long-term home of your craft. Learn it deeply.

The top layer — your *judgement*, your *taste*, your *briefing skill*, your *integration sense* — does not change. It is the layer the agents cannot copy, the layer the platforms cannot ship and the layer the next model release does not depreciate. Spend more time here than the toolchain wants you to.

The mistake I see working creatives make most often is to over-optimise the bottom layer and under-invest the top. The platform companies want you to spend your working hours chasing the new model release; the work that pays the bills, the work that finds an audience, and the work that survives a transition is built on the layer the platform companies cannot reach.

The toolchain, in the end, is the means. The work is the end. The tools change. The work, if it is any good, lasts.

That is the working operating model my studio has run on for the period this book covers. It is the model I would commend to anyone building, this year or next, a creative practice that survives the rest of the decade.

The transition is going to keep going. The tools will keep changing. The work that matters, on the other side, will be made by the people who kept their attention on the right layer.

[^1]: OpenAI, "Sora 2 is here," 30 September 2025. <https://openai.com/index/sora-2/>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^2]: LinkedIn News aggregation: "Sora Tops 1 Million Downloads in 5 Days." <https://www.linkedin.com/news/story/sora-tops-1m-downloads-in-5-days-6684988/>. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md).

[^3]: Google DeepMind, Veo 3.1 launch, mid-October 2025. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md).

[^4]: Runway product cycle: Gen-4.5 (December 2025), Gen-4.5 Image-to-Video (January 2026), Workflows, Story Panels, Characters API, Apps for Advertising — *Dream Machine* Issues [10](../Dream%20Machine%20MD/10.md), [14](../Dream%20Machine%20MD/14.md), [15](../Dream%20Machine%20MD/15.md), [16](../Dream%20Machine%20MD/16.md), [20](../Dream%20Machine%20MD/20.md).

[^5]: Runway CEO on indie films vs. blockbusters, [*Dream Machine* Issue 26](../Dream%20Machine%20MD/26.md).

[^6]: Chinese open-source AI video model releases, 2025–2026. *Dream Machine* Issues [3](../Dream%20Machine%20MD/3.md), [12](../Dream%20Machine%20MD/12.md), [22](../Dream%20Machine%20MD/22.md).

[^7]: *SiliconAngle*, "Higgsfield raises $80M on $1.3B valuation." <https://siliconangle.com/2026/01/15/higgsfield-raises-80m-1-3b-valuation-scale-ai-video-platform/>. *36kr*, "Higgsfield: Earns $200M in 9 Months." <https://eu.36kr.com/en/p/3650517574312323>. *Dream Machine* Issues [15](../Dream%20Machine%20MD/15.md), [16](../Dream%20Machine%20MD/16.md).

[^8]: Heygen Video Agent. <https://www.linkedin.com/posts/heygen_introducing-the-new-video-agent-activity-7421597801240801282-d1CF>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^9]: TechCrunch, "Synthesia hits $4B valuation, lets employees cash in." <https://techcrunch.com/2026/01/26/synthesia-hits-4b-valuation-lets-employees-cash-in/>. *Sifted*, "Synthesia rejects $3bn Adobe acquisition offer." <https://sifted.eu/articles/synthesia-acquisition-offer>. *Dream Machine* Issues [5](../Dream%20Machine%20MD/5.md), [16](../Dream%20Machine%20MD/16.md).

[^10]: ElevenLabs $500m ARR reporting, April 2026. [*Dream Machine* Issue 25](../Dream%20Machine%20MD/25.md).

[^11]: Adobe Firefly milestone data, in [*Dynamics of Generative AI Adoption*](A5_Deep_Dive_Adoption_Dynamics.md), §"The Ubiquity of AI in Visual and Digital Arts."

[^12]: Nano Banana inside Photoshop and inside Unreal Engine cross-integrations, October–November 2025. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^13]: Suno Studio launch. <https://www.techradar.com/ai-platforms-assistants/i-tried-suno-studio-the-new-platform-that-mixes-ai-music-generation-with-hands-on-editing-like-garageband-but-smarter>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^14]: Mureka, "Music Agent Studio" launch. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^15]: ElevenLabs Series funding, April 2026. [*Dream Machine* Issue 25](../Dream%20Machine%20MD/25.md).

[^16]: *MusicTech*, "Cardiff band speaks out after AI artist trained on their music outperforms them on Spotify." <https://musictech.com/news/industry/its-shocking-disheartening-and-insulting-cardiff-band-speaks-out-after-ai-artist-trained-on-their-music-outperforms-them-on-spotify/>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^17]: Variety, "AI Creator Behind Viral 'Deadpool,' 'Harry Potter' Christmas Clip Made His Film in a Ukrainian Bomb Shelter." <https://variety.com/2026/digital/news/ai-video-deadpool-harry-potter-andrii-daniels-1236624632/>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^18]: Music industry AI deal flow, October 2025 – May 2026. See Chapter 5 footnotes 31–37, and *Dream Machine* Issues [5](../Dream%20Machine%20MD/5.md), [7](../Dream%20Machine%20MD/7.md), [8](../Dream%20Machine%20MD/8.md), [12](../Dream%20Machine%20MD/12.md), [14](../Dream%20Machine%20MD/14.md), [16](../Dream%20Machine%20MD/16.md), [17](../Dream%20Machine%20MD/17.md).

[^19]: World Labs, "Bringing Marble to Life." <https://www.worldlabs.ai/case-studies/bringing-marble-to-life>. [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md).

[^20]: Sony Pictures Marble VP integration. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^21]: Google DeepMind, "Genie 3." <https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/>. Project Genie: <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/>. *Dream Machine* Issues [3](../Dream%20Machine%20MD/3.md), [17](../Dream%20Machine%20MD/17.md).

[^22]: Tencent, "HY World 1.5" and Hunyuan 3D Studio. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md).

[^23]: Luma AI, *UNI-1* launch, March 2026. [*Dream Machine* Issue 22](../Dream%20Machine%20MD/22.md).

[^24]: SuperSplat / Spark 2.0 / SOG releases through 2025–26. *Dream Machine* Issues [1](../Dream%20Machine%20MD/1.md), [25](../Dream%20Machine%20MD/25.md).

[^25]: Radiance Fields, "Apple Confirms that it's Gaussian Splatting that powers their personas." <https://radiancefields.com/apple-confirms-personas-use-gaussian-splatting>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^26]: ComfyUI Blog, "Ubisoft La Forge Open-Sources the CHORD Model." <https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model>. [*Dream Machine* Issue 11](../Dream%20Machine%20MD/11.md).

[^27]: Anthropic / Blender Foundation patronage, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^28]: OpenAI, "Introducing AgentKit." <https://openai.com/index/introducing-agentkit/>. [*Dream Machine* Issue 2](../Dream%20Machine%20MD/2.md).

[^29]: Anthropic Skills framework. *Dream Machine* Issues [11](../Dream%20Machine%20MD/11.md), [16](../Dream%20Machine%20MD/16.md), [29](../Dream%20Machine%20MD/29.md).

[^30]: Heygen Video Agent. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^31]: Adobe Summit 2026 CX Enterprise. [*Dream Machine* Issue 26](../Dream%20Machine%20MD/26.md).

[^32]: Adobe + NVIDIA / Google + NVIDIA partnerships. [*Dream Machine* Issue 21](../Dream%20Machine%20MD/21.md).

[^33]: ComfyUI funding round. <https://www.linkedin.com/posts/comfyui_we-raised-17-million-to-build-an-os-for-ugcPost-7373743341236236288-wkCc>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^34]: ComfyUI $500M valuation, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^35]: Hugging Face / Google Cloud and Meta / Hugging Face OpenEnv. *Dream Machine* Issues [5](../Dream%20Machine%20MD/5.md), [8](../Dream%20Machine%20MD/8.md).

[^36]: Unreal Engine 5 official AI Assistant. <https://www.linkedin.com/posts/wouterweynants_theres-an-official-ai-assistant-coming-to-ugcPost-7369377204226379776-pGiH>. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md).

[^37]: Unity AI Council (October 2025); Unity AI Open Beta (May 2026). *Dream Machine* Issues [1](../Dream%20Machine%20MD/1.md), [28](../Dream%20Machine%20MD/28.md).

[^38]: VFX AI integration metrics. See [*Dynamics of Generative AI Adoption*](A5_Deep_Dive_Adoption_Dynamics.md), §"Visual Effects (VFX) Automation."

[^39]: Anthropic / Blender Foundation patronage. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^40]: Andreessen Horowitz pitch-deck observations on Chinese open-source model usage. <https://www.linkedin.com/posts/stevenouri_a-wild-stat-80-of-startups-pitching-a16z-activity-7396182718998351872-xTKR>. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^41]: Korin AI launch, May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^42]: Google DeepMind, "Introducing Gemini Omni: Create Anything from Any input." <https://blog.google/technology/google-deepmind/gemini-omni-launch/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^43]: Beeple Canvas — Generative AI compositor. <https://www.beeple-canvas.com/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^44]: Sony AI, "Woosh — a sound effect foundation model." <https://ai.sony/blog/woosh-sound-effect-foundation-model/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^45]: Mirelo SFX 1.6, "edit sound, not just generate it." <https://mirelo.ai/sfx-1-6>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^46]: Stability AI, "Stable Audio 3.0 released — open-weight model family built for artistic experimentation." <https://stability.ai/news/stable-audio-3-0-released>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^47]: Tamber product page: <https://tamber.ai/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^48]: Beatport Track ID. <https://www.beatport.com/track-id>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^49]: NVIDIA SANA-WM model collection. <https://huggingface.co/collections/nvidia/sana-wm>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^50]: Odyssey, "Introducing Starchild-1, the first real-time multimodal world model." <https://odyssey.ml/introducing-starchild-1>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^51]: Odyssey, "Introducing Agora-1 — four-player AI-generated world built on a 1997 shooter." <https://odyssey.ml/introducing-agora-1>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^52]: Apple Machine Learning Research, "Apple Headsup: a Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures." <https://machinelearning.apple.com/research/apple-headsup-3d-gaussian-head>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^53]: Google, "Official skills for AI agents." <https://github.com/google/agent-skills>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^54]: Tencent Ardot, AI-native design agent platform. <https://ardot.tencent.com/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^55]: Anthropic, "Claude is now available as a partner node in ComfyUI." <https://www.anthropic.com/news/claude-comfyui-partner-node>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^56]: ECABridge — Unreal Engine MCP integration. <https://ecabridge.dev/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^57]: *Video Games Chronicle*, "Epic Games Veteran Claims He's Building AI-Heavy 'Fully European' Game Engine." <https://www.videogameschronicle.com/news/epic-games-veteran-ai-heavy-fully-european-game-engine/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^58]: PhotoGIMP — the open-source GIMP skin that mimics Photoshop. <https://github.com/Diolinux/PhotoGIMP>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).
