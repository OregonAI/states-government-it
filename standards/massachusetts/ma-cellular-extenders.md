---
schema_version: 1
corpus: states-government-it
jurisdiction: massachusetts
id: ma-cellular-extenders
title: Guidelines for Acceptable Use of Cellular Extenders and the Commonwealth Network Infrastructure
doc_type: standard
citation: Guidance for Cellular Extenders (policy advisory dated 04/25/2024)
authority_level: ''
issuing_body: Executive Office of Technology Services and Security
source_url: https://www.mass.gov/doc/guidelines-for-acceptable-use-of-cellular-extenders-and-the-commonwealth-network-infrastructure/download
source_format: pdf
retrieved: '2026-11-11'
source_sha256: aa097e016b9177c945371ab8540f3a779c33500489ee8bcbd8799a5f0adf6b7d
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Guidelines for Acceptable Use of Cellular Extenders and the Commonwealth Network Infrastructure (Guidance for Cellular Extenders (policy advisory dated 04/25/2024))

## At a glance

An 'EOTSS Defined Standard' on the acceptable use of cellular extenders on the Commonwealth network infrastructure (G.L. c. 7D, section 2). Network security rather than telecommunications service, so seeded; a reviewer may treat it as telecom (see left_out).

## Full text

                               EOTSS Defined Standards
                             Guidance for Cellular Extenders

Contents
Background ..................................................................................................................................... 2
Guidance ......................................................................................................................................... 3
Contact EOTSS ............................................................................................................................... 3
Document History ......................................................................................................................... 4

Background
What is a Cellular Extender?
All major cellular carriers have the capability to provide a device that plugs into a network,
establishes a connection via the internet to the carrier’s data center, and provides localized
cellular service within proximity around the device. These are known as “cellular extenders”,
“femtos”, “efemtos”, “Super Femto Cell Access Points”, etc.

While these devices are a quick and easy way for carriers to address in-building coverage issues,
this approach shifts support to EOTSS and simultaneously puts the customer at risk.

How Did EOTSS Make this Decision?
For the reasons listed in more detail below, EOTSS will not allow or support any cellular
extenders on the Commonwealth network.

Decision Point 1: Single Point of Failure
Use of cellular extenders on the Commonwealth network will potentially establish a single point
of failure. Because these devices would leverage the Commonwealth network over a standard
internet connection, all data, voice, and cellular communications would be contingent on the
network’s availability. While EOTSS strives for 100% uptime, unforeseen technological failures
can occur, rendering all communication methods inaccessible until the Commonwealth network
is restored. In the event of an outage caused by factors like weather, there is risk of an
extended period without communications.

Decision Point 2: Support
Given that these devices are not commodity devices or part of our portfolio (like laptops and
desktops), EOTSS cannot provide support for installation or the use of these devices.
Additionally, utilizing EOTSS infrastructure would shift the responsibility for addressing cellular
quality issues and cellular coverage within facilities to EOTSS, aspects for which we are presently
not equipped to support.

Decision Point 3: Security
These devices are considered “Internet of Things” (IoT) since they require internet connectivity.
The communication involves encryption, making it challenging for EOTSS and our security
systems to discern whether the traffic is legitimate or malicious.

Guidance
We are committed to offering guidance on available options and continue to actively participate
in discussions between our customers and ITT72 Category 1 approved cellular carriers to
identify acceptable solutions, ensure a mutual understanding of our concerns, and
collaboratively work towards comprehensive solutions for their services.

Solutions
EOTSS has provided and encouraged the carriers to offer two (2) solutions:

Option 1:
A fully managed network solution, where the cellular provider (and/or their third party)
provides a diverse internet connection, installs the cellular extender(s) and manages the cellular
extender(s) on that network connection.

Option 2:
Known as “inbuilding cellular”, cellular repeaters are used where antennas are placed on the
exterior of the building and cables from those antennas are run to a central device that
“repeats” the signal to the interior of the building.

Multiple Agencies in One Facility:
For facilities accommodating multiple agencies, carriers are urged to collaborate with the facility
manager to establish a unified offering for an entire facility. This will minimize the number of
solutions per location.

Multiple Carriers in One Facility:
In situations where buildings need support for multiple carriers, it is advisable to contemplate
the use of a carrier-agnostic cellular repeater. This approach aims to reduce the space and
infrastructure requirements necessary to accommodate the communication needs of the
building’s occupants.

Contact EOTSS
We at EOTSS certainly understand the situation and agree that cellular (like any wireless
medium) is a necessity today. If you have any questions or would like EOTSS to participate in
discussions between with your carrier to find an acceptable solution, you may reach out to Brad
Steele, Director of MassVoice: brad.steele@mass.gov.

  Document History
Version   Author/Editor       Reason for Change                                    Date
1.0       Brad Steele, Rob    Initial Document                                     2/27/2024
          Guerriero
2.0       Jessica Powers      Reformatted document template; edited language for   7/1/2024
                             clarity

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
