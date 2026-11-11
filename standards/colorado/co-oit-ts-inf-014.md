---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-inf-014
title: Network Switching Standard
doc_type: standard
citation: TS-INF-014
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1CK746GAXq71kFUGDnIYxg2S45XKJ16ML
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 1101650c092876d04a0935ccd1592c74aea9448d06d599cdbe79b65013d533dc
effective_date: '2025-05-13'
source_version: 3.0, last updated 04/22/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-014: Network Switching Standard'', links this file as https://drive.google.com/file/d/1CK746GAXq71kFUGDnIYxg2S45XKJ16ML/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1CK746GAXq71kFUGDnIYxg2S45XKJ16ML
  (the source URL above).'
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Network Switching Standard (TS-INF-014)

## At a glance

OIT technical standard TS-INF-014 (Infrastructure): Network Switching Standard. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-014: Network Switching Standard
  Document ID                       TS-INF-014
  Title                             Network Switching Standard
  Executive Sponsor                 Network Services Managers
  Issuing Authority                 Office of Information Technology (OIT)
  Applies to                        OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and
                                    vendors contracted by OIT or its stakeholders.
  Tier                              Standard
  Version                           3.0
  Effective Date                    05/13/2025
  Last Updated                      04/22/2026

1. Purpose
This standard is issued under the authority of the Governor's Office of Information Technology (OIT)
(C.R.S. 24-37.5, et seq.) and the Office of Enterprise Architecture (Rule 8 CCR 1501-7). It
communicates the standards OIT has developed to provide enterprise standard configurations for
network switches, describing the minimum requirements for network switches.

2. Scope
These standards apply to OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and vendors
contracted by OIT or its stakeholders, as a means to enforce technology standardization and assist in
making the usage, support, and/or purchase of technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●      Chairs and conducts business of the Architecture Review Board (ARB).
   ●      Updates effective date and/or last review date.
   ●      Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●      Engages stakeholders and subject matter experts to determine the standard.

                                                                                            Page 1 of 3

   ●   Reviews and approves the Standard (this document).
Network Services Managers
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Updates document standards and version number; presents to the Architecture Review Board
       for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Due to the variety of office sizes, building layouts, and networking requirements, a spectrum of
common switching architectures is outlined. As agencies and OIT upgrade their network, it is crucial
to procure devices that meet the minimum functionality required for seamless integration with the
Colorado State Network (CSN) and Software-Defined Wide Area Network (SD-WAN).
Must-Have Access-Layer and Distribution Features
   ●   Mandatory Core Features: Spanning Tree Protocol (STP), Gigabit capabilities, remote
       administration, SNMP, and MIB; PoE+ and Universal PoE (UPOE) models; high-capacity
       stacking; uplink options for Gigabit, 10 Gigabit, and 40 Gigabit Ethernet.
   ●   Advanced Routing Features for Layer 3 Switches: IPv4 and IPv6 routing, static routes, and
       advanced IP routing protocols (OSPF, BGP, IS-IS); policy-based routing and multicast
       capabilities.
   ●   Quality of Service (QoS) Features: Hierarchical bandwidth management, CoS, DSCP, shaping,
       and policing.
   ●   Mandatory Security Features: IEEE 802.1x, DHCP snooping, dynamic ARP inspection, RA guard,
       IP source guard, and ACLs; management via SSHv2 and SNMPv3; TACACS+ and RADIUS support;
       RSA key generation of at least 2048 bits.
   ●   Maintenance and Monitoring: Port monitoring capabilities; SolarWinds ability to read SNMP
       MIBs; centralized management platform connectivity; enhanced warranties with next business
       day (NBD) advance hardware replacement.
Site Size Recommendations
   ●   Small Sites (0–45 endpoints): Gigabit (PoE) ports, 1 Gig uplink, advanced spanning tree
       protocols.
   ●   Medium Sites (50–100+ endpoints): Similar features with 10 Gig uplinks.
   ●   Large Locations (150+ endpoints): Switch stacks connected to a distribution switch with L3
       capabilities.
Installation Standards
   ●   Mount the device in a 19" network rack (wall-mounted or floor standing) in a secured room
       with ventilation.
   ●   Location must have power availability compatible with a power filter, UPS, or surge
       protection.
   ●   Physical Security: The agency is responsible for securing the room and/or key management;
       switches must be installed in secure locations limited to authorized personnel only.
   ●   Configuration management must follow CISP-005.

                                                                                           Page 2 of 3

Refresh (End of Life)
   ●   Remote Location Access Switches: 4–6 years recommended refresh cycle.
   ●   Distribution Switches: 5–7 years, ideally updated with the full site refresh.
   ●   Core/Chassis Switches: 7–8 years recommended refresh cycle.

5. Exceptions and Variance
Requests for variances from any provision of this standard must be requested using the Technical
Standard End User Exception Request Procedure. Requests must include compensating controls. The
Secure Configuration Exception Request form must be submitted to oit_ciso@state.co.us.

6. References
   ●   OIT Hardware Standard Guidance
   ●   Cisco Configuration Management: Best Practices
   ●   Cisco Network Security Baseline
   ●   Cisco Guide to Harden IOS Devices

7. Definitions
Access Layer: The lowest layer of the TCP/IP protocol, providing means for the system to deliver
data to other devices directly attached to a network.
Network Switch: A computer networking device that connects devices together using packet
switching to receive, process, and forward data.
Port Density: A switch with a large number of switch ports.
RADIUS: A networking protocol providing centralized AAA management for users connecting to a
network service.
Redundancy: System design in which a component is duplicated so a backup exists if it fails.
TACACS+: A network protocol for remote authentication and authorization of users attempting to
access network resources.
SolarWinds: IT monitoring and management tool for an enterprise environment.

                                                                                         Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-014: Network Switching Standard', links this file as https://drive.google.com/file/d/1CK746GAXq71kFUGDnIYxg2S45XKJ16ML/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1CK746GAXq71kFUGDnIYxg2S45XKJ16ML (the source URL above).
