---
schema_version: 1
corpus: states-government-it
jurisdiction: delaware
id: de-in-dataclass-001
title: Data Classification Policy
doc_type: policy
citation: DTI Enterprise Policy IN-DataClass-001
authority_level: ''
issuing_body: Delaware Department of Technology and Information (DTI)
source_url: https://webfiles.dti.delaware.gov/pdfs/pp/DataClassificationPolicy.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 09e7d94e9eb9f09cb70ab85ad81c163c019075db2ca13cbdc986d6af7b438f59
effective_date: '2006-03-01'
source_version: Revision 3 (reviewed 02/26/2024)
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
- data
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Data Classification Policy (DTI Enterprise Policy IN-DataClass-001)

## At a glance

Item of the DTI Standards and Policies library, section 'Information'. Synopsis as printed: The goal of this policy is to enhance the State’s ability to protect data and information through data classification.

## Full text

                                                       STATE OF DELAWARE
                                         DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                     801 Silver Lake Blvd.
                                                    Dover, Delaware 19904

Doc Ref Number:     IN-DataClass-001                                 Revision Number: 3
Document Type:      Enterprise Policy                                    Page: 1 of 9
    Policy Title:   Data Classification Policy

      Synopsis:     The goal of this policy is to enhance the State’s ability to protect data
                    and information through data classification.
      Authority:    Title 29 Chapter 90C Delaware Code, §9004C – General Powers,
                    duties and functions of DTI “2) Create, implement and enforce
                    statewide and agency technology solutions, policies, standards and
                    guidelines, including as recommended by the CIO”
   Applicability:   This Policy is applicable to all users of the State of Delaware
                    communications and computing resources. DTI is an Executive
                    Branch Agency and has no authority over the customers in Legislative
                    and Judicial Branches, as well as Local Education Agencies, and other
                    Federal and Local Government entities that use these resources.
                    However, all users, including these entities, must agree to abide by
                    all policies, standards promulgated by DTI as a condition of access
                    and continued use of these resources.
      Effective:    3/1/2006
     Reviewed:      02/26/2024
   Approved By:     Chief Information Officer
       Sponsor:     Chief Security Officer

                       “Delivering Technology that Innovates”

                                                           STATE OF DELAWARE
                                               DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                         801 Silver Lake Blvd.
                                                        Dover, Delaware 19904

      Doc Ref Number:      IN-DataClass-001                             Revision Number: 3
       Document Type:      Enterprise Policy                               Page: 2 of 9
           Policy Title:   Data Classification Policy

TABLE OF CONTENTS

 Section                                                                                   Page

 I.       Policy                                                                              2

 II.      Definitions                                                                         6

 III.     Development and Revision History                                                    7

 IV.      Approval Signature Block                                                            7

 V.       Other Documents                                                                     8

I.     Policy

EXECUTIVE SUMMARY

This policy requires Data Stewards to classify all of the data used by their
organization. It describes the roles and responsibilities of a Data Steward, the four
types of data classifications and the minimum set of classifications. Generally, it lays
the groundwork for the proper classification and handling of data used by the State.
Further insight into this policy may be obtained through the organization’s IRM
(Information Resource Manager) or the DTI CES (Customer Engagement Specialist)
assigned to the organization.

This policy does not limit or redefine FOIA (Freedom of Information Act) laws or
regulations. In case of any conflict, the law shall prevail.

PURPOSE

This policy provides instruction for State organizations to better handle, secure,
access, and use data. Sound business judgment and practices must be applied, and
the State must comply with applicable Federal, State and Local laws and regulations,
as well as any agency-specific guidelines then in effect. Examples of such are HIPAA
and Gramm-Leach-Bliley (GLB), Federal Information Security Management Act

                           “Delivering Technology that Innovates”

                                                                     STATE OF DELAWARE
                                                   DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                                  801 Silver Lake Blvd.
                                                                 Dover, Delaware 19904

    Doc Ref Number:        IN-DataClass-001                                           Revision Number: 3
    Document Type:         Enterprise Policy                                              Page: 3 of 9
          Policy Title:    Data Classification Policy

(FSMA), Privacy Act, PCI DSS, Federal Tax Data Safeguards (IRS Publication 1075),
etc.1 This policy will be reviewed and revised periodically. However, the State is
obligated to comply with new laws or regulations coming into effect between
revisions.

This policy is expected to be referenced by other State policies and standards that
will further define the implications of the data classification. As such, the actual data
classification designations will have far-reaching effects on various aspects of
Information Technology throughout the State.

The National Institute of Standards and Technology (NIST) has drafted a
comprehensive approach to data classification and the risks that are associated with
different levels of data classification. Specifically, it addresses the integrity and
availability of data as well as confidentiality, which is the focal point of this policy.
NIST standards were used in the development of this policy.

DATA CLASSIFICATIONS

The Data Steward is responsible for classifying all data under the organization’s
control into one of the following classes.

    State of Delaware Public – Information available to the general public; eligible
       for public access.

    State of Delaware Confidential – Information covered by one or more laws.
       The disclosure of this information could endanger citizens, corporations,
       business partners and others. The types of information might be covered
       under non-disclosure agreements; or safeguarded by a general reference in
       law or best practices.

    State of Delaware Secret – Information that, if divulged, could compromise or
       endanger the people, or assets of the State; such as Public Safety

1
 HIPAA is the United States Health Insurance Portability and Accountability Act of 1996, PL 104-191.
The Financial Modernization Act of 1999, also known as the “Gramm-Leach-Bliley Act” or GLB Act.

                           “Delivering Technology that Innovates”

                                                         STATE OF DELAWARE
                                             DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                       801 Silver Lake Blvd.
                                                      Dover, Delaware 19904

   Doc Ref Number:       IN-DataClass-001                              Revision Number: 3
    Document Type:       Enterprise Policy                                 Page: 4 of 9
         Policy Title:   Data Classification Policy

       Information. Data that is specifically protected by law (e.g.. HIPAA).

   State of Delaware Top Secret – Information that could, if divulged, expose the
      State’s citizens and assets to great risk.

Generally, any data classification that is higher than public should be considered
non-public. The classifications stated herein are to be considered as minimum
classification levels for the data. The Data Steward may not specify a lower
classification.

These classifications are in line with the Federal Government data classifications. The
exception is that the Federal Government has no consistent designation for Public
data. In some cases, the term Unclassified is used to denote non-Confidential, non-
Secret and non-Top Secret data. For clarity, the State of Delaware chose to use the
term State of Delaware Public data rather than non-Confidential, non-Secret and
non-Top Secret data. One core value that distinguishes a classification from another
is the Risk of Harm. What is the risk that harm can result from the inappropriate
disclosure or use of this information?

       Minimum Classifications
       The following data elements are examples of data that must be classified no
       lower than as shown regardless of the context in which they are represented.

                         Data Element                             Classification
        Social Security Number                               State of Delaware
                                                             Confidential
        Employee ID                                          State of Delaware
                                                             Confidential
        Bank Account Number                                  State of Delaware
                                                             Confidential
        Credit Card Number                                   State of Delaware
                                                             Confidential
        Mother’s Name                                        State of Delaware
                                                             Confidential

                         “Delivering Technology that Innovates”

                                                          STATE OF DELAWARE
                                             DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                        801 Silver Lake Blvd.
                                                       Dover, Delaware 19904

   Doc Ref Number:       IN-DataClass-001                               Revision Number: 3
    Document Type:       Enterprise Policy                                  Page: 5 of 9
         Policy Title:   Data Classification Policy

        Father’s Name                                         State of Delaware
                                                              Confidential
        Place of Birth                                        State of Delaware
                                                              Confidential

The statewide policies and standards pertaining to data protection can be found at
the DTI website. Local guidelines are established by the state organization itself. For
a complete list, please contact the organization’s Information Resource Manager
(IRM).

ENFORCEMENT and WAIVER

DTI will enforce this policy during the course of normal business activities, including
review of proposed projects and during the design, development or support of
systems. This policy may also be enforced by others during the course of their
normal business activities, including audits.

If any dispute arises regarding the minimum classifications of data contained in this
policy, the waiver process will resolve the issue. If any disputes or questions arise
from the Data Classification Guidelines, the data steward or designee can present
them to the State’s Chief Security Officer for help in determining the proper
classification.

Failure to Comply
Failure to comply with the policy is a serious matter whether through intentional act
or negligence and may be grounds for discipline up to and including dismissal based
on the Just Cause standard set forth by Merit Rules, or collective bargaining
agreement, whichever is applicable to the subject employee. Exempt employees shall
be subject to appropriate discipline without recourse, except as provided by law.
While DTI has no authority to discipline employees of other agencies/organizations in
the Executive, Legislative, or Judicial branches of government, it will take the
appropriate steps to ensure any misconduct is appropriately addressed.

                         “Delivering Technology that Innovates”

                                                         STATE OF DELAWARE
                                             DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                       801 Silver Lake Blvd.
                                                      Dover, Delaware 19904

   Doc Ref Number:       IN-DataClass-001                              Revision Number: 3
    Document Type:       Enterprise Policy                                Page: 6 of 9
         Policy Title:   Data Classification Policy

II. Definitions

Data – Distinct pieces of information in digital (computer-readable) format that can
   be stored, read, manipulated, or transmitted.

Dataset – A Dataset is a collection of data elements in a structure that is its own
   unique entity and usually associated with a name. Examples include files,
   databases, etc. A Dataset’s classification must be at least as high as that of the
   highest data element contained therein (classification by association). This also
   applies to multiple Datasets when stored or transmitted together; the
   classification of the combined Datasets must be at least as high as that of the
   highest Dataset in the combination.

Data Owner –
   Consult the Delaware Information Security Policy for this definition

Data Steward –
   Consult the Delaware Information Security Policy for this definition

Data User -
   Consult the Delaware Information Security Policy for this definition

Information Resource Manager (IRM) – Those assigned the responsibility to act
   as the primary points of contact for appropriate communications between DTI
   and the organization.

Personally Identifiable Information (PII) – Information which can be used to
   identify or contact a person uniquely and reliably, or can be used with other
   sources to uniquely identify an individual. Examples include but are not limited
   to full name, full social security number, full date of birth, street address,
   telephone number, email address, and fingerprints or other biometric data.

                         “Delivering Technology that Innovates”

                                                        STATE OF DELAWARE
                                            DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                      801 Silver Lake Blvd.
                                                     Dover, Delaware 19904

   Doc Ref Number:      IN-DataClass-001                            Revision Number: 3
   Document Type:       Enterprise Policy                               Page: 7 of 9
       Policy Title:    Data Classification Policy

III. Development and Revision History

      Date               Revision
      3/1/2006           Rev 1 – Initial version
      2/28/2008          Rev 2 – Updated version
      3/22/2011          Rev 2 – Minor revision
      4/4/2014           Rev 2 – Minor revision
      1/19/2021          Rev 2 – Updates for data destruction
      2/3/2023           Rev 2 – Updates for links
      02/26/2024         Rev 3 – Updates for definitions and NIST reference
      11/1/2024          Rev 3 - Removed a reference to the Technology Investment
                         Council

IV. Approval Signature Block

        Name & Title:                                                Date

        State Chief Information Officer

                        “Delivering Technology that Innovates”

                                                    STATE OF DELAWARE
                                        DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                  801 Silver Lake Blvd.
                                                 Dover, Delaware 19904

Doc Ref Number:     IN-DataClass-001                            Revision Number: 3
Document Type:      Enterprise Policy                               Page: 8 of 9
    Policy Title:   Data Classification Policy

                    “Delivering Technology that Innovates”

                                                          STATE OF DELAWARE
                                             DEPARTMENT OF TECHNOLOGY AND INFORMATION
                                                        801 Silver Lake Blvd.
                                                       Dover, Delaware 19904

     Doc Ref Number:     IN-DataClass-001                               Revision Number: 3
     Document Type:      Enterprise Policy                                  Page: 9 of 9
         Policy Title:   Data Classification Policy

V.   Other Documents

A Data Classification Guideline has been published and it is hereby noted. If there is
any conflict between the Data Classification Guideline and this policy, the policy shall
prevail. To obtain more information, please reference the Enterprise Standards and
Policies and notable the Delaware Information Security Policy for further insight.

External Providers must provide written Certificate of Destruction as directed in the
Delaware Terms and Conditions Governing Cloud Services and Data Usage
Agreement.

                         “Delivering Technology that Innovates”

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
