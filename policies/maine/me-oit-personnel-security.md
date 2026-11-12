---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-personnel-security
title: Personnel Security Policy and Procedures (PS)
doc_type: policy
citation: MaineIT Personnel Security Policy and Procedures (PS)
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/PersonnelSecurityPolicy.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 8b4e651ac6347a72c6db1bab21e1fe37f3065a0fd26bd1ca3986be681feecbf4
effective_date: null
source_version: 'Latest Revision Date: September 19, 2025'
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

# Personnel Security Policy and Procedures (PS) (MaineIT Personnel Security Policy and Procedures (PS))

## At a glance

The State's policy and procedures governing screening of, and access to State information assets by, personnel (the NIST Personnel Security family).

## Full text

                     State of Maine
Department of Administrative and Financial Services
          Office of Information Technology

        Personnel Security Policy and Procedures (PS)

                                      Personnel Security Policy and Procedures (PS)

                                                                     Table of Contents

1.0.        Document Purpose ................................................................................................................................. 2

2.0.        Scope ............................................................................................................................................................ 2

3.0.        Policy Conflict ........................................................................................................................................... 2

4.0.        Roles and Responsibilities................................................................................................................... 2

5.0.        Management Commitment.................................................................................................................. 3

6.0.        Coordination Among Agency Entities ............................................................................................. 3

7.0.        Compliance ................................................................................................................................................ 3

8.0.        Procedures................................................................................................................................................. 3

9.0.        Document Details................................................................................................................................. 12

10.0. Review ...................................................................................................................................................... 12

11.0. Records Management ......................................................................................................................... 12

12.0. Public Records Exceptions ............................................................................................................... 12

13.0. Definitions .............................................................................................................................................. 12

14.0. Abbreviations ........................................................................................................................................ 14

Appendix A: OIT Pre-Hire and Orientation Checklist and Guidelines ........................................... 16

Appendix B: Exit Interview Checklist for OIT ......................................................................................... 19

State of Maine                                                                                                                                              Page 1 of 17

                       Personnel Security Policy and Procedures (PS)

1.0.      Document Purpose
          The purpose of this document is to define the State of Maine policy and procedures
          that are in place to govern screening and access to State of Maine information
          assets (see Definitions). This part of the security program is focused on protecting
          the confidentiality (see Definitions), integrity (see Definitions), and availability
          (see Definitions) of State information assets. This document corresponds to the
          Personnel Security Policy and Procedures (PS) Control Family of National Institute
          of Standards and Technology (NIST) Special Publication 800-53 (Rev. 5).1
2.0.      Scope
2.1.      This policy applies to all State of Maine employees and contractors (collectively
          referred to as personnel in this document) with access to:
          2.1.1.    Executive Branch Agency information assets, irrespective of location; and
          2.1.2.    Information assets from other State government branches that use
                    Executive Branch managed services.
3.0.      Policy Conflict
          If this policy conflicts with any law or union contract in effect, the terms of the
          existing law or contract prevail.
4.0.      Roles and Responsibilities
4.1.      Agencies:
          4.1.1.    In collaboration with OIT and IT Procurement, holds all
                    vendors/partners for externally hosted Information Assets accountable
                    to this Policy, within the vendor/partner’s span-of-control.
          4.1.2.    Ensures agency personnel are aware of all applicable penalties for
                    noncompliance, including the personnel sanctions identified in Section
                    8.7 of this policy.
          4.1.3.    Develops and implements agency-level policy and procedures to meet
                    any additional pertinent personnel security regulatory compliance
                    requirements.
          4.1.4.    Ensures that position risk designations are updated and applied
                    accurately.
          4.1.5.    Develops agency level personnel security policy and procedures as
                    required by state and federal law.
          4.1.6.    Identifying and maintaining privacy responsibilities in position
                    descriptions to meet relevant regulatory compliance requirements and
                    business needs.
4.2.      OIT Information Security:

1 https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final

State of Maine                                                                         Page 2 of 17

                        Personnel Security Policy and Procedures (PS)

          4.2.1.     Owns, executes, and enforces this Policy and Procedure.
          4.2.2.     Ensures that all OIT personnel are aware of all applicable penalties for
                     non-compliance.
4.3.      IT Procurement:
          4.3.1.     Ensures vendor contracts stipulate that third-party personnel are subject
                     to the requirements identified in 8.7, Third-Party Personnel Security.
          4.3.2.     In collaboration with the Agency Business Partner, holds all third-party
                     providers (including vendors, contractors, and other supplier
                     organizations providing information system development, IT services,
                     network and security management, suppliers, and partners for externally
                     hosted Information Assets) accountable to this Policy.
          4.3.3.     Third-party providers are responsible for managing third-party
                     personnel in accordance with this policy.
5.0.    Management Commitment
        The State of Maine is committed to following this policy and the procedures that
        support it.
6.0.    Coordination Among Agency Entities
6.1.    OIT coordinates personnel security with agencies to ensure the security of State of
        Maine information assets in accordance with Executive Order 25 FY 20/212 and Title
        5, Chapter 163 §1971-1985.3
6.2.    Agencies and OIT coordinate to meet all state and federal audit documentation and
        reporting compliance requirements.
7.0.    Compliance
7.1.    For State of Maine employees, failure to comply with this document may result in
        progressive discipline, up to and including dismissal.
7.2.    For State of Maine contractors and non-State of Maine personnel, failure to comply
        may result in the removal of the individual’s ability to access, and use, State of Maine
        data and systems. Employers of contractors will be notified of any violations.
7.3.    Personnel are also subject to any applicable penalties for statutory requirements
        compliance violations. Depending on the requirement, and the nature of the
        violation, penalties could include fines and/or criminal charges.
8.0.    Procedures
8.1.    The following standards apply to, and represent, the security controls established to
        meet an acceptable level of protection for, State of Maine personnel screenings and

2 https://www.maine.gov/governor/mills/sites/maine.gov.governor.mills/files/inline-

files/EO%2082%2025.pdf
3 https://legislature.maine.gov/statutes/5/title5ch163sec0.html

State of Maine                                                                        Page 3 of 17

                        Personnel Security Policy and Procedures (PS)

        access to information assets. This policy, standards, and procedures align with and
        adhere to NIST Special Publication 800-53 r54, Internal Revenue Service Publication
        10755, Acceptable Risk Controls for Affordable Care Act (ACA), Medicaid, and
        Partner Entities 1.02’ (ARC-AMPE)6, Criminal Justice Information (see Definitions)
        Services Security Policy7, Health Insurance Portability and Accountability Act
        Security Rule8, and applicable State and Federal law.
          8.1.1.     Position Risk Designations (PS-2)
                 8.1.1.1.    OIT works with agencies to determine if positions will have access,
                             or the substantial possibility of access, to data types that have been
                             classified by OIT and the agency as having a Personally Identifiable
                             Information (PII) (see Definitions) Impact Level of High (see also
                             the corresponding Cybersecurity and Infrastructure Security
                             Agency (CISA) Traffic Light Protocol (TLP) (see Definitions)
                             category Red for examples of state and federally-protected data
                             types in this category, such as: Federal Tax Information (FTI) (see
                             Definitions), Protected Health Information (PHI) (see Definitions),
                             Social Security Administration (SSA) data, Criminal Justice
                             Information (CJI), Financial/Credit Card Information, etc.).
                 8.1.1.2.    Individuals, including State of Maine employees, contractors, and
                             third-party personnel, with potential access to data types
                             classified as having a High PII impact level/TLP Red (CJI, PHI, FTI,
                             SSA or any other state or federally protected data types) must be
                             screened to at least the minimum standards specified by law and
                             regulations.
                 8.1.1.3.    When a position’s responsibilities or access levels change so that
                             the position has access or the substantial possibility of access to
                             data types that have been classified by OIT as having a High PII
                             Impact Level/TLP Red data or other similarly protected data types,
                             the individual must be screened to at least the minimum standards
                             specified by law and regulations.
                 8.1.1.4.    The method for determining examination and screening
                             requirements for all OIT positions is outlined in the Bureau of
                             Human Resources’ (BHR) Human Resources Policy and Practices
                             Manual.9
          8.1.2.     Personnel Screening (PS-3)

4 https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
5 Publication 1075 (Rev. 11-2021)
6 https://www.cms.gov/files/document/arc-ampe-vol-1-v102-508-5cr-04112025.pdf
7 CJIS Security Policy Resource Center — LE
8 Combined Text of All Rules | HHS.gov

9 https://www.maine.gov/bhr/state-hr-professionals/rules-policies/policy-practices-manual

State of Maine                                                                              Page 4 of 17

                        Personnel Security Policy and Procedures (PS)

                 8.1.2.1.   As outlined in the federal Immigration Reform and Control Act of
                            1986, the State of Maine is required to hire only U.S. citizens, and
                            aliens, who are authorized to work in the U.S.
                 8.1.2.2.   As per the BHR Policy and Practices Manual, Form I-9 must be
                            completed within three business days of the date of hire. To
                            complete Form I-9, the employee must provide certain documents
                            to establish both the employee’s identity and eligibility for
                            employment.
                 8.1.2.3.   All personnel are subject to, at minimum, a state criminal
                            background check.
                            8.1.2.3.1.   In the event the background check reveals a prior
                                         criminal conviction, the criminal record may
                                         legitimately be considered pursuant to and using the
                                         screening criteria specified by BHR.
                 8.1.2.4.   Fingerprint-based Background Checks – Access to CJI: The State of
                            Maine has adopted the Federal Bureau of Investigation’s (FBI)
                            Criminal Justice Information Services (CJIS) Security Policy as its
                            minimum-security requirement for CJI. All Information Systems
                            developed, acquired, or utilized as a service by OIT containing
                            CJIS-regulated information incorporate this security standard. The
                            CJIS Security Policy provides Criminal Justice Agencies (CJA) and
                            Noncriminal Justice Agencies (NCJA) with a minimum set of
                            security requirements for access to FBI CJIS Division systems and
                            information and to safeguard CJI. All entities with access to, or who
                            operate in support of, the FBI CJIS Division’s services and
                            information must comply with the FBI’s CJIS Security Policy and its
                            minimum-security requirement for the safeguarding of CJI. This
                            includes personnel and contractors of State of Maine agencies.
                            8.1.2.4.1.   Fingerprint-based background checks are required for
                                         all personnel and contractors that have unescorted
                                         access to areas where CJI is processed (i.e.,
                                         OIT/Department of Public Safety (DPS) Datacenter or
                                         telco rooms), or they have network access, system or
                                         security administrative privileges to systems that store
                                         or process CJI.
                            8.1.2.4.2.   The CJIS Information Security Officer (ISO), within the
                                         DPS, Maine State Police, is responsible for ensuring
                                         adherence to the CJIS Security Policy. The CJIS ISO
                                         performs a national criminal history record check
                                         initially, and every five years thereafter for personnel
                                         with access or the substantial possibility of access to
                                         CJI. Fingerprint-based background checks are
                                         processed through either the State Identification

State of Maine                                                                          Page 5 of 17

                        Personnel Security Policy and Procedures (PS)

                                          Bureau or a local law enforcement agency; prints are
                                          forwarded to the CJIS ISO to conduct the fingerprint-
                                          based background check. Upon completion, the CJIS ISO
                                          provides a response of pass/fail to the OIT ISO contact,
                                          who notifies the appropriate OIT supervisor. OIT is
                                          responsible for registering all personnel and
                                          contractors with approved access to CJI for the
                                          appropriate level of CJIS Security Awareness Training
                                          in CJIS Online.
                             8.1.2.4.3.   Disqualifiers for access to CJI data are determined by
                                          the CJIS ISO.
                 8.1.2.5.    Fingerprint-based Background Checks - Access to FTI: IRS
                             Publication 1075, requires local agencies to establish a personnel
                             security program that ensures background investigations are
                             completed to the appropriate level for any individual who will
                             have access to FTI as part of their job duties, both current and
                             prospective applicants, employees, and contractors. Agencies must
                             comply with federal and state compliance standards and minimum
                             background check requirements to implement these requirements
                             (see MRSA Title 5, Chapter 163 §198610 for OIT’s governing
                             statute; other agency business partners are responsible for
                             establishing their own statutory and regulatory compliance
                             requirements for fingerprint-based background checks). The OIT
                             requirements are as follows:
                             8.1.2.5.1.   All OIT employees with access to FTI are subject to
                                          local and federal background checks, FBI fingerprint-
                                          based criminal history record checks (CHRC).
                             8.1.2.5.2.   All necessary steps are taken before an employee is
                                          allowed access to FTI.
                             8.1.2.5.3.   The suitability background check is favorable.
                             8.1.2.5.4.   Current employees must submit to a background check
                                          upon implementation of this policy and every 10 years
                                          thereafter.
                             8.1.2.5.5.   OIT performs an FBI fingerprint-based CHRC upon
                                          hiring, and every five years, for personnel who have
                                          access or the substantial possibility of access to FTI,
                                          starting within the calendar year of enactment of the
                                          State implementation law (see Title 5, Chapter 163
                                          §198611).

10 https://legislature.maine.gov/statutes/5/title5sec1986.html
11 https://legislature.maine.gov/statutes/5/title5sec1986.html

State of Maine                                                                           Page 6 of 17

                        Personnel Security Policy and Procedures (PS)

                            8.1.2.5.6.   OIT uses the suitability criteria guidance provided by
                                         BHR for determining suitability standards for access to
                                         FTI. These factors assist the agency with determining
                                         suitability for access to FTI.
                 8.1.2.6.   Agencies may impose additional screening requirements within
                            the law, provided they are not less stringent than the minimum
                            federal standards articulated above for applicable data types.
                            Agencies are also responsible for ensuring that an appropriate
                            review of contractor background checks are completed as
                            specified in the contract.
                 8.1.2.7.   Upon receipt of the results of a background check report for State
                            employees, BHR refers criminal history conviction information to
                            agency management, who determines if the potential or current
                            employee should gain or retain access to controlled data (see
                            Definitions).
                            8.1.2.7.1.   Agency management makes a final decision after
                                         considering the above-listed factors relevant to the
                                         potential or current employee’s employment on a case-
                                         by-case basis.
                            8.1.2.7.2.   Agency management determines whether hiring the
                                         individual would potentially threaten the safety and
                                         well-being of State of Maine data, information assets,
                                         and/or employees and the public due to the threat to
                                         information assets. A determination that an employee
                                         is not suitable to access PII, CJI, FTI, SSA, PHI, and/or
                                         other controlled data may result in dismissal or
                                         removal from a position requiring access to those.
                            8.1.2.7.3.   Notwithstanding the foregoing, a position not requiring
                                         access to PII, CJI, FTI, SSA, PHI, and/or other controlled
                                         data should be open and available, the employee may
                                         be reassigned to this position, subject to the business
                                         needs of the agency and the capabilities of the
                                         employee.
                            8.1.2.7.4.   BHR is consulted before a final decision is made.
                 8.1.2.8.   Employees may be rescreened when transferring position and at
                            the agency’s discretion. When an employee moves from one
                            position to another, the higher level of clearance (i.e., national over
                            State only) should be adjudicated.
                 8.1.2.9.   Commencement of individual employment for OIT includes
                            completing the OIT Pre-hire and orientation checklist and
                            guidelines’ (See Appendix B).
          8.1.3.     Personnel Terminations (PS-4, PS-4(2))

State of Maine                                                                           Page 7 of 17

                        Personnel Security Policy and Procedures (PS)

                 8.1.3.1.   Termination of individual employment from OIT includes
                            completing the ‘Exit interview checklist for OIT (See Appendix B).
                            8.1.3.1.1.   State of Maine employees and contractor supervisors
                                         must complete the requirements of this form for
                                         personnel leaving State of Maine employment. This
                                         form accounts for:
                                                8.1.3.1.1.1. Disabling information system access
                                                             prior to or during the personnel
                                                             termination process/action.
                                                8.1.3.1.1.2. Terminating/Revoking any
                                                             authenticators/credentials
                                                             associated with the individual.
                                                8.1.3.1.1.3. Conducting exit interviews that
                                                             include a discussion of non-
                                                             disclosure of information security
                                                             and privacy information.
                                                8.1.3.1.1.4. Retrieving all security-related,
                                                             information systems-related
                                                             organizational property.
                                                8.1.3.1.1.5. Retaining access to organizational
                                                             information and information
                                                             systems formerly controlled by the
                                                             terminated individual.
                                                8.1.3.1.1.6. Notifying OIT via the ticket system
                                                             User Request form within one
                                                             calendar day.
                 8.1.3.2.   As determined by agency management and approved by BHR,
                            employees terminated for cause are immediately escorted out of
                            the organization.
          8.1.4.     Personnel Transfers (PS-5)
                 8.1.4.1.   For personnel transfer, the sending agency, the receiving agency,
                            and OIT jointly define the access requirements over the 30 days
                            prior to the transfer, in accordance with the Access Control Policy
                            and Procedures12 and the Access Control Procedures for Users13,
                            and changes in operational and regulatory compliance
                            requirements.

12 https://www.maine.gov/oit/policies/AccessControlPolicy.pdf
13 https://www.maine.gov/oit/policies/AccessControlProceduresForUsers.pdf

State of Maine                                                                           Page 8 of 17

                              Personnel Security Policy and Procedures (PS)

                    8.1.4.2.       Within one business day of the transfer, OIT is notified by either
                                   the sending agency, or the receiving agency, via the enterprise
                                   ticketing system.
                    8.1.4.3.       Based upon regulatory requirements, the sending agency, the
                                   receiving agency, and OIT jointly decide on the following:
                                   8.1.4.3.1.       The disposition of the legacy (prior to the transfer)
                                                    directory account, email, records, and access rights to
                                                    information assets.
                                   8.1.4.3.2.       The creation of the new (following the transfer)
                                                    directory account, email, records, and access rights to
                                                    information assets.
                                   8.1.4.3.3.       The extent of access, if any, to the legacy (prior to the
                                                    transfer) email, records, and information assets, which
                                                    is allowed to the personnel following the transfer.
                    8.1.4.4.       Based upon regulatory requirements, and the access rights to
                                   information assets necessary for the new position (following the
                                   transfer), the receiving agency, OIT, the Attorney General’s Office,
                                   and the BHR jointly decide on any additional screening that may
                                   be required for the transferring personnel.
            8.1.5.        Access Agreements (PS-6)
                    8.1.5.1.       Prior to accessing controlled data, personnel complete
                                   confidentiality and security training as required by the regulating
                                   entity. Additionally, enterprise security awareness training is
                                   repeated annually as a baseline for all employees, as specified in
                                   Security Awareness Training Policy and Procedures.14
                                   8.1.5.1.1.       Security Awareness Training includes signing the Rules
                                                    of Behavior.15
                    8.1.5.2.       Depending on what categories of controlled data personnel have
                                   access to, additional training may need to be conducted and
                                   agreements, including nondisclosure agreements, or other
                                   documents completed.
            8.1.6.        Third-Party Personnel Security (PS-7)
                    8.1.6.1.       Third-party personnel consist of contractors and subcontractors
                                   who provide or are subject to provide services to a State of Maine
                                   agency under an identified interconnection security agreement,
                                   memorandum of understanding/agreement, or contract. Third-
                                   party personnel who could access State of Maine information

14 https://www.maine.gov/oit/policies/SecurityAwarenessTrainingPolicy.pdf
15 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/RulesofBehavior.pdf

State of Maine                                                                                     Page 9 of 17

                        Personnel Security Policy and Procedures (PS)

                            assets are required to meet the same personnel security screening
                            criteria and requirements as State of Maine employees.
                            Requirements for third-party personnel are stipulated in their
                            contract.
                            8.1.6.1.1.   All third-party personnel are subject to, at the
                                         minimum, a state criminal background check. Third-
                                         party personnel who have access, or the substantial
                                         possibility of access, to data types that have been
                                         classified by OIT as having a PII Impact Level of
                                         High/TLP category Red are also subject to additional
                                         security screening requirements as stipulated above for
                                         compliance with state and federal laws, regulations, or
                                         policies.
                            8.1.6.1.2.   The Safeguard Contract Language from IRS Publication
                                         1075 is incorporated within all contracts that involve
                                         access to FTI, systems which contain those, or Maine
                                         Revenue Service information systems.
                            8.1.6.1.3.   Agency management in conjunction with the OIT ISO,
                                         determines if a position involves access, or the
                                         substantial possibility of access, to State of Maine
                                         information technology systems, or to data types that
                                         have been classified by OIT as having a PII Impact Level
                                         of High/TLP category Red, that reside on those
                                         systems.
                 8.1.6.2.   Third-party personnel access to state and federally protected data
                            types designated as PII impact Level of High/TLP Red requires
                            prior approval from the appropriate federal entity. Agencies are
                            responsible for receiving the appropriate approvals prior to
                            allowing third-party personnel access.
                 8.1.6.3.   Third-party personnel are responsible for notifying the immediate
                            State of Maine supervisor of the personnel, as well as agency
                            management, of personnel transfers and/or terminations within
                            15 calendar days so OIT can secure confidential information and
                            equipment.
                 8.1.6.4.   Third-party personnel are required to comply with the same
                            security requirements, laws, regulations, and policies as State of
                            Maine personnel.
                            8.1.6.4.1.   Agency staff overseeing the work of third parties shall
                                         be responsible for communicating and enforcing
                                         applicable laws, as well as State and agency security
                                         policies, and procedures. Agencies must monitor third-
                                         party provider compliance.

State of Maine                                                                        Page 10 of 17

                        Personnel Security Policy and Procedures (PS)

                             8.1.6.4.2.   Non-disclosure Agreements must be signed by
                                          authorized representatives of the third party before
                                          any information technology services are delivered.
                             8.1.6.4.3.   State confidential data and information assets must not
                                          be released to third parties without properly executed
                                          contracts and confidentiality agreements. These
                                          contracts must specify conditions of use and security
                                          requirements and the access, roles, and responsibilities
                                          of the third party before access is granted.
                 8.1.6.5.    IT Procurement works with the agencies to ensure compliance
                             with third-party personnel requirements.
          8.1.7.     Personnel Sanctions (PS-8)
                 8.1.7.1.    For State of Maine employees, failure to comply with the
                             procedures identified in this policy may result in progressive
                             discipline up to and including dismissal.
                 8.1.7.2.    For State of Maine contractors and non-State of Maine personnel,
                             failure to meet and comply with security policies and procedures
                             may result in removal of the individual’s ability to access and use
                             State of Maine data and systems, as well as whole or partial
                             termination of the contract depending on the nature of the breach.
                             Employers of non-State of Maine personnel will be notified of any
                             violations.
                 8.1.7.3.    In addition, for contractors, the failure to maintain the State’s
                             minimum-security standards during the term of the contract,
                             including renewals, will result in whole or partial termination of
                             the contract, depending on the nature of the breach.
                 8.1.7.4.    Personnel are also subject to any applicable penalties for statutory
                             requirements compliance violations. Depending on the
                             requirement and the nature of the violation, penalties could
                             include fines and/or criminal charges.
          8.1.8.     Position Descriptions (PS-9)
                 8.1.8.1.    SOM positions explicitly state security and privacy roles and
                             responsibilities as required by Title 5, §1982: Powers and duties.16
                             8.1.8.1.1.   The Chief Information Officer (CIO) is responsible for
                                          establishing rules for safeguarding, maintenance, and
                                          use of information systems and data.
                             8.1.8.1.2.   Agencies are responsible for documenting and
                                          assigning privacy responsibilities to meet relevant

16 https://legislature.maine.gov/legis/statutes/5/title5sec1982.html

State of Maine                                                                         Page 11 of 17

                        Personnel Security Policy and Procedures (PS)

                                          regulatory compliance requirements and business
                                          needs.
9.0.      Document Details
9.1.      Initial Issue Date: December 07, 2022
9.2.      Latest Revision Date: September 19, 2025
9.3.      Point of Contact: PolicyTeam.OIT@Maine.Gov
9.4.      Approved By: Chief Information Officer, OIT
9.5.      Legal Citation: Title 5, Chapter 163: Office of Information Technology 17
9.6.      Waiver Process: Waiver Policy 18
9.7.      Distribution: Internet19
10.0.     Review
          This document will be reviewed triennially, and when substantive changes are
          made to Policies, Procedures, or other authoritative regulations affecting this
          document.
11.0.     Records Management
          OIT security policies, plans, and procedures fall under the Major Administrative
          Policies and Procedures and Internal Control Policies and Directives records
          management categories. They will be retained for a minimum of six years after
          withdrawal or replacement and then destroyed in accordance with guidance20
          provided by Maine State Archives. Retention of these documents will be subject to
          any future State Archives General Schedule revisions that cover these categories.
12.0.     Public Records Exceptions
          Under the Maine Freedom of Access Act (FOAA),21 certain public records
          exceptions may limit disclosure of agency records related to information
          technology infrastructure and systems, as well as to security plans, procedures, or
          risk assessments. Information contained in these records may be disclosed to the
          Maine State Legislature or, in the case of a political or administrative subdivision,
          to municipal officials or board members under conditions that protect the
          information from further disclosure. Any aggrieved person seeking relief for an
          alleged violation of the FOAA may bring suit in any Superior Court in the State.
13.0.     Definitions
13.1.     Availability: Timely and reliable access to and use of information assets.

17 https://legislature.maine.gov/statutes/5/title5ch163sec0.html
18 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/waiver.pdf
19 https://www.maine.gov/oit/policies-standards
20 https://www.maine.gov/sos/arc/records/state/GS1Administrative.pdf
21 https://legislature.maine.gov/statutes/1/title1sec402.html

State of Maine                                                                         Page 12 of 17

                      Personnel Security Policy and Procedures (PS)

13.2. Confidentiality: The state of being kept private or secret, including preserving
      authorized restrictions on information access and disclosure, including means for
      protecting personal privacy and proprietary information.
13.3. Controlled Data: Information that law, regulation, or policy requires safeguarding or
      disseminating controls, special handling safeguards, or protection from
      unauthorized disclosure. All controlled data is TLP: Red, but not all TLP: Red data is
      controlled. Includes but is not limited to FTI, CJI, and PHI.
13.4. Criminal Justice Information (CJI): CJI is the abstract term used to refer to all of the
      Federal Bureau of Investigations (FBI) Criminal Justice Information Services (CJIS)
      provided data necessary for law enforcement agencies to perform their mission and
      enforce the laws, including but not limited to: biometric, identity history, person,
      organization, property (when accompanied by any PII), and case/incident history
      data. In addition, CJI refers to the FBI CJIS-provided data necessary for civil agencies
      to perform their mission; including, but not limited to, data used to make hiring
      decisions.
13.5. Federal Tax Information (FTI)
          13.5.1.   FTI consists of federal tax returns and return information (and
                    information derived from it) that is in the agency’s possession or control,
                    which is covered by the confidentiality protections of the Internal
                    Revenue Code (IRC), and subject to the IRC 6103(p)(4) safeguarding
                    requirements including IRS oversight. FTI may contain PII.
          13.5.2.   FTI includes return or return information received directly from the IRS
                    or obtained through an authorized secondary source, such as SSA,
                    Federal Office of Child Support Enforcement, Bureau of the Fiscal Service,
                    or Centers for Medicare and Medicaid Services, or another entity acting
                    on behalf of the IRS pursuant to an IRC 6103(p)(2)(B) Agreement.
          13.5.3.   FTI includes any information created by the recipient that is derived from
                    federal return or return information received from the IRS or obtained
                    through an authorized secondary source.
13.6. Information asset: Used interchangeably with Information System. A discrete,
      identifiable piece of information technology, including hardware, software,
      firmware, systems, services, and related technology assets used to execute work on
      behalf of OIT or another State agency. (National Institute of Standards and
      Technology (NIST) Special Publication (SP) 800-30).
13.7. Integrity: The accuracy and consistency (validity) of data over its lifecycle. Guarding
      the integrity of information assets against improper modification or destruction
      includes ensuring information nonrepudiation and authenticity.
13.8. Personally Identifiable Information (PII): Information that can be used to distinguish
      or trace the identity of an individual (e.g., name, Social Security Number, biometric
      records, etc.) alone, or when combined with other personal or identifying
      information that is linked or linkable to a specific individual (e.g., date and place of
      birth, mother’s maiden name, etc.).

State of Maine                                                                      Page 13 of 17

                        Personnel Security Policy and Procedures (PS)

13.9. Protected Health Information (PHI): PHI means individually identifiable health
      information that is transmitted by electronic media, maintained in electronic media,
      or transmitted or maintained in any other form or medium. This definition excludes
      individually identifiable health information in education records covered by the
      Family Educational Rights and Privacy Act, in employment records held by a covered
      entity in it its role as employer, and regarding a person who has been deceased for
      more than 50 years.
13.10. Traffic Light Protocol (TLP): OIT subscribes to the U.S. Department of Homeland
       Security CISA Traffic Light Protocol22 classification levels. See the Risk Assessment
       Policy and Procedures (RA-1)23 and the Data Classification Policy24 for a description
       of the classification levels.
14.0.     Abbreviations
14.1. BHR: Bureau of Human Resources
14.2. BYOD: Bring Your Own Device
14.3. CHRC: Criminal History Record Checks
14.4. CIO: Chief Information Officer
14.5. CISA: Cybersecurity and Infrastructure Security Agency
14.6. CJA: Criminal Justice Agencies
14.7. CJI: Criminal Justice Information
14.8. CJIS: Criminal Justice Information Services
14.9. DPS: Department of Public Safety
14.10. FBI: Federal bureau of Investigation
14.11. FTI: Federal Tax Information
14.12. IRC: Internal Revenue Code
14.13. ISO: Information Security Officer
14.14. NCJA: Noncriminal Justice Agencies
14.15. NIST: National Institute of Standards and Technology
14.16. OIT: Office of Information Technology
14.17. PHI: Protected Health Information
14.18. PII: Personally Identifiable Information
14.19. PS: Personnel Security

22 https://www.us-cert.gov/tlp
23 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/RiskAssessmentPolicyProcedure.pdf
24 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/DataClassificationPolicy.pdf

State of Maine                                                                                     Page 14 of 17

                     Personnel Security Policy and Procedures (PS)

14.20. SID: Security Identifier
14.21. SSA: Social Security Administration
14.22. TLP: Traffic Light Protocol

State of Maine                                                       Page 15 of 17

                          Personnel Security Policy and Procedures (PS)

      Appendix A: OIT Pre-Hire and Orientation Checklist and Guidelines

Supervisor:                                 Report Org (4-digit billing code):

Name:                                   Position:                                Start Date:

    Check One: _____ State Employee _____ Contractor
Item             Description                 Date         Initial       Form/Letter/Email
  #       (see next page for guide)                                        Completed
Prior to first day, supervisor collaborates with BHR and OIT for:
 1.    Background Check And I-9
2.       REQUEST FOR SECURITY
         BADGE (This Also Pertains to
         Contractors)
3.       Telephone Access Code – Pin
4.       Telephone Work Order
5.       SECURID
6.       Set Up Exchange E-Mail                                     User Ticket#
         (New/Modify/Delete User
         Request Form)                                              Footprints#

                                                                    Footprints#

7.       Cellular Phone or Smartphone
First day, supervisor works with BHR and employee to:
 8.    IT Policy
9.       BYOD
10.      Security and Privacy
         Awareness Training Including
         Rules of Behavior
11.      Work Rule – State Owned
         Equipment

      State of Maine                                                                Page 16 of 17

                         Personnel Security Policy and Procedures (PS)

Prior to first day:
• Background check and I-9: Prior to being offered a position, all potential State of
   Maine employees are subject to a state background check and I-9. The Personnel Office
   conducts these.
• Request for physical access badge: Please open a physical access request25 for a new
   badge (instructions).26 On their start date, please send the new hire to see the
   Enterprise Security Team for a badge photo. They will issue a physical access badge as
   long as the above has been completed and approved.
• Telephone Access Code: Complete on-line form27 indicating the limit for the telephone
   ID. Limits are 0 = International, 1 = North America, 2 = New England, 3 = Maine.
• Telephone Work Order: Initiate a Telephone Work Order Request ticket.28
• SecurID: For employees that will remote access State of Maine information assets,
   initiate a SecurID ticket.29
• New/Modify User and Computer request: Initiate a User Request ticket at
   New/Modify/Delete User Form to set up Active Directory (email), printers, distribution
   list, application access, and request device. The device is ordered on the same footprints
   ticket as the user request.
• Request phone/smartphone: If an employee requires a cellular phone or smartphone,
   complete the State Cellular Request Form.30

First day:
• Bring your own device (BYOD): If the employee wishes to use their own cell phone or
   smartphone for work-related functions and/or to access State of Maine information
   assets, including the SOM AIRE network, Intune and Lookout must be installed.
   Instructions and the request form are found at the Mobile Device Portal.31 See the
   Mobile Device Policy32 for more details.
• IT Policy: The Personnel Office will have the employee acknowledge the IT Policy.33 For
   contractors, the supervisor will ensure that the contractor acknowledges the IT Policy.
• Security and Privacy Awareness training: Enterprise Security Awareness training is
   automatically pushed out to new Agency personnel with email addresses. Agencies are

25 https://footprints.state.me.us/footprints/security.html
26 https://footprints.state.me.us/footprints/help/tutorials/security-request.pdf
27 http://inet.state.me.us/oit/eforms/access-codes/index.html
28 https://footprints.state.me.us/footprints/telco.html
29 http://footprints.state.me.us/footprints/rsa.html
30

https://stateofmaine.sharepoint.com/:w:/r/sites/MaineIT/Shared%20Documents/Employee%20Forms/sta
te-cellular-request-form02122018.doc?d=wa7617f0b99164835912e64bc4cf5e1af&csf=1&web=1&e=PfXcST
31 https://stateofmaine.sharepoint.com/sites/MaineIT/SitePages/Mobile/Mobile-Devices.aspx
32 https://www.maine.gov/oit/policies/MobileDevicePolicy.pdf
33 https://www.maine.gov/bhr/sites/maine.gov.bhr/files/inline-files/DAFSITPolicy.pdf

State of Maine                                                                      Page 17 of 17

                     Personnel Security Policy and Procedures (PS)

    responsible for the delivery of enterprise security awareness training for any agency
    personnel without a state email address.

State of Maine                                                                   Page 18 of 17

                                   Personnel Security Policy and Procedures (PS)

Appendix B: Exit Interview Checklist for OIT

Contingency Plan Participation:
 Employee holds a position of responsibility in the following contingency plans:                                     Yes    No
 Incident Response Policy and Procedures (IR)
 Contingency Planning Policy and Procedures (CP)
 Business Continuity and Disaster Recovery Policy
Have these roles been reassigned? Yes____ No_____

Office and Confidential Files
 Have the following been collected?                                                                            Yes   N/A   Date
 Office sensitive files
 Confidential information
 Protected information

Computing Equipment Asset Inventory
 Has the employee returned the following?                                                                      Yes   N/A   Date
 Laptop/desktop
 Mobile phone
 SecurID Key
 Flash Drives
 External Hard Drives
 Printers
 ID Badge
 Keys
 Security alarm codes
 Voice mail password
 Laptop security cable lock
 Other computing office equipment

Access Termination
 Have the following been completed?                                                                            Yes   N/A   Date
 OIT ticket to modify/delete user
 Procedure for Handling Files and Email of Departing or Transferring Users 34 (internal
 only)

Transition Period and Plan
 Have the following been completed?                                                                            Yes   N/A   Date
 Transfer of knowledge
 Transfer of accounts
 Location of electronic files

34http://inet.state.me.us/foaa/documents/ProcedureforHandlingFilesandEmailofDepartingorTransferringUsers.pdf

State of Maine                                                                                                       Page 19 of 17

                 Personnel Security Policy and Procedures (PS)

State of Maine                                                   Page 20 of 17

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
