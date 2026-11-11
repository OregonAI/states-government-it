---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-013
title: UPS/PDU for Network Systems
doc_type: standard
citation: TS-INF-013
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1p4pxd9yXTmugesIUhEsJEm9M-TyN26Zd
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 26de123e7273b2beb78a62cf87b633c120c7fe1226b751024d16e85309383bad
effective_date: '2025-05-13'
source_version: 3.0, last updated 04/22/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-013: UPS/PDU for Network Systems'', links this file as https://drive.google.com/file/d/1p4pxd9yXTmugesIUhEsJEm9M-TyN26Zd/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1p4pxd9yXTmugesIUhEsJEm9M-TyN26Zd
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

# UPS/PDU for Network Systems (TS-INF-013)

## At a glance

OIT technical standard TS-INF-013 (Infrastructure): UPS/PDU for Network Systems. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-013: UPS/PDU for Network Systems
  Document ID                     TS-INF-013
  Title                           UPS/PDU for Network Systems
  Executive Sponsor               Network Services, Network Services Manager
  Issuing Authority               Office of Information Technology (OIT)
  Applies to                      OIT and OIT-supported agencies, employees of OIT, agencies
                                  supported by OIT, and vendors contracted by the State of
                                  Colorado or its stakeholders.
  Tier                            Standard
  Version                         3.0
  Effective Date                  05/13/2025
  Last Updated                    04/22/2026

1. Purpose
This standard is issued under the authority of the Governor's Office of Information Technology (OIT)
(C.R.S. 24-37.5, et seq.) and the Office of Enterprise Architecture (Rule 8 CCR 1501-7). It addresses
stakeholder needs related to UPS and PDU standards for network communications equipment,
providing guidelines for agencies and OIT in selecting the appropriate uninterruptible power supply
or power distribution unit based on each agency's specific requirements.
The goal of this standard is to define the minimum requirements for designing, installing, securing,
monitoring, maintaining, and protecting UPS systems and PDUs, and to clarify the roles and
responsibilities of OIT, vendors, and agencies.

2. Scope
These standards apply to OIT and OIT-supported agencies. This standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by the State of Colorado or its
stakeholders, to enforce technology standardization and assist in making the usage, support, and/or
purchase of technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

                                                                                           Page 1 of 3

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Network Services - Network Services Manager
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Updates document standards and version number; presents to the Architecture Review Board
       for approval and adoption.
All OIT and agency facilities staff are responsible for knowing and following the standards outlined in
this document.

4. Standards
This standard for UPS (Uninterruptible Power Supply) and PDU (Power Distribution Unit) outlines the
minimum requirements for units that supply power to network equipment. All network
communication infrastructure within an agency's OIT support must have power protection, achieved
via a protected PDU or a UPS system.
Power Distribution Unit (PDU) Requirements
   ●   Power Protection: PDUs must include built-in surge protection, overload protection, and
       circuit breakers at each outlet or branch circuit.
   ●   Internal Transfer Switch: The PDU should include an Automatic Transfer Switch (ATS) with
       minimal delay (preferably under 10 ms) and a manual override option.
   ●   Power Filtering: When a UPS is not used, the PDU must include EMI/RFI filtering capable of
       filtering frequencies from 150 kHz to 100 MHz.
   ●   Form Factor: Rack-mount PDUs should be designed for standard 19-inch rack mounting (1U or
       2U), with modular components.
   ●   Compliance: PDUs should be UL-listed and comply with CE, IEC 60950, and IEC 62040, as well
       as RoHS regulations.
UPS Topology Options
   ●   Single-Conversion (Standby) UPS: More energy-efficient but less protective; best for smaller
       setups such as network closets (1–6 switches / 1 router).
   ●   Line-Interactive UPS: Ideal for core locations servicing ISP and backbone fabric for campuses
       and large buildings.
   ●   Double-Conversion UPS: Offers the highest level of protection; recommended for mission-
       critical systems.
   ●   Multi-Mode UPS: Balances efficiency and protection; suitable for smaller setups.

                                                                                            Page 2 of 3

UPS Rating
   ●   List all equipment to be protected; determine volts and amps drawn by each device to find
       maximum load.
   ●   Multiply volts by amps for a VA figure per device; sum all VA figures.
   ●   Multiply the sum by 1.2 to build in room for growth — the recommended UPS rating should
       equal or exceed this final number.
   ●   Add extra VA capacity for motors, variable-speed drives, or laser printers to account for high
       power inrush at startup.
Redundant Deployment Architectures
   ●   N+1 Redundancy: One additional UPS unit beyond the number needed to support the load.
   ●   2N Redundancy: Enough UPS units to support the load in case of a full failure; used where
       continuous operation is critical.
   ●   2N+1 Redundancy: Combines N+1 and 2N benefits with extra units beyond the full 2N setup.

5. Variances and Exception Process
Any request to procure or deploy technology that differs from the standards and provisions stated
within this document must be requested of, and approved by, the "Owner of Standard" listed under
Roles & Responsibilities.
Requests may be acquired by emailing the Director of Network Services, including any required
documentation as part of standard procurement or deployment procedures. The request will be
evaluated by Network Services leadership, with written approval or denial given within 10 business
days, and stored in the Network Services Google Drive.

6. Definitions
UPS (Uninterruptible Power Supply): A device providing emergency power to a load when the
primary input power source fails, supplying near-instantaneous protection from batteries.
PDU (Power Distribution Unit): A device with multiple outputs designed to distribute electric power,
especially to racks of computers and networking equipment.
Backup Time (Runtime): The amount of time a UPS can supply power to its load from batteries when
the main power source is unavailable.
Capacity: The maximum power load a UPS can support, measured in VA or kVA.
Automatic Voltage Regulation (AVR): Stabilizes output voltage without switching to battery power.
Transfer Time: The time it takes for a UPS to switch from mains to battery power; ideally
instantaneous or within milliseconds.
SNMP: A protocol for managing devices on IP networks, including UPS systems, enabling remote
monitoring and management.

                                                                                            Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-013: UPS/PDU for Network Systems', links this file as https://drive.google.com/file/d/1p4pxd9yXTmugesIUhEsJEm9M-TyN26Zd/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1p4pxd9yXTmugesIUhEsJEm9M-TyN26Zd (the source URL above).
