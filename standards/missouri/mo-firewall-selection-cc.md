---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-firewall-selection-cc
title: Firewall Selection
doc_type: standard
citation: 'Security Domain Compliance Component: Firewall Selection'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallSelectionARCApp.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 6527e1bce4f96aac4a615929f3eef3d9f4edc14e1b3f4328db114785b3b2ca71
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

# Firewall Selection (Security Domain Compliance Component: Firewall Selection)

## At a glance

Row 'Firewall Selection' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/firewall-selection-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/08/2004. The index lists it as an approved standard.

## Full text

                                             C
                                             Coom
                                                mpplliiaannccee C
                                                                Coom
                                                                   mppoonneenntt

                                                    D
                                                    DEEFFIIN
                                                           NIITTIIO
                                                                  ONN
Name                   Firewall Selection
                       Selecting the appropriate firewall for a specific environment requires an
                       understanding of the basic features of the various types of firewalls available.
Description            Supported feature sets, rather than firewall type, should drive the firewall
                       selection.

                       Recent advances in network infrastructure engineering and information security
                       have resulted in a combining of the various firewall functions into hybrid
                       products. It is not always a simple matter to decide which specific firewall
Rationale              product is the most suitable for a given application or enterprise infrastructure.
                       Hybridization of firewall platforms makes the pre-purchase product evaluation
                       phase of a firewall project important.

                       •   Selecting the appropriate firewall provides the security functions needed in
Benefits
                           the most efficient and cost-effective manner
                                    A
                                    ASSSSO
                                         OCCIIA
                                              ATTEED
                                                   DAARRC
                                                        CHHIITTEEC
                                                                 CTTU
                                                                    URREE LLEEVVEELLSS
List the Domain Name            Security
List the Discipline Name        Technical Controls
List the Technology Area Name   Secure Gateways and Firewalls
List Product Component Name
                                      C
                                      COOM
                                         MPPLLIIA
                                                ANNC
                                                   CEE C
                                                       COOM
                                                          MPPO
                                                             ONNEEN
                                                                  NTT TTYYPPEE
Document the Compliance
                                Guideline
Component Type
Component Sub-type
                                              C
                                              COOM
                                                 MPPLLIIA
                                                        ANNC
                                                           CEE D
                                                               DEETTA
                                                                    AIILL
                                Supported features, rather than firewall classification, should
                                drive firewall selection.

                                •    For speed, flexibility and simplicity, select a firewall that includes:
                                            o Packet Filter Firewall, or
                                            o Stateful Inspection Firewall
State the Guideline, Standard
                                •    For high-bandwidth or real-time applications select a firewall that
or Legislation
                                     includes:
                                            o Dedicated Proxy Server
                                •    For greater authentication, select a firewall that includes:
                                            o Application-Proxy Gateway Firewall, or
                                            o Dedicated Proxy Server
                                •    For greater logging capability, select a firewall that includes:

                                             o    Application-Proxy Gateway Firewall, or
                                             o    Dedicated Proxy Server
                              •   To perform specialized filtering (restrict outbound traffic to certain
                                  locations, examine all outbound email for viruses, restrict internal
                                  users from writing to the DMZ, track outgoing client ports
                                  individually, allow only established inbound connections) select a
                                  firewall that includes:
                                          o Dedicated Proxy Server, or
                                          o Stateful Inspection Firewall
                              •   To assist in foiling internally based attacks or malicious behavior,
                                  select a firewall that includes:
                                          o Dedicated Proxy Server, or
                                          o Personal Firewall
                              •   As an endpoint for a Virtual Private Network (VPN), select:
                                         o Personal Firewall

                              NOTE:
                              Many application-proxy gateway firewalls have implemented basic
                              packet filter functionality in order to provide better support for UDP
                              (User Datagram Protocol) based applications. Likewise, many packet
                              filter or stateful inspection packet filter firewalls have also implemented
                              basic application-proxy functionality to offset some of the weaknesses
                              associated with their firewall platform. In most cases, packet filter or
                              stateful inspection packet filter firewalls also implement application
                              proxies to provide improved network traffic logging and user
                              authentication in their firewalls.

Document Source Reference #
                                                 Standard Organization
                              NIST SP 800-41,
                                                                               www.csrc.nist.gov/publications/
Name                          Guideline for Firewalls and          Website
                                                                               nistpubs
                              Firewall Policy
Contact Information
                                                   Government Body
                              National Institute of
Name                          Standards and Technology             Website     http://csrc.nist.gov/
                              (NIST)
Contact Information
                                                     KKEEYYW
                                                           WOORRD
                                                                DSS
                              Hybrid, packet filter, application proxy, stateful inspection, personal
List all Keywords
                              firewall, dedicated proxy server
                                     C
                                     COOM
                                        MPPO
                                           ONNEEN
                                                NTT C
                                                    CLLA
                                                       ASSSSIIFFIIC
                                                                  CAATTIIO
                                                                         ONN
Provide the Classification        Emerging               Current             Twilight      Sunset
                                  Rationale for Component Classification
Document the Rationale for
Component Classification

                                        Conditional Use Restrictions
Document the Conditional Use
Restrictions
                                                  Migration Strategy
Document the Migration
Strategy
                                          Impact Position Statement
Document the Position
Statement on Impact
                                             C
                                             CUURRRREEN
                                                      NTT SSTTA
                                                              ATTU
                                                                 USS
Provide the Current Status)      In Development          Under Review           Approved     Rejected
                                                   A
                                                   AUUD
                                                      DIITT TTRRA
                                                                AIILL
Creation Date                  05/27/2004                   Date Accepted / Rejected   06/08/2004
    Reason for Rejection
Last Date Reviewed                                          Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
