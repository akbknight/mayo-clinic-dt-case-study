# Mayo Clinic Case Study: Technical and Industry Supplement
## ITEC-617 | Kogod School of Business, American University | Spring 2026

> This supplement is intended for students who have read the main case.
> It provides industry context, technical background, and analytical frameworks.
> All data sourced from publicly available materials; source tiers indicated.

---

## Part 1: Industry Context -- AI in Healthcare

### The 2019-2020 Inflection Point

Dr. John Halamka joined Mayo Clinic Platform in January 2020 at a historically significant moment for health AI. Three forces converged between 2018 and 2020 to create conditions that had not previously existed:

**Algorithmic capability**: The 2017 publication of "Attention Is All You Need" (Vaswani et al., Google Brain) introduced the transformer architecture that would eventually power GPT-3, BERT, and all modern large language models. By 2020, researchers were applying transformer-based models to clinical notes, radiology images, and genomic sequences with performance that exceeded earlier approaches by significant margins.

**Regulatory clarification**: In 2019, the FDA published its "Proposed Regulatory Framework for Modifications to Artificial Intelligence/Machine Learning-Based Software as a Medical Device," providing the first structured guidance for how adaptive AI clinical tools would be regulated. This reduced uncertainty that had previously discouraged capital investment in clinical AI.

**Cloud infrastructure maturity**: Google Cloud, AWS, and Microsoft Azure each launched dedicated healthcare cloud environments (Google Cloud Healthcare API, AWS HealthLake, Azure Health Data Services) between 2017 and 2020. These environments offered HIPAA-compliant storage, FHIR-native data exchange, and GPU compute -- infrastructure that previously required tens of millions in capital expenditure from health systems themselves.

These three forces created a window in which platforms combining institutional clinical data with cloud infrastructure and AI capability could potentially achieve durable competitive advantages. Mayo Clinic Platform's January 2020 founding was not coincidental to this timing.

### Market Overview

The global AI in healthcare market was valued at approximately $22.45 billion in 2023 and is projected to reach $208.23 billion by 2030, a compound annual growth rate of approximately 37.5%. Growth is driven by four factors:

1. **Data accumulation**: Electronic health records (EHRs) mandated since the HITECH Act of 2009 have generated massive, standardized clinical datasets.
2. **Compute availability**: Cloud infrastructure has made GPU-scale computation accessible to health systems that could not build it themselves.
3. **Regulatory maturation**: FDA clearance pathways for AI/ML-based Software as a Medical Device (SaMD) have become more defined since 2021.
4. **Workforce pressure**: Physician burnout, nursing shortages, and administrative documentation burden have created strong demand for AI automation.

### Key Application Areas

| Application | Description | Maturity |
|-------------|-------------|---------|
| Clinical decision support | Risk scoring, diagnostic flagging, treatment recommendation | Deployed at scale |
| Radiology AI | Image analysis (CT, MRI, X-ray) for fractures, tumors, abnormalities | Deployed at scale |
| Administrative automation | Prior authorization, clinical documentation, scheduling | Rapidly growing |
| Generative AI documentation | Ambient AI scribes, note summarization, patient communication | Early deployment |
| Drug discovery | Protein folding, compound screening, trial matching | Research/early commercial |
| Foundation models | Large multimodal models trained on clinical data | Emerging |

---

## Part 2: The Platform Model in Healthcare

### What is a Platform Business?

Platform businesses differ from traditional product or service businesses in a fundamental way: they create value by facilitating interactions between two or more distinct user groups rather than by directly producing goods or services.

The canonical examples -- Amazon (buyers and sellers), Uber (riders and drivers), App Store (developers and users) -- share three structural features:

1. **Network effects**: The platform becomes more valuable as more participants join.
2. **Data leverage**: Interactions generate data that improves the platform for everyone.
3. **Ecosystem creation**: Third-party producers add value that the platform owner could not produce alone.

Mayo Clinic Platform attempted to apply this logic to healthcare data. The patient data network, the solution developer ecosystem, and the distributed institutional data network all exhibit network effect characteristics: more data makes AI algorithms better; better algorithms attract more developers; more developers create more products that attract more institutional partners; more institutions contribute more data.

### The Network Effect Flywheel

A visualization of Mayo Clinic Platform's intended network effects:

```
[More Institutional Data Partners]
          |
          v
[Larger, More Diverse Patient Dataset]
          |
          v
[Higher-Quality, More Generalizable AI Algorithms]
          |
          v
[More Attractive to Solution Developers]
          |
          v
[More AI Products Available to Health Systems]
          |
          v
[More Health Systems Join as Partners]
          |
          +--> [More Institutional Data Partners]  <-- flywheel repeats
```

The critical strategic question: at what scale does this flywheel become self-sustaining? The Platform grew from a small set of institutional partners in 2021 to 61 health providers and 9 network partners by 2024, suggesting the flywheel was gaining momentum. Whether it has reached escape velocity -- the point at which competing platforms cannot easily replicate the combination -- is the strategic question the case leaves open.

### The Multi-Homing Problem

A risk for any platform is "multi-homing": the ability of participants on one or both sides to simultaneously use competing platforms. For Mayo Clinic Platform:

- **Developer multi-homing**: A health AI startup can request access to Mayo's enclave AND participate in Epic's App Orchard AND build on Google's Med-PaLM APIs. Mayo does not hold exclusive relationships with most developers.
- **Institutional multi-homing**: A health system can join Mayo's distributed data network AND use Microsoft Azure Health AND maintain its own Epic EHR. Switching costs are low in the early stages.

Multi-homing reduces the platform's power over its participants and limits its ability to capture value. Halamka's implicit response to this risk was to emphasize that the *combination* -- validated data, the Mayo brand, and clinical credibility -- was not replicable by any single technology competitor. The data under glass architecture also creates switching costs over time: once an institution has built governance infrastructure around the federated model, moving to a centralized alternative requires rebuilding that infrastructure from scratch.

### The "Convener" vs. "Controller" Model

Traditional platform owners (Apple, Google, Amazon) exercise strong control over who participates and on what terms. Halamka chose a different posture -- the "convener" model -- in which Mayo primarily sets standards and validates participants rather than controlling the underlying technology. This choice reflects both the regulatory environment (health data is more tightly regulated than consumer data) and the mission context (a nonprofit has legitimacy constraints a commercial platform does not).

The convener model sacrifices control for legitimacy. It may also sacrifice long-term revenue capture: if Mayo's primary function is validation and certification rather than proprietary technology, participants who complete the validation pipeline may route around Mayo in subsequent product iterations.

---

## Part 3: The "Data Under Glass" Architecture

### Technical Design

Mayo Clinic Platform's central technical innovation was a federated learning architecture that the National Academies of Sciences described as "data under glass."

**Traditional data sharing model:**

| Step | Action | Risk |
|------|--------|------|
| 1 | Institution transfers data to third party | Data leaves institutional control |
| 2 | Third party trains model on transferred data | Privacy exposure during training |
| 3 | Third party returns model to institution | Data cannot be "un-transferred" |
| 4 | Institution uses model in clinical setting | Ongoing residual re-identification risk |

**Data under glass (federated) model:**

| Step | Action | Safeguard |
|------|--------|-----------|
| 1 | Institution maintains data in private enclave | Data never leaves home jurisdiction |
| 2 | Third party sends algorithm INTO the enclave | Operator reviews algorithm before entry |
| 3 | Algorithm trains on data inside the enclave | "Bin size of 10" rule applied to all outputs |
| 4 | Only the trained model (not data) exits enclave | Post-exit: model audited before clinical use |

This model addresses the core privacy objection to health data sharing: the data never moves. The National Academies case study noted that the enclave used a "bin size of 10" standard for de-identification -- any output from the enclave must be attributable to at least 10 individuals, preventing re-identification of individuals from aggregate results. (National Academies of Sciences, 2023 [T2])

### Governance Layers Over the Enclave

Technical safeguards are reinforced by institutional governance at multiple levels:

1. **"One Table" multi-stakeholder task force** -- operational access review; reviews all developer requests to enter the enclave
2. **Health Data and Technology Advisory (DaTA) Board** -- community oversight; 11 members representing patients, clinicians, technologists, and ethicists; established 2021
3. **Mayo Clinic institutional and legal review** -- IRB-style oversight for any research application
4. **Joint steering committee for the Mayo-Google partnership** -- bilateral governance specific to the Google Cloud relationship

The layered governance model reflects deliberate redundancy: no single layer is expected to catch all problems. However, as the platform scaled to 81 solution developers and 9 institutional partners, the governance overhead of applying all four layers to each interaction became a non-trivial operational challenge. This is the "governance scaling problem" that the case surfaces in its closing section.

---

## Part 4: Regulatory Environment

### FDA SaMD Regulation

AI/ML-based clinical tools in the United States are regulated by the FDA as Software as a Medical Device (SaMD). Key regulatory frameworks relevant to Mayo Clinic Platform:

**FDA Predetermined Change Control Plans (2021):** Allow AI developers to pre-specify the types of algorithm updates that can be made without submitting a new 510(k) or PMA, reducing the regulatory burden on adaptive AI systems.

**De Novo pathway:** Used for novel AI diagnostic tools with no predicate device. ELEFT (the Eko Low Ejection Fraction Tool, co-developed by Mayo and Eko Health) received FDA clearance through this pathway in March 2024.

**Real-World Performance Monitoring:** FDA increasingly requires AI/ML devices to include post-market performance monitoring plans -- a requirement that favors platforms with ongoing access to real-world clinical data, such as Mayo Clinic Platform.

### International Regulatory Complexity

The distributed data network's expansion to Brazil, Israel, and Canada introduced a multi-jurisdictional regulatory environment. The federated model was specifically designed to navigate this complexity by keeping data local:

| Jurisdiction | Primary Law | Key Provision | Compatibility with Federated Model |
|--------------|------------|---------------|-----------------------------------|
| United States | HIPAA (1996) + HITECH (2009) | Expert Determination de-identification; data use agreements | High -- federated model designed to HIPAA standards |
| Brazil | LGPD (2020) | Consent requirements; data localization | High -- federated model keeps data in Brazil |
| Israel | Protection of Privacy Law (1981) | Heightened controls for sensitive health data | Medium-High -- local governance review required |
| Canada | PIPEDA (federal) + provincial laws | Purpose limitation; accountability principles | High -- data remains within Canadian institutions |
| European Union | GDPR (2018) + AI Act (proposed) | Right to explanation; high-risk AI obligations | Medium -- additional documentation required; not yet in Mayo network |

**Key insight**: The federated model's primary advantage in the international context is that it sidesteps data localization requirements. Because patient data never leaves the home institution's jurisdiction, each country's data sovereignty laws are satisfied by design -- not by legal workaround. This makes geographic expansion considerably easier than it would be for a centralized model that must negotiate separate cross-border data transfer agreements in each jurisdiction.

---

## Part 5: Competitive Analysis

### The Landscape of Health AI Platforms (2023-2024)

| Company | Data Strategy | AI Approach | Scale | Key Risk |
|---------|--------------|-------------|-------|----------|
| Mayo Clinic Platform | Federated enclave; institutional partners | Validation + foundation model development | 56M patient lives (2024) | Governance complexity at scale |
| Epic Systems | Proprietary EHR ecosystem; App Orchard | EHR-native predictive models | 250M+ patient records | Closed ecosystem limits external innovation |
| Google Health | Cloud-native; consumer data integration | Foundation models (Med-PaLM 2) | Multiple large health systems | Consumer trust; healthcare domain expertise |
| Microsoft Azure Health | Azure cloud; M365 Copilot | LLM-powered productivity; OpenAI partnership | Enterprise-wide | Generic LLM limitations in clinical settings |
| Amazon AWS Health | HealthLake; Comprehend Medical | NLP + data infrastructure | Broad SME market | Lack of clinical brand credibility |
| IBM Watson Health | Oncology AI (divested 2022) | Supervised learning | Sold to Francisco Partners | Overclaimed clinical capabilities; failed validation |

### The IBM Watson Health Warning

IBM Watson Health serves as the most studied cautionary tale in health AI. IBM announced Watson for Oncology in 2011 as a system that would recommend cancer treatment plans. By 2022, IBM had divested Watson Health after multiple health systems reported that its recommendations did not align with clinical standards, were trained on too few cases, and in some instances suggested unsafe treatments.

The failure had structural causes directly relevant to evaluating Mayo Clinic Platform:

- **Validation gap**: Watson was trained on cases from a single institution (Memorial Sloan Kettering) and did not generalize to different patient populations. MD Anderson Cancer Center discontinued a $62 million Watson project in 2017 after finding recommendations that contradicted physician judgment and, in some cases, suggested treatments that physicians considered clinically dangerous.
- **Explainability deficit**: Physicians could not understand why Watson made specific recommendations, making it impossible to calibrate trust. Without explainability, there is no principled mechanism to decide when to follow the AI and when to override it.
- **Overclaiming**: Commercial pressure led IBM to market capabilities the system had not demonstrated in controlled clinical evaluation. Watson was sold to hospital executives, not to the clinical researchers who could have identified its limitations before deployment.
- **Governance absence**: No independent mechanism existed to validate Watson's recommendations against actual patient outcomes at scale. There was no equivalent of Mayo's DaTA Board.

Mayo Clinic Platform's design choices -- federated governance, the DaTA Board, the "bin size of 10" de-identification standard, the Platform_Accelerate validation requirement, and the explicit framing of FDA clearance as a bar for deployment -- reflect lessons from the Watson failure. Whether those safeguards are sufficient at 56 million patient lives and 81 solution developers is a question the case invites students to examine critically.

---

## Part 6: Analytical Frameworks

### Framework 1: Platform Strategy (Two-Sided Markets)

Michael Katz and Carl Shapiro's work on network externalities, and subsequent platform strategy research (Rochet and Tirole; Parker, Van Alstyne, and Choudary), identifies key variables for platform success:

| Variable | Mayo Clinic Platform Application |
|----------|--------------------------------|
| Same-side network effects | More patient data makes algorithms more accurate for all users |
| Cross-side network effects | More developers attract more institutions; more institutions attract more developers |
| Envelopment risk | Could Google or Microsoft absorb Mayo's platform function entirely? |
| Multi-homing | Can startups use both Mayo data AND Epic App Orchard simultaneously? |
| Openness vs. control | How much control should Mayo retain over who enters the ecosystem? |

**Discussion prompt:** Where on the openness-control spectrum should Mayo Clinic Platform sit? What are the tradeoffs of making the enclave more vs. less open?

### Framework 2: Institutional Trust and Legitimacy

Organizational theorists (DiMaggio and Powell; Suchman) distinguish three types of organizational legitimacy:

- **Normative legitimacy**: The organization does what is considered "right" by its field
- **Cognitive legitimacy**: The organization's activities are taken for granted as sensible
- **Regulative legitimacy**: The organization complies with laws and regulations

Mayo Clinic's core asset in its Platform strategy is normative legitimacy -- the brand trust built over 157 years. Halamka explicitly invoked this:

> "The Mayo brand is a very powerful way to bring people together."
> -- Dr. John Halamka, HealthLeaders Media (2020) [T2]

**Discussion prompt:** What actions or decisions could erode Mayo's normative legitimacy? What governance mechanisms are designed to protect it? What happens to the platform business if that legitimacy is damaged?

### Framework 3: Disruptive Innovation (Christensen)

Clayton Christensen's disruption theory distinguishes between sustaining innovations (which improve existing products for existing customers) and disruptive innovations (which initially underperform on traditional metrics but create new markets by serving overlooked customers or reducing cost dramatically).

**Applying the disruption lens to Mayo Clinic Platform:**

| Dimension | Sustaining Reading | Disruptive Reading |
|-----------|------------------|------------------|
| Target customer | Existing Mayo patients and partner institutions | Health systems without AI capabilities; global populations underserved by traditional research |
| Performance trajectory | Better care for existing high-acuity cases | Lower-cost clinical AI validation pipeline for startups that previously could not access real patient data |
| Business model | Premium platform fees; not fundamentally different pricing | Per-use data access fees that could commoditize clinical AI validation |
| Incumbent threat | Does not directly threaten Epic or Google today | Could commoditize the validation service that startups currently pay premium prices for |

**Caution for students**: Christensen's framework is frequently misapplied by treating any "new" thing as disruptive. The relevant test is whether the innovation creates a new value network, not whether it uses new technology. Argue for a classification using the specific dimensions above, not intuition.

**Open question**: If Mayo Clinic Platform succeeds at scale, does it eventually become the incumbent that a future disruptor needs to challenge?

---

## Glossary

| Term | Definition |
|------|------------|
| Algorithm | A set of rules or statistical model that processes input data to produce an output |
| De-identification | Removal of personal identifiers from patient data to prevent re-identification |
| Federated learning | Machine learning technique where models train on distributed data without centralizing it |
| Foundation model | A large AI model trained on broad data and adapted for specific downstream tasks |
| SaMD | Software as a Medical Device -- software that meets FDA medical device definition |
| 510(k) | FDA clearance pathway for medical devices substantially equivalent to a predicate device |
| De Novo pathway | FDA clearance pathway for novel medical devices with no predicate; used for first-of-kind AI tools |
| HIPAA | Health Insurance Portability and Accountability Act -- US health data privacy law (1996) |
| HITECH | Health Information Technology for Economic and Clinical Health Act -- EHR adoption incentives (2009) |
| LGPD | Lei Geral de Proteção de Dados -- Brazil's comprehensive federal data protection law (2020) |
| PIPEDA | Personal Information Protection and Electronic Documents Act -- Canada's federal privacy law |
| EHR | Electronic Health Record -- digital patient medical record system |
| NLP | Natural Language Processing -- AI applied to human language (clinical notes, radiology reports, etc.) |
| Platform_Accelerate | Mayo Clinic's 30-week startup incubation program for health AI companies |
| Network effects | Property by which a platform's value increases as more participants join |
| Multi-homing | Participating in multiple competing platforms simultaneously; reduces platform lock-in |
| Envelopment | Platform strategy in which one platform expands to absorb the core function of a competing platform |
| Governance | Structures, processes, and accountability mechanisms for oversight and decision authority |

---

*Supplement prepared by: Akshay Kumar | ITEC-617 | Kogod School of Business, American University | Spring 2026*
*AI Tool: Claude Code (claude-sonnet-4-6) | Research date: April 26, 2026*
*All factual claims are sourced from publicly verified materials. Source tiers (T1/T2/T3) are indicated in body text where applicable. Market projections sourced from industry reports; cite original reports in any formal submission.*
