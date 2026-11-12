---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-application-proxy-gateway-firewalls-cc
title: Application - Proxy Gateway Firewalls
doc_type: standard
citation: 'Security Domain Compliance Component: Application - Proxy Gateway Firewalls'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallsApplicationProxyGatewayARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: afb9b19ad6cc90233d06305d907f29d5217c9d4d495cd764b756e08034ea9854
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

# Application - Proxy Gateway Firewalls (Security Domain Compliance Component: Application - Proxy Gateway Firewalls)

## At a glance

Row 'Application - Proxy Gateway Firewalls' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/application-proxy-gateway-firewalls-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/08/2004. The index lists it as an approved standard.

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
Name                   Application-Proxy Gateway Firewalls

                       Application-Proxy Gateway Firewalls combine OSI Layer 7 (Application Layer)
                       functionality with lower layer access control. The application-proxy gateway
Description
                       firewall software performs the routing between the inside and outside interfaces
                       of the firewall.

                       Application-Proxy Gateway Firewalls add to defense in depth when used with
Rationale              other types of firewalls. They strengthen enforcement of security policies and
                       provide user authentication capability.

                       •   In the event the application-proxy gateway software ceases to function, the
                           firewall system will not pass network packets through the firewall system.

                       •   Application-Proxy Gateway Firewalls usually have more extensive logging
                           capabilities than packet filter or stateful inspection because they examine
                           the entire network packet rather than just the network addresses and ports.

                       •   Application-Proxy Gateway Firewalls provide superior authentication than
                           packet filter or stateful inspection packet filter firewalls where network layer
                           addresses can be easily spoofed.
                       •   Application-Proxy Gateway Firewalls are less vulnerable to address spoofing
Benefits                   attacks than packet filter and stateful inspection firewalls.

                       NOTE:
                           •    Application-Proxy Gateway Firewalls are not generally well suited to
                                high-bandwidth or real-time applications. To reduce the load on the
                                firewall, a Dedicated Proxy Server can be used to secure less time-
                                sensitive services such as email and most web traffic.

                           •    Application-Proxy Gateway Firewalls tend to be limited in terms of
                                support for new network applications and protocols. A separate,
                                application-specific proxy agent is required for each type of network
                                traffic that needs to transit a firewall.
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
                                •   Each individual application-proxy, also referred to as a proxy agent,
                                    shall interface directly with the firewall access control rule set to
                                    determine whether a given piece of network traffic should be
                                    permitted to transit the firewall.

                                •   Each individual application-proxy shall have the ability to require
                                    authentication of each individual network user. This user
                                    authentication shall take two or more of the following forms:
                                    o     User ID and Password Authentication

                                    o     Hardware or Software Token Authentication

                                    o     Source Address Authentication (on dedicated circuits only)

                                    o     Biometric Authentication
State the Guideline, Standard
or Legislation
                                •   Proxy applications should be used for inbound/outbound HTTP
                                    connections and for inbound/outbound email that are capable of the
                                    following operations:
                                    o     Blocking Java applets and applications
                                    o     ActiveX and JavaScript filtering
                                    o     Blocking specific MIME extensions
                                    o     Scanning for viruses
                                    Note: This is not a recommendation to enable blocking of active web
                                    content, but to be capable of blocking it if necessary. The decision
                                    to block active content, excluding viruses, should be weighed
                                    carefully, as blocking active content will render many websites
                                    unusable or difficult to use. Organizations should not rely solely on
                                    the firewall proxies to remove the above content.
Document Source Reference #
                                               Standard Organization
                                NIST SP 800-41,
                                                                              www.csrc.nist.gov/publications/
Name                            Guideline for Firewalls and      Website
                                                                              nistpubs
                                Firewall Policy
Contact Information
                                                  Government Body
                                National Institute of
Name                            Standards and Technology         Website      http://csrc.nist.gov/
                                (NIST)
Contact Information

                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
                               Dedicated Proxy Server, proxy agent, block, packets, deny, ports,
List all Keywords              protocols, logging, attacks, Layer 7, application layer, OSI, HTTP,
                               ActiveX, Java, MIME, authentication, spoof
                                     C
                                     COOM
                                        MPPO
                                           ONNEEN
                                                NTT C
                                                    CLLA
                                                       ASSSSIIFFIIC
                                                                  CAATTIIO
                                                                         ONN
Provide the Classification       Emerging                Current                Twilight         Sunset
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
Provide the Current Status)      In Development          Under Review           Approved         Rejected
                                                   A
                                                   AUUD
                                                      DIITT TTRRA
                                                                AIILL
Creation Date                  06/08/2004                   Date Accepted / Rejected       06/08/2004
     Reason for Rejection
Last Date Reviewed                                          Last Date Updated
     Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
