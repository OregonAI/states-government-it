---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-nys-g25-002
title: Generative Artificial Intelligence Use in the Workplace
doc_type: policy
citation: NYS ITS Guideline NYS-G25-002
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/generative-artificial-intelligence-use-workplace
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 13d2c67f24e276fc560d4e7ec92bb4feef0e61e68fdbdaf14f5e3cf75c801dae
effective_date: null
source_version: 'Updated: 6/24/2026'
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Generative Artificial Intelligence Use in the Workplace (NYS ITS Guideline NYS-G25-002)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Policy, Statewide Policies' on the listing. The listing prints original publication 06/24/2026 and last modified 06/24/2026.

## Full text

                               State Capitol P.O. Box 2062
                                 Albany, NY 12220-0062
                                     www.its.ny.gov

     New York State Information
                                              No: NYS-G25-002
       Technology Guideline

              IT Guideline:                   Updated: 6/24/2026

  Generative Artificial                       Issued By: NYS Office of Information
                                              Technology Services
  Intelligence Use in
                                              Owner: Chief Artificial Intelligence
    the Workplace                             Office

1.0 Purpose and Benefits
The purpose of this guideline is to provide guidance for the use of Generative
Artificial Intelligence (GenAI) by State Agencies (SAs) in the workplace. This
guideline is designed to assist SAs in understanding the benefits and risks of
GenAI and encourages the adoption of best practices that will maximize benefits
and minimize risks to SAs that choose to use GenAI in their workplaces. Questions
on the elements of this guideline may be directed to the Office of Information
Technology Services’ (ITS) Chief Artificial Intelligence Office at
its.sm.caio.ai@its.ny.gov.

2.0 Authority
Section 103(10) of the State Technology Law provides the Office of Information
Technology Services (ITS) with the authority to establish statewide technology
policies, including technology and security standards. Details regarding this
authority can be found in NYS ITS Policy, NYS-P08-002 Authority to Establish
State Enterprise Information Technology (IT) Policy, Standards and Guidelines.

3.0 Scope
This guideline applies to all “State Agencies” as defined in Section 101 of the State
Technology Law. This includes employees and all third parties (such as local
governments, consultants, vendors, and contractors) that use or access any

Information Technology (IT) Resource for which the SA or ITS has administrative
responsibility, including systems managed or hosted by third parties on behalf of
the SA or ITS.

Non-SAs, including authorities, boards, and other New York State governmental
organizations are encouraged to consider this guideline in their use and adoption
of AI.

4.0 Information Statement
4.1    Generative Artificial Intelligence Definition

For the purposes of this guidance, “generative artificial intelligence” means an
artificial intelligence system that is capable of producing and being used to produce
synthetic digital content, including images, videos, audio, and text.

Examples of popular GenAI systems that fall under this definition are OpenAI’s
ChatGPT, Anthropic’s Claude, Google’s Gemini, Microsoft’s CoPilot, and ITS’s own
AI Pro.

4.2    Benefits and Risks

GenAI systems are a powerful tool that can improve the day-to-day operations of
SAs, leading to greater productivity and innovation. However, GenAI systems can
carry inherent risks that their users need to be aware of so that appropriate risk
mitigation strategies can be deployed. SAs should therefore encourage adoption
of GenAI systems where appropriate, train their employees on effective GenAI
usage, and ensure practices and procedures are in place to mitigate risks.

4.3    Best Practices

The following are a set of best practices SAs can encourage and adopt that
maximize efficient use of GenAI systems while minimizing their potential risks. This
list is not exhaustive, and SAs are encouraged to adopt other measures as
needed. SAs should remain mindful that technology in this area is fast-moving and
they should review and update their practices as appropriate.

4.3.1.1        Ensure Adequate Training Before GenAI Usage
SAs should ensure their staff undergo GenAI training before deploying a GenAI
system. Such training should, at a minimum, cover some of the topics discussed
in this guideline. The importance of ongoing training on GenAI systems cannot be
overstated as these systems evolve and their use cases increase.

4.3.1.2      Be Careful When Entering Personal, Private or Sensitive
       Information into GenAI Systems
Because GenAI systems may use user inputs and related outputs for training
purposes, SAs should be especially vigilant when using these systems. GenAI

NYS-G25-002                                                                Page 2 of 9

systems might not anonymize or deidentify data and may expose the information
to the internet. Additionally, inputting certain types of data may violate various laws
and regulations without the appropriate controls in place. Further, due to their
potential for hallucination 1 (e.g., inventing false facts, image generation errors,
doubling down on fabrications) and bias, GenAI systems and their outputs should
be reviewed for accuracy and fairness by users.

To minimize risks, avoid entering PPSI into GenAI systems without understanding
how the GenAI system handles this data and do not use these systems without SA
leadership approval. SAs should ensure GenAI outputs are frequently and
consistently reviewed by humans to ensure any issues are spotted and addressed.
At a minimum, SAs should ensure humans review GenAI outputs before they are
published or submitted to viewers outside the SA.

4.3.1.3         Ensure Human Oversight of GenAI Systems

SAs may utilize GenAI systems to support decision-making processes; however,
such systems cannot be permitted to fully automate these decisions. Any use of
automated decision-making systems by SAs must be subject to human review.
This entails that users, who are trained and understand the system's functionality,
risks, and limitations, should oversee and control all processes where GenAI
systems support decision-making. These users should have the authority to alter
or override decisions made by the system to ensure accountability and alignment
with legal, ethical, and operational standards.

4.3.1.4       Transparency
GenAI systems excel at producing content that mimics human output such as text,
voice, and images, making it difficult for recipients to distinguish between AI-
generated and human-created content. As such, SAs should review the
requirements of section 4.2.3 of NYS-P24-001 Acceptable Use of Artificial
Intelligence Technologies regarding the disclosure of the use of GenAI systems.

4.3.1.5       Practice Effective Prompting
GenAI systems generally operate based on human inputs, known as “prompts.”
GenAI systems can be very sensitive to prompt phrasing: inputs that seem
identical to humans can produce dramatically different results. As such, SAs
adopting GenAI systems should practice “prompt engineering.” Prompt
engineering is the practice of optimizing prompts to guide and improve GenAI
system outputs by trying different phrasing of the same prompt, or slightly
modifying the parameters of the prompt, to achieve a desired result.

There is no single best practice for prompt engineering, and ideal prompts vary
based on model and task. In general, users of GenAI systems should try a wide

1 AI hallucinations are when the response from an AI model contains false or misleading information

presented as fact.

NYS-G25-002                                                                             Page 3 of 9

variety of prompts when using GenAI systems, particularly if they are not getting a
desirable or helpful response. Examples of prompt engineering include:

Role-Based Prompts: Define the model's role within the prompt (e.g., "You are a
business case drafting expert...") to guide its responses within the appropriate
context and reduce off-topic or unexpected outputs.

Chain-of-Thought: Enhance outcomes by asking the model to generate a step-by-
step plan with an explanation, purpose, and expected outcome of each step. Users
then follow up within the same session, prompting the model to address each step
in sequence. This structured approach improves logical coherence and reduces
the likelihood of errors.

Iterative Prompt Refinement: Engage in a cycle of testing and refining prompts to
achieve desired outcomes. This process helps in identifying prompts that may
produce more relevant results.

4.3.1.6       Create User Feedback Mechanisms
SAs should set up clear and easy channels for users to flag inaccuracies or
concerns with GenAI outputs to their supervisors. This system for collecting
feedback is important because it helps identify issues that human reviewers might
miss and provides valuable information that can be used to improve the GenAI
system over time.

4.3.1.7        Maintain Detailed Usage Logs
All interactions with approved GenAI tools (e.g., ChatGPT, Copilot) should be
logged for a minimum of 90 days to enable accountability and help identify potential
misuse, security issues, or areas for improvement in system usage. SAs should
track who uses GenAI systems, what inputs are provided to the system, and how
outputs are utilized.

4.3.1.8       Incorporate Contractual Terms to Protect SA Data
SAs should consider incorporating terms into contracts with external GenAI
providers that safeguard an SA’s data and information. SAs should consider
applicable law and regulations regarding relevant data and information in
determining the necessity and scope of such terms. Terms to consider include, but
are not limited to:
   •   Prohibition against using an SA’s data or prompts for training a vendor’s
       GenAI without explicit written consent and that SA’s data is used for limited
       purposes. Data should be restricted for use and retention solely in providing
       contracted services.

   •   Ownership of GenAI-generated data.

   •   Requiring notice from vendor if a third party requests access to the SA’s
       data through, for example, a subpoena or court order.

NYS-G25-002                                                               Page 4 of 9

    •   Adherence to New York State Information Technology Policy No: NYS-P24-
        001 “Acceptable Use of Artificial Intelligence Technologies,” or any
        successor policies.

    •   Vendors providing clear and unambiguous notice to an SA prior to
        implementing GenAI, detailing its purpose, functionality, and data usage.

    •   Having GenAI tools not integral to a system disabled by default. SAs should
        detail the approval process required by the SA for any GenAI usage, and
        what approval is needed to implement GenAI.

    •   Compliance with all applicable local, state, policies, rules, and federal laws
        and regulations concerning GenAI. AI processing, transmitting, or storage
        of SA data reflect relevant geographic data residency requirements in
        applicable regulatory frameworks and the information classification
        standard. 2

4.3.1.9        Comply with All Relevant ITS Policies
GenAI systems are still a subset of AI systems and information technology tools.
As such, SAs that use GenAI systems should ensure that they continue to comply
with all relevant ITS policies and standards, including, but not limited to:

    1. NYS-P24-001 Acceptable Use of Artificial Intelligence Technologies

    2. NYS-P03-002 Information Security

    3. NYS-P14-001 Acceptable Use of Information Technology (IT) Resources

5.0 Compliance
This guideline shall take effect upon publication. Compliance with enterprise
guidelines is not compulsory, but strongly suggested. ITS may amend its
guidelines at any time; compliance with amended guidelines is not compulsory, but
strongly suggested.

6.0 Definitions of Key Terms
Except for terms defined in this policy, all terms shall have the meanings found in
http://www.its.ny.gov/glossary.

“Geographic data residency” refers to legal requirements regarding the geographic
locations where data can and cannot be received, processed, stored, accessed,
or transmitted. Examples including criminal justice information, governed by the

2It is the responsibility of the State Entity deploying GenAI tools to identify and comply with
geographic residency requirements. For more information, see ITS-P019-002 Cloud Computing
Policy.

NYS-G25-002                                                                         Page 5 of 9

CJIS Security Policy, and federal tax information, governed by IRS Publication
1075.

7.0 Contact Information
Submit all inquiries and requests for future enhancements to the policy owner at:

                     Chief Artificial Intelligence Office
                          Reference: NYS-P24-001
               NYS Office of Information Technology Services
                    State Capitol, ESP, P.O. Box 2062
                              Albany, NY 12220
                      Email: its.sm.caio.ai@its.ny.gov

  Statewide technology policies, standards, and guidelines may be found at the
                  following website: https://its.ny.gov/policies

8.0 Revision History
This policy should be reviewed consistent with the requirements set forth in ITS-
P24-003 Process for Establishing Information Technology Policies, Standards, and
Guidelines.

 Date            Description of Change                             Reviewer
 06/24/2026      Issued guideline                                  Chief Artificial
                                                                   Intelligence Office

9.0 Related Documents

NYS-G25-002                                                             Page 6 of 9

Appendix A: Common Use Cases and Examples
1. Summarization
GenAI Capability: This capability allows GenAI to read through large amounts of
text and generate shorter versions that highlight the most important points.

Purpose: To help agencies quickly understand and process large volumes of
textual information, saving staff time and improving access to key insights.

Examples:

       Summarize public comments received on a proposed regulation to identify
       key themes and common concerns.

       Summarize research papers or reports to inform policymakers on a topic.

       Create concise summaries of meeting minutes or lengthy emails.

Human Oversight: Employees should review the summaries for accuracy and
ensure they reflect the most relevant information for the intended purpose.

2. Content Generation (Text, Image, Video)
GenAI Capability: This capability allows GenAI to create original digital content,
such as text, images, and videos, based on prompts or input data.

Purpose: To quickly produce a variety of communication materials, creative
content, and visual aids for public outreach and internal communication.

Examples:

   •   Draft social media toolkits for emergency preparedness campaigns.

   •   Draft blog posts or newsletters for policy updates or civic engagement.

   •   Generate video explainers for new online digital services or programs.

Human Oversight: Employes should review content for tone, factual accuracy,
accessibility, and cultural sensitivity. All materials intended for the public should
follow branding and editorial guidelines.

3. Chatbots
GenAI Capability: GenAI-powered chatbots can simulate natural conversations to
guide users, answer questions, and assist with common tasks. They can adapt to
user needs, support multiple languages, and provide 24/7 support.

Purpose: To improve service delivery, reduce response times, and help residents
navigate agency services without requiring live assistance for every inquiry.

NYS-G25-002                                                                Page 7 of 9

Examples:

   •   Set up a chatbot that can guide users through services that may be
       available to them.

   •   Answer frequently asked questions at scale to reduce call volume.

   •   Shorten the time residents spend waiting on hold or talking with staff at state
       customer service centers.

Human Oversight: Employees should regularly review the chatbot's performance,
update responses as policies change, and ensure that complex or sensitive
questions are correctly identified and sent to a human agent for assistance.

4. Simplification
GenAI Capability: This capability enables GenAI to convert technical, legal, or
complex information into plain language explanations based on user input.

Purpose: To make government services and requirements more accessible to all
users, regardless of familiarity with agency processes.

Examples:

   •   Rephrase legal language on agency websites into easy-to-understand
       summaries.

   •   Simplify step-by-step instructions for processes, like filing taxes, registering
       a business, or applying for aid.

   •   Offer simplified explanations of eligibility criteria for state benefits through a
       conversational interface.

Human Oversight: Employees should always verify the accuracy and clarity of the
simplified content and explanations provided by the system.

5. Language Translation
GenAI Capability: This allows GenAI to automatically convert text or spoken
language from one language to another.

Purpose: To improve communication and increase accessibility for residents who
speak languages other than English, ensuring equitable access to state services,
information, and public participation opportunities.

Examples:

   •   Translate agency website content, forms, and outreach materials into
       multiple languages.

NYS-G25-002                                                                    Page 8 of 9

   •   Provide real-time written translation for staff responding to resident
       inquiries.

   •   Enable chatbots or virtual assistants to interact with users in multiple
       languages based on preference.

Human Oversight: Employees should review translated materials for accuracy,
tone, and cultural sensitivity prior to distribution or publication, especially those
documents deemed vital by an SA. SAs must abide by all applicable NYS language
access laws and policies.

NYS-G25-002                                                                Page 9 of 9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
