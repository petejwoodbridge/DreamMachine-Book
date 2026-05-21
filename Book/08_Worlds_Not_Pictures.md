# Chapter 8

## Worlds, Not Pictures

If you had asked me, in the autumn of 2025, what the most important AI release of the year was going to be, I would have said something obvious — Sora 2, or Veo 3.1, or one of the music models, or one of the editor-class tools like Runway Gen-4.5 or Adobe's new Firefly. Something that turned a prompt into a thing you could put on a screen.

Six months later, I don't think I would say any of those.

I think the most important release of the period this book covers was something that almost nobody outside of a relatively small community of practitioners noticed at the time, that produced no viral videos, that did not change the news cycle for a single day, and that I have come, over the course of the winter, to think of as the *actual* future of creative work: the public launch of **Marble**, by Fei-Fei Li's company **World Labs**, in November 2025.[^1]

Marble doesn't make videos. Marble makes worlds.

I want to spend this chapter on why that distinction is, in my view, the most strategically important one in creative AI right now, and why almost everything else in the toolchain — from generative video to AI music to the digital-human work in advertising — eventually has to be re-thought in its shadow.

### What a world model actually is

The phrase "world model" sounds like a marketing term. It isn't, exactly. It is a category of AI system that researchers have been chasing for the better part of a decade, and that — as of late 2025 — finally started shipping as production-ready software.

A generative *video* model takes a prompt and produces a sequence of frames. The frames are coherent because the model has learned the statistical regularities of video: things move smoothly, light behaves more or less correctly, faces stay faces. But the output is *flat*. It is a particular sequence of pixels. You cannot navigate it. You cannot move the camera. You cannot pick up the lamp on the table and look at the wall behind it.

A *world* model takes a prompt — or an image, or a video, or a rough 3D layout — and produces a *navigable three-dimensional environment.* You can move through it. You can change the camera angle. You can, depending on the model, walk around the table, look at the wall behind the lamp, and find that the wall continues to exist in a consistent way that the model didn't have to generate for you because it understood, structurally, that walls have backs.

The technical core, in the most common implementation, is **Gaussian splatting** — a representation where a scene is stored as a cloud of millions of tiny semi-transparent ellipsoids, each carrying colour and position information. The whole scene can be rendered in real time from any angle, because the system isn't drawing 2D pixels; it is rendering a structured 3D world. The output, in turn, can be exported as a splat file, as a mesh, or — if you want — as a flat video.[^2]

This is the part that took me, even as a working creative technologist, embarrassingly long to fully understand. Video is a *projection* of a world. A world is the more fundamental object. For two and a half years, the public-facing AI conversation has been about generating better projections. The actual capability landscape has been moving, in parallel, towards generating the worlds themselves.

When the worlds become cheap to generate, the projections — the videos, the images, the renders — become *outputs of the worlds*, not the primary medium. The whole production stack inverts.

### Marble, from the inside

DreamLab — the studio I run in the North West of the UK — has been a beta participant in Marble since October 2025, in the months before its public release.[^3] I want to share what that experience actually felt like, because the *technical* description of a world model and the *practitioner's* experience of using one are different in ways that matter for understanding what is happening to the toolchain.

Imagine, for the sake of example, that I am working on a client project that needs a scene of a market square at dusk in a Mediterranean town. In the old pipeline — which is to say, the pipeline of 2024 and most of 2025 — that brief would translate into something like the following:

A concept artist would produce a moodboard. A 3D artist or a virtual-production house would build a CGI version of the square, populated with assets either bought from a marketplace or modelled bespoke. Lighting would be set up in Unreal or Maya. The whole scene would be rendered out as a video plate or used as a backdrop on an LED volume. If any change was required — *can we move the camera left a bit, see what's on that side* — the rebuild was non-trivial.

In Marble, the same brief unfolds differently. I type, or paste in a reference image, or upload a quick phone-shot panorama of an actual market square I visited last year. Marble generates a complete, navigable 3D environment of that square. It exists, persistently, as a file on my account. I can move my virtual camera anywhere in it. I can hand it to a director and say *walk through this and tell me where the camera lives.* I can export the result as a Gaussian splat, drop it into Unreal Engine via SuperSplat or one of the other Gaussian-splat editors,[^4] and use it as the lit backdrop for an LED-volume shoot. I can also, if I just want a plate, render a flat video from a chosen camera move.

The economic implication is this: the cost of having "a place" — a navigable, lit, persistent environment with depth — has dropped, in twelve months, by something between one and two orders of magnitude. The thing that used to require a four-person team and a fortnight now requires a prompt and the time it takes a model to render.

This is not a marginal improvement to virtual production. It is a *category* change. The bottleneck of virtual production has, for the entire history of the discipline, been the cost and time of building the environment. When that bottleneck goes, what remains is exactly the human craft that the audience is paying for: blocking, performance, direction, lighting design, story.

In [**Issue 8**](../Dream%20Machine%20MD/8.md) of the newsletter, I noted that Sony Pictures had begun using Marble inside its virtual-production pipeline. The number the team quoted publicly was the one that should have made the front page of every trade publication: *40× faster than the traditional workflow.*[^5] If you sit inside the legacy economics of a virtual-production house — where building a single environment is a six-figure, multi-week proposition — that number is not an improvement. It is a *re-platforming* of the discipline. In [**Issue 12**](../Dream%20Machine%20MD/12.md), Disney showed off a "300,000 poses in an instant" demonstration that was conceptually similar — animation built on top of generative spatial infrastructure rather than against it.[^6] In [**Issue 27**](../Dream%20Machine%20MD/27.md), Netflix and Eyeline released **Vista4D**, a system that converts live-action footage into navigable 4D point clouds.[^7] The pattern is the same across the studios: a quiet pipeline shift, not a marketing story, that takes the entire "building the environment" stage out of the critical path of production.

### The world-model race

Marble was the first commercial product in this category, but it was not the only one. The autumn of 2025 and the spring of 2026 were essentially a foot-race between research labs to ship usable world models, and the pace of releases was so rapid that the *Dream Machine* readers' WhatsApp group routinely had three or four new ones to discuss per week.

**Google DeepMind**'s **Genie 3**, named by *Time* as one of the best inventions of 2025, generated playable 3D worlds at 24 frames per second from text prompts, with consistency held for several minutes — and in January 2026 was made publicly available to Google AI Ultra subscribers in the U.S. through a prototype web app called Project Genie. At Google I/O 2026, **Project Genie** was extended with a **Street View** integration that lets users generate navigable simulations of real-world locations directly from Street View map data, collapsing the gap between *the world that exists* and *the world that can be generated.*[^8] **Meta** announced **WorldGen** in November 2025, framed as research that could generate walkable 3D worlds from prompts like *"medieval village town square."*[^9] **Tencent** open-sourced **HY World 1.5**, a real-time world model framework, in December 2025, alongside the **Hunyuan 3D Studio** which integrated the company's art-grade 3D generative model **3D-PolyGen 1.5**.[^10] **SpAItial** launched **ECHO**, a spatial foundation model, in December 2025.[^11] Stanford AI Lab and others released **Wonderzoom** in January 2026, a multi-scale 3D world-generation model that let you "infinitely zoom into the details" of a generated environment.[^12] **OpenArt** launched its own world-generation product, **Worlds**, in March 2026.[^13]

The May 2026 wave was the most aggressive yet. **NVIDIA** released **SANA-WM**, a 2.6B-parameter open-source world model natively trained for 60-second video generation with explicit camera control — the first open-weight world model at meaningful scale, and a development whose long-term implications for the open-source-AI-tooling argument I make in [Chapter 16](16_The_Tools.md) are, in my view, substantial.[^26] **Odyssey** released **Starchild-1**, which it described as *"the first ever real-time multimodal world model"* — a system that doesn't just generate a world but understands and simulates it.[^27] **Apple** published **Headsup**, a large-scale, high-quality 3D Gaussian-head reconstruction pipeline built from multi-view captures of the kind a consumer iPhone can already produce — a continuation of the Apple-Personas-and-Gaussian-splat thread above.[^28] At the consumer end of the same wave, **WorldLens VR** rolled out an AI-powered Quest feature that adds subtle 3D depth to ordinary Google Street View environments, making the existing planetary-scale street-imagery dataset navigable in VR.[^29]

The most ambitious of all of these — and the one I think hints most clearly at where the category is going — was **Luma AI**'s **UNI-1**, launched in March 2026 with the framing: *"When worlds become instant, the race shifts to better thinking."*[^14] UNI-1 was the first commercial release I am aware of that *combined* world-model generation with what Luma called "reasoning" — that is, the model didn't just generate a scene, it could plan, modify and iterate on the scene as a coherent agent. The pitch was that you would no longer have a fragmented pipeline of prompt → image → video → iterate; you would have a single unified creative system that thought before it created.

UNI-1 is, in my view, the most important *category* announcement of the spring of 2026, even if the product itself is still rough at the edges. It is the announcement that says: world models are not the end state. They are the *substrate* on which something else — reasoning-led generative creativity — gets built.

By **May 2026**, you could find world-model capabilities embedded in the consumer tools as well. **CapCut**, the consumer-grade video editing app, integrated ByteDance's *Seedance 2.0* via the *Dreamina* product, giving phone-users the ability to generate spatial scenes alongside flat video.[^15] **Spark 2.0**, an open-source Gaussian-splat streaming framework, brought 100-million-splat scenes to web browsers at interactive frame rates.[^16] **Apple** confirmed in October 2025 that its Personas feature on Vision Pro and other devices was powered by Gaussian splatting under the hood, making this — for the millions of Apple device owners who had used the feature without knowing what it was — the most-deployed Gaussian-splat technology in consumer hardware.[^17]

The category, in eight months, went from a research demo to a consumer feature.

### The games industry, again

If world models are infrastructure, the industry that has been waiting for that infrastructure the longest is games.

The 2024 conversation in games about generative AI was, in significant part, about *flat assets* — concept art, textures, dialogue, music — and it was the conversation that produced most of the backlash. *Call of Duty: Black Ops 7*'s loading screens. *Anno 117*'s placeholder art "slipping through" the review process. *Fortnite*'s Chapter 8 controversy.[^18] The audience response, in every case, was visceral, and the studios learned, the hard way, that AI-generated 2D assets dropped into established franchises read to fans as a cost-cutting move, not a creative one.

The 2025–26 conversation in games is different in kind, because the AI is now being aimed at the *substrate* of the game — the worlds, the systems, the NPCs, the procedural infrastructure — and the audience response is, so far, much more nuanced.

**NVIDIA**, in partnership with Stanford, released **NitroGen** in January 2026 — a "plays-any-game" AI trained on 40,000 hours of gameplay across more than 1,000 games. The model wasn't being pitched as a way to *replace* games; it was being pitched as the foundation layer for a new generation of AI-aware game agents and procedural systems.[^19] **Google DeepMind**'s **SIMA 2**, released in November 2025, was an agent that could play, reason and learn alongside humans in virtual 3D environments.[^20] **Ubisoft** open-sourced its **CHORD** model in December 2025, for end-to-end PBR material generation, and ComfyUI nodes built on top of it within the same week.[^21] **Ubisoft's Teammates** — a voice AI tech demo first shown in November 2025 — promised a step-change in how NPCs would behave in next-generation titles. The team lead's hands-on framing, given to *Video Games Chronicle*, is the one I keep returning to: *"It's a tool first. We've been working on it for more than two years now, and our conclusion is that it's a super cool tool, but it's still a tool."*[^22] *Still a tool.* The whole AI-in-games debate, compressed into four words by the people inside Ubisoft who are actually building the thing.

The most interesting single release of the spring of 2026 was **YouTube's Playables Builder**, a closed-beta product launched in December 2025 that lets users create games with short text, video or image prompts, built on Gemini 3.[^23] The framing, when YouTube's product team described it publicly, was that *every YouTube creator* should have the ability to ship a playable game as easily as they currently ship a video. Within months, **Unity** announced an "AI Open Beta" — an in-editor AI suite that brought the same logic to the professional games-development pipeline.[^24]

Where this lands, in 2027 and 2028, is the question I find the most strategically charged in the whole industry. If creating a playable, navigable world becomes a thing a YouTube creator can do in an afternoon, the boundary between *games* and *video* — which has been collapsing slowly for fifteen years, through platforms like Roblox and Fortnite and the proliferation of interactive content on social platforms — collapses fully. The next generation of creators will not think in terms of *making a video* or *making a game.* They will think in terms of *making a thing*, and the thing will, by default, be navigable.

### What this means for film

I want to come back to film for a moment, because I think the consequences of world models for the film industry are bigger than the consequences for any other sector, and the least understood.

For the entire history of cinema, the discipline has been organised around a fundamental scarcity: *the cost of building the location.* Even when the location was real — a city street, a forest, a beach — capturing it required a crew, a lighting team, transport, permits, weather contingencies. When it wasn't real — when it was a sound stage, or a digital matte painting, or a CGI environment — the cost was, if anything, higher.

The entire industrial structure of cinema, from the location department to the gaffer's crew to the virtual-production house, exists because *the place is expensive to make.*

When the place becomes cheap — when a Marble-generated environment, exported as a splat, dropped into Unreal, lit interactively, can substitute for a $200,000-per-day exterior shoot at almost any quality bar a hero shot — the industrial structure that organised cinema starts to look like the manuscript-copying scriptorium did in 1450. The thing that was the bottleneck is no longer the bottleneck.

What replaces it? My best guess, six months into the transition, is *taste in places.* If everyone can generate a market square, the value of *choosing the right market square* — the one with the texture, the light, the cultural specificity, the lived-in-ness that makes a scene feel like it belongs to a real human story — becomes the new scarce skill. The location scout becomes the *world curator.* The production designer becomes the *spatial director.* The cinematographer becomes — even more than they already are — the person whose job is to find the *one camera move* in a near-infinite navigable space that tells the story.

This is, I think, an upgrade for the craft, not a downgrade. It moves the human contribution to the part of the work that humans actually do well — *judgement about what matters in a place* — and offloads the part of the work that has been a manufacturing problem for a hundred years.

### The risk

I want to flag the risk too, because I am trying — and I am sure I will not always succeed — to be honest about the downsides.

If world models become the substrate of creative work, the *training data* for those models becomes a question of enormous cultural consequence. A world model trained on, say, the visual archive of Hollywood will generate scenes that look like Hollywood. A world model trained on the photographic archive of Mumbai will generate scenes that look like Mumbai. The *aesthetic monoculture* that the early image-generation models produced — that vaguely Pixar-flavoured, vaguely Marvel-flavoured, vaguely YouTube-thumbnail look that you can recognise in a thousand 2024 AI outputs at a glance — is at risk of being amplified, not reduced, when the medium moves from images to navigable spaces.

The companies that own the largest world-model training datasets in 2030 will, in a real sense, own the visual language of the next generation of cinema, games and immersive media. If those datasets are biased — towards English, towards the global North, towards Hollywood production design, towards the architectural and cultural visual vocabulary of a small number of wealthy cities — the entire interior life of the next generation of creative work will reflect those biases.

This is not a hypothetical. We are seeing it now. The publicly available world models, in mid-2026, do a startlingly good job of generating "Mediterranean market square" and "American suburb" and "Tokyo street at night." They do a startlingly *thin* job of generating, say, "Lagos street at dusk during the rains" or "a contemporary Indigenous Australian community space" or "a Manchester terraced street in winter with the sodium lights coming on." The bias is in the training, and the training is in the assets, and the assets were in the corpus, and the corpus was English-internet-skewed.

If we want the next creative economy to look like the world rather than like the AI companies' biggest source datasets, the dataset question has to be a *first-order* design problem. Korin AI's late-2025 launch — "trained with African datasets, built by Africans" — is the kind of intervention that is going to have to multiply.[^25] So is the African Tech / India / Singapore-led wave of culturally-specific AI cinema that the trade press started covering in Issues [20](../Dream%20Machine%20MD/20.md) through [27](../Dream%20Machine%20MD/27.md). Diversity in training datasets, for the world-model era, is not a content-moderation question. It is a *cultural infrastructure* question.

### Six craft questions for the world-model era

Before I make the big claim, I want to put six craft questions on the page that working creatives — directors, designers, art directors, cinematographers, sound designers, level designers — will, by my estimate, be wrestling with for the rest of the decade. They are the world-model-era equivalents of the craft questions the *cinematographic* era took fifty years to develop a vocabulary for (where do you put the camera, how do you light the scene, how does the cut work, how does the sound do its work). The world-model era has, in 2026, no settled vocabulary for any of them. The vocabulary will be built by the working creatives who notice the question first.

**One. Where does the audience stand?** The most-overlooked craft question of the navigable-space era. A film positions the camera; the camera positions the audience. A world model produces a *navigable space*; the question of where the audience *enters* the space, where they are *invited* to stand, what they are *encouraged* to look at, is no longer fixed by the cinematographer. It is fixed — if it is fixed at all — by the *narrative scaffolding* the orchestrator builds around the navigable space. Marble's October-2025 update added explicit *suggested-camera-pose* primitives for exactly this reason. The craft question is which of those poses to specify and which to leave to the audience.

**Two. How does the cut work in a navigable scene?** The film cut depends on the audience being in a fixed position; the editor moves the camera between fixed positions in a way that the audience's eye follows. The navigable scene has, by default, no cut. The audience moves through it continuously. The craft question — for working directors and editors — is when to *break* the continuity, how to do so in a way the audience reads as deliberate rather than as a technical glitch, and what new grammar of transitions a navigable medium permits. Some early experiments in 2025–26 have used *spatial discontinuities* (an audience walks through a door and emerges in a different space) and *temporal discontinuities* (the same space at different times) as cuts. None of these has yet stabilised into a shared grammar.

**Three. How does performance survive the medium?** A film performance is captured by a camera at a fixed angle and pace. A world-model performance — a synthetic actor performing inside a navigable scene — has to be authored such that the performance *works* from every angle and every speed at which the audience might encounter it. This is, for working performers and motion-capture supervisors, an entirely new craft challenge. The film-era cliché of the actor "playing to the camera" is, in the world-model era, replaced by *playing to the spatial neighbourhood* — knowing that the audience may be six feet away, may be inside the actor's eyeline, may be behind the actor's shoulder, may be looking at the actor from above. Volumetric capture (Vista4D's live-action 4D reconstruction, NVIDIA's D-Rex digital-human pipeline) is the technical answer. The *performance* answer — what acting *means* in a medium where there is no fourth wall — has not been worked out.

**Four. What does sound design do in a navigable scene?** A film sound mix is, for the most part, a fixed track timed to the picture cut. A navigable-scene sound mix has to *follow the audience*. Spatial-audio tooling (the SonicLab SPATAI pipeline, Dolby Atmos for VR, the various Meta-and-Apple immersive-audio platforms) is the technical answer. The craft question is, again, what *good* spatial sound design looks like in a medium where the audience-author relationship has changed.

**Five. What is the *running-time* of a navigable scene?** A film has a fixed running time. A navigable scene does not. The audience could leave after thirty seconds or stay for two hours. The craft question for the working director is how to design the experience so that *both* extremes produce a satisfying piece of work. Games have, for fifty years, been grappling with this question — the *Dark Souls* answer (every player gets a different running time depending on skill and exploration) is different from the *Outer Wilds* answer (the running time is gated by narrative discovery) is different from the *Telltale Games* answer (the running time is broadly fixed across players). World-model cinema, in 2026, has not yet settled on its equivalent.

**Six. What is the *single best moment* of a navigable scene?** Film has scenes — discrete units of dramatic action with a recognisable shape, a recognisable peak, a recognisable end. A navigable scene, by default, does not. The craft question for the working director is whether to *design* the navigable scene around a single peak moment (which the audience may or may not reach) or to design it as a *texture* (which the audience experiences at whatever density their navigation produces). The peak-moment design pulls the medium back toward film conventions; the texture design pushes it toward something more like architecture or landscape design. Different working directors will, on the historical pattern, settle on different answers. The grammar will, over a decade, stabilise into a working vocabulary the way the cinematic-cut grammar stabilised between 1903 and 1925.

The six questions are not, in 2026, *theoretical* problems. They are the questions the working spatial-cinema teams I have talked to — the Wonderzoom group at Stanford, the World Labs developer cohort, the early adopters at Sony Pictures and Eyeline — are wrestling with on Wednesday afternoons. They are also, on the historical pattern of [Chapter 2](02_A_History_of_Resistance.md), the questions whose answers will define what working creatives in the next decade are *paid* to do. The directors and designers who develop a working vocabulary for them first will, on the available evidence, become the named *Walter Murchs* of the spatial-cinema era. The ones who wait for the vocabulary to settle will, in retrospect, look like the editors who waited too long to learn Avid.

### The big claim

Let me make the big claim, and then move on.

I think — and this is the most non-obvious bet in this book — that the **world model is the medium of the next twenty years of creative work**, in the same way that the **moving image** was the medium of the twentieth century and the **interactive screen** was the medium of the first quarter of the twenty-first.

I think people who are working in flat-video, flat-image, flat-audio formats in 2030 will increasingly be working in a *legacy* format — still alive, still culturally valuable, still where the highest-end of the craft lives, the way live theatre or vinyl-record production still lives — while the *dominant* mode of creative work will be the production, curation, performance and distribution of navigable spaces.

I think the studios, platforms and tool companies that are quietly investing in world models now — World Labs, DeepMind, Meta, NVIDIA, Tencent, Luma, Apple — will be the ones that set the rails for the next two decades.

I think the audience, having developed the antibodies described in Chapter 5 to slop-grade flat AI content, will eventually develop a parallel set of tastes for *navigable* content — and that the question of what makes a *good* AI world (rather than a *good* AI video) will be the central craft question of the late 2020s.

And I think — most importantly for the next chapter — that the toolchain to make all of this is being built, right now, by a small number of platform companies who have started saying out loud that AI is going to be *in everything, everywhere, all at once* — and who are, while you are reading this paragraph, designing the rails on which the next creative economy will run.

[^1]: World Labs, "Bringing Marble to Life." <https://www.worldlabs.ai/case-studies/bringing-marble-to-life>. [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md), "Editor's Pick: Marble by WorldLabs goes on public release," 13 November 2025.

[^2]: For a working primer on Gaussian splatting in the post-Marble era, see *Radiance Fields*, "World Labs Formally Launches Marble, A Generative World Model." <https://radiancefields.com/world-labs-formally-launches-marble-a-generative-world-model>.

[^3]: DreamLab AI Collective, beta participation in Marble, October–November 2025. Referenced in [*Dream Machine* Issue 7](../Dream%20Machine%20MD/7.md): "DreamLab have been part of the beta testing for this over the last few months and it's very neat."

[^4]: SuperSplat (PlayCanvas), open-source Gaussian splat editor, regular updates through 2025–26. [*Dream Machine* Issue 1](../Dream%20Machine%20MD/1.md): "PlayCanvas open sources SOG — WebP for 3D Gaussian Splatting"; Issue [7](../Dream%20Machine%20MD/7.md) / Issue [11](../Dream%20Machine%20MD/11.md) on SuperSplat v2 updates.

[^5]: Sony Pictures' use of Marble in Virtual Production: <https://www.linkedin.com/posts/brent-liang_tech-media-launch-ugcPost-7394911181091692546-TyUz>. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^6]: Disney "300,000 poses in an instant" livestream, March 2026. [*Dream Machine* Issue 23](../Dream%20Machine%20MD/23.md).

[^7]: Netflix + Eyeline, *Vista4D*: 4D point clouds from live-action. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^8]: Google DeepMind, "Genie 3: A new frontier for world models." <https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/>. Project Genie roll-out to AI Ultra subscribers in the U.S.: <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/>. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md) (initial announcement) and [Issue 17](../Dream%20Machine%20MD/17.md) (broader availability).

[^9]: Meta, "WorldGen — text-to-immersive-3D-worlds research update." <https://www.facebook.com/LifeAtMeta/videos/research-update-worldgen-text-to-immersive-3d-worlds/1879077432692421/>. *Dream Machine* Issues [9](../Dream%20Machine%20MD/9.md), [11](../Dream%20Machine%20MD/11.md).

[^10]: Tencent, "HY World 1.5" announcement: <https://x.com/TencentHunyuan/status/2001170499133653006>. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md).

[^11]: SpAItial, *ECHO* spatial foundation model. <https://www.spaitial.ai/>. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md).

[^12]: Stanford AI Lab, *Wonderzoom*: Multi-Scale 3D World Generation. <https://wonderzoom.github.io/>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^13]: OpenArt, *Worlds* product launch, March 2026. [*Dream Machine* Issue 21](../Dream%20Machine%20MD/21.md).

[^14]: Luma AI, *UNI-1* launch, March 2026. [*Dream Machine* Issue 22](../Dream%20Machine%20MD/22.md), "Editor's Pick: When worlds become instant, the race shifts to better thinking."

[^15]: ByteDance Seedance 2.0 in CapCut/Dreamina, March 2026. [*Dream Machine* Issue 22](../Dream%20Machine%20MD/22.md).

[^16]: *Spark 2.0*, open-source Gaussian-splat streaming framework, April 2026. [*Dream Machine* Issue 25](../Dream%20Machine%20MD/25.md).

[^17]: Radiance Fields, "Apple Confirms that it's Gaussian Splatting that powers their personas." <https://radiancefields.com/apple-confirms-personas-use-gaussian-splatting>. [*Dream Machine* Issue 5](../Dream%20Machine%20MD/5.md).

[^18]: *Video Games Chronicle*, "'It honestly sucks': Fans think Call of Duty: Black Ops 7 is filled with generative AI art." <https://www.videogameschronicle.com/news/it-honestly-sucks-fans-think-call-of-duty-black-ops-7-is-filled-with-generative-ai-art/>. *Video Games Chronicle*, "Ubisoft says AI-generated art in Anno 117 was a placeholder which 'slipped through our review process'." <https://www.videogameschronicle.com/news/ubisoft-says-ai-generated-art-in-anno-117-was-a-placeholder-which-slipped-through-our-review-process/>. *Polygon*, "Fortnite chapter 7 kicks off new controversy over AI art." <https://www.polygon.com/fortnite-chapter-7-season-1-generative-ai-art-epic-games/>. *Dream Machine* Issues [8](../Dream%20Machine%20MD/8.md), [10](../Dream%20Machine%20MD/10.md).

[^19]: NVIDIA + Stanford, *NitroGen*. <https://nitrogen.minedojo.org/>. [*Dream Machine* Issue 13](../Dream%20Machine%20MD/13.md).

[^20]: DeepMind, "SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds." <https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/>. [*Dream Machine* Issue 8](../Dream%20Machine%20MD/8.md).

[^21]: ComfyUI Blog, "Ubisoft La Forge Open-Sources the CHORD Model and ComfyUI Nodes for End-to-End PBR Material Generation." <https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model>. [*Dream Machine* Issue 11](../Dream%20Machine%20MD/11.md).

[^22]: *Video Games Chronicle*, "The future of gaming, or 'just a tool'? Hands-on with Teammates, Ubisoft's ambitious voice AI tech demo." <https://www.videogameschronicle.com/features/the-future-of-gaming-or-just-a-tool-hands-on-with-teammates-ubisofts-ambitious-voice-ai-tech-demo/>. [*Dream Machine* Issue 9](../Dream%20Machine%20MD/9.md).

[^23]: YouTube Playables Builder, closed-beta announcement: <https://www.youtube.com/playablesbuilder/>. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md).

[^24]: Unity AI Open Beta, in-editor AI suite, May 2026. [*Dream Machine* Issue 28](../Dream%20Machine%20MD/28.md).

[^25]: Korin AI, "trained with African datasets, built by Africans," May 2026. [*Dream Machine* Issue 27](../Dream%20Machine%20MD/27.md).

[^26]: NVIDIA SANA-WM, 2.6B open-source world model with 60-second video generation and camera control, May 2026. <https://huggingface.co/collections/nvidia/sana-wm>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^27]: Odyssey, "Introducing Starchild-1, the first real-time multimodal world model." <https://odyssey.ml/introducing-starchild-1>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^28]: Apple Machine Learning Research, "Headsup: a large-scale high-quality 3D Gaussian head reconstruction from multi-view captures." <https://machinelearning.apple.com/research/apple-headsup-3d-gaussian-head>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).

[^29]: WorldLens VR, "AI-powered 3D depth for Google Street View on Quest." <https://www.uploadvr.com/worldlens-vr-quest-street-view-3d-depth/>. [*Dream Machine* Issue 30](../Dream%20Machine%20MD/30.md).
