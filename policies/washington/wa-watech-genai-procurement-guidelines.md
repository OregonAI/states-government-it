---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-watech-genai-procurement-guidelines
title: Initial procurement guidelines for public sector procurement, deployment, and monitoring of Generative
  AI Technology
doc_type: policy
citation: WaTech Guidance, September 2024
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2024-11/Initial%20Procurement%20Guidelines%20for%20GenAI%20Final.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 603b16c6b8f2b1aa960fa246aeded538c5209a02c2cfd7e322c696b64c6f6151
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters).
last_verified: ''
verified_by: ''
maintainer: ''
relationships:
  implements: []
  implemented_by: []
  references_external: []
  related: []
  supersedes: []
tags:
- ai
- procurement
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Initial procurement guidelines for public sector procurement, deployment, and monitoring of Generative AI Technology (WaTech Guidance, September 2024)

## At a glance

Risk-tiered procurement, deployment and monitoring guidance for generative AI. WaTech guidance issued under Executive Order 24-01 and listed on the WaTech Artificial Intelligence Resources page (https://watech.wa.gov/artificial-intelligence-resources).

## Full text

Initial procurement guidelines for
public sector procurement,
deployment, and monitoring of
Generative AI Technology
September 2024

Table of Contents

Introduction ............................................................................................................................. 3
   Relevant legal and regulatory requirements ................................................................... 4
Deployment considerations .................................................................................................. 4
   Core concepts ..................................................................................................................... 5
       Definition of Generative AI Technology ....................................................................... 5
       Goals of using Generative AI Technology ................................................................... 6
       Washington State Agency Privacy Principles ............................................................... 7
       Generative AI Technology Guiding Principles ............................................................ 8
Generative AI procurement guidance ............................................................................... 10
   Phases ................................................................................................................................. 10
       Requirements development ........................................................................................ 10
       Procurement, development, and deployment .......................................................... 11
       Ongoing monitoring..................................................................................................... 11
       Generative AI procurement tasks................................................................................ 12
   Generative AI procurement tasks table .......................................................................... 13
   Purpose of Generative AI tasks ........................................................................................ 14
   Description of tasks ........................................................................................................... 14
   Actions or controls to take for tasks ................................................................................ 19
Appendix A ........................................................................................................................... 44
Sample Gen AI procurement questionnaire ..................................................................... 44
Appendix B ............................................................................................................................ 46
Sample Gen AI initial use case assessment ....................................................................... 46
Generative AI Technology Evolution.................................................................................. 48
Contact................................................................................................................................... 48
References ............................................................................................................................. 49

                                                                                                                 watech.wa.gov 2

Introduction
This guidance was created by Washington
Technology Solutions (WaTech) in
collaboration with the Department of             Gen AI guidance must
Enterprise Services (DES) and other              address safety and
partners pursuant to the Governor's              effectiveness,
Executive Order 24-01 to develop initial         algorithmic
guidance on the procurement and use of
                                                 discrimination, data
generative artificial intelligence (Gen AI)
technology.                                      privacy, and
                                                 cybersecurity.
The Executive Order (EO) recognizes that
Gen AI is a transformative technology
which has the capacity to improve the way the Washington state conducts
business and serves the public. The potential to catalyze innovation and
enhance human potential is substantial with this new technology. However, this
advancement must be tempered with the responsibility to deploy the
technology in a safe, responsible, ethical, and efficient manner. As such, the
Governor has directed that these Generative AI (Gen AI) guidelines be built on
guidance from the White House's Blueprint for an Al Bill of Rights and the
National Institute for Science and Technology's (NIST) Al Risk Management
Framework and address safety, effectiveness, algorithmic discrimination, data
privacy, and cybersecurity. Following the issuance of the Governor’s Executive
Order, NIST has also released a draft companion resource specific to
generative AI which we have also relied on for these guidelines.
“Generative AI Technology” is defined as a technology that can create content,
including text, images, audio, or video, when prompted by a user. Generative
AI systems learn patterns and relationships from large amounts of data, which
enables systems to generate new content that may be similar, but not
necessarily identical, to the underlying training data.” EO 24-01 defines “High-
Risk Generative AI System” and mandates the assessment of high-risk systems
prior to deployment. A “High-Risk Generative AI System” is defined as a
system “using generative AI technology that creates a high risk to natural
persons' health and safety or fundamental rights. Examples include biometric
identification, critical infrastructure, employment, health care, law enforcement,
and administration of democratic processes.” (See Appendix B for levels of
risk.)

                                                                 watech.wa.gov 3

This document is meant to be a resource for Washington state agencies to use
when procuring or using Gen AI. This document provides an overview of
principles and steps to take when considering procuring or using Gen AI for
public services. This guide does not represent the legal opinion of any
Washington state agency, including the Attorney General’s Office. Readers
should not rely on information in this guide regarding specific applications of
the laws without seeking legal counsel.

Relevant legal and regulatory requirements
All Generative AI procurement or use guidance shall defer to and work in
concert with procurement rules and laws in Washington including but not
limited to Chapter 39.26 RCW, Washington Department of Enterprise Services
procurement policies and rules, and WaTech technical and security policies.

Deployment considerations
This document includes a series of recommendations that should be
considered when evaluating the procurement, development, deployment, use,
or ongoing monitoring of Generative AI technology. These guidelines include
tasks that should take place throughout the lifecycle of use of a Gen AI
technology. For purposes of this procurement guidance, the
recommendations are organized into three different phases:
   1. Requirements development.
   2. Procurement, development , and deployment.
   3. Ongoing monitoring.

The purpose of this document is to provide procurement guidance that aligns
with the:

   •   White House's Blueprint for an Al Bill of Rights.
   •   National Institute for Science and Technology's Al Risk Management
       Framework.
   •   Washington state’s interim guidelines for purposeful and responsible
       use of artificial intelligence.

This guidance includes tasks and considerations of risks, as well as actions or
controls agencies can undertake to address risks and align with these
underlying principles.

                                                                 watech.wa.gov 4

In determining whether to proceed with the procurement, development,
deployment, or use of Gen AI, agencies should exercise discretion and
thoughtfulness. In doing so, agencies should consider the risks and goals of
using Gen AI, which are described in the Core Concepts section. With these
considerations in mind, agencies should consider the appropriateness of
progressing with the procurement or use of Gen AI and the business problem
its use seeks to address. As such, agencies should keep in mind that:

•   The capabilities of Gen AI technology may change over time with new
    productions or version releases.

•   Changes in Gen AI technology capabilities may change associated risks for
    both the agency and Washington residents, which could change review or
    approval requirements for development, procurement, or usage of
    particular Gen AI technology.

•   WaTech may adjust and update this Gen AI procurement, development,
    deployment, use, and ongoing monitoring guidance based on updated
    government and industry research, experiences, or legal requirements.

•   Agencies should be ready to be intentional and descriptive in their
    assessments and are encouraged to seek support and guidance from
    WaTech.

Core concepts
Definition of Generative AI Technology
For purposes of this initial Gen AI Procurement, Use, and Monitoring
Guidance, the following definitions of “Generative AI Technology” and “High-
Risk Generative AI System” shall be used (See EO 24-01):

    •   “Generative AI Technology” is a technology that can create content,
        including text, images, audio, or video, when prompted by a user.
        Generative AI systems learn patterns and relationships from large
        amounts of data, which enables systems to generate new content that
        may be similar, but not identical, to the underlying training data.
    •   “High-Risk Generative AI System” means systems using generative AI
        technology that creates a high risk to natural persons' health and safety
        or fundamental rights. Examples include biometric identification, critical
        infrastructure, employment, health care, law enforcement, and
        administration of democratic processes.

                                                                  watech.wa.gov 5

Goals of using Generative AI Technology
There are several goals of using generative AI technology, including:

•   Efficiency: Gen AI may assist governmental entities in streamlining
    processes and making administrative decisions more quickly and efficiently.

•   Economical: Gen AI may reduce costs by reducing the time necessary to
    record and analyze data, conduct calculations, and make decisions.

•   Equity: Reduce the biases and inaccuracies of current systems: While Gen
    AI may introduce and reinforce bias, it also potentially provides an
    opportunity to address biases.

•   Effectiveness: Improving delivery of public services: Gen AI may help the
    public receive improved and more accessible services.

Risks
Conversely, there are several known risks of using Gen AI technology today:

•   Inaccuracies: Gen AI technologies may reproduce biases or introduce new
    inaccuracies or “hallucinations” and may be less accurate than human
    decision-makers.

•   Automation bias: Humans tend to place too much trust in automated
    decisions. Humans may overestimate the accuracy of data analysis outputs
    by Gen AI systems, which may be as, or more, error-prone than human
    decision-makers. Automation bias can obfuscate or increase biased and
    inaccurate decision-making. This may include discounting contradictory
    information made without automation.

•   Non-transparency: It is difficult or impossible for individuals to know if an
    Gen AI is being used, how that system operates, and the impacts of the
    system on individuals and society.

•   Lack of explainability: Gen AI outputs are very difficult to explain in clear
    and concise language that would be understandable to those auditing the
    system or those potentially impacted by their use. This risk may be
    especially prevalent when a Gen AI tool is procured through a third-party
    vendor. Even the developers of Gen AI models may not know why or how
    particular outputs are provided due to the size and complexity of large
    models.

                                                                   watech.wa.gov 6

•   Lack of accountability: Individuals who are affected by Gen AI outputs may
    not have the ability to meaningfully challenge a system’s decisions.
    Governmental entities that procure or use Gen AI systems may overlook
    consulting with the individuals and communities that may be affected by its
    use or may not have a human-centered dispute resolution process.

•   Threats to privacy: Large amounts of data about individuals are often used
    to train Gen AI technologies (both simple and complex) to transform inputs
    into decisions or suggestions. Individuals may not understand or have
    given consent for their data to be used for such a purpose.

•   Threats to legitimacy and public trust: Use of Gen AI systems may
    undermine the legitimacy and public trust of governmental entities when
    such entities re-delegate their decision-making responsibilities to
    unaccountable and nontransparent systems.

•   Discrimination: Gen AI outputs may reproduce or exacerbate existing
    patterns of discrimination that are already present in our society. This can
    lead to harms on vulnerable or marginalized communities.

•   Threats to cybersecurity: Cybersecurity risks include prompt injections,
    malicious code, accidental data leaks and breaches due to control or
    permission issues when using unproperly reviewed resources or systems.

Washington State Agency Privacy Principles
The Washington State Agency Privacy Principles serve as a framework to guide
state agencies in protecting the privacy and security of personal information
they collect and maintain. These principles were developed to address the
growing concerns surrounding data privacy and ensure that individuals'
personal information is handled with care and transparency. Applying these
principles helps agencies balance the risks and goals of systems processing
personal information, especially in high-risk Generative AI systems. Along
those lines, these principles promote accountability, transparency, and the
responsible use of personal data by state agencies.
    1. Lawful, fair, and responsible use: The collection, use and disclosure of
       information is based on legal authority, not deceptive, not
       discriminatory or harmful, and relevant and reasonably necessary for
       legitimate purposes.

                                                                  watech.wa.gov 7

   2. Data minimization: The minimum amount of information is collected,
      used, or disclosed to accomplish the stated purpose for collecting the
      information.

   3. Purpose limitation: The reasons for gathering information are
      identified before it is collected. Use and disclosure is limited to what is
      reasonably necessary in relation to the specific reasons the information
      was collected.

   4. Transparency and accountability: Transparency means being open
      and transparent about what personal information is collected, for what
      purposes, and who it is shared with under what circumstances.
      Accountability means being responsible and answerable for following
      data privacy laws and principles.

   5. Due diligence: Taking reasonable steps and exercising care before and
      after entering into an agreement or arrangement with a third party that
      includes sharing personal information.

   6. Individual participation: Give people control of their information when
      possible.

   7. Security: Appropriate administrative, technical and physical security
      practices to protect the confidentiality, integrity, availability and control
      of personal information.

The Washington State Agency Privacy Principles aim to establish a culture of
privacy and data protection within state agencies, promoting trust and
confidence among individuals whose personal information is collected. By
adhering to these principles, state agencies can ensure the responsible
handling of personal data while balancing the need for data-driven decision-
making and public service delivery which may use Gen AI.

Generative AI Technology Guiding Principles
The intention of the state of Washington is to follow the principles in the White
House Blueprint for an AI Bill of Rights and the National Institute of Standard
and Technology (NIST) AI Risk Framework, which serve as the basis for the
purposeful and responsible use of artificial intelligence. A foundational part of
both the Blueprint and NIST AI Risk Framework is to ensure the trustworthiness
of systems that use AI, which includes Generative AI. The guiding principles
are:

                                                                   watech.wa.gov 8

•   Safe, secure, and resilient: AI should be used with safety and security
    in mind, minimizing potential harm and ensuring that systems are
    reliable, resilient, and controllable by humans. AI used by state agencies
    should not endanger human life, health, property, or the environment.

•   Valid and reliable: Agencies should ensure AI use produces accurate
    and valid outputs and demonstrates the reliability of system
    performance.

•   Fairness, inclusion, and non-discrimination: AI must be developed
    and used to support and uplift communities, particularly those
    historically marginalized. Fairness in AI includes concerns for equality
    and equity by addressing issues such as harmful bias and discrimination.

•   Privacy and data protection: AI should be used to respect user privacy,
    ensure data protection, and comply with relevant privacy regulations
    and standards. Privacy values such as anonymity, confidentiality, and
    control generally should guide choices for AI design, development, and
    deployment. Privacy-enhancing systems should safeguard human
    autonomy and identity where appropriate.

•   Accountability and responsibility: As public stewards, agencies
    should use AI responsibly and be held accountable for the performance,
    impact, and consequences of its use in agency work.

•   Transparency and auditability: Acting transparently and creating a
    record of AI processes can build trust and foster collective learning.
    Transparency reflects the extent to which information about a AI system
    and its outputs are available to the individuals interacting with the
    system. Transparency answers “what happened” in the system.

•   Explainable and interpretable: Agencies should ensure AI technology
    use in a system can be explained, meaning “how” the decisions or
    outputs that were made by the system can be understood.
    Interpretability of a system means an agency can answer the “why” for a
    decision made by the system, and its meaning or context to the user.

•   Public purpose and social benefit: The use of AI should support the
    state’s work in delivering better and more equitable services and
    outcomes to its residents. Where appropriate, individuals should be
    able to opt out of Gen AI technology or high-risk Generative AI systems
    in favor of a human alternative.

                                                              watech.wa.gov 9

Generative AI procurement guidance
This guidance is for Generative AI solutions that are both intentional and
incidental to technology procurements. Intentional generative AI is where an
agency is specifically seeking to purchase or use a generative AI product or
service. Incidental generative AI is when the Gen AI capability is built into the
product or service, which may include software as a service (SaaS) solutions.
However, please note this document is intended to be best practices and
recommendations for how to think about procuring and deploying Generative
AI responsibly.

Phases
   1. Requirements Development.
   2. Procurement, development, and deployment.
   3. Ongoing Monitoring.

Requirements development
The Requirements Development phase is the initial stage of the process where
an assessment is conducted before the system's development or procurement.
It involves evaluating the reasons for adopting the system and identifying the
associated risks in its design and implementation. This phase focuses on
considering factors such as:

   •   The system's benefits in fulfilling the agency's mission and societal
       goals.
   •   Identifying risks for potential inaccuracies, biases, or disproportionate
       effects.
   •   Considering the system's needed security against data disclosure or
       manipulation.
   •   Determining type and amount of data needed.
   •   Assessing its potential impact on public trust.

The phase also emphasizes the importance of providing opportunities for
public participation, documenting the process and decisions transparently,
and exercising caution in adopting new systems that lack testing for bias or
accuracy. This phase sets the foundation for informed decision-making and
paves the way for subsequent development or procurement stages.

                                                                 watech.wa.gov 10

Procurement, development, and deployment
The Procurement, Development, and Deployment phase refers to the stage in
which the system is either built or acquired for deployment. During this phase,
careful consideration is given to the system's design, functionality, and the
procurement process involved. It entails translating the identified requirements
and objectives into a tangible system, ensuring that it aligns with the intended
purpose and adheres to applicable guidelines and regulations. This phase
involves activities such as system development, vendor selection, contract
negotiation, and the establishment of technical specifications and deployment
plans. It also includes conducting thorough testing and validation to assess the
system's performance, accuracy, and potential biases before its deployment.
This procurement phase is critical in
ensuring that the Gen AI technology is
properly designed, sourced, and prepared    Ongoing monitoring and
for subsequent operational and              updated testing and
deployment phases. These guidelines         assessments should be
require that any vendor providing a high    required when substantive
risk Generative AI system to an agency must system modifications or
certify that the vendor has implemented an  changes in the Gen AI use
AI governance program consistent with the   occur.
National Institute of Standards and
Technology Artificial Intelligence Risk
Management Framework. (See Executive Order 24-01)

Ongoing monitoring
The Ongoing Monitoring phase refers to the continual process of observing,
evaluating, and assessing the system's performance, outcomes, and
adherence to established standards. It involves the regular monitoring of data
inputs, system outputs, and decision-making processes to identify any
potential issues, biases, inaccuracies, or unintended consequences. This phase
includes the collection and analysis of relevant data, such as audit trails, logs,
or hashes to evaluate the system's effectiveness, fairness, and reliability over
time.
Ongoing monitoring also involves periodically comparing the system's
outcomes against desired goals and benchmarks to ensure its alignment with
organizational objectives and societal values. Additionally, it may encompass
periodic assessments, independent audits, and participant engagement to
promote transparency, accountability, and ongoing improvement of the Gen

                                                                watech.wa.gov 11

AI technology. The monitoring phase aims to maintain the system's integrity,
address emerging challenges, and facilitate necessary adjustments and
enhancements to optimize its performance and mitigate potential risks.
Ongoing monitoring and updated testing and assessments should be required
when substantive system modifications or changes in the Gen AI use occur.

Generative AI procurement tasks
Ten activities should be completed during the procurement or deployment of
a Gen AI technology, which includes both intentional Gen AI and incidental
Gen AI. “Generative AI Technology” is defined as a technology that can create
content, including text, images, audio, or video, when prompted by a user.
Generative AI systems learn patterns and relationships from large amounts of
data, which enables systems to generate new content that may be similar, but
not necessarily identical, to the underlying training data.” (EO 24-01).
As shown in the chart below, some of these activities are tied to a specific
phase, while others span two or three phases. These tasks should be
considered throughout the Gen AI technology use but are not exhaustive or
exclusionary of other considerations. Detailed descriptions of the activities and
related tasks are below. The activities include:
1. Gen AI initial use case assessment.
2. Evaluation of whether to adopt a system.
3. Updated assessments.
4. Periodic testing.
5. Transparency of the model or system.
6. Audit trails.
7. Training to understand automation basis.
8. Evaluation of risks/determination whether to proceed.
9. Review of decisions by those affected.
10. Weighing advantages against known bias or inaccuracies.

                                                                watech.wa.gov 12

Generative AI procurement tasks table

           Phases           Requirements   Procurement,    Ongoing
                            development    development,   monitoring
                                               and
                                            deployment

1.    Gen AI Initial Use
      Case Assessment.
                                 √              √

2.    Evaluation of
      whether to adopt a
                                 √
      system.

3.    Updated
      assessments.
                                                              √

4.    Periodic testing.                                       √
5.    Transparency of
      the model or
                                 √              √             √
      system.

6.    Audit trails.              √              √             √
7.    Training to
      understand
                                 √              √             √
      automation basis.

8.    Evaluation of
      risks/determination
                                 √              √             √
      whether to
      proceed.

9.    Review of decisions
      by those affected.
                                 √              √             √

10.   Weighing
      advantages against
                                                √             √
      known bias or
      inaccuracies.

                                                     watech.wa.gov 13

Purpose of Generative AI tasks
The purpose of the ten tasks for Gen AI procurement, development,
deployment, or use is to mitigate the risk and help achieve the goals of
implementing Gen AI technology. This generally includes practices such as:
•   An evaluation of whether it is appropriate for governmental entities to use
    the Gen AI technology. Depending on system impacts, this evaluation
    should incorporate public participation and comment.
•   Independent testing for bias and inaccuracy.
•   Transparency so that the public is informed that a Gen AI technology is
    being used and understands information about the system and its use.
•   Accountability so that the public may meaningfully engage and allow
    individuals to seek redress when impacted by a Gen AI technology.

Description of tasks
This section provides a description of the Gen AI technology procurement
tasks identified above and the phase of the Gen AI procurement lifecycle each
activity should be performed.

•   Generative AI Initial Use Case Assessment: Prior to procurement,
    government organizations need to determine what is the business need or
    problem they are trying to solve. While Gen AI may be an appropriate
    solution, it may not always be optimal or necessary for an agency’s needs.
    Agencies should perform an Initial Generative AI Use Case Assessment for
    either intentional or incidental Gen AI (See example assessment in
    Appendix B) that informs the decision to pursue a Gen AI technology
    solution. This assessment includes considering cost-benefit analysis and
    operational benefits of procuring, developing, or deploying a Gen AI tool.
    As part of this process, agencies need to also determine if the use case
    meets the definition of “high-risk.”

    The Initial Gen AI Use Case Assessment considers various criteria to
    determine resource investment. These criteria may include factors such as:
       • The significant impact on identified or identifiable individuals.
       • The scale of influence on many individuals.
       • The potential for high error risks (especially for systems lacking
           transparency, bias testing, or accuracy assessment).
       • The agency's discretion in creating the model or system.
       • The level of automation with opportunities for human review.
       • How the Gen AI model will be used within a system.

                                                                watech.wa.gov 14

When the Gen AI technology significantly affects individuals in high-risk use
cases, the governmental entity should be transparent about its initial
assessment of the Gen AI technology and make it available to the public.

Phase(s):

       •    Requirements development.
       •    Procurement, development, and deployment.
       •    Ongoing monitoring.

•   Evaluation of whether to adopt a system: Before acquiring, creating, or
    employing a Gen AI technology, the government organization must
    conduct an evaluation of the rationale behind adopting such systems,
    identify business needs, and the associated risks related to their design and
    deployment. This assessment should leverage and optimize the existing
    procurement process to ensure the most effective use of resources. The
    evaluation should consider the following:

       •    Assess how the system contributes to the agency's mission and
            societal objectives.
       •    Conduct tests to identify any potential inaccuracies, biases, or
            disproportionate effects arising from the system or the data sources
            used in its design or training. If such issues are recognized, identify
            appropriate measures that should be taken to address them.
       •    Ensure the Gen AI system's resilience against unauthorized data
            disclosure or malicious manipulation (e.g. data poisoning, deep
            fakes, or unethical or offensive misuse).
       •    Determine whether the use of a Gen AI may adversely impact the
            public's trust in the actions of the Washington state government.
       •    Provide opportunities for public participation, including informing
            the public about the risks and benefits associated with the Gen AI
            technology and soliciting meaningful input from affected individuals
            and communities regarding its design and deployment.
       •    Document the process and decisions for adoption in a manner that
            enables future review while maintaining transparency for the public.
       •    Exercise extreme caution when considering the adoption of any new
            high-risk Gen AI system that will impact individuals’ rights and
            freedoms, employment, health care, or other democratic or judicial
            process that has not undergone bias or accuracy testing. And ensure
            that the testing process includes appropriate disclosures to facilitate

                                                                  watech.wa.gov 15

          independent review by members of the public or independent
          entities.

    By thoroughly evaluating these factors, the governmental entity can make
    informed decisions regarding the acquisition, development, and usage of
    Gen AI technology, prioritizing transparency, accountability, and public
    trust.
    Phase:
       • Requirements development.

•   Updated assessments: The evaluation of deployed Gen AI technology
    should be periodically reviewed and re-evaluated whenever there are
    subsequent modifications made to the Gen AI itself or to the data collection
    process (including new training data) that informs the model. These
    updates and reassessments must be conducted in a transparent manner,
    ensuring that the public is kept informed of any changes.

    Phase:
       • Ongoing monitoring.

•   Periodic testing: It is important to establish a process to regularly test the
    performance of the Gen AI while it is in use. This periodic testing aims to
    identify any indications of inaccuracies, biases, or unequal outcomes that
    may arise from the system, and should be conducted at intervals in
    proportion to the potential for risk. If such tendencies are detected, they
    should be promptly addressed, or if there are reasons for not addressing
    them, those reasons must be clearly explained in detail. The entire process
    and the subsequent testing results should be transparent and made
    available to the public. The establishment of a regular testing process,
    testing, and transparency of results ensures the fairness and accountability
    of the system's implementation by the government. For High-Risk Gen AI
    systems an independent third-party audit is highly recommended for
    periodic testing to ensure impartial review.

    Phase:
       • Ongoing monitoring.

•   Transparency of training data, inputs or outputs: While not always
    possible, it is encouraged that the training data, inputs, and outputs of the
    Gen AI systems be well understood by the agency. However, certain
    compelling reasons may exist to restrict the release, such as cases where

                                                                 watech.wa.gov 16

    there is a clear and demonstrable threat to governmental integrity or a
    significant risk that individuals may exploit the system, leading to a threat to
    governmental integrity or a significant cybersecurity risk. In situations where
    commercial or government interests justify the restriction of model training
    data, third-party evaluations should be conducted to assess the potential
    risks of inaccuracy or bias. It's important to note that while reviewing the
    training data is important, it cannot serve as a substitute for comprehensive
    testing to identify any inaccuracies or biases in the design and
    implementation of the Gen AI.

    Phase(s):
       • Requirements development.
       • Procurement, development, and deployment.
       • Ongoing monitoring.

•   Audit trails: The Gen AI should produce audit trails, logs, or hashes that
    document the inputs and outputs in its Gen AI process that are contained in
    system logs. This enables the governmental entity to furnish individuals with
    the rationale behind the Gen AI’s determinations and simplifies potential
    future scrutiny of those outputs. The recorded information should also be
    accessible to third-party researchers, granting them the opportunity to
    conduct impartial assessments of the system's accuracy and potential
    biases.

    Phase(s):
       • Requirements development.
       • Procurement, development, and deployment.
       • Ongoing monitoring requirements development.

•   Training to understand automation bias: Individuals engaged in the
    procurement, development, or operation of Gen AI should undergo
    training that explicitly addresses the concept of automation bias.
    Automation bias is an over-reliance on automated aids and decision
    support systems. As the availability of Gen AI outputs increases, it is a
    human tendency to rely on system outputs without question. Training on
    automation bias makes the workforce aware of these tendencies to mitigate
    against harmful or biased system outputs.

    Phase(s):
       • Requirements development.
       • Procurement, development, and deployment.
       • Ongoing monitoring.

                                                                  watech.wa.gov 17

•   Evaluation of risks/determination whether to proceed: Before
    deploying the Gen AI, and whenever there is a discovery of potential
    inaccuracies or biases, the governmental entity must assess whether the
    risks and impacts of such inaccuracies or biases on individuals and the
    potential erosion of public trust are significant enough to warrant not using
    the system. In making this determination, input from the individuals who
    will be impacted by the system should be considered along with other risks
    or harmful impacts that could emerge. The final decision should be clearly
    outlined in written form, transparent, and made available to the public.

    Phase(s):
       • Requirements development.
       • Procurement, development, and deployment.
       • Ongoing monitoring.

•   Review of decisions by those affected: Individuals impacted by a
    decision made or facilitated by a High-Risk Gen AI system should have the
    ability to examine and question the underlying foundation of that decision,
    especially in cases where the impacts to rights or responsibilities of
    individuals are significant. Part of the requirements development phase and
    development and procurement phase should include an evaluation of
    whether the Gen AI will be high risk and impact the rights and freedoms of
    individuals. If so, the ability to perform decision or output review should be
    part of those procurement phases as well as the ongoing monitoring phase
    for actual review. People should be made aware of any usage of a Gen AI
    system that affects them, should have the opportunity to opt-in or opt-out
    of the use of the Gen AI system, and should have clear channels through
    which to report issues or complaints.

    Phase(s):
       • Requirements development.
       • Procurement, development, and deployment.
       • Ongoing monitoring.

                                                                watech.wa.gov 18

•   Weighing advantages against known bias or inaccuracies: While
    acknowledging the significance of the benefits generated by Gen AI
    technology, it is essential to prioritize the prevention of harm to individuals
    caused by known or potential biases or inaccuracies. When weighing the
    advantages of benefits against the potential harm to natural persons, the
    avoidance of harm should be assigned considerably greater importance.

    Government organizations should assess the extent to which the acquisition
    and deployment of their Gen AI technology adheres to the Gen AI Guiding
    Principles and Washington State Privacy Principles. If it is discovered that
    the procurement, use, or deployment of a system fails to align with these
    principles, the governmental entity should identify the reasons for such
    non-alignment and take suitable actions to mitigate its uses based on the
    guiding principles.

    Phase(s):
       • Procurement, development, and deployment.
       • Ongoing monitoring.

Actions or controls to take for tasks
Each table below correlates to an activity described above. For each activity
there are actions or controls that agencies can take to mitigate risks and align
to the Washington State Agency Privacy Principles and AI Guiding Principles
for purposeful and responsible use of Gen AI technology. There may be
additional risks and principles addressed by controls agencies choose to
undertake with tasks, but the tables help identify predominant risks and
principles.
As Gen AI technologies are used, state agency staff should continue to work
with WaTech’s technology and privacy staff regarding implicated risk for the
state and its residents. Agency staff should complete and update its Gen AI
inventory to maintain a comprehensive record of Gen AI used throughout the
state. Appendix A lists additional sample questions to identify and assess the
Gen AI and its use to the agency in performing work for Washington.

                                                                  watech.wa.gov 19

 1. GENERATIVE AI INITIAL USE CASE ASSESSMENT FOR INTENTIONAL OR
                              INCIDENTAL GEN AI
Action or Control       Notes               Risk            Principles
                                            Addressed
What is the business    Has the agency      Lack of         Public purpose
need or problem         defined a clear     accountability and social
your agency is trying   purpose                             benefit
to solve?               addressable by
                        Gen AI
                        technology? Is it
                        the most
                        appropriate tool
                        for the solution?
Is this a high-risk use Consider risks to   Discrimination. Lawful, fair and
case?                   rights and          Lack of         responsible use.
                        freedoms to         explainability. Fairness,
                        individuals.        Threats to      inclusion, and
                        Is this a high-risk privacy.        non-
                        Gen AI system                       discrimination.
                        with potential                      Explainable and
                        impacts to critical                 interpretable.
                        infrastructure?                     Public purpose
                        Health? Safety?                     and social
                        Employment?                         benefit.
                        Democratic or
                        judicial process?
                        Biometric
                        identification or
                        verification?
                        Surveillance?
Consider the cost-                          Lack of         Due diligence.
benefit analysis of                         accountability. Accountability &
procuring,                                                  responsibility.
developing, or using
a Gen AI system.
Consider operational                        Lack of         Due diligence.
benefits of procuring,                      accountability. Accountability &
developing, or using                                        responsibility.
a Gen AI system.
Use Gen AI Initial Use                      Non-            Purpose
Case Assessment and                         transparency.   limitation.
Risk/Impact Matrix.                         Lack of         Accountability &
                                            accountability. responsibility.

                                                            watech.wa.gov 20

               2. EVALUATION OF WHETHER TO ADOPT SYSTEM
Action or       Notes                       Risk            Principles
Control                                     Addressed
Consider        Has the agency defined a Non-               Lawful, fair and
whether Gen clear purpose in using the transparency.        responsible Use
AI is able to   identified Gen AI system? Lack of           Purpose limitation.
address the                                 accountability. Transparency &
identified                                  Threats to      accountability.
problem or                                  legitimacy and Public purpose & social
issue.                                      public trust.   benefit. Safe, secure,
                                                            resilient.Fairness, inclusion,
                                                            and non-discrimination.
Consider        Has agency leadership       Non-            Lawful, fair and
whether         defined clear goals and     transparency.   responsible use.
there is        success criteria for        Lack of         Purpose limitation.
agency          adoption of the Gen AI      accountability. Transparency &
leadership      technology?                 Threats to      accountability.
support for                                 legitimacy and Public purpose & social
utilization of                              public trust.   benefit.
the Gen AI                                                  Safe, secure, resilient.
technology.                                                 Fairness, inclusion, and
                                                            non-discrimination.
                Have responsibilities of    Non-            Lawful, fair and
                agency staff involved in    transparency.   responsible use.
                adoption of Gen AI          Lack of         Purpose limitation.
                technology been             accountability. Transparency &
                delineated and              Threats to      accountability.
                communicated to:            legitimacy and Public purpose & social
                - Business staff.           public trust.   benefit.
                - Technical staff.
                - Executive/strategic level
                staff.
Consider        Differentiate between       Discrimination. Lawful, fair and
whether         technical and data          Inaccuracies.   responsible use.
there is        protection risks.           Lack of         Purpose limitation.
agency                                      accountability. Transparency &
leadership                                  Threats to      accountability.
support for                                 privacy.        Fairness, inclusion, and
utilization of                                              non-discrimination.
the Gen AI                                                  Privacy and data
technology.                                                 protection.
                                                            Transparency &
                                                            auditability.

                                                                       watech.wa.gov 21

               2. EVALUATION OF WHETHER TO ADOPT SYSTEM
  Action or    Notes                        Risk              Principles
   Control                                  Addressed
Consider the   Human worker                 Human-based       Transparency &
level of       involvement/interaction:     errors.           accountability.
agency         - Human worker-in-the-       Discrimination.   Valid and reliable.
human          loop (human decision-        Inaccuracies.     Safe, secure, resilient.
worker         making supports the          Non-              Fairness, inclusion, and
involvement    process).                    transparency.     non-discrimination.
in Gen AI      - Human worker-out-of-       Lack of
technology     the-loop (human              explainability.
used for       decision-making is not
decision-      part of the process).
making.        - Human worker-over-the-
               loop (human intervention
               may occur in the decision-
               making process).
               Factors to consider:         Human-based       Transparency &
               - Risk tolerance – what is   errors.           accountability.
               the risk tolerance of the    Discrimination.   Explainability &
               agency for human worker      Inaccuracies.     interpretable.
               involvement/interaction      Non-              Accountability &
               with Gen AI technology.      transparency.     responsibility.
               - Individual user-           Lack of
               experience – is the user-    explainability.
               experience enhanced or
               reduced by the
               involvement/interaction
               by a human worker in the
               Gen AI technology user
               flow.
               - Operational cost – what
               is the cost-benefit of a
               human worker
               involving/interacting with
               a Gen AI technology.

                                                                     watech.wa.gov 22

                        3. UPDATED ASSESSMENTS
Action or Control       Notes            Risk               Principles
                                         Addressed
Assess or re-evaluate   Factors to       Non-               Lawful, fair and
Gen AI if significant   consider:        transparency.      responsible use.
modifications are        - New training Lack of             Purpose
made to the model or        data         accountability.    limitation.
system.                  - Changes in    Threats to         Transparency &
                            model design legitimacy         accountability.
                         - New use       and public         Transparency &
                            case(s)      trust.             auditability.
                                                            Accountable &
                                                            responsible.

Assess or re-evaluate                     Non-          Lawful, fair and
Gen AI if subsequent                      transparency. responsible use.
changes are made to                       Lack of       Purpose
data collection                           accountability.
                                                        limitation.
process.                                  Threats to    Transparency &
                                          legitimacy    accountability.
                                          and public    Privacy and data
                                          trust.        protection.
                                                        Accountable &
                                                        responsible.
Assess or re-evaluate   Factors to      Non-            Lawful, fair and
Gen AI if significant   consider:       transparency. responsible use.
changes are made to     - New training Lack of          Purpose
training data that         data         accountability. limitation.
informs the model.      - Changes in    Threats to      Transparency &
                           model design legitimacy      accountability.
                        - New use       and public      Valid and
                           case(s)      trust.          reliable.
                                                        Accountability
                                                        and
                                                        responsibility.

                                                             watech.wa.gov 23

                                4. PERIODIC TESTING
Action or Control         Notes              Risk                Principles
                                             Addressed
Develop evaluation        Testing should be Lack of              Lawful, fair and
and testing plan for      proportionate to   accountability.     responsible use.
Gen AI technology.        potential risks of Non-                Accountability
                          the Gen AI         transparency.       and
                          technology.        Threats to          responsibility.
                                             legitimacy and
                                             public trust.
Create a process for      Process to include Automation          Lawful, fair, and
periodic testing.         how users or       bias.               responsible use.
                          public can flag    Inaccuracies.       Privacy and data
                          issues related to  Discrimination.     protection.
                          bias,                                  Valid and
                          discrimination, or                     reliable.
                          poor
                          performance.

Implement a plan and      Most likely to use   Automation        Due diligence.
use independent           independent third    bias.             Valid and
third-party to evaluate   parties for High-    Inaccuracies.     reliable.
risk.                     Risk Gen AI          Discrimination.   Privacy and data
                          systems.                               protection.

Publish results.                               Non-              Transparency &
                                               transparency.     accountability.
                                               Threats to        Transparency &
                                               legitimacy and    auditability.
                                               public trust.     Accountability
                                                                 and
                                                                 responsibility.

                                                                  watech.wa.gov 24

   5. TRANSPARENCY OF ALGORITHM, TRAINING DATA, INPUTS, or OUTPUTS
Action or Control     Notes                 Risk              Principles
                                            Addressed
Consider whether      If the agency         Discrimination.   Data minimization.
the Gen AI has a      needs to develop      Inaccuracies.     Purpose limitation.
data model            a data model for      Automation        Transparency &
developed or if the   evaluation,           bias.             accountability.
agency needs to       development           Non-              Transparency &
develop a data        and/or                transparency.     auditability.
model with agency     procurement of        Lack of           Valid and reliable.
data.                 the Gen AI system,    explainability.   Explainable &
                      utilize the agency                      interpretable.
                      designated data
                      scientist and/or
                      liaise with the
                      WaTech office for
                      guidance.
Consider whether      If the data model     Threat to         Data minimization.
the Gen AI has a      exists, does it       privacy.          Purpose limitation.
data model            conform to the                          Transparency &
developed or if the   Washington State                        accountability.
agency needs to       Agency Privacy                          Privacy and data
develop a data        Principles and the                      protection.
model with agency     Gen AI Guiding
data.                 Principles?

Consider whether      If individual or      Discrimination.   Data minimization.
the Gen AI has a      client data is used   Inaccuracies.     Purpose limitation.
data model            to develop data       Automation        Transparency &
developed or if the   model, did the        bias.             accountability.
agency needs to       agency review the     Non-              Privacy and data
develop a data        responses to          transparency.     protection.
model with agency     minimize false,       Lack of           Safe, secure, and
data.                 misleading or         explainability.   resilient.
                      inaccurate
                      responses?

                                                                watech.wa.gov 25

  5. TRANSPARENCY OF ALGORITHM, TRAINING DATA, INPUTS, or OUTPUTS

Action or Control        Notes                  Risk            Principles
                                                Addressed
Consider relevant      Have features or       Threats to       Lawful, fair and
features or            functionalities that   legitimacy and   responsible use.
functionalities that   will improve trust     public trust.    Data minimization.
have greatest          with the agency                         Purpose limitation.
impact on the          been identified?                        Accountability &
agency client or                                               responsibility.
customers affected
by the Gen AI
technology.
Consider relevant      Have features or       Threats to       Lawful, fair and
features or            functionalities that   legitimacy and   responsible use.
functionalities that   will reduce            public trust.    Data minimization.
have greatest          trust/harm                              Purpose limitation.
impact on the          reputation of the                       Fairness, inclusion,
agency clients or      agency been                             and non-
customers affected     identified?                             discrimination.
by the Gen AI
technology. (cont.)
Has the algorithm,                       Inaccuracies.         Transparency &
inputs and outputs                       Non-                  accountability.
of the Gen AI been                       transparency.         Valid and reliable.
assessed as valid                        Lack of               Transparency &
by an independent                        explainability.       auditability.
third-party?                             Lack of
                                         accountability.
Can the agency         Can reports be    Non-                  Transparency &
describe in “plain     generated by      transparency.         accountability.
English” how the       providing detail  Lack of               Individual
production version     on the            explainability.       participation.
of the Gen AI          explainability of Lack of               Explainable &
technology makes       Gen AI technology accountability.       interpretable.
decisions or           features and
generates outputs?     functionalities.

                                                                  watech.wa.gov 26

     5. TRANSPARENCY OF ALGORITHM, TRAINING DATA, INPUTS, or OUTPUTS

Action or Control      Notes               Risk              Principles
                                           Addressed
                     Consider formally Non-                 Transparency &
                     documenting and transparency.          accountability.
                     publishing an FAQ Lack of              Individual
                     about the Gen AI    explainability.    participation.
                     technology,         Lack of            Explainable &
                     including           accountability.    interpretable.
                     operational details Threats to
                     of the generating   legitimacy and
                     or decision-        public trust.
                     making model.

Can the agency       Document             Discrimination.   Transparency &
describe in “plain   potential            Inaccuracies.     accountability.
English” how the     limitations and      Automation        Accountable and
production version   gaps of the Gen AI   bias.             responsible.
of the Gen AI        technology           Non-              Transparency &
technology makes     generating or        transparency.     auditability.
decisions or         decision-making      Lack of
generates outputs?   model.               explainability.
(cont.)

                                                              watech.wa.gov 27

 5.   TRANSPARENCY OF ALGORITHM, TRAINING DATA, INPUTS, or OUTPUTS

Action or Control       Notes                 Risk            Principles
                                              Addressed
If certain features or Hold forums for     Lack of           Transparency &
functions of the       public or customer accountability.    Accountability.
Gen AI technology feedback.                Threats to        Individual
or model cannot be                         legitimacy and    participation.
explained in “plain                        public trust.     Transparency &
English,” consider                                           auditability.
conducting                                                   Fairness, inclusion,
additional tests in                                          and non-
pre-production                                               discrimination.
environments and       Work with           Human-based       Transparency &
additional user-       technical staff to  errors.           accountability.
acceptance tests       define different    Discrimination.   Fairness, inclusion,
with clients or        models of           Inaccuracies.     and non-
customers.             production          Automation        discrimination.
                       implementation      bias.             Valid and reliable.
                       for testing against Lack of
                       various customer    explainability.
                       subpopulations
                       against defined
                       success criteria.
Consider updating Link to a                Non-              Transparency &
agency privacy         developed FAQ.      transparency.     Accountability.
policy with                                Lack of           Individual
information                                accountability.   participation.
regarding use of                           Threats to        Transparency &
Gen AI systems,                            privacy.          auditability.
including                                                    Explainable and
information                                                  interpretable.
collected and
processed, and
how decisions are
made.

                                                                watech.wa.gov 28

 5.   TRANSPARENCY OF ALGORITHM, TRAINING DATA, INPUTS, or OUTPUTS

Action or Control        Notes                   Risk            Principles
                                                 Addressed
                       Consider               Non-              Transparency &
                       providing a just-in-   transparency.     accountability.
                       time notice for        Lack of           Individual
                       individuals            accountability.   participation.
                       regarding the use      Threats to        Accountable and
                       of Gen AI              privacy.          responsible.
                       technology (e.g.
                       chatbots).
Consider providing     See outline of         Non-              Transparency &
notice of intent for   process in RCW         transparency.     accountability.
use of High-Risk       43.386 re Facial       Lack of           Individual
Gen AI technology      Recognition for        accountability.   participation.
to public before       example.               Threats to        Accountable and
procurement,                                  privacy           responsible.
deployment, or
use.
Consider updating      Refer to DSA           Non-              Transparency &
data sharing           implementation         transparency.     accountability.
agreements (DSAs)      guidance.              Lack of           Due diligence.
if Gen AI systems                             accountability.   Privacy and data
are used in the                               Threats to        protection.
business-to-                                  privacy.
business                                      Threats to
relationship.                                 legitimacy and
                                              public trust.

                                                                  watech.wa.gov 29

                            6. AUDIT TRAILS
Action or Control   Notes                 Risk                 Principles
                                          Addressed
Consider            Consider              Non-                 Due diligence.
establishing a      documenting factors transparency.          Transparency &
knowledge           in making decision to Lack of              auditability.
management          develop, procure, or accountability.
repository/database use a Gen AI system. Threats to
to record/archive                         legitimacy and
relevant documents                        public trust.
regarding
developing,
procuring, or using
Gen AI technology.
Formally document Consider setting        Inaccuracies.        Transparency &
change              cadence of change     Non-                 accountability.
management          management            transparency.        Security.
program for Gen AI meetings for Gen AI Lack of                 Safe, secure,
technology.         technology.           explainability.      and resilient.
                                          Lack of              Accountability
                                          accountability.      and
                                                               responsibility.
                     Include assessment      Inaccuracies.     Transparency &
                     of implicated privacy   Non-              accountability.
                     risk per changes in     transparency.     Security.
                     change                  Lack of           Accountability
                     management              explainability.   and
                     program.                Lack of           responsibility.
                     Coordinate with         accountability.   Privacy and data
                     WaTech.                                   protection.

                                                               watech.wa.gov 30

                                 6. AUDIT TRAILS
Action or Control        Notes                    Risk              Principles
                                                  Addressed

Establish tracking                                Discrimination.   Lawful, fair and
and monitoring of                                 Automation.       responsible use.
role-based privacy-                               Bias.             Transparency &
relevant training on                              Lack of           accountability.
automation bias                                   explainability.   Fairness,
and additional                                    Threats to        inclusion, and
relevant data                                     privacy.          non-
protection                                        Threats to        discrimination.
implications of                                   legitimacy and    Accountability
using Gen AI.                                     public trust.     and
                                                                    responsibility.
If the Gen AI            Consider                 Inaccuracies.     Lawful, fair and
technology fails or      implications to          Automation.       responsible use.
flags a failure or       business continuity      Bias.             Transparency &
discrepancy in the       plan.                    Lack of           accountability.
decision/projected                                explainability.   Security.
answer, is there a                                                  Valid and
pre-determined                                                      reliable.
threshold?
Consider how staff
workers will be
notified of this prior
to a decision being
made by the high
risk Gen AI system.
Consider                 Use feedback from        Lack of           Individual
developing               clients or customers     accountability.   participation.
formalized               early in the             Threats to        Public purpose
feedback loop with       development &            legitimacy and    and social
affected clients or      procurement cycle to     public trust.     benefit.
customers.               support identification                     Fairness,
                         of success criteria.                       inclusion, and
                                                                    non-
                                                                    discrimination.
                                                                    Accountability
                                                                    and
                                                                    responsibility.

                                                                    watech.wa.gov 31

                             6. AUDIT TRAILS
Action or Control    Notes               Risk           Principles
                                         Addressed
                    Review risk         Lack of          Individual
                    reduction/          accountability. participation.
                    acceptance of       Threats to       Accountability
                    feedback throughout legitimacy and and
                    development &       public trust.    responsibility.
                    procurement cycle.
                    Document closed     Lack of          Individual
                    feedback loop;      accountability. participation.
                    document report for Threats to       Fairness,
                    publication.        legitimacy and inclusion, and
                                        public trust.    non-
                                                         discrimination.
                                                         Accountability
                                                         and
                                                         responsibility.

                                                          watech.wa.gov 32

                7.TRAINING TO UNDERSTAND AUTOMATION BIAS
Action or Control      Notes         Risk            Principles
                                     Addressed
Consider whether                     Discrimination. Lawful, fair and
agency staff involved                Inaccuracies.   responsible use.
in the development,                  Automation      Purpose
procurement, or use                  bias.           limitation.
of Gen AI technology                 Lack of         Transparency &
have been trained on                 accountability. accountability.
automation bias.                                     Fairness,
                                                     inclusion, and
                                                     non-
                                                     discrimination.
                                                     Accountability
                                                     and responsibility.

Consider whether                              Lack of           Lawful, fair and
agency staff involved                         accountability.   responsible use.
in the development,                           Threats to        Purpose
procurement, or use                           privacy.          limitation.
of Gen AI                                                       Transparency &
technologies have                                               accountability.
training on                                                     Privacy and data
Washington State                                                protection.
Agency Privacy
Principles and
responsible use of
Gen AI.
Consider designating      Alternatively,      Human-based       Lawful, fair and
a specialized role with   consider            errors.           responsible use.
specific                  formalizing         Inaccuracies.     Purpose
responsibilities          liaison             Lack of           limitation.
regarding ethical and     relationship with   explainability.   Transparency &
data protection issues    WaTech for such                       accountability.
of utilizing high risk    guidance.                             Fairness,
Gen AI systems within                                           inclusion, and
agency.                                                         non-
                                                                discrimination.
                                                                Accountability
                                                                and responsibility.

                                                                  watech.wa.gov 33

       8. EVALUATION OF RISKS/DETERMINATION WHETHER TO PROCEED
Action or Control       Notes                           Risk              Principles
                                                        Addressed
Consider whether        Is there a sand-box,            Inaccuracies.     Lawful, fair and
agency has ability to   development, testing or         Non-              responsible
test Gen AI systems     QA environment that can         transparency.     use.
before procurement      be used to test                 Lack of           Transparency &
or deployment.          implementation/integration      explainability.   accountability.
                        of Gen AI technology prior                        Safe, secure,
                        to production.                                    and resilient.
                                                                          Valid and
                                                                          reliable.
                        Is there an agreed-upon         Inaccuracies.     Lawful, fair and
                        requirements and/or             Non-              responsible
                        punch list that the Gen AI      transparency.     use.
                        technology should satisfy       Lack of           Transparency &
                        before moving to                explainability.   accountability.
                        production?                                       Safe, secure,
                                                                          and resilient.
                                                                          Valid and
                                                                          reliable.
Conduct risk            Consider the following          Human-based       Lawful, fair and
assessments.            types of assessments:           errors.           responsible
                        -Gen AI Initial Use Case        Discrimination.   use.
                        Assessment (See Appendix        Automation        Transparency &
                        B).                             bias.             accountability.
                        - AI Risk Threshold Analysis.   Non-              Safe, secure,
                        - AI Risk Impact                transparency.     and resilient.
                        Assessment.                     Lack of           Valid and
                        -Algorithmic Impact             explainability.   reliable.
                        Assessment                      Lack of           Privacy and
                                                        accountability.   data protection.
                                                        Threats to        Accountability
                                                        privacy.          and
                                                                          responsibility.

                                                                   watech.wa.gov 34

      8. EVALUATION OF RISKS/DETERMINATION WHETHER TO PROCEED
Action or Control          Notes                         Risk              Principles
                                                         Addressed
Consider                  Consider risks to rights and   Discrimination.   Lawful, fair and
identification of risks   freedoms to individuals.       Lack of           responsible
to clients or             Is this a High-Risk Gen AI     explainability.   use.
customers if the Gen      system with potential          Threats to        Fairness,
AI technology is          impacts to critical            privacy.          inclusion, and
deployed.                 infrastructure? Health?                          non-
                          Safety? Employment?                              discrimination.
                          Democratic or judicial                           Explainable
                          process? Biometric                               and
                          identification or                                interpretable.
                          verification? Surveillance?                      Public purpose
                                                                           and social
                                                                           benefit.

Can identified risks Determine a review period           Lack of           Lawful, fair and
be accepted,         for reassessment.                   accountability.   responsible
reduced, mitigated                                                         use.
or remediated by the                                                       Transparency &
agency in                                                                  accountability.
accordance with                                                            Safe, secure,
defined success                                                            and resilient.
criteria?

                          Determine key                  Lack of           Lawful, fair and
                          performance indicators or      accountability.   responsible
                          a cadence of review of                           use.
                          success criteria for                             Transparency &
                          deployment of Gen AI                             accountability.
                          technology in production.                        Safe, secure,
                                                                           and resilient.
                                                                           Valid and
                                                                           reliable.

                                                                   watech.wa.gov 35

     8. EVALUATION OF RISKS/DETERMINATION WHETHER TO PROCEED

Action or Control      Notes                           Risk              Principles
                                                       Addressed
                       Determine tracking and    Lack of                 Lawful, fair and
                       monitoring mechanisms for accountability.         responsible
                       managing risks and                                use.
                       success criteria.                                 Transparency &
                                                                         accountability.
                                                                         Safe, secure,
                                                                         and resilient.
                       Consider updating Incident      Lack of           Lawful, fair and
                       Response Plan, Business         explainability.   responsible
                       Continuity Plan and             Lack of           use.
                       Disaster Recovery Plan          accountability.   Transparency &
                       given certain safety and                          accountability.
                       operational features of Gen                       Security.
                       AI technology. Consider                           Safe, secure,
                       whether back-up systems                           and resilient.
                       or datasets need to be                            Valid and
                       generated/configured if                           reliable.
                       the Gen AI technology fails
                       or causes intolerable risk.
                       Are necessary agency staff
                       able to revert all control to
                       human worker decision-
                       making as needed?

Can the integrity of   Does the Gen AI system          Human-based       Lawful, fair and
decisions made or      flag or notify state agency     errors.           responsible
content produced by    workers of uncertainty in       Discrimination.   use.
High-Risk Gen AI       the answer/projected            Inaccuracies.     Purpose
systems or integrity   response to a series of data    Automation        limitation.
of outputs be          or information?                 bias.             Transparency &
confirmed or                                           Non-              accountability.
reviewed by state                                      transparency.     Explainable
agency workers?                                        Lack of           and
                                                       explainability.   interpretable.
                                                                         Transparency &
                                                                         auditability.

                                                                 watech.wa.gov 36

      8. EVALUATION OF RISKS/DETERMINATION WHETHER TO PROCEED

Action or Control      Notes                          Risk              Principles
                                                      Addressed
                       Does the Gen AI                Human-based       Lawful, fair and
                       technology permit the state    errors.           responsible
                       agency worker to override      Discrimination.   use.
                       or manipulate the output or    Inaccuracies.     Purpose
                       generated response?            Automation        limitation.
                                                      bias.             Transparency &
                                                      Non-              accountability.
                                                      transparency.     Safe, secure,
                                                      Lack of           and resilient.
                                                      explainability.   Accountability
                                                                        and
                                                                        responsibility.

Consider whether       If unsure, consider piloting   Human-based       Lawful, fair and
the testing            a proof-of-concept release     errors.           responsible
environment            of the Gen AI technology       Discrimination.   use.
accurately reflects    with production datasets to    Inaccuracies.     Purpose
the real-life          evaluate decisions-made or     Automation        limitation.
production             outputs by Gen AI              bias.             Transparency &
environment,           technology for validity and    Non-              accountability.
including the client   success.                       transparency.     Valid and
or customer                                           Lack of           reliable.
datasets.                                             explainability.

                                                                watech.wa.gov 37

     8. EVALUATION OF RISKS/DETERMINATION WHETHER TO PROCEED
Action or Control     Notes                       Risk              Principles
                                                  Addressed
Are clients or       What alternatives are        Discrimination.   Lawful, fair and
customers able to    available to clients or      Inaccuracies.     responsible
opt-out of           customers if they opt-out?   Non-              use.
participation in the                              transparency.     Purpose
High-Risk Gen AI                                  Lack of           limitation.
system and still                                  accountability.   Transparency &
obtain                                            Threats to        accountability.
benefits/services                                 privacy.          Privacy and
offered/administered                              Threats to        data protection.
by the agency?                                    legitimacy and    Fairness,
                                                  public trust.     inclusion, and
                                                                    non-
                                                                    discrimination.
                      Consider notification of    Threats to        Lawful, fair and
                      opt-out implications.       privacy.          responsible
                                                  Threats to        use.
                                                  legitimacy and    Purpose
                                                  public trust.     limitation.
                                                                    Transparency &
                                                                    accountability.
                                                                    Privacy and
                                                                    data protection.
                                                                    Fairness,
                                                                    inclusion, and
                                                                    non-
                                                                    discrimination.

                                                            watech.wa.gov 38

                 9. REVIEW OF DECISIONS BY THOSE AFFECTED
Action or            Notes            Risk            Principles
Control                               Addressed
Has the agency                        Discrimination. Lawful, fair and
identified the                        Lack of         responsible use.
populations that                      accountability. Privacy and data
will be involved                      Threats to      protection.
with and/or                           privacy.        Fairness, inclusion,
impacted by the                       Threats to      and Non-
deployment of                         legitimacy and discrimination.
the High-Risk Gen                     public trust.   Public purpose
AI system?                                            and social benefit.

Consider                                Discrimination.   Individual
assessing risk of                       Lack of           participation.
those affected at                       accountability.   Fairness, inclusion,
population-level                        Threats to        and non-
by conducting                           privacy.          discrimination.
user-testing.                           Threats to        Public purpose
                                        legitimacy and    and social benefit.
                                        public trust.
Consider                                Human-based       Lawful, fair and
implications of                         errors.           responsible use.
known                                   Discrimination.   Fairness, inclusion,
vulnerabilities of                      Inaccuracies.     and Non-
target                                  Threats to        discrimination.
populations.                            privacy.          Public purpose
                                        Threats to        and social benefit.
                                        legitimacy and
                                        public trust.

                                                            watech.wa.gov 39

             9. REVIEW OF DECISIONS BY THOSE AFFECTED
Action or Control      Notes                 Risk             Principles
                                             Addressed
Consider formally   Include different      Non-              Lawful, fair and
documenting and     components of the      transparency.     responsible use.
publishing an       FAQ:                   Lack of           Transparency &
FAQ about the       - Dataset              accountability.   accountability.
High-Risk Gen AI    information.           Threats to        Individual
system, including   - Model information.   legitimacy and    participation.
operational         - Human                public trust.     Transparency and
details of the      involvement in the                       auditability.
decision-making     High-Risk Gen AI
model.              system.
                     - Inferences and
                    projections of the
                    High-Risk Gen AI
                    system.
                    - Impact of
                    decisions-made by
                    the High-Risk Gen AI
                    system.
                    - Ability to appeal
                    decisions-made by
                    the High-Risk Gen AI
                    system.
Consider                                   Non-              Transparency &
publishing                                 transparency.     accountability.
outcomes of                                Lack of           Individual
evaluation to                              accountability.   participation.
procure or                                 Threats to        Accountability and
deployment of                              legitimacy and    responsibility.
High-Risk Gen AI                           public trust.     Transparency and
system.                                                      auditability.

                                                               watech.wa.gov 40

              9. REVIEW OF DECISIONS BY THOSE AFFECTED
Action or Control      Notes                Risk             Principles
                                            Addressed
Consider whether Consult with             Non-              Transparency &
the agency       WaTech.                  transparency.     accountability.
should have a                             Lack of           Individual
policy about                              accountability.   participation.
publishing a                              Threats to        Accountability and
report on agency                          legitimacy and    responsibility.
development &                             public trust.
procurement,
deployment or
use of High-Risk
Gen AI system.

Did the agency      Consider              Discrimination.   Data minimization.
address usability   developing            Lack of           Purpose limitation.
problems and        formalized feedback   accountability.   Transparency &
test whether user   loop with affected    Threats to        accountability.
interfaces served   populations.          privacy.          Individual
intended                                  Threats to        participation.
purposes?           Consult target        legitimacy and    Public purpose
                    population to further public trust.     and social benefit.
                    understand                              Valid and reliable.
                    potential or known
                    vulnerabilities.

                                                              watech.wa.gov 41

             9. REVIEW OF DECISIONS BY THOSE AFFECTED

Action or Control      Notes              Risk                Principles
                                          Addressed
Consider formal     Designate           Non-                 Transparency &
feedback channel    appropriate         transparency.        Accountability.
on impact or for    workforce personnel Lack of              Individual
questions           to manage the       accountability.      participation.
regarding High-     feedback channel.   Threats to           Public purpose
Risk Gen AI                             legitimacy and       and social benefit.
systems from                            public trust.        Fairness, inclusion,
both internal and                                            and Non-
external                                                     discrimination.
participants.       Formalize how          Non-              Transparency &
                    feedback will be       transparency.     Accountability.
                    ingested and           Lack of           Individual
                    considered by          accountability.   participation.
                    executive sponsors.    Threats to        Safe, secure, and
                                           privacy.          resilient.
                    Formalize how          Threats to        Valid and reliable.
                    feedback will be       legitimacy and    Fairness, inclusion,
                    utilized for ongoing   public trust.     and non-
                    review of High-Risk                      discrimination.
                    Gen AI system use.

Consider redress    Clarify redress for    Non-              Transparency &
process for         updating/correcting    transparency.     accountability.
individuals         client or customer     Lack of           Individual
regarding           data used in by        accountability.   participation.
decisions made      High-Risk Gen AI       Threats to        Fairness, inclusion,
about them by       System and/or the      legitimacy and    and non-
the High-Risk Gen   outcome/decisions      public trust.     discrimination.
AI system.          made by the High-
                    Risk Gen AI
                    regarding the
                    individual.

                                                               watech.wa.gov 42

      10. WEIGHING ADVANTAGES AGAINST KNOWN BIAS OR INACCURACIES
Action or            Notes                  Risk              Principles
Control                                     Addressed
Does the agency      Did the agency         Discrimination.   Lawful, fair and
staff have insight   account for            Automation        responsible use.
into the             unintended biases of   bias.             Data minimization.
model/dataset        the dataset through    Non-              Purpose limitation.
used for the Gen     mitigation/remediation transparency.     Transparency &
AI technology?       actions?               Lack of           accountability.
                                            explainability.   Explainable and
                                            Lack of           interpretable.
                                            accountability.   Transparency and
                                            Threats to        auditability.
                                            privacy.
                     Liaise with the agency Discrimination.   Lawful, fair and
                     data scientist and/or  Automation        responsible use.
                     WaTech to evaluate     bias.             Data minimization.
                     potential bias of data Non-              Purpose limitation.
                     model and/or dataset transparency.       Transparency &
                     of Gen AI model.       Lack of           accountability.
                                            explainability.   Fairness, inclusion, and
                                            Lack of           non-discrimination.
                                            accountability.
                                            Threats to
                                            privacy.
Consider             Identify and document Discrimination.    Lawful, fair and
perception of        perceived risk.        Inaccuracies.     responsible use.
risk of identified                          Automation        Data minimization.
Gen AI               Document risk          bias              Purpose limitation.
technology by        reduction strategies.  Non-              Transparency &
target                                      transparency.     accountability.
population or        Determine whether      Lack of           Fairness, inclusion, and
subpopulation.       agency should accept, explainability.    non-discrimination.
                     reduce, mitigate or    Lack of           Accountability and
                     remediate risks if     accountability.   responsibility.
                     development, r         Threats to
                     procurement,           privacy.
                     deployment, or use of
                     Gen AI technology
                     continues.

                                                                     watech.wa.gov 43

Appendix A
Sample Gen AI procurement questionnaire
   1. What is the Gen AI Technology name, vendor and version?
           a. Gen AI Model Name, LLM Version (including number of parameters)
               and list ALL model names/owners for the solution or offering.
                     i. Include the unique identifier or name assigned to the
                        specific Gen AI model or service.
                    ii. Identifiers should allow users to refer to and distinguish
                        between different Gen AI models.
   2. List Gen AI powered, or AI driven applications and/or product owners.
           a. Answer should include the name of the organization or entity
               responsible for creating or deploying the Gen AI model or service.
           b. Answer should help identify the source and accountability for the
               Gen AI system or technology.
   3. Describe the product.
           a. Provide a concise summary of the Gen AI model’s purpose,
               functionality, and key characteristics including model architecture,
               capabilities, and limitations.
           b. Provide a high-level understanding for users and government
               customers.
   4. What are the Use Case(s) for the Gen AI technology?
           a. Describe the intended use or goal of the Gen AI model (e.g. image
               recognition, natural language processing, text summarization, data
               analysis)
   5. What is the context, subject matter, or domain for which the Gen AI model
       is designed to operate effectively?
           a. Answer should help user determine if the Gen AI model is suitable
               for their specific use case.
           b. What data is the model trained on and what data will be input into
               the system when in use?
   6. What decisions or outputs is the system utilized to make?
   7. How is the input data gathered, how often is it updated, and are subjective
       inputs ever audited for consistency across data collectors?
   8. Is the training data or decision or output algorithm available for
       examination by the agency and/or the public?
   9. Has there been any public or community engagement used in selection or
       design of the system? If so, please describe this engagement.
   10. Does law or regulation mandate any of the decision system criteria? If so,
       which criteria?
   11. What quality control is in place to test and monitor for potential bias?
   12. What performance metrics were selected to determine the models’
       effectives? What is the model optimizing for, and under what constraints?

                                                                watech.wa.gov 44

        13. Do the system’s decisions intentionally differentially affect members of
            protected classes1, such as selecting persons with disabilities for certain
            benefits?
        14. Has the system been tested for unintended bias by the agency or an
            independent third party? If so, what were the results? Describe briefly the
            nature of the testing.
        15. Has the system been tested for misuse potential, including for the
            production of non-consensual intimate imagery, child sexual abuse
            material, hateful or harmful content, offensive cyber capabilities, or other
            types of misuse? If so, what were the results? Describe briefly the nature of
            the testing.
        16. Has the Gen AI technology produced known erroneous results and if so,
            what were those errors (including the results of any audits conducted to
            check for erroneous results)?
        17. How are the outcomes of the Gen AI system explained to subject matter
            experts, users, impacted individuals, others?
        18. In addition to any intentional differential effect on members of a protected
            class, are there other differential effects on protected classes as shown by
            comparison of the system’s data to general census data or, where relevant,
            subpopulation data, such as the effect on justice system defendants of
            color as contrasted with all defendants? If audits have been performed to
            determine such differential effects, what were the results of those audits?
        19. Can those affected by a High-Risk Gen AI system decision review and
            challenge the basis for that decision? If so, how, and what were the results
            of any such challenges?
        20. Is the high-risk Gen AI system operated by a third party? If so, what rules
            govern such operation and what audits are conducted to ensure
            compliance?
        21. What is the fiscal impact of the system, including initial cost, operating
            costs, and any cost savings established as flowing from use of the system?

1
 A protected class is a group of people who are protected from discrimination based on a
shared characteristic. These characteristics include race, color, religion, sex (which includes
pregnancy, sexual orientation, and gender identity), national origin, age, disability, and genetic
information (including family medical history).

                                                                             watech.wa.gov 45

Appendix B
Sample Gen AI initial use case assessment
Below is a method to identify and assess whether your use case is appropriate
for Gen AI technology and whether it is high-risk. Business needs or problems
to be assessed should be explained along with context information such as a
cost-benefit analysis, anticipated operational impacts, description of use case
or decisions being made, the approximate size of impacted population, and
the need or advantages of the Gen AI technology.

 Issue                       Question
 Identify business need or   What is the business need or problem your agency is
 problem                     trying to solve?
 Describe use case           What is the intended use or goal of the Gen AI model
                             (e.g. image recognition, natural language processing,
                             text summarization, data analysis)?

 Cost-benefit analysis       What is the cost-benefit analysis of procuring,
                             developing, or using a Gen AI system?
 Operational benefits        What are the operational benefits of procuring,
                             developing, or using a Gen AI system?
 Effect on individuals       What is impact on individual rights and freedoms?
 Risk of bias or errors      What is the data or training data involved in the
                             Gen AI technology? Risk of harmful effects of bias
                             content? Is there a perpetuation of stereotypes?
 Complexity                  What is Gen AI model generating or predicting?
                             What are the anticipated outputs?
 High-risk                   Does the Gen AI system have potential impacts to
                             critical infrastructure? Health? Safety?
                             Employment? Democratic or judicial process?
                             Biometric identification or verification? Perform
                             surveillance?

To determine risk for further review and assessment, agencies should evaluate
the following:
Effect on people
   •     Low: Gen AI technology does not impact legal rights or the provision of
         services or scrutiny that could lead to an impact on legal rights or
         services.

                                                                  watech.wa.gov 46

   •   Moderate: Gen AI technology impacts processing, relatively minor
       services or legal rights or financial impacts on individuals. Small number
       of impacted individuals.

   •   High: Gen AI technology can have a significant impact on the provision
       of services, financial impact, or legal rights. Large number of impacted
       clients.

Likelihood of bias or errors
   •   Low: Gen AI technology directly follows federal or state regulations or
       follows adopted policy or rule.
   •   Moderate: Gen AI technology developed with disclosure of information
       used and the model has been tested for bias and inaccuracy.
   •   High: Gen AI technology developed without disclosure of information
       used or the model inputs, training data or outputs created and has not
       been tested for bias or accuracy.

Complexity
   •   Low: Simple model or decision rule.
   •   Moderate: Simple calculation of existing data elements (i.e., a weighted
       average).
   •   High: Complex predictive modeling, deep learning, etc.

Matrixes could be used to determine a rating such as:
                        Low impact     Moderate Impact    High Impact
 Low likelihood               5              4                  4
 Moderate likelihood          4              3                  3
 High likelihood              4              2                  1

Risk and complexity rating can be used to determine the type of review, for
example:
   •   Low: Generative AI questionnaire.
   •   Moderate: AI risk analysis or formal outcome analysis.
   •   High: Gen AI impact assessment by professional or third party.

                                                                watech.wa.gov 47

Generative AI Technology Evolution
WaTech acknowledges that the field of generative artificial intelligence is
rapidly evolving.
The guidance provided serves as a tool for agencies, drawing from the
recommendations outlined in the White House's Blueprint for an Al Bill of
Rights and the National Institute for Science and Technology's (NIST) Al Risk
Management Framework and other work the state has undertaken in regard to
automated decision systems. It is rooted in a foundation of guiding principles,
providing a framework for agencies to navigate the complex landscape of
generative AI technology. It is important to recognize that this guidance will
evolve over time, reflecting the advancements and changing landscape of
technology and governance. While it is to be used as a best practice, it should
not serve as a substitute for regulations or agency policies that may be in
place. Instead, it should be adopted in alignment with other relevant resources
and tools, ensuring a comprehensive and well-rounded approach to
addressing the challenges and opportunities presented by generative artificial
intelligence.

Contact
Questions regarding this document can be directed to:
Washington Technology Solutions
ai@watech.wa.gov

                                                                watech.wa.gov 48

References
Executive Order 24-01 on Artificial Intelligence Section 3. requiring this deliverable
reads as follows:

By September 2024, WaTech, in collaboration with the Department of Enterprise
Services (DES), shall issue initial guidelines for public sector procurement, uses, and
ongoing monitoring of the use of generative AI technology. The guidelines should
build on guidance from the White House's Blueprint for an Al Bill of Rights and the
National Institute for Science and Technology's Al Risk Management Framework and
address safety and effectiveness, algorithmic discrimination, data privacy, and
cybersecurity. These guidelines shall include a requirement that any vendor providing
a High-Risk Generative AI System to an agency certify that the vendor has implemented
an AI governance program consistent with the National Institute of Standards and
Technology Artificial Intelligence Risk Management Framework. WaTech and DES shall
make the guidelines publicly available via posting on relevant agencies’ websites.

References and materials used to develop this document include the following:

   •   White House AI Bill of Rights Intro: https://www.whitehouse.gov/ostp/ai-bill-
       of-rights/
   •   White House AI Bill of Rights: https://www.whitehouse.gov/wp-
       content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf
   •   NIST AI RMF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
   •   NIST AI RMF: Gen AI: https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-
       Profile.ipd.pdf
   •   CA Gen AI Guidelines for Public Sector: https://cdt.ca.gov/wp-
       content/uploads/2024/03/3a-GenAI-Guidelines.pdf
   •   CA Gen AI Fact Sheet:
       https://www.documents.dgs.ca.gov/dgs/fmc/pdf/std1000.pdf
   •   Canada ADS Directive: https://www.tbs-sct.canada.ca/pol/doc-
       eng.aspx?id=32592
   •   World Economic Forum – AI Government Procurement Guidelines:
       https://www3.weforum.org/docs/WEF_AI_Procurement_in_a_Box_AI_G
       overnment_Procurement_Guidelines_2020.pdf
   •   World Economic Forum - AI Procurement in a Box Toolkit:
       https://www3.weforum.org/docs/WEF_AI_Procurement_in_a_Box_Work
       book_2020.pdf
   •   AI Institute Algorithmic Impact Assessment Report:
       https://ainowinstitute.org/publication/algorithmic-impact-assessments-
       report-2

                                                                      watech.wa.gov 49

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
