---
schema_version: 1
corpus: states-government-it
jurisdiction: wyoming
id: wy-wyit-2001-s2
title: Data Steward Standard
doc_type: standard
citation: WyIT 2001-S2
authority_level: ''
issuing_body: Wyoming Department of Enterprise Technology Services (Office of the Chief Information Officer)
source_url: https://drive.google.com/uc?export=download&id=1tzpDWV1eV8v7tNy8CDpohZj3PibHH0mE
source_format: pdf
retrieved: '2026-11-12'
source_sha256: fba2c7d8f51df0a6fc12a7a5e9e0a0cb37ee4e90cc06eb137ff3ef60148fb7ae
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

# Data Steward Standard (WyIT 2001-S2)

## At a glance

WyIT 2001-S2, Data Steward Standard: a statewide standard in the Enterprise Technology Services policy library. Per the Applicability section of the file it applies to all Executive Branch agencies, boards and commissions staff and to consultants, affiliates and temporary employees.

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
This standard establishes the requirements and duties for Data Steward functions to ensure consistent
day-to-day information classification, labeling, and handling in compliance with Wyoming information
management policies..

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
       1.1.​ Perform day-to-day classification of information assets according to established
             classification criteria and organizational sensitivity levels.​

       1.2.​   Apply appropriate classification labels and ensure proper handling procedures are
               followed for all information assets.​

       1.3.​   Maintain consistency of classification decisions within assigned data domains and
               identify classification discrepancies.​

       1.4.​    Document classification decisions with appropriate justifications and maintain
               classification decision records.​

       1.5.​   Identify when aggregated data requires higher classification levels and recommend
               appropriate reclassification.​

       1.6.​   Conduct annual reviews of classifications and provide recommendations for adjustments
               to Data Owners.​

The below table references federal audit standard requirements for ‘data owners’.

Requirement          NIST Cybersecurity          NIST Risk Management               NIST Privacy
                    Framework (CSF) 2.0          Framework (RMF) – SP          Framework Version 1.0
                                                         800-37 Rev. 2

   REQ-001           GV.AT-01, GV.RR-02              AT-2, AT-3, PS-2           GV.AT-P1, GV.PO-P3

                                                      2

                                                     ​

Requirement         NIST Cybersecurity        NIST Risk Management              NIST Privacy
                   Framework (CSF) 2.0        Framework (RMF) – SP        Framework Version 1.0
                                                         800-37 Rev. 2

   REQ-002          ID.AM-05, GV.SC-01                    RA-2, CM-2         ID.IM-P1, ID.IM-P2

   REQ-003          PR.DS-02, ID.AM-05                   MP-3, MP-4         PR.DS-P1, PR.DS-P2

   REQ-004          GV.OC-01, ID.AM-05                    PM-5, RA-2        GV.PO-P2, ID.IM-P3

   REQ-005          GV.OC-02, ID.AM-01                   PM-5, CM-2         GV.PO-P2, ID.IM-P3

   REQ-006          ID.RA-01, GV.SC-01                    RA-2, RA-3         ID.RA-P1, ID.IM-P2

   REQ-007          GV.RM-01, ID.RA-01                    CA-2, RA-3        GV.MT-P1, ID.RA-P1

   REQ-008          PR.AT-01, GV.AT-01                    AT-2, AT-4        CT.PO-P4, GV.AT-P1

   REQ-009          PR.DS-03, GV.SC-02                   MP-6, MP-4         PR.DS-P3, PR.DS-P4

   REQ-010         DE.CM-01, RS.CO-02                      IR-6, IR-8       PR.IR-P1, GV.MT-P2

   REQ-011          GV.RR-01, GV.SC-02                    PM-2, CA-2        GV.RR-P1, GV.RR-P2

Audit Controls and NIST Framework Mappings:
These are the standard controls from prior audits.

   1.​ (REQ-001) Data Steward Designation and Training
           a.​ Implementation. Agencies shall formally designate Data Stewards for each data domain
              with documented responsibilities and ensure completion of classification training within
              60 days of assignment.

                                                     3

                                                 ​
      b.​ Validation. Verify Data Steward appointments are documented with clear domain
          assignments and confirm completion of required training and annual refresher courses.

2.​ (REQ-002) Daily Classification Operations
      a.​ Implementation. Data Stewards shall classify new information assets within 5 business
          days of creation or acquisition using established classification criteria (Public, Internal,
          Confidential-Standard, Confidential-Regulated).
      b.​ Validation. Audit classification timeliness and accuracy through random sampling and
          verify adherence to classification criteria and documentation standards.

3.​ (REQ-003) Classification Labeling and Handling
      a.​ Implementation. Data Stewards shall apply appropriate classification labels to all
          information assets and ensure proper handling procedures are communicated to users
          and documented in accessible formats.
      b.​ Validation. Review labeling consistency across data domains and verify that handling
          procedures align with classification levels and regulatory requirements.

4.​ (REQ-004) Classification Decision Documentation
      a.​ Implementation. Data Stewards shall document all classification decisions with
          justifications, including sensitivity assessment rationale, regulatory considerations, and
          aggregation impact analysis.
      b.​ Validation. Audit classification documentation for completeness and verify that decision
          rationale aligns with organizational classification criteria.

5.​ (REQ-005) Data Domain Consistency Management
      a.​ Implementation. Data Stewards shall maintain consistency of classification decisions
          within their assigned data domains and identify inconsistencies or discrepancies
          requiring resolution.
      b.​ Validation. Conduct cross-domain consistency reviews and verify that similar data types
          receive consistent classification across organizational units.

6.​ (REQ-006) Aggregation Impact Assessment
      a.​ Implementation. Data Stewards shall evaluate when combining or aggregating data

                                                 4

                                                 ​
          elements requires higher classification levels and recommend appropriate
          reclassification to Data Owners.
      b.​ Validation. Review aggregation assessments for accuracy and verify that
          recommendations properly consider cumulative sensitivity and regulatory implications.

7.​ (REQ-007) Annual Classification Review Process
      a.​ Implementation. Data Stewards shall conduct comprehensive annual reviews of all
          classifications within their domains and provide documented recommendations for
          adjustments based on changing sensitivity or requirements.
      b.​ Validation. Verify completion of annual reviews within required timeframes and assess
          quality of recommendations provided to Data Owners.

8.​ (REQ-008) User Training and Communication
      a.​ Implementation. Data Stewards shall communicate classification requirements and handling
          procedures to data users and provide guidance on proper information handling based on
          classification levels.
      b.​ Validation. Assess effectiveness of user communication through feedback surveys and verify
          that users understand classification requirements for their assigned data.

9.​ (REQ-009) Media Sanitization Support
      a.​ Implementation. Data Stewards shall identify media containing classified information
          requiring sanitization and coordinate with Data Owners on appropriate sanitization
          methods based on classification levels.
      b.​ Validation. Verify proper identification of media requiring sanitization and confirm
          coordination with Data Owners meets established timelines and procedures.

10.​(REQ-010) Classification Incident Reporting
      a.​ Implementation. Data Stewards shall identify and report potential misclassification
          incidents, unauthorized disclosures, or classification policy violations to Data Owners
          and appropriate security personnel.
      b.​ Validation. Review incident reporting processes and verify that incidents are identified,
          documented, and escalated according to established procedures.

                                                  5

                                                   ​

   11.​(REQ-011) Regulatory Classification Support
           a.​ Implementation. Data Stewards handling Confidential-Regulated information shall
              maintain awareness of applicable regulatory requirements and ensure classification
              decisions support regulatory compliance obligations.
           b.​ Validation. Verify Data Steward understanding of applicable regulations through testing
              and audit classification decisions for regulatory compliance alignment.

Applicable State Policies, Federal, State or Industry Rules, Laws, and/or Regulations

   1.​ WyIT 2001, Information Classification
   2.​ WyIT 2001-S1, Data Owner Standard
   3.​ WyIT 2001-S3, Data Custodian Standard
   4.​ WyIT 2001-S4, Data Domain Standard
   5.​ WyIT 2001-G1, Information Classification Guide
   6.​ WyIT 2001-GL2, Information Classification Procedures Guide
   7.​ WyIT 2002, Data Protection for Electronic Government Services
   8.​ WyIT 2013, Electronic Data Destruction and Sanitization

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

                                                   6

                                                        ​
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
