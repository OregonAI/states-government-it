---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-security-voice-over-internet-protocol-voip-cc
title: Security for Voice Over Internet Protocol (VOIP)
doc_type: standard
citation: 'Security Domain Compliance Component: Security for Voice Over Internet Protocol (VOIP)'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Security-for-VOIP.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 9da57dfc2055432ce829dfbf808239611bad0e386355a3ca7642f7d6499017cb
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

# Security for Voice Over Internet Protocol (VOIP) (Security Domain Compliance Component: Security for Voice Over Internet Protocol (VOIP))

## At a glance

Row 'Security for Voice Over Internet Protocol (VOIP)' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/security-voice-over-internet-protocol-voip-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Under Review, not Approved, with Date Approved / Rejected 02/13/2025. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                       COMPLIANCE COMPONENT

                                                           DEFINITION
Name                   Security for Voice Over Internet Protocol (VOIP)
                       Security for Voice Over Internet Protocol (VOIP) refers to securing IP networks when
Description
                       transmitting voice across them.
                       Transmitting voice over data networks increases the complexity and vulnerability of the
                       networks. Although VOIP is widespread, the technology is often incorrectly implemented,
Rationale
                       and often lacks compatibility and continuity with existing systems. This can lead to
                       compromised security.
                              •   Securing VOIP transmissions ensures the confidentiality, integrity, and availability of
Benefits
                                  both voice and data communications

                                           ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name            Security
Specify the Discipline Name        Technical Controls
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
                                       •      Agencies must perform a risk assessment before deploying VOIP systems
                                              and as dictated by state or federal requirements.
                                                  o   The assessment must examine and ensure the agency can
                                                      acceptably manage and mitigate the risks to their information,
                                                      system operations, and continuity of essential operations.
                                       •      The agency network infrastructure and security, including firewalls, IDSs,
                                              VPNs, etc., shall be capable of supporting VOIP.
State the Guideline, Standard          •      Sufficient backup power shall be available for the office VOIP switch, if the
or Legislation                                VOIP function is critical.
                                       •      Agencies must ensure that adequate physical security is in place to restrict
                                              access to VOIP network components.
                                                  o   This will deter insertion of sniffers or other network monitoring
                                                      devices as well as physical damage.
                                       •      Agencies must use a mechanism to allow only authorized VOIP traffic
                                              through firewalls.

        o    A variety of protocol dependent and independent solutions are
             available, including firewalls that understand VOIP, application
             level gateways (ALGs) for VOIP protocols, Session Border
             Controllers, or other standards-based solutions when they mature.
Gateway Management
•   Strong authentication (see the Advanced/Strong Authentication
    Compliance Component) and access control must be used for
    administrators on voice gateway systems.
•   IPsec or Secure Shell (SSH) must be used for all remote management and
    auditing access.
        o    It is preferable to do VOIP gateway management from a physically
             secure system.
Softphones
•   “Softphone” systems shall not be used over a public network or
    connection, even if the voice conversation is not confidential, because it
    creates more avenues of attack into the data network.
    The only exception is that softphones may be used over a public network if
    the connection is via VPN without split-tunneling.
        o    A softphone is software and the communication system internal to
             the PC to replicate a standard telephone handset or deskset.
•   Softphone systems shall only be used over a private network if the user is
    not working with FTI, PII, etc.
•   Any remote access services, such as FTP and Telnet, shall be disabled on
    the laptop, workstation or mobile device, as well as any local
    administration and management features for the local user.
Desksets
•   When agencies use VOIP desksets, they must separate voice and data on
    logically different networks (VLANs). This includes separate address
    blocks used for voice and data traffic.
        o    Separate VLANs allows for proper configuration of firewall and
             intrusion detection systems, as well as making it easier to provide
             Quality of Service (QOS).
•   Any remote access features on the VOIP desksets, such as FTP and
    Telnet, shall be disabled as well as any local administration and
    management features.
•   Default login and administrator passwords on VOIP phones shall be
    changed from the default.
Remote IP Phones
•   Mobile units integrated with the VOIP system must use products
    implementing current industry standard encryption.
•   Default login and administrator passwords on VOIP phones shall be
    changed from the default.
Public and Private Networks
•   Encryption is required when transmitting confidential or trusted information
    over a public network, such as the Internet.

                                     •     Encryption may be required when transmitting confidential or trusted
                                           information over a private network, depending on the agency.
                                     •     Encryption must be done from end to end, which may negatively impact
                                           performance.
                                This document shall be reviewed annually or as needed.
                                NIST Special Publication 800-58, Security Considerations for Voice Over IP
Document Source Reference #     Systems (Jan 2005) www.csrc.nist.gov/publications/nistpubs/800-58/SP800-58-
                                final.pdf
                                                  Compliance Sources
                                National Institute of
                                Standards and Technology                           www.csrc.nist.gov/publications/fips/i
Name                                                                Website
                                (NIST), Computer Security                          ndex.html
                                Resource Center (CSRC)
Contact Information             inquiries@nist.gov
Name                                                                Website
Contact Information

                                                    KEYWORDS
                                Softphone, Telephony, IPT, H.323, PSTN, SIP, PBX, POTS, ALGs, WPA, RSN,
List Keywords
                                VoIP, encrypt, deskset, phone

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight           Sunset
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
Creation Date                   05/10/2005                    Date Approved / Rejected     02/13/2025

    Reason for Rejection
Last Date Reviewed         01/28/2025   Last Date Updated   02/13/2025
    Reason for Update      Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
