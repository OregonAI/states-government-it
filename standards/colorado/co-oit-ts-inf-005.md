---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-005
title: Structured Cabling
doc_type: standard
citation: TS-INF-005
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1B4EzwfWXJ8S0AllXfdp4GLUIVCwWzPqJ
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 5e26b8924dc90221532c1ca42e13a55aecd995c7f73ee05970e0bafd2f7e368f
effective_date: '2023-03-16'
source_version: 4.0, last updated 12/31/2025
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-005: Structured Cabling'', links this file as https://drive.google.com/file/d/1B4EzwfWXJ8S0AllXfdp4GLUIVCwWzPqJ/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1B4EzwfWXJ8S0AllXfdp4GLUIVCwWzPqJ
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

# Structured Cabling (TS-INF-005)

## At a glance

OIT technical standard TS-INF-005 (Infrastructure): Structured Cabling. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-005: Structured Cabling
  Document ID                     TS-INF-005
  Title                           Structured Cabling
  Executive Sponsor               Network Services, Sr. Manager of Network Operations
  Issuing Authority               Office of Information Technology (OIT)
  Applies to                      Any facility, site, or physical location maintained by, or in
                                  service of, an agency of the Executive Branch of the Colorado
                                  State Government.
  Tier                            Standard
  Version                         4.0
  Effective Date                  03/16/2023
  Last Updated                    12/31/2025

1. Purpose
OIT is statutorily obligated to provide IT support and services to the State and its stakeholders in the
most effective and efficient manner possible (as defined by C.R.S. 24-37.5). To satisfy stakeholder
needs surrounding Structured Cabling, this document is submitted as the standard for technology,
specifications, methodologies, and practices to provide the service.
The ultimate purpose of this standard is to describe the minimum requirements for installing
structured cabling at new and existing building sites that support Local Area Networks (LAN) and
Voice connectivity, so as to: accommodate the functional requirements of present and future
information services; support a multi-product and multi-vendor environment; facilitate the planning
and installation of cabling systems; and ensure uniformity of structured wiring and hardware
infrastructure installations in all State Agency facilities.

2. Scope
This standard governs the technology, practices, and materials used when installing cabling at any
facility, site, or physical location maintained by, or in service of, an agency of the Executive Branch
of the Colorado State Government.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
                                                                                             Page 1 of 4

   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Network Services - Sr. Manager of Network Operations
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Updates document standards and version number.
   ●   Presents to the Architecture Review Board for approval and adoption.
Network Operations and Engineers
   ●   Review floor plans and possible site surveys.
   ●   Initiate cabling quotes with approved cabling vendors.
   ●   Verify cabling is completed, review test reports, and update port mapping floor plans.
   ●   Set up network configuration after completing cabling.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Entrance Facilities (EF)
   ●   Must conform to ANSI/TIA/EIA-569 requirements.
   ●   At least two (2) four-inch underground conduits from the existing communication pedestal to
       the DMARC.
   ●   Conduit shall be installed using sweeps, not elbows, with no more than three bends and total
       bends not exceeding 270 degrees.
   ●   The conduit shall provide a pre-installed pull-string.
   ●   A minimum 4x4 plywood backboard is required in DMARC areas, installed in a secure area
       accessible only to those authorized by OIT Network Services.
Telecommunications Rooms (TR) / Data Closet
   ●   Consult ANSI/TIA/EIA 569 for design and provisioning requirements.
   ●   Room penetrations must be properly firestopped in compliance with applicable codes.
   ●   Ventilation and air conditioning (HVAC) must be present and operational 24 hours a day, 365
       days a year.
   ●   All equipment racks, cabinets, and systems must be properly connected to the independent
       ground bus per ANSI/TIA/EIA 607.
Horizontal Cabling
   ●   All components of the horizontal cabling system must be from the same manufacturer.
   ●   No horizontal cable should be exposed within the building area.
   ●   All copper cables shall be positioned at a minimum of 4 inches from any EMI-emitting device.

                                                                                           Page 2 of 4

   ●   Any new cabling runs must meet the CAT6e minimum rating or better.
   ●   All horizontal drops must be patched into a switch port so all ports are active.
Cable Length
   ●   Maximum distance between the telecommunications outlet and the horizontal cross-connect:
       90 meters.
   ●   Maximum length of all patch cords and jumpers in the telecommunications closet: 5 meters.
   ●   Total channel link length shall not exceed 100 meters (328 feet).
Backbone Cabling
   ●   Hierarchical star topology — each horizontal cross-connect connects to the main or
       intermediate cross-connect.
   ●   No more than two hierarchical levels of cross-connects in the backbone.
   ●   Recognized cables: 100 ohm twisted pair; 50/125 or 62.5/125 micron multimode fiber; single-
       mode fiber.
Test and Certify Cabling
   ●   Contracted vendor must test all wires with a Level III cable tester to certify conformance to
       ANSI/TIA/EIA-568-B specifications.
   ●   Printed and electronic Pass/Fail results must include: electrical length, cross-talk, end-to-end
       attenuation, continuity, and date of test.
   ●   Optical link testing must follow ANSI/TIA/EIA-568-B.3 for multi-mode fiber and ANSI/TIA/EIA-
       526-7 method A for single-mode fiber.
Port Mapping
   ●   All ports shall be labeled at the wall port, matching the label on the patch panel in the
       telecommunications room.
   ●   The agency, landlord, or general contractor will provide a digital copy of the current building
       floor plan.
   ●   After installation, the cabling vendor will update the floor plan with labeled port numbers at
       each cable drop.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of, and approved by, the "Owner of Standard" listed under
Roles and Responsibilities.
Requests may be acquired by emailing the Senior Network Operations Manager and including other
documentation required in standard procedures when executing a technology procurement or service
deployment.

6. References
   ●   TIA-568-C.0 through C.3, Commercial Building Telecommunications Cabling Standards
   ●   TIA-569-B, Commercial Building Standards for Telecommunications Pathways and Spaces
   ●   ANSI/TIA-606, Administration Standard for Commercial Telecommunications Infrastructures
   ●   ANSI J-STD-607-A, Commercial Building Grounding and Bonding Requirements for
       Telecommunications

                                                                                            Page 3 of 4

   ●   TIA-942, Telecommunications Infrastructure Standard for Data Centers

7. Definitions
DMARC: Demarcation point — the point at which the public switched telecommunications network
ends and connects with the customer's on-premises wiring.
Entrance Facilities: The entrance point for outside plant cable from telephone companies, private
network cables, and other access providers.
Horizontal Cabling: The portion of the cabling system extending from the work area outlet through
the wall/ceiling/floor to the patch panel in the telecommunications room.
Backbone Cabling: The interbuilding and intrabuilding cable connections between entrance
facilities, equipment rooms, and telecommunications closets.
Structured Cable: Building or campus telecommunications cabling infrastructure comprising
standardized smaller elements (subsystems), governed by standards specifying wiring for data
centers, offices, and apartment buildings.
Telecommunications Rooms: The critical point between the work area and the Equipment Room or
main cross-connect through backbone cabling and horizontal distribution.

                                                                                        Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-005: Structured Cabling', links this file as https://drive.google.com/file/d/1B4EzwfWXJ8S0AllXfdp4GLUIVCwWzPqJ/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1B4EzwfWXJ8S0AllXfdp4GLUIVCwWzPqJ (the source URL above).
