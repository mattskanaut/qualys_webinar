# Part 2 - Webinar Structure at a Glance (summary, aligned to outline-v3)

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Shape:** 60-min slot - ~38 min content + 10 min Q&A + 5 min host preamble. 17 slides, ~2.6 min each.
**Arc:** Problem-first (same as Part 1) - hit the problem first, pivot, then spend the back half on what to do.

---

## The five sections

### OPEN (slides 1-3) - earn the room, set the stakes, land one vivid hook
1. Title and the promise - non-product compact; Part 1 was build-time, today is run-time
2. You already shipped it - 91% run agents in production, only 29% feel ready; security is the #1 blocker to scaling
3. The attacker filled in a web form - the ForcedLeak hook, walked end to end

### SECTION 2 - THE RUNTIME RISK PILE (slides 4-9) - the problem, walked layer by layer
4. What you actually deployed - the six-layer anatomy (the map for everything after)
5. Real incidents in real deployments - Meta/Instagram + Lenovo Lena
6. How about lab conditions? - Gray Swan: every model fell, capability != robustness
7. The supply chain into your agent - ClawHub: ~1 in 8 marketplace skills malicious; registries don't vet
8. Your infrastructure is already on the internet - Bleeding Llama, exposed Ollama, NSA on MCP
9. Agents act, and you cannot stop them - ClawWorm + the containment gap

### SECTION 1 - THE REFRAME AND THE DISCIPLINE (slides 10-11) - the pivot
10. The attacker moves second - defences collapse under adaptive attack; the model cannot be your boundary
11. The discipline is being written now - Five Eyes, CoSAI, OWASP, ISO have converged

### SECTION 3 - WHAT TO DO (slides 12-15) - the response, the centre of gravity
12. Tooling - discover what you have, then defend it
13. Identity - agents are first-class identities
14. Process - red-team as launch criteria
15. Governance - anchor, owner, measure

### CLOSE (slides 16-17)
16. On the other hand - the steel-man: defences are arriving; the CISO is the enabler, not the brake
17. Q&A and series close

---

## Section breakdown

| Block | Slides |
|---|---|
| Open | 1 - 3 |
| Section 2 - The runtime risk pile (the problem) | 4 - 9 |
| Section 1 - The reframe and the discipline | 10 - 11 |
| Section 3 - What to do (the response) | 12 - 15 |
| Close | 16 - 17 |
| **Total** | **17 slides** |

---

## The narrative spine

You have already shipped it (Open) -> here is everything that is breaking, from real incidents down to the infrastructure (S2) -> so stop trusting the model to defend itself; defend with architecture, and you are not alone (S1 pivot) -> here is the architecture: tooling, identity, process, governance (S3) -> and the good news is it is arriving fast, which makes you the enabler (Close).

---

## Note on the section labels

The section numbers are non-sequential on purpose: Open -> **S2** -> **S1** -> **S3** -> Close. That ordering is inherited from Part 1, where "Section 1" was always *the discipline* and "Section 2" was *the problem*, and the problem-first restructure presents S2 before S1. It is correct, but the S1/S2/S3 tags are vestigial from Part 1 and can read oddly on their own. Open question: relabel to plain sequential names (e.g. "Part A - The Problem", "Part B - The Reframe", "Part C - What To Do")?
