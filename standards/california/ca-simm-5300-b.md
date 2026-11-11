---
schema_version: 1
corpus: states-it-governance
jurisdiction: california
id: ca-simm-5300-b
title: Foundational Framework
doc_type: standard
citation: SIMM 5300-B
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5300-B-Foundational-Framework.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 81acfe203cd4de32cea70fc124ad9ea0714e9557f76a86a964e1060265c1dda8
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Foundational Framework (SIMM 5300-B)

## At a glance

SIMM 5300-B, Foundational Framework: an item of the Office of Information Security's information security series (SIMM 5300), the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

       State of California
  Office of Information Security

Foundational Framework
          SIMM 5300-B
           October 2017

                                           REVISION HISTORY

   REVISION          DATE OF RELEASE                  OWNER            SUMMARY OF CHANGES
 Initial Release      November 2017            Office of Information          New
                                                     Security

California Department of Technology,Office of Information Security
Foundational Framework
SIMM 5300-B                                                                        October 2017

                                                          TABLE OF CONTENTS

 I.    INTRODUCTION ....................................................................................................................... 1

 II.   FOUNDATIONAL FRAMEWORK ............................................................................................ 2-17

            A. Application Security ............................................................................................................2

            B. Contingency Planning ........................................................................................................3

            C. Change and Configuration Management ..........................................................................4

            D. Data Security .................................................................................................................. 5-6

            E. Security Governance ...................................................................................................... 7-9

            F. Endpoint Security ............................................................................................................ 10

            G. Identity and Access Management ................................................................................... 11

            H. Mobile Security ................................................................................................................ 12

            I.   Security Analytics and Continuous Monitoring ............................................................... 13

            J. Network Security ............................................................................................................. 14

            K. Physical Security ..................................................................................................... 15

            L.    Vulnerability Management ......................................................................................... 16-17

California Department of Technology,Office of Information Security
Foundational Framework
SIMM 5300-B                                                                                                                            October 2017

 I. INTRODUCTION

     The Department of Technology, Office of Information Security has established this foundational
     framework comprised of 30 priority security objectives to assist state entities with prioritization
     of their information security efforts. The foundational framework is considered a starting point
     and will be used to consistently measure and mature state entity security compliance moving
     forward.

     As state entities achieve compliance with foundational framework objectives they will continue
     to address other applicable control areas to sufficiently protect information assets and address
     organizational risk.

Office of Information Security                                                                    Page | 1
Foundational Framework
SIMM 5300-B                                                                                October 2017

                                                                                                                                                    SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                               SAM 5300
                                                                                           2016‐2018 PRIORITY
Security Program Framework                                                                                                          NIST                                            TARGET STATE                                               REFERENCE                                     NIST 800‐53 REFERENCE
                                                                                               OBJECTIVES
                                                      GOALS                                                                    CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                                       FUNCTION                                                Like]                                                  [DEPLOY                                  (Control Family, Number, Name)
                                                                                         [MANAGE at This Level]
                                                                                                                                                                                                                                              at This Level]
                                                                                                                                                Formally defined, documented, and centrally managed software inventory
                                                                                                                                                management process, mandated by policy with senior management oversight, with
                                                                                                                                                regular and periodic review and update of inventory contents.
                                                                                    Application Inventory Management:
                                                                                                                                                                                                                                        5305.5 Information Asset
                                                                                                                                                Use of automated tools for software discovery and inventory content maintenance         Management
                                                                                    Develop a formal, comprehensive                             with owner and stakeholder input.
                                                                                       software application inventory                                                                                                                                                Configuration Management:
                                                                                                                                                                                                                                        5315.3 Information Asset
                                                                                 management process that includes regular          Identify     Inventory contents include associated software characteristics include owners,                                       CM‐8 INFORMATION SYSTEM COMPONENT INVENTORY
                                                                                                                                                                                                                                        Documentation
                                                                                  and periodic reviews, management and                          assurance and protection requirements, sensitive data stored or processed,                                           PM‐5 INFORMATION ASSET INVENTORY
                                                                                      stakeholder input and approval,                           infrastructure requirements, aging and skill set requirements.                          5315.7 Software Usage
                                                                                     integration with enterprise asset
                                                                                                                                                                                                                                        Restrictions
                                                                                          management processes
                                                                                                                                                Approach and applicability of the enterprise software inventory and contents is
                                                                                                                                                enhanced and enforced through a regular and periodic program of review, audit, and
                                                                                                                                                update.

                                                                                                                                                Application assurance levels have been formally defined, documented and governed
                                                                                                                                                through enterprise application development policy with senior management
                                                                                                                                                oversight.

                                                                                                                                                All applications are regularly and periodically assessed.
                                         Establish security controls for the               Application Assurance                                                                                                                        5315 Information Security
                                       development, acquisition, and use of                   Level Definition:                                 Threats, vulnerabilities, and consequences are used to identify the security            Integration
                                                                                                                                                                                                                                                                     System and Services Acquisition:
     APPLICATION SECURITY                  software applications that are                                                                       requirements of the application in terms of business requirements.                                                   SA‐8 SECURITY ENGINEERING PRINCIPLES
                                   commensurate with the defined security risk   Define application   assurance levels based       Identify                                                                                             5315.2 SDLC
                                                                                                                                                                                                                                                                     SA‐11 DEVELOPER SECURITY TESTING AND EVALUATION
                                   for use and operations of those applications.   on criticality to business mission and
                                                                                 sensitivity of data, as well as operational                    Assurance ratings are maintained as part of application inventory management            5315.1 System and Services
                                                                                             threat environment                                 process, and used to define appropriate secure coding and testing methodologies.        Acquisition

                                                                                                                                                Assurance definitions and assignments are enhanced and enforced through a regular
                                                                                                                                                and periodic program of review, audit, and update.

                                                                                                                                                Secure coding practices (software development and programming methods,
                                                                                                                                                techniques and standards) are formally defined, documented and governed through
                                                                                           Secure Code Practices:                               enterprise application development policy with senior management oversight.

                                                                                        Establish and deploy software
                                                                                  development and programming methods,                          Practices are defined, documented, integrated, and enforced across all system                                        System and Services Acquisition:
                                                                                  techniques and standards (secure coding                       development environments.                                                                                            SA‐17 DEVELOPER SECURITY ARCHITECTURE AND DESIGN
                                                                                                                                   Protect                                                                                              5315 SDLC
                                                                                        practices) used specifically for                                                                                                                                             CM‐7 LEAST FUNCTIONALITY
                                                                                    implementing software in a way that                         App developers are regularly and periodically trained and secure coding practices for                                SI‐10 INFORMATION INPUT VALIDATION
                                                                                     prevents, avoids, or does not create                       applicable system development environments.
                                                                                    security vulnerability in the resulting
                                                                                                  application                                   Practices are enhanced and enforced through a regular and periodic program of
                                                                                                                                                review, audit, and update.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                               2
SIMM 5300‐B                                                                                                                                                                                                                                                                                                               October 2017

                                                                                                                                             SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                SAM 5300
                                                                                            2016‐2018 PRIORITY
Security Program Framework                                                                                                           NIST                                             TARGET STATE                                              REFERENCE                                     NIST 800‐53 REFERENCE
                                                                                                OBJECTIVES
                                                      GOALS                                                                     CYBER SECURITY                                                                     [What Good Looks
    [REPORT at this level]                                                                                                        FUNCTION                                                  Like]                                                [DEPLOY                                 (Control Family, Number, Name)
                                                                                         [MANAGE at This Level]
                                                                                                                                                                                                                                               at This Level]
                                                                                                                                                 Enterprise Business Impact Analysis (BIA) is conducted regularly and periodically
                                                                                                                                                 resulting in realistic Recovery Time Objectives (RTO) and Recovery Point Objectives
                                                                                                                                                 (RPO) for all critical systems and supporting IT infrastructure.

                                                                                                                                                                                                                                        5325 Business Continuity with
                                                                                         Business Impact Assessment:
                                                                                                                                                 Recovery objectives are commensurate with assigned assurance‐level of each             Technology Recovery
                                                                                    Develop and vet an enterprise Business                       application and aligned with service recovery objectives established in the enterprise
                                                                                                                                                 Business Continuity Plan (BCP).                                                        5325.1 Technology Recovery Contingency Planning:
                                                                                      Impact Analysis (BIA) with realistic
                                                                                                                                                                                                                                        Plan                          CP‐2 CONTINGENCY PLAN
                                                                                     Recovery Time Objectives (RTO) and
                                                                                                                                   Recover                                                                                                                            CP‐4 CONTINGENCY PLAN TESTING
                                                                                       Recovery Point Objectives (RPO)
                                                                                                                                                 Service recovery objectives are reviewed and approved by key business process          5325.4 Alternate Storage and CP‐6 ALTERNATE STORAGE SITE
                                                                                    commensurate with assurance‐level of
                                                                                                                                                 stakeholders.                                                                          Processing Site               CP‐7 ALTERNATE PROCESSING SITE
                                                                                   each application and aligned with service
                                                                                      recovery objectives established in
                                                                                                                                                 BIA is reviewed and updated at least annually with a complete refresh at least every    5325.5 Telecommunications
                                                                                   enterprise Business Continuity Plan (BCP)
                                    Deploy controls to prevent unauthorized or                                                                   three years.                                                                            Services
                                    unacceptable loss of customer, critical, and
                                                                                                                                                 Disaster recovery testing results are used as feedback to periodically enhance BIA‐
                                     sensitive information. In keeping with a
    CONTINGENCY PLANNING                                                                                                                         based recovery objectives between BIA refresh cycles.
                                     systematic and comprehensive security
                                       program, deploy controls to protect
                                                                                                                                                 Disaster Recovery (DR)/Business Continuity (BC) testing is conducted as part of a
                                             information availability.
                                                                                                                                                 formal, documented plan integrated with the regular and periodic review of the
                                                                                                                                                 DR/BC plans.

                                                                                                                                                 Testing is structured as a tiered testing program that includes table‐top scenario‐     5325.1 Technology Recovery
                                                                                         Comprehensive DRP Testing:                              based and live partial (function, infrastructure, system or application‐specific)       Plan
                                                                                                                                                                                                                                                                    Contingency Planning:
                                                                                                                                                 recovery testing, as well as live, full failover and recovery testing for all systems                              CP‐2 CONTINGENCY PLAN
                                                                                     Existing disaster recovery processes to                     supporting critical business processes.                                                 5325.3 Technology Recovery
                                                                                                                                   Recover                                                                                                                          CP‐3 CONTINGENCY TRAINING
                                                                                    include periodic live testing of recovery                                                                                                            Testing
                                                                                                                                                                                                                                                                    CP‐4 CONTINGENCY PLAN TESTING
                                                                                   capabilities and incorporating feedback to                    Test results are used as feedback to the plan review process and incorporated as
                                                                                                                                                                                                                                                                    CP‐9 INFORMATION SYSTEM BACKUP
                                                                                               refine the processes                              refinements to the plan.                                                                5325.6 Information System
                                                                                                                                                                                                                                         Backups
                                                                                                                                                 Testing occurs at least annually.

                                                                                                                                                 Full, live testing occurs at least every three years.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                               3
SIMM 5300‐B                                                                                                                                                                                                                                                                                                               October 2017

                                                                                                                                        SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                            SAM 5300
                                                                                     2016‐2018 PRIORITY
Security Program Framework                                                                                                    NIST                                            TARGET STATE                                                  REFERENCE                                    NIST 800‐53 REFERENCE
                                                                                         OBJECTIVES
                                                      GOALS                                                              CYBER SECURITY                                                                    [What Good Looks
    [REPORT at this level]                                                                                                 FUNCTION                                                Like]                                                      [DEPLOY                                (Control Family, Number, Name)
                                                                                  [MANAGE at This Level]
                                                                                                                                                                                                                                            at This Level]
                                                                                                                                           Practices are formally defined and governed by enterprise policy with senior
                                                                                                                                           management oversight.

                                                                                                                                           Enterprise policy is comprehensively applied across the enterprise; mandates the
                                                                                                                                           maintenance of an enterprise change management processes; and defines the assets
                                                                                                                                           to be managed via the process; outlines specific management and administration
                                                                                                                                           responsibilities including change advisory board (CAB) and formal security change
                                                                                  Comprehensive Enterprise                                 impact evaluations.
                                                                                 Change Management Process,
                                                                                   Workflow, and Database:
                                                                                                                                           Implementation includes the use of automation for workflow, cataloging, tracking,         5315.5 Configuration
                                                                                                                                                                                                                                                                 Configuration Management:
                                                                              Establish organization‐wide change                           and reporting.                                                                            Management
                                                                                                                                                                                                                                                                 CM‐3 CONFIGURATION CHANGE CONTROL
                                                                            management (CM) process and standards            Identify
                                                                                                                                                                                                                                                                 CM‐4 SECURITY IMPACT ANALYSIS
                                                                               applicable to all IT and information                                                                                                                  5315 Information Security
                                                                                                                                                                                                                                                                 CM‐5 ACCESS RESTRICTIONS FOR CHANGE
                                                                            (hardware, software, infrastructure, and                       Monitoring and reporting processes are defined and established to ensure policy
                                                                                                                                                                                                                                     Integration
                                                                              data); support change management                             adherence.
                                Establish change and configuration
                                                                            process with single automated workflow
                               management controls that include a
                                                                              tool and central CM data repository                          Integrated with enterprise configuration and asset management processes.
                              workflow model with documentation,
                           attribution, approval processes, testing, and
 CHANGE AND CONFIGURATION
                              execution of the change. Additionally,
      MANAGEMENT                                                                                                                           Approach and applicability of the change management policy is enhanced and
                          establish controls to protect the integrity and
                                                                                                                                           enforced through a regular and periodic program of review, audit, and approach
                            confidentiality of the change management
                                                                                                                                           update.
                               process commensurate with level of
                            criticality of the resources being changed.
                                                                                                                                           Practices are formally defined and governed by enterprise policy with senior
                                                                                                                                           management oversight.

                                                                                                                                           Enterprise policy is comprehensively applied across the enterprise; mandates the
                                                                                                                                           maintenance of an enterprise change management process that includes formal
                                                                              Embed Formal Security Evaluations                            security change impact evaluations to qualify the level of alteration to the enterprise
                                                                                 in Enterprise CM Process:                                 security posture resulting from the proposed change; defines the threshold criteria
                                                                                                                                           for identifying types of changes subject to security impact evaluations; outlines                                     Configuration Management:
                                                                                                                             Detect
                                                                                 Integrate formal security impact                          specific management and administration responsibilities including actions and                                         CM‐4 SECURITY IMPACT ANALYSIS
                                                                            evaluation and approval in enterprise risk                     authority of change advisory board (CAB) to stop, suspend, or approve changes based
                                                                               management processes and panels                             on results of security impact evaluation.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                           4
SIMM 5300‐B                                                                                                                                                                                                                                                                                                           October 2017

                                                                                                                                                SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                   SAM 5300
                                                                                            2016‐2018 PRIORITY
Security Program Framework                                                                                                            NIST                                            TARGET STATE                                                 REFERENCE                                          NIST 800‐53 REFERENCE
                                                                                                OBJECTIVES
                                                      GOALS                                                                      CYBER SECURITY                                                                    [What Good Looks
    [REPORT at this level]                                                                                                         FUNCTION                                                Like]                                                    [DEPLOY                                      (Control Family, Number, Name)
                                                                                         [MANAGE at This Level]
                                                                                                                                                                                                                                                  at This Level]

                                                                                                                                                   Business data use cases and practices are formally defined and governed by
                                                                                                                                                   enterprise policy with senior management oversight.
                                                                                                                                                                                                                                            5305.5 Information Asset
                                                                                                                                                   Enterprise policy defines practices for data classification that includes identification Management
                                                                                                                                                   and definition of data and information types used, processed, and stored throughout
                                                                                                                                                   the enterprise in alignment with business processes.                                     5310.1 State Entity Privacy
                                                                                                                                                                                                                                            Statement And Notice On
                                                                                                                                                                                                                                            Collection
                                                                                                                                                   Authorized use case guidelines are provided for data‐at‐rest, in‐motion, and in‐use, as
                                                                                                                                                   well as required standards for protection per use case.
                                                                                                                                                                                                                                            5310.2 Limiting Collection

                                                                                                                                                   Use case requirements include data exchange, retention, and destruction, as well as     5310.3 Limiting Use And
                                                                                          Data Classification Policy                               hardcopy and mobile media applicability.                                                Disclosure
                                                                                             and Enforcement:                                                                                                                                                             Awareness and Training Risk Assessment:
                                                                                                                                                   Training on appropriate use is included in regular and periodic security awareness      5310.4 Individual Access to    RA‐2 SECURITY CATEGORIZATION
                                                                                   Establish enterprise policy and practices                       program.                                                                                Personnel Information
                                                                                      for data classification that includes          Identify                                                                                                                           System and Communications Protection:
                                                                                   identification and definition of data and                       Monitoring and reporting processes are defined and established to ensure policy         5310.5 Information Integrity SC‐8 TRANSMISSION CONFIDENTIALITY AND INTEGRITY
                                                                                   information types used, processed, and                          adherence.                                                                                                           SC‐13 CRYPTOGRAPHIC PROTECTION
                                                                                     stored throughout the enterprise in                                                                                                                   5310.6 Data Retention and SC‐28 PROTECTION OF INFORMATION AT REST
                                                                                      alignment with business processes                            Approach and applicability of the enterprise data classification policy is enhanced and Destruction
                                                                                                                                                   enforced through a regular and periodic program of review, audit, and approach
                                                                                                                                                   update.                                                                                 5310.7 Security Safeguards

                                                                                                                                                                                                                                           5320 Training and Awareness
                                                                                                                                                                                                                                           for Information Security and
                                                                                                                                                                                                                                           Privacy

                                                                                                                                                                                                                                           5365.2 Media Protection

                                   Deploy governance processes and protection                                                                                                                                                              5365.3 Media Disposal
                                        controls to prevent unauthorized or
                                      inappropriate access to or disclosure of
                                    private or sensitive information. In keeping
                                       with a systematic and comprehensive                                                                         Enterprise privacy policy is defined with senior management accountability. Appoints
         DATA SECURITY
                                   security program, deploy controls to protect                                                                    a Chief Privacy Officer (CPO) or Privacy Coordinator (PC) responsible for the
                                     information confidentiality in addition to                                                                    development, implementation, maintenance of a privacy program to protect
                                    controls for other major security objectives                                                                   individual privacy and to ensure the compliance with applicable laws and regulations
                                     as they relate to comprehensive data and                                                                      regarding the collection, use, maintenance, sharing and disposal of personally
                                              information protection.                                                                                                                                                                                                   Accountability, Audit, and Risk Management:
                                                                                                                                                   information by programs and information systems.                                                                     AR‐1 GOVERNANCE AND PRIVACY PROGRAM
                                                                                                                                                                                                                                                                        AR‐2 PRIVACY IMPACT AND ASSESSMENT
                                                                                                                                                   Policy is defined to support achievement of privacy objectives commensurate with                                     AR‐3 PRIVACY REQUIREMENTS FOR CONTRACTORS AND SERVICE PROVIDERS
                                                                                                                                                   business objectives.                                                                                                 AR‐4 PRIVACY MONITORING AND AUDITING
                                                                                                                                                                                                                                                                        AR‐6 PRIVACY REPORTING
                                                                                                                                                   Policies are regularly and periodically reviewed and updated for alignment with                                      AR‐7 PRIVACY ENHANCED SYSTEM DESIGN AND DEVELOPMENT
                                                                                                                                                   current prevailing industry practices and applicable threats.                           5305.2 Policy, Procedure and AR‐8 ACCOUNTING OF DISCLOSURES
                                                                                            Data Privacy Program                                                                                                                           Standards Management
                                                                                             and Enforcement:                                      Policies and any updates are regularly and periodically communicated to personnel                                    Risk Assessment:
                                                                                                                                                                                                                                           5305.6 Risk Management       RA‐1 RISK ASSESSMENT POLICY AND PROCEDURES
                                                                                                                                                   with respect to applicability and enforcement.
                                                                                    Establish an enterprise policy and direct
                                                                                   the development and maintenance of an                           Policy is supported by comprehensive, set of defined policy implementation standards 5305.7 Risk Assessment            Program Management:
                                                                                      organizational Privacy Program that                          and guidelines, as well as requirements for minimum baseline policy enforcement                                        PM‐9 RISK MANAGEMENT STRATEGY
                                                                                                                                     Protect
                                                                                   defines the overall Privacy Program as it                       across all aspects of the architecture and business processes.                       5310.1 State Entity Privacy
                                                                                     explicitly describes the applicability of                                                                                                          Statement and Notice on           Authority and Purpose:
                                                                                      privacy policy to enterprise business                                                                                                             Collection                        AP‐1 AUTHORITY TO COLLECT
                                                                                     processes and ensures the compliance                          Privacy policy definition, applicability, and enforcement is enhanced and validated                                    AP‐2 PURPOSE SPECIFICATION
                                                                                   with the California Information Practices                       through a program of regular and periodic review, maintenance, update, monitoring 5310.2 Limiting Collection
                                                                                                       Act.                                        and audit.
                                                                                                                                                                                                                                                             5310.3       Data Minimization and Retention:
                                                                                                                                                   All public websites contain a Privacy Policy Statement. All online and hard copy forms Limiting Use and Disclosure     DI‐1 MINIMIZATION OF PERSONALLY IDENTIFIABLE INFORMATION
                                                                                                                                                   that collect personal information contain a Notice on Collection.
                                                                                                                                                                                                                                          5310.4 Individual Access        Individual Participation and Redress:
                                                                                                                                                                                                                                                                          IP‐1 CONSENT
                                                                                                                                                                                                                                           5310.5 Information Integrity
                                                                                                                                                                                                                                                                          Transparency:
                                                                                                                                                                                                                                           5310.6 Data Retention and      TR‐1 PRIVACY NOTICE
                                                                                                                                                                                                                                           Destruction

                                                                                                                                                                                                                                           5315.3 Information Asset
                                                                                                                                                                                                                                           Documentation
                                                                                                                                                   Comprehensive privacy risk assessment strategy is formally defined and governed by
                                                                                                                                                                                                                                      5330.1 Security Assessments
                                                                                                                                                   the enterprise privacy policy with senior management oversight.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                                          5
SIMM 5300‐B                                                                                                                                                                                                                                                                                                                          October 2017

                                                                                                                                    SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                     SAM 5300
                                                                               2016‐2018 PRIORITY
Security Program Framework                                                                                                 NIST                                           TARGET STATE                                               REFERENCE                                    NIST 800‐53 REFERENCE
                                                                                   OBJECTIVES
                                                      GOALS                                                           CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                              FUNCTION                                                Like]                                                 [DEPLOY                                 (Control Family, Number, Name)
                                                                             [MANAGE at This Level]
                                                                                                                                                                                                                                    at This Level]
                                                                                                                                       Policy identifies privacy‐specific management and administrative roles and
                                                                                                                                       responsibilities including applicability to vendors and contractors.

                                                                                                                                       Regular and periodic assessment of privacy‐related risk and formal acceptance of
                                                                                                                                       residual risk by accountable organization management for programs, systems and
                                                                                                                                       technologies and including existing and new through informal and formal project
                                                                                                                                       management processes include Privacy Threshold Assessments (PTA) and Privacy
                                                                                                                                       Impact Assessments (PIA).

                                                                                                                                       The assessment process is based on an industry‐accepted leading practice privacy
                                                                                                                                       framework and includes criteria for qualifying risk commensurate with the business
                                                                                                                                       mission of the organization.

                                                                                                                          Protect      Process addresses residual risk in all aspects of the enterprise including
                                                                                                                                       telecommunications perimeter, major systems and applications, infrastructure,
                                                                                                                                       resources and data, governance, and procurement/acquisition.

                                                                                                                                       The process is enforced through a program of regular and periodic monitoring and
                                                                                                                                       testing to validate assessment findings, with resulting metrics used to provide input to
                                                                                                                                       residual risk acceptance process.

                                                                                                                                       Privacy program is periodically supplemented by privacy assessments conducted by
   DATA SECURITY, (CONT'D).                                                                                                            independent third‐parties.

                                                                                                                                       Privacy assessment results are provided as input into overall enterprise risk and
                                                                                                                                       compliance management processes.

                                                                                                                                       Privacy assessment processes are enhanced and validated through a program of
                                                                                                                                       regular and periodic review, maintenance, update, and audit.

                                                                                                                                       Data‐at‐rest protection practices are defined and governed in accordance with the
                                                                                                                                       enterprise information classification policy requirements for sensitive data.

                                                                               Protecting Confidential                                 Appropriate, current‐state technological protection, such as encryption, masking and
                                                                                 and Sensitive Data:                                   obfuscation, or tokenization, are employed on all enterprise and organization‐specific                              Media Protection:
                                                                                                                                       electronic media and devices with the capability to store information.                 5310.7 Security Safeguards
                                                                                                                                                                                                                                                           MP‐5 MEDIA TRANSPORT
                                                                       Employ encryption technology to protect
                                                                                                                                                                                                                            5350.1 Encryption
                                                                       sensitive data‐at‐rest, in accordance with                                                                                                                                          System and Communications Protection:
                                                                                                                                       Encryption strength (key and algorithm) is commensurate with assurance‐level
                                                                      the enterprise data classification policy, in       Protect                                                                                                                          SC‐12 CRYPTOGRAPHIC KEY ESTABLISHMENT AND MANAGEMENT
                                                                                                                                       requirements of the devices and media, as well as use cases in which the devices and 5365.2 Media Protection
                                                                        all enterprise and organization‐specific                                                                                                                                           SC‐17 PUBLIC KEY INFRASTRUCTURE CERTIFICATES
                                                                                                                                       media are used.
                                                                       structured data repositories that contain                                                                                                                                           SC‐28 PROTECTION OF INFORMATION AT REST
                                                                                                                                                                                                                            5350 Operational Security
                                                                      sensitive information including databases                                                                                                                                            SC‐8 TRANSMISSION CONFIDENTIALITY AND INTEGRITY
                                                                                                                                       Encryption approach(es) are supplemented with sufficient encryption key
                                                                         and enterprise content management                                                                                                                                                 SC‐13 CRYPTOGRAPHIC PROTECTION
                                                                                                                                       management processes to ensure protected and managed data recovery for loss, mis‐
                                                                                        systems
                                                                                                                                       configuration, or forensic investigation.

                                                                                                                                       Data‐at‐rest protection practices are enhanced and enforced through a regular and
                                                                                                                                       periodic program of review, audit, testing, and update.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                       6
SIMM 5300‐B                                                                                                                                                                                                                                                                                                       October 2017

                                                                                                                                               SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                 SAM 5300
                                                                                           2016‐2018 PRIORITY
Security Program Framework                                                                                                            NIST                                           TARGET STATE                                                REFERENCE                                     NIST 800‐53 REFERENCE
                                                                                               OBJECTIVES
                                                      GOALS                                                                      CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                                         FUNCTION                                               Like]                                                   [DEPLOY                                 (Control Family, Number, Name)
                                                                                         [MANAGE at This Level]
                                                                                                                                                                                                                                                at This Level]
                                                                                                                                                  Regular and periodic security awareness training is mandated by enterprise security
                                                                                                                                                  policy with senior management oversight.

                                                                                                                                                  Awareness training is mandatory for all enterprise personnel, as well as all vendors,
                                                                                                                                                  suppliers, and providers which make use of or operate IT resources and information
                                                                                                                                                  on behalf of the organization.
                                                                                                                                                                                                                                          5305.4 Personnel
                                                                                                                                                  Training compliance is formally tracked, managed, and reported, and enforced            Management
                                                                                                                                                  through suspension of access to IT assets required for job function.
                                                                                                                                                                                                                                        5320 Training And
                                                                                                                                                                                                                                        Awareness For Information     Awareness and Training:
                                                                                        Awareness Training Program:
                                                                                                                                                  Training content includes awareness of security policy applicability and enforcement, Security And Privacy          AT‐1 SECURITY AWARENESS POLICY AND PROCEDURES
                                                                                                                                                  applicable threats, and reporting.                                                                                  AT‐2 SECURITY AWARENESS TRAINING
                                                                                    Establish a comprehensive enterprise
                                                                                                                                                                                                                                        5320.1 Security And Privacy   AT‐3 ROLE‐BASED SECURITY TRAINING
                                                                                    security awareness and training policy
                                                                                                                                    Respond       Training content is regularly and periodically updated to maintain currency with      Awareness                     AT‐4 TRAINING RECORDS
                                                                                  with requirements for regular and periodic
                                                                                                                                                  prevailing events.
                                                                                  (annual) awareness training for all users of
                                                                                                                                                                                                                                        5320.2 Security And Privacy   Security Planning:
                                                                                      IT operated by or on behalf of the
                                                                                                                                                  Training program is multi‐faceted to include formal training, mass communications, Training                         PL‐4 RULES OF BEHAVIOR
                                                                                                  enterprise
                                                                                                                                                  and topic‐specific messaging.
                                                                                                                                                                                                                                        5320.3 Security And Privacy
                                                                                                                                                  Training program includes role‐specific training for audiences from at least the      Training Records
                                                                                                                                                  general‐user, technical, and management perspectives.
                                                                                                                                                                                                                                        5320.4 Personnel Security
                                                                                                                                                  Metrics exist to measure success of awareness program as it relates to improved
                                                                                                                                                  security and decreased risk.

                                                                                                                                                  Security awareness training program is enhanced through a program of regular and
                                                                                                                                                  periodic review, maintenance, update, and audit.

                                     Establish a high‐level enterprise Security
                                                                                                                                                  Enterprise security policy is defined with senior management accountability.                                   Access Control:
                                    Governance process led by an information
                                                                                                                                                                                                                                                                 AC‐1 ACCESS CONTROL POLICY AND PROCEDURES
                                    security officer (ISO) who is empowered to
                                                                                                                                                                                                                                                                 Awareness and Training:
     SECURITY GOVERNANCE            protect enterprise IT assets while removing
                                                                                                                                                                                                                                                                 AT‐1 SECURITY AWARENESS AND TRAINING POLICY AND PROCEDURES
                                     the barriers to productivity through well‐
                                                                                                                                                                                                                                                                 Audit and Accountability:
                                      understood management processes and
                                                                                                                                                                                                                                                                 AU‐1 AUDIT AND ACCOUNTABILITY POLICY AND PROCEDURES
                                               governance principles.
                                                                                                                                                                                                                                                                 Security Assessment and Authorization:
                                                                                                                                                                                                                                                                 CA‐1 SECURITY ASSESSMENT AND AUTHORIZATION POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 Configuration Management:
                                                                                                                                                                                                                                                                 CM‐1 CONFIGURATION MANAGEMENT POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 Contingency Planning:
                                                                                                                                                  Policy is defined to support achievement of security objectives commensurate with                              CP‐1 CONTINGENCY PLANNING POLICY AND PROCEDURES
                                                                                                                                                  business objectives.                                                                                           Identification and Authentication:
                                                                                           Comprehensive Security                                                                                                                                                IA‐1 IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES
                                                                                              Policy Structure:                                   Policy is regularly and periodically reviewed and updated for alignment with current                           Incident Response:
                                                                                                                                                  prevailing industry practices and applicable threats.                                5305 Information Security
                                                                                                                                                                                                                                                                 IR‐1 INCIDENT RESPONSE POLICY AND PROCEDURES
                                                                                                                                                                                                                                       Program
                                                                                     Formally establish and document a                                                                                                                                           Maintenance:
                                                                                                                                     Protect      Policy updates are regularly and periodically communicated to personnel with respect
                                                                                  consolidated, comprehensive enterprise‐                                                                                                                                        MA‐1 SYSTEM MAINTENANCE POLICY AND PROCEDURES
                                                                                                                                                  to applicability and enforcement.                                                    5305.2 Policy, Procedures
                                                                                     specific security governance policy                                                                                                                                         Media Protection:
                                                                                                                                                                                                                                       and Standards Management
                                                                                       structure that includes policy,                                                                                                                                           MP‐1 MEDIA PROTECTION POLICY AND PROCEDURES
                                                                                                                                                  Policy is supported by comprehensive, set of defined policy implementation standards
                                                                                  requirements, and supporting standards                                                                                                                                         Physical and Environmental Protection:
                                                                                                                                                  and guidelines, as well as requirements for minimum baseline policy enforcement
                                                                                                                                                                                                                                                                 PE‐1 PHYSICAL AND ENVIRONMENTAL PROTECTION POLICY AND PROCEDURES
                                                                                                                                                  across all aspects of the security architecture and all business processes.
                                                                                                                                                                                                                                                                 Planning:
                                                                                                                                                                                                                                                                 PL‐1 SECURITY PLANNING POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 Personnel Security:
                                                                                                                                                                                                                                                                 PS‐1 PERSONNEL SECURITY POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 Risk Assessment:
                                                                                                                                                                                                                                                                 RA‐1 RISK ASSESSMENT POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 System and Services Acquisition:
                                                                                                                                                                                                                                                                 SA‐1 SYSTEM AND SERVICES ACQUISITION POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 System and Communications Protection:
                                                                                                                                                                                                                                                                 SC‐1 SYSTEM AND COMMUNICATIONS PROTECTION POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                 System and Information Integrity:
                                                                                                                                                                                                                                                                 SI‐1 SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                                7
SIMM 5300‐B                                                                                                                                                                                                                                                                                                                October 2017

                                                                                                                                     SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                           SAM 5300
                                                                                2016‐2018 PRIORITY
Security Program Framework                                                                                                 NIST                                             TARGET STATE                                                   REFERENCE                                         NIST 800‐53 REFERENCE
                                                                                    OBJECTIVES
                                                      GOALS                                                           CYBER SECURITY                                                                     [What Good Looks
    [REPORT at this level]                                                                                              FUNCTION                                                 Like]                                                       [DEPLOY                                     (Control Family, Number, Name)
                                                                             [MANAGE at This Level]
                                                                                                                                                                                                                                           at This Level]
                                                                                                                                        Comprehensive security and risk assessment strategy is formally defined and
                                                                                                                                        governed by the enterprise security management policy with senior management
                                                                                                                                        oversight.

                                                                                                                                        Policy identifies security‐specific management and administrative roles and
                                                                                                                                        responsibilities including applicability to vendors and contractors.

                                                                                                                                        Policy mandates process for residual security risk management that includes regular
                                                                                                                                        and periodic assessment of security‐related risk and formal acceptance of residual risk
                                                                                                                                        by accountable organization management.
                                                                                                                                                                                                                                    5305 Information Security
                                                                                                                                                                                                                                    Program
                                                                                                                                        The assessment process is based on an industry‐accepted leading practice security                                         Security Assessment and Authorization:
                                                                             Security Management Plan:
                                                                                                                                        framework and includes criteria for qualifying risk commensurate with the business                                        CA‐7 CONTINUOUS MONITORING
                                                                                                                                                                                                                                    5305.1 Information Security
                                                                        Establish an enterprise policy and direct                       mission of the organization.                                                                Program Management
                                                                                                                                                                                                                                                                  Program Management:
                                                                       the development and maintenance of an
                                                                                                                                        Process addresses residual risk in all aspects of the enterprise including                                                PM‐1 INFORMATION SECURITY PROGRAM PLAN
                                                                      organizational Security Management Plan                                                                                                                       5305.2 Risk Management
                                                                                                                          Protect       telecommunications perimeter, major systems and applications, infrastructure,
                                                                      (SMP) that defines the overall information
                                                                                                                                        resources and data, governance, and procurement/acquisition.                                                              Risk Assessment:
                                                                      protection program as it relates to security                                                                                                                  5305.6 Risk Management
                                                                                                                                                                                                                                                                  RA‐3 RISK ASSESSMENT
                                                                          and privacy, and explicitly describes
                                                                                                                                                                                                                                                                  RA‐1 RISK ASSESSMENT POLICY AND PROCEDURES
                                                                       applicability of security and privacy policy                                                                                                              5305.7 Risk Assessment
                                                                                                                                        The process is enforced through a program of regular and periodic monitoring and
                                                                           to enterprise business processes
                                                                                                                                        testing to validate assessment findings, with resulting metrics used to provide input to
                                                                                                                                                                                                                                 5330.1 Security Assessments
                                                                                                                                        residual risk acceptance process.

                                                                                                                                        Assessment program is periodically supplemented by assessments conducted by
                                                                                                                                        independent third‐parties.

                                                                                                                                        Assessment results are provided as input into overall enterprise risk and compliance
                                                                                                                                        management processes.

                                                                                                                                        Security and risk assessment processes are enhanced and validated through a
                                                                                                                                        program of regular and periodic review, maintenance, update, and audit.

         SECURITY
    GOVERNANCE, (CONT'D).                                                                                                               Comprehensive security planning and system authorization strategy is formally
                                                                                                                                        defined and governed by the enterprise security management policy with senior
                                                                                                                                        management oversight.

                                                                                                                                        Policy identifies security‐specific management and administrative roles and
                                                                                                                                        responsibilities including applicability to vendors and contractors.                                                      Security Assessment and Authorization:
                                                                                                                                                                                                                                                                  CA‐5 PLAN OF ACTION AND MILESTONES
                                                                                                                                        Policy mandates the development and periodic maintenance of system‐specific                5305.6 Risk Management         CA‐6 SECURITY AUTHORIZATION
                                                                                                                                        security plans, and requires senior management approval of the plans, as well as
                                                                                                                                        approval to operate the system or application in the risk environment documented in 5305.7 Risk Assessment                Program Management:
                                                                                                                                        the plan.                                                                                                                 PM‐4 PLAN OF ACTION AND MILESTONES PROCESS
                                                                                                                                                                                                                                   5315.9 Security                PM‐9 RISK MANAGEMENT STRATEGY
                                                                                                                                        Policy defines and identifies accountable management designated to formally accept Authorization                          PM‐10 SECURITY AUTHORIZATION PROCESS
                                                                                   Risk Acceptance:                                     residual risk per organization‐specific criteria which includes overall responsibility for
                                                                                                                                        providing data and services to end‐users, and the authority to provide and/or manage                                      Risk Assessment:
                                                                      Formally establish an organization‐specific                       funding required to appropriately mitigate risks to an acceptable level.                                                  RA‐3 RISK ASSESSMENT
                                                                      policy and supporting process for residual
                                                                       security risk management that includes             Identify
                                                                          regular and periodic assessment of                            Security plans align established security policy with applicable business‐specific
                                                                            security‐related risk and formal                            processes.
                                                                      acceptance of residual risk by accountable
                                                                              organization management                                   Security plans are established for all systems and applications identified as critical to
                                                                                                                                        the organization and successful execution of the business, and identify the
                                                                                                                                        approaches used to satisfy the confidentiality, availability, and integrity requirements
                                                                                                                                        of the systems and data processed, stored, or used by the system.

                                                                                                                                        Security plans define the overall information protection approach applied to the
                                                                                                                                        system and application as it relates to security and privacy, including policies,
                                                                                                                                        processes, and controls.

                                                                                                                                        Security planning and system authorization processes are enhanced and validated
                                                                                                                                        through a program of regular and periodic review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                               8
SIMM 5300‐B                                                                                                                                                                                                                                                                                                               October 2017

                                                                                                                              SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                 SAM 5300
                                                                              2016‐2018 PRIORITY
Security Program Framework                                                                                           NIST                                            TARGET STATE                                                REFERENCE                                      NIST 800‐53 REFERENCE
                                                                                  OBJECTIVES
                                                      GOALS                                                     CYBER SECURITY                                                                    [What Good Looks
    [REPORT at this level]                                                                                        FUNCTION                                                Like]                                                   [DEPLOY                                  (Control Family, Number, Name)
                                                                           [MANAGE at This Level]
                                                                                                                                                                                                                                at This Level]
                                                                                                                                 Procurement governance is formally established, including the identification of spend
                                                                                                                                 thresholds, and governed by enterprise policy.
                                                                                                                                                                                                                         5230.4 Principles for IT
                                                                                                                                 Policy is aligned to the strategic business objectives and articulates the business     Procurement
                                                                                                                                 value.                                                                                                             Access Control:
                                                                          Procurement and Acquisition:                                                                                                             5305.8 Provisions for            AC‐20 USE OF EXTERNAL INFORMATION SYSTEMS
                                                                                                                                 Procurement process workflow is documented to illustrate how stakeholders acquire Agreements with State and
                                                                      Establish and deploy contract terms and                    IT systems/services.                                                              Non‐State Entities               Personnel Security:
                                                                      conditions as appropriate for enforcing                                                                                                                                       PS‐7 THIRD‐PARTY PERSONNEL SECURITY
         SECURITY
                                                                        enterprise security risk management         Protect      Process includes incorporation of security‐specific requirements commensurate with 5315 Information Security
    GOVERNANCE, (CONT'D).
                                                                       policies and requirements in software,                    the type (hardware, software, services) and level of assurance of items being      Integration                     System and Services Acquisition:
                                                                       hardware, or services acquisition and                     acquired.                                                                                                          SA‐9 EXTERNAL INFORMATION SYSTEM SERVICES
                                                                       procurement, including outsourced or                                                                                                         5330 Information Security       SA‐10 DEVELOPER CONFIGURATION MANAGEMENT
                                                                              other contracted efforts.                          Procurement decisions are documented for transparency, and the results are         Compliance                      SA‐4 ACQUISITION PROCESS
                                                                                                                                 commensurate with established policy.                                                                              SA‐4 (1) Functional Properties of Security Controls
                                                                                                                                                                                                                    5315.1 System and Services
                                                                                                                                 Procurement process is periodically assessed, improvement areas identified, and    Acquisition
                                                                                                                                 enhancements implemented.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                 9
SIMM 5300‐B                                                                                                                                                                                                                                                                                                 October 2017

                                                                                                                                                 SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                   SAM 5300
                                                                                             2016‐2018 PRIORITY
Security Program Framework                                                                                                              NIST                                           TARGET STATE                                                REFERENCE                                NIST 800‐53 REFERENCE
                                                                                                 OBJECTIVES
                                                      GOALS                                                                        CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                                           FUNCTION                                               Like]                                                   [DEPLOY                             (Control Family, Number, Name)
                                                                                           [MANAGE at This Level]
                                                                                                                                                                                                                                                  at This Level]
                                                                                                                                                    Platform development / build standards, processes, and procedures are formally
                                                                                                                                                    defined and governed by enterprise policy with senior management oversight.

                                                                                                                                                    Policy identifies specific management and administrative roles and responsibilities,
                                                                                                                                                    including dependencies of vendors and contractors.
                                                                                             Platform‐Specific Build
                                                                                                                                                                                                                                           5315.6 Activate Only
                                                                                           Standards and Procedures:                                Practices include the application of security configuration hardening requirements     Essential Functionality
                                                                                                                                                    that are based on industry‐accepted standards for platform security configuration                                Configuration Management:
                                                                                    Establish enterprise policy that directs the                    management.                                                                                                      CM‐2 BASELINE CONFIGURATION
                                                                                                                                       Protect                                                                                             5335.2 Auditable Events
                                                                                        development and maintenance of                                                                                                                                               CM‐2 (1) Reviews and Updates
                                                                                          organization‐specific platform                            Practices are applied comprehensively for all platform (hardware and operating                                   CM‐3 CONFIGURATION CHANGE CONTROL
                                                                                                                                                                                                                                           5315.5 Configuration
                                                                                    development / build standards, processes,                       system) types in the organization IT asset inventory.
                                                                                                                                                                                                                                           Management
                                                                                                 and procedures
                                                                                                                                                    Policy and standards align with and complement business‐specific processes related
                                        Deploy appropriate management and                                                                           to IT platform use.
                                     protection controls on endpoint platforms
                                    that will maintain stated security objectives                                                                   Security hardening requirements are enforced through a program of regular and
                                       for hosted data and applications under                                                                       periodic review, maintenance, update, and audit.
                                   specific use cases, establish minimal controls
      ENDPOINT SECURITY            for protecting systems, and enforce location‐
                                      based policies with respect to applicable
                                       information, network, and application
                                    architectures. Choose a protection portfolio                                                                    Platform development / build standards, processes, and procedures are formally
                                     that includes preventative, detective, and                                                                     defined and governed by enterprise policy with senior management oversight.
                                      responsive (react or adapt) technologies.                                                                     Policy identifies specific management and administrative roles and responsibilities,
                                                                                           Platform‐Specific Hardening                              including dependencies of vendors and contractors.
                                                                                            Standards and Procedures:
                                                                                                                                                    Practices include the application of security configuration hardening requirements     5315.6 Activate Only
                                                                                                                                                                                                                                                                     Configuration Management:
                                                                                                                                                    that are based on industry‐accepted standards for platform security configuration      Essential Functionality
                                                                                    Establish and document formal enterprise                                                                                                                                         CM‐6 CONFIGURATION SETTINGS
                                                                                                                                       Protect      management.
                                                                                    security policy and standards for platform
                                                                                                                                                                                                                                           5355 Endpoint Defense
                                                                                       configuration management including
                                                                                     requirements for security configuration                        Practices are applied comprehensively for all platform (hardware and operating
                                                                                                    (hardening)                                     system) types in the organization IT asset inventory.

                                                                                                                                                    Policy and standards align with and complement business‐specific processes related
                                                                                                                                                    to IT platform use.

                                                                                                                                                    Security hardening requirements are enforced through a program of regular and
                                                                                                                                                    periodic review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                             10
SIMM 5300‐B                                                                                                                                                                                                                                                                                                              October 2017

                                                                                                                                              SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                SAM 5300
                                                                                            2016‐2018 PRIORITY
Security Program Framework                                                                                                           NIST                                           TARGET STATE                                                REFERENCE                                   NIST 800‐53 REFERENCE
                                                                                                OBJECTIVES
                                                      GOALS                                                                     CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                                        FUNCTION                                                Like]                                                   [DEPLOY                               (Control Family, Number, Name)
                                                                                         [MANAGE at This Level]
                                                                                                                                                                                                                                                at This Level]
                                                                                                                                                 Comprehensive identity and access management strategy is formally defined and
                                                                                                                                                 governed by enterprise policy with senior management oversight.
                                                                                                                                                                                                                                                                  Access Control:
                                                                                                                                                                                                                                                                  AC‐1 ACCESS CONTROL POLICY AND PROCEDURES
                                                                                                                                                 Enterprise policy is applied comprehensively for all business use cases.                                         AC‐1 (1) Automated Account Management
                                                                                                                                                                                                                                                                  AC‐1 (2) Remove of Temporary/Emergency Accounts
                                                                                                                                                 Policy identifies specific management and administrative roles and responsibilities,                             AC‐1 (3) Disable Inactive Accounts
                                                                                                                                                 including applicability to vendors and contractors.                                                              AC‐1 (4) Automated Audit Actions
                                                                                   Comprehensive Documented Enterprise                                                                                                                 5305.4 Personnel
                                                                                                                                                                                                                                                                  AC‐2 ACCOUNT MANAGEMENT
                                                                                          Access Management                                                                                                                            Management
                                                                                                                                                 Strategy is enforced through IAM‐specific architecture and aligned with organization‐                            AC‐3 ACCESS ENFORCEMENT
                                                                                        and Provisioning Strategy:
                                                                                                                                                 specific business objectives and enterprise security objectives.                                                 AC‐5 SEPARATION OF DUTIES
                                                                                                                                                                                                                                       5360 Identity and Access
                                                                                                                                                                                                                                                                  AC‐6 LEAST PRIVILEGE
                                                                                     Establish organization‐specific access                                                                                                              Management
                                                                                     management processes that includes
                                                                                                                                    Protect      Enterprise policy is enforced through use of provisioning processes to track, report,                            Identification and Authentication:
                                                                                        identity lifecycle management,                                                                                                                   5360.1 Remote Access
                                                                                                                                                 and validate individual user access rights and privileges.                                                       IA‐1 IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES
                                                                                   consolidated and comprehensive use case
                                                                                                                                                                                                                                                                  IA‐2 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)
                                                                                     provisioning and change management                                                                                                                  5360.2 Wireless Access
                                                                                                                                                 Policy is implemented through use of modern, enterprise‐class automated                                          IA‐3 DEVICE IDENTIFICATION AND AUTHENTICATION
                                                                                       workflow, and centralized access
                                                                                                                                                 provisioning and access management technology.                                                                   IA‐4 IDENTIFIER MANAGEMENT
                                                                                       authentication and authorization                                                                                                          5365.1 Access Control for
                                                                                                                                                                                                                                                                  IA‐5 AUTHENTICATOR MANAGEMENT
                                                                                                    processes                                    Compliance and reporting requirements are enforced through the deployment of    Output Devices
                                                                                                                                                                                                                                                                  IA‐8 IDENTIFICATION AND AUTHENTICATION (NON‐ORGANIZATIONAL USERS)
                                                                                                                                                 modern Governance‐Risk‐Compliance (GRC) technology integrated with provisioning
                                                                                                                                                 processes.                                                                                                       Personnel Security:
                                                                                                                                                                                                                                                                  PS‐3 PERSONNEL SCREENING
                                                                                                                                                 Strategy and policy, processes, and integrity of identity data is enhanced and                                   PS‐5 PERSONNEL TRANSFER
                                                                                                                                                 validated through a program of regular and periodic review, maintenance, update,                                 PS‐6 ACCESS AGREEMENTS
                                                                                                                                                 and audit.

                                                                                                                                                 Standards for credentials for gaining access to IT resources are formally defined and
                                                                                                                                                 governed by enterprise policy with senior management oversight.

                                                                                                                                                 Policy identifies specific management and administrative roles and responsibilities,
                                                                                                                                                 including applicability to vendors and contractors, and is applied and enforced                                  Access Control:
                                                                                                                                                 comprehensively for all use cases and platforms in the enterprise IT asset inventory.                            AC‐1 ACCESS CONTROL POLICY AND PROCEDURES
                                                                                                                                                                                                                                                                  AC‐2 ACCESS CONTROL POLICY AND PROCEDURES
                                     Establish an identity management service                                                                                                                                                                                     AC‐17 REMOTE ACCESS
                                   layer that provides consistent access control                                                                 Policy enforcement addresses requirements applicable to levels of authentication
                                     and policy enforcement; identity lifecycle          Multi‐Factor Authentication                             assurance for systems and data commensurate with business processes and impact of                                Identification and Authentication:
        IDENTITY AND
                                     and credential management; and identity             for Elevated Risk Use Cases:                            risk exposure.                                                                    5305.4 Personnel               IA‐1 IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES
     ACCESS MANAGEMENT
                                      data services for all subjects (users and                                                                                                                                                    Management                     IA‐2 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)
                                         services) and resources (systems,         Replace the use of traditional passwords                      Standards address password strength as applicable to assurance requirements, and                                 IA‐2 (1) Network Access to Privileged Accounts
                                      applications, data) in the environment.        for authentication by acquiring and            Protect      are based on industry‐accepted standards for consumer authentication.             5360 Identity and Access       IA‐2 (2) Network Access to Non‐Privileged Accounts
                                                                                     deploying appropriate multi‐factor                                                                                                            Management                     IA‐2 (3) Local Access to Privileged Accounts
                                                                                   authentication for all high risk use cases                                                                                                                                     IA‐2 (4) Local Access to Non‐Privileged Accounts
                                                                                    and users with write/modify‐rights to                        Traditional passwords have been replaced by multi‐factor credentials for all high risk 5360.1 Remote Access      IA‐4 IDENTIVER MANAGEMENT
                                                                                                sensitive data                                   use cases including remote access users, privileged users and administrators (i.e.,                              IA‐5 AUTHENTICATOR MANAGEMENT
                                                                                                                                                 users authorized to bypass or modify security controls and device or data                                        IA‐8 IDENTIFICATION AND AUTHENTICATION (NON‐ORGANIZATIONAL USERS)
                                                                                                                                                 configurations), and users with write/modify‐rights to sensitive data.
                                                                                                                                                                                                                                                                  Personnel Security:
                                                                                                                                                                                                                                                                  PS‐5 Personnel Transfer
                                                                                                                                                 Credentials are administered and managed through enterprise provisioning process.                                PS‐6 Access Agreements

                                                                                                                                                 Standards are further enforced and enhanced through a program of regular and
                                                                                                                                                 periodic review, maintenance, update, and audit.

                                                                                                                                                 Approach for user access authorization rights and privilege management is defined
                                                                                                                                                 and governed as part of the enterprise IAM policy.

                                                                                                                                                 Authorization management practices are managed through enterprise provisioning
                                                                                        Privileged User Management                               process, enforced through enterprise authoritative identity data sources, and
                                                                                       and Best Practices Enforcement:                           integrated with centralized access management processes and technology.                                          Access Control:
                                                                                                                                                                                                                                                                  AC‐1 ACCESS CONTROL POLICY AND PROCEDURES
                                                                                   Enhance the administration of privileged                                                                                                              5305.4 Personnel
                                                                                                                                                                                                                                                                  AC‐2 ACCOUNT MANAGEMENT
                                                                                   accounts (i.e., users authorized to bypass                    Execution of authentication rights and privileges are contingent on successful          Management
                                                                                                                                                                                                                                                                  AC‐6 LEAST PRIVILEGE
                                                                                   or modify security controls and device or                     authentication, and are comprehensively used to facilitate reduced sign‐on, role and
                                                                                                                                                                                                                                                                  AC‐17 REMOTE ACCESS
                                                                                     data configurations) by acquiring and          Protect      entitlement management, and transaction monitoring as applicable.                    5360 Identity and Access
                                                                                   deploying appropriate Privileged Account                                                                                                           Management
                                                                                                                                                                                                                                                                  Identification and Authentication:
                                                                                     Management solution. Configure and
                                                                                                                                                                                                                                                                  IA‐1 IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES
                                                                                    systematically enforce expiration of all                     Authorization management enforcement is strengthened through regular and                5360.1 Remote Access
                                                                                                                                                                                                                                                                  IA‐5 AUTHENTICATOR MANAGEMENT
                                                                                       privileged accounts. Consider the                         periodic re‐validation of individual user access requirements and assignments.
                                                                                                                                                                                                                                                                  IA‐11 RE‐AUTHENTICATION
                                                                                     implementation of a shared‐account
                                                                                      password management capability
                                                                                                                                                 Processes and integrity of authorization data is enhanced and validated through a
                                                                                                                                                 program of regular and periodic review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                                 11
SIMM 5300‐B                                                                                                                                                                                                                                                                                                                  October 2017

                                                                                                                                            SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                           SAM 5300
                                                                                           2016‐2018 PRIORITY
Security Program Framework                                                                                                         NIST                                          TARGET STATE                                              REFERENCE                                NIST 800‐53 REFERENCE
                                                                                               OBJECTIVES
                                                      GOALS                                                                   CYBER SECURITY                                                                  [What Good Looks
    [REPORT at this level]                                                                                                      FUNCTION                                               Like]                                                [DEPLOY                             (Control Family, Number, Name)
                                                                                        [MANAGE at This Level]
                                                                                                                                                                                                                                          at This Level]
                                                                                                                                               Devices configurations are formally defined and governed by enterprise policy.

                                                                                                                                               Configurations are enforced through comprehensive device management
                                                                                                                                               technologies that include configuration control and remote wipe; data transmission
                                       Deploy appropriate management and                                                                       and on‐device encryption; data archiving and containerization; on‐device application                         Access Control:
                                    protection controls on mobile devices that               Enterprise Mobile                                 control and enterprise mobile application lifecycle management; user authentication 5350.1 Encryption        AC‐19 ACCESS CONTROL FOR MOBILE DEVICES
                                    will maintain stated security objectives for            Device Management:                                 to device and device authentication to environment.
                                    hosted data and applications under specific
                                                                                                                                                                                                                                    5365.3 Media Disposal   Configuration Management:
        MOBILE SECURITY              use cases, establish minimal controls for         Establish and document a formal            Protect
                                                                                                                                                                                                                                                            CM‐2 BASELINE CONFIGURATION
                                     protecting devices, and enforce location‐     enterprise security policy and standards                    Training on appropriate use is included in regular and periodic security awareness
                                                                                                                                                                                                                                    5315.5 Configuration
                                     based policies with respect to applicable     for mobile handheld devices and device                      program.
                                                                                                                                                                                                                                    Management              Identification and Authentication:
                                      information, network, and application               configuration management
                                                                                                                                                                                                                                                            IA‐3 DEVICE IDENTIFICATION AND AUTHENTICATION
                                                   architectures.                                                                              Monitoring and reporting processes are defined and established to ensure policy
                                                                                                                                               adherence.

                                                                                                                                               Device configurations and protections are enhanced and validated through a program
                                                                                                                                               of regular and periodic review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                     12
SIMM 5300‐B                                                                                                                                                                                                                                                                                                      October 2017

                                                                                                                                             SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                SAM 5300
                                                                                          2016‐2018 PRIORITY
Security Program Framework                                                                                                           NIST                                           TARGET STATE                                                REFERENCE                                      NIST 800‐53 REFERENCE
                                                                                              OBJECTIVES
                                                      GOALS                                                                     CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                                        FUNCTION                                                Like]                                                   [DEPLOY                                 (Control Family, Number, Name)
                                                                                        [MANAGE at This Level]
                                                                                                                                                                                                                                                at This Level]
                                                                                                                                                 Modern, enterprise‐class network intrusion prevention/detection technologies are
                                                                                                                                                 deployed and operational to provide feedback on protection of critical IT resources
                                                                                                                                                 and business processes with significant sensitive information responsibilities.

                                                                                                                                                 Solution(s) are: aligned with organization‐specific business processes; tailored
                                                                                                                                                 commensurate with enterprise data classification policy; aligned and integrated with
                                                                                                                                                 enterprise telecommunications and network services strategy as well as the network                                  Audit and Accountability:
                                                                                                                                                 zoning strategy.                                                                                                    AU‐2 AUDIT EVENTS
                                                                                                                                                                                                                                         5335.1 Continuous
                                                                                                                                                                                                                                                                     AU‐3 CONTENT OF AUDIT RECORDS
                                                                                                                                                 Monitoring capabilities include: critical alert escalation through enterprise incident  Monitoring
                                                                                                                                                                                                                                                                     AU‐6 AUDIT REVIEW, ANALYSIS, AND
                                                                                     Exposure and Intrusion Detection                            response process; supplementation with active network segment blocking, re‐routing,
                                                                                                                                                 or resource suspension; integration with enterprise security information and event     5335 Information Security
                                                                                        and Prevention Capability:                                                                                                                                                   Reporting:
                                                                                                                                                 management (SIEM) capability and/or security operations center (SOC).                  Monitoring
                                                                                                                                                                                                                                                                     AU‐7 LOG AGGREGATION
                                                                                      Deploy monitoring and response                                                                                                                                                 AU‐12 AUDIT GENERATION
                                                                                                                                                                                                                                         5335.2 Auditable Events
                                                                                     processes and technologies for all             Detect
                                                                                                                                                 Monitoring effectiveness is maintained through a program of regular and periodic
                                                                                 inbound, internal, and outbound network                                                                                                                                             Incident Response:
                                                                                                                                                 review, update, and audit.                                                           5340 Information Security
                                                                                 activity to identify suspicious patterns and                                                                                                                                        IR‐4 INCIDENT HANDLING
                                                                                                                                                                                                                                      Incident Management
                                                                                 correct malicious or unauthorized actions                                                                                                                                           IR‐1 INCIDENT RESPONSE POLICY AND PROCEDURES
                                                                                                                                                 A baseline of activity within the organization has been created from which anomalous
                                                                                               or policy violations                                                                                                                                                  IR‐5 INCIDENT RESPONSE MONITORING
                                                                                                                                                 activity can be identified and investigated.                                         5340.3 Incident Handling

                                    Deploy controls that monitor and prevent                                                                     Baseline maintenance is part of the development lifecycle and revalidated as part of                                System and Information Integrity:
                                                                                                                                                                                                                                         5340.4 Incident Reporting
    SECURITY ANALYTICS AND          attacks or limit the consequences of their                                                                   the testing new services.                                                                                           SI‐3 MALICIOUS CODE PROTECTION
   CONTINUOUS MONITORING              success on the network or within the                                                                                                                                                                                           SI‐4 INFORMATION SYSTEM MONITORING
                                                  infrastructure.                                                                                Signature based tools are used at appropriate choke points within the organization to
                                                                                                                                                 identify malicious activity embedded in valid traffic flows.

                                                                                                                                                 There is a well defined incident response process when anomalous activity is
                                                                                                                                                 detected, which includes a pre‐defined action plan and a communication plan for key
                                                                                                                                                 stakeholders.

                                                                                                                                                 Organization‐specific Security Information and Event Management (SIEM) risk                                         Audit and Accountability:
                                                                                                                                                 monitoring capabilities are deployed for critical infrastructure environments and                                   AU‐2 AUDIT EVENTS
                                                                                   Enterprise Specific Event Correlation                         those with significant sensitive information contents.                                  5335.1 Continuous           AU‐3 CONTENT OF AUDIT RECORDS
                                                                                        and Evaluation Capability:                                                                                                                       Monitoring                  AU‐6 AUDIT REVIEW, ANALYSIS, AND REPORTING
                                                                                                                                                 SIEM integrates and archives alert and transaction log information from all critical                                AU‐7 LOG AGGREGATION
                                                                                  Acquire and deploy organization‐specific                       perimeter and infrastructure processing, monitoring, and control devices.               5335 Information Security   AU‐12 AUDIT GENERATION
                                                                                     event analysis capabilities for critical                                                                                                            Monitoring
                                                                                                                                    Detect
                                                                                    infrastructure environments and those                                                                                                                                            Incident Response:
                                                                                     with significant sensitive information                      Alerts are integrated with organization‐specific incident response process.             5335.2 Auditable Events     IR‐4 INCIDENT HANDLING
                                                                                   contents. Consider engaging a Managed
                                                                                  Security Service Provider (MSSP) to assist                     Risk monitoring and analytics processes and technologies are enhanced and validated 5355.2 Security Alerts,         System and Information Integrity:
                                                                                 in monitoring and analyzing system events                       through a program of regular and periodic review, maintenance, update, and audit. Advisories, and Directives        SI‐3 MALICIOUS CODE PROTECTION
                                                                                                                                                                                                                                                                     SI‐4 INFORMATION SYSTEM MONITORING
                                                                                                                                                                                                                                                                     SI‐5 SECURITY ALERTS, ADVISORIES, AND DIRECTIVES

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                               13
SIMM 5300‐B                                                                                                                                                                                                                                                                                                                October 2017

                                                                                                                                               SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                    SAM 5300
                                                                                           2016‐2018 PRIORITY
Security Program Framework                                                                                                            NIST                                           TARGET STATE                                                   REFERENCE                                      NIST 800‐53 REFERENCE
                                                                                               OBJECTIVES
                                                      GOALS                                                                      CYBER SECURITY                                                                   [What Good Looks
    [REPORT at this level]                                                                                                         FUNCTION                                                Like]                                                     [DEPLOY                                  (Control Family, Number, Name)
                                                                                        [MANAGE at This Level]
                                                                                                                                                                                                                                                   at This Level]
                                                                                                                                                  Comprehensive standards for internal telecommunication network architecture are
                                                                                                                                                  formally defined and governed by enterprise policy with senior management
                                                                                                                                                  oversight.

                                                                                                                                                  Standards include identification and definition of zones of trust including perimeter
                                                                                                                                                  zones such as De‐Militarized Zones, Trusted Zones such as user and resource zones,
                                                                                 Technical Enforcement of Security Layers                         and Restricted Zones such as high‐value asset, Control, or Audit Zones.
                                                                                       and Data Center Separation:

                                                                                  Create multiple distinct zones separated                        Standards address authorized internal network protocols, zone perimeter                                               System and Communications Protection:
                                                                                 by firewall functionality. Deploy technical                      configurations, and protection and monitoring controls commensurate and aligned           5315.8 Information Asset    SC‐7 BOUNDARY PROTECTION
                                                                                 security separation controls (e.g., firewall‐                    with enterprise data classification and telecommunications and network services           Connections
                                                                                                                                     Protect      policies and standards.
                                                                                 enforced network segmentation) between                                                                                                                                                 Security Assessment and Authorization:
                                                                                   user resources and infrastructure (e.g.,                                                                                                                 5350 Operational Security   CA‐3 SYSTEM INTERCONNECTIONS
                                                                                                                                                  Authorized use case guidelines for each zone are defined and enforced, and include
                                                                                       servers, mainframes, network
                                                                                                                                                  the protection of data and resources used, processed, stored, or transmitted through
                                                                                   components) resources located on the
                                                                                                                                                  the zone.
                                                                                   internal, trusted network (data center
                                                                                                   firewall)                                      Standards are enforced through integration of modern network segmentation
                                                                                                                                                  technologies and methodologies into enterprise perimeter control and monitoring
                                                                                                                                                  infrastructure.

                                                                                                                                                  Standards and zoning architecture are enhanced and validated through a program of
                                                                                                                                                  regular and periodic review, maintenance, update, and audit.

                                       Deploy controls that establish external                                                                    Comprehensive endpoint connection and remote access strategy is formally defined
                                        perimeters to separate zones of trust                                                                     and governed by enterprise policy with senior management oversight.
      NETWORK SECURITY               (enterprise‐wide, business unit/function,
                                      location) and to enforce controls on the
                                        traffic entering or leaving each zone.                                                                    Strategy includes identification and definition of authorized business‐justified remote
                                                                                                                                                  access use cases, and identifies security‐specific management and administrative
                                                                                                                                                  roles and responsibilities including applicability to vendors and contractors.
                                                                                                                                                                                                                                            5315.8 Information Asset
                                                                                                                                                                                                                                            Connections
                                                                                                                                                  Strategy is aligned and integrated with enterprise telecommunications and network
                                                                                                                                                  services policy, as well as device configuration management strategy.                                                 Security Assessment and Authorization:
                                                                                                                                                                                                                                            5355.1 Malicious Code
                                                                                        Network Admission Control:                                                                                                                                                      CA‐2 SECURITY ASSESSMENTS
                                                                                                                                                                                                                                            Protection
                                                                                                                                                                                                                                                                        CA‐5 PLAN OF ACTION AND MILESTONES
                                                                                  Establish enterprise policy and practices                       Policy and practices for establishing connections with the IT infrastructure includes                                 CA‐6 SECURITY AUTHORIZATION
                                                                                                                                                                                                                                            5360.1 Remote Access
                                                                                  for establishing connections with the IT                        identification and definition of connection types used throughout the enterprise in                                   CM‐7 LEAST FUNCTIONALITY
                                                                                                                                     Detect
                                                                                 infrastructure that includes identification                      alignment with business processes.
                                                                                                                                                                                                                                            5360.2 Wireless Access
                                                                                  and definition of connection types used                                                                                                                                               Program Management:
                                                                                  throughout the enterprise in alignment                          Authorized use case guidelines for connection approaches include remote, wired,                                       PM‐4 PLAN OF ACTION AND MILESTONES PROCESS
                                                                                                                                                                                                                                            5315.5 Configuration
                                                                                          with business processes                                 wireless, and other over‐the‐air, as well as required standards for security and data                                 PM‐9 RISK MANAGEMENT STRATEGY
                                                                                                                                                                                                                                            Management
                                                                                                                                                  protection per use case.                                                                                              PM‐10 SECURITY AUTHORIZATION PROCES

                                                                                                                                                  Secure access policy enforces: standards for user and device identification and           5360 Identity and Access
                                                                                                                                                  authentication; device configuration with respect to operating system, patch level,       Management
                                                                                                                                                  anti‐malware software, endpoint protection mechanisms, and telecommunications
                                                                                                                                                  capabilities; device health with respect to unauthorized or malicious software.

                                                                                                                                                  Implementation is enhanced and validated through a program of regular and periodic
                                                                                                                                                  review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                                   14
SIMM 5300‐B                                                                                                                                                                                                                                                                                                                    October 2017

                                                                                                                                           SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                          SAM 5300
                                                                                          2016‐2018 PRIORITY
Security Program Framework                                                                                                        NIST                                          TARGET STATE                                              REFERENCE                                    NIST 800‐53 REFERENCE
                                                                                              OBJECTIVES
                                                      GOALS                                                                  CYBER SECURITY                                                                 [What Good Looks
    [REPORT at this level]                                                                                                     FUNCTION                                              Like]                                                 [DEPLOY                                 (Control Family, Number, Name)
                                                                                        [MANAGE at This Level]
                                                                                                                                                                                                                                         at This Level]
                                                                                                                                              Comprehensive physical protection and access strategy is formally defined and
                                                                                                                                              governed by enterprise policy with senior management oversight.

                                                                                                                                              Strategy identifies security‐specific management and administrative roles and                                   Identification and Authentication:
                                                                                                                                              responsibilities including applicability to vendors and contractors.                                            IA‐2 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)
                                                                                                                                                                                                                                  5365 Physical Security
                                                                                                                                              Strategy is commensurate with business use cases and aligned with business and                                  Media Protection:
                                                                                   Physical Security Policy Enforcement                       security objectives.                                                                5365.1 Access Control for   MP‐2 MEDIA ACCESS
                                     Ensure that a defense‐in‐depth approach
                                                                                    for Data Center and Remote Sites:                                                                                                             Output Devices              MP‐4 MEDIA STORAGE
                                      includes physical controls that protect
                                                                                                                                              Policy is enforced through comprehensive hybrid of modern technological and
       PHYSICAL SECURITY                against unauthorized access to or                                                        Protect
                                                                                   Evaluate and enforce existing physical                     procedural methods which address: hazard free building location (airports, nuclear    5365.2 Media Protection   Physical and Environmental Protection:
                                   inadvertent exposure of critical IT equipment
                                                                                   security policies and practices through                    power plants); building perimeter and interior access controls; visitor and vendor                              PE‐1 PHYSICAL AND ENVIRONMENTAL PROTECTION POLICY AND PROCEDURES
                                            and sensitive information.
                                                                                      monitoring and audit reporting                          control and logging; locking office space and printer protection; hardcopy protection 5365.3 Media Disposal     PE‐2 PHYSICAL ACCESS AUTHORIZATIONS
                                                                                                                                              including retention, storage, destruction, and "clean desk"; video surveillance for                             PE‐3 PHYSICAL ACCESS CONTROL
                                                                                                                                              internal, perimeter, and external; emergency procedures; personnel badging and key 5320.4 Personnel Security    PE‐5 ACCESS CONTROL FOR OUTPUT DEVICES
                                                                                                                                              access.                                                                                                         PE‐6 MONITORING PHYSICAL ACCESS
                                                                                                                                                                                                                                                              PE‐18 LOCATION OF INFORMATION SYSTEM COMPONENTS
                                                                                                                                              Policy and practices enforcements are enhanced and validated through a program of
                                                                                                                                              regular and periodic review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                             15
SIMM 5300‐B                                                                                                                                                                                                                                                                                                              October 2017

                                                                                                                                               SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                                      SAM 5300
                                                                                            2016‐2018 PRIORITY
Security Program Framework                                                                                                            NIST                                           TARGET STATE                                                     REFERENCE                                        NIST 800‐53 REFERENCE
                                                                                                OBJECTIVES
                                                      GOALS                                                                      CYBER SECURITY                                                                    [What Good Looks
    [REPORT at this level]                                                                                                         FUNCTION                                                Like]                                                       [DEPLOY                                    (Control Family, Number, Name)
                                                                                          [MANAGE at This Level]
                                                                                                                                                                                                                                                     at This Level]
                                                                                                                                                  Comprehensive anti‐malicious software strategy is formally defined and governed by
                                                                                                                                                  enterprise security management policy.

                                                                                                                                                  Policy identifies process‐specific operational, management, and administrative roles
                                                                                                                                                  and responsibilities including applicability to vendors and contractors.

                                                                                                                                                  Strategy is commensurate with business use cases and aligned with business and
                                                                                                                                                  security objectives.

                                                                                                                                                  Anti‐malicious software/endpoint protection solutions are deployed on all server and
                                                                                                                                                  workstation platforms used across the enterprise, including mobile devices.

                                                                                                                                                  Enterprise class Secure Web Gateway (SWG) and Secure Email Gateway are deployed
                                                                                                                                                  to filter critical infrastructure environments from malicious software, external attacks,
                                                                                                                                                  and other inappropriate or unauthorized activity.

                                                                                       Comprehensive Platform‐Specific                                                                                                                        5355 Endpoint Defense        System and Information Integrity:
                                                                                          Anti‐Malware Approach:                                  Solution(s) are aligned with organization‐specific business processes and tailored                                       SI‐3 MALICIOUS CODE PROTECTION
                                                                                                                                                  commensurate with enterprise acceptable use and data classification policies.               5355.1 Malicious Code        SI‐3 (1) Central Management
                                                                                       Deploy anti‐malicious software or             Protect                                                                                                  Protection                   SI‐3 (2) Automatic Updates
                                                                                   endpoint protection solution on all server                                                                                                                                              SI‐4 INFORMATION SYSTEM MONITORING
                                                                                                                                                  Prevention controls are enforced with active blocking and alerting.
                                                                                   and workstation platforms used across the                                                                                                                  5355.2 Security Alerts,      SI‐4 (2) Automated Tools for Real‐Time Analysis
                                                                                                  enterprise                                                                                                                                  Advisories, and Directives   SI‐4 (5) Stystem Generated Alerts
                                                                                                                                                  Deployment is comprehensive across all server platform types including application,
                                                                                                                                                  file share, data base and data repository, communication and collaboration, and
                                                                                                                                                  domain management.

                                                                                                                                                  Deployment encompasses all platforms in all environments including external and
                                                                                                                                                  internal‐facing, production, development, test, and stand‐alone.

                                                                                                                                                  Solutions are configured to accept timely updates to attack recognition criteria or
                                    Deploy controls to track and map assets to                                                                    signature information, as well as processing and analysis engine software.
                                     technical security policy, monitor and scan
                                    for known vulnerabilities, and evaluate and
                                                                                                                                                  Solution is configured for centralized alerting and notification, and integrated with
                                       mitigate vulnerabilities by patching the
                                                                                                                                                  security event management or security operations center, and incident response and
                                        software, changing configurations, or
 VULNERABILITY MANAGEMENT                                                                                                                         management processes.
                                      deploying other controls in an attempt to
                                      reduce the attack surface at the resource
                                                                                                                                                  Control effectiveness is enhanced and validated through a program of regular and
                                     layer (system or device operating systems,
                                                                                                                                                  periodic review, maintenance, update, testing, and audit.
                                          applications, databases, and other
                                       information technology (IT) resources).                                                                    Comprehensive security incident handling strategy is formally defined and governed
                                                                                                                                                  by enterprise policy with senior management oversight.

                                                                                                                                                  Policy identifies security‐specific management and administrative roles and
                                                                                                                                                  responsibilities including applicability to vendors and contractors.

                                                                                                                                                  Incident response and management plan is documented and includes identification
                                                                                                                                                  and definition of potential and actual incident events and associated priorities,
                                                                                                                                                  responses, authority, roles and responsibilities, points of escalation, and closure.

                                                                                                                                                  Plan identifies security‐specific technical, operational, management and
                                                                                                                                                  administrative roles and responsibilities, including applicability to vendors and
                                                                                                                                                  contractors.                                                                                5340 Information Security
                                                                                                                                                                                                                                                                           Incident Response:
                                                                                      Comprehensive Incident Response                                                                                                                         Incident Management
                                                                                                                                                                                                                                                                           IR‐1 INCIDENT RESPONSE POLICY AND PROCEDURES
                                                                                          and Management Plan:                                    Plan includes communication plan that addresses emergency notification,                                                  IR‐2 INCIDENT RESPONSE TRAINING
                                                                                                                                                  management escalation, peer and partner notification, public affairs communication 5340.2 Incident Response              IR‐3 INCIDENT RESPONSE TESTING
                                                                                      Establish repeatable and consistent           Respond       management, and constituent (service/product customer/consumer) notification with Testing                                IR‐4 INCIDENT HANDLING
                                                                                   enterprise policy, processes, and practices                    respect to applicable statutory regulations.                                                                             IR‐5 INCIDENT MONITORING
                                                                                       for security incident response and                                                                                                            5340.3 Incident Handling
                                                                                                                                                                                                                                                                           IR‐6 INCIDENT REPORTING
                                                                                                  management
                                                                                                                                                                                                                                                                           IR‐8 INCIDENT RESPONSE PLAN
                                                                                                                                                  Incident handling process, governed by the plan, addresses event reporting intake           5340.4 Incident Reporting
                                                                                                                                                  and coordination, immediate incident response and triage, near‐term vulnerability
                                                                                                                                                  remediation and testing, long‐term enterprise architecture enhancement, tracking
                                                                                                                                                  and reporting events metrics and lessons learned, and formal closure.

                                                                                                                                                  Incident handling processes is integrated with and escalation to business continuity,
                                                                                                                                                  disaster recovery, and emergency management plans as appropriate.

                                                                                                                                                  Incident response and management plan is maintained through a program of regular
                                                                                                                                                  and periodic formal reviews and testing, as well as personnel training.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                                       16
SIMM 5300‐B                                                                                                                                                                                                                                                                                                                        October 2017

                                                                                                                                   SIMM 5300‐B FOUNDATIONAL FRAMEWORK

                                                                                                                                                                                                                                          SAM 5300
                                                                               2016‐2018 PRIORITY
Security Program Framework                                                                                                NIST                                            TARGET STATE                                                    REFERENCE                                       NIST 800‐53 REFERENCE
                                                                                   OBJECTIVES
                                                      GOALS                                                          CYBER SECURITY                                                                     [What Good Looks
    [REPORT at this level]                                                                                             FUNCTION                                                 Like]                                                      [DEPLOY                                    (Control Family, Number, Name)
                                                                             [MANAGE at This Level]
                                                                                                                                                                                                                                         at This Level]
                                                                                                                                      Incident reporting process is addressed through enterprise security awareness
                                                                                                                                      program.

                                                                                                                        Respond       Incident response and management plan and processes are enhanced and validated
                                                                                                                                      through a program of regular and periodic review, maintenance, update, and audit.

                                                                                                                                      Patch management standards are formally defined and governed by enterprise
                                                                                                                                      configuration management policy with senior management oversight.

                                                                                                                                      Policy identifies specific management and administrative roles and responsibilities,
                                                                                                                                      including dependencies of vendors and contractors.

                                                                                                                                      Standards address all platform and 3rd‐party software.
                                                                          Comprehensive Platform‐Specific
                                                                           Vulnerability Patching Process:                            Processes are used to ensure that applicable vendor platform operating system,
                                                                                                                                      software releases, patches are appropriately identified, evaluated, tested, and             5305.8 Provisions for        Configuration Management:
                                                                           Establish a formal, comprehensive                          deployed in a timely manner for all IT assets in use by or managed on behalf of the         Agreements with State and    CM‐2 BASELINE CONFIGURATION
                                                                             organization‐specific platform                           organization.                                                                               Non‐State Entities
                                                                          management process to ensure that                                                                                                                                                    System and Services Acquisition:
                                                                        vendor platform operating system and             Protect      Processes includes testing in target or like environment, and deployment to individual 5345 Vulnerability and            SA‐10 DEVELOPER CONFIGURATION MANAGEMENT
                                                                           software releases and patches are                          devices through a controlled process from a managed distribution environment.          Threat Management                 SA‐22 UNSUPPORTED SYSTEM COMPONENTS
                                                                      appropriately identified, evaluated, tested,
                                                                       and deployed in a timely manner for all IT                                                                                                          5355.2 Security Alerts,             System and Information Integrity:
                                                                       assets in use by or managed on behalf of                       Patch management is enforced through metrics related to successful testing and       Advisories, and Directives          SI‐2 FLAW REMEDIATION
                                                                         the organization (patch management                           deployment, and include closed‐loop follow‐up verification of successful deployment.
                                                                                         process)

                                                                                                                                      Patch management tools include automated patch management solution, and
                                                                                                                                      integrate tracking through organization‐specific change management process.

                                                                                                                                      Patch management processes are enhanced and validated through a program of
 VULNERABILITY MANAGEMENT,                                                                                                            regular and periodic review, maintenance, update, and audit.
            CONT.
                                                                                                                                      Vulnerability management practices are formally defined, documented, and governed
                                                                                                                                      by enterprise configuration management policy with senior management oversight.

                                                                                                                                      Policy identifies security‐specific management and administrative roles and
                                                                                                                                      responsibilities including applicability to vendors and contractors.

                                                                                                                                      Comprehensive enterprise vulnerability scanning and testing program includes
                                                                                                                                      regular and periodic vulnerability scanning of all operational applications, platforms,
                                                                                                                                      and devices operating in production as well as prior to placing any applications,
                                                                                                                                      platforms, or devices into production.
                                                                            Comprehensive Vulnerability
                                                                      Identification Program Including Periodic                       Pre‐production vulnerability scanning is used to supplement all software and
                                                                       and Pre‐Production Vulnerability Scans                         hardware build, promotion, and production‐release processes.                                                             Risk Assessment Policy and Procedures:
                                                                           for Platforms and Applications:                                                                                                                                                     RA‐5 VULNERABILITY SCANNING
                                                                                                                                      The scanning program is enforced at both the enterprise and organization‐specific           5345 Vulnerability and
                                                                          Establish a formal, comprehensive                           levels, as well as from both external and internal perspectives.                            Threat Management            System and Services Acquisition:
                                                                        enterprise vulnerability scanning and            Detect                                                                                                                                SA‐11 DEVELOPER SECURITY TESTING AND EVALUATION
                                                                      testing program that includes regular and                       Vulnerability scanning program is supplemented with additional program of regular           5355.2 Security Alerts,
                                                                         periodic vulnerability scanning of all                       and periodic active penetration testing.                                                    Advisories, and Directives   System and Information Integrity:
                                                                       operational applications, platforms, and                                                                                                                                                SI‐2 FLAW REMEDIATION
                                                                       devices operating in production as well                        Critical or repeat findings are escalated to enterprise level for tracking and reporting.                                SI‐7 SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY
                                                                           prior to placing any applications,
                                                                        platforms, or devices into production
                                                                                                                                      Enforce policy for remediation of critical, externally‐determined findings within
                                                                                                                                      specific period of time with defined consequences for lack of compliance.

                                                                                                                                      Integrate remediation of scan and test findings with organization‐specific change
                                                                                                                                      management process.

                                                                                                                                      Vulnerability scanning processes are enhanced and validated through a program of
                                                                                                                                      regular and periodic review, maintenance, update, and audit.

California Department of Technology, Office of Information Security
Foundational Framework                                                                                                                                                                                                                                                                                                           17
SIMM 5300‐B                                                                                                                                                                                                                                                                                                            October 2017

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
