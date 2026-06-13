# Part 2 - Defending AI in Production: Speaker Notes v4

Working document, synced to the REORDERED deck (display order, 19 slides).

Order now: Title -> hook -> architecture primer (anatomy, agents, what you
deploy) -> breach cluster (ForcedLeak, Meta/Lenovo) -> lab conditions -> supply
chain -> infra -> can't stop -> attacker moves second -> discipline -> Discover /
Identity / Process / Govern -> optimism -> close.

- Notes drafted/existing: 1, 2, 3, 4, 5, 6, 7, 8
- Notes still to write: 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19

Existing notes reproduced verbatim from the deck (spelling left as-is), unicode
normalised to ascii. Nothing here is final - we are workshopping.

---

## Voice / tone reference (from Part 1)

Keep these when we rewrite:

- Warm, humble open; credentials worn lightly; "why this matters to me," not status.
- Caveat hard and early; comfortable saying "I'm not sure, to be honest."
- Self-deprecating ("which idiot wrote this - oh, it was me").
- Generous credit to researchers ("big thanks to them").
- One strong analogy per major turn (Part 1: building trade, aviation autopilot).
- The refrain: "none of these are new controls" = the "new attack, old control" spine.
- Direct address and solidarity: "you already know this," "we as practitioners."
- British, spoken rhythm; "So," openers; long natural sentences.
- Close on an honest optimistic steel-man.

NB: the polished/rhetorical register in the slide 8 notes was AI-assisted - do
NOT use it as the model. Match slides 1, 3 (anatomy), 5 instead.

---

## DISPLAY 1 - Title: Defending AI in Production

ON SLIDE: "The New Normal: Software, Security and the AI Stack - Part 2 of 2".
Defending AI in Production. Matt Campbell, Senior Security Solutions Architect.

SPEAKER NOTES (existing):

Hello again everyone, and thank you once again for taking the time out of your
no-doubt packed schedules to join us today, and thank you John for the
introduction.

My name is Matt Campbell, and as you can see on the slide, I'm one of the
solution architects at Qualys, assisting our customers, and prospective
customers to select, deploy and optimize Qualys products to achieve their
security objectives, but also advising on their security practices more
generally.

As I said last time, this isn't what I've always done, I started my career as a
developer and then application architect, then moved on to work in various
system architecture roles working large scale and complex CI/CD programmes at
Ericsson, one of the largest telco infrastructure OEM's. There we spent a lot of
time thinking about how we could deploy our products securely...

In part 1 of this two part series, we looked at the security implications of the
rise of AI tools being used in the software development lifecycle. We looked at
some of the latest research that's been published, by both commercial and
academic authors, about the security weakenesses AI tooling can introduce when
used by your developers. Then explored some of the mitigations you can apply as
organisations to try to manage and reduce those risks, while accepting that some
level of risk is currently unavoidable as thing currently stand.

Today, we're going to take a look at what happens post development, when you
yourselves have shipped AI features - a model, a prompt, tools, agents, a supply
chain - and you are now defending a system whose inputs can come from anyone on
the internet, and whose output is non-deterministic.

Like last time, I need to start with a heavy caveat. Things are moving extremely
fast in this space, and none of us know what the future holds even in the short
term.

I was at Infosec last week and good conversation with a security architect from a
large retailer, who'd been tasked by his leadership to produce a 10 year cyber
security plan. We both had a bit of chuckle about that.

So, as last time, its hard to give clear guidance on these issues, there are no
simple answers at the moment, so the best I can do is give my opinion on what I
think practitioners and the industry as a whole needs to do to mitigate some of
the clear dangers we can see.

Also, like last time, no doubt your organisations will be grappling with these
issues over the comming months and years, so please do use forums like this, and
others, or blog posts, or conferences to share your findings and learnings, what
works, what doesn't, so we can all progress.

---

## DISPLAY 2 - It's already out there

ON SLIDE: 99% of organisations already run autonomous AI agents in production
(Palo Alto, 2026). 83% plan agentic AI, yet only 29% feel ready to secure it
(Cisco, 2026). 62% name security as #1 blocker (McKinsey via Stanford AI Index
2026). Live poll: "Has someone in your organisation shipped an AI feature you did
not know about? The gap between deployed and defended is where you live."

SPEAKER NOTES (draft v4 - in Matt's own voice):

So before we get into any of the architecture, or look at how this is actually
being exploited, I just want to ground us in where we are right now, as
organisations.

And I'm going to go quite quickly over the obvious part. Everyone in this room
knows AI is out there, you know your developers are using it, you know there are
agents running somewhere in your business. I don't need to convince anyone of
that, and that first figure, nearly every organisation now running agents in
production, really just confirms what you already feel in your bones.

The bit I think is actually worth pausing on is the gap. Because at the same time
as more or less everyone is shipping this stuff, only about a third feel anything
like ready to secure it. And when the question was asked about what's holding back
scaling agentic AI, security came out as the number one blocker, ahead of the
technical limitations. So this isn't me, as a security person, standing up here
telling you that security is the problem. It's the businesses themselves saying
it.

That gap, between what we've already deployed and what we can actually defend, is
really what this whole session is about. It's where you, as the people carrying
the responsibility for this, are living right now.

[POLL] And before I move on, I'd like to do a quick poll, just to make it a bit
more real. Has someone in your organisation shipped an AI feature that you, in
security, didn't know about until later? Have a think, be honest, it stays
anonymous. In my experience the honest answer for a lot of organisations is
"probably, and we're not completely sure", and that's really the heart of it. You
can't defend something you don't know you've got, and that idea, discovery, is one
we'll keep coming back to today.

So over the next forty minutes or so I want to do a few things. First get clear on
what an "AI feature" actually is, because it's a good deal more than just the
model. Then look at some real incidents, because that's where the patterns start
to show. Then be honest about why we can't just lean on the model to defend
itself. And finally, what I think we should actually be doing about it, which, as
you'll see, is mostly things you already know how to do.

[Transition note: this verbal roadmap doubles as the content for a roadmap slide
if one is added.]

---

## DISPLAY 3 - System anatomy

ON SLIDE: Model / Harness / MCP Server. Tools and RAG are similar.
(ref: anthropic.com/engineering/code-execution-with-mcp)

SPEAKER NOTES (existing):

Before digging any futher, I'd like to just clarify a few architecural points
about what an AI, and in particular I'm talking about an LLM here, actual is in
operation, because there's a lot of confusion and misunderstanding out the in
industry.

So, firstly the model itself. Often hosted on remote servers supplied by the
model builders, like Anthropic or OpenAI, or on a hyperscaler platform like AWS
Bedrock, or Azure AI Foundry.

The model is the brain of the system and its what does the reasoning. They are
complex collections of matrix operations that generate text in response to input
text. So, pass in text, get text out.

Some key features

- They're stateless. They have no sense of time and no memory. You add text in
  one side and get text out the other side as a 1 hit.

- They're static. The model is trained then released and after that release it
  does not change for the duration of its lifetime. They do not train on what
  they see, that is common myth, they do not learn while in operation (of course
  the model provider may be capturing your input to add to the training data of
  their next model, but the model you are using yourself won't learn from you.

- They're probabilistic. Although they're pure functions, not dependent on
  history or anything external, other than the prompt, they still have a level of
  non determinism because their response is sampled from a probability
  distribution of possible responses. I won't go any deeper into that, but if
  anyone would like to dig further, go and look up what the temperature setting
  does as a jumping off point to understand this better.

Given these characteristics of the model, they aren't very useful without a
harness. Harnesses are things like Claude Code, a developers AI enabled
development environment like Windsurf or cursor, or the chatgpt web interface.
The harness is what makes it all come alive. It's the harness that's managing the
chat history that makes the model feel statful. Its the harness, as we can see
here, that interacts with things like an MCP server to allow tool calls or
information to be fetched.

One very important thing to understand is becuase the model is stateless, the
entire context, so the full conversation history, including everything you sent
to the model, and all the models replies are sent to the model each turn. That's
what makes it feel conversation or stateful, the model is recieving the entire
history of the session each time, with your latest addition that it responds to,
but responding to it after processing the entire context.

And finally shown here, we have an MCP that allows tool calls to be made, which
could be basically anything.

And here's the one thing I really want you to take away from this slide, because
it comes back again and again today. All of that context, everything going into
the model each turn, is just one block of text as far as the model is concerned.
The instructions you gave it, the system prompt the harness wrapped around it, a
document it pulled in, an email it was asked to read, the result of a tool call,
it all arrives as the same kind of thing, down the same channel. The model has no
reliable way of telling "this part is a trusted instruction from my operator"
from "this part is just some data I was asked to look at". To the model, it all
looks the same. And almost every attack we're going to look at today, when you
strip it back, is really just someone taking advantage of that one fact.

---

## DISPLAY 4 - Autonomous agents

ON SLIDE: Same model underneath, stateless, text in / text out; what changes is
who's driving the loop. Chatbot/coding assistant: you're in the loop every turn.
An agent hands "what's next" to the model and runs the loop itself. That autonomy
is the whole point - and the whole risk.

SPEAKER NOTES (v4 - warmed into Matt's voice):

So we've got the model now, and we've got the harness wrapped around it, holding
the conversation and making the tool calls. The thing I want to pull out on this
slide is the difference between a harness you sit and work with, and an agent,
because they're really not the same thing and that distinction matters a lot for
the rest of today.

When you're using a chatbot, or a coding assistant like Cursor, you're in the
loop the whole way through. You ask it something, it answers, you read what it
said, you decide if you're happy with it, and you decide what to ask next. Every
single turn, there's a human, you, making the call about what happens next. It's
quick, but it's still you doing the driving.

An agent is what you get when you take that decision, the "right, what do we do
next" decision, and hand it over to the model itself. You give it a goal, and
instead of coming back to you at every step, it works out the next step on its
own, it takes an action, and by action I mean actually going off and doing
something, calling a tool, reading a file, firing off a request, then it looks at
whatever came back, and round it goes again. Over and over, until it reckons the
job's done.

And underneath, nothing's really changed about the model. It's still that same
stateless, text in text out thing we were just talking about, being called over
and over with the whole context each time. What's changed is you. You've stepped
out of the loop. All those little decisions you used to make every turn, they're
being made by the model now, on its own.

And that's the shift that matters for everything that follows. Think back to that
one fact from the last slide, that the model can't really tell your instructions
apart from data it's been handed. With a chatbot that's not the end of the world,
because if it gets tricked and says something daft, there's a human sat right
there to catch it before anything actually happens. Take that human out, which is
exactly what an agent does, and there's no one in the middle any more. It just
acts on its own judgement, and if that judgement's wrong, or if someone's slipped
it instructions through that same channel, well, it acts on that too, and carries
straight on to the next step. So we've gone from a thing that answers to a thing
that acts, and that, really, is the whole ballgame for everything we look at
today.

---

## DISPLAY 5 - What you actually deploy

ON SLIDE: Anatomy of a production AI feature. Six layers, each a threat vector:
Model (provenance, poisoned weights, malicious pickle files); Prompt (injection,
direct and indirect); Tools/MCP/RAG (tool poisoning, over-broad scope); Memory
(poisoning and persistence); Identity (sprawl and over-privilege, shared service
accounts); Data Flow (exfiltration and logging gaps). Self-audit: most
organisations lack visibility on three or more of these layers.

SPEAKER NOTES (existing):

So understanding AI systems are way more than just the model in use, so lets
build up some shared vocabulary, so we can turn "AI workload or system" into a
concrete inventory we can reason about through the rest of the webinar.

We'll also touch on some of ways these various system components are vulnerable to
attack, start enumerating this "new attack surface" I'm talking about.

[CLICK]

Firstly, the model itself. Who vended it, where did it come from. You're probably
less concerned about this if you're using Anthropic, or OpenAI (although even
then you may have concerns about training bias that could impact your particular
use case), but as the model landscape broadens or we start using open source
models and things, we're opening ourselves up to some quite sophisticated attacks
that could be all but impossible to detect, at least as we currently understand
it. Not seen in the wild yet, as far as I know, but there have been
demonstrations done. The other vectors are bit more standard, basically packaging
malicous code alongside model weights as part of their serialization formats.

[CLICK]

Prompt injection, and we've really already met this one, it's that same-channel
problem from the anatomy slide a moment ago. It's the layer everyone thinks of
first. The idea is simply that if you can get malicious instructions into the
model's prompt, you can get it behaving in ways at odds with whoever's hosting
it. And it comes in two flavours. There's direct injection, where the attacker
types straight into something you've exposed, a chat box on your website say. And
then there's indirect, where the malicious instructions ride in on data the model
goes off and fetches for itself, a document, a web page, a record in a database.
And it's that indirect kind that's the quiet killer, because the attacker never
has to talk to your system at all. In fact we'll see exactly that in a minute
with the Salesforce breach.

[CLICK]

Tools, MCP servers and Retrival Augmented Generation are a key ways we can allow
interaction with systems outside the immediate harness process. They can wrap
databases, or other software tools, anything at all really so that models (or
more accurately model harnesses) can pull data into the prompt, or allow the
model to take downstream action. Clearly this makes them a major threat vector,
both for context posioning, which is just another way to say prompt injection,
and for downstream exploits, an MCP server that's permissions are too broad
increases the blast radius of any expoit that happens with the model or with any
harness components.

[CLICK]

Attacking the memory system of harnesses is another way to achieve prompt
injection. A lot of tools and agents have memory systems now, of varying levels
of sophistication. The idea being, LLMs are stateless remember, that key
information can be written by harnesses during operation that mean that agents or
systems can resume with a history, mainly by just loading that history into the
harness session.

[CLICK]

Looking at some more traditional security issues now, identity is as important a
control over your security as anything else. Identity as the new perimeter, as we
say in cloud (not so new any more), where its good control over identity that
limits the blast radius of any breach. Again, pre-AI security practicies and
tooling can secure our systems, even when the threat vectors are new. Now, in
order to do something useful, most like your AI systems will need access to data
that is sensitive at some level, the key point is to take positive control of
that and know clearly what your identity boundaries are, and having tooling in
place to manage them

[CLICK]

Finally, securing your data flows. Here many things that aren't new. Limit access
to data to only what's required for the task, control egress channels with
controls at various levels, level 7 for domain whitelisting, Layers 3 and 4 for
network level controls. Like many other controls is about taking concious control
of the scope you give to your agents and the channels they can use, and block
everything else, with tooling to maintain that configuration over time so things
can't drift.

So keep these six in your head, because the breaches we look at next aren't
anything exotic, they're just these layers going off, usually two or three of
them at once. And the uncomfortable bit is really that line at the bottom of the
slide, that most organisations can't see three or more of these layers at all.
Which is that same discovery problem from the poll earlier, you can't defend a
layer you don't even know you've got.

---

## DISPLAY 6 - The attacker filled in a web form (ForcedLeak: the input is hostile)

ON SLIDE: "Forcedleak: The input is hostile". Agent Deployed -> Hidden Payload
(Web-to-Lead) -> Agent Executes (lead summary) -> Data Exfiltrated (image call to
trusted domain). CVSS 9.4, Noma Labs, Sep 2025. No social engineering, no
phishing - a description field in a web form and a carelessly maintained URL allow
list. (First panel of the input/action/output triad continued on DISPLAY 7.)

SPEAKER NOTES (existing + same-channel fill):

So, right on cue, here's that indirect injection I mentioned on the last slide,
only now it's a real breach rather than a definition. And I want to give this one
a bit of time, because for us as practitioners this kind of breach analysis is
really valuable, it puts flesh on the bones and you start to see the patterns
that come up again and again. This one's courtesy of Noma Labs, big thanks to
them, and it's a cracking example of the new attack surface we've been building
up.

And the heading there is the key to it, the input is hostile. Think back to that
one fact, that the model can't tell your instructions from data it's been handed.
Well, this is an attacker getting their instructions in as data, and by about the
simplest route you can imagine, they just filled in a web form. No social
engineering, no phishing, no access to anything at all.

So, late last year, Noma Labs found a vulnerability chain in Salesforce's
Agentforce, which is their agentic AI framework.

[CLICK]

Agentforce is an AI agent platform built into Salesforce that lets businesses
deploy autonomous AI agents to handle tasks across sales, service, and marketing
without human intervention. The agents can reason, take action, and work across
Salesforce data and workflows in response to real-world triggers.

[CLICK]

This data can include data submitted by external actors, and the vector for this
vulnerability was the Salesforce "web to lead" feature, that allows external
users, think website vistors, conference attendees and so on, to submit lead
information that directly integrates with the Salesforce CRM system. This is
where a hostile actor can include malicious instructions in data an AI agent
will later process.

[CLICK]

When an internal user tasks the AI agent with say, summarizing the leads
generated at conference, that malicious payload becomes part of the agents
context and if the prompt is crafted properly, could be used to exfiltrate data.

[CLICK]

Now, Salesforce has controls in place and guardrails for their agents to prevent
this kind of thing, but they'd left a hole. The exfitration vector in this case
was a call out a url my-salesforce-cms.com that was an expired Salesforce URL
that Noma Labs was able to buy for $5. But key here is that it was still allow
listed as an approved domain in Salesforces security controls.

[CLICK]

This attack is also interesting because it yet again brings home the point that
in the vast majority of cases, a vulnerability on its own is not enough for a
successful attack. It's extremely rare to find a vulnerability only exploit,
which means that good posture hygene can protect us, even when the nature of the
threat is new and poorly understood. So novel threat surface, yes, and that's
challenging, I'm not minimising that, but you defend with tools you do already
know and understand.

---

## DISPLAY 7 - Real incidents in real deployments (action unauthorized / output hostile)

ON SLIDE: Meta/Instagram (in the wild, Jun 2026) - "The action is unauthorized" -
AI support agent tricked into sending reset links to attackers; 20,225 accounts
hijacked (incl. @WhiteHouse); cause debated (prompt injection vs missing auth);
either way the agent acted on unverified instructions. Lenovo "Lena" (red-team,
Aug 2025) - "The output is hostile" - one ~400-char message made the bot emit
attacker HTML; rendering it stole the support agent's session cookies; opened
Lenovo's support back-end. Prompt injection + unsanitised output.

SPEAKER NOTES (v4 - warmed into Matt's voice):

So now we've got those mental models a bit clearer, and we've seen the first of
the three. ForcedLeak there was about hostile input getting in. These next two
are about the other two faces of an agent, what it does, and what it sends back
out, and the patterns really start to jump out.

[CLICK]

So, Meta and Instagram, and the label here is the action is unauthorized. Where
the Salesforce one was a researcher's proof of concept, this one actually
happened, out in the wild, real victims, and a very big name attached to it. It
came to light through 404 Media, and Meta confirmed it in their own breach
notice.

The system was Meta's AI assistant for Instagram account support, the one that
helps people who've locked themselves out get back in. And honestly, a sensible
thing to automate, account recovery is high volume and a real pain to staff.

And the attackers just talked to it. They used a VPN to look like they were in
the right part of the world, then asked the assistant to add a new email address
onto somebody else's account. And it did, off it went and sent the reset links to
the attacker's address, without ever checking that address had anything to do
with the real owner.

That's a full account takeover, and not one or two of them. Meta's own notice
puts it at over twenty thousand accounts, including the old dormant White House
handle, which got defaced, and a senior US Space Force officer.

Now here's the bit I find really instructive. The press called this prompt
injection. Meta called it a bug in a separate bit of code that failed to verify
the email. And the honest answer is, they're both right. Take the AI out of it
altogether, and what you're left with is a privileged action, changing the
recovery email on an account, happening on the say-so of someone who was never
verified. We've known how to defend that for decades. The AI didn't invent a new
kind of vulnerability here, it just bolted a friendly, automated front door onto
a privileged action, and nobody checked who was knocking.

So, a new-feeling attack, but the control that was missing is one you already run
everywhere else. An agent that can go and do something needs the same
authorisation checks as anyone else who could do that something.

[CLICK]

And the last one in this little section, Lenovo's Lena, where the label is the
output is hostile, and this one shows how your own AI gets turned against your own
staff. This came from researchers at Cybernews, and to be fair to Lenovo, it was
disclosed properly and fixed before it went public, so nobody actually got hit,
but it was live and it worked.

Lena is Lenovo's customer support chatbot on their website. Again, a completely
normal thing to have running.

And the whole attack was a single message, a few hundred characters. It reads
like an ordinary product question, but tucked inside it tells the bot to reply in
HTML, and slips in an image tag pointing at a web address that doesn't exist.

And this is the clever bit. The attacker never writes a line of malicious code
themselves, they get the trusted chatbot to write it, in its own reply. So now
the dangerous content is coming from Lenovo's own system, and it walks straight
past all the checks that would've caught an outsider typing it in.

Then when that image fails to load, the browser quietly ships the user's session
cookie off to the attacker. And because the message just sits there in the chat
history, when a human support agent opens the conversation later, it runs on
their machine too, and steals their session, and that's what gets the attacker
into Lenovo's support systems, and all the customer conversations sitting behind
them.

So what do we take from it? The weakness itself is genuinely new and AI-shaped, a
prompt injection, and a bot producing output it never should have. But the actual
break-in is cross-site scripting and cookie theft, and we've understood those for
twenty years. And so are the defences, sanitise what the bot puts out, lock down
what the browser's allowed to run, and treat anything the AI produces as
untrusted, because as we've just seen, it'll quite happily write an attacker's
payload for them, and your systems trust it purely because it came from the AI.

So there it is, the three faces, hostile input, unauthorised action, hostile
output. Three different breaches, three different missing controls, and notice not
one of those controls is new. But you'll have spotted that all three turn on the
model doing something it shouldn't, on being talked into it. And the obvious
question then is, well, can't we just train the model to resist that? Which is
exactly where we go next.

---

## DISPLAY 8 - How about lab conditions? (Gray Swan ASR)

ON SLIDE: (chart) ref arxiv.org/pdf/2603.15714

SPEAKER NOTES (existing - AI-assisted register, callback opener edited; flagged
to rewrite in Matt's own voice):

So - remember right at the start, with the Salesforce one, I said the
instructions and the data come down the same channel and the model can't reliably
tell them apart. That's the attack surface we keep coming back to. The immediate
pushback to that - and your engineers will make it - is "fair, but the models are
trained to resist injection, and they're getting better at it, so isn't that
enough?" This slide exists to answer that one question: how much is the model's
own resistance actually worth? Because if you can lean on it, half of what I'll
recommend later is wasted effort. So let's put a number on it.

The number comes from a competition run by Gray Swan with the US AI Safety
Institute at NIST and the UK's AI Safety Institute - government-backed, not a
vendor marking its own homework. Thirteen frontier models, opened to the public,
464 people attacking them: about 272,000 attempts. Each bar is the Attack Success
Rate for one model - the share of attacks that landed, that got the model to do
what the attacker wanted instead of what it was meant to do. Lower is better.

There's a real spread - the most robust, Claude Opus, at about half a percent;
the most vulnerable, a top-tier Gemini, up around eight and a half. So models
genuinely differ.

The ranking follows capability within Claude's own range - Opus more robust than
Sonnet, Sonnet more than Haiku - and that makes sense: the resistance is trained
in, and the flagship inherits the most of it. But don't read it as "buy the
cleverest model and you're safe." It only holds inside one vendor's family.
Across vendors it breaks - that top-tier Gemini was the most capable model in the
field and the most attackable, more exposed than the smallest Claude. Robustness
comes from how hard the maker trained the model to resist, not from how clever it
is.

But here's the answer to our question: there is no bar at zero. All thirteen were
successfully attacked - and there never will be a zero, because a model resists
injection the way a trained person resists being fooled: pattern-recognition, not
a firewall. Good, but never certain.

And Opus's half a percent sounds reassuring until you remember it's per attempt.
Attackers don't go once; they go over and over, and the successes just accumulate
- they never level off. Half a percent per attempt becomes a near-certainty given
enough goes. We come back to that shortly.

So, back to the question we opened with - can you rely on the model's own
resistance? You can pick a more robust one, and you should. But you cannot rely
on it, because every model on the board can be turned, and the surface stays open
whichever you choose. Which is why the answer isn't "pick a better model" - it's
"stop relying on the model to defend itself."

---

## DISPLAY 9 - The supply chain into your agent

ON SLIDE: A new, unvetted channel feeding code straight to your agents. ~1 in 8
malicious - 341 of 2,857 skills on one marketplace were outright malicious (real
infostealer campaign: browser creds, SSH keys, crypto wallets) - Koi Security,
Feb 2026. Code Execution: a "skill" is code the agent runs with its own
permissions. Zero Review: OX Security submitted a malicious package to 11
AI-tool registries; 9 published it with zero review. A supply chain you didn't
build, can't see, and nobody's vetting.

SPEAKER NOTES (existing):

So far, the attacks we've looked at all work the same way - by manipulating the
AI. A clever prompt, a poisoned input; and on the last slide, just how little the
model itself resists that. Now I want to turn it around, because there's a
simpler attack that needs no cleverness at all. Why bother tricking the model
into misbehaving, when you can just hand it the malicious code and let it run
that for you?

And that's possible because of something that's grown up around agents very fast
- marketplaces of "skills" you install to give an agent new abilities, and
registries of MCP servers you plug in. It's a whole new software supply chain,
with almost none of the security maturity something like an app store built up
over fifteen years.

Researchers at Koi Security - big thanks to them - audited one of these skill
marketplaces. Of the roughly two thousand eight hundred skills on it, three
hundred and forty-one were outright malicious - about one in eight. And these
weren't theoretical; they were shipping a real credential stealer, going after
browser logins, SSH keys, crypto wallets.

Now, the reason this is worse than a dodgy app store is what a skill actually is.
It isn't something the agent just reads - it's instructions and scripts the agent
runs, on your machine, with your agent's permissions. So a malicious skill isn't
a vulnerability someone has to find and exploit; it's just code, and your agent
runs it the moment it's used.

And you can't lean on the marketplace to catch it. A separate team, OX Security,
took a deliberately malicious package and submitted it to eleven of these
registries to see who'd stop them - nine of the eleven published it, with no
review at all.

So the point of this one's fairly simple. It's got nothing to do with whether
your model is clever or gullible. You've wired your agents to a supply chain you
didn't build and nobody's checking - and you almost certainly couldn't list
what's plugged in. That list, and treating all of it as untrusted, is where
defending an agent has to start.

NB: notes above are present in the deck. (You had marked 9 onward as draft - this
one already has prose; treat as existing, polish in your voice.)

---

## DISPLAY 10 - Your infrastructure is already on the internet

ON SLIDE: ~300,000 internet-facing Ollama servers ("Bleeding Llama" dumps memory
in 3 unauthenticated calls, CVE-2026-7482, Cyera May 2026). 175,000 exposed
Ollama hosts across 130 countries (SentinelLABS/Censys). vLLM pre-auth RCE
CVSS 9.8 (CVE-2026-22778). ~2,000 production MCP servers, none authenticated at
deployment (NSA, May 2026). Common thread: every exposure began with a deployment
that was never inventoried. The asset existed; the owner did not.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 11 - Agents act, and you cannot stop them

ON SLIDE: ClawWorm (arXiv:2603.15727) - self-propagating agent attack, 40,000
instances, 64.5% aggregate ASR. Agents of Chaos live exercise 2026 - 10 of 11
scenarios produced critical failures; SSN leaked on a "forward" vs "share"
wording change; an agent destroyed its own mail server; display-name spoofing
handed over admin creds; no working kill switch in any scenario. Containment gap:
65% had an agent incident in last 12 months; 82% found agents they didn't know
about (CSA 2026); 109:1 machine vs human identities. 60% cannot terminate a
misbehaving agent today (Kiteworks).

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 12 - The attacker moves second

ON SLIDE: Defences that test at ~1% fail at >90% under a real attacker. Twelve
published defences evaluated against adaptive attacks (arXiv:2510.09023;
contributors from OpenAI, Anthropic, Google DeepMind). Spotlighting ~1% ->
>95%. MetaSecAlign 2% -> 96%. Circuit Breakers low -> 100%. Even frontier models
yield ~50% injection success within 10 attempts under adaptive conditions
(International AI Safety Report 2026). Static benchmarks are not a security
posture. Defend with architecture.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 13 - The discipline is being written now

ON SLIDE: "If you cannot understand, monitor or contain an agent's actions, it is
not ready for deployment." - Five Eyes / UK NCSC, May 2026. Five Eyes (careful
adoption of agentic AI, six governments). CoSAI (agentic identity framework + ADR
spec, RSAC 2026). OWASP (Agentic Top 10 + risk-tiering, Infosec Europe Jun 2026).
ISO/IEC 27090 (AI security threats, final draft). All four converged within
twelve months.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 14 - Tooling: discover what you have, then defend it

ON SLIDE: Step zero - you cannot defend an inventory you do not have. Discover
continuously: deployed models and inference endpoints; MCP servers and tool
registries; agent identities and service accounts; AI-adjacent services and data
flows (feeds your AI-BOM). Defend in depth: AI gateway with egress control (cuts
ForcedLeak channel); layered injection defence (PromptArmor; data-channel output
filtering); agent sandboxing as OS primitive (Microsoft Execution Containers);
log everything.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 15 - Identity: agents are first-class identities

ON SLIDE: Make every agent stoppable by design. With machine/AI identities 109:1,
shared service accounts are no longer acceptable. (1) A named human owner - no
owner, no agent in production. (2) Its own credential - per-agent, enabling
attribution/revocation/audit (Entra Agent ID). (3) Task-scoped, just-in-time
access - blast radius bounded by design. (4) A rehearsed kill switch - a control
plane, tested quarterly (CoSAI blueprint). 60% cannot terminate a misbehaving
agent today.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 16 - Process: red-team as launch criteria

ON SLIDE: Static ASR numbers from vendors are not a security posture. If you did
not attack it, you have not tested it. (1) Red-team your own models - prompt
injection against deployed systems; Garak, PyRIT, AgentDojo; a launch gate not an
annual tick. (2) Scan your MCP attack surface - tool poisoning, excessive scope,
missing auth. Red-teaming now runs at agent speed (681 assessments in ~3 hours,
Dreadnode 2026). AI-aware IR playbooks; kill-switch tabletops quarterly.

NOTE: on-slide text says "as Slide 10 demonstrated" - that ref now points at the
infra slide, not the ASR slides (DISPLAY 8 / 12). Fix to reference by name.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 17 - Governance: anchor, owner, measure

ON SLIDE: Controls without governance have no durability. Anchor: ISO/IEC 42001
today; ISO/IEC 27090 at final draft; EU AI Act transparency Aug 2026, high-risk
Dec 2027; Annex IV maps to an AI-BOM. Owner: a named human against every
inventory entry - no owner, no production. Measure: report upwards - ASR per
category, blast radius per agent, shadow-AI exposure (employee AI use tripled to
45%, DBIR 2026). Translate metrics into pounds and owners.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 18 - On the other hand: the defences are arriving

ON SLIDE: The honest steel-man for optimism. Layered defence works - reaches 1%
ASR under adaptive attack (Anthropic). Containment is a product - sandboxing as
OS primitive (Microsoft Execution Containers); kill switches engineered not
improvised. The discipline consolidated - Five Eyes, CoSAI, OWASP, ISO converged
within twelve months. Security is the #1 blocker to scaling AI, so fixing it
unlocks the roadmap - you are the enabler, not the brake.

NOTE: "discipline consolidated" bullet duplicates DISPLAY 13 - decide whether to
cut it here and keep 18 purely about defences/products working.

SPEAKER NOTES: [TO WRITE]

---

## DISPLAY 19 - Questions / Series Close

ON SLIDE: The two-part series. Part 1: The New SDLC - securing the AI that writes
your code. Part 2: Running AI in Production - what you are actually defending now.
Monday-morning checklist: discover your AI estate; make every agent a named,
scoped, killable identity; red-team your own models and MCP surface continuously;
translate it for the board in dollars and owners. Full bibliography on request.

SPEAKER NOTES: [TO WRITE]
