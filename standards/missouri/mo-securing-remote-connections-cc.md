---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-securing-remote-connections-cc
title: Securing Remote Connections
doc_type: standard
citation: 'Security Domain Compliance Component: Securing Remote Connections'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Securing-Remote-Connections.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: ed9604e926652c4f6ef9a4be2b280ee775b9c464a5de8d1b8691679a15039996
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

# Securing Remote Connections (Security Domain Compliance Component: Securing Remote Connections)

## At a glance

Row 'Securing Remote Connections' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/securing-remote-connections-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Under Review, not Approved, with Date Approved / Rejected 11/08/05. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                    COMPLIANCE COMPONENT

                                                     DEFINITION
Name                   Securing Remote Connections
                       Securing Remote Connections is necessary to ensure the confidentiality, integrity and
Description            availability of information transmitted via the Internet.

                       Remote access poses a higher risk to State of Missouri information systems.
Rationale
                       Due to the growth of remote work, there is an increasing number of people who need
                       secure remote access.
                          • Provides a means of securing a system that is connected to an agency via a public
Benefits
                               provider

                                      ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name         Security
Specify the Discipline Name     Technical Controls
Specify the Technology Area
                                Remote Access Controls
Name
Specify the Product
Component Name

                                           COMPLIANCE COMPONENT TYPE
Document the Compliance
                                Guideline
Component Type
Component Sub-type

                                               COMPLIANCE DETAIL
                                Securing Remote Connections
                                   • Only agency-approved equipment may be remotely connected to State of
                                       Missouri systems.
                                   • Endpoint protection software must be installed and up to date on devises
                                       utilized for remote connections.
                                   • A firewall must be installed and properly configured on all remotely
                                       connected systems (see the Firewall Rules Compliance Component)
                                   • Computers connected to the State of Missouri systems shall not
State the Guideline, Standard          simultaneously connect to any other network via another network device.
or Legislation                               o Split-tunneling must not be enabled on the VPN.
                                             o Shares between the agency systems and non-agency systems
                                                 must be disabled when the remote device is connected to any
                                                 State of Missouri system.
                                   • Data should not be stored on remote devices.
                                   • Agency approval is required before any user may connect remotely to the
                                       agency network.
                                   • Remote connections must meet the cryptography compliance component
                                       requirements (see the Cryptography CC)
                                   • Remote connections require multi-factor authentication.

                                NIST Special Publication 800-46, Guide to Enterprise Telework,
Document Source Reference #
                                Remote Access, and Bring Your Own Device (BYOD) Security, Rev. 2 (July 2016)
                                                 Compliance Sources
                                NIST, CERT®Coordination
Name                                                                Website        csrc.nist.gov, www.cert.org
                                Center
Contact Information
Name                                                                Website
Contact Information

                                                    KEYWORDS
                                Broadband, Cable, Digital Subscriber Line (DSL), Wireless, Broadband over Power
List Keywords                   Line (BPL), Power Line Communications (PLC), Satellite, Internet, Virtual Private
                                Network (VPN),

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight          Sunset
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
Provide the Current Status          In Development            Under Review               Approved          Rejected

                                                       AUDIT TRAIL
Creation Date                   03/31/2005                    Date Approved / Rejected     11/08/05
     Reason for Rejection
Last Date Reviewed              06/06/2024                    Last Date Updated            06/21/2024
     Reason for Update          Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
