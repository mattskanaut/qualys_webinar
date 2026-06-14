# Part 2 - Defending AI in Production: Speaker Notes v4

Working document, MIRRORED to the deck (display order, 16 slides).
Last synced to `Running-AI-in-Production.pptx`: 2026-06-14.

DECK REORDERED 2026-06-14: old DISPLAY 10 (infra exposed), 11 (agents can't be
stopped) and 12 (a number is not a posture) were CUT. The old back half has been
renumbered down by three (old 13 -> new 10, ... old 19 -> new 16).

SOURCE OF TRUTH: the .pptx is now canonical for displays 1-9. Matt edits the
notes directly in the deck; this file mirrors it. NEVER edit the .pptx from
tooling - Matt copies notes in by hand. When the deck changes, re-extract and
update this file.

- Notes COMPLETE in the deck (Matt's own voice): displays 1-10.
- Notes DRAFTED in this doc (approved), pending copy-in to deck: displays 11-15.
- Notes TO WRITE: display 16 (Questions / series close).
- LIVE DECK STATE (2026-06-14): the .pptx physically has 21 slides - the three
  cut slides are PARKED at the end (displays 19 infra, 20 agents-act, 21
  attacker-moves-second), and the discipline slide is currently DUPLICATED three
  times (displays 10-12). This doc reflects the intended 16-slide structure;
  deck cleanup (delete the two extra discipline copies; remove/keep the parked
  slides) is still pending.
- ON SLIDE lines below are condensed from the live slide text. SOURCES lines are
  verified scaffolding. ON SLIDE / SOURCES are NOT spoken. `[CLICK]` markers are
  kept verbatim (they map to slide builds).
- Unicode normalised to ascii.

---

## Voice / tone reference (from Part 1)

Keep these when we write:

- Warm, humble open; credentials worn lightly; "why this matters to me," not status.
- Caveat hard and early; comfortable saying "I'm not sure, to be honest."
- Self-deprecating ("which idiot wrote this - oh, it was me").
- Generous credit to researchers ("big thanks to them").
- One strong analogy per major turn (Part 1: building trade, aviation autopilot).
- The refrain: "none of these are new controls" = the "new attack, old control" spine.
- Direct address and solidarity: "you already know this," "we as practitioners."
- British, spoken rhythm; "So," openers; long natural sentences.
- Close on an honest optimistic steel-man.

NB: the polished/rhetorical register is AI-assisted - do NOT use it as the model.
Match the live notes on slides 1, 3, 5 instead. Do not add fake typos.

---

## DISPLAY 1 - Title: Defending AI in Production

ON SLIDE: "The New Normal: Software, Security and the AI Stack - Part 2 of 2".
Defending AI in Production. Matt Campbell, Senior Security Solutions Architect.
mcampbell@qualys.com / linkedin.com/in/matthew-mark-campbell/

SPEAKER NOTES (in deck):

Hello again everyone, and thank you once again for taking the time out of your no-doubt packed schedules to join us today, and thank you John for the introduction.

My name is Matt Campbell, and as you can see on the slide, I'm one of the solution architects at Qualys, assisting our customers, and prospective customers to select, deploy and optimize Qualys products to achieve their security objectives, but also advising on their security practices more generally.

As I said last time, this isn't what I've always done, I started my career as a developer and then application architect, then moved on to work in various system architecture roles working large scale and complex CI/CD programmes, where I spent a lot of time thinking about how we could deploy our products securely...

In part 1 of this two part series, we looked at the security implications of the rise of AI tools being used in the software development lifecycle.

Today, we're going to take a look at what happens post development, when you yourselves have shipped AI features - a model, a prompt, tools, agents, a supply chain - and you are now defending a system whose inputs can come from a range of sources in a range of different formats, and whose output is non-deterministic.

Like last time, I need to start with a heavy caveat. Things are moving extremely fast in this space, and none of us know what the future holds even in the short term.

I was at Infosec last week and good conversation with a security architect from a large retailer, who'd been tasked by his leadership to produce a 10 year cyber security plan. We both had a bit of chuckle about that.

So, as last time, its hard to give clear guidance on these issues, there are no simple answers at the moment, so the best I can do is give my opinion on what I think practitioners and the industry as a whole needs to do to mitigate some of the clear dangers we can see.

Also, like last time, no doubt your organisations will be grappling with these issues over the comming months and years, so please do use forums like this, and others, or blog posts, or conferences to share your findings and learnings, what works, what doesn't, so we can all progress.

---

## DISPLAY 2 - It's already out there

ON SLIDE: 99% of organisations already run autonomous AI agents in production
(Palo Alto Networks 2026 Identity Security Landscape). 83% plan agentic AI, yet
only 29% feel ready to secure it (Cisco, 2026). 62% name security as #1 blocker,
ahead of technical limits at 38% (McKinsey via Stanford AI Index 2026). Live
poll: "Has someone in your organisation shipped an AI feature you did not know
about? The gap between deployed and defended is where you live."

SPEAKER NOTES (in deck):

So before we get into any of the security weakenesses you should expect, or look at how this is actually being exploited, I just want to ground us in where we are right now, as organisations.

[CLICK]

And I'm going to go quite quickly over the obvious part. Everyone in this room knows AI is out there, you know your developers are using it, you know there are agents running somewhere in your business. Note here that this figure is so high because its including any agentic AI in tooling you're using, for example an agentic AI note taker.

[CLICK]

The bit I think is actually worth pausing on is the gap. Because at the same time as more or less everyone is shipping this stuff, only about a third feel anything like ready to secure it. And when the question was asked about what's holding back scaling agentic AI, security came out as the number one blocker, ahead of the technical limitations.

[CLICK]

That gap, between what we've already deployed and what we can actually defend, is really what this whole session is about. It's where you, as the people carrying the responsibility for this, are living right now.

[CLICK]

So I'd like to do a quick temperature check. Has someone in your organisation shipped an AI feature that you, as the security org, didn't know about until after it was up and running? In my experience the honest answer for a lot of organisations is "probably, and we're not completely sure", and that's really the heart of it. You can't defend something you don't know you've got, and that idea, discovery, is one we wil return to today.

So over the next forty minutes or so I want to do a few things. First get clear on what an "AI feature" actually is, because it's a good deal more than just the model. Then look at some real incidents, because that's where the patterns start to show. Then finally, what I think we should actually be doing about it, which, as you'll see, is mostly things you already know how to do.

---

## DISPLAY 3 - System anatomy

ON SLIDE: Model / Harness / MCP Server. Tools and RAG are similar.
(ref: anthropic.com/engineering/code-execution-with-mcp)

SPEAKER NOTES (in deck):

Before going any futher, I'd like to just clarify a few architecural points about what an AI, and in particular I'm talking about an LLM here, actually is in operation, because there's a lot of confusion and misunderstanding out there in industry.

So, firstly the model itself. Often hosted on remote servers supplied by the model builders, like Anthropic or OpenAI, or on a hyperscaler platform like AWS Bedrock, or Azure AI Foundry.

The model is the brain of the system and its what does the reasoning. They are complex collections of matrix operations that generate output, often text but also graphics, video etc, in response to input an input. So, pass in bytes, or tokens, get bytes out.

Some key features
 - They're stateless. They have no sense of time and no memory. You add data in one side and get data out the other side as a 1 hit process.
 - They're static. The model is trained then released and after that release it does not change for the duration of its lifetime. They do not train on what they see, that is common myth, they do not learn while in operation (of course the model provider may be capturing your input to add to the training data of their next model, but the model you are using yourself won't learn from you.
 - They're probabilistic. Although they're pure functions, not dependent on history or anything external, other than the prompt you send in, they still have a level of non determinism because their response is sampled from a probability distribution of possible responses. I won't go any deeper into that, but if anyone would like to dig further, go and look up what the temperature setting does as a jumping off point to understand this better.

Given these characteristics of the model, they aren't very useful without a harness. Harnesses are things like Claude Code, or the chatgpt web interface. The harness is what makes it all come alive. It's the harness that's managing the chat history that makes the model feel stateful. Its the harness, as we can see here, that interacts with things like an MCP server to allow tool calls or information to be fetched.

One very important thing to understand is becuase the model is stateless, the entire context, so the full conversation history, including everything you sent to the model, and all the models replies are sent to the model each turn. That's what makes it feel like a conversation or stateful, the model is recieving the entire history of the session each time, with your latest addition that it responds to, but responding to it after processing the entire context.

And finally shown here, we have an MCP Server that allows tool calls to be made, which could be basically any other system.And here's the one thing I really want you to take away from this slide, because it comes back again and again today. All of that context, everything going into the model each turn, is just one block of text as far as the model is concerned. The instructions you gave it, the system prompt the harness wrapped around it, a document it pulled in, an email it was asked to read, the result of a tool call, it all arrives as the same kind of thing, down the same channel. The model has no reliable way of telling "this part is a trusted instruction from my operator" from "this part is just some data I was asked to look at". To the model, it all looks the same. And almost every attack we're going to look at today, when you strip it back, is really just someone taking advantage of that one fact.

---

## DISPLAY 4 - Autonomous agents

ON SLIDE: Same model underneath, stateless, text in / text out; what changes is
who's driving the loop. Chatbot/coding assistant: you're in the loop every turn.
An agent hands "what's next" to the model and runs the loop itself - works out a
step, calls a tool to actually do something, reads the result, and goes again, no
human in between. That autonomy is the whole point of an agent and the whole risk.
(ref: docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)

SPEAKER NOTES (in deck):

So we've got the model now, and we've got the harness wrapped around it, holding the conversation and making the tool calls. The thing I want to pull out on this slide is the difference between a harness you sit and work with, and an agent, because they're really not the same thing and that distinction matters for the rest of our discussion today.

When you're using a chatbot, or a coding assistant like Cursor, you're in the loop the whole way through. You ask it something, it answers, you read what it said, you decide if you're happy with it, and you decide what to ask next. Every single turn, there's a human, you, making the call about what happens next.

An agent is what you get when you take the decision about what to do next, and hand it over to the model itself. You give it a goal, and instead of coming back to you at every step, it works out the next step on its own, it takes an action, and by action I mean actually going off and doing something, calling a tool, reading a file, then it looks at whatever came back, and round it goes again. Over and over, until it decides the job's done.

And underneath, nothing's really changed about the model. It's still that same stateless, text in text out thing we were just talking about, being called over and over with the whole context each time. What's changed is you. All those little decisions you used to make every turn, they're being made by the model now, on its own.

This has big implications for system safety. There isn't a human sanity checking the output, then refining the prompt to keep the model on track and get the answer that makes sense, the model uses its own judgment, so if that judgement is influenced by instructions that someone has injected into the context, the agent will carry on building on that unsafe foundation, turn after turn.

---

## DISPLAY 5 - What you actually deploy

ON SLIDE: Anatomy of a production AI feature. Six layers, each a distinct threat
vector: Model (provenance, poisoned weights, malicious pickle files in
open-source checkpoints); Prompt (injection, direct and indirect); Tools/MCP/RAG
(tool poisoning, over-broad scope); Memory (poisoning and persistence); Identity
(sprawl and over-privilege, shared service accounts with no named owner); Data
Flow (exfiltration and logging gaps via side channels). Self-audit: most
organisations lack visibility on three or more of these layers. You cannot defend
an inventory you do not have.

SPEAKER NOTES (in deck):

So understanding AI systems are way more than just the model in use, so lets build up some shared vocabulary, so we can turn "AI workload or system" into a concrete inventory we can reason about.

We'll also touch on some of ways these various system components are vulnerable to attack, start enumerating this "new class of attack surface" introduced by deploying AI in your production environment.

[CLICK]

Firstly, the model itself. Who vended it, where did it come from. You're probably less concerned about this if you're using Anthropic, or OpenAI (although even then you may have concerns about training bias that could impact your particular use case), but as the model landscape broadens or we start using open source models and things, we're opening ourselves up to some quite sophisticated attacks that could be all but impossible to detect, at least as we understand it, basically biasing the model to behaviours that are odds with what's advertised or desired. Not seen in the wild yet, as far as I know, but there have been demonstrations done. The other vectors are bit more standard, basically packaging malicous code alongside model weights as part of their serialization formats.

[CLICK]

Prompt injection, and we've really already met this one, it's that same-channel problem from the anatomy slide a moment ago. It's the layer everyone thinks of first. The idea is simply that if you can get malicious instructions into the model's prompt, you can get it behaving in ways at odds with whoever's hosting it. And it comes in two flavours. There's direct injection, where the attacker types straight into something you've exposed, a chat box on your website say. And then there's indirect, where the malicious instructions ride in on data the model goes off and fetches for itself, a document, a web page, a record in a database. And it's that indirect kind that can be particularly difficult, because the attacker never has to directly talk to your system at all. In fact we'll see exactly that in a minute with the Salesforce breach.

[CLICK]

Tools, MCP servers and Retrival Augmented Generation are a key ways we can allow interaction with systems outside the immediate harness process. They can wrap databases, or other software tools, anything at all really so that models (or more accurately model harnesses) can pull data into the prompt, or allow the model to take downstream action. Clearly this makes them a major threat vector, both for context posioning, which is just another way to say prompt injection, and for downstream exploits, an MCP server that's permissions are too broad increases the blast radius of any expoit for example.

[CLICK]

Attacking the memory system of harnesses is another way to achieve prompt injection. A lot of tools and agents have memory systems now, of varying levels of sophistication. The idea being, LLMs are stateless remember, that key information can be written by harnesses during operation that mean that agents or systems can resume with a history, mainly by just loading that history into the harness session.

[CLICK]

Looking at some more traditional security issues now, identity is as important a control over your security as anything else. Identity as the new perimeter, as we say in cloud (not so new any more), where good control over identity and permissions is what limits the blast radius of any breach. Again, pre-AI security practicies and tooling can secure our systems, even when the threat vectors are new.

[CLICK]

Finally, securing your data flows. Here many things that aren't new. Limit access to data to only what's required for the task, control egress channels with controls at various levels, things domain allowlisting, or network level controls. Like many other controls, this is about taking concious control of the scope you give to your agents and the channels they can use, and block everything else, with tooling to maintain that configuration over time so things can't drift.

[CLICK]

So keep these six in your head, because the breaches we look at next aren't anything exotic, they're just these layers going off, usually two or three of them at once.

---

## DISPLAY 6 - The attacker filled in a web form (ForcedLeak: the input is hostile)

ON SLIDE: "Forcedleak: The input is hostile." Agent Deployed (company connects AI
agent to CRM) -> Hidden Payload (attacker embeds instructions in Web-to-Lead) ->
Agent Executes (employee requests lead summary; agent follows payload) -> Data
Exfiltrated (pipeline data sent via image call to trusted domain). Rated CVSS 9.4
by Noma Labs (September 2025). No social engineering, no phishing, no access to
the system - just a description field in a web form and a carelessly maintained
URL allow list.

SPEAKER NOTES (in deck):

So, here's a great example of that indirect injection I mentioned on the last slide, only now it's a real breach rather than a definition. And I want to give this one a bit of time, because for us as practitioners this kind of breach analysis is really valuable, it puts flesh on the bones and you start to see the patterns that come up again and again. This one's courtesy of Noma Labs, big thanks to them, and it's an excellent example of the new type of attack surface we've exposing.

And the heading there is the key to it, the input is hostile. Think back to that one fact, that the model can't tell your instructions from data it's been handed. Well, this is an attacker getting their instructions in as data, and by about the simplest route you can imagine, they just filled in a web form.

So, late last year, Noma Labs found a vulnerability chain in Salesforce's Agentforce, which is their agentic AI framework.

[CLICK]

Agentforce is an AI agent platform built into Salesforce that lets businesses deploy autonomous AI agents to handle tasks across sales, service, and marketing without human intervention. The agents can reason, take action, and work across Salesforce data and workflows in response to real-world triggers.

[CLICK]

This data can include data submitted by external actors, and the vector for this vulnerability was the Salesforce "web to lead" feature, that allows external users, think website vistors, conference attendees and so on, to submit lead information that directly integrates with the Salesforce CRM system. This is where a hostile actor can include malicious instructions in data an AI agent will later process.

[CLICK]

When an internal user tasks the AI agent with say, summarizing the leads generated at conference, that malicious payload becomes part of the agents context and if the prompt is crafted properly, can be used to exfiltrate data.

[CLICK]

Now, Salesforce has controls in place and guardrails for their agents to prevent this kind of thing, but they'd left a hole. The exfitration vector in this case was a call out a url my-salesforce-cms.com that was an expired Salesforce URL that Noma Labs was able to buy for $5. But key here is that it was still allow listed as an approved domain in Salesforces security controls.

[CLICK]

This attack is also interesting because it yet again brings home the point that in the vast majority of cases, a vulnerability on its own is not enough for a successful attack. It's extremely rare to find a vulnerability only exploit, which means that good posture hygene can protect us, even when the nature of the threat is new and poorly understood. So novel threat surface, yes, and that's challenging, I'm not minimising that, but you defend with tools you do already know and understand.

SOURCES (verified): ForcedLeak, Noma Labs, September 2025. CVSS 9.4. Salesforce
Agentforce via the Web-to-Lead feature; exfil to an expired-but-allowlisted
Salesforce domain (my-salesforce-cms.com) bought for $5.

---

## DISPLAY 7 - Real incidents in real deployments (action unauthorized / output hostile)

ON SLIDE: Meta/Instagram (in the wild, May 2026) - "The action is unauthorized" -
AI support agent tricked into sending reset links to attackers; 20,225 accounts
hijacked (incl. @WhiteHouse); cause debated (prompt injection vs missing auth
check); either way the agent acted on unverified instructions. Lenovo "Lena"
(red-team, Aug 2025) - "The output is hostile" - one ~400-char message made the
bot emit attacker HTML; rendering it stole the support agent's session cookies;
opened Lenovo's support back-end (live and archived customer chats). A pure AI
weakness: prompt injection + unsanitised output.

SPEAKER NOTES (in deck):

Two more breaches to look at now to see some other classes of AI threat.

[CLICK]

So, just last month Instagram was breach via an AI vector.

The compromise was via Meta's AI assistant for Instagram account support, the one that helps people who've locked themselves out get back in. And honestly, its a reasonble thing to seek to automate, account recovery is high volume and a real pain to staff.

The attackers used a VPN to look like they were in the right part of the world, then asked the assistant to add a new email address onto somebody else's account and then request a password reset link.

That was it, and the AI tool did that without any verification the new address had anything to do with the account owner. Meta's own notice puts it at over twenty thousand accounts, including the old dormant White House handle, which got defaced, and a senior US Space Force officer.

Now here's the bit I find really instructive. The press called this prompt injection, which I guess is technically true, but it was very basic one, they litterally just asked a chat interface to add an email address to the account.

Meta called it a bug in a separate bit of code that failed to verify the email, which I think is also a stretch. Take the AI out of it altogether, and what you're left with is a privileged action, changing the recovery email on an account, happening on the say-so of someone who was never verified. We've known we should defend that for decades.

This is an permissions boundary issue, the agent was over permissioned and could act without appropriate safeguards.

[CLICK]

The Lenovo Lena breach was another one discovered by security researchers, this time at Cybernews, and to be fair to Lenovo, it was disclosed properly and fixed before it went public, so nobody actually got hit, but it was live and it worked.

Lena is Lenovo's customer support chatbot on their website. Again, a completely standard thing to deploy using an AI tool.

And the whole attack was a single message, a few hundred characters. It reads like an ordinary product question, but tucked inside it tells the bot to reply in HTML and to include an image tag pointing at a url controlled by the attacker that includes all cookie data as part of the url parameters. From there it becomes a classic cross site scripting attack via a poisioned session context, because what happens next is the attacker asks to speak to a customer service agent.

When the customer service agent opens the chat history, their own browser intprets the models HTML output and the attackers endpoint is hit with the support agents full cookie collection. This would allow access into the support agent's account.

Here, Lenovo were actually santising the input from external users, and HTML data would have been filtered or blocked, but they didn't have the same controls on their AI system's output.

The weakness itself is genuinely new and AI-shaped, a prompt injection, and a bot producing output it never should have. But the actual break-in is cross-site scripting and cookie theft, and we've understood those for twenty years. And so are the defences, sanitise what the bot puts out, lock down what the browser's allowed to run, and treat anything the AI produces as untrusted.

So, three different threat vectors for AI, hostile input, unauthorised action, hostile output. But notice that not one of the compenstating controls that could have prevented the attacks is new. But you'll have spotted that all three turn on the model doing something it shouldn't, on being talked into it. And the obvious question then is, well, can't we just train the model to resist that?

SOURCES (verified): Meta/Instagram, in the wild, May 2026, 20,225 accounts
(per Meta notice; incl. dormant @WhiteHouse handle, senior US Space Force
officer). Lenovo "Lena", Cybernews red-team, Aug 2025, disclosed and fixed
pre-publication.

---

## DISPLAY 8 - How about lab conditions? (Gray Swan ASR)

ON SLIDE: (chart) ref arxiv.org/pdf/2603.15714

SPEAKER NOTES (in deck):

Which is exactly what the model providers are trying to do.

The plot above is from a paper written about a competition run earlier this year by Gray Swan, together with CAISI, that's the NIST AI standards body, the UK's own AI Safety Institute and representatives from Anthropic, Open AI and Meta.

In the competition they got participants to attempt indirect prompt injection attacks, so instructions hidden in data the agents read, against real agents. They tested thirteen of the at the time frontier models, with 464 participants running nearly 300 thousand attack attempts.

Each bar on the chart is the attack success rate for one model, so the share of attacks that actually landed, that got the model to do what the attacker wanted instead of what it was supposed to do. So lower is better here.

And there's a real spread. The most robust on the day was Claude Opus, down at about half a percent. The most vulnerable, Gemini 2.5 Pro, up at eight and a half. So the models genuinely do differ, this isn't all the same.

Now here's the bit I find genuinely interesting, and a bit counterintuitive. You might assume the cleverer, more capable model is the safer one. It isn't. The researchers found robustness barely tracked capability at all. The clearest example is that Gemini, which was about the most capable model in the whole field at the time, and also the most attackable one on the board. So robustness comes from how hard the maker actually worked to train the thing to resist, it is not something you get for free by buying the cleverest model.

But here's the real answer to our question. Look along the bottom, there's no bar at zero. Every single one of the thirteen got successfully attacked. And there will likely never will be a zero, because a model resists this stuff the way a well-trained person resists being conned, it's pattern recognition, it's not a firewall. It's good, but it's never a certainty.

And even that half a percent for Opus, which sounds reassuring, remember that's per attempt. And attackers don't have one go and wander off, they go again and again and again, and the successes just stack up, they never level off. So half a percent an attempt quietly becomes a near certainty if someone's determined enough to keep going.

So, back to where we started, can you rely on the model's own resistance? You can pick a more robust one, and you absolutely should. But you can't rely on it, because every model up there can be turned, and the door stays open whichever one you pick. Which is why the answer was never "pick a better model", it's "stop asking the model to defend itself in the first place", and start building the defences around it. And that's what the rest of the session is really about.

SOURCES (verified): Gray Swan Indirect Prompt Injection Arena, Q1 2026 (ran 25
Feb - 11 Mar 2026), run with CAISI + UK AISI. 13 models, 464 participants,
272,000 attempts, 8,648 successful attacks across 41 scenarios. ASR range 0.5%
(Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro); no model at zero; robustness only
weakly correlated with capability. arXiv 2603.15714; NIST/CAISI research blog.
(CAISI = renamed US AISI; do NOT call it "US AI Safety Institute at NIST". Note:
deck notes round 272,000 to "nearly 300 thousand".)

---

## DISPLAY 9 - The supply chain into your agent

ON SLIDE: A new, unvetted channel feeding code straight to your agents. ~1 in 8
malicious - 341 of 2,857 skills on one marketplace were outright malicious (a
real infostealer campaign: browser credentials, SSH keys, crypto wallets) - Koi
Security, Feb 2026. Code Execution: an installed "skill" is code the agent runs
with its own permissions; a poisoned skill needs no exploit, it just runs. Zero
Review: OX Security submitted a malicious package to 11 AI-tool registries; 9
published it with zero review. A supply chain you didn't build, can't see, and
nobody's vetting.

SPEAKER NOTES (in deck):

So, every attack we've looked at so far works the same basic way, by manipulating the AI. A clever prompt, a poisoned bit of input, and on that last slide, just how little the model itself really resists that. Now I want to flip it round, because there's a much simpler attack that needs no cleverness at all. Why go to all the trouble of tricking the model into misbehaving, when you can just hand it the malicious code and get the model to run that for you without even realising its done it?

[CLICK]

And that's possible because of something that's sprung up around agents incredibly fast. There are now whole marketplaces of "skills" you install to give an agent new abilities (its content you add to the prompt), and registries of MCP servers you plug in. It's a whole new software supply chain, really, except without any of the security maturity that something like a phone app store has built up over fifteen-odd years.

So, researchers at Koi Security, big thanks to them, went and audited ClawHub, a skills marketplace. And of the two thousand eight hundred odd skills on it, three hundred and forty-one came back outright malicious. That's about one in eight. And these weren't proof-of-concept, hypothetical things, they were shipping a real credential stealer, going after browser logins, SSH keys, cloud credentials, the lot.

Now, the reason this so seriously is due to what a skill actually is. It isn't something the agent just reads and thinks about, it's instructions and scripts the agent runs, on your machine, with your agent's permissions. More akin to malware than anything else, but without a user having to take any action.

[CLICK]

And you can't really lean on the marketplace to catch this for you either. A separate team, OX Security, took a deliberately malicious package and submitted it to eleven of these AI tool registries, just to see who'd stop them. Nine of the eleven published it, no review at all.

So the point of this one's pretty simple really. It's got nothing to do with whether your model's clever or gullible. You've wired your agents up to a supply chain you didn't build and nobody's checking, and you almost certainly couldn't tell me right now what's plugged in. And that, having that list, and then treating everything on it as untrusted until it's proven otherwise, is where defending an agent actually has to start.

SOURCES (verified): Koi Security "ClawHavoc" audit of ClawHub (Jan-Feb 2026) -
341 of 2,857 skills malicious (~11.9%, ~1 in 8); infostealer payloads targeting
browser cookies, .env files, SSH keys, cloud credentials (count has since grown
past 800). OX Security MCP supply-chain advisory (Apr 2026) - benign PoC package
accepted with no review by 9 of 11 registries. koi.ai blog; ox.security blog.

---

## DISPLAY 10 - You're not inventing this alone anymore  (was DISPLAY 13)

ON SLIDE: Deck heading "THE DISCIPLINE IS BEING WRITTEN NOW" / sub-head "You are
not inventing this alone any more". Quote: "If you cannot understand, monitor or
contain an agent's actions, it is not ready for deployment" (attributed on slide
to Five Eyes, Apr 2026). Four bodies that converged within ~12 months:
- Five Eyes - "Careful Adoption of Agentic AI Services", FIVE governments
  (UK/US/AU/CA/NZ). [deck now correctly says five, not six]
- CoSAI - "The Future of AI Agent Security" + "Agentic Identity and Access
  Management" (two RSAC 2026 publications).
- OWASP - Agentic Top 10 (published Dec 2025; presented at Infosec Europe, Jun 2026).
- ISO/IEC 27090 - AI security threats standard, final draft.

BRIDGE (slide 9 -> 10): slide 9 ends the problem half at its bleakest and most
concrete - a supply chain you can't see, where "defending an agent has to start"
with inventory and distrust. That is a daunting, lonely place. Slide 10 pivots on
that feeling: you don't have to work out the rest from scratch, because the
discipline has converged in the last twelve months. Logic: "here's where defence
starts" -> "and here's the shared blueprint for the rest." Emotion: overwhelmed
and alone -> supported, not alone.

SPEAKER NOTES (synced from deck 2026-06-14 - Matt's own rewrite; reproduced
verbatim, his organic typos preserved as this mirrors the deck):

So, I'm aware that's a lot of information about the threat landscape.

We've gone from someone filling in a web form, to an agent quietly handing out password resets, to the model itself not being able to reliably defend its own front door, and then to a whole supply chain you didn't build and can't really see.

The first thing to to take away, and I hope that's been clear up to now, that the major work in defending your AI in production is to be even more rigourous with the basics than you have been up to this point. Posture controls, authentication boundaries, traditional network segementation, so much of the protection your organisation needs will come from these fundamentals. Make sure you have tooling in place to automate this and you will go a long way to being secure.

The second piece of good news is that the standards bodies are starting to publish some really excellent work on AI security frameworks to help guide our work. A lot of this is really hot of the press.

[CLICK]

Then this month, at InfoSec in London, OWASP presented their Agentic Top 10, although it was published in December 2025. That updates the AI top 10 specifically for agentic deployments. If you take nothing else away from this webinar it should be to familiarise yourself with the various OWASP top 10s that impact AI deployments, the Agentic Top 10 is just the latest in that series. Very readable, and a very useful guide for evaluating your security practices and tooling.

[CLICK]

CoSAI, or coallition for secure AI is an industry body that was only formed two years ago to create best practices, tools and methodologies for securing AI systems. At RSAC this year (RSAC is the new name for the RSA conference) CoSAI presented two key publications.

The first is an exploration of the weakness of our current security processes and controls that remain anchored to the execution and operational patterns of human-driven workflows, and detail how agentic systems produce an attack surface at the semantic layer that these mechanisms were never designed to engage.

The second deals in more detail on management of Agentic Identity, basically Agentic IAM which looks at what changes we need to IAM models for agentic systems. Things like agents needing to provide verifiable identity claims around model, harness and tool versions, short lived identities. Think configuration control or AI bill or materials, linked to something akin to a zero trust framework.

[CLICK]

Just over a month ago, cyber and sig int agencies from the so called "Five Eyes" collaboration, so UK, US, Australia, Canada and New Zealand published their guidance document titled "Careful Adoption of Agentic AI Services". It lays out the threat and best practice guidence for designing, developing, deploying and operating AI Agents Securely. Clear and readable, it contains very quotable material for your stakeholder discussions, especially because you can throw around names like the NSA or GCHQ.

[CLICK]

and I lifted a quote I thought summed up in one sentence the security gate you should have in place before you deploy an agentic system, thought that was really well put.

[CLICK]

The final one to include is the new ISO standard 27090, which is now in final draft. This is the first international standard squarely aimed at AI security threats and its a good idea to start becoming familiar with this one. This is the standard we should all expect to be audited against eventually.

Now, I'm not going to pretend four frameworks landing at once makes tomorrow morning simple, there's a real job in reading across them. But just step back and notice what's actually happened. A year ago there was very little to point at. Now governments, industry and the standards bodies have converged, in about a twelve-month window, on the same handful of ideas, know what you've got, give it an identity, be able to contain it. To borrow an analogy from Part 1 of this series, It's the building trade finally getting its building codes written, and it's happening remarkably fast. So whatever you build from here, you're building it on a floor that's being poured underneath you. And for the rest of our time, what I want to do is take those converging ideas and turn them into the concrete things I think you should actually go away and do.

---

## DISPLAY 11 - Tooling: discover what you have, then defend it  (was DISPLAY 14)

ON SLIDE: Step zero - you cannot defend an inventory you do not have. Discover
continuously: deployed models and inference endpoints; MCP servers and tool
registries; agent identities and service accounts; AI-adjacent services and data
flows (feeds your AI-BOM). Defend in depth: AI gateway with egress control (cuts
the zero-click exfiltration channel from ForcedLeak); layered injection defence
(PromptArmor <1% FP/FN; data-channel output filtering); agent sandboxing as an OS
primitive (Microsoft Execution Containers 2026); log everything.

SPEAKER NOTES (draft 2026-06-14, Matt's voice - APPROVED, pending copy-in to deck):

So, like I said, let's turn all of that into the concrete things I think you should actually go and do. And I want to start exactly where the last slide left off, with the basics, because the very first one is the most basic of the lot, and it's the one almost everyone skips.

[CLICK]

Discovery. Step zero. You cannot defend an inventory you do not have, and we keep bumping into this all the way through today. It's the poll we did right at the start, the honest "probably, and we're not completely sure". It's that line on the layers slide, that most of you can't see three or more of them. It's the supply chain a few slides ago, where I said you almost certainly couldn't tell me right now what's actually plugged into your agents. Same problem, over and over. So before any clever defence, you need a live, continuous picture of what you're actually running in production, your deployed models and the endpoints they sit behind, your MCP servers and tool registries, the identities your agents are using, and the data flowing in and out. Continuous, mind, not a spreadsheet somebody did once last spring, because this estate changes by the week. And that inventory isn't just for its own sake, it's what feeds the AI bill of materials we'll come to on the governance slide.

[CLICK]

Then, and only then, defence in depth, and you'll notice none of these are exotic either. An AI gateway with egress control, so you take charge of where your agent is actually allowed to send things, and that on its own would have stopped ForcedLeak, because remember that whole attack came down to data walking out to a domain that should never have been on the allow list. Then layered injection defence, and here's a point worth being honest about, you can filter what goes in, and you should, but input filtering is the weakest link, a determined attacker just adapts around it. The more durable control is on the way out, sanitising what the model produces and controlling the channel it's allowed to use, and that's the layer that actually held up in testing where the input-side guards fell over. It's also, as it happens, exactly the two controls that would have caught the Lenovo bot, sanitise the output, lock down the channel. Then sandboxing, which is now arriving as a proper operating-system feature rather than something you have to bolt on yourself. And finally, log everything, every prompt, every tool call, every memory write, because when, not if, something does go wrong, that log is the difference between an afternoon's investigation and a very long week.

[CLICK]

And the line at the bottom there is really the whole philosophy of this half of the talk. Discover first. Then assume the model is fallible, take it as a given that it can be talked into something daft, and build the architecture so that when it is, the damage is contained. That's the shift from hoping the model behaves, to engineering as though it won't. And the single highest-leverage place to start that engineering is identity, which is exactly where we're going next.

NOTE (orphaned stat from the cut): the "82% found agents they did not know about"
(CSA 2026) figure lived on cut old-DISPLAY-11 and is now absent from the deck. It
is a strong discovery-spine stat - consider relocating it here to open the
"discover" half.

---

## DISPLAY 12 - Identity: agents are first-class identities  (was DISPLAY 15)

ON SLIDE: Highest-leverage control. The answer to "you cannot stop them" is: make
every agent stoppable by design. With machine/AI identities outnumbering humans
109:1, shared service accounts are no longer acceptable. (1) A named human owner -
no owner, no agent in production. (2) Its own credential - per-agent, enabling
attribution/revocation/audit (Entra Agent ID). (3) Task-scoped, just-in-time
access - blast radius bounded by design. (4) A rehearsed kill switch - a control
plane, tested quarterly (CoSAI blueprint). 60% cannot terminate a misbehaving
agent today.

SPEAKER NOTES (draft 2026-06-14, Matt's voice - APPROVED, pending copy-in to deck):

So, identity. If you take one practical thing from this whole second half, I'd want it to be this one, which is why it's flagged there as the highest-leverage control. And it's the answer to the most uncomfortable problem sitting under everything we've looked at, that an agent acts on its own, at machine speed, and if it gets something wrong, whether it's been tricked into it or it's just made a daft call by itself, you need to be able to step in and stop it. So the whole game on this slide is making every agent stoppable by design.

And the way you do that isn't new either, it's identity, the thing I flagged right back on the layers slide as the new perimeter. What's changed is the scale. Machine and AI identities already outnumber human ones by something like a hundred and nine to one, and that's only heading one way. At that scale, the old habit of letting a handful of agents share some catch-all service account is finished, because the moment you do, you've lost any hope of knowing which agent did what. So, four things, and you already run every one of them for your people.

[CLICK - box 1]

First, a named human owner. An actual person accountable for what that agent does, what it's allowed to touch, and how long it lives. No owner, no production, simple as that.

[CLICK - box 2]

Second, its own credential, no sharing, ever. Because a unique identity per agent is the only thing that gives you real attribution, the ability to revoke just the one without taking everything else down with it, and a clean audit trail. And this is becoming a platform feature now, Microsoft's Entra has agent identities built in.

[CLICK - box 3]

Third, access that's scoped to the task and granted just in time, handed over when the job starts and taken straight back the moment it's finished, so the blast radius is bounded by design rather than by luck.

[CLICK - box 4]

And fourth, a rehearsed kill switch, and I'd really lean on the word rehearsed, because a kill switch you've never tested is a hope, not a control. Think of it as a control plane rather than one big red button, and tabletop it quarterly the same way you'd rehearse any other incident. CoSAI have published a blueprint for building exactly this.

[CLICK - bottom line]

And here's why all of this actually bites. Today, around sixty percent of organisations admit they could not terminate a misbehaving agent right now, if they had to. So this isn't theoretical tidiness. But notice none of those four is exotic, it's named owners, individual credentials, least privilege, and a tested way to pull the plug, every one of them something you already know how to do. The shift is just insisting they apply to your agents too. If a thing can act in your environment, it has to be an identity you can name, scope, and stop. And once it is, you've finally got something you can hold to account, which leads us straight into how you make sure it's actually behaving.

PROVENANCE (the four rules): synthesis of CoSAI "Agentic Identity and Access
Management" (RSAC 2026; per-agent identity, named owner(s), JIT task-scoped
access, kill switch) + the industry "four pillars" consensus (ownership / JIT /
kill switch / distinct identity) + Microsoft Entra Agent ID (per-agent credential
as a platform feature). Stats: 60% cannot terminate = Kiteworks; 109:1 = Palo
Alto. NOTE: not a verbatim quote from one document - CoSAI frames it as nine
imperatives and asks for TWO named humans (sponsor + owner). Attribute as "drawn
from CoSAI + emerging consensus", not "CoSAI's four rules". Also: the on-slide
'answer to "you cannot stop them"' callback lost its setup slide (parked) - the
notes above re-establish that point so it still lands.

---

## DISPLAY 13 - Process: red-team as launch criteria  (was DISPLAY 16)

ON SLIDE: Static ASR numbers from vendors are not a security posture. If you did
not attack it, you have not tested it. (1) Red-team your own models - prompt
injection against deployed systems; Garak, PyRIT, AgentDojo; a launch gate not an
annual tick. (2) Scan your MCP attack surface - tool poisoning, excessive scope,
missing auth. Red-teaming now runs at agent speed (681 assessments in ~3 hours,
Dreadnode 2026). AI-aware IR playbooks; kill-switch tabletops quarterly.

SPEAKER NOTES (draft 2026-06-14, Matt's voice - APPROVED, pending copy-in to deck):

So, you've discovered your estate, you've built the architecture around it, and you've given every agent an identity you can name and stop. The obvious next question is, how do you actually know any of it works? And the honest answer is the same one we landed on at the lab-conditions slide, you don't, not until you've attacked it yourself.

Because think back to that Gray Swan chart, every one of those frontier models had a published safety story, and every single one of them still fell. So a number a vendor hands you, an attack success rate from their own testing, is genuinely useful, but it is not your security posture. It was measured on their system, against their attacks, not yours. The only number that means anything is the one you get attacking your own deployment. Or, the way it's put up there, if you didn't attack it, you haven't tested it.

[CLICK]

So, two practices, and neither is new to anyone in this room, we've been doing this to web apps for twenty years, this is just pointing the same discipline at AI. The first is to red-team your own models, actually run prompt injection attacks against the system you've deployed, the way a real attacker would. There's a decent open toolkit for it now, things like Garak, PyRIT and AgentDojo, and the key shift is to make this a launch gate, something a system has to pass before it goes live, not an annual tick-box you do once and file away.

[CLICK]

The second is to scan your MCP attack surface, and this is the supply chain from earlier coming back round, every MCP server and every skill you've plugged in, checked for tool poisoning, for permissions that are far too broad, for missing authentication. Same cadence, continuously, not once.

[CLICK]

And the reason it has to be continuous is speed. The attackers are operating at machine speed now, and the good news is so can your testing, there's work showing red-team tooling running something like six hundred assessments in a matter of hours. So the principle is simple, your evaluation cadence has to match your deployment cadence, if you ship weekly you test weekly. Alongside that, make sure your incident response actually knows what an AI incident looks like, memory poisoning, an agent gone rogue, a compromised vendor model, those aren't the playbooks you wrote for ransomware. And rehearse that kill switch we just talked about, quarterly, so it's muscle memory before you ever actually need it.

So that's the operating rhythm that keeps everything else honest. But controls and testing on their own won't survive contact with a busy organisation, things drift, people leave, budgets move. And that's where the last piece comes in, governance.

NOTE (parked deck fix): on-slide text says "as Slide 10 demonstrated" - that
reference pointed at the old infra slide (now parked) and is broken. The spoken
notes above instead reference the Gray Swan / lab-conditions slide (DISPLAY 8) by
name; the ON-SLIDE text still needs the same fix. TO VERIFY: Dreadnode "681
assessments in ~3 hours" (notes soften to "~600 in a matter of hours").

---

## DISPLAY 14 - Governance: anchor, owner, measure  (was DISPLAY 17)

ON SLIDE: Controls without governance have no durability. Anchor: ISO/IEC 42001
today; ISO/IEC 27090 at final draft; EU AI Act transparency Aug 2026, high-risk
Dec 2027; Annex IV maps to an AI-BOM. Owner: a named human against every
inventory entry - no owner, no production. Measure: report upwards - ASR per
category, blast radius per agent, shadow-AI exposure (employee AI use tripled to
45%, DBIR 2026). Translate metrics into pounds and owners.

SPEAKER NOTES (draft 2026-06-14, Matt's voice - APPROVED, pending copy-in to deck):

So, governance, and I know the word makes some people's eyes glaze over, but stay with me, because this is the bit that stops everything we've just covered quietly falling apart six months after you've built it. Controls without governance have no durability, the rigour slips, things drift, and you're back where you started. So, three simple pillars, and the real value of them is that they translate all this technical work into language a board actually responds to.

[CLICK]

First, anchor it to a standard, so you're not just making it up as you go. ISO 42001 is there today for managing AI, and 27090, the AI security one I mentioned earlier, is at final draft, so start getting familiar with it now. And there's a clock on this, the EU AI Act, its transparency obligations land this August, and the high-risk ones at the end of next year, and crucially its Annex IV documentation maps more or less directly onto an AI bill of materials. Which is that inventory from the discovery slide coming full circle, the list you built isn't just operational hygiene, it's the thing the regulator is going to ask you for, so far better to be building it now than in a panic later.

[CLICK]

Second, owner. Now we said back on the identity slide that every agent needs a named human against it, and this is simply the governance side of that exact same coin. At the technical level, an owner is what makes your kill switch usable. At the board level, it's accountability, a real person whose name is against that system. And the rule is just as blunt, no owner, no production. That isn't bureaucracy, it's the thing that makes every other control actually enforceable.

[CLICK]

And third, measure, because the board can't act on what it can't see. Report a handful of things upward, and regularly, your attack success rates by category, the blast radius each agent could cause if it went wrong, and your shadow AI exposure, and that last one is very real, employee AI use roughly tripled in a year, to something like forty-five percent. But here's the important part, don't report it in attack success rates and CVE numbers, translate it into pounds, and into named owners, because that's the language the board makes decisions in. Do that, and you've turned all of this from the security team's private worry into something the business actively manages.

And getting it measured, and spoken about in the boardroom's own language, sets up the very last thing I want to leave you with, which is, genuinely, good news.

TO VERIFY: EU AI Act dates (transparency Aug 2026 / high-risk end-2027); DBIR 2026
"shadow AI tripled to ~45%". Both carried from v3, not re-checked this session.
NOTE: "owner" is deliberately framed as the governance side of the DISPLAY 12
owner (resolves the double-owner overlap); "AI-BOM = inventory full circle" pays
off the DISPLAY 11 discovery promise.

---

## DISPLAY 15 - You are the enabler, not the brake  (was DISPLAY 18; REDESIGNED 2026-06-14)

ON SLIDE (redesigned - lean reframe slide; replaces the old "defences are
arriving" tooling recap). Deliberately spare - the argument lives in the spoken
notes, not on the slide:
- Kicker: ON THE OTHER HAND
- Title: You are the enabler, not the brake
- One big stat (echoes slide 2): 62% say security is the #1 blocker to scaling AI
- One-line reframe: So the team that opens that gate safely doesn't slow the
  roadmap - it unlocks it.
- Source: McKinsey / Stanford AI Index 2026

DROPPED from the old slide: the MXC/sandboxing re-list and "layered defence works"
(duplicated DISPLAY 11), and "discipline consolidated" (duplicated DISPLAY 10).
NOTE: the live deck (display 17) still has the OLD "defences are arriving" content
- this redesign is pending copy-in.

SPEAKER NOTES (draft 2026-06-14, Matt's voice - APPROVED, pending copy-in to deck):

So, I've thrown a lot of uncomfortable things at you over the last half hour, and I really don't want to leave you with the impression that any of this is hopeless, because I genuinely don't think it is. So let me end on the other side of the coin, and on something I think is actually a real opportunity for everyone in this room.

[CLICK]

Cast your mind right back to the very start, to that figure I put up, that across organisations security came out as the number one thing holding back the scaling of agentic AI, ahead of all the technical limitations. Now when I showed you that at the beginning, it was a problem, it was the size of the gap we're all living in. But I want you to look at it again now, from the other end, because it's also the single most empowering number in this whole talk.

Think about what it actually means. The business wants AI, badly, it's the thing every board is pushing on right now. And their own assessment, not ours, not security crying wolf, their own assessment is that the one thing standing between them and that ambition is security. So just follow that through. If security is the gate, then the people who can open that gate safely, and that's you, you are not the brake on the AI roadmap. You're the thing that unlocks it.

And that's a genuine shift for our profession. For most of my career security's been cast as the department of no, the cost centre, the people who slow the business down. And here, for once, on the biggest strategic bet most of these companies are making, it's the other way round. Everything we've talked about today, discovering what you've got, giving your agents real identities, red-teaming your own systems, getting the governance in place, none of that is a tax on AI, it's the permission slip for it. It's what lets the business say yes, and say it with some confidence.

And the means to do it are arriving, and quickly. The frameworks are being written, as we saw, and the controls and the tooling are maturing fast. This is a solvable problem, it genuinely is, it's just not a solved one yet. So I'd really encourage you to walk out of here and take that reframe back to your leadership. You are not the brake. Done well, you are the single biggest enabler of the thing your business most wants to do. And I think that's a rather brilliant position for us to be in.

---

## DISPLAY 16 - Questions / Series Close  (was DISPLAY 19)

ON SLIDE: The two-part series. Part 1: The New SDLC - securing the AI that writes
your code. Part 2: Running AI in Production - what you are actually defending now.
Monday-morning checklist: discover your AI estate (models, MCP servers, agents,
inference endpoints); make every agent a named, scoped, killable identity;
red-team your own models and MCP surface continuously; translate it for the board
in dollars and owners. Full bibliography on request. Non-product.

SPEAKER NOTES: [TO WRITE]
