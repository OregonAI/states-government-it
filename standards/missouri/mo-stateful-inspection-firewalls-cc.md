---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-stateful-inspection-firewalls-cc
title: Stateful Inspection Firewalls
doc_type: standard
citation: 'Security Domain Compliance Component: Stateful Inspection Firewalls'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallsStatefulInspectionARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 1a6cefb90a1c8abed18eeadc2b3ef306be376a0b1c48c1b9f3325d13bc1b895b
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

# Stateful Inspection Firewalls (Security Domain Compliance Component: Stateful Inspection Firewalls)

## At a glance

Row 'Stateful Inspection Firewalls' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/stateful-inspection-firewalls-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/08/2004. The index lists it as an approved standard.

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
Name                   Stateful Inspection Firewalls
                       Stateful Inspection Firewalls are packet filter firewalls that incorporate added
                       awareness of the data at the OSI model Layer 4 (Transport Layer). The first
                       line of the packet filter rule set allows any inbound connection if the destination
Description            port is between 1023 and 16384. Opening this many ports creates an immense
                       risk of intrusion. Stateful inspection firewalls reduce this risk by creating a state
                       table of outbound TCP connections, along with each session's corresponding
                       port greater than 1023, which is then used to validate any inbound traffic.
                       Stateful Inspection Firewalls add to defense in depth when used with other
Rationale              types of firewalls. They strengthen enforcement of security policies and add
                       transport layer filtering.
                       • Speed
                       • Flexibility
                       • Simplicity
Benefits
                       • Greater security than packet filter firewall because the Stateful Inspection
                           Firewall tracks outgoing client ports individually and allows only established
                           inbound connections.
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
                                •    Stateful Inspection Firewalls shall create a state table of outbound
                                     TCP connections greater than 1023, along with each session's
                                     corresponding inbound port. This table shall be used to validate
                                     inbound and outbound traffic.
                                •    According to TCP specifications, the client source port shall be some
State the Guideline, Standard        number greater than 1023. According to convention, the destination
or Legislation                       port on the remote host will likely be less than 1024.
                                •    Stateful Inspection Firewalls shall accept a packet and examine its
                                     source address, destination address, port, and protocol. The firewall
                                     shall apply the rule set and perform one of the following:
                                       o Accept: Pass the packet through the firewall as requested.
                                       o Deny: Drop the packet and return an error message to the

                                          source system.
                                       o  Discard: Drop the packet, but do not return an error message
                                          to the source system. This particular action does not reveal
                                          the firewall’s presence (“black hole methodology”) to an
                                          outsider.
                               •    Outbound filtering should be employed on IP addresses, ports,
                                    protocols and application traffic to block unauthorized users, internal
                                    and external, from connecting to sensitive systems.
Document Source Reference #
                                               Standard Organization
                               NIST SP 800-41,
                                                                                   www.csrc.nist.gov/publications/
Name                           Guideline for Firewalls and           Website
                                                                                   nistpubs
                               Firewall Policy
Contact Information
                                                    Government Body
                               National Institute of
Name                           Standards and Technology              Website       http://csrc.nist.gov/
                               (NIST)
Contact Information
                                                      KKEEYYW
                                                            WOORRD
                                                                 DSS
List all Keywords
                                       C
                                       COOM
                                          MPPO
                                             ONNEEN
                                                  NTT C
                                                      CLLA
                                                         ASSSSIIFFIIC
                                                                    CAATTIIO
                                                                           ONN
Provide the Classification         Emerging                Current               Twilight         Sunset
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
Provide the Current Status)        In Development          Under Review          Approved         Rejected
                                                     A
                                                     AUUD
                                                        DIITT TTRRA
                                                                  AIILL
Creation Date                  04/22/2004                     Date Accepted / Rejected      06/08/2004

    Reason for Rejection
Last Date Reviewed         Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
