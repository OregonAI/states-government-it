---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-access-controls-cc
title: Access Controls
doc_type: standard
citation: 'Security Domain Compliance Component: Access Controls'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/12/CC-Access-Controls.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 3fd1d77c41051da3cd61c894744d56d631e6f9d6048ff1ce6b490522f63078b2
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

# Access Controls (Security Domain Compliance Component: Access Controls)

## At a glance

Row 'Access Controls' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/access-controls-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Under Review, not Approved, with Date Approved / Rejected 12/18/2025. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                     COMPLIANCE COMPONENT

                                                     DEFINITION
Name                   Access Controls
                       Access Controls prescribe who or what is to have access to a specific system resource and
Description            the type of access permitted.
                       Access controls allow (or prohibit) the use of various computer resources. Users must have
Rationale              access to the resources they need to perform their job duties, but no more. Access controls
                       enforce policy and help ensure that unauthorized actions are not permitted.
                       Access controls:
                           Prescribe who or what is to have access to a specific system resource
                           Prescribe type of access that is permitted
                           Protect operating systems and other system software from unauthorized
                              modification or manipulation
Benefits
                           Protect the integrity and availability of information by restricting the number of users
                              and processes with access
                           Helps protect confidential information from being disclosed to unauthorized
                              individuals

                                       ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name         Security
Specify the Discipline Name     Technical Controls
Specify the Technology Area
                                Logical Access Controls
Name
Specify the Product
Component Name

                                           COMPLIANCE COMPONENT TYPE
Document the Compliance
                                Guideline
Component Type
Component Sub-type

                                                 COMPLIANCE DETAIL
                                The requirements for using—and prohibitions against the use of—various system
                                resources vary considerably from one system to another. Access is based on the
                                concept of least privilege. It may also be important to control the kind of access
                                that is permitted (e.g., the ability for the average user to execute, but not change,
                                system programs). These types of access restrictions enforce policy and help
                                ensure that unauthorized actions are not taken.
State the Guideline, Standard
                                Access control is the process of granting or denying specific requests to:
or Legislation
                                     1) Obtain and use information and related information processing services
                                     2) Enter specific physical facilities (e.g., state buildings, data centers,
                                         correctional facilities, state hospitals).

                                System-based access controls are called logical access controls. Logical access
                                controls can prescribe not only who or what (in the case of a process) is to have

                                access to a specific system resource, but also the type of access that is permitted.
                                These controls may be built into the operating system, incorporated into
                                applications programs or major utilities (e.g., database management systems,
                                communications systems), or implemented through add-on security packages.
                                Logical access controls may be implemented internally to the system being
                                protected or in external devices.
                                Examples of access control security controls include:
                                    • account management
                                    • separation of duties
                                    • least privilege
                                    • session lock
                                    • information flow enforcement
                                    • session termination
                                Organizations limit:
                                    1) System access to authorized users
                                    2) Processes acting on behalf of authorized users
                                    3) Devices, including other systems
                                    4) Types of transactions and functions that authorized users are permitted to
                                         exercise

                                This document will be updated annually.
Document Source Reference #     NIST SP 800-12 Rev. 1, Guide to Computer Security (June 2017)

                                                Compliance Sources
                                National Institute of
                                Standards and Technology
Name                                                              Website      http://csrc.nist.gov/
                                (NIST), Computer Security
                                Resource Center (CSRC)
Contact Information
Name                                                              Website
Contact Information

                                                     KEYWORDS
List Keywords                   logical, physical, password, database, protection, access.

                                           COMPONENT CLASSIFICATION
Provide the Classification          Emerging                Current                Twilight             Sunset
     Sunset Date

                                        COMPONENT SUB-CLASSIFICATION
 Sub-Classification          Date                       Additional Sub-Classification Information
    Technology Watch
    Variance
    Conditional Use

                                      Rationale for Component Classification
Document the Rationale for
Component Classification

                                                 Migration Strategy
Document the Migration
Strategy

                                          Impact Position Statement
Document the Position
Statement on Impact

                                                 CURRENT STATUS
Provide the Current Status      In Development            Under Review               Approved       Rejected

                                                   AUDIT TRAIL
Creation Date                02/01/2007                   Date Approved / Rejected     12/18/2025
    Reason for Rejection
Last Date Reviewed           12/17/2025                   Last Date Updated            12/18/2025
    Reason for Update        Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
