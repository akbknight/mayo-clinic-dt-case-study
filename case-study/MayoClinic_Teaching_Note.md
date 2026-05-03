# Mayo Clinic Case Study: Teaching Note
## *For Instructor Use Only*
## ITEC-617 | Kogod School of Business, American University | Spring 2026

---

## Case Synopsis

In January 2020, Dr. John Halamka became the inaugural President of Mayo Clinic Platform, a new business unit charged with turning Mayo Clinic's patient data -- accumulated over 157 years -- into the foundation of a technology platform. Halamka had to make three interconnected strategic decisions: (1) how to structure data governance in a way that preserved patient trust while enabling commercial innovation; (2) which external partners to choose and on what terms; and (3) how to balance Mayo's nonprofit mission against the commercial logic of platform businesses.

By 2024, the Platform had grown to 56 million patient lives across 9 institutional partners on 4 continents, with 81 solution developers and major partnerships with both Google Cloud and Microsoft. But the core strategic tensions -- speed vs. safety, mission vs. revenue, openness vs. control -- remained unresolved and were growing larger with scale.

---

## Case Position in Curriculum

This case is designed for use in **ITEC-617** at the intersection of three course themes:

1. **AI and organizational strategy**: The platform model as a vehicle for AI-driven competitive advantage in a regulated, trust-sensitive industry.
2. **Data governance**: The technical and institutional mechanisms required to deploy sensitive data responsibly at scale.
3. **Technology and mission alignment**: Whether and when commercial technology strategy is compatible with nonprofit institutional purpose.

**Recommended placement**: After students have covered platform strategy basics (Parker, Van Alstyne, Choudary: *Platform Revolution*), AI governance fundamentals, and at least one case involving mission-driven organizations using commercial strategies (e.g., Kaiser Permanente, Cleveland Clinic, academic medical centers).

**Prerequisite reading**: The main case (MayoClinic_Case.md) and the Technical Supplement (MayoClinic_Supplement.md). Students who have not read both will miss the IBM Watson contrast and the data governance technical background necessary for the Section 2 discussion.

**Session length**: 80 minutes. The discussion guide below is calibrated for 80 minutes with one optional section (Section 2.5) that can be cut if time runs short.

---

## Learning Objectives

After discussing this case, students should be able to:

1. **Analyze platform business models** in non-commercial (nonprofit, healthcare) contexts, including the specific network effects, governance challenges, and legitimacy constraints that distinguish healthcare platforms from commercial platforms.

2. **Evaluate data governance frameworks** for sensitive data, including the tradeoffs between federated and centralized models, the role of community oversight boards, and the limitations of de-identification at scale.

3. **Apply AI governance frameworks** to evaluate when AI clinical deployment is premature, using the IBM Watson Health failure as a contrasting case.

4. **Assess the tension between institutional mission and commercial strategy** in organizations where trust is the primary competitive asset.

5. **Evaluate the organizational implications of generative AI deployment** at scale, using the Microsoft 365 Copilot deployment as a case within the case -- distinguishing administrative AI automation from clinical diagnostic AI.

---

## Instructor Preparation Notes

### What This Case Does Well

- Provides a genuine strategic dilemma with no obvious "right answer" -- the case does not resolve its tensions
- Uses a named protagonist with strong, quotable public positions that students can engage with directly
- Connects technical concepts (federated learning, de-identification) to strategic decisions, rewarding students who read the supplement
- Offers the IBM Watson contrast case organically within the narrative, without requiring a separate reading
- Works across disciplines: MBA students engage with platform strategy; technology management students engage with AI governance; public policy students engage with the nonprofit/commercial tension

### What This Case Does Not Cover

- Patient perspectives on data commercialization (deliberately absent -- this is a known bias to be named explicitly in class)
- Detailed financial modeling of the Platform business unit's revenue contribution (financial data is at the Mayo Clinic level, not Platform-level)
- Internal Mayo Clinic organizational dynamics, including resistance from clinical staff or internal governance conflicts
- The specific mechanics of any individual AI algorithm deployed on the platform

### Common Instructor Questions

**Q: Students ask what "data under glass" actually means technically. Should I explain this?**

Yes -- briefly. The key insight is that the algorithm moves, not the data. Draw on the board: two boxes labeled "Institution" and "Google Cloud." Draw an arrow going FROM Cloud TO Institution (algorithm enters the enclave). Draw an arrow going FROM Institution TO Cloud (trained model exits). Then draw a large X over any arrow showing patient data leaving the institution. That is the entire architecture in 30 seconds. The supplement's Part 3 provides the governance layering (DaTA Board, One Table, etc.) for students who want more depth.

**Q: Is the IBM Watson failure fair to include given how old it is?**

Yes. Watson for Oncology is the most thoroughly documented failure in health AI and is still routinely cited by practitioners and regulators. The MD Anderson $62M write-off (2017) and IBM's full Watson Health divestiture (2022) are both recent enough to be contextually relevant. The more important point: IBM was actively marketing Watson to hospital executives as recently as 2019 -- the same year Mayo began building its Platform architecture. Halamka's governance choices were made in direct awareness of the Watson experience.

**Q: A student claims Mayo is "just doing research." How do I respond?**

Ask the student to describe the revenue model. Mayo Clinic Platform collects licensing fees from solution developers, partner fees from institutional network members, and value-sharing arrangements from commercial partnerships (Google, Microsoft). This is a commercial platform operating under a mission overlay -- not a research operation. The distinction matters for thinking about long-term incentive structures: research operations optimize for knowledge production; platforms optimize for ecosystem growth and value capture.

**Q: Students disagree about whether 56 million patient lives is large or small. How do I frame this?**

Both. It is large relative to any single health system's data (Mayo's own patient population is approximately 1.3 million annually). It is small relative to Epic Systems (250M+ records), Google Health (billions of consumer health searches), or the U.S. population (330M). The relevant comparison is not size alone but *diversity* of clinical presentations, genetic backgrounds, and care settings. The distributed network (Brazil, Israel, Canada) is specifically designed to improve diversity, not just volume.

---

## Suggested Pre-Class Assignment Questions

Assign these before class. Students should bring written notes (not formal memos):

1. What is the core strategic logic of Mayo Clinic Platform? Who are its "two sides"?

2. What does "data under glass" mean, and why did Mayo choose this model over simpler alternatives such as licensing data to partners directly?

3. Halamka said change management is "always the hardest task." Give a specific example from the case where this claim is supported or challenged.

4. **(Optional -- for advanced sections)**: Read a brief account of the IBM Watson Health failure. What would Halamka need to demonstrate to convince you that Mayo Clinic Platform has avoided Watson's structural mistakes?

---

## Discussion Guide (80-minute session)

### Opening (8 minutes)

**Question to open:** "What is Mayo Clinic Platform selling -- and to whom?"

**Purpose:** Forces students to identify the two-sided market structure. Many will initially say "healthcare data" -- push back: Mayo is not selling data. It is selling access to a validated environment for algorithm development, and separately, selling validated AI tools to health systems. The distinction matters for both legal and strategic reasons.

**Expected range of responses:**
- "Data to technology companies" -- correct instinct, incorrect mechanism; Mayo never transfers data
- "Validated AI algorithms to health systems" -- closer, but misses the developer side
- "A platform that connects algorithm developers with clinical validation infrastructure" -- most precise

**Transition:** "OK, so if it is a platform -- let's map its sides and think about whether the network effects actually work the way Halamka claims."

---

### Section 1: Platform Logic (18 minutes)

**Focus:** Does the Mayo Clinic Platform business model exhibit genuine platform dynamics, or is it fundamentally a research services business that is being described in platform language?

**Key questions:**

1. "What are the same-side and cross-side network effects in this platform?"

   *Purpose*: Tests whether students can apply platform theory rigorously, not just use platform vocabulary.

   *Expected answer*: More patient data leads to better algorithms (same-side, data quality effect); more developers make the platform more attractive to institutional partners, and more institutional partners attract more developers (cross-side). Some students will struggle to articulate the cross-side effect clearly -- push them to name both sides explicitly.

2. "What is Mayo Clinic's competitive moat? Could Google or Microsoft replicate this platform?"

   *Purpose*: Gets at whether institutional brand and trust is a durable advantage or a temporary one.

   *Instructor note*: Google has more compute, more ML talent, and more consumer health data. But Google does not have 157 years of longitudinal inpatient records, Mayo's clinical credibility with physician partners, or the regulatory standing of a Tier 1 academic medical center. Students should identify specifically which dimensions favor Mayo and which favor Google -- not just assert that "Mayo has trust."

3. "Why did Halamka choose a federated network model instead of buying or licensing data from a central health data broker?"

   *Purpose*: Links the business model choice to governance constraints and patient trust as a strategic asset.

**Board plan:** Draw a two-sided market diagram with Mayo Clinic Platform as the intermediary. Left side: health AI solution developers. Right side: institutional data partners and health systems. Label: data enclave (center), network effects (bidirectional arrows), governance layer (surrounding box). Add: "IBM Watson" as a ghost on the left side -- a developer that accessed data without adequate governance, and was eventually expelled from the ecosystem.

---

### Section 2: The IBM Watson Contrast (15 minutes)

**Focus:** What does Watson Health's failure teach us about what Mayo is doing differently -- and whether those differences are sufficient?

**Key questions:**

1. "What structural factors caused Watson Health to fail? Which of those factors does Mayo Clinic Platform address? Which does it not?"

   *Purpose*: Forces students beyond "Mayo is better because it's Mayo" to identify specific mechanisms.

   *Expected answer*: Watson failed on validation scope (trained on one institution's data), explainability (physicians couldn't understand recommendations), overclaiming (marketed to executives rather than clinicians), and governance (no independent oversight of outcomes). Mayo's governance model directly addresses the last two. The first two -- generalizability and explainability -- are addressed by the distributed network and FDA clearance requirement, but neither is a guarantee. This is the analytically interesting gap.

2. "Halamka mentioned that Mayo deploys a colonoscopy algorithm that reduces error rates to 3%. What would you need to see before trusting that claim?"

   *Purpose*: Teaches clinical validation standards concretely.

   *Expected elements*: Peer-reviewed publication, prospective randomized trial, comparison to current standard of care baseline (not just the algorithm's own retrospective performance), independent validation at institutions other than Mayo, post-deployment performance monitoring.

3. "At 81 solution developers and 56 million patient lives, is Mayo still able to apply the same governance it applied when the platform had 4 startups and 1 institutional partner?"

   *Purpose*: Surfaces the governance scaling problem directly.

---

### Section 2.5: Generative AI and Administrative Automation (10 minutes, optional)

*Cut this section if time runs short. It is most valuable for sections with a technology management focus.*

**Focus:** The Microsoft 365 Copilot deployment (September 2023) represents a fundamentally different kind of AI deployment than the clinical algorithm work -- administrative rather than clinical, generative rather than predictive, enterprise-wide rather than controlled-enclave.

**Key questions:**

1. "Should administrative generative AI (Copilot for clinical documentation) be governed differently than clinical diagnostic AI? Why or why not?"

   *Expected student positions*: Administrative AI is lower-stakes (no direct patient harm if a note summary is imprecise) versus administrative AI at scale still affects care quality (a prior authorization error affects patient access to treatment).

2. "CIO Cris Ross said the Microsoft partnership is about improving 'operational efficiency' and 'staff wellbeing.' If staff are more efficient, what happens to headcount over time? Is this a benefit or a risk to the organization?"

   *Purpose*: Connects AI efficiency gains to workforce implications -- a recurring theme in ITEC-617.

3. "The Microsoft partnership is for administrative AI. The Google partnership is for clinical AI. Is it strategically coherent to have two major cloud AI partners with explicitly different scopes? What are the coordination and integration risks three years from now?"

---

### Section 3: Mission vs. Commercial Logic (20 minutes)

**Focus:** Can a nonprofit hospital be a technology platform? What gets sacrificed?

**Key questions:**

1. "Halamka's explicit goal was to make Mayo into a 'digital data business by 2025.' Is this language appropriate for a nonprofit? What does it signal to patients? What does it signal to physicians and nurses who chose Mayo because of its mission?"

2. "Mayo's 2023 operating income was $1.1 billion -- up 82% in a year. The Platform contributes to this through data licensing, developer fees, and partner relationships. At what point does data commercialization compromise the nonprofit mission?"

3. "Some of Mayo's distributed data network partners compete with Mayo for patients and talent. How would you redesign the 'One Table' governance to address this conflict of interest?"

**Expected student positions:**

| Position | Core Argument | Best Challenge |
|----------|---------------|----------------|
| Platform is compatible with mission | Revenue funds research; better AI helps more patients globally | If revenue is the goal, patient care decisions will eventually be distorted by commercial incentives |
| Platform undermines mission | Data commercialization creates incentives misaligned with patient trust | Mayo has sustained its nonprofit mission for 157 years -- trust, not charity, is its product |
| Scale is the problem, not the model | The governance model is sound but will break under this level of complexity | Name the specific governance change that would fix it |
| Spin it out as for-profit | For-profit structure would enable faster movement and clearer commercial incentives | Would the Mayo brand survive -- and retain value -- if separated from the nonprofit institution? |

---

### Section 4: The AI Replacement Question (12 minutes)

**Focus:** What does Halamka mean when he says "if your doctor can be replaced by AI, then your doctor should be replaced by AI"? And is he right?

This quote polarizes students. Use that polarization deliberately.

**Opening move:** Ask for a show of hands: who agrees? Who disagrees? Present both camps without resolving. Then push each camp.

**Push pro-AI students:** "What clinical tasks specifically should AI replace? What are the human error rates for those tasks vs. the AI error rates? What happens when the AI is wrong and no physician was involved in the decision?"

**Push skeptical students:** "If a radiologist misses a pulmonary embolism 12% of the time and an AI misses it 3% of the time, what is the argument for keeping the radiologist in that specific task loop?"

**Resolution (or non-resolution):** Surface the distinction between task-level replacement and relationship-level replacement. AI may outperform physicians on specific, well-defined, high-volume tasks in controlled conditions. It does not replicate the doctor-patient relationship, the ability to navigate clinical ambiguity, or the judgment required in edge cases not represented in the training set. The Watson failure illustrates exactly what happens when AI is deployed beyond the task boundaries it was validated for.

**Instructor note:** Do not let students settle into "AI should assist, not replace." That is the comfortable answer, not the analytically rigorous one. The real question is: for which specific tasks, at what performance threshold, with what oversight mechanism, should AI replace human judgment entirely? The supplement's IBM Watson analysis provides a vocabulary for answering this precisely.

---

### Closing (7 minutes)

**Closing question (choose one based on where discussion landed):**

A. "If you were advising Dr. Halamka in 2025, what is the single most important governance change you would recommend for Mayo Clinic Platform as it scales toward 100 million patient lives?"

B. "Should Mayo Clinic Platform be spun out as a separate for-profit entity, or should it remain inside the nonprofit? What does your answer depend on -- and what would change your mind?"

C. "Five years from now, what is the scenario in which Mayo Clinic Platform has clearly succeeded? What is the scenario in which it has clearly failed -- for reasons we could have identified today?"

**Do NOT provide a resolution.** End with constructive uncertainty. The case does not have a right answer, and students who leave class convinced they found one have missed the point.

---

## Board Plan

By end of class, the board should show:

**Left column -- Platform Structure:**
- Two-sided market diagram: [Developers] | [Mayo Enclave] | [Institutional Partners]
- Network effect arrows: data quality up leads to algorithm quality up leads to developer interest up
- Governance layers: One Table / DaTA Board / FDA clearance requirement

**Center column -- Tension Map:**
- Speed vs. Safety: (IBM Watson failure) vs. (Mayo governance model)
- Mission vs. Revenue: (nonprofit identity) vs. (commercial platform logic)
- Openness vs. Control: more partners = more risk = more governance cost
- Admin AI vs. Clinical AI: (Microsoft Copilot, enterprise-wide) vs. (Google enclave, controlled)

**Right column -- Student Positions:**
*Fill in during discussion: capture the 2-3 strongest positions students took, with the specific case evidence they cited. This column makes visible what the class actually argued, not what the case says.*

---

## Assessment Options

### Option A: Individual Write-Up (500-750 words)

> "Halamka described Mayo Clinic Platform's goal as transforming Mayo into a digital data business. Evaluate whether this goal is compatible with Mayo's nonprofit mission. Draw on specific evidence from the case and at least one analytical framework from the supplement."

**Strong responses will:**
- Distinguish between the data governance model and the revenue model
- Apply platform theory or institutional legitimacy theory specifically, not generically
- Engage with the IBM Watson contrast as a governance benchmark
- Acknowledge what is genuinely unknown or unresolved
- Avoid claiming there is an obvious right answer

**Weak responses will:**
- Restate case facts without analysis
- Apply framework vocabulary without connecting it to specific case decisions
- Resolve the mission-revenue tension too cleanly in either direction

### Option B: DaTA Board Exercise (15-minute group exercise)

> "Your group advises the DaTA Board (the 11-member community oversight board for Mayo Clinic Platform). A pharmaceutical company has requested access to the enclave to train a model that would predict which patients are most likely to seek treatment for a condition for which it has a new drug -- enabling targeted outreach. Should you approve this request? What conditions, if any, would you attach?"

**Evaluation criteria:**
- Identification of the specific ethical concerns (commercial targeting, conflict of interest, consent)
- Application of the governance framework (what are the DaTA Board's actual review criteria?)
- Acknowledgment of the revenue vs. mission tension in concrete terms
- Quality of any conditions proposed: are they specific and enforceable, or vague aspiration?

### Option C: Comparative Memo (750-1,000 words -- advanced sections)

> "Compare Mayo Clinic Platform's governance model to a health AI initiative that failed (IBM Watson Health) or succeeded differently (Epic App Orchard). What structural differences explain the different outcomes so far? What does this comparison predict about Mayo Clinic Platform's long-term viability, and what assumptions does that prediction depend on?"

**Evaluation criteria:**
- Accurate characterization of both cases (no strawmanning)
- Specific structural comparison: not "Mayo is more careful" but *why* it is more careful and what that costs
- Explicit prediction with stated assumptions that could be falsified
- Acknowledgment of what the comparison cannot tell us

---

## Note on AI Tool Use in This Case Study

This case study was developed using AI tools (Claude Code, claude-sonnet-4-6) as a research and writing assistant. Instructors should feel comfortable acknowledging this if students ask: the case is itself a demonstration of responsible AI-assisted academic work, with explicit source tracking, verification tiers, and human judgment applied at every decision point.

An AI usage log (ai-usage-log.md) documents all tool contributions in development of this case -- what the AI generated, where human judgment was required, where the AI was incorrect or incomplete. This transparency is a direct application of the course's framework for responsible AI deployment: the same framework the case asks students to evaluate in Mayo's clinical AI work.

---

## Potential Bias Acknowledgment (for Instructor)

This case draws heavily on sources that reflect Mayo Clinic's own perspective -- press releases, official announcements, and Halamka's own public statements. Critical perspectives are not represented: patients whose data is in the enclave, startups who did not succeed in Platform_Accelerate, physicians who resisted AI deployment, or community members skeptical of health data commercialization.

Instructors should explicitly name this limitation in class: "We are seeing this through Halamka's eyes. What would we hear if we talked to the DaTA Board's community members? To a radiologist whose clinical judgment was overridden by an AI recommendation? To a startup that went through Platform_Accelerate and did not receive a commercial pathway? To a patient who did not know their de-identified records were used to train a pharmaceutical company's targeting model?"

Naming the absent voices is itself an analytical act. It models the critical reading that students should apply to all management cases -- and to all AI-generated content.

---

*Teaching note prepared by: Akshay Kumar | ITEC-617 | Kogod School of Business | Spring 2026*
*AI Tool: Claude Code (claude-sonnet-4-6) | April 26, 2026*
