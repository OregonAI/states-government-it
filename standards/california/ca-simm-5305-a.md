---
schema_version: 1
corpus: states-it-governance
jurisdiction: california
id: ca-simm-5305-a
title: Information Security Program Management Standard
doc_type: standard
citation: SIMM 5305-A
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5305-A-Information-Security-Program-Management-Standard.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 29f867ba4c8c366e414694ae1816ec7d677a162829238b3109da5688f92d4e80
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
- cybersecurity
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Information Security Program Management Standard (SIMM 5305-A)

## At a glance

SIMM 5305-A, Information Security Program Management Standard: an item of the Office of Information Security's information security series (SIMM 5300), the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

             State of California

        Department of Technology

Information Security Program
      Management Standard
Statewide Information Management Manual – 5305-A

                   April 2026

Table of Contents
Revision History ............................................................................................................ 2

Introduction ................................................................................................................... 3

   Purpose........................................................................................................................ 3

   Scope ........................................................................................................................... 3

   Compliance .................................................................................................................. 3

Information Security Program Management ............................................................... 4

   Governance ................................................................................................................. 4

   Security Program Management ................................................................................... 4

Information Security and Privacy Roles and Responsibilities .................................. 5

Information Asset Categorization and Classification .............................................. 19

   Information Classification ........................................................................................... 20

   Information System Security Categorization .............................................................. 23

Critical System Reporting .......................................................................................... 24

Policy, Standards, and Procedures Management .................................................... 25

   Administrative Policies and Procedures ..................................................................... 25

   Operational and Technical Policies and Procedures .................................................. 26

Questions..................................................................................................................... 29

California Department of Technology                                                                                                 1
Information Security Program Management
SIMM Section 5305-A                                                                                                      April 2026

  Revision History
 Revision         Date of Release           Owner                Summary of Changes

Initial Release   September 2013      California        Standard, procedure and instructions
     v. 1.0                           Information       transferred from State Administrative
                                      Security Office   Manual, Chapter
                                                        5300 to new standard

Minor Update      January 2018        Office of         Office Name Change; SIMM 5330- B
     v. 1.1                           Information       reference name change
                                      Security (OIS)

    Minor         July 2022           OIS               Consistent with the Policy, Standards
   Updates                                              and Procedure Management section
     v. 1.2                                             introduction and corresponding NIST
                                                        controls added “and procedure” where
                                                        missing; added additional examples for
                                                        limitation on ISO designation carrying
                                                        multiple roles; and “latest revision” for
                                                        NIST SP 800-53 reference added for
                                                        clarity.

Minor Update      December 2023       OIS               Updated GC 6250-
     v. 1.3                                             6265 to 7920.000-
                                                        7931.000

Minor Update      August 2025         OIS               Added roles and functions to Information
   v. 1.4                                               Security and Privacy Roles and
                                                        Responsibilities section, updated
                                                        verbiage for clarity and reviewed content.
                                                        Added a new section called "Critical
                                                        System Reporting" (on page 24)

Minor Update      September 2025      OIS               Explicitly added organizational policy
   v. 1.5                                               review/acceptance/approval as specific
                                                        function of State Entity Head

Minor Update      April 2026          OIS               Corrected typo introduced in v. 1.4,
   v. 1.6                                               restored social media policy as item d.
                                                        under Administrative Policies and
                                                        Procedures item 8.

  California Department of Technology                                                           2
  Information Security Program Management
  SIMM Section 5305-A                                                                  April 2026

Introduction

Purpose

Executive management within state entities must demonstrate a strong commitment to
information security and risk management. Risk management should include a clear
division of responsibilities among management, technical staff, and program personnel,
with written documentation outlining specific roles and duties.

Security policies and procedures within the state entity must be thoroughly documented,
and all staff members must be familiar with them.

This standard provides a framework for a top-down approach to establishing,
implementing, and governing a state entity’s Information Security Program (ISP). It
ensures that those responsible for protecting information assets actively drive and
nurture the program.

Scope

This standard applies to all California state entities, including agencies, departments,
divisions, bureaus, boards, and commissions, as defined in Government Code Section
11546.1.

Compliance

As outlined in Government Code (GC) Section 11549.3, the Office of Information
Security (OIS) is entrusted with creating, issuing, and maintaining policies, standards,
and procedures, overseeing information security risk management for agencies and
state entities, providing information security and privacy guidance, and ensuring
compliance with State Administrative Manual (SAM) Chapter 5300 and Statewide
Information Management Manual (SIMM) section 5300.

State entities must adhere to OIS-issued information security and privacy policies and
all relevant laws, regulations, rules, and standards governing their state entity.

California Department of Technology                                                          3
Information Security Program Management
SIMM Section 5305-A                                                                  April 2026

Compliance may be reflected in audit findings and maturity scores. Non-compliance will
be addressed according to the Office of Information Security Policy Compliance and
Enforcement Standard (SIMM 5330-H).

Information Security Program Management
Governance

Leadership, organizational structure, communications, relationships, and processes
form the basis of information security governance.

Information security governance will ensure the following:

   •   Alignment of information security objectives with business strategy

   •   Effective risk management

   •   Optimized security investments

   •   Measurable program results

Security Program Management

Information security program management shall be based upon an appropriate division
of responsibility among management, technical, and program staff, with written
documentation of specific responsibilities.

This principle extends to acting roles and backups filling in for the key security
personnel. Management must assign ownership of information assets, including each
automated file or database used by the state entity.

Normally, responsibility for automated information resides with the manager of the state
entity program that employs the information.

When the information is used by more than one program, considerations for determining
ownership responsibilities include the following:

   1. Which program collected the information?

   2. Which program is responsible for the accuracy and integrity of the information?

California Department of Technology                                                          4
Information Security Program Management
SIMM Section 5305-A                                                                  April 2026

   3. Which program budgets the costs incurred in gathering, processing, storing, and
       distributing the information?

   4. Which program has the most knowledge of the useful value of the information?

   5. Which program would be most affected, and to what degree, if the information
       were lost, compromised, delayed, or disclosed to unauthorized parties?

SAM Chapter 5300 provides the security and privacy policy framework that state entities
must follow. The Federal Information Processing Standards (FIPS), the National
Institute of Standards and Technology (NIST), Special Publication 800-53, and the
California government’s specific standards and procedures shall be used as the
implementation control framework.

Using these standards will facilitate a more consistent, comparable, and repeatable
approach to securing state assets and create a foundation from which standardized
assessment methods and procedures may be used to measure the security program's
effectiveness.

Information Security and Privacy Roles and Responsibilities
Each state entity shall ensure that the roles and responsibilities of information security
and privacy are effectively established and carried out in their organizations.

 Role                   Responsibility (Task)                Specific Functions (Task)
 Secretary/Director     Responsible for:                     • Approve, accept, and
                          • Entity operations                  assume accountability for all
 (or equivalent head
                             (including mission,               organizational policies.
 of the state entity,        functions, image, or            • On an annual basis, the
                             reputation).                      head of each state entity
 herein after
                          • The protection and                 must submit the following to
 referred to as state        appropriate use of                the Office of Information
 entity head)                information assets held by        Security (OIS):
                             the state entity.                  • A Designation Letter
                          • Taking reasonable                     (SIMM 5330-A)
                             measures for                         identifying the
                             implementation and                   designation of critical
                             maintenance of the                   personnel, including a
                             program.                             Chief Information Officer,
                                                                  Information Security
                                                                  Officer, Privacy
California Department of Technology                                                          5
Information Security Program Management
SIMM Section 5305-A                                                                April 2026

                            •   Understanding the state            Officer/Coordinator, and
                                entity’s RRPOAM and risk           Technology Recovery
                                management strategy.               Coordinator.
                            •   Ensuring compliance with        • A Technology Recovery
                                information security and           Program Certification
                                privacy requirements.              (SIMM 5325-B) along
                            •   Ensuring designated                with a copy of the state
                                personnel (Designees)              entity’s current
                                possess the qualifications,        Technology Recovery
                                authority, and                     Plan.
                                management support to           • An Information Security
                                carry out their designated         and Privacy Program
                                role and responsibility            Compliance Certification
                                effectively.                       (SIMM 5330-B) certifying
                            •   Ensuring knowledge and             that the state entity is in
                                understanding of any state         compliance with all
                                entity partnerships                requirements governing
                                including host/hosted and          information security, risk
                                steward/client                     state management, and
                                relationships.                     privacy for the state
                                                                   entity’s programs.
                                                                • An Information
                                                                   Technology Cost Report
                                                                   (SIMM 55-B & 55-C)
                                                                   summarizing the entity’s
                                                                   actual and projected IT
                                                                   costs.
 Executive              Responsible for:                      On an ongoing basis:
 Management               • Establishing the                     • Be visibly committed to
                             governance body that will              achieving information
                             direct staff resources,                security program goals
                             funding, and the activities            and objectives and
                             necessary to implement                 practicing management.
                             and maintain the                    • Create a security and
                             information security                   privacy-aware
                             program fully.                         organizational culture.
                          • Effectively managing risk            • Complete annual
                             and achieving compliance               information security and
                             with information security              privacy training
                             and privacy laws and
                             regulations.
 Agency Chief           Responsible for:                      On an ongoing basis:
 Information              • IT, including IT assets,             • Be visibly committed to
 Officer (AIO)               projects, and                          achieving information
                             infrastructure, through the            security program goals
                             oversight and                          and objectives and
California Department of Technology                                                        6
Information Security Program Management
SIMM Section 5305-A                                                                April 2026

                             management of the CIO                 practicing risk
                             and development of                    management.
                             Agency Enterprise                 •   Attend Information
                             Architectures.                        Technology Leadership
                          • Providing oversight,                   Executive Council
                             driving adoption of                   (ITEC).
                             strategies, and reporting         •   Create a security and
                             on cybersecurity risk to              privacy-aware
                             state entities.                       organizational culture.
                          • Ensuring the creation and          •   Be informed of
                             maintenance of Agency                 cybersecurity incidents.
                             cybersecurity policies,           •   Complete annual
                             standards, and                        information security and
                             procedures.                           privacy training.
                          • Ensuring the
                             establishment and
                             maintenance of
                             information security and
                             privacy programs.
                          • Providing oversight and
                             driving the adoption of risk
                             mitigating strategies for
                             departments within their
                             agency.
                          • Providing oversight,
                             identifying, and
                             implementing risk
                             mitigation plans of action
                             and milestones that
                             mitigate and remediate
                             risks across multiple
                             departments within their
                             agency.
                          • Providing oversight and
                             flex resources between
                             departments within their
                             agency for information
                             security program resource
                             gaps.
 Agency Chief           Responsible for:                    On an ongoing basis:
 Information              • The creation and                   • Attend Information
 Security Officer            maintenance of Agency                Security Advisory
 (AISO)                      cybersecurity policies,              Council (ISAC).
                             standards and                     • Complete the “ISO
                             procedures.                          Basic Training” course
                                                                  offered by OIS, within
California Department of Technology                                                      7
Information Security Program Management
SIMM Section 5305-A                                                              April 2026

                            •Coordination of OIS                    the six months of
                             requirements and                       designation.
                             initiatives with state entity      •   Be visibly committed to
                             ISOs.                                  achieving information
                          • Informing and advising                  security program goals
                             Agency leadership on                   and objectives and
                             cybersecurity risks,                   practicing risk
                             threats, and incidents.                management.
                          • Assisting with resource             •   Create a security and
                             prioritization.                        privacy-aware
                          • Reinforcing statewide                   organizational culture.
                             cybersecurity culture.             •   Attend the OIS-chaired
                          • Developing and exercising               ISO and Incident
                             Agency strategy to                     Response Bi-monthly
                             leverage capabilities and              meetings.
                             resources across the               •   Not be assigned
                             Agency.                                multiple designated
                          • Establishing and                        roles or roles that
                             maintaining information                present a conflict of
                             security and privacy                   interest, such as having
                             programs.                              direct responsibility for
                          • Providing oversight and                 application
                             driving the adoption of risk           development,
                             mitigating strategies for              information processing,
                             departments within their               technology operations,
                             agency.                                internal auditing
                          • Providing oversight,                    functions, or state entity
                             identifying and                        programs.
                             implementing risk                  •   Complete annual
                             mitigation plan of action              information security and
                             and milestones that                    privacy training
                             mitigate and remediate
                             risks across multiple
                             departments within their
                             agency.
                          • Providing oversight and
                             flex resources between
                             departments within their
                             agency for information
                             security program resource
                             gaps.
 Chief Information      Responsible for:                     On an ongoing basis:
 Officer (CIO)            • Overseeing the                      • Be visibly committed to
                             information technology                achieving information
                             portfolio and information             security program goals
                             technology services within            and objectives and
California Department of Technology                                                        8
Information Security Program Management
SIMM Section 5305-A                                                                April 2026

                             his or her state entity            practicing risk
                             through the operational            management.
                             oversight of information        • Create a security and
                             technology budgets of              privacy-aware
                             departments, boards,               organizational culture.
                             bureaus, and offices within     • Complete annual
                             the state entity.                  information security and
                          • Developing the enterprise           privacy training
                             architecture for the state
                             entity, subject to the
                             review and approval of the
                             California Technology
                             Agency, to rationalize,
                             standardize, and
                             consolidate information
                             technology applications,
                             assets, data, and
                             procedures for all
                             departments, divisions,
                             and offices within the state
                             entity.
                          • Providing oversight,
                             driving adoption of
                             strategies, and reporting
                             on cybersecurity risk to
                             state entities.
                          • Ensuring the creation and
                             maintenance of state
                             entity cybersecurity
                             policies, standards, and
                             procedures.
                          • Ensuring the
                             establishment and
                             maintenance of
                             information security and
                             privacy programs.
 Information            Responsible for:                  On an ongoing basis:
 Security Officer         • Manage and oversee the           • Complete the “ISO
 (ISO)                       state entity’s Information         Basic Training” course
                             Security and Privacy               offered by OIS, within
                             Programs, ensuring the             the first six months of
                             protection of the state            designation.
                             entity’s information assets.    • Attend the OIS-chaired
                          • Providing oversight,                ISO and Incident
                             driving adoption of                Response Bi-monthly
                             strategies, and reporting          meetings.
California Department of Technology                                                   9
Information Security Program Management
SIMM Section 5305-A                                                           April 2026

                             on cybersecurity risk to        • Create a security and
                             state entities.                    privacy-aware
                          • Ensuring the creation and           organizational culture.
                             maintenance of state            • Be informed of security
                             entity cybersecurity               incidents and assist in
                             policies, standards, and           remediation.
                             procedures.                     • Not be assigned
                          • Coordination of OIS                 multiple designated
                             requirements and                   roles or roles that
                             initiatives.                       present a conflict of
                          • Informing and advising              interest, such as having
                             state entity leadership on         direct responsibility for
                             cybersecurity risks,               application
                             threats, and incidents.            development,
                          • Emphasizing                         information processing,
                             cybersecurity                      technology operations,
                             management and strategic           internal auditing
                             planning, driving the              functions, or state entity
                             implementation of                  programs.
                             baseline cybersecurity          • Complete annual
                             capabilities, and attesting        information security and
                             to their maturity.                 privacy training.
                          • Assisting with resource
                             prioritization.
 Technology             Responsible for:                  On an ongoing basis:
 Recovery                 • Working with the state           • Complete the “ISO
 Coordinator (TRC)           entity’s program                   Basic Training” course
                             management (business               offered by the OIS,
                             owners) and continuity             within the first six
                             planners to develop, test          months of designation.
                             and maintain a technology       • Attend the OIS chaired
                             recovery plan.                     TRC Bi- monthly
                          • Representing the state              meetings.
                             entity in the event of a        • Not be assigned
                             disaster or other event            multiple designated
                             resulting in the severe loss       roles or roles which
                             of information technology          present a conflict of
                             systems capabilities.              interest, such as having
                          • Possessing the                      direct responsibility for
                             qualifications (education,         application
                             training, skills, and              development,
                             knowledge) sufficient to           information processing,
                             effectively execute the            technology operations,
                             duties and responsibilities        internal auditing
                             of the position, including         functions, or for state
                             sufficient knowledge of            entity programs.
California Department of Technology                                                    10
Information Security Program Management
SIMM Section 5305-A                                                             April 2026

                             information management          • Complete annual
                             and information                    information security and
                             technology within the state        privacy training.
                             entity to work effectively
                             with the data centers and
                             vendors in re- establishing
                             information processing
                             and telecommunications
                             services after an event
                             has occurred.
 Privacy                Responsible for:                  On an ongoing basis:
 Officer/Privacy          • Maintaining an ongoing           • Complete the “ISO
 Program                     privacy program, including         Basic Training” course
 Coordinator                 an annual training                 offered by OIS, within
 (occasionally               component for existing             the first six months of
 referred to as the          and new personnel.                 designation.
 Disclosure Officer)      • Ensuring the state entity        • Attend the OIS-chaired
                             complies with all of the           Privacy Bi-monthly
                             provisions of the California       meetings.
                             Information Practices Act       • Not be assigned
                             (Civil Code Section 1798           multiple roles
                             et seq.) and any other             designated roles or
                             privacy-related legal              roles that present a
                             requirements that may              conflict of interest, such
                             apply to the administration        as having direct
                             of the state entity’s              responsibility for
                             programs, including but            application
                             not limited to, Government         development,
                             Code section 11019.9 and           information processing,
                             State Administration               technology operations,
                             Manual 5310-5310.7.                internal auditing
                                                                functions, or state entity
                                                                programs.
                                                             • Complete annual
                                                                information security and
                                                                privacy training
                                                             • Assist program
                                                                management with
                                                                conducting Privacy
                                                                Impact Assessments
                                                             • Assist program
                                                                management, technical
                                                                management, and the
                                                                ISO with incident
                                                                response when

California Department of Technology                                                    11
Information Security Program Management
SIMM Section 5305-A                                                             April 2026

                                                                incidents involve
                                                                personal information.
 Information            Responsible for:                  On an ongoing basis:
 Technology (IT)          • Implementing the                 • Be visibly committed to
 Management                  necessary technical                achieving information
                             controls to preserve the           security program goals
                             state entity's information         and objectives and
                             assets' confidentiality,           practicing risk
                             integrity, and availability.       management.
                          • Managing the risks               • Creating a security and
                             associated with those              privacy-aware
                             assets.                            organizational culture.
                          • Monitor and report any           • Complete annual
                             actual or attempted                information security and
                             security incidents to the          privacy training and
                             information security               ensure personnel
                             officer.                           supervised complete
                                                                annual training.
 Personnel              Responsible for:                  On an ongoing basis:
 Management               • Working closely with the         • Assist with the
                             information asset owners,          identification of security
                             program management, the            roles and
                             ISO, and Privacy                   responsibilities for all
                             Officer/Privacy Program            personnel to ensure
                             Coordinator to establish,          they are informed of
                             implement and enforce              their roles and
                             information security and           responsibilities for using
                             privacy program                    state entity information
                             requirements.                      assets, to reduce the
                          • Consulting the California           risk of inappropriate
                             Department of Human                use, and to establish a
                             Resources.                         documented process to
                                                                remove access when
                                                                changes occur.
                                                             • Implement employment
                                                                history, fingerprinting
                                                                and or criminal
                                                                background checks on
                                                                personnel who work
                                                                with or have access to
                                                                confidential, personal,
                                                                or sensitive information
                                                                or critical applications
                                                                as necessary and within
                                                                the state entity’s
                                                                authority to do so.
California Department of Technology                                                    12
Information Security Program Management
SIMM Section 5305-A                                                             April 2026

                                                           •  Assist with ensuring
                                                              state entity personnel
                                                              receive security and
                                                              privacy awareness
                                                              training regarding user,
                                                              state entity, and
                                                              statewide security
                                                              responsibilities and
                                                              policies before being
                                                              granted access to
                                                              information assets and
                                                              at least annually
                                                              thereafter.
                                                           • Assist with the receipt
                                                              and maintenance of
                                                              signed
                                                              acknowledgments of
                                                              security responsibility
                                                              by all personnel.
                                                           • Assist with transfer
                                                              procedures that ensure
                                                              access rights and
                                                              permissions to state
                                                              entity information
                                                              assets are reviewed for
                                                              appropriateness and
                                                              reauthorized by
                                                              program management
                                                              when personnel are
                                                              transferred within the
                                                              state entity so that
                                                              access to information
                                                              assets is limited to what
                                                              personnel need to
                                                              perform their job-related
                                                              duties.
                                                           • Assist with termination
                                                              procedures that ensure
                                                              state entity information
                                                              assets are not
                                                              accessible to separated
                                                              personnel.
 Program                Responsible for the following   On an ongoing basis:
 Management (also       within their areas of program      • Be visibly committed to
 often referred to as   responsibility:                       achieving information
                                                              security program goals
California Department of Technology                                                 13
Information Security Program Management
SIMM Section 5305-A                                                          April 2026

 Business                   •   Specify the business                 and objectives and
 Managers)                      needs as expressed in                practicing risk
                                terms of confidentiality,            management.
                                integrity, and availability      •   Creating a security and
                                requirements for                     privacy-aware
                                information processes and            organizational culture.
                                systems (both manual and         •   Complete annual
                                automated) used to                   information security and
                                administer state entity              privacy training and
                                programs.                            ensure personnel
                            • Working collaboratively                supervised complete
                                with the ISO and                     annual training.
                                Governing Body to
                                develop and implement
                                program-specific
                                information handling
                                policies, procedures, and
                                practices.
                            • Monitoring the security
                                and use of information
                                assets.
                            • Ensuring program staff
                                and other information
                                users are informed of and
                                carry out information
                                security and privacy
                                responsibilities.
 Information Asset      Responsible for the following         On an ongoing basis:
 Owners (often the      within their areas of program            • Coordinate these
 Program Unit and       responsibility:                             responsibilities with the
 Management                 • Eliminating the                       state entity ISO and
 affiliated with a              unnecessary collection,             Privacy Officer/Privacy
 particular program)            use, and maintenance of             Program Coordinator.
                                personal information in          • Perform these
                                state entity records.               responsibilities
                            • Providing proper notice               throughout the
                                with the collection of              information security life
                                personal information, as            cycle of the information
                                required by Civil Code              asset until its proper
                                Section 1798.17 and in              disposal.
                                accordance with the              • Complete annual
                                Privacy Statement and               information security and
                                Notices Standard (SIMM              privacy training
                                5310-A)
                            • Subject to executive
                                management review,
California Department of Technology                                                       14
Information Security Program Management
SIMM Section 5305-A                                                                April 2026

                                classifying information
                                assets, including each
                                record, file, or database
                                for which it has ownership
                                responsibility in
                                accordance with the need
                                for precautions in
                                controlling access to and
                                preserving the security
                                and integrity of the
                                information asset.
                            •   Defining precautions for
                                controlling access to and
                                preserving the security
                                and integrity of information
                                assets that have been
                                classified as requiring
                                such precautions.
                            •   Authorizing access to the
                                information in accordance
                                with the classification of
                                the information and
                                legitimate business need
                                for access to the
                                information.
                            •   Monitoring and ensuring
                                compliance with all
                                applicable laws, state
                                entity and state security
                                policies and procedures
                                affecting the information.
                            •   Identify the level of
                                acceptable risk for each
                                information asset.
                            •   Reporting security
                                incidents and filing
                                Information Security
                                Incident Reports with the
                                OIS. See SAM Section
                                5340. NOTE: This is
                                usually done through the
                                ISO or the Privacy Officer.
                            •   Submitting a breach
                                notification to the OIS for
                                review and approval

California Department of Technology                                   15
Information Security Program Management
SIMM Section 5305-A                                            April 2026

                             before its dissemination or
                             release to any individuals.
                          • Monitoring and ensuring
                             authorized users and
                             custodians know and
                             comply with these
                             responsibilities.
 Designers/Develo       Responsible for:                  On an ongoing basis:
 pers of                  • Working collaboratively          • Coordinate with the
 Information                 with the information asset         information asset owner
 Systems and                 owner, the ISO, and the            and the state entity ISO
 Applications                privacy officer/coordinator        and Privacy
                             for their state entity to          Officer/Privacy Program
                             identify and document              Coordinator.
                             system confidentiality,         • Complete annual
                             integrity, and availability        information security and
                             requirements.                      privacy training.
                          • Ensuring system design
                             and architecture are
                             implemented to support
                             security requirements and
                             enforcement of security
                             policies and procedures.
                          • Applying secure coding
                             standards and practices,
                             which include adherence
                             to the principle of least
                             privilege, use of default
                             deny protection schema,
                             input validation, sanitizing
                             data, threat modeling,
                             defense in-depth strategy,
                             and effective quality
                             assurance techniques.
 IT Personnel           Responsible for:                  On an ongoing basis:
                          • Working closely with the         • Implement and enforce
                             ISO in establishing and            the necessary technical
                             implementing a systematic          controls to preserve the
                             process to prevent                 state entity's
                             potential adversaries from         information assets'
                             obtaining confidential,            confidentiality, integrity,
                             sensitive, or personal             and availability.
                             information related to the      • Manage the risks
                             state entity’s planning and        associated with those
                             activities.                        assets.

California Department of Technology                                                     16
Information Security Program Management
SIMM Section 5305-A                                                              April 2026

                                                              • Monitor for and report
                                                                any actual or attempted
                                                                security incidents to the
                                                                Information Security
                                                                Officer.
                                                             • Maintain strong
                                                                passwords, at least 15
                                                                characters, for all
                                                                system administrator
                                                                accounts.
                                                             • Not use system
                                                                administrator accounts
                                                                for anything other than
                                                                system administration
                                                                functions.
                                                             • Complete annual
                                                                information security and
                                                                privacy training.
 Security               Responsible for:                  On an ongoing basis:
 Operations               • Working closely with the         • Monitor for and report
 Personnel                   ISO in establishing and            any actual or attempted
                             implementing a systematic          security incidents to the
                             process to prevent                 Information Security
                             potential adversaries from         Officer.
                             obtaining confidential,         • Maintain strong
                             sensitive, or personal             passwords, at least 15
                             information related to the         characters, for all
                             state entity’s planning and        system administrator
                             activities through:                accounts.
                          • Identification of                • Complete annual
                             confidential, sensitive, or        information security and
                             personal information               privacy training.
                          • Analysis of threats
                          • Analysis of vulnerabilities
                          • Assessment of risks
                          • Application of appropriate
                             countermeasures.
 Custodians of          Responsible for:                  On an ongoing basis:
 Information              • Monitoring and ensuring          • Monitor for and report
                             compliance with all                any actual or attempted
                             applicable laws, and state         security incidents to the
                             entity and state security          Information Security
                             policies and procedures            Officer.
                             affecting the information.      • Complete annual
                          • Complying with any                  information security and
                             additional security policies       privacy training
California Department of Technology                                                   17
Information Security Program Management
SIMM Section 5305-A                                                            April 2026

                                and procedures
                                established by the
                                information asset owner
                                and the state entity ISO.
                            •   Advising the information
                                asset owner and the state
                                entity ISO of vulnerabilities
                                that may threaten the
                                information and of specific
                                means of protecting that
                                information.
                            •   Notifying the information
                                asset owner and the state
                                entity ISO of any actual or
                                attempted violations of
                                security policies,
                                practices, and procedures.

 Information Asset      Responsible for:                 On an ongoing basis:
 Users                    • Using state information         • Monitor for and report
                             assets only for state             any actual or attempted
                             purposes.                         security incidents to the
                          • Taking adequate steps to           Information Security
                             safeguard the confidential,       Officer.
                             personal, or sensitive         • Complete annual
                             information in your care          information security and
                             from unauthorized view            privacy training if
                             and access, use,                  applicable to the role.
                             modification, disposal,
                             loss, or theft, whether
                             paper records or
                             electronic devices
                             containing protected
                             information such as a
                             laptop or mobile device.
                          • Limiting access and use of
                             state information assets to
                             that necessary to perform
                             their assigned duties.
                          • Not using authorized
                             access capabilities to
                             access, view, or obtain
                             information that may be
                             accessible but not
                             necessary to perform their
                             assigned duties.
California Department of Technology                                                  18
Information Security Program Management
SIMM Section 5305-A                                                           April 2026

                            •   Complying with applicable
                                state laws and policies
                                (including copyright and
                                license requirements), as
                                well as any additional
                                security policies and
                                procedures established by
                                the owner of the
                                information and the state
                                entity ISO.
                            •   Notifying the information
                                owner and the state entity
                                ISO of any actual or
                                attempted violations of
                                security policies,
                                practices, and procedures.

The table above is not considered or intended to be an all-inclusive list. Each state
entity must establish additional roles and responsibilities as deemed necessary to
effectively manage risk and implement and manage their state entity’s information
security and privacy programs.

Information Asset Categorization and Classification
The categorization and classification of information assets is a prerequisite for
determining the level of protection needed. Each information asset for which the state
entity has ownership responsibility shall be inventoried and identified to include the
following:

   1. Description and value of the information asset.

   2. Owner of the information asset.

   3. Custodians of the information asset.

   4. Users of the information asset.

   5. Classification of information.

California Department of Technology                                                        19
Information Security Program Management
SIMM Section 5305-A                                                                 April 2026

    6. FIPS Publication199 categorization and level of protection (Low, Moderate, or
        High).

    7. The importance of information assets in executing the state entity’s mission and
        program function.

    8. Potential consequences and impacts if the information asset's confidentiality,
        integrity, and availability were compromised.

Information Classification

Information classification is the characterization of information based on an assessment
of legal and regulatory requirements and the potential impact that a loss of
confidentiality, integrity, or availability of such information would have on organizational
operations, organizational assets, individuals, other organizations, and possibly the
nation.

Subject to executive management review, the program unit that is the designated owner
of the information asset is responsible for determining whether it is to be classified as
public or confidential and whether it contains personal and/or sensitive data. The
information asset owner is responsible for defining special security precautions that
must be followed to ensure the information asset's security (confidentiality, integrity, and
availability).

The state's information assets, including paper and electronic records, automated files,
and databases, are essential public resources that must be given appropriate protection
from unauthorized use, access, disclosure, modification, loss, or deletion. Each state
entity must classify each record, file, and database as either public or confidential using
the following classification structure:

    1. Public Information - information maintained by state agencies that is not exempt
        from disclosure under the provisions of the California Public Records Act (GC
        Sections 7920.000- 7931.000) or other applicable state or federal laws.

    2. Confidential Information - information maintained by state agencies that is
        exempt from disclosure under the provisions of the California Public Records Act

California Department of Technology                                                         20
Information Security Program Management
SIMM Section 5305-A                                                                 April 2026

       (GC Sections 7920.000- 7931.000) or has restrictions on disclosure in
       accordance with other applicable state or federal laws.

Sensitive Information and Personal Information, as defined below, may occur in Public
Information and/or Confidential Information.

   3. Sensitive Information - Information maintained by state entities that requires
       special precautions to protect from unauthorized use, access, disclosure,
       modification, loss, or deletion. Sensitive information may be either public or
       confidential. It is information that requires a higher-than-normal assurance of
       accuracy and completeness. Thus, the key factor for sensitive information is that
       of integrity. Typically, sensitive information includes records of state entity
       financial transactions and regulatory.

   4. Personal Information - information that identifies or describes an individual as
       defined in, but not limited by, the statutes listed below. This information must be
       protected from inappropriate access, use, or disclosure and must be made
       accessible to data subjects upon request. See Civil Code Section 1798.3.

           a. Notice-Triggering Personal Information - specific items or personal
              information (name plus Social Security Number, driver's license/California
              identification card number, financial account number, medical information,
              or health information) that may trigger a requirement to notify individuals if
              it is reasonably believed to have been acquired by an unauthorized
              person. See Civil Code Section 1798.29.

           b. Protected Health Information - individually identifiable information created,
              received, or maintained by such organizations as health care payers,
              health care providers, health plans, and contractors to these entities, in
              electronic or physical form. State laws require special precautions to
              protect from unauthorized use, access, or disclosure. See Confidentiality
              of Medical Information Act, Civil Code Section 56 et seq. and the Patients'
              Access to Health Records Act, Health and Safety Code Sections 123100-
              123149.5.

California Department of Technology                                                          21
Information Security Program Management
SIMM Section 5305-A                                                                  April 2026

           c. Electronic Health Information - individually identifiable health information
              transmitted by electronic media or maintained in electronic media. Federal
              regulations require state entities that are health plans, health care
              clearinghouses, or health care providers that conduct electronic
              transactions to ensure the privacy and security of electronic protected
              health information from unauthorized use, access, or disclosure. See
              Health Insurance Portability and Accountability Act, 45 C.F.R. parts 160
              and 164.

           d. Personal Information for Research Purposes - personal information
              requested by researchers specifically for research purposes. Releases
              may only be made to the University of California or other non-profit
              educational institutions and in accordance with the provisions set forth in
              the law, including the prior review and approval by the Committee for the
              Protection of Human Subjects (CPHS) of the California Health and Human
              Services Agency before such information is released. See Civil Code
              Section 1798.24(t).

Records, files, and databases containing sensitive and/or personal information require
special precautions to prevent inappropriate disclosure. When confidential, personal, or
sensitive information is contained in public records, procedures must be used to protect
it from inappropriate disclosure. Such procedures include removing, redacting, or
otherwise masking the information's confidential, sensitive, or personal portions,
rendering them unrecoverable before a public record is released or disclosed.

While the state entity's need to protect data from inappropriate disclosure is essential,
so is the need for the state entity to take necessary action to preserve the integrity of
the data. Agencies must develop and implement procedures for access, handling, and
maintenance of personal and sensitive information in accordance with the Privacy
Individual Access Standard (SIMM 5310-B).

Once information is classified in accordance with the above-referenced structure, state
entities shall use FIPS Publication 199 to further categorize it based on potential impact,

California Department of Technology                                                          22
Information Security Program Management
SIMM Section 5305-A                                                                   April 2026

as described in the next section, to determine the applicable baseline security controls
to be implemented.

Information System Security Categorization

Each state entity shall use the FIPS Publication 199 to categorize its information
systems and determine the level of protection based on the information system security
categorization process. FIPS Publication 199 defines three levels of potential impact on
organizations or individuals should there be a security breach (i.e., a loss of
confidentiality, integrity, or availability). These are illustrated in the following table.

 Potential        If…                            Examples
 Impact is…
      Low         The loss of confidentiality,   The loss of confidentiality, integrity, or
                  integrity, or availability     availability might: (i) cause a degradation in
                  could have a limited           mission capability to an extent and duration
                  adverse effect on              that the organization can perform its primary
                  organizational operations,     functions, but the effectiveness of the functions
                  assets, or individuals.        is noticeably reduced; (ii) result in minor
                                                 damage to organizational assets; (iii) result in
                                                 minor financial loss; or (iv) result in minor harm
                                                 to individuals.
   Moderate       The loss of confidentiality,   The loss of confidentiality, integrity, or
                  integrity, or availability     availability might (i) cause significant
                  could seriously adversely      degradation in mission capability to an extent
                  affect organizational          and duration that the organization can perform
                  operations, organizational     its primary functions, but the effectiveness of
                  assets, or individuals.        the functions is significantly reduced; (ii) result
                                                 in significant damage to organizational assets;
                                                 (iii) result in significant financial loss; or (iv)
                                                 result in significant harm to individuals, that
                                                 does not involve loss of life or serious life-
                                                 threatening injuries.
     High         The loss of confidentiality,   The loss of confidentiality, integrity, or
                  integrity, or availability     availability might: (i) cause severe degradation

California Department of Technology                                                                    23
Information Security Program Management
SIMM Section 5305-A                                                                             April 2026

 Potential       If…                           Examples
 Impact is…
                 could be expected to have     in or loss of mission capability to an extent and
                 a severe or catastrophic      duration that the organization is not able to
                 adverse effect on             perform one or more of its primary functions; (ii)
                 organizational operations,    result in significant damage to organizational
                 organizational assets, or     assets; (iii) result in major financial loss; or (iv)
                 individuals.                  result in severe or catastrophic harm to
                                               individuals involving loss of life or serious life-
                                               threatening injuries.

Once the state entity completes the categorization process, it will use the appropriate
baseline security controls from NIST Special Publication 800-53.

Critical System Reporting
State entities must include their critical systems in the Technology Recovery Plan (SIMM
5325-A) and conduct a thorough Cal-CSIRS NIST System Assessment. The results of
NIST assessments must be documented in the state entity’s RRPOAM.

Failure to address identified risks may impact audit and risk scores, potentially triggering
the Policy Compliance and Enforcement Policy (SIMM 5330-H) enforcement.
Additionally, it is essential to incorporate all security-related risks from all sources
(internal and external) into the RRPOAM. Examples of risk sources and their relative
findings include, but are not limited to, the following sources:

   •   Internal & External Assessments

   •   Internal & External Audits

   •   Independent Security Assessments

   •   Asset Scanning Vulnerability Reports

   •   Compliance Reviews

California Department of Technology                                                                    24
Information Security Program Management
SIMM Section 5305-A                                                                         April 2026

   •   Self-Assessments

   •   Asset Assessments

Policy, Standards, and Procedures Management
State entities shall implement internal administrative, operational, and technical policies
and procedures to support the information security program's goals, objectives, and
compliance.

Administrative Policies and Procedures

The state entity’s internal administrative policies and procedures shall include, at a
minimum, the following:

   1. Security planning policy and procedures which provide for the effective
       implementation of security controls.

   2. Security awareness and training policy and procedure ensuring a well-trained
       workforce is employed as part of a defense-in-depth strategy to protect
       organizations against various threats targeting or leveraging personnel.

   3. Contingency planning policies and procedures are part of an overall
       organizational program for achieving continuity of operations for
       mission/business functions.

   4. Risk assessment policies and procedures that ensure the state entity is
       effectively managing risk.

   5. System and services acquisition policy and procedures that identify audit events
       that are significant and relevant to the security of information systems and the
       environments in which those systems operate to meet the specific and ongoing
       audit needs.

   6. Security assessment and authorization policy and procedure ensure residual risk
       is identified and accepted as authorized by state entity heads or their designees.

   7. Audit and accountability policy and procedure which identifies the information
       security-related audit review, analysis, and reporting performed by the state
California Department of Technology                                                       25
Information Security Program Management
SIMM Section 5305-A                                                                April 2026

         entity, including, for example, auditing that results from monitoring of account
         usage, remote access, wireless connectivity, mobile device connection,
         configuration settings, system component inventory, use of maintenance tools
         and nonlocal maintenance, physical access, temperature and humidity,
         equipment delivery and removal, communications at the information system
         boundaries, use of mobile code, and use of VoIP.

      8. Acceptable use (rules of behavior) and disclosure policies and procedures that
         clearly delineate appropriate use and the limitations and restrictions associated
         with the use of state entity-owned information assets, including:

            a. Display of system use notification message or security banner.

            b. Email use, retention, forward and auto-response agents, and etiquette.

            c. Internet use, browsing, downloads, and etiquette

            d. Social media technologies, when approved by the state entity, are properly
                monitored and managed, and their use is in compliance with the Social
                Media Standard (SIMM 66B).

Operational and Technical Policies and Procedures

The state entity’s internal operational and technical policies and procedures shall
include, at a minimum, the following:

 1.       Access control policy and procedure, which ensures the identification of
          authorized users and the specification of access privileges.

 2.       Identification and authentication policy and procedures for identifying and
          authenticating state entity users and devices.

 3.       Technology upgrade policy and procedures, which include, but are not limited
          to, timely operating system upgrades on servers, routers, and firewalls. The
          policy and procedures must address appropriate planning and testing of
          upgrades and state entity criteria for deciding which upgrades to apply.

California Department of Technology                                                          26
Information Security Program Management
SIMM Section 5305-A                                                                  April 2026

 4.     Security patches and security upgrade policies and procedures include but are
        not limited to, servers, routers, desktop computers, mobile devices, and
        firewalls. The policy and procedures must address the application and testing of
        the patches and/or security upgrades, in addition to departmental criteria for
        deciding which patches and security upgrades must be applied and how quickly.

 5.     Firewall configuration policy and procedures must require the creation and
        documentation of a baseline configuration for each firewall, updates of the
        documentation for all authorized changes, and periodic verification of the
        configuration to ensure that it has not changed during software modifications or
        equipment reboots.

 6.     Server configuration policy and procedures must address all servers that
        interact with Internet, extranet, or intranet traffic. The policy and procedures
        must require creating and documenting a baseline configuration for each server,
        updating the documentation for all authorized changes, and periodic checking of
        the configuration to ensure that it has not changed during software
        modifications or equipment rebooting.

 7.     Server hardening policy and procedures must cover all servers within the
        department, not only those that fall within the jurisdiction of the department's IT
        area. The policy and procedures must include the process for making changes
        based on newly published vulnerability information as it becomes available.
        Further, the policy and procedures must address and be consistent with the
        department's policy for making security upgrades and security patches.

 8.     Software management and licensing policy and procedures must address
        acquisition from reliable and safe sources, identification and maintenance of an
        inventory of software approved for use on state entity systems, and clearly state
        the department's policy about not using pirated or unlicensed software and the
        consequences for doing so.

 9.     Peer-to-peer technology policy and procedures must indicate that peer-to-peer
        technology use for any non-business purpose is strictly prohibited. This includes

California Department of Technology                                                        27
Information Security Program Management
SIMM Section 5305-A                                                                 April 2026

        but is not limited to, the transfer of music, movies, software, and other
        intellectual property. The CIO and ISO must approve the business use of peer-
        to-peer technologies.

 10.    All personal, sensitive, or confidential information stored on portable electronic
        storage media (such as CDs, DVDs, tapes, portable hard drives, and thumb
        drives) and on portable computing devices (including laptops, netbooks, tablets,
        and smartphones) must adhere to encryption policies and procedures. This
        means that encryption or approved alternative security controls are required.
        Any alternatives to encryption must be assessed individually and must receive
        written approval from the state entity’s Chief Information Officer (CIO) and
        Information Security Officer (ISO) after a thorough risk assessment.

 11.    Remote access policy and procedures requiring remote access or telework
        arrangements to adhere to the Telework and Remote Access Security Standard
        (SIMM 5360-A).

 12.    Data download policy and procedures require that if a data file is downloaded to
        a mobile device or desktop computer from another computer system, the
        specifications for information integrity and security established for the original
        data file must be applied in the new environment.

 13.    System and communications protection policy and procedures.

 14.    Incident response policy and procedures, which must align with Incident
        Reporting and Response Instructions (SIMM 5340-A) and Requirements to
        Respond to Incidents Involving a Breach of Personal Information (SIMM 5340-
        C)

 15.    Media protection policy and procedures that address media access, marking,
        storage, and transport security.

 16.    Physical and environmental protection policy and procedures that outline the
        state entity’s facility access and environmental protection controls.

 17.    Data destruction policy and procedures.

California Department of Technology                                                          28
Information Security Program Management
SIMM Section 5305-A                                                                 April 2026

Questions
Questions regarding the implementation of this standard may be sent to:

California Department of Technology
Office of Information Security
security@state.ca.gov

California Department of Technology                                              29
Information Security Program Management
SIMM Section 5305-A                                                       April 2026

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
