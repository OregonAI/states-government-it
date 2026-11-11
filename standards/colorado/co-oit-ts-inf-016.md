---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-inf-016
title: Network Routing and SD-WAN Routers
doc_type: standard
citation: TS-INF-016
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=174iBuG2xg5C58640lYX0cWB-qR7okzYH
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 4f37c5207b89abf4e661a8c57d23a740a3b7694039ebb369e85db8aefc000abd
effective_date: '2026-04-13'
source_version: 3.0, last updated 08/04/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-016: Network Routing and SD-WAN Routers'', links this file as https://drive.google.com/file/d/174iBuG2xg5C58640lYX0cWB-qR7okzYH/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=174iBuG2xg5C58640lYX0cWB-qR7okzYH
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

# Network Routing and SD-WAN Routers (TS-INF-016)

## At a glance

OIT technical standard TS-INF-016 (Infrastructure): Network Routing and SD-WAN Routers. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-016: Network Routing and SD-WAN
Routers
  Document ID                       TS-INF-016
  Title                             Network Routing and SD-WAN Routers
  Executive Sponsor                 Network Services Managers
  Issuing Authority                 Office of Information Technology (OIT)
  Applies to                        OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and
                                    vendors contracted by OIT or its stakeholders.
  Tier                              Standard
  Version                           3.0
  Effective Date                    04/13/2026
  Last Updated                      08/04/2026

1. Purpose
This standard is issued under the authority of the Governor's Office of Information Technology (OIT)
(C.R.S. 24-37.5, et seq.) and the Office of Enterprise Architecture (Rule 8 CCR 1501-7). It
communicates the standards OIT has developed for enterprise-standard configurations of network
routers, describing the minimum requirements for network routers.

2. Scope
These standards apply to OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and vendors
contracted by OIT or its stakeholders, to enforce technology standardization and assist in making the
use, support, and/or purchase of technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●      Chairs and conducts business of the Architecture Review Board (ARB).
   ●      Updates effective date and/or last review date.
   ●      Publishes the ARB-approved Standard to the OIT public-facing website.

                                                                                            Page 1 of 4

Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Network Services Managers
   ●   Owner of Standard; engages stakeholders and subject matter experts to establish the
       standard.
   ●   Updates document standards and version number; presents to the Architecture Review Board
       for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Due to the varying scale of agency networks, building complexities, and diverse connectivity
requirements, a spectrum of common routing architectures is outlined. Routers play a pivotal role in
directing traffic between different networks, ensuring efficient data flow, and providing secure
connectivity for integration with the Colorado State Network (CSN) and SD-WAN.
Mandatory Core and Edge Router Features
   ●   Support for IPv4 and IPv6 routing, static routes, and advanced IP routing protocols (OSPF,
       BGP, IS-IS).
   ●   Policy-based routing and multicast capabilities, including PIM and IGMP snooping (v1, v2, v3).
   ●   High-capacity interface options for Gigabit, 10 Gigabit, 40 Gigabit, and 100 Gigabit Ethernet
       ports.
   ●   Redundant power supplies and fan options for high availability.
   ●   Hardware-based forwarding for high-performance packet processing.
   ●   Support for Virtual Routing and Forwarding (VRF-Lite) for network segmentation.
   ●   NetFlow/IPFIX support for traffic analysis and monitoring.
Mandatory SD-WAN Features & Requirements
   ●   FIPS 140-2/3 Validated Encryption: All traffic, especially CJIS and FTI, must be encrypted in
       transit using FIPS 140-2/3 validated IPsec VPN tunnels (e.g., AES-256).
   ●   Centralized Security Policy Enforcement: Leverage vManage for consistent, enterprise-wide
       policy definition and deployment, including granular Role-Based Access Control (RBAC).
   ●   Network Segmentation: Support for VRFs and VLANs to logically isolate sensitive data and
       enforce least privilege principles.
   ●   Integrated Security Services using SASE: Must include an application-aware cloud firewall, IPS,
       URL filtering, and Advanced Malware Protection (AMP).
   ●   Strong Authentication & Secure Management: Support for TACACS+, RADIUS, SSHv2, and
       SNMPv3 for administrative access.
   ●   Comprehensive Logging & Auditing: Generate detailed, tamper-resistant audit logs integrated
       with centralized SIEM systems.
   ●   High Availability & Resilience: Support dual-path redundancy and dynamic path selection to
       ensure continuous connectivity.

                                                                                           Page 2 of 4

Mandatory Security Features for All Router Types
   ●   Management connectivity via SSHv2 and SNMPv3; individual administration logins; support for
       TACACS+ and RADIUS servers.
   ●   Capability to store Type 9 hashed passwords using the SCRYPT hashing algorithm (RFC 7914);
       RSA key generation of at least 2048 bits.
   ●   Support for session/login timeouts; Access Control Lists (ACLs) for traffic filtering; Control
       Plane Policing (CoPP); and Unicast Reverse Path Forwarding (uRPF).
   ●   Event logging to a centralized logging server and NTP support for timestamp accuracy.
Refresh (End of Life)
   ●   Remote Location Edge Routers: 4–6 years recommended refresh cycle.
   ●   Medium Site Edge Routers: 5–7 years recommended refresh cycle.
   ●   Core/Chassis Routers: 7–8 years recommended refresh cycle.
   ●   At a minimum, manufacturers' lifecycle recommendations must be followed, replacing
       equipment before security vulnerabilities or loss of OS support.

5. Exceptions and Variance
Requests for variances from any provision of this standard must be made to the Director of Network
Services for review and approval. The Exception Request must address business or technical reasons
for the inability to adhere to one or more requirements, including proposed compensating controls.
The Secure Configuration Exception Request form must be submitted to oit_ciso@state.co.us.

6. References
   ●   OIT Hardware Standard Guidance
   ●   NIST SP 800-171, Rev. 3, Protecting Controlled Unclassified Information in Nonfederal Systems
       and Organizations
   ●   IRS Safeguard Computer Security Evaluation Matrix (SCSEM)
   ●   FIPS 140-2/3, Security Requirements for Cryptographic Modules
   ●   Colorado OIT CISP-004 (Data Security Policy) and CISP-003 (IT Security Risk Management
       Policy)

7. Definitions
Edge Router: A router located at a network boundary enabling an internal network to connect to
external networks.
Core Router: A router optimized for handling high-volume, high-speed data traffic within the
backbone of an extensive network.
SD-WAN (Software-Defined Wide Area Network): A virtual WAN architecture allowing enterprises to
leverage any combination of transport services to connect users to applications securely.
SASE (Secure Access Service Edge): A cloud-based architecture combining WAN capabilities with
comprehensive network security functions into a single, integrated cloud service model.
BGP (Border Gateway Protocol): A standardized exterior gateway protocol for exchanging routing
and reachability information among autonomous systems.

                                                                                             Page 3 of 4

Control Plane Policing (CoPP): A feature configuring a QoS policy for the control plane to protect
the CPU from excessive traffic.
OSPF (Open Shortest Path First): A widely used interior gateway protocol routing packets within a
single autonomous system based on shortest path first.
uRPF (Unicast Reverse Path Forwarding): A security feature that helps mitigate IP spoofing by
verifying the source IP address of incoming packets against the router's routing table.

                                                                                          Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-016: Network Routing and SD-WAN Routers', links this file as https://drive.google.com/file/d/174iBuG2xg5C58640lYX0cWB-qR7okzYH/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=174iBuG2xg5C58640lYX0cWB-qR7okzYH (the source URL above).
