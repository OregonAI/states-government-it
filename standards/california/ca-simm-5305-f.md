---
schema_version: 1
corpus: states-government-it
jurisdiction: california
id: ca-simm-5305-f
title: Generative Artificial Intelligence Risk Assessment
doc_type: standard
citation: SIMM 5305-F
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5305-F-Generative-Artificial-Intelligence-Risk-Assessment.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 35a51d145547d0063c6f679e8e4031a394f40c0fe3e246fb17e0d443da072785
effective_date: null
source_version: August 2025
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). source_version is the month, or the revision month, the document prints (a month with no day
  is not made into a date).
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Generative Artificial Intelligence Risk Assessment (SIMM 5305-F)

## At a glance

SIMM 5305-F, Generative Artificial Intelligence Risk Assessment: an item of the Office of Information Security's information security series (SIMM 5300), the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

        State of California
   Department of Technology
  Office of Information Security

      Generative Artificial
Intelligence Risk Assessment

          SIMM 5305-F

            August 2025

                                                  REVISION HISTORY

Revision                   Date of Release          Owner                       Summary of Changes
Initial Release            January 2024             California Office of        Initial Release of SIMM 5305-F
                                                    Information Security        Generative Artificial Intelligence Risk
                                                    - Payam Hojjat              Assessment
Minor Update               July 2024                California Office of        Added clarifying questions for GenAI
                                                    Information Security        regarding:
                                                    - Payam Hojjat              • Review and consultation.
                                                                                • State entity policies.
                                                                                • User training.
Major Update               February 2025            California Office of        • Updated Format
                                                    Information Security        • Restructured and revised questions
                                                    - Kory Fesliyan             • Added a new section to document
                                                                                   safeguards
                                                                                • Added a new section for data types
                                                                                • Updated risk assessment table
Minor Update               August 2025              California Office of        • Added Labor Relations
                                                    Information Security          Engagement
                                                    - Kory Fesliyan

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                       August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                              Page 2 of 28

                                                               Table of Contents
I.        Introduction ........................................................................................................................................ 4

II.       Risk Assessment - Part 1 .................................................................................................................. 5
                  Data Types .......................................................................................................... 6

III.      GenAI Risk Table Assessment Scale ............................................................................................... 7
                  Risk Assessment Questionnaire....................................................................... 8
                        Signatures and Acknowledge (Required Completion)..................................... 12

IV.       Risk Assessment - Part 2 ................................................................................................................ 13
                  Signatures and Acknowledge (Required Completion)..................................... 16

V.        GenAI Use Cases & Safeguard Samples........................................................................................ 17
                  Safeguards (Common) ..................................................................................... 17
                        Safeguards (Use-Case Specific)...................................................................... 19

VI.       Definitions ........................................................................................................................................ 27

VII.      References........................................................................................................................................ 27

VIII. Questions ......................................................................................................................................... 28

      Office of Information Security
      Generative Artificial Intelligence Risk Assessment                                                                                    August 2025
      SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                                           Page 3 of 28

I. Introduction

Generative Artificial Intelligence (GenAI) has the potential to improve the delivery of government services
and operations. GenAI enables enhancements to the development, adoption, and implementation of new
technologies to streamline and optimize business operations and state services to Californians. With that, it
is critical for entities to be cognizant to ensure that GenAI does not lead to a state in which human life,
health, property, or the environment is endangered, nor have public services be solely contingent upon
these systems. GenAI systems are to be used only to augment and improve workflows, not to replace or
impair the services received by the public.

As described in the State of California Report: Benefits and Risks of GenAI report, GenAI offers a wide
variety of potential applications with varying impacts. Any application of GenAI tools within the California
state government will adhere to appropriate protocols and testing procedures. To proactively address
potential threats to state-owned information assets, privacy, and the welfare of California's citizens, the
Statewide Information Management Manual (SIMM) 5305-F, GenAI Risk Assessment introduces a risk
assessment methodology that will aid state entities in evaluating the risks associated with GenAI systems.

This SIMM is to ensure alignment with:
   • Executive Order (EO) N-12-23
   • NIST Artificial Intelligence Risk Management Framework

Please note that a completed SIMM 5310-C Privacy Threshold Assessment and Privacy Impact Assessment
must be accessible upon request.

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                           August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                  Page 4 of 28

II. Risk Assessment - Part 1

Generative Artificial Intelligence Risk Assessment Part 1:
This section completed by the Chief Information Officer (CIO)
Instructions:
 • This risk assessment is required for all GenAI procurements, acquisitions, renewals and internally developed
    systems.
 • This risk assessment applies to free GenAI products and services, defined as any free software or service that
    interacts with state data. Examples include users entering state data into conversational GenAI platforms or
    installing GenAI plugins and extensions. However, this assessment does not apply in cases where state data is
    not being used, such as browsing the web with search engine GenAI results or using conversational GenAI
    systems where no state data is entered.
 • This risk assessment is required for existing GenAI tools that were acquired prior to the release of this
    document. These assessments must be retained and accessible by the entity as it may be requested during an
    information security program audit or assessment.
 • State entities complete SIMM 5305-F, Risk Assessment Part 1 to determine the level of risk associated with a
    GenAI system.
 • After completion, submit a Case via the New Technology Consultation and Assessment request, in the CDT IT
    Service Portal for all risk levels. When the request has been processed, a CDT Customer Engagement
    Services (CES) representative will reach out to provide a secure location to upload the required documents.
 • CDT reserves the right to audit and consult on "Low" GenAI Risk Levels with potential higher risk concerns.
 • Only complete SIMM 5305-F, Risk Assessment Part 2 if the GenAI system risk level is rated Moderate or High.
 • Important: Once completed, this form is confidential and may be exempt from disclosure pursuant to
    Government Code sections 7929.210 and 8592.45.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                               August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                      Page 5 of 28

Data Types
Select all that apply to identify the data types at risk. Take into account the potential impact to data types in
this risk assessment questionnaire (note: data types may overlap across categories).
☐ Personal Information (Privacy) or PII - Information       ☐ Confidential - Information maintained by state agencies that is
that can be used to distinguish or trace an individual’s    exempt from disclosure under the provisions of the California Public
identity, including those in accordance with Civil Code     Records Act (Government Code Sections 7923.75-7923.55, 7929.210,
1798.3 & 1798.29.                                           7930.000-7930.005, 7930.100-7930.215) or has restrictions on
                                                            disclosure in accordance with other applicable state or federal laws.
1.  ☐ Individual’s first name or initial and last name
2.  ☐ Date of Birth                                         1. ☐ Intelligence information in support of Homeland Security and
3.  ☐ Social Security Number                                    National Defense
4.  ☐ Physical description                                  2. ☐ Attorney/Client Privileged and/or Work Product
5.  ☐ Home address                                          3.  ☐ Controlled Technical Information (CTI) (e.g., Network security
                                                                info, diagrams, security & transaction logs, encryption keys)
6.  ☐ Telephone number
                                                            4. ☐ Intellectual property, such as patents, copyright, trade secrets
7.  ☐ Education
                                                            5. ☐ Proprietary
8.  ☐ Financial matters, including financial/bank
    account number, credit or debit card number, or any 6. ☐ Electronic Health Record (EHR) information subject to Health
    code that would permit access to an individual’s            Insurance Portability and Accountability Act (HIPAA) Privacy and
    financial account                                           Security Rules
9. ☐ Medical history and medical information                7.  ☐ Protected Health Information (PHI) subject to HIPAA Privacy or
                                                                Security Rules
10. ☐ Health data – other identifiable medical data not
    covered by Health Insurance Portability and             8. ☐ Medical information as defined by the California Confidentiality
    Accountability Act (HIPAA). (e.g., occupational             of Medical Information Act (CMIA)
    health, services qualification, personal health record) 9.  ☐ Family Educational Rights and Privacy Act (FERPA) data
11. ☐ Employment history                                    10. ☐ Federal Tax Information (FTI) subject to Internal Revenue
12. ☐ Statements made by & attributed to an individual          Service (IRS) Publication 1075 requirements
13. ☐ Driver’s license number                               11. ☐ Controlled Unclassified Information (CUI)
14. ☐ California identification card number                 12. ☐ Criminal Justice Information Services (CJIS) information
15. ☐ Tax identification number                             13. ☐ Department of Defense Covered Defense Information (CDI)
16. ☐ Passport number                                       14. ☐ Export Controlled Research information subject to International
                                                                Traffic in Arms Regulations (ITAR) and Export Administration
17. ☐ Military identification number
                                                                Regulations (EAR)
18. ☐ Other unique identification number issued on a
                                                            15. ☐ Sensitive data that requires a higher-than-normal assurance of
    government document commonly used to verify
                                                                accuracy and completeness
    identity of a specific individual
                                                            16. ☐ Other:
19. ☐ Security code, access code, password, and
    username/email address
20. ☐ Health insurance information
21. ☐ Unique biometric data, such as fingerprints,          ☐ Public Information - Information maintained by state agencies that
    retina, or iris scans, used for authentication          is not exempt from disclosure under the provisions of the California
22. ☐ Physical or digital photograph, if used or stored     Public Records Act, Government Code Sections 7929.210, or other
    for facial recognition purposes                         applicable state or federal laws.
23. ☐ Information collected through automated license
                                                            1. ☐ Non-Human Research Data (Animals, etc.)
    plate recognition systems (GC Section 1798.90.5).
                                                            2. ☐ Other Program-Related Research Data
24. ☐ Genetic data
                                                            3. ☐ Aggregated Data (Census, traffic, crime, etc.)
25. ☐ Personal data as defined by European Privacy
    Law (EEA and UK GDPR)                                   4. ☐ Federal Acquisition Regulations information other than CUI
26. ☐ Special data as defined by EEA and UK GDPR            5.  ☐ Sensitive data that requires a higher-than-normal assurance of
                                                                accuracy and completeness
27. ☐ Other:
                                                            6. ☐ Other:

     Office of Information Security
     Generative Artificial Intelligence Risk Assessment                                                           August 2025
     SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                  Page 6 of 28

III. GenAI Risk Table Assessment Scale

This table categorizes a system's risk level by evaluating the GenAI system's nature (use case), data type,
and potential impact (FIPS 199) of a security breach, with the highest applicable category determining the
overall risk level. For example, FIPS 199 Low + Mission Related (Moderate) + Processes confidential data
(High) would result in a risk level of high based on the use case examples.

    FIPS 199 Impact                                 Data Type                                       Use Case Examples
           HIGH              Confidential/Personally Identifiable Information             • Inputs and processing of confidential data,
           (Red)             • The data inputs, activities, and outputs involve including data that identifies or describes
 Depending on the nature       processing Personally Identifiable Information (PII)         an individual, authentication, biometric
 & sensitivity of the          or confidential data.                                        identification, financial, medical,
 affected systems or                                                                        procurement, investigative, national
                             Safety Related                                                 security, network architecture schematics,
 information, losses
                             • The data inputs, activities, and outputs support ports, protocols, and others.
 related to confidentiality,
                               decision-making processes that impact public • Inputs and processing of data that inform
 integrity, & availability
                               safety.                                                      safety decisions, such as water treatment
 may still result in severe
 or catastrophic adverse                                                                    ratios, load-bearing specifications for
 impacts                                                                                    bridges, and similar critical information.
        MODERATE             Decision Related, Non-Confidential/Non-PII                   • Code Analysis & Development Tools (e.g.,
           (Yellow)          Related, Resident (Public) Related                             static and dynamic code analysis, code
 Depending on the nature     • The  data  inputs, activities, and   outputs  are  non-PII   generation tools, code assistant tools,
 & sensitivity of the          and  non-confidential   but lead  to  decision  making  in   platforms used to create GenAI solutions).
 affected systems or           public (resident)  programs    and  services.              • Chatbots (e.g., internal chatbots for
 information, losses                                                                        resource finding and process advice,
                             Decision Related, Non-Confidential/Non-PII
 related to confidentiality, Related, Not Validated                                         resident-facing chatbots for public
 integrity, & availability                                                                  interaction and information retrieval).
                             • The data inputs, activities, and outputs are non-PII, • Public & Direct Contact Services (e.g.,
 may still result in serious
                               non-confidential, and support decision-making, but
 adverse impacts                                                                            customer service, public relations,
                               the GenAI model/output lacks verification by a
                                                                                            jurisprudence, output providing
                               qualified subject matter expert against the original
                                                                                            recommendations such as legal, tax,
                               data source used by the GenAI.
                                                                                            regulatory information).
                             Mission Related, Resident (Public) Facing Web                • Critical Infrastructure & Safety (e.g.,
                             Apps                                                           handling mission-critical apps/systems,
                             • The data inputs, activities, and outputs involve service eligibility assessments for housing
                               mission-critical, state-critical, critical infrastructure,   or income assistance, drafting
                               or public-facing systems.                                    organizational documents, generating data
                                                                                            for public use like soil composition or
                                                                                            seismic considerations).
             LOW             Non-Decision Related, Non-Confidential/Non-PII               • Network & Security Tools (e.g., packet
           (Green)           Related                                                        inspection, system monitoring, intrusion
 Depending on the nature • The data inputs, activities, & outputs are non-PII,              prevention/detection, spam filtering tools,
 & sensitivity of the          non-confidential,   &   neither   involve   nor   lead  to   malware detection tools like anti-virus, anti-
 affected systems or           decision-making       throughout       the     end-to-end    malware, & endpoint detection &
 information, losses           business  process                                            response).
 related to confidentiality, Decision Related, Non-Confidential/Non-PII                   • Content & Communication Tools (e.g.,
 integrity, & availability                                                                  grammar correction tools, summarization
                             Related, Validated
 may still result in limited                                                                tools, reference generating tools like laws,
                             • The data inputs, activities, and outputs are non-PII, case law, policies, translation tools, text to
 adverse impacts
                               non-confidential, and support decision-making, with          speech, & content creation tools for image,
                               the original data source of the GenAI output verified        video, ads, and marketing).
                               by a qualified subject matter expert.

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                                                     August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                            Page 7 of 28

Risk Assessment Questionnaire

GenAI Description and Use Case:
(a) What is the vendor’s name that offers the GenAI?

 (b) What is the application and/or product name?

 (c) What is the model and version of the product?

 (d) What is the license tier of the GenAI product, if applicable (free, enterprise, platinum, etc.)?

 (e) How is the GenAI solution delivered: IaaS, PaaS, SaaS, or will it be deployed on-premises?
    (Indicate if this is a thin client, thick client, web extension, plugin, etc.)

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                                   August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                          Page 8 of 28

(f) What is the current end-to-end business process?
   (Provide a brief overview of the workflow that is currently being performed).

(g) Which aspects of the end-to-end business process will the GenAI support AND how will you use GenAI?
   (Provide a brief overview of what the GenAI solution will replace, enhance, or introduce as a new functionality
   and/or services. If only certain features will be enabled, explain their purpose and use in detail.)

 Office of Information Security
 Generative Artificial Intelligence Risk Assessment                                                   August 2025
 SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                          Page 9 of 28

(h) What safeguards will be deployed with this GenAI product?

Work with your security teams to identify safeguards that apply. Review section V - GenAI Sample Safeguards to
help complete this section if applicable. Please note that CDT Safeguards are inherited when CDT managed
services are used.
    • For example: Safeguard: Will ensure all GenAI input and output data is validated by an adequately qualified
       subject matter expert.
    • State agencies/entities must consider their own tailored mitigation processes and procedures specific to their
       GenAI product.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                  August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                         Page 10 of 28

(i) What GenAI features of this product will be disabled,        (j) Will there be tailored training and specific rules of
      if any (e.g., incidental GenAI features that come with         engagement for stakeholders to ensure proper
      renewals but will be disabled)?                                usage of the system, with adherence required for
                                                                     each use case?
                                                                 ☐ Yes
                                                                 ☐ No

FIPS 199 Categorization Level: to be completed by ISO or equivalent
All GenAI data must be taken into context, and an associated categorization must be given based on the highest
severity. This includes prompt data, output data, data source, training data, etc.
 (a) Is the GenAI tool being used for mission-critical applications or processes? Briefly explain.

(b) Confidentiality: What is the potential impact to the organization if this system results in unauthorized
    disclosure of information.
Level (choose only one):                                    Impact Description:

☐ High
☐ Moderate
☐ Low

(c) Integrity: What is the potential impact of unauthorized modification or destruction of information.
Level (choose only one):                                    Impact Description:

☐ High
☐ Moderate
☐ Low

(d) Availability: What is the potential impact of disruption to the availability of the system or its services.
Level (choose only one):                                     Impact Description:

☐ High
☐ Moderate
☐ Low

(e) Based on the responses to the FIPS 199 Categorizations, what is the overall level of the protection for this
    system/application/service?
FIPS 199 - Protection Level Needed (choose only         Comments or additional notes (if any):
one):

☐ High
☐ Moderate
☐ Low

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                           August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                  Page 11 of 28

GenAI Risk Level: According to section III. GenAI Risk Table Assessment Scale, what is the highest risk level
based on the FIPS 199 System Categorization, Data Type, and Use Case? (CDT reserves the right to audit and
consult on "Low" GenAI Risk Levels with potential higher risk concerns)
                              ☐ Low                 ☐ Moderate           ☐ High
Safeguard Level: Based on the safeguards in (h), what level of safeguards have been identified for implementation
for this GenAI system.
 ☐ Not Identified - Safeguards have not yet been reviewed or considered for this system or use case
 ☐ Partially Identified - Some safeguards have been recognized, but further evaluation is needed
 ☐ Mostly Identified - Most safeguards have been identified, with minor gaps remaining
 ☐ Fully Identified - All safeguards have been identified and documented for implementation
 ☐ Not Applicable - Safeguards are deemed unnecessary or irrelevant for this system or use case

Signatures and Acknowledgement (Required Completion)
Required Signatures for Risk Assessment Part 1
You are required to ensure that the Acceptable Use Policy is updated to address GenAI. A completed SIMM 5310-C
Privacy Threshold Assessment and Privacy Impact Assessment must be accessible upon request. If additional GenAI
features are enabled in the future beyond those outlined in this document, a new SIMM 5305-F must be submitted for
review.

By signing this document, the signatory is confirming that the state entity certifies the intended GenAI use case, its risk
level, and understands that all procurements are mandated to comply to all CDT-published security and privacy policies
(SAM Sections 5100 and 5300 - 5399).
Labor Relations Engagement
California state hiring authorities are responsible for ensuring that the implementation of changes affecting state
employees’ terms and conditions of employment complies with relevant policies and codes. For specific guidance on
applicable labor relations policies and procedures, please coordinate with your labor relations office or CalHR Labor
Relations.

☐ As the CIO (or equivalent), I acknowledge that our Department's Labor Relations officer (or equivalent) has received
and reviewed a copy of this 5305-F Risk Assessment form.

_______________________                                          _______________________
ISO Name (print)                                                 CIO Name (print)

_______________________                 ___________              _______________________            ___________
ISO Signature (or equivalent)           Date                     CIO Signature (or equivalent)      Date

    End of Risk Assessment Part 1 – Only continue if the GenAI Risk Assessment is Moderate or High.

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                                       August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                              Page 12 of 28

IV. Risk Assessment - Part 2

 Generative Artificial Intelligence Risk Assessment Part 2:
 This section completed by the Chief Information Officer (CIO)
 Instructions:
  • State entities complete this form when required.
  • Complete SIMM 5305-F, Part 2 if the GenAI system risk level is rated Moderate or High.
  • After completion, submit a Case via the New Technology Consultation and Assessment request, in the CDT IT Service
      Portal for all risk levels. When the request has been processed, a CDT Customer Engagement Services (CES)
      representative will reach out to provide a secure location to upload required documents as part of the GenAI consultation
      process.
  • Important: Once completed, this form is confidential and may be exempt from disclosure pursuant to Government Code
      sections 7929.210 and 8592.45.
 Mandatory Minimum Safeguards:
 Instructions:
  • Checkmark all the safeguards your system is in compliance with. All safeguards must be met and will be discussed with
      CDT during consultation for compliance.
 Yes      No     N/A
          ☐       ☐
                         The GenAI system workflow includes human verification to ensure accuracy and
  ☐                      factuality of the output.
  ☐       ☐       ☐      The GenAI system will not have the potential to degrade public services.

  ☐       ☐       ☐
                         The GenAI system will not adversely impact the availability of resources and services
                         provided by the State of California.

  ☐       ☐       ☐
                         If the GenAI system is a shared system, is there an existing data-sharing agreement
                         between parties including roles & responsibilities for data owner, custodian, user, etc.?

  ☐       ☐       ☐
                         User accounts for the GenAI tool is managed by a state-owned identity access and
                         management tool (e.g. Active Directory).
                         Business services are not contingent on the system's use. In the event of system
  ☐       ☐       ☐      failure or inaccurate results, the State of California can continue to provide the same
                         level of services without disruption.

  ☐       ☐       ☐
                         The state entity has safeguards in place to protect data used by the GenAI tool from
                         being exposed to the internet.

  ☐       ☐       ☐
                         The state entity uses safeguards that comply with the state-defined security
                         parameters for NIST SP 800-53, SIMM 5300-A, and SAM Section 5300.5.
                         Cloud-based GenAI systems comply with Cloud Computing Policy SAM 4983.1 and
  ☐       ☐       ☐      Cloud Security Guide SIMM 140, which states that all data will remain in the United
                         States and that no remote access will be allowed outside of the United States.

  ☐       ☐       ☐
                         All remote access uses Multi-Factor Authentication (MFA) and complies with the
                         Telework and Remote Access Security Standard (SIMM 5360-A).
                         All confidential, sensitive, or personal information is encrypted in accordance with
  ☐       ☐       ☐
                         SAM 5350.1 (Encryption) and SIMM 5305-A (Information Security Program
                         Management Standard) and at the necessary level of encryption for the data
                         classification pursuant to SAM 5305.5 (Information Asset Management).
                         All data, hardware, software, internal systems, and essential third-party software,
  ☐       ☐       ☐      including for on-premises, cloud, and hybrid environments, are aligned with a zero-
                         trust architecture model in accordance with NIST 800-27.

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                                             August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                    Page 13 of 28

         ☐      ☐
                       All data is subject to Civil Code 1798.99.80 – 1798.99.89 and will not be sold or
☐                      advertised to data brokers.
                       Unless specified in the contract, prompts or Generated Data resulting from such
                       Prompts constitute a Work Product. Contractors may not use, copy, modify, distribute,
 ☐       ☐      ☐      or disclose any such Prompts or Generated Data for any purpose other than
                       performing their obligations under the Contract unless expressly authorized by the
                       State in writing.

 ☐       ☐      ☐
                       To the extent any Prompts or Generated Data constitute Work Product, the State will
                       retain Government Purpose Rights.

 ☐       ☐      ☐
                       The GenAI system will opt out of any data collection and model training features that
                       may be used to train commercial instances of GenAI systems.
                       GenAI output will not infringe on copyright or intellectual property laws and is
                       compliant with open-source licenses, if applicable. GenAI output will be cited (from
 ☐       ☐      ☐      credible sources) if any statements used as facts are generated and published for
                       consumer use. All generated images and videos will cite any GenAI used in their
                       creation, even if the images are substantially edited afterward.
                       The GenAI system will not spoof or engage in fraud, including deepfake creation,
 ☐       ☐      ☐      impersonation, phishing, other social engineering, or manipulation of other GenAI
                       systems.

 ☐       ☐      ☐
                       The GenAI system is designed to avoid generating or creating illicit content that may
                       be controversial, subjective, or potentially not widely accepted by the public.

 ☐       ☐      ☐
                       The GenAI system will not improperly systematically, indiscriminately, large-scale
                       monitor, surveil, or track individuals.

Details of Transparency:
(a) What mechanism will the GenAI system use to                  (b) What mechanisms can be used to audit the system
     notify a user that they are interacting with a GenAI             and its data?
     system rather than a human?

(c) How will the system disclose to the customer                 (d) How will customers receive an output, and what
     that the data generated is by GenAI? (e.g.                       is the mechanism to correct or appeal an error?
     watermark, banner)

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                     August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                            Page 14 of 28

Human Oversight and Monitoring:
(a) How will system owners identify and mitigate                 (b) Will the system be publicly accessible or only within
      hallucinations and that data outputs are accurate                 a state-managed environment? Who is the intended
      and factual? What ability will system owners have to              audience, and will it impact a specific group of
      accept, reject, and correct data?                                 individuals or communities? Briefly explain.

(c) How will system owners test, evaluate, and verify            (d) Will logs be available in a non-proprietary format,
      that the GenAI system’s original designated GenAI                 that can be ingested into a Security Information and
      Risk Level will or has not changed? (e.g., changes                Event Management (SIEM) tool? Briefly explain.
      to use, data, privacy, cost)

Ensuring Equity:
(a)   Does the output of the system make decisions that           (b)   Will the output of the system make decisions that
      impact access to, or approval for, housing or                     factor in the Diversity, Equity, Inclusion, and
      accommodations, education, employment, credit,                    Accessibility (DEIA) of individuals? Briefly explain.
      health care, or criminal justice? If so, please
      describe.

(c)   Will the system impact a minor under the age of 18?         (d)   Will system decisions impact public safety? (e.g.,
      Briefly explain.                                                  water pollution metrics)? Briefly explain.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                             August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                    Page 15 of 28

Signatures and Acknowledgement (Required Completion)
Required Signatures for Risk Assessment Part 2
You are required to ensure that the Acceptable Use Policy is updated to address GenAI. A completed SIMM 5310-C
Privacy Threshold Assessment and Privacy Impact Assessment must be accessible upon request. If additional GenAI
features are enabled in the future beyond those outlined in this document, a new SIMM 5305-F must be submitted for
review.

By signing this document, the signatory is confirming that the state entity certifies the intended GenAI use case, its risk
level, and understands that all procurements are mandated to comply to all CDT-published security and privacy policies
(SAM Sections 5100 and 5300 - 5399).
Labor Relations Engagement
California state hiring authorities are responsible for ensuring that the implementation of changes affecting state
employees’ terms and conditions of employment complies with relevant policies and codes. For specific guidance on
applicable labor relations policies and procedures, please coordinate with your labor relations office or CalHR Labor
Relations.

☐ As the AIO (or equivalent), I acknowledge that our Department's Labor Relations officer (or equivalent) has received
and reviewed a copy of this 5305-F Risk Assessment form.

______________________                                         ______________________
AISO Name (print)                                              AIO Name (print)

______________________                  ___________            ______________________                ___________
AISO Signature (or equivalent)          Date                   AIO Signature (or equivalent)          Date

                                         End of Risk Assessment part 2

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                                       August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                              Page 16 of 28

V. GenAI Use Cases & Safeguard Samples
The following section lists high-level categories for the wide variety of functionality for GenAI with sampled
public sector use cases. The example use cases are only intended to help illustrate the potential uses for
state government adoption of GenAI tools.
While these use cases and safeguards offer a solid foundation for mitigating risks associated with GenAI tools,
state entities are required to tailor their approach to the specific use cases and products that they employ.
Given the diverse range of GenAI applications and their associated risks, it is crucial to conduct a thorough
risk assessment for each specific use case. By analyzing factors such as system categorization, data type
and business process, entities can optimize their security posture and minimize potential risks.

Safeguards (Common)
This section outlines a list of general risks along with their corresponding safeguards. These risks are not tied to any
specific use case. State agencies/entities should review this section in conjunction with the section relevant to their
specific use case to gain a better understanding of potential risks and their mitigation strategies.

 Common Safeguards
 Risk: Inadvertent exposure of           Mitigation: Anonymize or obfuscate sensitive information before inputting it into
 sensitive or confidential               GenAI systems.
 information, either through data        Mitigation: Implement strict role-based access to GenAI platforms and their
 input, processing, storage, or          outputs, limiting access to GenAI tools and data to authorized personnel,
 generated outputs.                      enforcing the principle of least privilege.
                                         Mitigation: Use end-to-end encryption for all data interactions with GenAI tools.
                                         Mitigation: Apply data masking or redaction to sensitive data before processing
                                         it through GenAI tools.
                                         Mitigation: Avoid using third-party or public GenAI solutions for sensitive use
                                         cases.
                                         Mitigation: Ensure acceptable use policies include a data handling component
                                         that addresses the use of sensitive and confidential information with publicly
                                         available GenAI tools; including the use of internally hosted generative AI tools
                                         that are on commercial clouds that could still expose that data to the internet.
                                         Mitigation: Review vendor privacy statements to identify what type of
                                         information is being shared with affiliates and that privacy and confidential data
                                         does not get shared.
                                         Mitigation: Use vendors with clear data protection and non-retention policies.
                                         Mitigation: Obtain copies of vendor certificates to ensure their stated security
                                         compliance matches their security certificate (e.g., vendor claims SOC Type2
                                         compliance but uses a certificate from their hosting provider and not their own).
                                         Mitigation: Review data sharing statements to ensure data transmitted does not
                                         leave the continental United States.
                                         Mitigation: Review vendor privacy statements to ensure that the data is
                                         encrypted in transmit and at rest.
                                         Mitigation: Opt for in-house or private cloud-based GenAI solutions when
                                         handling sensitive data.
                                         Mitigation: Require review of outputs by network security professionals to
                                         ensure that no sensitive details are unintentionally revealed or misrepresented.
                                         Mitigation: Deploy GenAI tools in isolated, secure environments without
                                         external internet connectivity to prevent data leaks.
                                         Mitigation: Train employees about appropriate usage and discourage inputting
                                         personal or sensitive data.

   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                                       August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                              Page 17 of 28

Risk: GenAI may produce errors,         Mitigation: Require subject matter expert (SME) review and approval of all
inconsistencies, or outputs that do     outputs before implementation.
not align with the business             Mitigation: Use well-curated, domain-specific datasets to improve the model's
context, leading to flawed              understanding and accuracy.
decisions.                              Mitigation: Integrate tools to validate outputs for correctness and alignment with
                                        predefined rules.
                                        Mitigation: Perform regular audits of GenAI-generated data to ensure continued
                                        accuracy and to detect any emerging errors or discrepancies.
                                        Mitigation: Include metadata or disclaimers with summaries indicating potential
                                        limitations or areas requiring manual review.
                                        Mitigation: Review laws and regulations to ensure that GenAI tools are
                                        following disclosures and disclaimers from regulatory entities (government
                                        codes, assembly bills, election laws, etc.)
                                        Mitigation: Allow users to flag inaccuracies and provide feedback for system
                                        improvement.
                                        Mitigation: Configure the tools to provide links back to the source material.
                                        Mitigation: Train staff on how to verify outputs for accuracy and find source of
                                        truth.
                                        Mitigation: Use a curated set of validated responses for frequently asked
                                        questions.
Risk: Outputs may reflect biases        Mitigation: Regularly audit GenAI systems for bias and apply techniques to
present in the training data,           reduce bias in outputs.
leading to unfair or discriminatory     Mitigation: Ensure datasets are inclusive, representative, and free of systemic
results.                                bias.
                                        Mitigation: Use explainable AI (XAI) techniques to assess and justify outputs.
                                        Mitigation: Provide clear and transparent mechanisms for individuals to appeal
                                        decisions made using GenAI tools.
                                        Mitigation: Involve DEIA professionals in the review and validation of outputs
                                        used for decision-making.
                                        Mitigation: Use representative test cases to evaluate the model's behavior
                                        across different demographics or situations.
Risk: Excessive dependence on           Mitigation: Combine human expertise with GenAI insights rather than fully
GenAI could reduce human                automating decisions.
oversight and critical thinking,        Mitigation: Educate users on the limitations of GenAI and the importance of
increasing susceptibility to            maintaining human judgment.
undetected errors.                      Mitigation: Establish manual processes to take over in case GenAI fails or
                                        outputs unreliable results.
                                        Mitigation: Use models that provide clear explanations for their decisions to
                                        enable better oversight.
                                        Mitigation: Implement new GenAI-driven decision-making systems in controlled
                                        environments before full deployment to evaluate reliability and fairness.
Risk: GenAI systems and their           Mitigation: Host GenAI systems in secure environments with firewalls, intrusion
outputs may be targeted by              detection, and vulnerability scanning.
attackers to steal or manipulate        Mitigation: Conduct periodic reviews to identify and address vulnerabilities in
sensitive information.                  GenAI systems.
                                        Mitigation: Limit the flow of sensitive data to only the required systems and
                                        processes.
Risk: GenAI outputs may                 Mitigation: Use automated tools to validate GenAI outputs against relevant laws
unintentionally breach compliance       and standards.
with laws and regulations, e.g.,        Mitigation: Have legal teams review processes and outputs that may affect
data privacy regulations,               compliance.
procurement standards.                  Mitigation: Maintain detailed documentation of how data is processed by GenAI
                                        to ensure auditability.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                       August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                              Page 18 of 28

Risk: GenAI-generated content       Mitigation: Use plagiarism detection tools to ensure outputs are unique.
may unintentionally replicate       Mitigation: Train models only on licensed, public domain, or organizationally
copyrighted material or proprietary owned datasets.
information from training data.     Mitigation: Include IP experts to review outputs for potential infringement risks.
Risk: Outputs may include           Mitigation: Implement safeguards to identify and block offensive or
insensitive, offensive, or harmful  inappropriate outputs.
content, leading to ethical         Mitigation: Transparently disclose the use of GenAI and its role in decision-
concerns or reputational harm.      making.
                                    Mitigation: Use diverse and representative datasets to train GenAI to minimize
                                    the risk of generating harmful stereotypes.
                                    Mitigation: Have culturally aware reviewers assess content targeted at specific
                                    demographics.
Risk: It may be unclear who is      Mitigation: Establish clear policies assigning responsibility for validating and
accountable for errors or harm      approving GenAI outputs.
caused by GenAI-generated           Mitigation: Maintain logs that track who used the GenAI system, what inputs
outputs.                            were provided, and how outputs were utilized.
                                    Mitigation: Periodically assess the system's performance and outputs to identify
                                    areas for improvement.
Risk: The computational demands Mitigation: Use lightweight GenAI models or distributed processing to reduce
of GenAI-based solutions (e.g.,     system impact.
processing large datasets or        Mitigation: Implement tools to monitor and manage resource utilization in real
analyzing complex code samples) time.
might strain system resources,      Mitigation: Ensure backup systems are available in case of resource
leading to reduced system           exhaustion during high-demand periods.
performance or slower response
times.
Risk: The public (residents) may    Mitigation: Integrate tools that provide clear explanations of how eligibility
struggle to understand the          decisions were made.
reasoning behind GenAI-             Mitigation: Maintain detailed logs of input data, the model’s decision process,
generated eligibility               and outcomes for auditability and accountability.
determinations, leading to          Mitigation: Ensure eligibility decisions are conveyed in a clear and accessible
confusion or mistrust.              manner to applicants.
                                    Mitigation: Ensure all GenAI input and output data is validated by an adequately
                                    qualified subject matter expert.
Risk: The GenAI may not be fully Mitigation: Ensure the GenAI tool complies with accessibility standards, such
accessible to individuals with      as WCAG, to accommodate users with disabilities.
disabilities or may fail to support Mitigation: Provide support for multiple languages or dialects, depending on the
diverse user groups effectively.    demographic it serves.
                                    Mitigation: Conduct user testing with diverse groups to optimize ease of use
                                    and accessibility.
Risk: GenAI might fail to identify  Mitigation: Implement clear rules for escalating complex or sensitive
when an issue or interaction        interactions to human agents.
requires escalation to a human      Mitigation: Use intent recognition models to identify and flag interactions that
representative, leading to          may require escalation.
unresolved or improperly handled Mitigation: Collect user feedback to identify gaps in the escalation process and
situations.                         improve the system.

Safeguards (Use-Case Specific)
Grammar correcting tools
e.g., grammar assistant tools, rewording and revising text, providing alternative text

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                    August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                           Page 19 of 28

Risk: Inadvertently exposing data       Mitigation: Host the tools internally on the state network.
to the internet due to working with     Mitigation: Leverage API instead of working directly with the vendor’s website.
sensitive and confidential              Mitigation: Update acceptable use policy to address data handling of sensitive
information throughout the course       and confidential information with grammar correcting tools.
of work.                                Mitigation: Disable the tool by default and allow user to enable as needed.
                                        Mitigation: Read privacy statements to identify what type of information gets
                                        processed by the vendors cloud, how long it is stored, and how it gets deleted.
                                        Mitigation: Purchase the right license level that gives the state more
                                        configuration options over the tools.
                                        Mitigation: Negotiate and redline contracts on data collection and data sharing
                                        with vendors to minimize the data exposure.

Mission, State, or Critical Infrastructure
e.g., handling systems classified as mission, state, or critical infrastructure
Risk: Tools may be hosted in an      Mitigation: Ensure that the safeguards implemented match the level of the
environment with insufficient        criticality of the mission, state, or critical infrastructure (e.g., mission critical web
safeguard that expose mission,       apps at moderate safeguards replicate to a moderate development
state, or critical infrastructure.   environment).
                                     Mitigation: Segment the network so that systems categorized as low, moderate,
                                     and high have security zones that match low, moderate, and high safeguards.
                                     Mitigation: Adopt a Zero Trust security model, where every interaction with
                                     critical infrastructure—whether initiated by GenAI or a human operator—
                                     requires verification before granting access.
                                     Mitigation: Implement comprehensive logging and monitoring of GenAI
                                     activities within mission-critical apps/systems, including auditing interactions
                                     that involve sensitive configuration or system design tasks.

Network Analysis Tools
e.g., packet inspection, system monitoring, intrusion prevention/detection
Risk: GenAI models could               In addition to the safeguards given for inaccuracies in GenAI performance in
generate false positives               Common Risks/Safeguards section, consider the following:
(incorrectly flagging benign           Mitigation: Regularly retrain GenAI models using updated threat intelligence to
activities as threats) or false        reduce false positives and false negatives.
negatives (failing to detect actual    Mitigation: Implement a human review process for flagged threats to validate
threats), potentially undermining      or dismiss potential issues.
the reliability of intrusion detection Mitigation: Fine-tune detection thresholds based on feedback and observed
and prevention systems.                network behavior to reduce incorrect alerts.

Spam and Malware Detection
e.g., web gateway filtering, email gateway filtering
e.g., anti-virus, anti-malware, endpoint detection & response
Risk: GenAI models may                In addition to the safeguards given for the risk of inaccuracies in GenAI
incorrectly identify legitimate       performance in Common Risks/Safeguards section, consider the following:
emails, web content, and files as     Mitigation: Implement mechanisms for users to report false positives and retrain
spam or malware, causing              the model based on this feedback.
disruptions to business               Mitigation: Allow for exceptions through whitelisting of critical email addresses,
communications and workflows.         domains, web content, or files.
Risk: The model may fail to detect In addition to the safeguards given for the risk of inaccuracies in GenAI
sophisticated spam, phishing          performance in Common Risks/Safeguards section, consider the following:
attempts, malicious content, or       Mitigation: Combine traditional rule-based filtering with GenAI models to
malware potentially leading to        improve detection accuracy.
security breaches.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                           August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                  Page 20 of 28

                                        Mitigation: Continuously retrain GenAI with up-to-date spam, phishing patterns,
                                        and malware samples to identify evolving threats.
                                        Mitigation: Augment spam filtering and malware detection solutions with tools
                                        that monitor for malicious activity post-delivery (e.g., link-click analysis, sandbox
                                        execution).
Risk: Attackers may deliberately        Mitigation: Regularly test the spam filter and malware detectors against
craft spam or malicious content to      adversarial examples to ensure robustness.
bypass GenAI filters and poison         Mitigation: Vet incoming training data to avoid incorporating malicious or
the model’s learning process,           misleading inputs.
reducing its effectiveness.             Mitigation: Use isolated environments to test model updates before deploying
                                        them into production.

Reference Generating Tools
e.g., laws, case law, judgements, policies, procedures
Risk: GenAI tools may generate    Mitigation: Continuously update the training data with the latest legal, policy,
references based on outdated            and procedural information.
laws, policies, or judgments, or        Mitigation: Validate generated references against official or authoritative
omit critical updates, leading to       sources before use.
incorrect or incomplete advice.         Mitigation: Include metadata indicating when the reference was last verified to
                                        highlight potential currency issues.
Risk: GenAI may generate                Mitigation: Train GenAI models with data specific to the relevant contexts.
references that are applicable to a     Mitigation: Require users to provide jurisdictional or contextual information to
different jurisdiction or context,      guide GenAI outputs.
leading to misapplication of laws       Mitigation: Require legal experts to confirm applicability and accuracy of
or policies.                            references in the given context.

Content Creation Tools
e.g. image creators, video creators, ads, marketing
Risk: GenAI tools may collect and Mitigation: Redline contracts to minimize data collection.
process personal data, which          Mitigation: Review license levels to identify if there are product versions that
could be vulnerable to breaches.      enable administrative configuration by state staff to restrict data collection.
                                      Mitigation: Use template contracts that do not have personal, proprietary or
                                      organizational information.
Risk: GenAI tools may produce         Mitigation: Establish clear organizational policies for acceptable content
content that is misleading,           creation, ensuring compliance with advertising standards and consumer
manipulative, or violates ethical     protection laws.
marketing practices, potentially      Mitigation: Require a review process to validate that content aligns with ethical
harming trust or misleading           and legal standards before publication.
consumers.                            Mitigation: Disclose when content has been AI-generated to maintain trust.
                                      Mitigation: Prepare plans to mitigate fallout from potential reputational harm
                                      caused by AI content.

Translation Tools
e, g., meeting summarization, audio/video to text
Risk: AI tools may collect and      In addition to the safeguards given for the risk implying inadvertent exposure of
process sensitive information,      sensitive information given in Common Risks/Safeguards section, consider the
such as personal conversations      following:
and proprietary business data.      Mitigation: Obtain consent before recording meetings.
                                    Mitigation: Limit how long audio, video, and transcription data are stored and
                                    ensure proper deletion protocols.
  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                          August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                                 Page 21 of 28

Generative AI Platforms & Code Analysis
e.g., static and dynamic code analysis, code generation tools, code assistant tools
e.g., developer tools
Risk: AI models can introduce        Mitigation: Generate small batches of code at a time and have staff review it
bugs and backdoors over time, or to ensure that they understand everything that is being generated.
do not adhere to best practices of   Mitigation: Avoid generating thousands of lines of code that can’t be
security (e.g., lack of input        thoroughly inspected.
validation, hardcoding credentials) Mitigation: Add comments to each line of code that is AI generated that
                                     explains what it is doing to confirm staff understand the code that was
                                     generated.
Risk: mismatched safeguard           Mitigation: Deploy the same level of safeguards as the systems that are
levels with supported computing      being supported.
resources (e.g., development         Mitigation: Sanitize data being used in development environments.
server has Low safeguards, but       Mitigation: Implement strong access controls and strong authentication
the supported systems are            mechanisms to limit unauthorized access to LLM model repositories and
classified as moderate, thereby      training environments.
exposing moderate development        Mitigation: Restrict the LLMs access to network resources, internal services
(e.g., code, data records) in the    and API's.
development environment with         Mitigation: Regularly monitor and audit access logs and activities related to
Low safeguards.                      LLM model repositories to detect and respond to any suspicious activities.
Risk: Developers may over-rely       Mitigation: Require thorough documentation of all AI-generated code to
on AI-generated code, leading to     promote understanding and accountability.
reduced understanding of             Mitigation: Encourage collaborative review processes where one developer
underlying logic and potential       writes while another reviews the code (pair programming).
propagation of errors.
Risk: AI-generated code may          Mitigation: Use tools to identify and validate the security and maintenance
suggest or introduce third-party     status of suggested dependencies.
libraries or dependencies that are Mitigation: Restrict AI tools to a pre-approved list of secure and well-
outdated, insecure, or poorly        maintained libraries.
maintained.                          Mitigation: Regularly review third-party dependencies in generated code for
                                     vulnerabilities.
Risk: AI-generated code might        Mitigation: Use automated tools to check generated code for licensing
inadvertently replicate copyrighted conflicts.
material or violate licensing terms, Mitigation: Ensure AI models are trained on datasets with clear, appropriate
leading to intellectual property     licensing.
disputes.                            Mitigation: Involve legal teams to review and approve policies governing the
                                     use of AI-generated code.
Risk: AI-generated code may be       Mitigation: Apply performance profiling tools to assess and optimize
suboptimal, leading to               generated code.
performance issues such as           Mitigation: Compare AI-generated outputs against best-practice
increased memory usage or            implementations to ensure efficiency (benchmarking).
slower execution times.              Mitigation: Allow developers to iteratively refine AI outputs for better
                                     performance.
Risk: Generated code might not       Mitigation: Incorporate compliance checks as part of the code review
comply with industry regulations,    process.
security standards, or               Mitigation: Train developers to understand applicable compliance
organizational policies (e.g., SIMM requirements for their industry.
5300 series).                        Mitigation: Use AI tools that are specifically designed to comply with relevant
                                     regulations.
Risk: When errors arise in AI-       Mitigation: Require AI-generated code to be committed to version control
generated code, it may be difficult with clear labeling.
to assign accountability or trace    Mitigation: Enable logging of AI tool activities to maintain traceability of code
the origin of the problem.           generation.
  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                     August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                            Page 22 of 28

                                        Mitigation: Ensure developers take ownership of AI-generated code by
                                        requiring signoffs.
Risk: False positives (granting         Mitigation: Use biometrics in combination with other authentication factors
access to unauthorized users) or        (e.g., PIN, token).
false negatives (denying access to      Mitigation: Regularly validate the accuracy of biometric algorithms with
legitimate users) due to errors in      diverse datasets.
biometric recognition models.           Mitigation: Implement secondary authentication methods for denied users to
                                        verify their identity, aka fallback mechanisms.
Risk: Sensitive biometric data          Mitigation: Encrypt biometric data at rest and in transit using strong
(e.g., fingerprints, facial data)       cryptographic methods.
could be exposed, stolen, or            Mitigation: Store only necessary biometric templates instead of raw biometric
misused, leading to identity theft      data.
or privacy breaches.                    Mitigation: Process data locally rather than transmitting it to external servers,
                                        where feasible.
                                        Mitigation: Implement strict access controls to ensure only authorized
                                        personnel can access biometric data.
Risk: LLM documents become              Mitigation: Create an LLM update and release strategy to minimize the gap
stale resulting in inaccurate           between changes to documents and the re-training of the LLM model.
information being provided to staff     Mitigation: Communication to staff when policies change prior to updates to
or the public.                          the LLM.
Risk: Reliance on open LLMs             Mitigation: Continuously benchmark the model's performance against
data sources can weaken model           established benchmarks to identify unexpected drops in accuracy or changes
accuracy due to malicious actors        in behavior.
manipulating the training data.         Mitigation: Enforce privilege control on LLM access to backend systems.
                                        Mitigation: Segregate external content from user prompts and limit the
                                        influence when untrusted content is used.
                                        Mitigation: Maintain fine user control on decision making capabilities by LLM.
                                        Mitigation: Use content safety filters for prompt inputs and its responses.
                                        Mitigation: Use TLS to encrypt all HTTP-based network traffic. Use other
                                        mechanisms, such as IPSec, to encrypt non-HTTP network traffic that
                                        contains customer or confidential data.
Risk: Insufficient scrutiny of LLM      Mitigation: Treat the model as any other user. Adopt a zero-trust approach.
output, unfiltered acceptance of        Apply proper input validation on responses coming from the model to backend
the LLM output could lead to            functions.
unintended code execution.              Mitigation: Encode model output back to users to mitigate undesired code
                                        execution by JavaScript or Markdown.
Risk: Extensions, plugins, API’s        Mitigation: Ensure there is a vulnerability management policy in place.
that are out of date or unknown         Mitigation: Ensure there is a vulnerability patch and update procedures in
can expose the development              place.
environment and reach mission,          Mitigation: Carefully vet data sources and suppliers, including T&Cs and their
state, or critical infrastructure.      privacy policies, only using trusted suppliers.
                                        Mitigation: Only use reputable plug-ins and ensure they have been tested for
                                        your application requirements.
                                        Mitigation: Implement sufficient monitoring to cover component and
                                        environment vulnerabilities scanning, use of unauthorized plugins, and out-of-
                                        date components, including the model and its artifacts.

Chatbots
e.g. used internally by entity for finding resources, getting advice on processes and procedures, locating
documents.
Risk: Employees may be unable            Mitigation: Maintain alternative methods for accessing internal resources.
to access critical internal              Mitigation: Use load balancing to handle high usage volumes and ensure
resources if the chatbot is              consistent availability.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                       August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                              Page 23 of 28

unavailable due to outages or high      Mitigation: Set up alerts for system downtime and have a defined escalation
demand.                                 process to resolve issues quickly.
Risk: Staff input personal              Mitigation: Create or update the acceptable use policy and outline how the
information into the chatbot to try     tool should be used.
and get tailored information.           Mitigation: Add a one-time popup disclaimer that users acknowledge that the
                                        tool should be used for work related activities only.
Risk: Staff input personal and          Mitigation: Update acceptable use to mitigate for misuse.
confidential information into           Mitigation: Communicate to staff that inputs get logged and safeguard their
prompts that get logged.                own information by not entering personal information into GenAI tools.
Risk: Staff input questions related     Mitigation: provide default prompt responses letting staff know that the
to bias or DEIA                         information is not available and to only use the tool as outlined in the
                                        acceptable use policy.
Risk: Staff use GenAI outputs to        Mitigation: Add disclaimers, banners, and contact reminders that AI tools can
make decisions.                         make mistakes and to verify and validate the source of the outputs.
                                        Mitigation: Verify and validate the outputs by an adequately qualified subject
                                        matter expert.
Risk: Administrators see                Mitigation: Ensure administrators who have access to the input/output logs
input/output logs that contain          have the right background clearance and security training to be able to view
confidential information.               that data.
                                        Mitigation: Configure data anonymization.
Risk: Crafty inputs can train the       Mitigations: Create a test plan and include various crafty prompts that try to
back end LLM.                           get the LLM to respond in an unintended manner.

Input Processing
e.g., inputting and processing of hiring information
e.g., inputting and processing of personal or sensitive data in an open environment
e.g., processing sensitive data for national security or intelligence purposes
Risk: GenAI models may                 In addition to the safeguards in Common Risks/Safeguards regarding bias:
unintentionally introduce or           Mitigation: Clearly document and explain how hiring decisions are made to
perpetuate bias in hiring              ensure fairness and compliance with anti-discrimination laws.
processes, leading to
discriminatory practices (e.g.,
favoring or disfavoring candidates
based on gender, ethnicity, or
other protected characteristics).
Risk: GenAI may inadvertently          Mitigation: Incorporate legal reviews into the hiring workflows to verify that
violate laws regarding equal           outputs comply with relevant employment regulations.
opportunity employment by relying Mitigation: Implement constraints within GenAI systems to disallow
on non-compliant criteria for          processing or consideration of protected attributes.
candidate assessment.
Risk: Sensitive data might be          In addition to the safeguards in Common Risks/Safeguards regarding
inadvertently exposed to               exposure of sensitive information:
unauthorized parties in an open        Mitigation: Require secure connections (e.g., VPNs, HTTPS) when handling
environment (e.g., public Wi-Fi,       sensitive data in open environments.
shared workspaces, or non-             Mitigation: Ensure devices used in open environments are equipped with
secured devices).                      firewalls, antivirus software, and updated security patches.
                                       Mitigation: Implement Data Loss Prevention solutions to monitor and prevent
                                       sensitive data from being transmitted outside authorized channels.
                                       Mitigation: Train personnel to identify and mitigate risks of working with
                                       sensitive data in open environments (e.g., avoiding public Wi-Fi, locking
                                       screens when leaving devices unattended).
Risk: The compromise of GenAI          In addition to the safeguards in Common Risks/Safeguards regarding
systems or outputs could expose        exposure of sensitive information:

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                     August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                            Page 24 of 28

highly sensitive national security Mitigation: Use physically isolated environments to process national security
or intelligence data, potentially  data, ensuring GenAI tools are disconnected from external networks.
endangering public safety or       Mitigation: Implement stringent clearance procedures for individuals
operational integrity.             accessing GenAI systems used for national security.
                                   Mitigation: Use data compartmentalization to ensure that only specific,
                                   authorized segments of data are accessible to any given process or user.
Risk: Adversaries or insiders      Mitigation: Require multiple layers of review and cross-validation by
might intentionally manipulate     authorized intelligence personnel.
GenAI outputs to mislead or        Mitigation: Maintain immutable logs of GenAI inputs, processing, and outputs
disrupt decision-making processes for forensic auditing.
related to national security.      Mitigation: Frequently audit and test models to ensure they are not
                                   compromised or manipulated.
Risk: GenAI systems may            Mitigation: Deploy advanced cybersecurity measures such as intrusion
become specific targets of nation- prevention systems, endpoint detection and response (EDR), and zero-trust
state adversaries or advanced      architecture (ZTA).
threat actors aiming to disrupt or Mitigation: Use updated threat intelligence feeds to anticipate and mitigate
infiltrate intelligence workflows. evolving APT tactics.
                                   Mitigation: Establish robust recovery mechanisms to ensure continuity of
                                   operations in the event of a successful attack.

Confidential Data Handling
e.g., processing or analyzing medical records or health data
Risk: GenAI systems may              In addition to the safeguards in Common Risks/Safeguards regarding lack of
inadvertently process or generate compliance with laws and regulations:
outputs that violate health-specific Mitigation: Ensure that GenAI systems are explicitly designed to comply with
legal or regulatory requirements     health data regulations like HIPAA.
for data protection.                 Mitigation: Create and enforce tailored policies for the use of GenAI in
                                     healthcare contexts.
Risk: GenAI may produce outputs In addition to the safeguards in Common Risks/Safeguards regarding
that misinterpret medical data       inaccuracies:
(e.g., symptoms, diagnoses,          Mitigation: Limit GenAI usage to non-critical medical contexts unless
treatment plans), leading to         extensively validated.
incorrect or unsafe conclusions.
Risk: GenAI's use of health data     In addition to the safeguards in Common Risks/Safeguards regarding biases:
could lead to unintended ethical     Mitigation: Obtain explicit patient consent before using their health data in
dilemmas, such as perpetuating       GenAI systems.
biases in diagnoses or treatments. Mitigation: Involve ethics boards to oversee and evaluate the application of
                                     GenAI in healthcare.

Resident (Public) Facing
e.g., chatbots that residents (public) interact with to find web resources and information
e.g., direct contact with the public, customer service, public relations, jurisprudence
e.g., output provides recommendations, legal, tax, regulatory compliance advice, benefit qualifications
Risk: Crafty inputs can train the       Mitigations: Create a test plan and include various crafty prompts that try to
back end LLM.                           get the LLM to respond in an unintended manner.
Risk: liability for the actions or      Mitigation: Include legal in the review process.
statements of the GenAI tools           Mitigation: Provide a banner somewhere on the tool that indicates something
used by residents.                      along the lines of “GenAI can make mistakes, double-check important
                                        information.”
Risk: liability for non-compliance      Mitigation: Review all relevant Generative AI laws and regulations and
with laws and regulations.              incorporate requirements into the build of the tools (e.g., statements,
                                        disclaimers, banners, that are in Gov Codes).

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                                     August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                            Page 25 of 28

Mobile Device
e.g., mobile GenAI solutions and GenAI app Downloads
Risk: GenAI apps may be            Mitigations: Establish an acceptable use policy outlining permitted and
downloaded and misused by staff. prohibited downloads on company devices.
                                   Mitigations Configure devices to disable app store downloads prior to issuing
                                   phones.
                                   Mitigations: Restrict all app downloads to the company portal.
                                   Mitigations: Enforce the use of company certificates as a prerequisite for
                                   downloading apps on devices.
Risk: GenAI may be built into      Mitigations: Disable GenAI mobile capabilities, including GenAI intelligence
mobile devices resulting in        features.
inadvertent disclosures of
sensitive & confidential info
Risk: Work and Personal data       Mitigations: Configure devices to prevent logging out of company accounts,
may be mixed causing data          ensuring mobile devices remain subject to mobile device management (MDM)
ownership issues.                  configurations.

  Office of Information Security
  Generative Artificial Intelligence Risk Assessment                                               August 2025
  SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                      Page 26 of 28

VI. Definitions

Relevant definitions for this guidance are available in SAM 4819.2 and 5300.4

Generative Artificial Intelligence means an artificial intelligence system that can generate derived
synthetic content, including text, images, video, and audio that emulates the structure and characteristics of
the system’s training data.

Human Verification is the process in which one or more people review and validate the output generated
by an automated system, such as a GenAI tool, to ensure its accuracy, correctness, and alignment with
factual information before it is used or implemented. This step acts as a safeguard against errors or
misleading content produced by the automated system.

Personal Identifiable Information is information that can be used to distinguish or trace an individual’s
identity, either alone or when combined with other information that is linked or linkable to a specific
individual.

Proprietary Information is material and information relating to or associated with a company's products,
business, or activities, including but not limited to financial information; data or statements; trade secrets;
product research and development; existing and future product designs and performance specifications;
marketing plans or techniques; schematics; client lists; computer programs; processes; and know-how that
has been clearly identified and properly marked by the company as proprietary information, trade secrets, or
company confidential information. The information must have been developed by the company and not be
available to the Government or to the public without restriction from another source.

Redlining is the process of marking up a contract with suggested changes and revisions. It's usually done
during contract negotiations.

Resident Facing Service refers to any service or application that interacts directly with residents or the
public. This typically involves systems or tools that provide information, make decisions, or deliver services
to residents.

VII. References

Please refer to the latest version of the following resources when implementing this standard:

 1. Generative Artificial Intelligence
    https://www.genai.ca.gov/

 2. Algorithm Risk Management
    Ethics & Algorithms Toolkit (beta) (ethicstoolkit.ai)

 3. Artificial Intelligence Risk Management Framework (AIRMF1.0)
    https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf

 4. AI Risk Management Framework:
    https://www.nist.gov/itl/ai-risk-management-framework/

 5. Definition of High-Risk Automated Decision System:
    https://legiscan.com/CA/text/AB302/id/2814759
   Office of Information Security
   Generative Artificial Intelligence Risk Assessment                                             August 2025
   SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                    Page 27 of 28

  6. Executive Department State of California Executive Order N-12-23
     https://www.gov.ca.gov/wp-content/uploads/2023/09/AI-EO-No.12-_-GGN-Signed.pdf

  7. Federal Information Processing Standards, Standards for Security Categorization of Federal Information
     and Information Systems (FIPS 199)
     https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.199.pdf

  8. California Government Operations Agency website
     GovOps | Government Operations (ca.gov)

  9. NIST Special Publication 800-53 Security & Privacy Controls for Information Systems & Organizations
     https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final

  10. Statewide Administrative Manual (SAM) policies:
      https://www.dgs.ca.gov/en/Resources/SAM/TOC/

  11. Statewide Information Management Manual (SIMM) policies:
      https://cdt.ca.gov/policy/simm/#SIMM

  12. San José Generative AI Guidelines
      https://www.sanjoseca.gov/home/showpublisheddocument/100095/638255600904300000/

  13. San José Digital Privacy and GenAI Manual
      https://www.sanjoseca.gov/home/showpublisheddocument/82093/637889898788170000/

  14. State of California Benefits and Risks of Generative Artificial Intelligence Report
      State of California Benefits and Risks of Generative Artificial Intelligence Report

VIII. Questions

 Please reference SIMM 71B for questions regarding procurement. For all other inquiries and implementation
 of this standard, please contact the California Department of Technology, Office of Information Security at
 Security@state.ca.gov.

    Office of Information Security
    Generative Artificial Intelligence Risk Assessment                                         August 2025
    SIMM 5305-F (Confidential and Exempt - Government Code Section 7929.210(a))                Page 28 of 28

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the month, or the revision month, the document prints (a month with no day is not made into a date).
