---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-genai
title: GenAI Policy
doc_type: policy
citation: MaineIT GenAI Policy
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/GenAIPolicy.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 54a1af5c2e58af7d834d8f5d79270c1325906a27f757a2d35262a23289c8d627
effective_date: null
source_version: 'Latest Revision Date: October 30, 2026'
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
- governance
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# GenAI Policy (MaineIT GenAI Policy)

## At a glance

The State's policy on generative AI: Guiding Principles and Directives for responsible, transparent and ethical use of GenAI within the Executive Branch of Maine State Government. The principal AI instrument binding Maine agencies.

## Full text

                          Generative Artificial Intelligence Policy

                                Maine State Government
                  Department of Administrative and Financial Services
                        Office of Information Technology (OIT)

                  Generative Artificial Intelligence (GenAI) Policy

1.0.    Statement
1.1.    The purpose of this policy is to specify Guiding Principles and Directives for
        responsible, transparent, and ethical use of GenAI within the Executive Branch of
        Maine State Government.

1.2.    The rapid rise in GenAI technologies has been widely acknowledged as
        unprecedented. It holds significant potential for enhancing state government
        efficiency through automation, data analysis, streamlining processes, and optimizing
        resource allocation. By harnessing its potential, agencies can more efficiently
        identify areas of cost-saving measures and greatly enhance citizen services.
        However, the risks to privacy, security, the State’s workforce, safety, government
        accountability, and fundamental human rights are just beginning to be understood.
        Many of these tools lack transparency in their design, making it challenging to
        assess the risks involved with their use. Furthermore, their development often
        involves the ingestion of data not vetted by the State. Absent appropriate
        safeguards, the use of these technologies opens the door to significant risks,
        including inaccuracies, algorithmic bias, unauthorized use of intellectual property,
        privacy and security vulnerabilities, severe bias, and false information. Additionally,
        GenAI can be leveraged by malicious cybercriminals for a number of nefarious
        purposes, including, but not limited to, opening new physical and digital security
        vulnerabilities, generating misinformation campaigns, and assisting with
        sophisticated social engineering attacks. Creating a transparent and collaborative
        GenAI deployment process and creating upskilling programs that support effective
        transition to this technology ensures the protection of Maine citizens and the data
        entrusted to the State.

2.0.    Definitions
2.1.    Agentic AI: A Generative Artificial Intelligence agent that autonomously (i.e., without
        human intervention) completes a defined workflow, end-to-end.

2.2.    AI Chatbot: An Artificial Intelligence (AI) application that simulates human
        conversation and interaction through textual or aural communications.

2.3.    Bundled Application: An end-user application whose primary purpose is NOT AI, but
        uses AI to deliver its primary purpose. Example: Canva is a end-user application for

State of Maine                   Of�ice of Information Technology                      Page 1 of 9

                          Generative Artificial Intelligence Policy

        graphical and video content. However, Canva bundles AI features to deliver its
        primary purpose.

2.4.    Embedded GenAI: GenAI capabilities added into a tool or product that has previously
        been vetted and utilized by the State of Maine. The primary purpose of the tool or
        product is not GenAI.

2.5.    End-user AI Application: An end-user application whose primary purpose is AI.
        Examples include Microsoft Copilot, OpenAI ChatGPT, Google Gemini, Anthropic
        Claude, Amazon Quick, etc.

2.6.    Generative Artificial Intelligence (GenAI): Umbrella term for technologies that
        synthesize content mirroring human creativity. Encompassing machine learning and
        language models, GenAI generates human-like text, audio, imagery, video, and other
        digital content.

2.7.    Human in the Loop (HITL): The mechanism where human judgment and decision-
        making are integrated into GenAI outputs. This approach ensures that while
        machines handle tasks with speed and efficiency, humans oversee, guide, and
        intervene when necessary.

2.8.    Human on the Loop (HOTL): Applies to Agentic AI. By definition, an Agentic AI does
        not allow human intervention. Therefore, it does not allow HITL. Because the
        Agentic workflow will break if a human is inserted into the loop. Hence HOTL, where
        a human supervises the Agentic AI through statistical sampling, over time. The basic
        principle is the same as HITL in that the Human is still accountable for the
        performance of the Agentic AI. The human must continuously monitor outcomes,
        correct mistakes, and guide long-term improvement.

2.9.    Information Assets: The full spectrum of all I.T. products, including business
        applications, system software, development tools, utilities, appliances, etc.

2.10. Large Language Model (LLM): A statistical engine that has been pre-trained upon
      massive amounts of text. LLMs are the foundations of Generative Artificial
      intelligence.

2.11. Personal Productivity: In the context of GenAI, this is any GenAI action that a person
      undertakes as part of their own work-deliverables. This includes actions like email
      summarization, report drafting, etc. The important distinction is that the direct end-
      consumer of the GenAI is the person themself. This is in contrast to any work-
      deliverable that extends beyond that individual person. Any GenAI work product
      that is shared by a workgroup, or is business-critical, is, by definition, not Personal
      Productivity.

2.12. Private GenAI: GenAI tools that are specific to an entity or organization and their
      data. Private GenAI tools are developed in-house by the State for its own use or

State of Maine                    Of�ice of Information Technology                       Page 2 of 9

                         Generative Artificial Intelligence Policy

        obtained from a third-party vendor. These systems are configured in a way that
        ensures the State’s sensitive data is segmented from other Training Data and
        accessible to only the State or organization that owns it.

2.13. Public GenAI: GenAI tools that are openly available to multiple entities,
      organizations, or the general public and use widely sourced data from the internet,
      as well as data from users or customers to train the GenAI model. Public GenAI tools
      do not guarantee the privacy of data input by users, entities, or organizations.
      Additionally, Training Data and models are not owned by a public organization
      unless otherwise noted.

2.14. Training Data: Data used to train an LLM and other predictive algorithms.

3.0.    Applicability
3.1.    This Policy applies to:
        3.1.1. The Maine State Executive Branch, including all agencies, departments,
               commissions, committees, authorities, divisions, boards, or other
               administrative units, that operate under the direction of the Governor;
        3.1.2. All Personnel, both employees and contractors/vendors, within the Maine
               State Executive Branch;
        3.1.3. All Information Assets in use within the Maine State Executive Branch; and
        3.1.4. Information Assets from other branches of Maine State Government that are
               reliant upon the State Wide Area Network (WAN) for their operation.

4.0.    Responsibilities
4.1.    Agency Management:
        4.1.1. Ensures that their personnel are aware of, and compliant with, this Policy;
        4.1.2. Ensures that any approved GenAI usage is managed in compliance with this
               Policy; and
        4.1.3. Collaborates with the Chief Information Officer (CIO) in executing and
               enforcing this Policy.
        4.1.4. Informs OIT of relevant changes to existing-software under section 6.14

4.2.    Chief Information Security Officer (CISO):
        4.2.1. Resolves any conflicts under this Policy;
        4.2.2. Determines the risk associated with GenAI tools/products; and
        4.2.3. Collaborates with Agency Management in executing and enforcing this Policy.

4.3.    Chief Information Officer (CIO):
        4.3.1. Owns and interprets this Policy.

4.4.    OIT Architecture and Policy:
        4.4.1. Vets all net-new Information Assets before permitted usage.

4.5.    OIT Account Managers:

State of Maine                   Of�ice of Information Technology                 Page 3 of 9

                            Generative Artificial Intelligence Policy

        4.5.1. Liaise with Agency Management in executing and enforcing this Policy.

5.0.    Principles
5.1.    The following Guiding Principles serve as guardrails for use of GenAI within the
        Executive Branch of Maine State Government. These Principles were informed by a
        variety of sources, including the NIST Artificial Intelligence Risk Management
        Framework (AI RMF 1.0) 1. The following Principles are intended to guide personnel
        in the responsible development, deployment, and use of GenAI on the State’s IT
        enterprise:
        5.1.1. Valid and Reliable: The GenAI tool should consistently produce verifiable
                results and dependable outcomes under the conditions of expected use. Its
                robustness is equally essential, with the tool maintaining its performance
                under a variety of circumstances. The tool’s accuracy must be evaluated and
                managed throughout the application lifecycle to ensure the tool’s outputs are
                trustworthy and can be confidently relied upon.
        5.1.2. Safe, Secure, and Resilient: Securing the State’s Information Assets is
                essential to the State IT enterprise’s mission. GenAI tools must be evaluated
                for their safety, security, and resiliency to ensure the confidentiality,
                integrity, and availability of State data. These tools must adhere to
                established information security policies, procedures, and best practices to
                mitigate risk and protect against unauthorized access and misuse of data.
        5.1.3. Accountable and Transparent: GenAI tools should appropriately detail the
                processes for generating outputs and ensuring users have access to relevant
                information behind its decisions and operations. This includes traceability,
                explainability, communication regarding the sources of training data, and
                being able to attribute the tool’s outputs to specific data subsets when
                necessary. Mechanisms will be employed to identify responsibilities, to
                provide accountability for the use of GenAI and its outcomes, and to be
                reviewed for compliance with applicable laws and regulations prior to use.
        5.1.4. Explainable and Interpretable: The GenAI models and outputs are easily
                interpreted and explained to the greatest extent possible, ensuring that users
                can grasp both the mechanics (how) and the meaningful context (why) of the
                tool’s decision and/or outputs, particularly regarding its impact on decisions
                and/or outputs impacting sensitive and confidential data.
        5.1.5. Privacy-Enhanced: All applicable laws, regulations, policies, and procedures
                governing the privacy, quality, and integrity of State of Maine data must be
                applied in the development and use cases for all GenAI tools.
        5.1.6. Fair, with Harmful Bias Managed: The GenAI tool should be under
                continuous scrutiny to identify and mitigate potential impacts arising from
                data, human or algorithmic bias, to the greatest extent possible. Given the
                potential for these tools to amplify existing biases, continuous monitoring
                and proactive interventions shall prioritize countermeasures to reduce the
                risk of harmful bias or discrimination and to uphold fairness.

1 https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

State of Maine                       Of�ice of Information Technology                Page 4 of 9

                             Generative Artificial Intelligence Policy

6.0.      Directives
6.1.      This policy supersedes the Chief Information Officer's GenAI Moratorium.

6.2.      This policy is anchored in the Governor’s Artificial Intelligence Taskforce Report. 2

6.3.      All personnel must adhere to the Guiding Principles in 5.1 when using GenAI to
          enable the delivery of government services.

6.4.      Prior to using a GenAI tool, personnel must complete a GenAI training, as
          determined by the CISO/CIO. In addition, personnel must complete GenAI training
          provided by MaineIT on an annual basis, as well as complete any applicable use-
          case-specific GenAI training, as determined by the CISO/CIO.

6.5.      An output from a GenAI tool must never be:
          6.5.1. Used without a review; or
          6.5.2. Be assumed to be truthful, or accurate, or credible, or trustworthy; or
          6.5.3. Be used as the sole source of reference; or
          6.5.4. Be used in total to issue official statement (i.e. policy, legislation, or
                 regulations); or
          6.5.5. Be used to arrive at a final decision; or
          6.5.6. Be used to impersonate individuals or organizations.

6.6.      Should a GenAI tool be used to generate a batch output, then an appropriate Agency
          expert must use their domain knowledge to vet that batch output through
          appropriate statistical sampling techniques.

6.7.      Before being disseminated, or otherwise acted upon, any output from a GenAI tool
          must always be:
          6.7.1. Vetted by an appropriate agency human operator (HITL), and the
                 organizational level/standing of the agency human operator should be
                 commensurate with the significance/impact of the underlying content.

          6.7.2. At a minimum, this vetting must account for accuracy, appropriateness,
                 privacy, and security while meeting Section 6.9 of this policy.

6.8.      For any dissemination (irrespective of whether internal or external) of content that
          incorporates GenAI output, an explicit disclosure/attribution must be made by the
          agency. Such a disclosure/attribution may be achieved by a notation in the footnote,
          or header, or any comparable means.
           6.8.1. Example "Advised that XXX (a product with GenAI) was used to draft this
                  content. However, I/we have verified the content, and remain accountable
                  for it."

2
    https://www.maine.gov/future/sites/maine.gov.future/files/2025-10/_AI%20Report_DIGITAL.pdf

State of Maine                       Of�ice of Information Technology                       Page 5 of 9

                             Generative Artificial Intelligence Policy

6.9.    Sensitive or confidential information (TLP: Amber, Amber+Strict, or Red 3) protected
        from disclosure under federal or state statutes or regulations, as well as any
        information protected from disclosure under Maine’s Freedom of Access Act, must
        never be used as an input to a Public GenAI tool (as defined in 2.11), never be used in
        Public GenAI queries, and never be used for building or training Public GenAI tools.
        Furthermore, under no circumstances may personnel provide State of Maine data
        classified as non-public data (TLP: Amber, Amber+Strict or Red4) to a Public GenAI
        tool.

6.10. For a GenAI tool that allows such a feature, the history of usage must be disabled
      (i.e., turned off).

6.11. Material that is proprietary, or otherwise copyrighted, must never be used as an
      input to a GenAI tool.

6.12. GenAI must never be used by personnel for any activity that violates any federal or
      state laws, regulations, policies, or procedures.

6.13. Any vendor and/or contractor creating any Information Asset for the State of Maine
      Executive Branch must explicitly declare any usage of GenAI, especially the nature of
      the data used as input, and be subject to a risk assessment during the procurement
      process.

6.14. OIT will continuously maintain a webpage Generative AI Tools and Acceptable Use 5
      (internal-only) that lists the GenAI tools and use cases that are currently approved
      for use by the Executive Branch of Maine State Government. Any such use is
      explicitly subject to all stipulations detailed in this Policy. The tools listed on the
      website are subject to removal, compensating controls, or conversion to an
      enterprise-based GenAI offering, at the discretion of the CISO such that risks to the
      confidentiality, integrity, and availability of State data are appropriately managed
      and rigorous information security standards and safeguards are in place to support
      scaling GenAI usage at the enterprise level. Any GenAI tool or use case not explicitly
      approved on this webpage is expressly prohibited from use within the Executive
      Branch of Maine State Government. To request consideration for an AI tool or use
      case, send an email to Enterprise.Architect@Maine.Gov.

6.15. A pre-approved GenAI tool (see above) may be used purely for Personal
      Productivity. Any usage of a pre-approved GenAI tool beyond Personal Productivity,
      and/or any proposed usage of a tool that is not pre-approved must be routed
      through the Enterprise Architecture vetting workflow.

3 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/DataClassificationPolicy.pdf
4 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/DataClassificationPolicy.pdf
5 https://stateofmaine.sharepoint.com/sites/MaineIT-

Security/Shared%20Documents/Policies/GenAIToolsandAcceptableUse.pdf

State of Maine                        Of�ice of Information Technology                            Page 6 of 9

                                Generative Artificial Intelligence Policy

6.16. Any application/tool/product/information asset that has previously been vetted
      and approved through the OIT New Technology workflow, but which now embeds
      GenAI, shall continue to stay approved, unless such an approval has been explicitly
      rescinded by the CISO/CIO.

6.17. A product containing Generative Artificial Intelligence (GenAI) capabilities may be
      evaluated and treated as non-GenAI in cases when all GenAI functionality can be
      fully disabled through documented administrative controls and is inaccessible to
      end users.
      6.17.1. In these cases, because GenAI functionality may be enabled by
                administrative action, continued treatment as non-GenAI requires
                separation of duties, formal change management, and auditability.
      6.17.2. Administrative authority to enable or expose GenAI features must be
                restricted, subject to prior security and risk approval, and periodically
                validated.
      6.17.3. Unauthorized or unreviewed enablement of GenAI functionality constitutes
                a configuration control failure, at which point the product must be treated
                as GenAI-capable for risk, security, and compliance purposes.

6.18. Existing pre-approved tools must be reviewed at least annually, or more frequently
      if the agency is notified of changes to terms and conditions or platform changes that
      incorporate the use of GenAI, to ensure ongoing compliance with all state-set
      software usage and AI usage policies.

6.19. In terms of interactive GenAI assistants, Microsoft Copilot is the State’s primary
      approved enterprise GenAI assistant. Legacy, pre-approved usage of ChatGPT
      Enterprise is grandfathered for now. Any agent, pre-built by Microsoft, and rolled
      out into the enterprise Copilot remains pre-approved. Anything that can be done
      with the built-in agents graphicially, via a widget, within the enterprise Office 365
      tenant, remains pre-approved. Any GenAI built into the approved browsers remains
      to be pre-approved.

6.20. For bundled applications (as defined in 2.3), only mainstream, public, North
      America-based LLMs are eligible for consideration for State of Maine Executive
      Branch GenAI usage. The eligible LLMs are listed in OIT’s Approved Tools and
      Acceptable Use Cases 6. Approval of an underlying LLM does not constitute approval
      of any corresponding end-user application (as defined in 2.5) or service. End-user
      applications remain subject to review and approval by OIT. End user products
      approved by OIT will be listed: Approved Tools and Acceptable Use Cases 7.

6.21. AI prompts and other interactions with generative AI are generally considered
      transitory working materials when they are used solely for drafting, brainstorming,
      research, or similar purposes and have no continuing administrative, legal, fiscal, or

6
    https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/GenAIToolsandAcceptableUse.pdf
7
    https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/GenAIToolsandAcceptableUse.pdf

State of Maine                            Of�ice of Information Technology                            Page 7 of 9

                                Generative Artificial Intelligence Policy

           historical value. In these circumstances, they may be managed under General
           Schedule 5.6 (Transitory Correspondence) 8 or other applicable transitory records
           schedules. However, if an AI prompt or conversation documents agency decision-
           making, provides substantive instructions, establishes policy, supports official
           actions, or otherwise meets the definition of a government record under Maine law,
           it must be retained according to the applicable records retention schedule. The final
           agency work product, together with any supporting records required to document
           official business, constitutes the official record.

6.22. For any privacy concerns, absent an Agency Privacy Officer, contact the Enterprise
      Architect mailbox at Enterprise.Architect@Maine.gov.

7.0.       Account Creation
7.1.       GenAI tools often require that users enter an email address to register and create an
           account. Users who are utilizing an approved Public GenAI tool for State purposes
           must use their State e-mail address for registration and account creation purposes.

7.2.       Once created, the account associated with a user’s State e-mail address must be used
           solely for State business purposes. Personal use of Public GenAI from an account
           using a State e-mail is prohibited.

7.3.       Upon completion of the registration and the account creation process, users must
           opt-out of data sharing and disable the chat history within the Public GenAI system.
           If unable to opt-out, the user must contact OIT at Enterprise.Architect@Maine.gov
           prior to using the Public GenAI system.

8.0.       AI Chatbot Disclosure Requirements; Prohibited Conduct
8.1.       Use of an AI chatbot in communications with consumers must include a clear and
           conspicuous disclosure that the consumer is interacting with an AI chatbot and not a
           human being.
           8.1.1. Pursuant to Public Law 2025, chapter 294, a violation of this section
                   constitutes a violation of the Maine Unfair Trade Practices Act.

8.2.       The requirements of this section are intended to supplement the provisions of this
           policy and operate in addition to, and in conjunction with, the policy as a whole.

9.0.        Compliance
9.1.        For employees, failure to comply with this policy may result in progressive
            discipline, up to and including dismissal.

9.2.        For contractors and non-State of Maine personnel, failure to comply may result in
            removal of the individual’s ability to access and use State of Maine Information
            Assets. Employers of non-State of Maine personnel will be notified of any
            violations.

8
    https://www.maine.gov/sos/sites/maine.gov.sos/files/content/assets/GS5Correspondence.pdf

State of Maine                           Of�ice of Information Technology                      Page 8 of 9

                            Generative Artificial Intelligence Policy

9.3      In addition, Public Law 2025, chapter 294 enacted new disclosure requirements
         governing communications with consumers through the use of AI chatbots. The law
         prohibits a person from using an AI chatbot to engage in trade or commerce with a
         consumer in a manner that may mislead or deceive a reasonable consumer into
         believing that the consumer is engaging with a human being unless the consumer is
         notified that the consumer is not engaging with a human being. A violation of this
         prohibition is a violation of the Maine Unfair Trade Practices Act.

10.0.   Document Information
10.1.   Initial Issue Date: July 19, 2024
10.2.   Latest Revision Date: October 30, 2026
10.3.   Point of Contact: PolicyTeam.OIT@Maine.Gov
10.4.   Approved By: Chief Information Officer, OIT
10.5.   Legal Citation: Title 5, Chapter 163: Office of Information Technology 9
10.6.   Waiver Process: Waiver Policy 10
10.7.   Distribution: Internet 11

9 https://legislature.maine.gov/statutes/5/title5ch163sec0.html
10 https://www.maine.gov/oit/policies/waiver.pdf
11 https://www.maine.gov/oit/policies-standards

State of Maine                       Of�ice of Information Technology              Page 9 of 9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
