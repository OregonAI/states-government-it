---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-scio-sec-314
title: Risk Assessment Policy (RA)
doc_type: policy
citation: SCIO-SEC-314
authority_level: ''
issuing_body: North Carolina Department of Information Technology
source_url: https://it.nc.gov/documents/statewide-policies/scio-risk-assessment/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 525ca80ead1db119b8c8d8c02d173a4c98d770a7f94ba683f7eba435e0291eec
effective_date: '2018-01-29'
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Risk Assessment Policy (RA) (SCIO-SEC-314)

## At a glance

One of the 18 Statewide Information Security Policies (SCIO-SEC-314), each aligned to a NIST SP 800-53 Rev. 5 control family and binding executive branch agencies under G.S. 143B-1376.

## Full text

                                                                                          Document No.
                                        Risk                                              SCIO-SEC-314

                                  Assessment Policy
Effective Date                    Review Date                             Version         Page No.
01/29/2018                        03/26/2025                              4               1 of 21

Scope
  The Statewide Information Security Policies are the foundation for information technology security in
  North Carolina. They set out the statewide information security standards required by N.C.G.S. §143B-
  1376, which directs the State Chief Information Officer (State CIO) to establish a statewide set of
  standards for information technology security to maximize the functionality, security, and
  interoperability of the State’s distributed information technology assets, including, but not limited to,
  data classification and management, communications, and encryption technologies. This policy covers
  all State information and information systems to include those used, managed, or operated by a
  contractor, an agency, or other organization on behalf of the State. This policy applies to all State
  employees, contractors, and all other users of State information and information systems that support
  the operation and assets of the State. Use by local governments, local education agencies (LEAs),
  community colleges, constituent institutions of the University of North Carolina (UNC) and other
  executive branch agencies is encouraged to the extent allowed by law. This security policy is consistent
  with applicable laws, executive orders, directives, regulations, other policies, standards, and
  guidelines.

  This policy document provides the State of North Carolina’s (State) risk assessment policy statements
  and commitment to develop, implement, maintain a Risk Assessment Policy, conduct annual risk and
  security assessments on all State information systems to help understand and identify all current
  threats, vulnerabilities and gaps within their process that may create critical risks availability,
  confidentiality and integrity for information systems and data of which the State is considered the
  owner.

Material Superseded
  This current policy supersedes all previous versions of the policy. All State agencies and vendors of the
  State are expected to comply with the current implemented version of this policy.

Responsibilities
  All covered personnel that are included in IT risk assessment activities are responsible for adhering to
  this policy and with any local Risk Assessment requirements.
   Role               Definition
   Senior             Senior Management (the Agency Head, the Chief Information Officer (CIO), the Chief
   Management         Information Security Officer (CISO), or other designating organizational official) is
                      responsible for the sponsorship, dissemination and support of the Risk Management Plan
                      and process, participating on the Risk Management Council, the review and approval of
                      risk assessments and control recommendations and reporting to the SCRO what
                      mitigation actions have been taken.

                                                                                              Document No.
                                        Risk                                                  SCIO-SEC- 314

                                  Assessment Policy
Effective Date                    Review Date                                 Version         Page No.
01/29/2018                        03/26/2025                                  4               2 of 21

   State Chief        The State Information Security Officer (SCISO) as delegated by the State CIO is assigned
   Information        the responsibility for the continued development, implementation, and maintenance of
   Security Officer   the risk management program.
   Risk               The Enterprise Security and Risk Management Office (ESRMO) is responsible for
   Management         governing the overall Security and Risk Management process, reviews presented Risk
                      Assessment Reports and approves risk treatment plans or recommended controls.
   Security Liaison   Security Liaisons are responsible for conducting the risk assessments, analyzing the risk
                      and recommends controls, presenting risks for approval, documenting the process, and
                      managing and facilitating the implementation of recommended controls.
   System Owner /     System Owners/Administrators are responsible for participating in the identification and
   Administrator      analysis process, participating on the Risk Management Council and for the
                      implementation of technical controls.
   Functional         Managers in the functional areas are responsible for participating in the risk identification
   Managers           and analysis process, providing some participation on the Risk Management Council, and
                      for the implementation of administrative controls.

RA-1 – Policy and Procedures
  All information assets that process, store, receive, transmit or otherwise could impact the
  confidentiality, integrity, and accessibility of State data must meet the required security controls
  defined in this policy document that are based on the NIST SP 800-53, Security and Privacy Controls.
  Agencies shall manage risks appropriately. This document addresses the requirements set forth by the
  State to implement the family of Risk Assessment security controls at the organization, process and/or
  system level for all information assets / State data. Risk management includes the identification,
  analysis, and management of risks associated with an agency’s business, information technology
  infrastructure, the information itself, and physical security to protect the state’s information
  technology assets and vital business functions:
  a. The State of North Carolina recognizes that each agency, through its management, must
     implement an appropriate Information Technology (IT) Risk Management Program to ensure the
     timely delivery of critical automated business services to the state’s citizens.
  b. The risk management program must identify and classify risks and implement risk mitigation as
     appropriate.
  c. The program must include the identification, classification, prioritization, and mitigation processes
     necessary to sustain the operational continuity of mission critical information technology systems
     and resources.
  d. In general, “risk” is defined as a condition or action that may adversely affect the outcome of a
     planned activity. Some types of risk are as follows:

                                                                                        Document No.
                                         Risk                                           SCIO-SEC- 314

                                   Assessment Policy
Effective Date                     Review Date                           Version        Page No.
01/29/2018                         03/26/2025                            4              3 of 21

      i.   Business risk – The cost of and/or lost revenue associated with an interruption to normal
           business operations
      ii. Organizational risk – The direct or indirect loss resulting from one or more of the following:
                 1. Inadequate or failed internal processes
                 2. People
                 3. Systems or external events
      iii. IT risk – The loss of an automated system, network or other critical information technology
           resource that would adversely affect business processes.
      iv. Legal risk – Parameters established by legislative mandates, federal and state regulations,
          policy directives and executive orders that impact delivery of program services.
      v. Reputational risk – General estimation, by the public, on how state services are delivered
         (integrity, credibility, trust, customer satisfaction, image, media relations, political
         involvement).
      vi. Citizen Services risk – Program services mandated by charter, legislation, or policy that
          provides for the delivery of state’s business (education, human services, highways, law
          enforcement, health and safety, unemployment benefits, vital records, etc.).

  To meet the intent of N.C.G.S 143B-1376, ESRMO has developed a Continuous Monitoring Plan which
  requires that all agencies complete an annual risk and security assessment of their critical systems
  and infrastructure and that there are ongoing processes in place to assess the current posture of the
  environment. The Continuous Monitoring Plan is designed as a three-year program to ensure that all
  agencies are assessed using one or a combination of assessment methods identified below:
      a. Third Party Independent Assessment
      b. Self-Assessment

  All agencies must complete a risk and security assessment annually. It is the agency’s responsibility to
  ensure that an appropriate budget amount is requested to meet the ends of the legislative mandate.
  The Department of Information Technology (DIT), ESRMO may conduct compliance readiness reviews
  with the Executive Branch agencies to validate cyber readiness.

  Within 30 days of completion of an assessment, all agencies are required to provide the ESRMO with
  the results and submit a plan to remediate the findings in the Enterprise Governance, Risk and
  Compliance (EGRC) tool. This tool will be used to create and maintain corrective actions plans for
  those deficiencies noted during a risk assessment, including vulnerability scans, and will ensure:
      a. Accurate reporting on the status of corrective actions

                                                                                            Document No.
                                         Risk                                               SCIO-SEC- 314

                                   Assessment Policy
Effective Date                     Review Date                              Version         Page No.
01/29/2018                         03/26/2025                               4               4 of 21

      b. Development of a process to evaluate supporting documentation and the time to monitor
         recommendations
  Agencies shall coordinate with the ESRMO to address residual risks for those controls that cannot be
  implemented.

  The State has adopted the Risk Assessment security principles established in NIST SP 800-53, “Risk
  Assessment” control guidelines as the official policy for this security domain. The “RA” designator
  identified in each control represents the NIST-specified identifier for the Risk Assessment control
  family. The following subsections in this document outline the Risk Assessment requirements that the
  State and each Agency must implement and maintain to be compliant with this policy.
  This policy and associated procedures shall be reviewed and updated annually, at a minimum. They
  shall also be updated following agency-defined events that necessitate such change.
  This policy and the associated procedures shall be developed, documented, and disseminated by the
  Agency Head, the Chief Information Officer (CIO), the Chief Information Security Officer (CISO), or
  other designated organizational officials at the senior leadership level.

  Risk Management Program Activities:
  The Risk Management program at a minimum shall focus on the following four types of activities:

  a. Identification of Risks: A continuous effort to identify which risks are likely to affect business
     continuity and security functions and documenting their characteristics.
  b. Analysis of Risks: An estimation of the probability, impact, and timeframe of the risks,
     classification into sets of related risks, and prioritization of risks relative to each other.
  c. Mitigation Planning: Decisions and actions that will reduce the impact of risks, limit the probability
     of their occurrence, or improve the response to a risk occurrence. For moderate or high rated risks,
     mitigation plans should be developed, documented, and assigned to managers. Plans should
     include assigned manager’s signatures.
  d. Tracking and Controlling Risks: Collection and reporting of status information about risks and their
     mitigation plans, response to changes in risks over time, and management oversight of corrective
     measures taken in accordance with the mitigation plan.

  Business Continuity Risk Management Processes:
  For business continuity risk management, the focus of risk management is an impact analysis for those
  risk outcomes that disrupt agency business. Agencies should identify the potential impacts in order to
  develop the strategies and justify the resources required to provide appropriate level of continuity

                                                                                         Document No.
                                         Risk                                            SCIO-SEC- 314

                                   Assessment Policy
Effective Date                     Review Date                             Version       Page No.
01/29/2018                         03/26/2025                              4             5 of 21

  initiatives and programs. Agencies should conduct business risk impact analysis activities that include
  the following:

  a. Define the agency’s critical functions and services
  b. Define the resources (technology, staff, and facilities) that support each critical function or service
  c. Identify key relationships and interdependencies among the agency’s critical resources, functions,
     and services
  d. Estimate the maximum elapsed time that a critical function or service can be inoperable without a
     catastrophic impact
  e. Estimate the maximum amount of information or data that can be lost without a catastrophic
     impact to a critical function or service
  f.   Estimate financial losses over time of each critical function or service
  g. Estimate tangible (non-financial) impacts over time of each critical function or service
  h. Estimate intangible impacts over time of each critical function or service
  i.   Document any critical events or services that are time-sensitive or predictable and require a
       higher- than-normal priority (For example - tax filing dates, reporting deadlines, etc.)
  j.   Identify any critical non-electronic media required to support the agency’s critical functions or
       services
  k. Identify any interim or workaround procedures that exist for the agency’s critical functions or
     services.
  l.   Assess the professional capability of third parties and ensure that they provide adequate contact
       with the agencies and meet the agency’s RTO and RPO requirements. Review dependence on third
       parties and take actions to mitigate risk.
  m. Provide direction on synchronization between any manual work data and the automated systems
     that occur during a recovery period.

  Security Risk Process:
  The focus of security risk management is an assessment of those security risk outcomes that may
  jeopardize agency assets and vital business functions or services. Agencies should identify those
  impacts to develop the strategies and justify the resources required to provide the appropriate level
  of prevention and response. It is important to use the results of risk assessment to protect critical
  agency functions and services in the event of a security incident. The lack of appropriate security
  measures would jeopardize agency critical functions and services. Security risk impact analysis
  activities include the following:

                                                                                        Document No.
                                        Risk                                            SCIO-SEC- 314

                                  Assessment Policy
Effective Date                    Review Date                            Version        Page No.
01/29/2018                        03/26/2025                             4              6 of 21

  a. Identification of the Federal, State, and Local regulatory or legal requirements that address the
     security, confidentiality, and privacy requirements for agency functions or services.
  b. Identification of confidential information stored in the agency’s files and the potential for fraud,
     misuse, or other illegal activity.
  c. Identification of essential access control mechanisms used for requests, authorization, and access
     approval in support of critical agency functions and services.
  d. Identification of the processes used to monitor and report to management on whatever
     applications, tools, and technologies the agency has implemented to adequately manage the risk
     as defined by the agency (e.g., baseline security reviews, review of logs, use of IDs, logging events
     for forensics, etc.).
  e. Identification of agency’s IT Change Management and Vulnerability Assessment processes.
  f.   Identification of security mechanisms in place to preserve and protect the confidentiality,
       integrity and availability of State data and systems (e.g., encryption, PKI, etc.).

RA-2 – Security Categorization
  Organizations must address the following requirements:

  a. Systems and the information processed, stored, transmitted, and received by them shall be
     categorized in accordance with applicable State and Federal laws, policies, regulations, standards,
     and guidance. NIST SP 800-60 Volumes 1 and 2 serves as a guidance for the categorization process.
     The security categories are based on the potential impact on an organization should certain events
     occur that jeopardize the confidentiality, integrity, and availability of the information and
     information systems needed by the organization to accomplish its assigned mission, protect its
     assets, fulfill its legal responsibilities, maintain its day-to-day functions, and protect individuals.
     The impact to the Agency, State, personnel, and other external entities must be considered during
     the security categorization process.
  b. System Owners need to be involved with the security categorization of an information system if
     they are responsible for the following:
       i. Any interconnected system dependencies, e.g., systems that share information
       ii. A system that may inherit a security control from their respective system
  c. Include the security categorization process as a part of the system development lifecycle (SDLC).
     The security categorizations shall be developed early in the initiation stage ensuring the planning
     and implementation of the appropriate security controls throughout the SDLC

                                                                                        Document No.
                                       Risk                                             SCIO-SEC- 314

                                 Assessment Policy
Effective Date                    Review Date                            Version        Page No.
01/29/2018                        03/26/2025                             4              7 of 21

  d. Verify the security categorization decision is reviewed and approved by the authorized or
     designated representative
  e. Update documents to address changes to the information system/environment of operation or
     problems identified during plan implementation or security control assessments
  f.   The Business Owner, System Owner and supporting security liaison must assist with the
       development of the security categorization
  Information includes all data, regardless of physical form or characteristics, made or received in
  connection with the transaction of public business by any agency of State government. The State’s
  information shall be classified and handled in a manner that protects the information from
  unauthorized or accidental disclosure, modification, or loss. State Agencies must use the North
  Carolina Department of Information Technology Data Classification and Handling Policy for detailed
  requirements for the storage, labeling, classification and destruction of State data.

  In addition, a Privacy Threshold Analysis (PTA) form shall be completed for each system, State or cloud
  hosted, that will contain State data. A PTA is the official State document that records the privacy
  sensitivity of a system that will host State data.

RA-3 – Risk Assessment
  Risk assessments consider risks posed to State agency operations and assets, or individuals from
  external parties, including but not limited to entities such as Service providers; Contractors operating
  information systems on behalf of the Agency; Individuals accessing State data and information
  systems; and Outsourcing organizations.

  Organizations shall identify threats to and vulnerabilities in the system as part of the Risk assessment
  process.

  Organizations must conduct security/risk assessments to evaluate the level of risk, including the
  likelihood and magnitude of harm, from the unauthorized access, use, disclosure, disruption,
  modification or destruction of the information system and the information it processes, stores, or
  transmits and any related information.

  Organizations must also conduct privacy/risk assessments to evaluate the level of risk, including the
  likelihood and impact of adverse effects on individuals arising from the processing of personally
  identifiable information.

  Organizations shall integrate risk assessment results and risk management decisions from the
  organization and mission or business process perspectives with system-level risk assessments.

                                                                                          Document No.
                                          Risk                                            SCIO-SEC- 314

                                    Assessment Policy
Effective Date                       Review Date                          Version         Page No.
01/29/2018                           03/26/2025                           4               8 of 21

  Organizations shall conduct security/risk assessments at minimum annually, or whenever there are
  significant changes to the critical information system or environment of operation or other conditions
  that may impact the security or privacy state of the system.

  For State Agencies, an agency-wide third-party assessment of all critical systems (Restricted or Highly
  Restricted) and associated security controls will be conducted at a minimum every 3 years. Agencies
  that completed an agency-wide third-party assessment in year 1, may opt to complete a self-
  assessment or a more targeted and system specific assessment during years 2-3.

  a. All assessment results will be provided to the ESRMO within thirty (30) days of completion. Risk
     assessment results shall be documented in Security and Privacy plans. The assessment shall
     include, at a minimum, the following:
      i.   The rate of compliance with the enterprise-wide security standards.
      ii. An assessment of security organization, security practices, security information standards,
          network security architecture, and current expenditures of State funds for information
          technology security.
      iii. Estimate the cost to implement the security measures needed for agencies to fully comply with
           the standards.
  b. The risk assessment must consider risks posed to State’s operations, assets, or individuals from
     external parties, including but not limited to the following:
      i.   Organizations such as foreign nations and business competitors that may have an interest in
           information supplied to the agencies.
      ii. Service Providers:
           1. Contractors operating information systems on behalf of the State
           2. Individuals accessing the State’s information systems
           3. Outsourcing entities/organizations (e.g., cloud service providers (CSPs))
                 i.   Agencies need to obtain prior approval from the State CIO before contracting with
                      cloud-hosted solutions or off-site hosting.
                 ii. Agencies must ensure vendor compliance with Statewide security policies and obtain
                     a Vendor Readiness Assessment Report (VRAR) from the vendor prior to contract
                     approval.
                 iii. Agencies shall ensure that contract language requires vendors to provide as
                      attestation to their compliance, an industry recognized, third party assessment
                      report. Examples of acceptable attestation reports include Federal Risk and
                      Authorization Management Program (FedRAMP) certification, Service Organization

                                                                                          Document No.
                                          Risk                                            SCIO-SEC- 314

                                    Assessment Policy
Effective Date                      Review Date                            Version        Page No.
01/29/2018                          03/26/2025                             4              9 of 21

                     Controls (SOC) 2 Type 2, ISO/IEC 27001 Information Security Management Standard,
                     and HITRUST CSF (Common Security Framework).
                 iv. Procurement language must also require, in addition to initial validation,
                     cloud/vendor must annually provide the agency validation of their continued
                     compliance. This requirement includes all vendors supporting Infrastructure as a
                     Service (IaaS), Platform as a Service (PaaS), and/or Software as a Service (SaaS).
                     Examples of acceptable assessment reports include Federal Risk and Authorization
                     Management Program (FedRAMP) certification, Service Organization Controls (SOC) 2
                     Type 2, ISO/IEC 27001 Information Security Management Standard, and HITRUST CSF
                     (Common Security Framework). CSPs must demonstrate to the State that continuous
                     monitoring activities are in place and compliance is being met. Note: SaaS vendors
                     cannot use IaaS/PaaS certifications unless the application is explicitly covered as part
                     of those assessments.

  c. When planning and budgeting for security/risk assessments, the Agency must follow these
     requirements:
      i.   Multi-year planning and budgeting techniques must be used.
      ii. Annual assessments must be included in information system budgets and planning.
      iii. Other significant, planned activities must be considered in budgets and planning (e.g., life
           cycle activities, enhancements, audits) to ensure cost effective use of resources.
      iv. All information systems in an agency must be considered to ensure resource efficiencies.
      v. Assessments must be coordinated between information systems with security control
         inheritance and other relational dependencies.
      vi. Agencies shall conduct an assessment using NIST 800-53 controls that includes at a
          minimum their critical systems.
      vii. An agency may perform an annual self-assessment of their organization or systems for
           two of the years out of a three year period. An independent third-party assessment shall be
           completed at least once every three (3) years.
      viii. An independent assessor or assessment team shall assess the security controls in the
            information system using an ESRMO provided assessment template.
  d. A Plan of Action and Milestones (POA&M) or Corrective Action Plan (CAP) for the system
     documenting the planned, remedial actions to correct weaknesses or deficiencies in security and
     privacy controls and to reduce or eliminate known vulnerabilities must be developed.

                                                                                      Document No.
                                         Risk                                         SCIO-SEC- 314

                                   Assessment Policy
Effective Date                      Review Date                            Version    Page No.
01/29/2018                          03/26/2025                             4          10 of 21

  e. The existing POA&M or CAP must be updated weekly for any critical/high risk findings
     of weaknesses and monthly for any medium/low risk findings of weaknesses including,
     but not limited to, the following:
       i.   Reviews, tests, audits, or assessments
       ii. Security and Privacy impact analyses
       iii. Independent verification and validation findings
       iv. Continuous monitoring activities
       v. Incidents
  f.   All findings, recommendations, and their source must be tracked to the related item in the POA&M
       or CAP.
  g. Findings must be analyzed as to their level of risk (e.g., high, medium, low) and a determination
     must be made for appropriate action(s) to be taken to correct or mitigate, as appropriate, the
     identified weaknesses to an acceptable level of risk.
  h. One or more tasks to remediate a finding must be documented in the POA&M or CAP for any of the
     following:
       i.   Critical-level risks that are not remediated within 7 days
       ii. High-level risks that are not corrected within 21 days
       iii. Medium-level risks that are not corrected within 30 days
       iv. Low level risks as required by the Agency CIO and that are not corrected within 90 days
  i.   All findings must be entered into a corrective action plan (CAP).

  Risk Assessment/Analysis
  Risk assessment or analysis is the act of determining the probability that a risk will occur and the
  impact that event would have if it does occur. This analyzes the cause and effect of each possible
  event. Once risks have been identified and documented, risk analysis must be performed. During the
  risk analysis process, each potential risk event will be evaluated for the following:
        a. The probability that the risk will occur
        b. The impact of the risk if it occurs
  These two factors of assessing the risk involving probability and impact shall be measured for
  probability using a scale of Low, Medium, and High, and giving each an associated number.

                                                                                        Document No.
                                        Risk                                            SCIO-SEC- 314

                                  Assessment Policy
Effective Date                    Review Date                               Version     Page No.
01/29/2018                        03/26/2025                                4           11 of 21

  For impact, the State shall use a qualitative method for analysis as it is typically a quicker and usually
  more cost-effective way to analysis risks. Analysis will be performed with the goal of gathering data on
  the following:
       a. The likelihood of the risk occurring
       b. The qualitative impact on the company, system, or data
       c. The quality of the risk data being utilized

  Business Risk Analysis of each business system shall be utilized to assist in impact determination.

  Impact Definitions
Magnitude                                       Impact Definition
of Impact
   High   If an event could be expected to have a severe or catastrophic adverse effect on agency
          operations, agency assets, or individuals; and cause a loss of mission capability for a period
          that poses a threat to human life, or results in a loss of major assets.
 Medium   If an event could be expected to have a serious adverse effect on agency operations,
          agency assets or individuals, and cause significant degradation in mission capability, place
          the agency at a significant disadvantage, or result in major damage to assets, requiring
          extensive corrective actions or repairs.
   Low    If an event could be expected to have a limited adverse effect on agency operations
          (including mission, functions, image or reputation, agency assets, or individuals; and cause
          a negative outcome or result in limited damage to operations or assets, requiring minor
          corrective actions or repairs.
  As Risks are identified and quantified, they are entered into the into the DIT Enterprise Governance
  Risk Compliance (EGRC) reporting and tracking tool. All risks are reported based on type of risk,
  probability, impact, and overall risk. To determine and quantify the overall risk, the below table
  (based on NIST 800-30) is used.

Threat Likelihood                 Low (10)                  Medium (50)                  High (100)

        High                        Low                       Medium                        High
        (1.0)                   10 x 1.0 = 10               50 x 1.0 = 50              100 x 1.0 = 100
       Medium                       Low                       Medium                      Medium
        (0.5)                   10 x 0.5 = 5                50 x 0.5 = 25              100 x 0.5 = 50
        Low                         Low                         Low                         Low
        (0.1)                   10 x 0.1 = 1                50 x 0.1 = 5                10 x 0.1 = 10

                                                                                       Document No.
                                         Risk                                          SCIO-SEC- 314

                                   Assessment Policy
Effective Date                     Review Date                           Version       Page No.
01/29/2018                         03/26/2025                            4             12 of 21

  Risk Response
  For each identified risk, a response must be identified. The Agency Security Liaison will select a risk
  response for each risk. The probability and impact of the risk will be the basis of recommending which
  actions should be taken to mitigate the risk. During response planning, strategies and plans are
  developed to minimize the effects of the risk to a point where the risk can be controlled and managed.
  Avoid: Risk avoidance involves changing aspects of the overall business process or system architecture
  to eliminate the threat.
  Transfer: Risk transference involves shifting the negative impact of a threat (and ownership of the
  response) to a third party. Risk transference does not eliminate a threat it simply makes another party
  responsible for managing it. This would include identifying avenues of insurance, etc.
  Mitigate: Risk mitigation involves reducing the probability and/or the impact of risk threat to an
  acceptable level. Taking early and pro-active action against a risk is often more effective than
  attempting to repair the damage a realized risk has caused. Developing contingency plans are
  examples of risk mitigation.
  Accept: Risk acceptance should normally only be taken for low-priority risks. All risks should have a
  recommendation of control(s) and / or alternative solutions to mitigate risk.

Risk Level       Risk Description and Necessary Actions
High             Mandatory need for corrective measures. CAP must be in place for 60 days.
Medium           Plan must be developed to mitigate corrective measures within 90 – 120 days.
Low              Decision on whether to implement corrective measures or accept the risk.

  Use of Independent Assessors
  When assessments must be conducted by an entity with an explicitly determined degree of
  independence to the organization, independence must be determined by the Agency CIO based on the
  security categorization of the information system and/or the risk to Agency operations and assets, and
  to individuals.
  To make an informed, risk-based decision, the selection of independent assessors must consider the
  following criteria to ensure credibility of the security assessment results and to receive the most
  objective information possible. Preserving the impartial and unbiased nature of the assessment
  process including, but not limited to, freedom from any perceived or actual conflicts of interest with
  respect to the following:
  a. The development, operation, and/or management of the information system
  b. The chain of command associated with the information system

                                                                                       Document No.
                                       Risk                                            SCIO-SEC- 314

                                 Assessment Policy
Effective Date                   Review Date                            Version        Page No.
01/29/2018                       03/26/2025                             4              13 of 21

  c. The determination of security control effectiveness
  d. A competitive relationship with any organization associated with the information system
     being assessed or impacts on their reputations
  e. Undue influence as a result of a contractual or other related relationship
  f.   The assessor’s technical expertise and knowledge of State and federal requirements

RA-4 – Risk Assessment Update
  Withdrawn: Incorporated into RA-3.

RA-5 – Vulnerability Monitoring and Scanning
  All State Risk Assessment programs must include the following requirements:

  a. All malware (malicious software) scanning software shall be current, actively running on deployed
     workstations and servers, and capable of generating audit logs of virus events.
  b. Monitoring and scanning for vulnerabilities in information systems and hosted applications must
     be performed at least every 7 days and when new critical vulnerabilities potentially affecting the
     system/applications are identified and reported if existing data does not allow for quick
     determination of affected systems. Vulnerability scanning shall include scanning for specific
     functions, ports, protocols, and services that should not be accessible to users or devices and for
     improperly configured or incorrectly operating information flow mechanisms.
  c. Real-time scanning for spyware, adware, and bots (software robots) with one or more anti-
     spyware programs that detect these malicious programs and help protect the system against
     infection.
  d. Scan for malware on files that are downloaded from the Internet or any other outside source,
     including all external media, such as flash drives, CDs, etc. shall be conducted.
  e. Viruses, spyware, Trojan applications, and other malicious code may cause damage to the State’s
     infrastructure via Web browsers and therefore all internet traffic shall be scanned to prevent
     malicious code from infecting the State’s infrastructure.
  f.   External computers or networks making remote connection to internal agency computers or
       networks shall utilize an agency-approved active virus scanning and repair program and an agency-
       approved personal firewall system (hardware or software). The agency shall ensure that updates
       to virus scanning software and firewall systems are available to users. Non-State computers or
       networks making a remote connection to a public Web server are exempted.

                                                                                       Document No.
                                        Risk                                           SCIO-SEC- 314

                                  Assessment Policy
Effective Date                     Review Date                           Version       Page No.
01/29/2018                         03/26/2025                            4             14 of 21

  g. Organizations shall scan their networks and take remediation actions to identify any
     multifunctional devices (MFD)s on the network that are vulnerable and/or configured insecurely.
  h. Conduct scanning independently or as a coordinated effort with ESRMO.
  i.   Prior to commencing vulnerability scanning efforts, the following should be addressed:
       i. Scanner selection – Evaluate the mandated tools for use within the respective environments
       ii. The network and host-based vulnerability scanner shall provide the following capabilities:
            1. Identify active hosts on networks.
            2. Identify active and vulnerable services (ports) on hosts.
            3. Identify vulnerabilities associated with discovered operating systems and applications

  The ESRMO shall implement a suite of automated monitoring tools to effectively monitor and identify
  vulnerabilities on networked computer servers and workstations. Agencies shall utilize the tools
  provided by the ESRMO, if the agency tools are determined to duplicate functionality. Vulnerability
  monitoring tools and techniques are employed that promote interoperability among tools and
  automate parts of the vulnerability management process by using standards for the following:
       i.   Enumerating platforms, software flaws, and improper configurations
       ii. Formatting and making transparent, checklists and test procedures
       iii. Measuring vulnerability impact
       iv. Analyzing vulnerability scan reports and results from vulnerability monitoring
       v. Remediating legitimate vulnerabilities in accordance with the agency’s assessment of risk and
          the established mitigation timeframes. Refer to Vulnerability Mitigation section below. See
          also Vulnerability Risk Ratings and Remediation section in System and Information Integrity
          Policy, SI-2 – Flaw Remediation.
       vi. Employing vulnerability monitoring tools that include the capability to readily update the
           vulnerabilities to be scanned
  Sharing information obtained from the vulnerability scanning process and security control assessments
  with designated personnel throughout the organization to help eliminate similar vulnerabilities in
  other information systems (e.g., systemic weaknesses or deficiencies).

  Vulnerability Management
  System administrators shall ensure that all current maintenance and security vulnerability patches are
  applied and that only essential application services and ports are enabled and opened in the system’s
  firewall, as applicable. Vulnerabilities that threaten the security of the State’s network or IT assets
  shall be addressed through updates and patches based upon assigned vulnerability ratings:

                                                                                         Document No.
                                        Risk                                             SCIO-SEC- 314

                                  Assessment Policy
Effective Date                     Review Date                            Version        Page No.
01/29/2018                         03/26/2025                             4              15 of 21

  a. Personnel shall manage systems to reduce vulnerabilities through vulnerability testing and
     management, promptly installing patches and updates, and eliminating or disabling unnecessary
     services.
  b. Where possible tools that express vulnerabilities in the Common Vulnerabilities and Exposures
     (CVE) naming convention and that use the Open Vulnerability Assessment Language (OVAL) shall
     be used to test for the presence of vulnerabilities.
  c. Perform scans, typically, on systems and networks known to be stable and preferably during times
     of least impact to the critical functionality of the system. Expect vulnerability scanning to occur
     during various phases of the system’s life cycle.

  Vulnerability Mitigation
  a. Vulnerability mitigation procedures must specify, at a minimum, the proposed resolution to
     address identified vulnerabilities, required tasks necessary to affect changes, and the assignment
     of the required tasks to appropriate personnel.
  b. Vulnerability exceptions are permitted in documented cases where a vulnerability has been
     identified but a patch is not currently available. When a vulnerability risk is ‘high-level’ and no
     patch is available, steps must be taken to mitigate the risk through other compensating control
     methods (e.g., group policy objects, firewalls, router access control lists). A patch needs to be
     applied when it becomes available. When a ‘high-level’ risk vulnerability cannot be totally
     mitigated within the requisite time frame, agencies need to notify agency management and the
     State Chief Information Officer of the condition.
  c. Appropriate testing and assessment activities shall be performed after vulnerability mitigation
     plans have been executed to verify and validate that the vulnerabilities have been successfully
     addressed.
  d. Appropriate notification shall be provided after vulnerability mitigation plans have been executed.
  e. In the event of a zero-day vulnerability, a situation where an exploit is used before the developer
     of the software knows about the vulnerability, agencies shall mitigate the vulnerability
     immediately, if possible, and apply patches as soon as possible after the vendor provides them.
  f.   For vulnerability risk ratings and mitigation timelines, please refer to SI-2 – Flaw Remediation.

  Vulnerability Information Review and Analysis
  a. Relevant vulnerability information from appropriate vendors, third party research, and public
     domain resources shall be reviewed on a regular basis.
  b. Relevant vulnerability information, as discovered, shall be distributed to the appropriate personnel,
     including the security office.

                                                                                        Document No.
                                        Risk                                            SCIO-SEC- 314

                                  Assessment Policy
Effective Date                     Review Date                           Version        Page No.
01/29/2018                         03/26/2025                            4              16 of 21

  c. Appropriate personnel shall be alerted or notified in near real-time about warnings or
     announcements involving "High-risk" vulnerabilities.

  Requirements for Compliance
  a. Procedures must be developed to ensure the timely and consistent use of security patches and use
     a consistent vulnerability naming scheme to mitigate the impact of vulnerabilities in systems.
  b. An explicit and documented patching and vulnerability policy is required, as well as a systematic,
     accountable, and documented set of processes and procedures for handling patches.
  c. The patching and vulnerability policy shall specify techniques an organization will use to monitor
     for new patches and vulnerabilities and personnel who will be responsible for such monitoring.
  d. An organization’s patching process shall define a method for deciding which systems are patched
     and which patches are installed first, as well as the method for testing and safely installing patches.
  e. The process for handling patches shall include the following:
       i.   Using organizational inventories
       ii. Using the Common Vulnerabilities and Exposures vulnerability naming scheme for vulnerability
           and patch monitoring (See http://cve.mitre.org)
       iii. Patch prioritization techniques
       iv. Organizational patch databases.
       v. Patch testing, patch distribution, patch application verification, patch training, automated
          patch deployment, and automatic updating of applications
  f.   A list of sources of information about security problems and software updates for the system and
       application software shall be developed.
  g. A procedure for monitoring those information sources shall be established.
  h. Updates for applicability to the systems shall be evaluated.
  i.   The installation of applicable updates shall be planned.
  j.   Updates shall be installed using a documented plan.
  k. New computers shall be deployed with up-to-date software.
  l.   After making any changes in a system’s configuration or its information content, new cryptographic
       checksums or other integrity-checking baseline information for the system shall be created.

  Agencies shall utilize the vulnerability management tools provided by ESRMO, if the agency tools are
  determined to duplicate functionality. The vulnerabilities to be scanned need to be readily updated as

                                                                                          Document No.
                                        Risk                                              SCIO-SEC- 314

                                  Assessment Policy
Effective Date                     Review Date                             Version        Page No.
01/29/2018                         03/26/2025                              4              17 of 21

  new vulnerabilities are discovered, announced, and scanning methods developed. This updating
  process helps to ensure that potential vulnerabilities in the information system are identified and
  addressed as quickly as possible.

RA-5 (2) – Vulnerability Monitoring and Scanning – Frequency of Updates
  The list of system vulnerabilities scanned shall be updated prior to a new scan or when new
  vulnerabilities are identified and reported.

RA-5 (5) – Vulnerability Monitoring and Scanning – Privileged Access
  Privileged access authorization to an information system shall be implemented for vulnerability
  scanning activities. In certain situations, the nature of the vulnerability scanning may be more intrusive
  or the information system component that is the subject of the scanning may contain Highly Restricted
  information. Privileged access authorization to selected system components facilitates more thorough
  vulnerability scanning and protects the sensitive nature of such scanning.

  This control is optional for LOW risk information systems.

Enforcement
  Violations of this policy or failure to implement provisions of this policy may result in disciplinary
  action up to and including termination, civil litigation, and/or criminal prosecution.

                                                                                            Document No.
                                          Risk                                              SCIO-SEC- 314

                                    Assessment Policy
 Effective Date                      Review Date                             Version        Page No.
 01/29/2018                          03/26/2025                              4              18 of 21

APPENDIX A – AGENCY ANNUAL ASSESSMENT AND COMPLIANCE REPORT TEMPLATE

                                        [AGENCY LETTER HEAD]

TO:               xxxx
                  State Chief Information Officer

FROM:             [AGENCY]

SUBJECT:          yyyy Agency Compliance Report

Pursuant to the authorities and powers of the State Chief Information Officer enumerated in Session Law
2015-241, and as Agency head for [AGENCY];

A. I certify that [AGENCY] has implemented the appropriate processes and procedures listed below to be
in compliance with the Statewide Information Security Manual and State statues:

☐       No data of a confidential nature, as defined in the General Statutes or federal law, was entered into
        or processed through any information technology system or network established under this Article
        until safeguards for the data's security satisfactory to the State CIO have been designed and installed
        and are fully operational.

☐       Agency obtained approval from the State CIO prior to contracting for the storage, maintenance, or
        use of State data by a private vendor.

☐       Agency ensured all information technology security goods, software, or services purchased using
        State funds, or for use by a State agency or in a State facility, was subject to approval by the State
        CIO in accordance with security standards

☐       Agency completed annual risk assessments to identify compliance, operational, and strategic risks to
        the enterprise network. These assessments may include methods such as penetration testing or
        similar assessment methodologies.

                  Type of Assessment                   Completion Date              Cost for Assessment

                                                                                        Document No.
                                       Risk                                             SCIO-SEC- 314

                                 Assessment Policy
Effective Date                    Review Date                            Version        Page No.
01/29/2018                        03/26/2025                             4              19 of 21

      [Enter 3rd party/vendor details or
      Self-Assessment]

☐     Agency ensured all contracts for third party assessment and testing, was approved by the State CIO
      (as applicable) and resulting sanitized assessment reports were made public.

☐     Agency provided the full details of the State agency's information technology and operational
      requirements and of all the agency's information technology security incidents within 24 hours of
      confirmation

☐     Agency designated an agency liaison in the information technology area to coordinate with the State
      CIO.

☐     Agency completed an annual assessment of the agency's contracted vendors, to comply with the
      current security enterprise-wide set of standards. The assessment shall include, at a minimum, the
      rate of compliance with the enterprise-wide security standards and an assessment of security
      organization, security practices, security information standards, network security architecture, and
      current expenditures of State funds for information technology security.

          Cloud Service                                                          Review/Assessment
                                  Cloud Offering            Service Type               Date
            Provider

       Ex. Microsoft            Office 365               IaaS / SaaS / PaaS

      [Add Rows Needed]

☐     Agency submitted disaster recovery plans to the State CIO on an annual basis and as otherwise
      requested by the State CIO

                                                                                       Document No.
                                         Risk                                          SCIO-SEC- 314

                                   Assessment Policy
 Effective Date                    Review Date                           Version       Page No.
 01/29/2018                        03/26/2025                            4             20 of 21

                   Business Continuity Plan
                                                                   Business Continuity Test Date
                  (Review/Submission Date)

☐      Agency achieved completion rate > 95 percent for annual Cybersecurity Awareness Training
       during CY 20XX

         Number of Employees (including            Number of Users who               Training Budget
            contractors), involved                 Completed the training               Required

☐      [AGENCY] has not completed all requirements but have identified a plan to be in compliance.
       Attached is our assessment report to include corrective action plan indicating when the agency
       will meet these requirements.

B. In accordance with § 143B-1342, below is the estimated cost to implement security measures needed for
agencies to fully comply with the standards.

SECURITY / BUDGET DEFICIENCIES:

                                                                                   Agency budget
                                                   Estimated Cost to
                   Security Gaps                                                     approved?
                                                       Remediate
                                                                                       (Y/N)
        Ex. Security boundary devices,
        Personnel, Training, Vulnerability
        Management, End of Life Support

For additional information about this submission please contact: [INSERT AGENCY CONTACT]

                                                       Document No.
                                   Risk                SCIO-SEC- 314

                             Assessment Policy
 Effective Date               Review Date   Version    Page No.
 01/29/2018                   03/26/2025    4          21 of 21

_______________________________________           ________________
Printed Name of Secretary/CIO or Designee          [Date]

_______________________________________
Signature of Secretary/CIO or Designee

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
