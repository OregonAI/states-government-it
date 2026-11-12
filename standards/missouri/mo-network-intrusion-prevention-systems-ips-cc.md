---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-network-intrusion-prevention-systems-ips-cc
title: Network Intrusion Prevention Systems (IPS)
doc_type: standard
citation: 'Security Domain Compliance Component: Network Intrusion Prevention Systems (IPS)'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Network-IPS.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 6a6c4d82306733ce6be9352affe0361ea3e281db1d0656816d5004bc30f5ae31
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

# Network Intrusion Prevention Systems (IPS) (Security Domain Compliance Component: Network Intrusion Prevention Systems (IPS))

## At a glance

Row 'Network Intrusion Prevention Systems (IPS)' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/network-intrusion-prevention-systems-ips-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 5/14/2003. The index lists it as an approved standard.

## Full text

                                       COMPLIANCE COMPONENT

                                                       DEFINITION
Name                   Intrusion Prevention Systems (IPS)
                       Intrusion Prevention Systems collect and analyze information from within
                       network traffic for the purpose of preventing, detecting and mitigating malicious
Description
                       activity.

                       IPS has become a necessary addition to the security infrastructure. IPS is
                       deployed as part of a multi-tiered approach to security to protect the system
Rationale
                       from internet based threats.

                              •   Identifies malicious internet based threats and prevent attacks.
                              •   Identifies patterns that may lead to attacks
                              •   Identifies deviations of protocol states by comparing observed events
                                  with predetermined profiles
Benefits
                              •   An IPS can correct cyclic redundancy (CRC) errors, defrag packet
                                  streams, mitigate TCP sequencing issues, and clean up unwanted
                                  transport and network layer options

                                        ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name           Security
Specify the Discipline Name       Technical Controls
Specify the Technology Area
                                  Intrusion Prevention Systems
Name
Specify the Product
Component Name

                                             COMPLIANCE COMPONENT TYPE
Document the Compliance
                                  Guideline
Component Type
Component Sub-type

                                                 COMPLIANCE DETAIL
                                  General IPS Requirements
                                  • Administrators shall be trained on the IPS before implementation.
                                  • IPS shall be controlled directly from a central location(s).

                                  IPS Deployment Requirements
State the Guideline, Standard     • IPS shall be installed on any internet egress points where sensitive or
or Legislation                      critical information is transmitted.

                                  IPS Analysis Requirements
                                  • IPS must submit logs to the Security Information and Event
                                  Management (SIEM) system.
                                  • IPS must:

                                 o   Drop malicious packets
                                 o   Reset malicious connections
                                 o   Block traffic from malicious source address
                                 o   Use heuristic methods and Anomaly Detection
                                 o   support customized signatures

                              • Administrators shall follow a schedule for checking the results of the
                              IPS to ensure attackers have not modified the system.

                              IPS Response Requirements
                              • IPS must respond in real-time.
                              • IPS must provide active responses to intrusions by:
                                   o Collecting additional information;
                                   o Turning up the number of events logged, or
                                   o Capturing all packets, not just those targeting a particular
                                      port or system
                                   o Changing the environment by:
                                       • Terminating the connection
                                           • Blocking packets from the intruder’s IP address
                                           • Blocking network ports, protocols or services
                                           • Resetting all connections that use certain network
                                           interfaces
                              • IPS should provide passive responses requiring subsequent human
                              action to intrusions by:
                                   o Generating alarms and notifications or
                                   o Reporting alarms and alerts using SNMP traps and plug-in
                                       central network management consoles.
                              • All IPS communications shall be secure and use encrypted tunnels or
                              other cryptographic measures.
                              • IPS shall create output with the following information for each intrusion
                              detected:
                                   o Time/date
                                   o Sensor IP address
                                   o Specific attack name or anomaly
                                   o Source and destination IP addresses
                                   o Source and destination port numbers
                                   o Network protocol used
                                   o Description of the attack type
                                   o Attack severity level
                              • IPS reports should combine redundant attack entries and make attacks
                              of highest importance stand out.
                              NIST SP 800-94 (www.csrc.nist.gov/publications/nistpubs)
Document Source Reference #
                              Guide to Intrusion Detection and Prevention Systems (IDPS)
                                            Compliance Sources
                              National Institute of
                              Standards and Technology
Name                          (NIST), Computer             Website      http://csrc.nist.gov/
                              Security Resource Center
                              (CSRC)
Contact Information           inquiries@nist.gov
Name                                                       Website
Contact Information

                                                        KEYWORDS
                                buffer overflows, sniffing, exploit, probes, heuristics, anomaly,
List Keywords
                                malicious, suspicious, IDS, NIDS

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight       Sunset
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
Provide the Current Status          In Development            Under Review               Approved       Rejected

                                                       AUDIT TRAIL
Creation Date                   04/03/2003                    Date Approved / Rejected     5/14/2003
     Reason for Rejection
Last Date Reviewed                                            Last Date Updated            11/15/2016
     Reason for Update          Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
