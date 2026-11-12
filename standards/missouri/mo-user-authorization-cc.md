---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-user-authorization-cc
title: User Authorization
doc_type: standard
citation: 'Security Domain Compliance Component: User Authorization'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-UserAuthorization03-23-07ARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: bb864cdc351f7495d5c80f95994ccabd672c8d839685c096806d4da0c884b40a
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

# User Authorization (Security Domain Compliance Component: User Authorization)

## At a glance

Row 'User Authorization' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/user-authorization-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 03/23/2007. The index lists it as an approved standard.

## Full text

                                    COMPLIANCE COMPONENT

                                                      DEFINITION
Name                   User Authorization
                       User Authorization is the use of access control policies and associated access enforcement
Description
                       mechanisms that are employed by agencies to control access between users and objects.
                       User authorization is used to mitigate risk to agency operations, assets, and individuals
Rationale
                       associated with information access.
                          • Helps protect agency resources and information
Benefits                  • Allow users access to only those resources needed (least privilege)
                          • Protects users from accidentally accessing unneeded resources and information

                                        ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name         Security
Specify the Discipline Name     Technical Controls
Specify the Technology Area
                                Identification and Authorization
Name
Specify the Product
Component Name

                                           COMPLIANCE COMPONENT TYPE
Document the Compliance
                                Guideline
Component Type
Component Sub-type

                                                COMPLIANCE DETAIL
                                User Authorization should be based on least privilege
                                   • The information system enforces the most restrictive set of rights and
                                       privileges or accesses needed by users

                                    •    Processes acting on behalf of users for the performance of specified tasks
                                            o Including specific ports, protocols, and services

                                    •    The agency employs the practice of least privilege for specific duties and
                                         information systems in accordance with risk assessments

State the Guideline, Standard   User Authorization access control policies should require
or Legislation                     • Documented procedures which facilitate the implementation of the access
                                       control policy and associated access controls
                                           o Address purpose, scope, roles, responsibilities, management
                                                commitment, coordination among organizational entities, and
                                                compliance

                                    •    Developed, disseminated, and periodically reviewed policies and
                                         associated access enforcement mechanisms

                                    •    Access to the information system based on:
                                            o A valid need-to-know that is determined by assigned duties

                                               o   Intended system usage

                                    •    Access administrators are notified when system users are:
                                            o Terminated
                                            o Transferred
                                            o Assigned to different tasks

                                Additional Access Controls
                                   • In addition to controlling access at the information system level, access
                                        enforcement mechanisms are employed at the application level, when
                                        necessary, to provide increased information security for the agency.

                                    •    In the event of emergencies or other serious events, consideration is given
                                         to the implementation of a controlled, audited, and manual override of
                                         automated mechanisms.

                                Information Flow Control
                                    • The information system enforces assigned authorizations for controlling
                                        the flow of information within the system and between interconnected
                                        systems in accordance with applicable policy.

                                    •    Flow control is based on the characteristics of the information. Specific
                                         examples of flow control enforcement can be found in boundary protection
                                         devices (e.g., proxies, gateways, guards, encrypted tunnels, firewalls, and
                                         routers) that employ rule sets or establish configuration settings that
                                         restrict information system services or provide a packet filtering capability.

                                Separation of Duties
                                   • The information system enforces separation of duties through assigned
                                       access authorizations. (See Separation of Duties CC).
Document Source Reference #     NIST SP 800-53

                                                   Compliance Sources
                                National Institute of
                                Standards and Technology
Name                                                               Website       http://csrc.nist.gov/
                                (NIST), Computer Security
                                Resource Center (CSRC)
Contact Information
Name                                                               Website
Contact Information

                                                       KEYWORDS
                                Control, access, need-to-know, separation of duties, information flow, least
List Keywords
                                privilege.

                                           COMPONENT CLASSIFICATION
Provide the Classification          Emerging                 Current                 Twilight              Sunset
     Sunset Date

                                        COMPONENT SUB-CLASSIFICATION
 Sub-Classification          Date                         Additional Sub-Classification Information
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
Provide the Current Status     In Development            Under Review               Approved       Rejected

                                                  AUDIT TRAIL
Creation Date                01/04/2007                  Date Approved / Rejected     03/23/2007
    Reason for Rejection
Last Date Reviewed                                       Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
