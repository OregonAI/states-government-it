---
schema_version: 1
corpus: states-government-it
jurisdiction: maryland
id: md-doit-ai-card-call-recording
title: 'AI Governance Card: AI-Powered Call Recording & Transcription Tools'
doc_type: policy
citation: 'DoIT AI Governance Card: Call Recording & Transcription, version 1.0'
authority_level: ''
issuing_body: Maryland Department of Information Technology
source_url: https://doit.maryland.gov/policies/ai/Pages/AI-governance-card-call-recording-transcription-tools.aspx
source_format: html
retrieved: '2026-11-11'
source_sha256: 52896c4e296bdd9eca3d6fa11419d72905e566847f77bbea8011809ca7fd22dd
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text taken from the page's main content (title and rich-text field) as DoIT's SharePoint
  site serves it, one line per paragraph, heading, list item and table row (a table row's cells are joined
  by ' | '; list items carry a bullet or their number). Links are written as their text, pictures and
  page navigation are not read, and an e-mail address the site obscures prints as '[email protected]'.
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

# AI Governance Card: AI-Powered Call Recording & Transcription Tools (DoIT AI Governance Card: Call Recording & Transcription, version 1.0)

## At a glance

Listed on DoIT's AI policies page (https://doit.maryland.gov/policies/ai/Pages/default.aspx) and ai.maryland.gov/state-employee-guidance/policies. As the page prints its purpose: This governance card provides guidance on baseline definitions and guidelines in Maryland's Responsible AI Policy, Responsible AI Implementation Guidance, SB818, and Governor's EO applied to AI-powered call recording and transcription.

## Full text

AI Governance Card: AI-Powered Call Recording & Transcription Tools
Revision History:
• Last Revised: 08/07/2025
• Date Issued: 09/05/25
• Version: 1.0
• Author: Solomon Abiola
1.0 Purpose and Scope
This governance card provides guidance on baseline definitions and guidelines in Maryland's Responsible AI Policy, Responsible AI Implementation Guidance, SB818, and Governor's EO applied to AI-powered call recording and transcription. Agencies may adopt this guidance wholesale or institute stricter guidance given their specific context, in accordance with their agency's IT policies.
2.0 Risk Classification
Risk Tier: Limited Risk | Minimal Risk | High Risk | Unacceptable Risk
Risk Summary: AI call recording/transcription services are considered Limited or Minimal Risk per the Responsible AI Implementation Guidance risk matrix.
3.0 Acceptable Use Guide (Do's and Don'ts)
DO
• Opt out of data sharing or model-training uses. If a tool does not allow you to opt out, consult your agency's IT security office or the Maryland Department of Information Technology (DoIT) for guidance on approved tools.
• Actively decide if a meeting should be recorded instead of recording by default. Transcribed notes and recordings may be subject to release under the Maryland Public Information Act, and agencies need to store them securely and retain or dispose of them per State records schedules. Agency IT leads are advised to work alongside their agency’s Public Information Act Officer to determine if additional agency policies or best practices should be written based on the specific considerations of their agency.
• Use versions under State contracts (e.g., using the tools already built into your agency’s business productivity suite) rather than free consumer accounts (e.g., accessing a tool like ChatGPT from the internet), so that State IT terms (security, privacy, liability) apply.
DON'T
• Erase the "Created by AI" watermark at the end of meeting summaries and transcription notes. For example, Gemini's watermark: This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
• Record meetings or transcriptions if one (1) participant who logs in does not consent. Always ask for consent before you begin recording and transcribing.
• Record confidential meetings (e.g., personnel discussions, legal consultations, discussions that include confidential or restricted information), as doing so could introduce legal risks (attorney-client privilege waiver, Health Insurance Portability and Accountability Act (HIPAA) violations, etc.).
• Let external participants create meeting recordings from their end or use their own software for transcription. Their tools have not been vetted by DoIT or your agency’s IT leadership, and the risk level may be higher than is allowed for Maryland State Agencies.
4.0 Key Risks and Mitigation Strategies
4.1 Data Privacy and Confidentiality
Risk: Meeting transcriptions and recordings produced by AI are considered public records, and therefore could be subject to disclosure in response to a Public Information Act (PIA) request. Attendees should be mindful of the content they discuss in recorded meetings. Exposure of personally identifiable information, sensitive State data, or confidential information through transcription services.
Mitigation:
• Actively decide if a meeting should be recorded instead of recording on default.
• Avoid discussing personal and sensitive information (SSNs, passwords, health details, immigration status, information about children under 18 years old) in recordings.
• Do not record confidential meetings (e.g., personnel discussions, legal consultations, IT security infrastructure), as doing so could introduce legal risks (attorney-client privilege waiver, etc.). Similarly, do not record personal and sensitive information (SSNs, passwords, health details, immigration status, information about children under 18 years old).
4.2 Bias, Equity, and Accessibility
Risk: AI transcription may produce inaccurate transcriptions for certain accents, regional dialects, or when technical terminology is used. See Appendix A for a detailed evaluation of common transcription errors, including:
• Accents (Likelihood: High)
• Punctuation errors (Likelihood: High)
• Acronyms/Out of Vocabulary terms (Likelihood: High)
• Foreign Languages issues (Likelihood: Low)
• General Errors (Likelihood: Medium)
Mitigation:
• Do not erase the "Created by AI" watermark at the end of meeting summaries and transcription notes. For example, Gemini's watermark: This editable transcript was computer-generated and might contain errors. People can also change the text after it was created.
4.4 Over-Reliance and Accountability
Risk: Users may accept AI transcription outputs without critical evaluation, leading to errors in official records or decision-making based on inaccurate transcriptions.
Mitigation:
• Maintain human oversight as the final point of accountability for transcript accuracy
• Be aware that transcription errors are common and review is essential
5.0 Governance and Compliance
5.1 Approved Tools & Vendor Requirements
Approved Tools: The tools that are currently approved for usage for Maryland State Agencies for meeting transcription are:
• Gemini Enterprise for Google Meet
• Copilot for Microsoft Teams
Vendor Requirements:
• Gemini and Copilot both have FedRAMP High Authorizations. To learn more: Gemini FedRAMP High Approval and Copilot Studio for US Government customers.
• Gemini SOC2
• Gemini also has additional privacy and security protections for its enterprise version: Generative AI in Google Workspace Privacy Hub.
Additional Tool Approval Process:
• If you would like to use a different software than Gemini and Copilot, the AI Enablement team will have to review the policies, terms, and conditions applicable to the software and its use case before granting approval. Please fill out an AI intake ticket by emailing [email protected]
• For more details about the AI intake process, refer to Responsible AI Implementation Guidance
5.2 Data Handling and Retention
• Transcribed notes and recordings may be subject to release under the Maryland Public Information Act, and agencies need to store them securely and retain or dispose of them per State records schedules
• Do not record confidential meetings (e.g., personnel discussions, legal consultations) or meetings that would include confidential and restricted information (SSNs, passwords, health details)
5.3 Consent and Disclosure Protocol
Required Consent Process:
• Obtain consent from all participants for meeting recordings and transcriptions by either notifying in the invite, "this meeting will be recorded and transcribed with AI, if you would like to opt-out, please decline," OR requesting verbal consent from all participants before starting the recording/transcription, or after if they join late.
• Do not record/transcribe meetings if one participant who logs in does not consent.
• Notice of recording is required due to Maryland’s 2-party consent requirement.
AI Transcription Scenario Flowchart
FAQ's
Q: My agency uses/interacts with data that is subject to more regulations. How do I ensure the chosen service complies with relevant regulations, and what regulations should I think about?
A: Example regulations your agency may be subject to include General Data Protection Regulation (GDPR) if any data involves European Union (EU) persons, or HIPAA if health info is discussed. Many consumer-grade transcription services are not HIPAA-compliant by default. If an agency must disclose protected health information, it should only use an AI transcription service that offers a Security Rule-compliant environment and executes a Business Associate Agreement.
Q: My agency has Gemini/Copilot enabled. How do I use transcription during my meetings?
A: For Gemini, follow the directions/guidance here:
• DoIT AI Productivity Guide - Covering productive AI use cases and how to use Google Workspace systems.
• AI Gemini Governance Card - Covering cases of Gemini and Google Workspace usage beyond transcription.
For Copilot:
• DoIT AI Productivity Guide - Covering productive AI use cases and how to use Copilot in Microsoft 365 products.
Q: Why Gemini and Copilot?
A: Gemini and Copilot both have FedRAMP High Authorizations. To learn more about the importance of FedRAMP High Authorization, please read Gemini FedRAMP High Approval and Copilot Studio for US Government customers. Gemini also has additional privacy and security protections for its enterprise version: Generative AI in Google Workspace Privacy Hub.
Q: I would like to use a different software than Gemini and Copilot. Am I prohibited from using it?
A: DoIT’s AI Enablement team will have to review the policies, terms, and conditions applicable to the software and its use case before granting approval. Please submit your AI request through intake by emailing [email protected]. For more details about the AI intake process, refer to Responsible AI Implementation Guidance.
Q: Why can't I use software that hasn't been approved by the AI Enablement Team, if transcription is an approved use case?
A: The AI Enablement team evaluates the risk level of the software in addition to the use case, by referencing Maryland's Data Classification Policy and higher authority standards like HIPAA and FedRAMP. This process is not meant to hinder you from using AI, but to abide by statutory AI inventory requirements and acceptable risk levels.
Q: I have more legal questions than what's covered in this card.
A: These questions are best directed to your agency's counsel.
Appendices
Appendix 1: Evaluation Section
Last updated: 09/05/2025
Even though speech-to-text transcription software has become more accurate and has increased formatting functionality with each iteration of AI, there are still some weaknesses that users should be aware of when reviewing the generated transcripts for errors. Likelihood here refers to the likelihood that this presents as something to be concerned about by using these tools.
1. Accents: Since text-to-speech relies on trying to translate sound waves into words based on probability and context, it's possible that the context gets outweighed by the soundwave translation. Likelihood: High
2. Punctuation: Because punctuation's effects can vary in speech, and people's speech can be imperfect, speech recognition can add or omit punctuation based on speech delivery, i.e. adding a period when someone took an extra long pause in their speech or not having commas because someone didn't take a long enough pause. Likelihood: High
3. Acronyms/Out of Vocabulary terms: As in most local communities, there is a lexicon that only exists within the Maryland State Government. (Ex: PIN = Position Identification Number) Transcription software may not transcribe the correct term or acronym because of its general use case nature. Likelihood: High
4. Misspellings based on uncommon pronunciations: Perhaps similar to accents, AI sometimes doesn't recognize words said in regional accents, such as "Gloucester" in Massachusetts versus elsewhere. Most variations are probably common enough where speech recognition has accounted for them, such as different pronunciations of "data" or "project". Likelihood: Low
5. Foreign Languages: Currently, you need to set the language that the AI Transcription software is expecting. As a result, if participants are speaking in a language that the software does not recognize or they switch between two languages throughout the meeting, the software does not perform well in capturing all what is discussed. Likelihood: Medium
6.General Errors Sometimes an error will occur that doesn't match a matter. In testing, for example, when the speaker said "Does", the software transcribed it as "Is". While these errors are generally harmless, it is possible that the error changes the meaning of the sentence. Likelihood: Medium
Appendix 2: Current Gemini and Copilot Policies
Last updated: 07/15/2025
Google's Disclosures:
• Gemini feature suggestions don't represent Google's views, and should not be attributed to Google.
• Don't rely on Gemini features as medical, legal, financial or other professional advice.
• Gemini features may suggest inaccurate or inappropriate information. Your feedback makes Gemini more helpful and safe.
• Enterprise end users can submit feedback about their experience using this feature. End users are informed before they submit feedback that the feedback data shouldn't contain personal, sensitive, or confidential information.
Privacy/Security Policy:
Gemini abides by your organization's existing controls and data handling practices. Gemini accesses customer data in order to provide personalized responses, such as summarizing a document in Google Docs or analyzing data in a Google Sheet.
Data stored by the customer through use of Google Workspace services is considered customer data as defined by the Cloud Data Processing Addendum (CDPA) and, as such, is governed by the data processing terms set out in the CDPA. Google only accesses and processes customer data in accordance with customer instruction as set out in the CDPA.
• Your interactions with Gemini stay within your organization. Gemini does not share your data outside your organization without your permission.
• Gemini brings the same enterprise-grade security as the rest of Google Workspace, automatically applying your organization's existing controls and data handling practices.
• Your content is not used for any other customers. None of your content is used for generative AI model training outside of your domain without permission.
Additional Support: For additional support, explore Maryland’s AI resources and tools at the state’s official AI portal.

## Curator notes

Text taken from the page's main content (title and rich-text field) as DoIT's SharePoint site serves it, one line per paragraph, heading, list item and table row (a table row's cells are joined by ' | '; list items carry a bullet or their number). Links are written as their text, pictures and page navigation are not read, and an e-mail address the site obscures prints as '[email protected]'.
