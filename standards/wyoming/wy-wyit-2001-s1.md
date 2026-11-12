---
schema_version: 1
corpus: states-government-it
jurisdiction: wyoming
id: wy-wyit-2001-s1
title: Data Owner Standard
doc_type: standard
citation: WyIT 2001-S1
authority_level: ''
issuing_body: Wyoming Department of Enterprise Technology Services (Office of the Chief Information Officer)
source_url: https://drive.google.com/uc?export=download&id=1toSZpeB_m8YKjmczFgcwY0__XgRiomv8
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 09396dd129de82a1fdaf34ba7c3dea3786ed4407663b4c3c8daa72220197a5e2
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

# Data Owner Standard (WyIT 2001-S1)

## At a glance

WyIT 2001-S1, Data Owner Standard: a statewide standard in the Enterprise Technology Services policy library. Per the Applicability section of the file it applies to all Executive Branch agencies, boards and commissions staff and to consultants, affiliates and temporary employees.

## Full text

Data Owner Standard
WyIT.2001-S1

 Document Owner         Department of Enterprise Services, Data Privacy
 Document Contact       Pat Potter, Deputy Chief Data Officer
 Document Approver      Wyoming Data Governance Committee (WDGC)
 Effective Date         September 12, 2025
 Next Review Date       April 1, 2027
 Document Version       2026-09.1
 Associated Policy      WyIT 2001, Information Classification

​
Introduction:
A Data Owner is identified, and assigned by the Agency Director or their designee to be the key
resource that understands what data is collected, how and where it is stored, who has access to it, and
how and when it should be retired. This Data Owner’s key roles and responsibilities are defined herein.

This standard establishes the requirements and duties for Data Owner functions to ensure proper
information classification, protection, and governance in compliance with Wyoming information
management policies.

Data Owners should be identified for all data domains in the agency. Data domains included both
structured and unstructured.

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
 1.​   DATA OWNER IDENTIFICATION​

       1.1.​   The Agency will identify Data Owner(s) that will have the primary responsibility to
               understand state data classifications, related access and management requirements and
               final approval for classification decisions.

 2.​   DATA OWNER RESPONSIBILITIES
       2.1.​ Understand state data classifications, related access and management requirements
             and final approval for classification decisions.​

       2.2.​   Approve classification decisions for information assets under their authority according to
               organizational sensitivity levels and regulatory requirements.​

       2.3.​   Establish and maintain access control criteria and approval processes for each
               classification level of assigned data domains. (WyIT 3005, Access Controls)​

       2.4.​   Ensure understanding, application, and auditing of applicable federal and state
               regulations for regulated information assets.​

       2.5.​   Identify, document, and maintain oversight of logical data domains that group related
               data types for consistent governance​

       2.6.​   Verify that technical and administrative controls are properly implemented according to
               classification requirements.​

       2.7.​   Ensure oversight of Data Stewards and all controls and that all controls are followed and
               meet or exceed Agency business requirements.​

       2.8.​   Approve appropriate sanitization and destruction methods based on information
               classification levels and regulatory requirements.​

                                                      2

                                                ​
      2.9.​   Define the roles of Data Steward and Data Custodian for each data domain they are
              responsible for.
The below table references federal audit standard requirements for ‘data owners’.

 Requirement        NIST Cybersecurity       NIST Risk Management            NIST Privacy
                   Framework (CSF) 2.0       Framework (RMF) – SP       Framework Version 1.0
                                                     800-37 Rev. 2

   REQ-001         GV.RR-02, GV.OC-01           PM-5, AT-2, PS-2         GV.PO-P1, GV.PO-P3

   REQ-002          ID.AM-05, GV.SC-01                RA-2, PM-2           ID.IM-P1, ID.IM-P2

   REQ-003         PR.AC-01, GV.PO-01                 AC-2, AC-3          CT.PO-P1, CT.PO-P2

   REQ-004         GV.RR-01, GV.SC-02                 PM-2, CA-2         GV.RR-P1, GV.RR-P2

   REQ-005          ID.AM-01, GV.OC-02                PM-5, RA-3          ID.IM-P3, GV.PO-P2

   REQ-006          PR.IP-01, GV.OV-01                CA-5, CA-6         CT.PO-P3, PR.PO-P1

   REQ-007          PR.AT-01, GV.AT-01                AT-2, AT-3          CT.PO-P4, GV.AT-P1

   REQ-008          ID.RA-01, GV.RM-01                RA-3, CA-2          ID.RA-P1, GV.MT-P1

   REQ-009         PR.DS-03, GV.SC-01                MP-6, MP-6(1)       PR.DS-P1, PR.DS-P2

   REQ-010         PR.DS-03, GV.SC-02                MP-6(8), SA-9       PR.DS-P3, GV.PO-P4

   REQ-011         GV.RR-01, PR.DS-03           MP-6(2), MP-6(3)         GV.RR-P2, PR.DS-P4

                                                 3

                                                     ​
Audit Controls and NIST Framework Mappings:
These are the standard controls from prior audits.

   1.​ (REQ-001) Data Owner Designation and Training
           a.​ Implementation. Each agency shall identify and formally designate Data Owners for all
              information collections, with documented authority and responsibility scope.
           b.​ Validation. Verify Data Owner appointments are documented, current, and include
              completed information classification training within 90 days.

   2.​ (REQ-002) Information Asset Classification
           a.​ Implementation. Data Owners shall classify all information assets under their authority
              using established classification levels (Public, Internal, Confidential-Standard,
              Confidential-Regulated) based on sensitivity and regulatory requirements.
           b.​ Validation. Audit classification decisions annually and verify documentation of
              classification rationale and regulatory considerations.

   3.​ (REQ-003) Access Control Criteria Development
           a.​ Implementation. Data Owners shall establish and document access control criteria for
              each classification level, including approval authorities and access review requirements.
           b.​ Validation. Review access control criteria documentation and verify implementation
              through access control system configuration audits.

   4.​ (REQ-004) Regulatory Compliance Management
           a.​ Implementation. Data Owners of Confidential-Regulated information shall maintain
              current knowledge of applicable regulations and coordinate with technical teams on
              control implementation.
           b.​ Validation. Verify Data Owner completion of regulation-specific training and
              documentation of compliance control mapping.

   5.​ (REQ-005) Data Domain Documentation
           a.​ Implementation. Data Owners shall identify and document data domains under their
              authority, grouping related data types for consistent classification and governance
              decisions.

                                                     4

                                               ​
      b.​ Validation. Review data domain documentation for completeness and verify consistency
          of classification decisions within domains.

6.​ (REQ-006) Control Implementation Oversight
      a.​ Implementation. Data Owners shall verify that appropriate technical and administrative
          controls are implemented according to information classification levels and coordinate
          with IT custodians on control effectiveness.
      b.​ Validation. Conduct quarterly control effectiveness reviews and verify Data Owner
          sign-off on control implementation validation.

7.​ (REQ-007) Staff Training Coordination
      a.​ Implementation. Data Owners shall ensure all employees and affiliates with access to
          their data receive appropriate information handling training based on classification
          levels.
      b.​ Validation. Verify training completion records and assess staff understanding through
          periodic testing or review.
8.​ (REQ-008) Classification Review and Updates
      a.​ Implementation. Data Owners shall conduct annual reviews of information
          classifications and approve reclassification requests based on changing sensitivity or
          regulatory requirements.
      b.​ Validation. Review classification change documentation and verify approval workflow
          compliance.

9.​ (REQ-009) Media Sanitization Method Approval
      a.​ Implementation. Data Owners shall approve appropriate sanitization methods (Clear,
          Purge, or Destroy) for electronic media based on information classification levels and
          intended disposition (internal reuse, agency transfer, or external disposal).
      b.​ Validation. Verify Data Owner approval documentation for all media sanitization
          activities and audit compliance with classification-based disposal requirements.​

10.​(REQ-0100) Destruction Vendor Management
      a.​ Implementation. Data Owners shall approve qualified vendors for media destruction
          services when verification is required and ensure certificates of destruction are obtained

                                               5

                                                   ​
             that detail method, date, location, and witness information.
          b.​ Validation. Review vendor qualification documentation, destruction certificates, and
             verify Data Owner approval for all external destruction activities.​

   11.​(REQ-011) Regulatory Sanitization Compliance
          a.​ Implementation. Data Owners of Confidential-Regulated information shall identify
             applicable federal and state regulations governing media sanitization and ensure
             compliance with specific destruction requirements (HIPAA, FERPA, IRS 1075, CJIS, PCI
             DSS).
          b.​ Validation. Audit regulatory compliance documentation and verify sanitization methods
             meet or exceed regulatory requirements for each applicable standard

Applicable State Policies, Federal, State or Industry Rules, Laws, and/or Regulations

   1.​ WyIT 2001, Information Classification
   2.​ WyIT 2001-S2, Data Steward Standard
   3.​ WyIT 2001-S3, Data Custodian Standard
   4.​ WyIT 2001-S4, Data Domain Standard
   5.​ WyIT 2001-G1, Information Classification Guide
   6.​ WyIT 2001-GL2, Information Classification Procedures Guide
   7.​ WyIT 2002, Data Protection for Electronic Government Services
   8.​ WyIT 2013, Electronic Data Destruction and Sanitization
   9.​ WyIT 3005, Access Controls
   10.​NIST Cybersecurity Framework (CSF) 2.0
   11.​NIST Risk Management Framework (RMF) – SP 800-37 Rev. 2
   12.​NIST Privacy Framework Version 1.0

Compliance & Exceptions:
Compliance
This document supports an established policy, so there are no compliance requirements.

Exceptions
Since standards are not held to a compliance standard, there are no exceptions to this standard.

                                                   6

                                                        ​
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
