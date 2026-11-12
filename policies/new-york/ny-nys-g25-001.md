---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-nys-g25-001
title: AI Inventory Guidance
doc_type: policy
citation: NYS ITS Guideline NYS-G25-001
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/ai-inventory-guidance-document
source_format: pdf
retrieved: '2026-11-11'
source_sha256: fcfba968cd13b7cab71b94cf811c0f10ec7d5ede233c5b4f25bfbff4554f405e
effective_date: null
source_version: 'Issued: 03/04/2025'
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# AI Inventory Guidance (NYS ITS Guideline NYS-G25-001)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Technology Development/Use' on the listing. The listing row prints no dates.

## Full text

                                                            State Capitol
                                                           P.O. Box 2062
                                                       Albany, NY 12220-0062
                                                           www.its.ny.gov

         New York State
Information Technology Guideline No: NYS-G25-001

                   IT Guideline:                                 Issued: 03/04/2025

                                                                 Issued By: NYS Office of Information
           AI System                                             Technology Services

           Inventory                                             Owner: Chief Data Office

           Guidance
           Document

1.0 Purpose and Benefits
   The purpose of this guideline is to provide detailed instructions to State Entities (SEs)
   for the creation and reporting of an Artificial Intelligence (AI) System Inventory to ITS.
   The objectives of this AI system inventory are to document and maintain records of all
   AI systems in use across SEs and facilitate public accessibility to select data elements
   from this AI system inventory to promote transparency, ensure accountability, and foster
   trust in the use of AI technologies.

2.0 Authority
   Section 103(10) of the State Technology Law provides the Office of Information
   Technology Services (ITS) with the authority to establish statewide technology policies,
   including technology and security standards. Section 2 of Executive Order No. 117 1,
   issued January 2002, provides the State Chief Information Officer with the authority to
   oversee, direct and coordinate the establishment of information technology policies,
   protocols and standards for State government, including hardware, software, security

   1 All references to Executive Order 117 refer to that which was originally issued by Governor George E. Pataki on January 28, 2002
   and continued by Executive Order 5 issued by Governor Eliot Spitzer on January 1, 2007, Executive Order 9 issued by Governor
   David A. Patterson on June 18, 2008, Executive Order 2 issued by Governor Andrew M. Cuomo on January 1, 2011 and Executive
   Order 6 issued by Governor Kathy Hochul on October 8, 2021.

   and business re-engineering. Details regarding this authority can be found in NYS ITS
   Policy, NYS-P08-002 Authority to Establish State Enterprise Information Technology
   (IT) Policy, Standards and Guidelines.

   Section 103-e of the State Technology Law (STL) requires publication of an annual
   inventory of state agency artificial intelligence systems by ITS by December 30. State
   agencies are required to submit information to ITS at least sixty (60) days in advance.

3.0 Scope
   This guideline applies to all “State Entities” (SE), defined as “State Government” in
   Executive Order 117 or “State Agencies” as defined in Section 101 of the State
   Technology Law. This includes employees and all third parties (such as local
   governments, consultants, vendors, and contractors) that use or access any Information
   Technology (IT) Resource for which the SE or ITS has administrative responsibility ,
   including systems managed or hosted by third parties on behalf of the SE or ITS.

   The AI system inventory will include AI systems, as defined by NYS-P24-001
   Acceptable Use of Artificial Intelligence Technologies Policy (AUAI Policy), in use by
   the SE, whether developed internally or acquired from external sources and used within
   the operational, analytical, or decision-making processes. Please see the AUAI Policy
   for further information, including the definition of AI systems and covered use details.

4.0 Information Statement
   Per the AUAI Policy and section 103-e of the STL, ITS is responsible for maintaining an
   inventory of AI systems in use by SEs. To assist in this effort, SEs will be provided
   access to an Excel workbook to provide information on AI systems currently in use.

   4.1    Submission Process

   Central to this initiative’s success is the role of an SE designated primary and secondary
   contact responsible for collecting and compiling all required AI system information. This
   centralized approach will ensure accuracy and completeness in the data collected and
   significantly reduce the potential for errors and duplications.
   The AI system inventory Excel workbook outlines the specific information that needs to
   be collected and recorded. Once the workbook is complete, the designated primary
   contact or secondary contact is to email it to the ITS Chief Data Office within 180 days
   of the issue date of this guideline (see Section 8.0 below). The contact information for
   this office is provided below.

   NYS-G25-001                                                                     Page 2 of 7

4.2      AI System Inventory Excel Workbook Information

      4.2.1 Workbook Structure

      The Excel workbook is organized with four separate Excel worksheets:

         ● Coversheet: This is for entering the primary and secondary contact names
           and Email addresses, for ITS purposes only.
         ● Instructions and examples: This is an informational worksheet that provides
           a data dictionary with column names transposed. It includes rows identifying
           what data will be collected for public AI inventory reporting, information stating
           if the data field is a drop-down menu choice or text (key entered), an example
           for each column heading, and an additional column showing if a field is
           required or only required if applicable/available.
         ● Drop-down menu choices and descriptions: This is an informational
           worksheet only providing the drop-down menu choices and their descriptions
           for help when completing the workbook. This is also included in Appendix A
           and B of this document.
         ● AI inventory worksheet: To be used to enter AI system inventory records. This
           worksheet includes a row entered as an example and information in the
           column name that indicates if a drop-down menu is to be used.

      4.2.2 Data Elements to be Collected in the AI System Inventory Worksheet:

         ● State entity/agency information:
               o State entity/agency name: The name of your state entity/agency. This
                  can be selected from a drop-down menu.
         ● AI system details:
               o AI system manufacturer and product name: Information identifying the
                  AI system’s manufacturer and product name, e.g., SampleAI is the
                  manufacturer of the NoNameSystem product.
               o AI capability: Primary capability category describing the ability of the
                  AI system to perform a function, with an additional field for a
                  description, if "other" is selected as a capability. The primary capability
                  field will have drop-down menu options to choose from.
                      ▪ Please see Appendix A of this document
               o Specific use case description: A brief narrative describing the purpose
                  and uses of the AI system within the SE.

4.3      Review, Validation, and Public Accessibility

ITS will review submissions for accuracy and completeness. This process may involve
requests for additional information or clarification. If further information or clarification is
needed, ITS will reach out to the primary and secondary contact identified on the AI
system inventory Excel workbook cover page.

NYS-G25-001                                                                          Page 3 of 7

    ITS will ensure that information from the AI system inventory collection is reported to
   the public, respecting confidentiality and integrity. This will include publishing the
   selected information from the inventory on the Open Data NY public platform, in
   accordance with section 103-e of the STL. When submitting their AI system inventory
   Excel workbook, SEs should provide a detailed explanation, in accordance with Articles
   6 and 6-A of the Public Officers Law, as to why they believe certain information
   contained within the workbook cannot be released publicly at the time of submission.
   ITS and the SE will work together to assess whether publication of this information is
   practicable until such time as a final decision is made; however, SEs are still required
   to submit the information to ITS to initiate this review process.

   ITS may withhold certain information from the AI system inventory collection pursuant
   to Article 6 or 6-A of the Public Officers law, including but not limited to, if it is deemed
   that disclosure of the information would jeopardize the capacity to guarantee the
   security of information technology assets, would interfere with a law enforcement
   investigation or reveal criminal investigative techniques or procedures, or would
   endanger the life or safety of a person.

   4.4    Confidentiality and Assistance

   Information within the AI system inventory will be treated with the utmost confidentiality
   and used solely for AI governance, risk management, and policy compliance purposes.

   For assistance or questions regarding the AI system inventory Excel workbook or
   submission process, please contact the ITS Chief Data Office at cdo@its.ny.gov.

5.0 Compliance
   This guideline shall take effect upon publication. ITS may amend its guidelines at any
   time.

6.0 Definitions of Key Terms
   Except for terms defined in this policy, all terms shall have the meanings found in the
   ITS Glossary.

7.0 Contact Information
   Submit all inquiries, requests, and the completed AI system inventory Excel workbook
                                             to:

                                       Chief Data Office
                                  Reference: NYS-G25-001
                       NYS Office of Information Technology Services
                                State Capitol, PO Box 2062
                                   Albany, NY 12220-0062

   NYS-G25-001                                                                        Page 4 of 7

                                 Email: cdo@its.ny.gov

       Statewide technology policies, standards, and guidelines may be found at the
                        following website: https://its.ny.gov/policies

8.0 Revision History
   This guidance document should be reviewed consistent with the requirements set forth
   in ITS-P24-003 Process for Establishing Information Technology Polices, Standards
   and Guidelines.

    Date            Description of Change                           Reviewer
    03/04/2025      Issued Guidance                                 CDO

9.0 Related Documents

   NYS-G25-001                                                                 Page 5 of 7

  Appendix A – AI System Capability Categories and Descriptions

                                       AI system capability descriptions (Capability:
AI system capability categories        The ability of the AI system or tool to facilitate
                                       or assist with the following)

Agriculture                            Monitoring crop health, optimizing resource usage,
                                       and predicting yields
Assistive Technology                   Helping individuals with disabilities    in various
                                       tasks
Automation                             Streamlining repetitive tasks and processes

Code Assistance                        Optimizing, debugging, generating, or testing code
                                       more efficiently and effectively
Content Creation                       Creating various forms of content, such as text,
                                       images, music, etc. (ex: GenAI like ChatGPT,
                                       DALL-E, or Claude)
Customer Service/Conversational AI     Improving customer interactions and satisfaction
                                       through automated support systems (ex: Virtual
                                       Assistant Chatbot)
Document     AI/Intelligent   Document Assisting humans in extracting, classifying, or
Processing (IDP)                       analyzing information from various types of
                                       documents.
Education                              Personalizing learning experiences, providing
                                       feedback, and automating administrative tasks
Energy                                 Optimizing energy consumption, managing power
                                       grids, and analyzing demand
Environmental Protection               Monitoring pollution levels, predicting potential
                                       environmental      changes,    and     facilitating
                                       management of natural resources
Finance                                Analyzing   market       trends    and     managing
                                       investments
Fraud Detection                        Identifying fraudulent activities or transactions (ex:
                                       Financial fraud, such as Medicaid fraud detection)
Health Care Diagnostics                Diagnosing diseases, predicting patient outcomes,
                                       and personalizing treatment plans
Image Recognition/Computer Vision      Identifying objects, people, or features within
                                       images or videos

NYS-G25-001                                                                  Page 6 of 7

                                      AI system capability descriptions (Capability:
AI system capability categories       The ability of the AI system or tool to facilitate
                                      or assist with the following)
Legal                                 Analyzing legal documents, predicting case
                                      outcomes, and automating routine legal tasks
Manufacturing                         Optimizing production processes, predicting
                                      equipment failures, and improving quality control
Monitoring and Surveillance (Cyber)   Continuously observing data to detect anomalies or
                                      potential issues (ex: EDR, MDR)
Natural Language Understanding        Extracting meaning and intent from human
                                      language (ex: Summarizing online meetings,
                                      language translation, etc.)
Process or Operation Optimization     Fine-tuning processes and allocating resources
                                      more effectively
Personalization                       Tailoring products, services, or experiences to
                                      individual preferences
Prediction/Predictive Analytics       Forecasting future events or outcomes based on
                                      historical data
Research and Development              Scientific research and innovation (Ex: Assisting
                                      scientists in analyzing unstructured data to discover
                                      new phenomena or relationships)
Sentiment Analysis                    Determining the sentiment or opinion expressed in
                                      text data
Speech/Text Recognition               Converting spoken language into text or text into
                                      spoken language
Transportation                        Optimizing traffic flow, managing logistics, and
                                      enabling autonomous vehicles
Other

NYS-G25-001                                                                 Page 7 of 7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
