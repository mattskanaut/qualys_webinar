# ROCon EMEA 2026 - Demo Script
## "Operationalising Cloud-Native Risk with TruRisk and Agentic AI"

**Duration:** 12-15 minutes (5 parts, ~2.5-3 minutes each)
**Format:** Speaker talks over pre-recorded video, pausing at key moments
**Presenter:** Matthew Campbell

---

## OPENING (30 seconds)

So, many of you will already be using ETM, and certainly VMDR, and understand what TruRisk scoring brings to the table when it comes
to prioritising based on real exploitability rather than raw CVSS base scores.

But the world isn't standing still. You're running multi-cloud, you've
got containers in production, your dev teams are spinning up AI
workloads, and I think the question a lot of organisations are
asking right now is: how do we bring that same TruRisk-driven,
risk-prioritised approach into these cloud-native environments?

That's what I want to walk you through today, the full journey with cloud and container, from discovery through to risk assessment and 
to remediation, all within the Qualys platform, and all of is supported by our suite of autonomous AI agents.  Qualys moving from 
a vital tool to your key sec ops collaborator.

---

## PART 1: Agent Vikram - Agentic Discovery & Onboarding (~2 minutes)

**[VIDEO: Agent Vikram onboarding workflow]**

**Key talking points (before/during video):**

Let's start with a problem I know every one of you has, because
I see it in pretty much every customer engagement I do: unscanned
assets, blind spots, cloud accounts that were spun up by a dev team
somewhere and never properly onboarded into your security programme.

Agent Vikram is our dedicated cloud security AI agent, and this is
exactly the problem it solves. Rather than relying on those manual
processes to find and onboard cloud assets, Vikram works
autonomously, continuously monitoring your multi-cloud
environment for exposure gaps and closing them by configuring agentless scans or deploying assets to your cloud resources.

**[PAUSE video at statistics screen]**

So look at what Vikram has found here. 21 assets with SSM
available that can be enabled for API-based scanning straight away.
33 unscanned assets that need connector onboarding. 30 instances
that are shut down,and here's the thing, we can use snapshot-
based scanning on those, you don't need to power them on. And then
8 cloud accounts that haven't been connected at all,potential
blind spots in your programme you might not even know about.

This is happening autonomously, continuously, inside the platform.
No human intervention required.

**[RESUME video - show one-click remediation actions]**

And critically, Vikram doesn't just tell you what's wrong, it
gives you the actions. Deploy a connector, enable snapshot scanning,
activate API-based scanning, all within a few clicks. Or, if you're
comfortable with it, Vikram can operate fully autonomously and just
handle these onboarding actions for you. You have the choice --
manual, guided, or fully autonomous.

**Transition:** So, once we've got that full visibility, let's look
at what we can actually see.

---

## PART 2: Multi-Cloud Inventory, Posture & DSPM (~3 minutes)

**[VIDEO: Multi-cloud inventory dashboard]**

### 2A: Multi-Cloud Inventory (~1 minute)

**Key talking points:**

This is the new TotalCloud dashboard, your single multi-cloud landing page for
cloud workloads across AWS, Azure, GCP and OCI.

Now, what I want you to notice here is the breadth of what's being
discovered. It's not just compute instances and storage buckets.
We're surfacing identities, data resources, network configurations,
and,this is new,application and AI services. See AWS Bedrock
there? All these resources are being identified for differnent scan types, 
including being onboarded to TotalAI and TotalAppSec were appropriate, extending discovery right out to the AI
and application workloads your teams are deploying.

And we're massively expanding the resource types that get a TruRisk score. 
That S3 bucket doesn't just have posture evaluations, it has a risk score based on its actual
on that posture, its level of exposure, whether there's sensitive data in it,
and whether it sits on an exploitable attack path. This is the same
risk-centric approach you know from ETM, extended to your cloud
resources.

**[PAUSE at resource detail view showing Azure VMs]**

When we drill into compute, we can see across all subscriptions
which instances have public IPs, which ones have critical
misconfigurations, which have unpatched vulnerabilities. This is
multi-cloud inventory with risk context, not just an asset list,
but a prioritised view of what you as a security team need to focus on.

### 2B: Cloud Posture & DSPM (~2 minutes)

**[VIDEO: Posture dashboard and DSPM workflow]**

Now let's look at posture. Those of you who've studied any breach analysis 
know then importance of posture
management. In breach after breach, there's a misconfiguration 
somewhere in the attack chain. This is a unified multi-cloud posture view showing
misconfigurations across network, compute, IAM, and data services,
all in one place.

But here's what's new and what I'm personally really excited about.

**[PAUSE at DSPM data issues filter]**

See this filter for data issues? This is DSPM, our new Data Security
Posture Management tool, built directly into TotalCloud. Now, we've
always been able to tell you if an S3 bucket or an Azure Blob
Storage account is exposed to the internet. That's a
misconfiguration, and CSPM catches it.

But the question you really need answered is: how serious a problem 
is this? Is there sensitive data in that bucket? Because an exposed
bucket with log data in it is a very different risk proposition to
an exposed bucket full of PII or PCI data.

That's what DSPM does. We're now classifying the data inside your
storage accounts, databases, and container images. PII, 
customer health data, banking or payment information
data, secrets, API keys,over 100 detection categories. And I
should stress, we don't extract your secrets or take your data. We
identify the metadata and show you the location, so you know
exactly where to go to address it.

**[RESUME video - show sensitive data detail]**

When I click into this storage account, we can see it contains customer health
data. That immediately makes it a crown jewel asset. And now that
classification feeds directly into our attack path analysis,so
when we're prioritising risks, we know which ones are exposing your
most sensitive data. That's risk prioritisation driven by actual data
classification, not assumptions.

We also link these findings to compliance frameworks,PCI DSS,
HIPAA, GDPR, so your compliance reporting reflects the real
picture.

**Transition:** Now let's see how this extends to containers.

---

## PART 3: Container Security & AI Workload Protection (~3 minutes)

**[VIDEO: Container security workflow]**

### 3A: Agentless Container Discovery & QLP (~1.5 minutes)

When we onboard cloud connectors, we automatically discover your
Kubernetes clusters, AKS, EKS, GKE. And this is where things get
interesting.

With one click, we deploy agentless cluster scanning. We put
components into your service account and our cluster collector talks
to the Kubernetes API to pull your inventory, you don't need to expose
your Kubernetes API outside your cloud. For serverless
containers, Fargate, ACI, we hook into EventBridge to detect
new tasks as they spin up. No agent deployment required to get
started. You get TruRisk scoring on vulnerabilities and compliance
immediately.

**[PAUSE at container inventory / Group By view]**

Now, one of the really practical challenges with containers at
scale, and anyone who's managed a large container estate will
know this, is just keeping track of what you've got. When you
have hundreds or thousands of container instances, listing them
individually is unmanageable.

This is where QLP comes in, Qualys Locator Path. QLP gives every
container a stable, hierarchical identity based on where it lives in your
infrastructure: account, cluster, namespace, pod, container. A logical address
for your container workloads, not dependent on the underlying, ephemeral host.

So instead of scrolling through thousands of flat entries, you can
group by QLP and instantly drill down. Show me everything in this
cluster, in this namespace, in this pod. Containers originating from
the same image get grouped together. It turns your complex container 
estate into a navigable hierarchy, and because TruRisk is fully 
aggregatable, we can apply TruRisk scoring at every level of that
hierarchy.

### 3B: Runtime Context & AI Workload Detection (~1 minute)

**[RESUME video at namespace/pod view with TruRisk scores]**

Now, you can deploy runtime sensors for additional threat
visibility and exploit confirmation via eBPF, and I'd recommend you
do to get that rich threat data, but you don't have to
start there to get value. Agentless scanning gives you immediate risk visibility, runtime adds depth.

What I want to highlight here is the TruRisk scoring at every level
of the QLP hierarchy, cluster, namespace, pod. When new namespaces
or pods spin up, they get scored automatically. This is how you
handle ephemeral workloads, you can't rely on periodic scanning
when containers live for minutes, you need something that's
assessing risk continuously as things change.

Notice also, that we're marking which containers are running AI
workloads. We're identifying AI software in your container images,
MCP servers running inside containers, and flagging these for
additional scrutiny. This is new, and given the pace at which
organisations are deploying AI workloads, I think it's going to be
increasingly important."

### 3C: The Differentiation,Runtime + Exposure Context (~1 minute)

**[VIDEO: Image layer detail with code findings]**

Here we can see the actual image layers. There's a LangChain
dependency that was introduced as an application layer vulnerability.
We can see the git commit that introduced it,we're showing the
actual git diff. So we know exactly when and how it got in.

But more than that, we know this image is actually deployed in a
running container, connected to the internet, sitting on an
exploitable attack path, and running an MCP server. That is what
drives prioritisation when you have thousands of containers. Not
what could theoretically be exploited based on image scans, 
but what's actually running, actually exposed, and actually 
measurably increasing the risk in your environment."

**[RESUME video - show eBPF threat detections]**

"And on the detection side, we're correlating eBPF runtime events,
MCP server interactions, flow log detections, and CloudTrail
anomalies. This gives you end-to-end visibility across your entire
containerised and AI attack surface. 

**Transition:** "So we've discovered everything, we've assessed the
risk. Now the question is, how do we actually act on it? Analysis
without remediation isn't putting you in a better place risk wise.

---

## PART 4: Attack Path & Agentic AI Orchestration (~2.5 minutes)

**[SLIDE/VIDEO: Attack path visualization]**

### 4A: Attack Path & Agent Nexa - Risk Prioritisation (~1 minute)

"Attack path analysis shows you not just individual findings, but
how risks chain together. And I think this is crucial, because if
there's one thing we've learnt from studying breaches,and those
of you who've attended our webinars know how important I think
breach analysis is,it's that breaches are almost never a single
failure. They're cascades. An exposed VM with a critical
vulnerability, connected to an IAM role with excessive permissions,
which has access to a database containing PHI data. That's a story,
not just three separate findings.

Agent Nexa takes this further. Nexa prioritises the most
exploitable risks and attack paths based on runtime behaviour and
exposure context. It explains the attack path to you in plain
language,here's what an attacker could do, here's why this
matters, here's what to look at first."

### 4B: Agent Steve - Remediation Playbooks (~1 minute)

**[VIDEO: Agentic AI orchestration - Nexa to Steve handoff]**

"And now we hand off to Agent Steve. Steve is our remediation agent,
and once Nexa has identified and prioritised the risk, Steve builds
you a remediation playbook.

Steve already knows the context from the attack path. It will
suggest out-of-the-box remediation options,tighten the security
group, enforce MFA, patch the vulnerability, restrict the IAM role.

But here's where it gets really interesting,you might not want
our default recommendation. Maybe you don't want to terminate that
VM. Maybe you want to migrate it to a hardened network segment.
Maybe your organisation has specific landing zone policies or
network segmentation practices that we're not aware of.

So you can provide your own prompts. Tell Steve what your
remediation strategy looks like, and it will build an LLM-powered
playbook tailored to how your organisation actually operates. I
think this is really powerful, because it means the agentic
workflows adapt to you, not the other way around."

### 4D: Agent Val - Exploit Confirmation (brief mention) (~30 seconds)

"And then closing the loop,Agent Val, our exploit validation
agent. Val uses TruConfirm to safely prove whether a vulnerability
is actually exploitable in your environment. Not theoretically
exploitable. Actually exploitable, right now, against your specific
configuration.

So the full cycle is: discover, assess, prioritise, remediate,
and then Val goes back and revalidates to confirm the exposure is
actually closed. That closed-loop verification is something I think
is going to be really important as we move to more autonomous
security operations."

**Transition:** "Finally, let's bring the developers into the
picture."

---

## PART 5: QScanner & Developer Workflows (~1.5 minutes)

**[VIDEO/SLIDE: QScanner as MCP Server in developer IDE]**

"Everything I've shown you so far has been from the security team's
perspective,the agents, the dashboards, the prioritisation. But
at the end of the day, for your container workloads, remediation happens 
in code. It happens in
pull requests, in CI/CD pipelines, on developer workstations. 

QScanner is our CLI tool that developers can integrate directly
into their workflows. It scans container images, does SCA analysis,
generates SBOMs, enforces policies,all before code reaches
production. Those of you interested in shift-left security, this is
where it starts.

But here's what takes this further: QScanner as an MCP Server.
This means developers can interact with Qualys security data
directly from their IDE, VS Code, GitHub, GitLab. They can check
if their image has vulnerabilities, get remediation guidance, and
see exactly what's been flagged against the images they're building.

When a pull request comes in, the developer sees the full context,
which vulnerability, which image layer, which dependency introduced
it, and the suggested fix. No security console required. No context
switching. Security data landing right in their toolchain, which as
someone with a development background, I can tell you makes an
enormous difference to adoption.

This is the code-to-cloud-to-runtime remediation loop: QScanner
catches it in the pipeline, Steve provides the remediation guidance,
Val confirms the exposure is closed. End to end."

---

## CLOSING (30 seconds)

"So let me pull this together. What you've just seen is the full
journey:

1. **Agent Vikram** discovers and onboards your cloud assets
   autonomously,no more blind spots
2. **TotalCloud** gives you unified multi-cloud inventory with
   TruRisk scoring on every resource
3. **DSPM** classifies your sensitive data so you know what
   actually matters
4. **Container Security** with QLP provides full lifecycle
   coverage with the runtime and exposure context that drives
   real prioritisation
5. **Agentic AI**, Nexa, Steve, and Val, prioritises,
   remediates, and validates in a closed loop
6. **QScanner** brings it all to developers right where they work

This is TruRisk for cloud-native. The same risk-first approach
you know from ETM, extended to your entire cloud and container
estate.

I'd love to chat to anyone after the session about any of this in
more detail, and particularly about how it applies to your
specific environment. Thank you."

---

## TIMING NOTES

| Part | Content | Target Time |
|------|---------|-------------|
| Opening | ETM context, session setup | 0:30 |
| Part 1 | Agent Vikram - Discovery | 2:00 |
| Part 2 | Inventory, Posture, DSPM | 3:00 |
| Part 3 | Container Security & AI | 3:00 |
| Part 4 | Attack Path & Agentic AI | 2:30 |
| Part 5 | QScanner & Dev Workflows | 1:30 |
| Closing | Summary & CTA | 0:30 |
| **Total** | | **~13:00** |

## VIDEO REQUIREMENTS

- **Video 1:** Agent Vikram onboarding flow (statistics, recommendations, one-click actions)
- **Video 2:** Multi-cloud inventory dashboard -> posture -> DSPM data classification
- **Video 3:** Container cluster discovery -> agentless scanning -> QLP group by -> image layers -> eBPF events
- **Video 4:** Attack path -> Nexa prioritisation -> Steve remediation playbook -> Val exploit confirmation
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
8. Attack path visualisation (explain the cascade)
9. Agent Steve remediation options (explain customisation)

## KEY MESSAGES TO REINFORCE

- **"TruRisk for cloud-native"**,the same risk-first approach you know from ETM, extended to cloud and containers
- **Runtime + exposure context**,this is what differentiates from open-source tools; not just what could be exploited, but what's actually running, actually exposed, actually risky
- **Agentic, not just automated**,agents understand context, recommend actions, adapt to your organisation's policies
- **Developer-centric remediation**,security data delivered where developers work, not in a separate console
- **Reduced TCO**,full-stack discovery, event-driven scanning, agentless options
- **Crown jewel protection**,DSPM ensures you prioritise risks to your most sensitive data
- **Closed-loop verification**,discover, validate, remediate, revalidate
