---
schema_version: 1
corpus: states-government-it
jurisdiction: wyoming
id: wy-wyit-2001-s3
title: Data Custodian Standard
doc_type: standard
citation: WyIT 2001-S3
authority_level: ''
issuing_body: Wyoming Department of Enterprise Technology Services (Office of the Chief Information Officer)
source_url: https://drive.google.com/uc?export=download&id=14Ep1qWF7SBX6bTC4BPT2_3tIXhSEA_aW
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 3ab60a11756328b880aaac738b9beb60edff144be2fdf183e8438d5c3e032d2d
effective_date: '2025-09-12'
source_version: 2026-09.1
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). effective_date is the Effective Date cell of the file's header table, as printed. source_version
  is the Policy Version (or Document Version) cell of the header table, as printed.
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
- data
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Data Custodian Standard (WyIT 2001-S3)

## At a glance

WyIT 2001-S3, Data Custodian Standard: a statewide standard in the Enterprise Technology Services policy library. Per the Applicability section of the file it applies to all Executive Branch agencies, boards and commissions staff and to consultants, affiliates and temporary employees.

## Full text

Data Custodian Standard
WyIT.2001-S3

 Document Owner         Department of Enterprise Services, Data Privacy
 Document Contact       Pat Potter, Deputy Chief Data Officer
 Document Approver      Wyoming Data Governance Committee (WDGC)
 Effective Date         September 12, 2025
 Next Review Date       April 1, 2027
 Document Version       2026-09.1
 Associated Policy      WyIT 2001, Information Classification

​
Introduction:
This standard establishes the requirements and duties for Data Custodian functions to ensure proper
technical implementation and maintenance of security controls for information protection in compliance
with Wyoming information management policies.

This standard applies to all Executive Branch agencies, boards, and commissions staff (collectively
referred to as "agencies"). This standard is also applicable to consultants, affiliates, third party vendors
and temporary employees that use or store data.

Authority
This standard is promulgated under the authority of Wyoming State Statute 9-2-2906 and its
subsections, the Department of Enterprise Technology Services is required to adopt and enforce
information technology standards, and promote efficient use of information technology throughout state
government.

Specifically, this policy is further promulgated under the authority of the below listed Wyoming State
Statute subsections.

   ●​ Implements and maintains an information technology governance program for state agencies
      (W.S 9-2-2906,(b), (ii));
   ●​ Establishes and enforces data security and privacy policies and standards for the state data
      infrastructure Establishes review criteria for the agencies information technology projects,
      procurements and purchases. (W.S 9-2-2906,(b), (iii)); and

                                                     ​
Adopts information technology policies and standards and ensures agency compliance with those
policies and standards (W.S. 9-2-2906,(b), (vi)).

Audience
This policy applies to all Executive Branch agencies, boards, and commissions staff (collectively
referred to as "agencies"). This policy is also applicable to consultants, affiliates, third party vendors
and temporary employees that use or store state data.

Definitions
Key Definitions, Acronyms, and Terms

Primary Duties:
 1.​   DUTY DESCRIPTION
       1.1.​ Implement and maintain technical security controls for data protection based on
             information classification levels and Federal regulatory requirements. (WyIT 2002, Data
             Protection for Electronic Services)​

       1.2.​   Coordinate with system administrators on control implementation, configuration
               management, and security maintenance activities.​

       1.3.​   Monitor security controls effectiveness and report security issues, incidents, and
               vulnerabilities to Data Owners and Agency Security Liaisons.​

       1.4.​   Ensure proper technical handling of data according to classification requirements and
               implement appropriate access controls and data protection measures​

       1.5.​   Implement and oversee technical aspects of media sanitization and destruction
               processes according to approved methods and classification requirements.​

       1.6.​   Implement and maintain data backup, recovery, and business continuity capabilities that
               align with classification levels and regulatory requirements.
The below table references federal audit standard requirements for ‘data owners’.

 Requirement          NIST Cybersecurity          NIST Risk Management          NIST Privacy Framework
                     Framework (CSF) 2.0          Framework (RMF) – SP                  Version 1.0
                                                          800-37 Rev. 2

    REQ-001           GV.AT-01, PR.AT-01                 AT-2, AT-3, PS-2          GV.AT-P1, PR.AT-P1

                                                      2

                                                         ​

  Requirement           NIST Cybersecurity           NIST Risk Management       NIST Privacy Framework
                       Framework (CSF) 2.0           Framework (RMF) – SP             Version 1.0
                                                              800-37 Rev. 2

    REQ-002            PR.AC-01, PR.DS-01                AC-3, SC-7, SC-8        CT.PO-P1, PR.AC-P1

    REQ-003             PR.IP-01, GV.OV-01              CM-3, CM-4, SA-10        CT.PO-P3, GV.OV-P1

    REQ-004            DE.CM-01, RS.RP-01                    SI-4, IR-4, IR-6     PR.IR-P1, DE.AE-P1

    REQ-005            PR.AC-01, PR.AC-04                AC-2, AC-3, AC-6         CT.PO-P1, CT.PO-P2

    REQ-006            PR.DS-01, PR.DS-02              SC-8, SC-12, SC-13        PR.DS-P1, PR.DS-P2

    REQ-007             PR.DS-03, PR.IP-06                   MP-6, MP-6(1-3)     PR.DS-P3, PR.DS-P4

    REQ-008             PR.IP-04, RC.RP-01              CP-9, CP-10, CP-4         PR.IP-P1, RC.RP-P1

    REQ-009             PR.IP-01, PR.IP-02              CM-2, CM-3, CM-6          PR.IP-P1, CT.PO-P3

    REQ-010            DE.CM-08, RS.MI-03                    SI-2, SI-3, RA-5    DE.AE-P2, PR.DS-P5

    REQ-011            GV.RR-01, PR.DS-01                PM-2, SC-7, AC-3        GV.RR-P1, PR.DS-P1

    REQ-012             PR.IP-01, GV.OV-03               CA-2, CA-5, CA-7        CT.PO-P5, GV.MT-P1

Audit Controls and NIST Framework Mappings:
These are the standard controls that are from prior audits.

    1.​ (REQ-001) Data Custodian Designation and Training
            a.​ Implementation. Agencies shall formally designate Data Custodians for each technical
                system or infrastructure component with documented technical responsibilities and
                ensure completion of security control training within 60 days of assignment.

                                                         3

                                              ​
      b.​ Validation. Verify Data Custodian appointments are documented with clear system
         assignments and confirm completion of required technical security training and annual
         updates.

2.​ (REQ-002) Technical Security Control Implementation
      a.​ Implementation. Data Custodians shall implement appropriate technical security
         controls based on information classification levels, including access controls, encryption,
         monitoring, and data protection measures as specified by Data Owners.
      b.​ Validation. Audit security control implementation against classification requirements and
         verify controls are properly configured, tested, and documented.

3.​ (REQ-003) System Administration Coordination
      a.​ Implementation. Data Custodians shall coordinate with system administrators on
         security control implementation, configuration changes, and maintenance activities to
         ensure security measures remain effective and properly integrated.
      b.​ Validation. Review coordination documentation and verify that security considerations
         are properly integrated into system administration activities and change management
         processes.

4.​ (REQ-004) Security Monitoring and Incident Response
      a.​ Implementation. Data Custodians shall implement continuous monitoring of security
         controls, detect security incidents and vulnerabilities, and report issues to Data Owners
         and Agency Security Liaisons within established timeframes.
      b.​ Validation. Assess monitoring system effectiveness and verify incident reporting meets
         established timelines and documentation requirements.

5.​ (REQ-005) Access Control Management
      a.​ Implementation. Data Custodians shall implement and maintain access control systems
         that enforce classification-based permissions, user authentication, and authorization
         controls as defined by Data Owners.
      b.​ Validation. Audit access control configurations, review user access logs, and verify that
         permissions align with classification levels and approved access criteria.

                                               4

                                              ​
6.​ (REQ-006) Encryption and Data Protection
      a.​ Implementation. Data Custodians shall implement appropriate encryption for data at rest
         and in transit based on classification levels, including FIPS 140-2 validated encryption
         for Confidential-Regulated information as required.
      b.​ Validation. Verify encryption implementation meets classification requirements and
         regulatory standards, and audit encryption key management practices.

7.​ (REQ-007) Media Sanitization Technical Implementation
      a.​ Implementation. Data Custodians shall technically implement approved media
         sanitization methods (Clear, Purge, Destroy) according to Data Owner approvals and
         ensure proper execution of sanitization procedures based on classification levels.
      b.​ Validation. VAudit sanitization implementation processes and verify that technical
         procedures meet NIST SP 800-88 guidelines and classification-based requirements.

8.​ (REQ-008) Backup and Recovery Operations
      a.​ Implementation. Data Custodians shall implement and maintain data backup and
         recovery systems that protect classified information according to established
         requirements and ensure business continuity capabilities align with data sensitivity
         levels.
      b.​ Validation. Test backup and recovery procedures regularly and verify that backup data
         receives appropriate classification-based protection and access controls.

9.​ (REQ-009) Configuration Management
      a.​ Implementation. Data Custodians shall maintain secure system configurations,
         implement configuration baselines, and manage security-related configuration changes
         through established change control processes.
      b.​ Validation. Audit configuration management processes and verify that security baselines
         are maintained and changes are properly reviewed and approved.

10.​(REQ-010) Vunerability Management
      a.​ Implementation. Data Custodians shall implement vulnerability scanning, assessment,
         and remediation processes appropriate to the classification levels of data handled by

                                              5

                                                  ​
             their systems and coordinate remediation activities with Data Owners.
          b.​ Validation. Review vulnerability management processes and verify that vulnerabilities
             are identified, assessed, and remediated within timeframes appropriate to data
             sensitivity and regulatory requirements.

   11.​(REQ-011) Regulatory Technical Compliance
          a.​ Implementation. Data Custodians supporting Confidential-Regulated information shall
             implement technical controls that meet specific regulatory requirements (HIPAA, FERPA,
             IRS 1075, CJIS, PCI DSS) and maintain compliance documentation.
          b.​ Validation. Audit regulatory compliance implementation and verify that technical controls
             meet or exceed regulatory requirements for each applicable standard.

   12.​(REQ-012) Security Control Testing and Validation
          a.​ Implementation. Data Custodians shall conduct regular testing and validation of security
             controls, document control effectiveness, and coordinate with Data Owners on control
             assessment results and improvement recommendations.
          b.​ Validation. Review security control testing documentation and verify that testing occurs
             at required frequencies and results are properly communicated to Data Owners.

Applicable State Policies, Federal, State or Industry Rules, Laws, and/or Regulations

   1.​ WyIT 2001, Information Classification
   2.​ WyIT 2001-S1, Data Owner Standard
   3.​ WyIT 2001-S2, Data Steward Standard
   4.​ WyIT 2001-S4, Data Domain Standard
   5.​ WyIT 2001-G1, Information Classification Guide
   6.​ WyIT 2001-G2, Information Classification Procedures Guide
   7.​ WyIT 2002, Data Protection for Electronic Government Services
   8.​ WyIT 2013, Electronic Data Destruction and Sanitization
   9.​ WyIT 3015, Physical Media
   10.​NIST Cybersecurity Framework (CSF) 2.0
   11.​NIST Risk Management Framework (RMF) – SP 800-37 Rev. 2
   12.​NIST Privacy Framework Version 1.0

                                                  6

                                                        ​
Compliance & Exceptions:
Compliance
 This document supports an established policy, so there are no compliance requirements.

Exceptions
 Since standards are not held to a compliance standard, there are no exceptions to this standard.

Review/Approval:
Date Issued/Review Date
This policy shall be reviewed at least annually and updated / reviewed / approved as defined in the
Office of Chief Information Officer (OCIO) Policy lifecycle.

The review and update process shall be coordinated by Governance, Risk and Compliance (GRC),
completed by the policy owner and approved through the OCIO policy review workflow.

Approval
This policy as signed by the appropriate officer (listed below) is considered approved and enforced, per
Wyoming State Statutes (W.S 9-2-2906,(b), (iii)) and (W.S. 9-2-2906,(b), (vi)).

To obtain a signed copy of this document, contact Enterprise Technology Services Governance,
Risk and Compliance (ets-ocio-grc@wyo.gov).

 Jeffrey Clines                                                    Chief Information Officer
 Officer Name                                                      Officer Title

 Officer’s Signature                                               Date

Revision History
The current version of this policy, as identified in the Revision History below, supersedes all previous documents
listed below.

 Version        Change                                          Author(s)                  Date of Change
 2026-09.1      ETS Director signature                          GRC                        September 2026
 2025-09.1      Original Document                               Pat Potter, Deputy CDO     September 2025

                                                         7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). effective_date is the Effective Date cell of the file's header table, as printed. source_version is the Policy Version (or Document Version) cell of the header table, as printed.
