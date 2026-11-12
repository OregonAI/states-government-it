---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-packet-filter-firewalls-cc
title: Packet Filter Firewalls
doc_type: standard
citation: 'Security Domain Compliance Component: Packet Filter Firewalls'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallsPacketFilterARCApp.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 0817639fe1d8651e909b3db75122db810b3653be3cfaf96f5fd3f219f5f257bf
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

# Packet Filter Firewalls (Security Domain Compliance Component: Packet Filter Firewalls)

## At a glance

Row 'Packet Filter Firewalls' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/packet-filter-firewalls-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/08/2004. The index lists it as an approved standard.

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
Name                   Packet Filter Firewalls
                       Packet Filter Firewalls are the most basic, fundamental type of firewall. Packet
                       filter firewalls are essentially routing devices that include access control
                       functionality for system addresses and communication sessions. The access
                       control functionality of a packet filter firewall is governed by a set of directives
Description
                       collectively referred to as a rule set. In the basic form, packet filters operate at
                       Layer 3 (Network) of the Open Systems Interconnect (OSI) model. This
                       provides network access control based upon information contained in the
                       packet.
                       Packet Filter Firewalls allow for speed and flexibility, as well as the capability to
                       block denial-of-service and related attacks. This makes them ideal for
                       placement at the outermost boundary with an untrusted network. The packet
Rationale              filter firewall, commonly placed on a boundary router, can block certain attacks,
                       filter unwanted protocols and perform simple access control. Packet filter
                       firewalls are very suitable for high-speed environments where logging and user
                       authentication with network resources are not important.
                       • Packet Filter Firewalls provide:
                            • Speed
                            • Flexibility
                            • Simplicity
                       NOTE:
Benefits               • Packet Filter Firewalls are only an initial layer of defense and should be used
                            in conjunction with other types of firewalls
                       • Packet Filter Firewalls cannot prevent attacks that employ application-
                            specific vulnerabilities or functions
                       • Most packet filter firewalls do not support advanced user authentication
                       • Limited logging functionality
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
State the Guideline, Standard   •    Packet Filter Firewalls shall accept a packet and examine its source
or Legislation                       address, destination address, port, and protocol. The firewall shall
                                     apply the rule set and perform one of the following:

                                            o     Accept: Pass the packet through the firewall as
                                                  requested.
                                            o     Deny: Drop the packet and return an error message to
                                                  the source system.
                                            o     Discard: Drop the packet, but do not return an error
                                                  message to the source system. This particular action does
                                                  not reveal the firewall’s presence (“black hole
                                                  methodology”) to an outsider.
                                  •    Packet Filter Firewalls shall be able to filter both outbound as well
                                       as inbound traffic.
                                  •    Outbound filtering should be employed on IP addresses, ports,
                                       protocols and application traffic to block unauthorized users,
                                       internal and external, from connecting to sensitive systems.
Document Source Reference #
                                                Standard Organization
                               NIST SP 800-41,
                                                                               www.csrc.nist.gov/publications/
Name                           Guideline for Firewalls and         Website
                                                                               nistpubs
                               Firewall Policy
Contact Information
                                                  Government Body
                               National Institute of
Name                           Standards and Technology            Website     http://csrc.nist.gov/
                               (NIST)
Contact Information
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
                               Block, packets, deny, ports, protocols, rule set, logging, attacks, black
List all Keywords
                               hole, layer 3, OSI, boundary router
                                      C
                                      COOM
                                         MPPO
                                            ONNEEN
                                                 NTT C
                                                     CLLA
                                                        ASSSSIIFFIIC
                                                                   CAATTIIO
                                                                          ONN
Provide the Classification       Emerging                Current             Twilight      Sunset
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
Provide the Current Status)      In Development          Under Review        Approved      Rejected

                                        A
                                        AUUD
                                           DIITT TTRRA
                                                     AIILL
Creation Date              04/22/2004            Date Accepted / Rejected   06/08/2004
    Reason for Rejection
Last Date Reviewed                               Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
