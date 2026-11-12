---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-statewide-network-labeling
title: Statewide Network Labeling Standard
doc_type: standard
citation: OMES Statewide Network Labeling Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/statewide-network-labeling-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 5ca102b0359d168941d6034226de87c752dee05226c13688f85fb625c942a211
effective_date: '2025-06-17'
source_version: Last revised 05/13/2025
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Statewide Network Labeling Standard (OMES Statewide Network Labeling Standard)

## At a glance

A CIO standard in the 'Network and Servers' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: The purpose of this standard is to set consistency across port numbers and wireless access points. The goal is to have consistent number and easy identifications should any repairs need to take place. This standard applies to all customer-facing data ports and associated wireless access points and should be followed on all new installations and labeling projects.

## Full text

                                 Network Labeling Standard

Introduction
Structured cabling projects require consistency and consistent identification for future repairs
and interactive future projects. By setting a standard for network labeling going forward, the
Office of Management and Enterprise Services can ensure ease of work going forward.

Purpose
The purpose of this standard is to set consistency across port numbers and wireless access
points. The goal is to have consistent number and easy identifications should any repairs need
to take place. This standard applies to all customer-facing data ports and associated wireless
access points and should be followed on all new installations and labeling projects.

Definitions
AP – Access Point.
OMES – Office of Management and Enterprise Services.

Standard
The following practices for network labeling should be observed:
   • Patch Panel Labeling – Customer-Facing Data Ports.
           o Format: [Floor] . [Closet Number] - [Port Number].
                   Example:
                           • 1.1-001 = Floor 1, Closet 1, Port 1.
           o Instructions:
                   Label only customer-facing data ports using this format.
                   Number closets per floor using .1, .2, etc.
                           • Example:
                                  o 1.1 = Floor 1, Closet 1.
                                  o 1.2 = Floor 1, Closet 2
                   Label patch panel ports sequentially across all panels in the rack:
                           • Example:
                                  o Panel 1: 1.1-001 to 1.1-048.
                                  o Panel 2: 1.2-049 to 1.1-096
                           • Continue as needed, without restarting numbering per panel.
                   Labels must be durable, clearly legible and affixed directly to the patch
                      panel at the rack.
   • Wireless Access Point Labeling.
           o At the rack:
                   Format: AP- ###.
                           • Example:
                                 o AP-001, AP-002, etc.
                   This label identifies the patch panel port where the AP is terminated.
           o On the AP device itself:
                   Format: AP - ### - XXXX
                           • Where XXXX is the last four characters of the MAC address.
                   Example:
                           • AP-001-3F5C.

                    The label should be affixed directly to the AP device in a clearly visible
                     location.
          o Instructions:
                  AP numbers should be assigned sequentially within the building.
                  Ensure each AP’s rack port (AP - ###) corresponds with its device label
                     (AP - ### - XXXX).
   •   General Guidelines.
          o This standard applies to all customer-facing data ports and wireless access
             points statewide.
          o Avoid duplicate numbering within any closet or building.
          o Always use padded port numbers (e.g., 001, 002) for consistency and storability.
          o For any classification or edge cases, contract OMES prior to installation.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§
34.11.1 and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended
standards policies and standards at any time. Compliance is expected with all published policies
and standards, and any published amendments thereof. Employees found in violation of this
standard may be subject to disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases
and projects to enable the chief information officer to assess the needs and capabilities of state
agencies as well as streamline and consolidate systems to ensure that the state delivers
essential public services to its citizens in the most efficient manner at the lowest possible cost to
taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 06/17/2025         Review cycle: Annual
 Last revised: 05/13/2025           Last reviewed: 11/20/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
