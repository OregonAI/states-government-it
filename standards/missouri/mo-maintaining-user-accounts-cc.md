---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-maintaining-user-accounts-cc
title: Maintaining User Accounts
doc_type: standard
citation: 'Security Domain Compliance Component: Maintaining User Accounts'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Maintaining-User-Accounts.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 27b84c80aa532ad3dbacd200dd851aedc207b26a1a2cc8cec06bbb53c887652e
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

# Maintaining User Accounts (Security Domain Compliance Component: Maintaining User Accounts)

## At a glance

Row 'Maintaining User Accounts' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/maintaining-user-accounts-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 02/19/2025. The index lists it as an approved standard.

## Full text

                                       COMPLIANCE COMPONENT

                                                          DEFINITION
Name                   Maintaining User Accounts
                       Maintaining User Accounts involves the process of requesting, establishing, issuing,
Description
                       modifying, and terminating user accounts along with tracking user access authorizations.

                       Maintaining User Accounts reinforces individual accountability and helps keep information
Rationale              secure by granting the user the least amount of permission necessary to accomplish their
                       job functions.

                       •      No idle accounts are available, limiting possible security vulnerabilities.
Benefits               •      Users only have permissions necessary to perform their current job functions.
                       •      Provides methodology for auditing user accounts.

                                           ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name            Security
Specify the Discipline Name        Management Controls
Specify the Technology Area
                                   Personnel Security
Name
Specify the Product
Component Name

                                               COMPLIANCE COMPONENT TYPE
Document the Compliance
                                   Guideline
Component Type
Component Sub-type

                                                     COMPLIANCE DETAIL
                                   Usernames
                                       •      Usernames must be unique and must follow a standard naming
                                              convention. Naming conventions should take several factors into account:
                                                 o   The chance of duplicate usernames
                                                 o   The structure of your agency
                                                 o   The constraints of the applications
State the Guideline, Standard
or Legislation                                   o   The confidentiality of the username (for example, not using the
                                                     SSN)
                                                 o   The change of a username. Such changes must consider:
                                                            All affected systems
                                                            Updating the ownership of all files and other user-specific
                                                             resources
                                                            Handling email issues
                                                            Removal of previous username from affected systems

                                 •   A username must identify a unique individual or resource at any given time
                                     if the username has permission to make modifications to systems or
                                     information

                              Authentication
                                 •   See the Password Controls CC and the Strong Authentication CC

                              Access Control Information
                                 •   See the Logical Access Controls TA.
                                 •   A user account must be appropriately reconfigured to add or remove
                                     accesses after a job change
                                 •   Agencies must have a procedure where the IT department is notified in a
                                     timely manner of a new person’s arrival and the accesses required
                                 •   Agencies must have a procedure where the IT department is notified in a
                                     timely manner of a person’s departure. At the very least, the appropriate
                                     actions should include:
                                         o     Immediately disabling the user's access to all systems and related
                                               resources
                                         o     Preserving the user's files to meet compliance standards in case
                                               something is needed at a later time
                                         o     Coordinating access to the user's files with the user's manager

                              Audit and Management Reviews
                                 •   Agencies must periodically review user accounts, to include at least the
                                     following:
                                         o     Levels of authorized access for each user
                                         o     Identification of inactive, idle or orphaned accounts
                                         o     Whether required training or certification has been completed
                                 •   These reviews can be conducted on at least two levels
                                         o     On an application-by-application basis
                                         o     On a system wide basis
                                 •   Both levels of reviews can be conducted by
                                         o     In-house systems personnel (a self-audit)
                                         o     The agency’s internal audit staff
                                         o     External auditors
                              This document will be reviewed annually or as needed.

Document Source Reference #   NIST Special Publication 800-12 Rev. 1, An Introduction to Computer Security

                                             Compliance Sources
Name                          NIST                              Website       csrc.nist.gov
Contact Information           inquiries@nist.gov
Name                                                            Website

Contact Information

                                                     KEYWORDS
                                Audit, user ID, username, account name, password, authentication,
List Keywords                   access control, authorization, permissions, tracking, active directory,
                                RACF, AD, idle, orphaned, inactive, web application

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight         Sunset
     Sunset Date

                                           COMPONENT SUB-CLASSIFICATION
 Sub-Classification          Date                          Additional Sub-Classification Information
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
Provide the Current Status          In Development            Under Review           Approved             Rejected

                                                       AUDIT TRAIL
Creation Date                   03/02/2006                    Date Approved / Rejected     02/19/2025
     Reason for Rejection
Last Date Reviewed              02/19/2025                    Last Date Updated            02/19/2025
     Reason for Update          Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
