---
schema_version: 1
corpus: states-government-it
jurisdiction: wyoming
id: wy-wyit-2001-g2
title: Data Classification Procedures Guide
doc_type: policy
citation: WyIT 2001-G2
authority_level: ''
issuing_body: Wyoming Department of Enterprise Technology Services (Office of the Chief Information Officer)
source_url: https://drive.google.com/uc?export=download&id=1KigL9P3SRMetSZ5XjVn5WNgiyRs-5hYj
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 7f1c7cd67c8e581356e206015bca3edcd16070652f147678acf9fe59204661f4
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

# Data Classification Procedures Guide (WyIT 2001-G2)

## At a glance

WyIT 2001-G2, Data Classification Procedures Guide: a statewide guide in the Enterprise Technology Services policy library. Per the Applicability section of the file it applies to all Executive Branch agencies, boards and commissions staff and to consultants, affiliates and temporary employees.

## Full text

Data Classification Procedures Guide
WyIT.2001-G2

 Policy Owner           Drew Dilly, Chief Data Officer
 Policy Contact         Pat Potter, Deputy Chief Data Officer
 Policy Approver        Jeff Clines, Chief Information Officer
 Effective Date         September 12, 2025
 Next Review Date       April 1, 2027
 Policy Version         2026-09.1
 Associated Policy      WyIT 2001, Information Classification

​
Introduction:
This guide provides detailed information regarding Information Classification, supporting WyIT 2001,
Information, to support Wyoming state agencies in properly classifying state information.

This standard applies to all Executive Branch agencies, boards, and commissions staff (collectively
referred to as "agencies"). This standard is also applicable to consultants, affiliates, third party vendors
and temporary employees that use or store data.​

Authority
This guideline is promulgated under the authority of Wyoming State Statute 9-2-2906 and its
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

Data Governance Roles
   ●​ Data Owner

         o​ The agency or program with statutory authority and ultimate responsibility for the data.
         o​ Determines access rights and establishes controls.
   ●​ Data Custodian

         o​ Individual or entity responsible for the storage, maintenance, and technical safeguarding
            of data.
   ●​ Data Steward

           o​ Individual(s) appointed by the Data Owner to be responsible for proper data
              classification, quality, and management practices.
Other Key Concepts
   ●​ Classification Inheritance

        o​ The process by which compiled or derivative information takes on the highest
            classification level of any component information.
        o​ When information consists of elements with different classification levels, the entire
            information asset shall be classified at the highest level of any component element.
   ●​ Aggregated Data

           o​ Collections of data elements from multiple sources that may require higher classification
              than individual elements due to revealing patterns or sensitive insights when combined.
           o​ Agencies must consider whether aggregated data requires higher classification than its
              component parts due to mosaic effects or inference risks.

Detailed Classification System:
 1.​   INITIAL CLASSIFICATION
       1.1.​ Data Stewards shall classify information at creation or acquisition.​

       1.2.​   Classification decisions shall be documented with justification.

       1.3.​   When classifying information, consider the following factors:
               1.3.1.​ Sensitivity of the information and privacy implications;

                                                      2

                                                   ​

              1.3.2.​   Applicable legal and regulatory requirements (state and federal);

              1.3.3.​   Potential impact if disclosed, modified, or unavailable;

              1.3.4.​   Aggregation effects when combined with other information;

              1.3.5.​   Business value and operational importance;

              1.3.6.​   Temporal sensitivity (does classification change over time?);

              1.3.7.​   Public disclosure requirements under W.S. §16-4-201 through §16-4-205);

              1.3.8.​   Contractual obligations regarding confidentiality;

              1.3.9.​   Relationship to other classified information.​

2.​   RECLASSIFICATION
      2.1.​ Data Stewards shall review classifications at least annually.​

      2.2.​   Classification changes must be documented with justification.​

      2.3.​   When reclassifying to a lower level, written approval from the Data Owner is required.​

      2.4.​   Consider changes in business context, regulatory environment, or aggregation effects.

3.​   CLASSIFICATION DISPUTE RESOLUTION
      3.1.​ If agencies disagree on the classification of shared information, the higher classification
            shall apply until it is resolved.​

      3.2.​   Confidential-Standard information is sensitive business or operational information.

              3.2.1.​   Example data types: security plans, sensitive strategic plans, contract
                        negotiations, legal opinions, processing volumes, service pricing, equipment
                        configurations, vendor information, application software configurations, and
                        other similar business and technical information.​

              3.2.2.​   The Wyoming Data Governance Council shall serve as the final arbiter for
                        classification disputes between agencies.

4.​   AUTOMATED CLASSIFICATION SUPPORT
      4.1.​ Agencies are encouraged to implement data discovery tools to identify potentially
            sensitive information.​

      4.2.​   Where feasible, automated classification suggestions should be used to supplement
              manual classification decisions.​

                                                   3

                                                   ​
      4.3.​   Classification metadata should be embedded in document properties where technically
              possible.​

      4.4.​   Visual labels or watermarks should be added to documents according to their
              classification level.

5.​   CLASSIFICATION DECISION TREE
      5.1.​ Would disclosure of this information violate federal or state law, regulations, or
            contractual obligations?​

              5.1.1.​   YES → Classify as CONFIDENTIAL (determine appropriate subcategory)​

              5.1.2.​   NO → Continue to question 5.2​

      5.2.​   Would disclosure of this information potentially harm individuals, compromise
              operations, damage the State's reputation, or create financial/legal liability?​

              5.2.1.​   YES → Classify as CONFIDENTIAL (determine appropriate subcategory)​

              5.2.2.​   NO → Continue to question 5.3​

      5.3.​   Is this information intended for unrestricted public disclosure?​

              5.3.1.​   YES → Classify as PUBLIC​

              5.3.2.​   NO → Classify as INTERNAL​

      5.4.​   For information that does not have a pre-determined classification by statute or
              regulation, use the following decision path:
              (When in doubt, classify at the higher level until a definitive determination can be made)​

6.​   LABELING REQUIREMENTS
      6.1.​ All information should be clearly labeled with its classification level.​

      6.2.​   Unlabeled information shall be considered "Internal" by default unless otherwise
              specified in W.S. §16-4-203.​

      6.3.​   Where technically feasible, use headers, footers, watermarks, or metadata to indicate
              classification.​

      6.4.​   Classification labels should be clearly visible and easily understood.

                                                    4

                                                  ​
7.​   HANDLING PRACTICES BY CLASSIFICATION LEVEL
      7.1.​ Public Information​

              7.1.1.​   No special handling requirements beyond normal good practices.​

              7.1.2.​   Can be freely distributed within and outside the organization.​

              7.1.3.​   No restrictions on storage or transmission methods.​

      7.2.​   Internal Information​

              7.2.1.​   Should not be disclosed to external parties without appropriate review.

              7.2.2.​   Use standard security controls for systems containing internal information.

              7.2.3.​   Transmission via standard email is acceptable.

              7.2.4.​   Can be stored on state-managed systems without encryption​

      7.3.​   Confidential Information
               7.3.1.​ Access strictly limited to authorized individuals with a need to know.

              7.3.2.​   Strong access controls required for all systems containing confidential
                        information.

              7.3.3.​   Encryption required for storage and transmission.

              7.3.4.​   Physical documents should be stored in locked containers when not in use.

              7.3.5.​   Sharing requires appropriate approvals and secure methods.​

              7.3.6.​   Special handling procedures may apply for regulated data types.​

8.​   IMPLEMENTATION APPROACH
      8.1.​ Agencies should implement this classification framework using the following phased
            approach:​
            ​
            (Agencies should adjust these timelines based on their size, complexity, and available
            resources.)​

      8.2.​   Phase 1: Foundation (0-3 months)​

              8.2.1.​   Educate key stakeholders on classification levels and data domains;

              8.2.2.​   Identify and document core data domains (3-5 initial domains);

                                                   5

                                               ​

        8.2.3.​   Designate Data Owners and Data Stewards for each domain;

        8.2.4.​   Inventory critical information assets within each domain;

        8.2.5.​   Develop agency-specific classification procedures (if needed).​

8.3.​   Phase 2: Classification (3-6 months)​

        8.3.1.​   Classify critical information assets starting with high-value, high-risk domains;

        8.3.2.​   Implement labeling for classified information;

        8.3.3.​   Establish access controls aligned with classification levels;

        8.3.4.​   Develop monitoring mechanisms to verify proper classification;

        8.3.5.​   Conduct initial training for all staff.​

8.4.​   Phase 3: Integration (6-12 months)
        8.4.1.​   Expand classification to all remaining information assets;

        8.4.2.​   Integrate classification with related policies (retention, sharing, encryption);

        8.4.3.​   Implement automated tools to support classification where feasible;

        8.4.4.​   Conduct compliance verification through sampling and review;

        8.4.5.​   Refine and expand data domains based on experience.​

8.5.​   Phase 4: Maturity (12+ months)​

        8.5.1.​   Establish regular review cycles for classifications and domains;

        8.5.2.​   Implement metrics and reporting on classification effectiveness;

        8.5.3.​   Automate classification where possible;

        8.5.4.​   Conduct advanced training for specialized roles;

        8.5.5.​   Share best practices across agencies.

                                                6

                                                ​
Data Handling Requirements by Classification Level:

Requirement                    Public                  Internal             Confidential
Access                  No restrictions         Basic authentication   Strong authentication +
Controls                                                               authorization
Storage Encryption      Not required            Not required           Required
Transmission            Not required            Recommended            Required
Encryption
Labeling                Optional                Required               Required with
                                                                       subcategory
 Sharing              Not required            Manager approval        Data Owner approval
 Approval
 Storage              Any approved            State-managed           Secured state systems
 Location             system                  systems                 only
 Remote               Permitted               Permitted               With additional controls
 Access
 Disposal             Standard deletion       Clearing                Purging or destruction
 Methods
 Audit                Not required            Basic                   Comprehensive
 Logging
 Backup               Standard                Standard                Enhanced
 Requirements
Note on Retention Requirements: Classification levels do not automatically determine retention
periods for information. Agencies must follow appropriate retention schedules as established by
the Wyoming State Archives.
However, classification levels should inform storage methods and security controls throughout
the retention period.

Applicable State Policies, Federal, State or Industry Rules, Laws, and/or Regulations

    1.​ WyIT 2001, Information Classification
    2.​ WyIT 2001-S1, Data Owner Standard
    3.​ WyIT 2001-S2, Data Steward Standard
    4.​ WyIT 2001-S3, Data Custodian Standard
    5.​ WyIT 2001-S4, Data Domain Standard
    6.​ WyIT 2001-GL1, Information Classification Procedures Guide

                                                 7

                                                   ​
   7.​ WyIT-2004, Information Breach, Disclosure or Data Leak
   8.​ WyIT 2004-GL, Information Breach Response Guide
   9.​ WyIT-2005, Information Residency and Transportation
   10.​WyIT-2006, Agency Official for Privacy (AOP)
   11.​WyIT-2011, Wyoming State Data Collection, Transparency, and Consent
   12.​WyIT-2013, Electronic Data Destruction and Sanitization
   13.​WyIT 2014, Data Sharing Agreement Documentation and Governance

Compliance & Exceptions:
Compliance
This document supports an established policy, so there are no compliance requirements.

Exceptions
Since guides are not held to a compliance standard, there are no exceptions to this standard.

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

 Jeffrey Clines                                             Chief Information Officer
 Officer Name                                               Officer Title

 Officer’s Signature                                        Date

                                                   8

                                                        ​
​
​

Revision History
The current version of this policy, as identified in the Revision History below, supersedes all previous documents
listed below.

    Version     Change                                                         Author(s)         Date of Change
    2026-09.1   ETS Director signature                                           GRC               September
                                                                                                      2026
    2025-09.0   WyIT 2001-G1, Information Classification Guide,               Pat Potter           September
        1       Updated Document Template                                    Deputy CDO               2025
     October    WyIT 2001-GL, Information Classification Guideline          Wyoming Data          August 2024
      2022      Replaced by                                                  Governance
                ●​ WyIT 2001-S1, Data Owner Standard                         Committee
                ●​ WyIT 2001-S2, Data Steward Standard
                ●​ WyIT 2001-S3, Data Custodian
                ●​ WyIT 2001-S4, Data Domain Standard

                WyIT 2001-S, Information Classification Standard
                Replaced by
                ●​ WyIT 2001-S1, Data Owner Standard                     Wyoming Data
      UKN       ●​ WyIT 2001-S2, Data Steward Standard                   Governance                August 2024
                ●​ WyIT 2001-S3, Data Custodian                          Committee
                ●​ WyIT 2001-S4, Data Domain Standard

      UKN       08100-P131, Policy Information Classification            UKN                     November 2018
                Replaced by
                ●​ WyIT 2001-S, Information Classification Standard
                ●​ WyIT 2001-GL, Information Classification
                   Guideline

      UKN       08100-S131, Information Classification Standard          UKN                         May 2018
                Replaced by
                ●​ WyIT 2001-S, Information Classification Standard
                ●​ WyIT 2001-GL, Information Classification
                   Guideline​

                                                         9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). effective_date is the Effective Date cell of the file's header table, as printed. source_version is the Policy Version (or Document Version) cell of the header table, as printed.
