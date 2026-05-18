# Chapter 2

## The Human-AI Agency Continuum

A week after I sent the first edition of *Dream Machine*, on the Monday of the second week of October 2025, OpenAI held its annual DevDay conference and quietly changed what the conversation about AI in creative work was about.

The first edition had been about Sora 2. The second edition was about something I was less prepared for: the launch of a thing called **AgentKit**.[^1]

AgentKit was, at first glance, a set of developer tools. Agent Builder. A connector registry. An eval framework. ChatKit, for embedding agents into other products. The launch post on OpenAI's blog framed it, in the slightly forced register that all platform-launch posts use, as a way for developers to "build, deploy, and optimize agentic workflows."[^2] On its own, this was an unremarkable announcement.

What was remarkable, looking back, was the *category claim* the announcement carried with it. Sam Altman, in his DevDay keynote that day, declared the start of "the age of agentic AI" — by which he meant the moment that AI systems stopped being prompt-and-respond chat boxes and started being things that could plan, decide and execute "for hours on end" without further human input.[^3]

For someone like me, sitting in a small studio in the North West of England — running tools all day, looking at my pipeline, thinking about my team's labour — that phrase did a particular kind of work. It rearranged the question.

The question, until that week, had been: *what does AI do for creative work?* The question after that week became: *where, in any given piece of creative work, does my agency end and the model's begin?*

The second question is the one I want this chapter to be about. I called it, in the second issue of the newsletter, the **Human–AI Agency Continuum**.[^4] The frame has stuck with me. I think it is the most useful thing I have ever written down about all of this, and I think — at the risk of overselling it — the rest of the book leans on it.

### The continuum

Imagine a horizontal line.

On the far left of the line is **pure human agency**: the writer at the desk, the painter at the canvas, the songwriter at the piano. No machine intermediation other than the tool itself — and the tool, in this position, is dumb. It records what you do; it doesn't decide.

On the far right of the line is **pure machine agency**: an autonomous system that, given a goal, produces a finished creative output with no human in the loop. A prompt, a setting, a render. No one looks at the intermediate steps. No one steers.

The conversation about AI in the creative industries in 2024 mostly took place on the assumption that "generative AI" sat about three-quarters of the way along that line — closer to the machine end. You typed a prompt; the machine made the thing; you accepted or rejected. There were variants, of course. But the geometry was prompt-and-respond, and the question was simply where on the line, between you and the model, the actual creative work happened.

What changed at OpenAI DevDay on 6 October 2025 — and what was reinforced almost every week of the six months that followed — was that the line is not, as it turned out, a single line. It is a *family of lines*, one per creative function, and they all move at different speeds.

A film, broken down, is not one act of agency. It is a thousand. The choice of subject. The treatment. The casting. The script revisions. The cinematography. The blocking on set. The performance, take by take. The editorial assembly. The grade. The sound. The music. The marketing. Each of those is a sub-discipline, with its own craft, its own labour pool, its own union, its own pay scale and its own internal hierarchies.

AI doesn't slide along *the* line. It slides along each of those lines independently.

A working filmmaker in late 2025 might sit at the absolute left of the continuum on *performance* (a real actor, in the room, in real time, the work itself) and at the absolute right on *background plate generation* (a Veo 3.1 shot, signed off in a Slack message, no human ever drawing a frame).[^5] A working musician might sit at the absolute left on *songwriting* (a song in a notebook) and on the right edge of the centre on *vocal alignment and pitch correction* (an iZotope Ozone 12 assistant, accepted with one click).[^6]

The crisis of authorship is not that machines do creative work. Machines have done parts of creative work for as long as there have been cameras, samplers, Photoshop filters and Logic plug-ins. The crisis is that we don't have an honest, shared, public vocabulary for *which* parts. The Continuum, written down honestly per project, is the start of one.

### Agents are not generators

The reason the Continuum became urgent the week of DevDay, and not before, is that "agent" is a different kind of object on the line than "generator" is.

A generator is a tool. You aim it at a problem; it makes an output. The agency is in the aiming.

An agent is something more like a junior collaborator. You give it a goal — *find me ten reference images for this shot,* *generate a rough sound design for this scene,* *book the courier for tomorrow's pickup* — and it goes away, makes a series of sub-decisions, and comes back with a result. The agency is distributed. You set the direction; it makes the moves.

The reason this matters in creative work is that the moves are where the craft lives. Anybody can describe a final film in a sentence. The film is in the thousand decisions between the sentence and the screen. A generator that makes the screen-ready file from your sentence isn't doing your craft. It is taking your craft out of the loop.

An agent, properly deployed, can do something different and — to me, anyway — more interesting. It can take the parts of the loop that are not where your craft lives, and quietly handle them, so that the parts of the loop that *are* where your craft lives become the parts you actually spend your time on.

That is the optimistic case for agentic AI in creative work, and it is the case that almost every working creative I respect makes when you sit down with them in private. It is also the case Adobe's 16,000-creator survey, released a few weeks after DevDay, came in to support: 70% of respondents were optimistic about agentic AI, framed as "tools that act on your behalf"; 85% said they would use AI that learned their creative style.[^7]

The pessimistic case is the one Adobe's same survey also captured: 69% of respondents worried about their work being used to train AI without consent.[^8]

Both numbers are about agency. The first is about *gaining* it back, by handing routine work to a competent assistant. The second is about *losing* it, by having the work that defines you absorbed into a system you do not control. Both are true at the same time, for the same creators, in the same workflows.

### Where agents went, between October and May

In the six months between DevDay and the time I'm writing this, the agent layer of the creative toolchain went from "interesting demo" to "shipping product," faster than any technology shift I have lived through in twenty years of practice. I want to give you a sketch of the trajectory, because it is what most of the rest of this book is reacting to.

By **mid-October 2025**, Mureka — a Chinese music platform — launched a thing called *Music Agent Studio*, six specialised AI agents for songwriting, arrangement and production.[^9] A startup called AdsGency raised $12m in seed to build agents that could autonomously run a brand's entire paid marketing workflow.[^10] A company called Lenny launched an agent for organising live music events.[^11] Each of these felt, at the time, like a specialist tool. In retrospect, they were the first signs that whole production functions — not individual tasks — were being handed over.

By **the end of November**, EA, in the middle of a brutal financial year, told its 15,000 employees to use AI as a "thought partner" for everything from character art to playtesting.[^12] The framing — *thought partner* — was the precise rhetorical move that turned an agent from a tool into a colleague. The colleague has opinions. The colleague has time. The colleague has a seat at the meeting.

By **December**, Adobe announced that you could now use Photoshop and Express *inside* ChatGPT — meaning that the creative output itself was no longer happening inside Adobe's interface, but inside an agent's.[^13] This was a small thing on the surface and an enormous thing underneath. It was the moment that Adobe — a company that has, since 1990, owned the metaphor of the *creative tool* — accepted that the new metaphor was the *creative agent*, and that they would rather be inside someone else's agent than not in the conversation at all.

By **late January 2026**, Anthropic shipped Claude apps — interactive, custom assistants embedded directly in workplace tools — and a company called Heygen released *Video Agent*, which could script, edit and assemble entire videos from reference images.[^14] By **March**, Adobe announced its **CX Enterprise** platform alongside NVIDIA: a stack of AI agents embedded across the entire content lifecycle, from brief to delivery.[^15] By **April**, the *Adobe Summit* keynote made it official — "agentic creative intelligence" was now the headline category, not a feature.[^16] By **May**, Sony was using a multi-agent team of forty-nine Claude Code agents, working with seventy-two skills, to coordinate game-development work.[^17]

The trajectory, in one sentence: in October 2025 we were arguing about whether agents were a thing. By May 2026, the entire creative production pipeline at a global game publisher was being run by a team of them.

### What this means for craft

The natural fear, reading that timeline, is that the agency line drifts inexorably to the right — towards the machine end — and that the craft of the human in the loop becomes thinner and thinner until it disappears.

I do not think that is what happens. I think what happens is more interesting and more demanding.

What I see, in my own studio, in my friends' studios, in the working musicians and filmmakers and games designers I talk to every week, is that agentic AI doesn't compress craft into nothing. It *relocates* craft to a different place on the continuum.

If your job, last year, was "make the thing", your job this year is "decide what gets made, brief the agents that make the constituent parts, and judge the output." That isn't a smaller job. In some ways it is a bigger one. It requires *more* taste, not less, because taste is now the only signal you bring that the agents cannot.

Anthropic, in a blog post in early 2026 that I have ended up quoting repeatedly in talks, made the point this way: agentic systems work best when they are deployed by people who already have the taste and judgment to know what good output looks like.[^18] The agents accelerate the work *of people who are already good at it*. They do not — at least, not yet — manufacture good work from nothing.

This is the central — and I think non-obvious — claim of the Continuum frame: as the line for any given function slides to the right, the *value of the human at the left edge of the line* doesn't decrease. It increases. Because the question being asked of that human gets sharper. Not "can you make this," but "*should* this be made, and *why this version,* and *who is it for*, and *what does it need to do in the world*."

That is craft. It is just craft sitting in a different chair.

### Where the Continuum breaks

I want to be honest about where my frame stops working, because nothing is more boring than a writer who only quotes the people who agree with him.

In November 2025, the games designer Charles Cecil — the head of Revolution Software, the studio that made *Broken Sword* — told *gamesindustry.biz*, in a sentence that has been quoted, retweeted and emailed around my industry approximately a million times: "AI was an expensive mistake."[^19]

Cecil's argument was specific. Revolution Software had, like a lot of indie game studios, experimented with using generative AI in early production. They had found that the time saved on the front end of the pipeline was lost — and then some — on the back end, where artists, writers and designers had to reverse-engineer, fix, replace and reintegrate AI-generated assets that didn't quite fit the game's tone, didn't quite match the existing art direction, didn't quite work with the engine, didn't quite carry the IP. Net-net: more time spent, not less. More cost, not less. Hence: "an expensive mistake."

This is what the Continuum frame doesn't capture on its own. *Where on the line* a given task sits is not a fixed property of the task. It is a function of the surrounding system: how the tools integrate, how the team is structured, how the IP works, how the audience receives the output. A generative tool that sits comfortably on the right-hand side for one studio's marketing department sits awkwardly in the middle for another studio's lead-artist pipeline.

In the same six months that I was watching the agent layer eat the creative toolchain, I was also watching studios push back. Larian, the makers of *Baldur's Gate 3*, backed off from generative AI for their next *Divinity* game in January 2026. Their public note was carefully worded: *"I know there's been a lot of discussion about us using AI tools as part of concept art exploration. We already said this doesn't mean the actual concept art is generated by AI but we understand it created confusion."*[^20] Games Workshop ruled it out entirely for *Warhammer 40,000*.[^21] Manor Lords publisher Hooded Horse said it wouldn't work with developers using generative AI — its founder's framing, when asked about the line, was unusually direct: AI in his pipeline was *"cancerous,"* and the studio's job was *"constantly having to watch and deal with it and try to prevent it from slipping in."*[^22] Jagex, the maker of *RuneScape*, said in early 2026 that it would *never* use generative AI to make in-game content, and that the commitment *"goes so far that we are now doing an audit and having a conversation with our various external partners that work with us to ensure that no AI is being used in inappropriate ways in any of their work that might filter through."*[^23]

These were not statements made by Luddites. They were strategic decisions made by people whose creative product is, in significant part, the *human* fingerprint on the work. The audience for a *Warhammer* miniature, or a *RuneScape* quest line, or a Larian dialogue tree, comes to those products in part because they know — and want to know — that real people made them. The Continuum slides differently in those companies because the *output* sits at a different point on the continuum of what the audience wants.

This is the thing about the agency line that the OpenAI keynote, the Adobe Summit, the NVIDIA GTC keynote, the Anthropic blog post and the Salesforce Dreamforce all keep glossing over. The position of the line is not just about what is technically possible. It is about what the work, in its finished form, is *for*.

### A working frame

If I were going to leave you with one tool from this chapter, it would be this:

The next time you sit down to plan a piece of creative work, draw the lines.

Not one line — that's the trap of the "AI debate" — but as many lines as the work has functions. *Ideation.* *Research.* *Writing.* *Direction.* *Performance.* *Image-making.* *Sound.* *Editing.* *Distribution.* For each one, ask the same two questions. *Where do I want to sit on this continuum, and where am I willing to let the agent sit on my behalf?* And then — the harder question — *what does the work lose if I move further to the right, and what does it gain?*

The honest answer, for almost every creative person I know, varies wildly by function. Most of us are happy to let agents sit on the right-hand side of distribution and admin. Most of us are not happy to let them sit on the right-hand side of the performance, the writing, the moments where the audience can feel a person in the work. The middle is where the interesting fights are.

If you can articulate where the lines sit for *your* work, you can articulate it to your clients, your team, your collaborators, your union, your audience. You can write it into your contract. You can put it on your website. You can fight for it.

If you can't articulate it — if you wave at "AI" as if it were a single thing — you will end up with the lines drawn for you, by tool vendors and platform companies and CFO spreadsheets that have very different ideas about where your agency should sit than you do.

The Human–AI Agency Continuum, in the end, is not a description. It is a defence.

[^1]: [*Dream Machine* Issue 2](../Dream%20Machine%20MD/2.md), "Editor's Pick," 10 October 2025. <https://www.linkedin.com/pulse/dream-machine-creative-ai-news-insight-oct-25-2-pete-woodbridge-mnrjc/>.

[^2]: OpenAI, "Introducing AgentKit," 6 October 2025. <https://openai.com/index/introducing-agentkit/>.

[^3]: TechCrunch, "OpenAI launches AgentKit to help developers build and ship AI agents," 6 October 2025. <https://techcrunch.com/2025/10/06/openai-launches-agentkit-to-help-developers-build-and-ship-ai-agents/>. Also coverage at *InfoQ*, "OpenAI Dev Day 2025 Introduces GPT-5 Pro API, Agent Kit, and More." <https://www.infoq.com/news/2025/10/openai-dev-day/>.

[^4]: [*Dream Machine* Issue 2](../Dream%20Machine%20MD/2.md): "Agentic AI — the class of AI systems that can plan, act, and pursue goals with autonomy — promises a new era of collaboration in creative industries… Its another step along the Human-AI Agency Continuum." See also *TVB Europe*, "Is Agentic AI About to Change the Media and Entertainment Industry?" <https://www.tvbeurope.com/artificial-intelligence/opinion-is-agentic-ai-about-to-change-the-media-and-entertainment-industry>.

[^5]: Google DeepMind, Veo 3.1 release, October 2025. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md).

[^6]: *MusicTech*, "iZotope Ozone 12's AI assistant is cool, but the Stem EQ is the real star." <https://musictech.com/reviews/plug-ins/izotope-ozone-12-review/>. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md).

[^7]: Adobe, "Inaugural Adobe Creators' Toolkit Report," October 2025. <https://news.adobe.com/news/2025/10/adobe-max-2025-creators-survey>. Survey of 16,000 creators across eight countries, released at Adobe MAX 2025. [*Dream Machine* Issue 6](../Dream%20Machine%20MD/6.md).

[^8]: Adobe, *op. cit.* The same survey: 86% of creators use creative generative AI; 76% say it has helped grow their business or brand; 81% say AI lets them make content they otherwise couldn't have made; 69% worry about their work being used to train AI without consent; 70% are optimistic about agentic AI; 85% would use AI that learns their creative style.

[^9]: Mureka, "Music Agent Studio" launch, mid-October 2025. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md). <https://www.linkedin.com/posts/sherrihendrickson_mureka-unveils-music-agent-studio-and-enhanced-share-7384999251526864896-cNYg/>.

[^10]: *Finsmes*, "AdsGency Raises $12M in Seed Funding," October 2025. <https://www.finsmes.com/2025/10/adsgency-raises-12m-in-seed-funding.html>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^11]: *Musically*, "Meet Lenny, an AI agent to help organisers of live music events." <https://musically.com/2025/10/20/meet-lenny-an-ai-agent-to-help-organisers-of-live-music-events/>. [*Dream Machine* Issue 4](../Dream%20Machine%20MD/4.md).

[^12]: *GamesRadar*, "Even under USD20 million in debt, EA reportedly pushes 15,000 employees to use AI as a 'thought partner' for everything from character art to playtesting." <https://www.gamesradar.com/games/even-under-usd20-million-in-debt-ea-reportedly-pushes-15-000-employees-to-use-ai-as-a-thought-partner-for-everything-from-character-art-to-playtesting/>. [*Dream Machine* Issue 6](../Dream%20Machine%20MD/6.md).

[^13]: PYMNTS, "Adobe Lets Users Design and Edit Using ChatGPT." <https://www.pymnts.com/artificial-intelligence-2/2025/adobe-lets-users-design-and-edit-using-chatgpt/>. Adobe blog: "Edit images, designs, and PDFs right inside ChatGPT — thanks to Adobe Express, Photoshop, and Acrobat." <https://blog.adobe.com/en/publish/2025/12/10/edit-photoshop-chatgpt>. [*Dream Machine* Issue 12](../Dream%20Machine%20MD/12.md).

[^14]: TechCrunch, "Anthropic launches interactive Claude apps, including Slack and other workplace tools," 26 January 2026. <https://techcrunch.com/2026/01/26/anthropic-launches-interactive-claude-apps-including-slack-and-other-workplace-tools/>. *Heygen Video Agent*: <https://www.linkedin.com/posts/heygen_introducing-the-new-video-agent-activity-7421597801240801282-d1CF>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).

[^15]: [*Dream Machine* Issue 21](../Dream%20Machine%20MD/21.md), "Editor's Pick: Adobe and NVIDIA Just Raised the Stakes for Creative AI," 19 March 2026.

[^16]: Adobe Summit 2026, "Agentic Creative Intelligence" keynote framing. [*Dream Machine* Issue 26](../Dream%20Machine%20MD/26.md).

[^17]: [*Dream Machine* Issue 29](../Dream%20Machine%20MD/29.md), May 2026, citing Sony's adoption of Claude Code studios with multi-agent coordination.

[^18]: Anthropic, public statements on agent deployment patterns through Q1 2026. Cf. *Dream Machine* Issues [11](../Dream%20Machine%20MD/11.md), [16](../Dream%20Machine%20MD/16.md), [22](../Dream%20Machine%20MD/22.md).

[^19]: *gamesindustry.biz*, "'AI was an expensive mistake': Charles Cecil on innovation, insolvency, and Broken Sword." <https://www.gamesindustry.biz/ai-was-an-expensive-mistake-charles-cecil-on-innovation-insolvency-and-broken-sword>. [*Dream Machine* Issue 3](../Dream%20Machine%20MD/3.md).

[^20]: *Niche Gamer*, "Larian Studios backs off from gen AI, says tech won't be used in new Divinity." <https://nichegamer.com/larian-studios-backs-off-from-gen-ai/>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^21]: *Decrypt*, "'Warhammer 40,000' Maker Games Workshop Rules Out Generative AI." <https://decrypt.co/354482/warhammer-40000-maker-games-workshop-rules-out-generative-ai>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^22]: *Niche Gamer*, "Manor Lords publisher Hooded Horse won't work with devs using gen AI." <https://nichegamer.com/manor-lords-publisher-hooded-horse-wont-work-with-devs-using-gen-ai/>. [*Dream Machine* Issue 14](../Dream%20Machine%20MD/14.md).

[^23]: *gamesindustry.biz*, "RuneScape maker Jagex says it will never use generative AI to make in-game content." <https://www.gamesindustry.biz/runescape-maker-jagex-says-it-will-never-use-generative-ai-to-make-in-game-content>. [*Dream Machine* Issue 16](../Dream%20Machine%20MD/16.md).
