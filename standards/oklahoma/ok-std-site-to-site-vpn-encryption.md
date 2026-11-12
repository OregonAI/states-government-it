---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-site-to-site-vpn-encryption
title: Site to Site VPN Encryption Standard
doc_type: standard
citation: OMES Site to Site VPN Encryption Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/site-to-site-vpn-encryption-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: f21c53dd0bf2e823aeba70e376e5187456f78b3bca0959471726d9da7342034b
effective_date: '2022-08-29'
source_version: Last revised 02/06/2025
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Site to Site VPN Encryption Standard (OMES Site to Site VPN Encryption Standard)

## At a glance

A CIO standard in the 'Network and Servers' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document establishes both the minimum and preferred configuration standards for IPsec VPN communications.

## Full text

                            Site to Site VPN Encryption Standard

Introduction
Data exchanged over the internet without encryption is vulnerable to security breach. To ensure the
confidentiality of conversations with remote partners along with the integrity of the exchanged data,
OMES Cyber Command, in cooperation with the OMES network team, must define which operational
virtual private network security parameters are acceptable.

Purpose
This document establishes both the minimum and preferred configuration standards for IPsec VPN
communications.

Definitions
IPsec – Internet Protocol Security is a widely used network layer security control for protecting
communications. IPsec is a framework of open standards for ensuring private communications over
Internet Protocol networks.

Standard
The preferred and minimum phase 1 and phase 2 security parameters are defined as follows:

        Preferred:

         Phase 1
         IKE Mode                            Main
         IKE Version                         V2
         Encryption Algorithm                AES-256-GCM
         Authentication Algorithm            SHA-384
         Key Exchange                        Group 19
         Lifetime (seconds)                  28800
         Authentication Method               PSK (Minimum 64 Characters)

         Phase 2
         Protocol                             ESP
         Encryption Algorithm                 AES-256-GCM
         Authentication Algorithm             HMAC-SHA-256
         Lifetime (seconds)                   3600
         PFS Key Group                        Group 19

         Minimum:

         Phase 1
         IKE Mode                              Main
         IKE Version                           V1
         Encryption Algorithm                  AES-128-CBC
         Authentication Algorithm              SHA-256
         Key Exchange                          Group 14
         Lifetime (seconds)                    28800
         Authentication Method                 PSK (Minimum 64 Characters)

         Phase 2
         Protocol                              ESP
         Encryption Algorithm                  AES-128-CBC
         Authentication Algorithm              HMAC-SHA-256
         Lifetime (seconds)                    3600
         PFS Key Group                         Group 14

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§ 34.11.1 and
34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended standards policies and
standards at any time. Compliance is expected with all published policies and standards, and any
published amendments thereof. Employees found in violation of this standard may be subject to
disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases and
projects to enable the chief information officer to assess the needs and capabilities of state agencies
as well as streamline and consolidate systems to ensure that the state delivers essential public
services to its citizens in the most efficient manner at the lowest possible cost to taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.

  Effective date: 08/29/2022           Review cycle: Annual
  Last revised: 02/06/2025             Last reviewed: 08/21/2026
  Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
