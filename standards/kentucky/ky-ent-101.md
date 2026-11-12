---
schema_version: 1
corpus: states-government-it
jurisdiction: kentucky
id: ky-ent-101
title: ENT-101 Enterprise Data Classification Standard
doc_type: standard
citation: ENT-101
authority_level: ''
issuing_body: Commonwealth Office of Technology
source_url: https://technology.ky.gov/policies-and-procedures/PoliciesProcedures/ENT-101%20Enterprise%20Data%20Classification%20Standard.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 3b441b7d0a3f47fa8196f551d763d7b20e431bf5abcc6681e21b4800ed034ed7
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# ENT-101 Enterprise Data Classification Standard (ENT-101)

## At a glance

Listed on COT's Policies pageas 'ENT-101 Enterprise Data Classification Standard' (type Standards):

## Full text

                                 ENT-101: Enterprise Data Classification Standard

ENT-101: Enterprise Data Classification Standard
                                             Document Revision History

 Version      Date      Change Description / Notes                                                   Author / Editor

 1.0       8/29/2019    Creation and incorporation of document.                                      Tom Walters
 1.0       12/27/2021   Reviewed                                                                     Tom Walters
                        Removal of role Data Stewart with those duties re-allocated to the Cabinet   Karen Chrisman /
 2.0       3/13/2025
                        and minor grammar, layout and formatting changes.                            Tracy Burgess

Overview
Each Cabinet will identify its data for the purpose of defining its value, location, and level of protection. This
standard defines the classification scheme and outlines the expected data handling requirements throughout the
lifecycle of data. This document also provides recommended sample disclaimers to be used when storing and
transferring data of various classifications.

KRS 61.870 (7) defines a “Public record” as all books, papers, maps, photographs, cards, tapes, discs, diskettes,
recordings, software, or other documentation regardless of physical form or characteristics, which are prepared,
owned, used, in the possession of or retained by a public agency. This is the data classification scheme for
these public records.

This standard is the minimum Commonwealth Office of Technology (COT) requirement for data classification. If an
agency has a business need for or a statutory or regulatory requirement with a stricter standard, the stricter
standard is required. This standard is applicable when a stricter standard does not apply.

                        “Remainder of this page intentionally left blank”

                                                     Page 1 of 8

                                 ENT-101: Enterprise Data Classification Standard

Standard Data Classification Levels

Classification                                                 Some Examples
                 Definition
Level                                                          Not a complete list of each category
                                                                • Press releases
                                                                • Open access website pages
                 Applies to data that is readily available
Open                                                            • Brochures
                 to the public with anonymous access.
                                                                • Published information (including data files)
                                                                • Public presentations

                 Applies to data that is intended for use
                 within the Commonwealth.
                 Unauthorized external disclosure could
                 adversely impact the Commonwealth,
                 its citizens, employees, and business          • Employment application records and employee
                 partners.                                        records
                                                                • Licensed software
Internal         This classification also applies to open       • Communication between Commonwealth
                 records as defined by the Kentucky               citizens and Commonwealth staff
                 Open Records Act, KRS 61.870 (2).              • Memos
                 Applies to data that is not openly             • Training manuals
                 published, but that can be made
                 available via open record requests.
                 Direct access to this data is restricted to
                 authenticated and authorized users.
                                                                • Criminal history data (especially pre-conviction)
                                                                • Trade secrets
                                                                • Government classified information
                                                                • Authentication Verifier (password, cryptographic
                                                                  private keys)
                                                                • Protected Health Information
                                                                • Personal Information as defined by KRS
                 Applies to data that must be kept                61.931(6)
                 private under federal, local, or state         • Business Strategy
Confidential
                 laws, or contractual agreements, or to         • Payment card information
                 protect its proprietary value, or must be
                                                                • Social security numbers
                 kept private for any combination of
                                                                • Federal Tax Information
                 these reasons.
                                                                • Personally Identifiable Education records
                                                                • Personal Data as defined by the General Data
                                                                  Protection Regulation (GDPR) and that is
                                                                  subject to the GDPR
                                                                • Data protected by federal code or regulation or
                                                                  state statute or regulation
                                                                • System Documentation
                                                     Page 2 of 8

                               ENT-101: Enterprise Data Classification Standard

Electronic Data Handling Requirements Matrix
Creation
                   Open               Internal                                                       Confidential
                                      All Open requirements and the following requirements:          All Open and
                                                                                                     Internal
                   Ensure proper      Creation/discussion of new data in public or on a public
                                                                                                     requirements
                   labeling           network is prohibited.
                                                                                                     and the
                   immediately upon
                                      Ensure use of secure connection (e.g. https, VPN, SFTP)        following
                   creation.
                                                                                                     requirement:
Creation of data                      Creation of Internal data must be approved by the
                   Creation of Open
                                      appropriate data owner(s).                                     Ensure all
                   data must be
                                                                                                     creation/
                   approved by the
                                                                                                     discussion is
                   appropriate data
                                                                                                     done in private
                   owner(s).
                                                                                                     with authorized
                                                                                                     personnel only.
Storage
                   Open               Internal                                                       Confidential
                                      All Open requirements and the following requirements:
                                                                                                     All Open and
                                      Must be stored within a protected boundary that is             Internal
                                      continuously monitored.                                        requirements
                                      Physical boundary protections must be in place to prevent      and the
Storing of data                       unauthorized physical access.                                  following
on static assets                                                                                     requirements:
                                      Appropriate access control mechanisms must be employed
                                      to prevent unauthorized logical access and enforce least       Access to
                                      privileged access.                                             confidential data
Non-removable      Follow
                                                                                                     must be logged
media              Commonwealth       Data must be protected in transit through encryption or        and logs
                   drive storage      isolation.
(Examples:                                                                                           retained for a
                   conventions.
servers,                              Data encryption is not required but recommended.               minimum of 90
workstations,                                                                                        days or as
endpoint                              All encryption keys must be managed including creation,        required by
devices)                              issuance, renewal, and disposal.                               regulatory
                                                                                                     guidance.
                                      For mobile computing devices, full drive encryption is
                                      required. (Example: a workstation that is mobile such as a     Data must be
                                      laptop or a tablet)                                            encrypted at rest
                                                                                                     and in transit.

                                                                                                     All Open and
                   Follow
                                                                                                     Internal
                   Commonwealth       All Open requirements and the following requirements:
Storage of data                                                                                      requirements
                   drive storage
on any                                The removable media device shall be encrypted.                 and the
                   conventions and
removable                                                                                            following
                   ensure secure      The removable media shall be securely stored and
media                                                                                                requirement:
                   storage of the     transported.
(CD, DVD USB       physical device.                                                                  Chain of custody
drive, storage                        Data must be sanitized in compliance with enterprise policy.   documenting the
                   Label removable
external to a                                                                                        lifecycle of the
                   media with
computing                                                                                            media from
                   appropriate
device)                                                                                              creation through
                   classification
                                                                                                     sanitization must
                   level.
                                                                                                     be documented.

                                                   Page 3 of 8

                                   ENT-101: Enterprise Data Classification Standard

Electronic Data Handling Requirements Matrix (continued)

Usage
                       Open                          Internal                         Confidential
                                                     Standard user
                                                     authentication practices in
                                                     place for remote access to       All Internal requirements and the
                                                     systems hosting the data         following requirement:
                       Anonymous access              (username and password).
Accessing of data                                                                     Two-factor authentication for remote
                       allowed                       Remote access by VPN that
                                                                                      access, and auditable data system
                                                     is managed by a central
                                                                                      administration.
                                                     directory.
                                                     Data is password protected.
                                                                                      All Internal requirements and the
                                                     Auditing data is restricted to   following requirements:
                                                     designated internal users. All
                                                                                       Ensure system logging, audit of user
                       Change history of Open        unusual behavior (alterations
Auditing of data                                                                      credentials and use, audit of errors,
                       data is publicly available.   and/or deletions) is brought
                                                                                      failed attempts, permissions, and
                                                     to the attention of the data
                                                                                      changes.
                                                     owner.
                                                                                      File integrity monitoring is performed.
                       Printed data follows the
                       requirements of the Non-                                       All Open and Internal
Printing of data                                     All Open requirements.
                       Digital Data Handling                                          requirements.
                       Requirements Matrix.
Posting data on
                       Permitted                     Not permitted                    Not permitted.
social media

Transmission

                       Open                          Internal                         Confidential

                                                                                      All Open and Internal
                                                     All Open requirements and
                                                                                      requirements and the following
                       All email defaults to an      the following requirements:
                                                                                      requirements:
                       Internal category and
                                                     Data must not be emailed
Emailing of data       displays language such as                                      Data must be email encrypted or
                                                     outside of the organization
internally             the Sample Email                                               password protected.
                                                     unless approved to do so.
                       Disclaimer and
                                                                                      If using password encryption, the
                       Restrictions.                 All email defaults to Internal
                                                                                      password must be sent in a separate
                                                     requirements.
                                                                                      communication.
Granting
                                                     Must follow formal data
permission to
                                                     sharing agreements and/or
view, write, or edit   None                                                           All Internal requirements.
                                                     formal contractual
data externally
                                                     agreements.
(i.e. third parties)

                                                       Page 4 of 8

                                ENT-101: Enterprise Data Classification Standard

Electronic Data Handling Requirements Matrix (continued)

Archiving
                         Open                      Internal             Confidential
                         All archiving shall
                         follow KDLA State
                         Government Records
                         Retention Schedules
                                                   All Open
Archiving of data        and follow the                                 All Open and Internal requirements.
                                                   requirements.
                         requirements of the
                         Electronic Data
                         Handling
                         Requirements Matrix.

Destruction
                         Open                      Internal             Confidential
                         Destruction or
                         sanitization only in
                         accordance with KDLA
Destruction (or
                         State Government
sanitization) of data                              All Open
                         Records Retention                              All Open and Internal requirements.
and data bearing                                   requirements.
                         Schedules and must
devices.
                         comply with CIO-092
                         Media Protection
                         Policy.

                         Must follow formal data
Destruction of data      sharing agreements
                                                   All Open
on third-party hosted    and/or formal                                  All Open and Internal requirements.
                                                   requirements.
services                 contractual
                         agreements.

                        “Remainder of this page intentionally left blank”

                                                    Page 5 of 8

                          ENT-101: Enterprise Data Classification Standard

Non-Digital Data Handling Requirements Matrix
Creation
           Open                     Internal                          Confidential

                                                                      All Open and Internal requirements and
           Ensure proper labeling                                     the following requirement:
Creation   immediately upon         All Open requirements.            All creation or discussion of data must be
           creation.                                                  completed in private with authorized
                                                                      personnel only.

Storage
           Open                     Internal                          Confidential
                                    All Open requirements and
                                    the following requirements:
                                    Data must be kept out of sight    All Open and Internal requirements and
                                    after business hours or when      the following requirement:
           Follow KDLA State        visitors are present.
Storage    Government Records                                         Data must be stored in a secure
           Retention Schedules.     Access to the facility requires   environment or locked compartment, such
                                    centralized electronic badge      as a filing cabinet or desk drawer when
                                    access based upon least           not attended by an authorized user.
                                    privilege.
                                    Access is reviewed regularly.

Usage
           Open                     Internal                          Confidential
                                    Data should only be printed       All Internal requirements and the
                                    when there is a legitimate        following requirements:
                                    business need. Data should        Copies must only be shared with
                                    only be printed/copied            individuals with authorized clearance.
Usage      None                     internally or to satisfy an       Data can only be printed if allowed by
                                    Open Records Request.             statute or regulation.
                                    Copies must only be shared        All data must be marked as
                                    with individuals on a need-       appropriate (e.g., “Confidential”). All
                                    to-know basis.                    usage must be performed in private.

                                               Page 6 of 8

                        ENT-101: Enterprise Data Classification Standard

Non-Digital Data Handling Requirements Matrix (continued)

Transmission
                 Open                    Internal                  Confidential
                                                                   All Internal requirements and the
                                         Include a statement       following requirement:
                                         identifying the           Transmission must be logged.
Transmission     None                    classification level      Agencies should comply with any
                                         and list restrictions     additional agency requirements for
                                         for redistribution.       transmission of confidential
                                                                   information.

Archiving
                 Open                    Internal                  Confidential

                                         All Open
                                         requirements and
                                         the following
                                         requirement:
                 Follow KDLA State
                 Government              Ensure physical
Archiving                                security of the offsite   All Open and Internal requirements.
                 Records Retention
                 Schedules.              facility with
                                         centralized
                                         management of
                                         access based upon
                                         least privilege.

Destruction
                 Open                    Internal                  Confidential

                                         Follow KDLA State
                                         Government
                                         Records Retention
Destruction      None                                              All Internal requirements.
                                         Schedules and CIO-
                                         092 Media Protection
                                         Policy.

                                          Page 7 of 8

                               ENT-101: Enterprise Data Classification Standard

Sample Disclaimers and Statements

Sample Email Disclaimer and Restrictions
The following table provides sample disclaimers and statements to include in transmission of email containing
information that has been classified as Internal or Confidential in accordance with the Commonwealth’s CIO-
110 Enterprise Data Management Policy, ENT-101 Enterprise Data Classification Standard (this document),
and ENT-102 Data Classification Process.

For Confidential data, the classification must be labeled in the subject line in all capital letters
(CONFIDENTIAL), and the attached document(s) must be labeled with the classification. This label alerts the
recipient to the level of care and restriction required.

 Classification Sample Email Disclaimer and Restrictions

                  This email and any attachments contain information that has been classified as “[Internal
                  (or) Confidential].” It is intended exclusively for the use of the individual(s) to whom it is
 Internal or      addressed. This information may be protected by federal and state laws or regulations.
 Confidential     If you are not the intended recipient, you may not use, copy, distribute, or forward this
                  message or contents to anyone. If you have received this email in error, please notify the
                  sender immediately and delete the email from your email system.

Sample Non-Digital Data Disclaimer and Restrictions
The following table provides sample disclaimers and statements to include along with any mailing that has
been classified in accordance with the Commonwealth’s CIO-110 Enterprise Data Management Policy, ENT-
101 Enterprise Data Classification Standard (this document), and ENT-102 Data Classification Process.

For Confidential data, the classification must be labeled in all capital letters (CONFIDENTIAL) and the attached
document(s) or devices must be labeled with the classification of the data they contain. This label alerts the
recipient to the level of care and restriction required.

 Classification Sample Non-Digital Data Disclaimer and Restrictions

                  This document and any attachments contain information that has been classified as
                  “[Confidential].” It is intended solely for the use of the individual(s) to whom it is
                  addressed. It contains information that may be protected by federal and state laws or
                  regulations.
 Confidential
                  If you are not the intended recipient, you may not use, copy, distribute, or forward this
                  document, its content, or its attachments to anyone. If you have received this document in
                  error, please notify the sender immediately.

References
Helpful references can be found on the Enterprise IT Policies webpage.

                                                     “END”

                                                   Page 8 of 8

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
