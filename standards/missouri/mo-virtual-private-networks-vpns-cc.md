---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-virtual-private-networks-vpns-cc
title: Virtual Private Networks (VPNs)
doc_type: standard
citation: 'Security Domain Compliance Component: Virtual Private Networks (VPNs)'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-VPNs.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 727216e1474e7f6873b9811eaeec7e5db0ca4597043aa4b2203bdf8e3c20ad73
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

# Virtual Private Networks (VPNs) (Security Domain Compliance Component: Virtual Private Networks (VPNs))

## At a glance

Row 'Virtual Private Networks (VPNs)' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/virtual-private-networks-vpns-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 10/04/2016. The index lists it as an approved standard.

## Full text

                                        COMPLIANCE COMPONENT

                                                         DEFINITION
Name                   Virtual Private Network (VPN)
                       A Virtual Private Network (VPN) can be a software or hardware network technology that
Description            creates a secure encrypted network connection over a public network to an agency’s
                       network.
                       A Virtual Private Network (VPN) provides a low-cost means of establishing a secure private
Rationale              connection for remotely accessing an agency’s private network.
                              •   Provide opportunities for increased productivity of mobile employees,
                                  telecommuters, business partners and remote sites by allowing access to agency
                                  resources
                              •   Provides for the confidentiality and integrity of the agency’s data in transit across
Benefits                          the public network
                              •   More cost effective than alternatives such as dedicated private telecommunications
                                  lines between agencies or branch offices

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
                                   Standard
Component Type
Component Sub-type

                                                    COMPLIANCE DETAIL

                                   • VPNs must meet the Cryptography for VPNs Compliance Component (CC)
                                     requirements
                                   • VPNs must meet applicable requirements in the Securing Remote Computers
                                     and Connections CC
State the Guideline, Standard
or Legislation                     • An anomaly-identifying software or hardware (Intrusion Detection and
                                     Prevention System) should be in place inside the point in the agency network
                                     where VPN traffic is decrypted (see the Intrusion Prevention System IPS CC)
                                   •   Site-to-Site VPNs:
                                         o A VPN uses dedicated equipment and strong encryption to secure point
                                              to point communications over a public network.

                                      o Must authenticate the tunnel with a:
                                       o Pre-shared key or
                                       o certificate
                                      o May utilize Access Control Lists (ACLs) on the VPN device to limit what
                                         resources can be accessed
                                      o Must not allow split-tunneling unless an agency-controlled firewall is
                                         properly positioned between the agency network and any non-agency or
                                         public network (see the Firewall Environments CC)
                                         NOTE: Split tunneling occurs when concurrent access is allowed to
                                         resources on the agency network and a non-agency or public network via
                                         the VPN
                                • Remote Access VPNs:
                                      o Remote Access VPN is a client-to-LAN connection by users who need to
                                         securely connect to the agency network from remote locations. This can
                                         be via wireless, Digital Subscriber Line (DSL), cable modem, etc.
                                      o Must authenticate the VPN tunnel with a:
                                                Two-Factor authentication (NIST SP 800-63-1)
                                      o Must not allow split tunneling (only one network connection is allowed)
                                      o Should utilize Access Control Lists (ACLs) to limit what resources can be
                                       accessed by a remote client (see Access Control Lists CC)
                                NIST Special Publication 800-46 v2, SP 800-114, SP 800-47, SP 800-77, SP 800-
Document Source Reference #
                                113
                                                  Compliance Sources
                                National Institute of
Name                            Standards and Technology           Website      http://csrc.nist.gov
                                (NIST)
Contact Information             info@nist.gov
Name                                                               Website
Contact Information

                                                       KEYWORDS
                                Broadband, Cable, DSL, Wireless, Satellite, Modem, Internet, Dial-Up,
List Keywords
                                telecommute, mobile, remote, IPSec, tunnel, site-to-site

                                           COMPONENT CLASSIFICATION
Provide the Classification          Emerging                 Current                Twilight            Sunset
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
Provide the Current Status      In Development            Under Review               Approved        Rejected

                                                   AUDIT TRAIL
Creation Date                10/04/2016                   Date Approved / Rejected      10/04/2016
    Reason for Rejection
Last Date Reviewed                                        Last Date Updated            10/04/2016
    Reason for Update        Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
