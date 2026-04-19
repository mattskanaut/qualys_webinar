# ROCon EMEA 2026 - Demo Script Outline
## "Operationalizing Cloud-Native Risk with TruRisk and Agentic AI"

**Duration:** 12-15 minutes (5 parts, ~2.5-3 minutes each)
**Format:** Speaker talks over pre-recorded video, pausing at key moments
**Presenter:** Matthew Campbell

---

## OPENING (30 seconds)

"You already know and love ETM. You're using VMDR, you understand TruRisk, you
know what it means to prioritize based on real exploitability rather than raw
CVSS scores.

But your environments aren't standing still. You're running multi-cloud. You've
got containers in production. Your developers are deploying AI workloads. And
the question is: how do we bring that same TruRisk-driven, risk-prioritized
approach to cloud-native workloads?

That's what I'm going to show you in the next 12 minutes. We're going to walk
through the full journey -- from discovery, through risk assessment, to
agentic remediation -- all within TotalCloud."

---

## PART 1: Agent Vikram - Agentic Discovery & Onboarding (~2 minutes)

**[VIDEO: Agent Vikram onboarding workflow]**

**Key talking points (before/during video):**

"Let's start with a problem every one of you has: unscanned assets. Blind
spots. Cloud accounts that got spun up by a dev team and never onboarded to
your security programme.

Agent Vikram is our dedicated cloud security AI agent. Rather than relying on
manual processes to find and onboard cloud assets, Vikram works autonomously.
It continuously monitors your multi-cloud environment for exposure gaps."

**[PAUSE video at statistics screen]**

"Look at what Vikram has found here. 21 assets with SSM that can be enabled
for API-based scanning immediately. 33 unscanned assets that need connector
onboarding. 30 shut-down instances where we can use snapshot-based scanning --
no need to power them on. And 8 cloud accounts that haven't been connected at
all -- potential blind spots in your security programme.

This is the kind of guidance that used to require a consultant or an SE visit.
Now it's happening autonomously, continuously, inside the platform."

**[RESUME video - show one-click remediation actions]**

"And critically, Vikram doesn't just tell you what's wrong -- it gives you
the actions. Deploy a connector, enable snapshot scanning, activate API-based
scanning -- all within a few clicks. Or, if you choose, Vikram can operate
fully autonomously and handle these actions for you."

**Transition:** "Once we've got full visibility, let's look at what we can see."

---

## PART 2: Multi-Cloud Inventory, Posture & DSPM (~3 minutes)

**[VIDEO: Multi-cloud inventory dashboard]**

### 2A: Multi-Cloud Inventory (~1 minute)

**Key talking points:**

"This is the TotalCloud dashboard -- your single landing page for cloud
workloads across AWS, Azure, and GCP.

What I want you to notice here is the breadth of discovery. It's not just
compute instances and storage buckets. We're surfacing identities, data
resources, network configurations, and -- this is new -- application and AI
services. See AWS Bedrock there? That's being identified for scanning with
TotalAI and TotalAppSec.

Every resource type gets a TruRisk score. That S3 bucket? It's not just
'exists' -- it has a risk score based on its configuration, exposure, data
sensitivity, and whether it sits on an exploitable attack path."

**[PAUSE at resource detail view showing Azure VMs]**

"When we drill into compute, we can see across all subscriptions which
instances have public IPs, which have critical misconfigurations, which have
unpatched vulnerabilities. This is multi-cloud inventory with risk context --
not just an asset list."

### 2B: Cloud Posture & DSPM (~2 minutes)

**[VIDEO: Posture dashboard and DSPM workflow]**

"Now let's look at posture. This is a unified multi-cloud posture view --
misconfigurations across network, compute, IAM, and data services, all in
one place.

But here's what's new and what I'm really excited about."

**[PAUSE at DSPM data issues filter]**

"See this filter for data issues? This is DSPM -- Data Security Posture
Management -- built directly into TotalCloud. We've always been able to tell
you if an S3 bucket or Azure Blob Storage is exposed to the internet. That's
a misconfiguration.

But the question security teams really need answered is: does it MATTER?
Is there actually sensitive data in that bucket?

That's what DSPM does. We're now classifying the data inside your storage
accounts, databases, and even container images. PII, PHI, PCI data, secrets,
API keys -- over 100 detection categories. And critically, we don't extract
your secrets. We identify the metadata and show you the location."

**[RESUME video - show sensitive data detail]**

"When I click into this storage account, we can see it contains PHI data.
That makes it a crown jewel asset. And now that classification feeds directly
into our attack path analysis -- so when we prioritize risks, we know which
ones are exposing your most sensitive data.

We also link these findings to compliance frameworks -- PCI DSS, HIPAA, GDPR
-- so your compliance reporting is driven by actual data classification, not
assumptions."

**Transition:** "Now let's see how this extends to containers."

---

## PART 3: Container Security & AI Workload Protection (~3 minutes)

**[VIDEO: Container security workflow]**

### 3A: Agentless Container Discovery & QLP (~1.5 minutes)

"When we onboard cloud connectors, we automatically discover your Kubernetes
clusters -- AKS, EKS, GKE. And here's where things get interesting.

With one click, we deploy agentless cluster scanning. We put components into
your service account and our cluster collector talks to the Kubernetes API to
pull your inventory. For serverless containers -- Fargate, ACI -- we hook
into EventBridge to detect new tasks as they spin up.

No agent deployment required to get started. You get TruRisk scoring on
vulnerabilities and compliance immediately."

**[PAUSE at container inventory / Group By view]**

"Now, one of the big challenges with containers at scale is just keeping
track of what you've got. When you have hundreds or thousands of container
instances, listing them individually becomes unmanageable.

This is where QLP comes in -- Qualys Locator Path. QLP gives every container
a hierarchical identity based on where it lives: account, cluster, namespace,
pod, container. Think of it as a logical address for every running container.

So instead of scrolling through thousands of flat entries, you can group by
QLP and instantly drill down -- show me everything in this cluster, in this
namespace, in this pod. Containers that originate from the same image get
grouped together. It turns container chaos into a navigable hierarchy, and
it's the foundation for how we apply TruRisk scoring at every level of that
hierarchy."

### 3B: Runtime Context & AI Workload Detection (~1 minute)

**[RESUME video at namespace/pod view with TruRisk scores]**

"You CAN deploy runtime sensors for additional threat visibility and
exploit confirmation via eBPF. But the key message is: you don't HAVE to.
The agentless scanning gives you immediate value. Runtime adds depth.

What I want to highlight here is the TruRisk scoring at every level of
the QLP hierarchy -- cluster, namespace, pod. When new namespaces or pods
spin up, they get scored automatically. This is how you handle ephemeral
workloads -- you can't rely on periodic scanning when containers live for
minutes.

And notice -- we're marking which containers are running AI workloads.
We're identifying AI software in your container images, MCP servers running
inside containers, and flagging these for additional scrutiny."

### 3C: The Differentiation -- Runtime + Exposure Context (~1 minute)

**[VIDEO: Image layer detail with code findings]**

"This is where we differentiate from open-source tools like Trivy. Yes,
Trivy can scan an image. But it doesn't have the runtime and exposure context.

Here we can see the actual image layers. There's a LangChain dependency
that was introduced as an application layer vulnerability. We can see the
git commit that introduced it -- we're showing the actual git diff.

But more than that -- we know this image is actually deployed in a running
container, connected to the internet, sitting on an exploitable attack path,
and running an MCP server. THAT is what drives prioritization when you have
millions of containers. What's actually running, actually exposed, and
actually risky?"

**[RESUME video - show eBPF threat detections]**

"And on the detection side -- we're correlating eBPF runtime events, MCP
server interactions, flow log detections, and CloudTrail anomalies. This
gives you end-to-end visibility across your entire containerized and AI
attack surface."

**Transition:** "So we've discovered everything, we've assessed the risk.
Now -- how do we act on it?"

---

## PART 4: Attack Path & Agentic AI Orchestration (~2.5 minutes)

**[SLIDE/VIDEO: Attack path visualization]**

### 4A: Attack Path & Agent Nexa - Risk Prioritization (~1 minute)

"Attack path analysis shows you not just individual findings, but how risks
chain together. An exposed VM with a critical vulnerability, connected to an
IAM role with excessive permissions, which has access to a database containing
PHI data -- that's a story, not just three separate findings.

Agent Nexa takes this further. Nexa prioritizes the most exploitable risks
and attack paths based on runtime behaviour and exposure context. It
explains the attack path to you in plain language -- here's what an attacker
could do, here's why this matters, here's what to look at first."

### 4B: Agent Steve - Remediation Playbooks (~1 minute)

**[VIDEO: Agentic AI orchestration - Nexa to Steve handoff]**

"And now we hand off to Agent Steve. Steve is our new remediation agent.
Once Nexa has identified and prioritized the risk, Steve builds you a
remediation playbook.

Steve already knows the context from the attack path. It will suggest
out-of-the-box remediation options -- tighten the security group, enforce
MFA, patch the vulnerability, restrict the IAM role.

But here's the powerful bit -- you might not want our default recommendation.
Maybe you don't want to terminate that VM. Maybe you want to migrate it to
a hardened network segment. Maybe your organisation has specific landing zone
policies we're not aware of.

So you can provide your own prompts. Tell Steve what your remediation
strategy is, and it will build an LLM-powered playbook tailored to your
organisation's practices."

### 4C: Agent Luther - Operationalising Remediation (~1 minute)

**[VIDEO/SLIDE: Agent Luther workflows - SNOW, PR, QFlow]**

"So Steve has built the playbook. Now how does that actually get executed?
This is where Agent Luther comes in.

Luther is the agent that turns remediation intent into action across your
operational toolchain. Three key capabilities:

First -- **ServiceNow integration.** Luther can automatically create SNOW
tickets from prioritized findings. The ticket arrives with full context:
the attack path, the affected resources, the recommended remediation, the
TruRisk score. Your ops team isn't starting from scratch.

Second -- **Auto-merge PRs.** Luther leverages QScanner as an MCP Server
to work directly with GitHub, GitLab, or your SCM of choice. It can
generate a fix, open a pull request, and -- if your policy allows -- auto-
merge it. Code-level remediation without the developer needing to context-
switch into a security console.

Third -- **QFlow with LLM prompts.** For more complex or custom
remediations, Luther connects to QFlow where you can type a natural
language prompt describing what you need. The LLM builds the workflow,
you review and approve it, and it executes. This is where your
organisation's specific policies and practices get built in."

### 4D: Agent Val - Exploit Confirmation (brief mention) (~30 seconds)

"And closing the loop -- Agent Val, our exploit validation agent. Val uses
TruConfirm to safely prove whether a vulnerability is actually exploitable
in YOUR environment. Not theoretically exploitable. Actually exploitable,
right now, against your specific configuration.

So the full cycle is: discover, assess, validate, remediate via Luther,
and then Val revalidates to confirm the exposure is actually closed."

**Transition:** "Finally, let's bring the developers into the picture."

---

## PART 5: QScanner & Developer Workflows (~1.5 minutes)

**[VIDEO/SLIDE: QScanner as MCP Server in developer IDE]**

"Everything I've shown you so far has been from the security team's
perspective -- the agents, the dashboards, the prioritisation. But
remediation ultimately happens in code. It happens in pull requests, in
CI/CD pipelines, on developer workstations.

QScanner is our CLI tool that developers can integrate directly into their
workflows. It scans container images, performs SCA analysis, generates
SBOMs, and enforces policies -- all before code reaches production.

But here's what's new and what ties back to what Luther is doing:
QScanner as an MCP Server. This means developers can interact with Qualys
security data directly from their IDE -- VS Code, GitHub, GitLab. They
can check if their image has vulnerabilities, get remediation guidance,
and see exactly what Luther has flagged for them.

When Luther opens that auto-merge PR, the developer sees the full context
-- which vulnerability, which image layer, which dependency introduced it,
and the suggested fix. No security console required. No context switching.

This is the code-to-cloud-to-runtime remediation loop: QScanner catches
it in the pipeline, Luther operationalises the fix, Val confirms the
exposure is closed. End to end."

---

## CLOSING (30 seconds)

"So let me bring this together. What you've just seen is the full journey:

1. **Agent Vikram** discovers and onboards your cloud assets autonomously
2. **TotalCloud** gives you unified multi-cloud inventory with TruRisk scoring
3. **DSPM** classifies your sensitive data so you know what actually matters
4. **Container Security** provides full lifecycle coverage with runtime context
5. **Agentic AI** -- Nexa, Steve, Luther, Val -- prioritizes, remediates,
   operationalises, and validates
6. **QScanner** brings it all to developers where they work

This is TruRisk for cloud-native. This is the Risk Operations Centre
extended to your entire cloud and container estate.

Come find me after the session -- I'd love to show you any of this in more
detail and talk about how it applies to your environment. Thank you."

---

## TIMING NOTES

| Part | Content | Target Time |
|------|---------|-------------|
| Opening | ETM context, session setup | 0:30 |
| Part 1 | Agent Vikram - Discovery | 2:00 |
| Part 2 | Inventory, Posture, DSPM | 3:00 |
| Part 3 | Container Security & AI | 3:00 |
| Part 4 | Attack Path, Agentic AI & Luther | 3:30 |
| Part 5 | QScanner & Dev Workflows | 1:30 |
| Closing | Summary & CTA | 0:30 |
| **Total** | | **~14:00** |

## VIDEO REQUIREMENTS

- **Video 1:** Agent Vikram onboarding flow (statistics, recommendations, one-click actions)
- **Video 2:** Multi-cloud inventory dashboard -> posture -> DSPM data classification
- **Video 3:** Container cluster discovery -> agentless scanning -> image layers -> eBPF events
- **Video 4:** Attack path -> Nexa prioritization -> Steve remediation playbook -> Luther (SNOW ticket, auto-merge PR, QFlow prompt)
- **Video 5:** QScanner in IDE / MCP Server integration (may be slide-based if not ready)

## PAUSE POINTS

Key moments to pause the video and add commentary:
1. Agent Vikram statistics screen (unscanned asset breakdown)
2. Multi-cloud inventory showing TruRisk on S3 bucket
3. DSPM data issues filter (explain the classification approach)
4. Sensitive data detail on storage account
5. Container inventory Group By view (introduce QLP hierarchy)
6. Container namespace view with TruRisk scores at each QLP level
7. Image layer detail showing LangChain vulnerability + git diff
8. Attack path visualization (explain the chain)
9. Agent Steve remediation options (explain customisation)
10. Agent Luther workflows (SNOW ticket creation, auto-merge PR, QFlow prompt)

## KEY MESSAGES TO REINFORCE

- **"TruRisk for cloud-native"** -- the same risk-first approach you know from ETM, extended to cloud and containers
- **Runtime + exposure context** -- this is what differentiates from open-source tools
- **Agentic, not just automated** -- agents understand context, recommend actions, adapt to your policies
- **Developer-centric remediation** -- security data delivered where developers work
- **Reduced TCO** -- full-stack discovery, event-driven scanning, agentless options
- **Crown jewel protection** -- DSPM ensures you prioritize risks to your most sensitive data
