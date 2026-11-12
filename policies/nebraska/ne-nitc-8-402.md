---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-402
title: 8-402. Network transmission security.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-402
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-402.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 08a3257fd498f5aa229c518969bc771228b3a42da3c43584eb547b2a3aba7e0d
effective_date: null
source_version: History through July 14, 2023
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). source_version is the latest date on the section's History line (adoption, renumbering or
  amendment); the section prints no separate effective date, so effective_date stays empty.
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

# 8-402. Network transmission security. (NITC Technical Standards and Guidelines 8-402)

## At a glance

NITC Technical Standards and Guidelines section 8-402, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                                    Nebraska Information Technology Commission
                                                                               Technical Standards and Guidelines

8-402. Network transmission security.
     The following are network transmission security requirements:
    (1) All encryption must be approved by the state information security officer. Any
transmissions over unsecured networks (such as the Internet) that contain HIGH IMPACT or
MODERATE IMPACT information must be encrypted using technology that is FIPS 140-2
compliant;
    (2) Network scanning and monitoring is prohibited, unless prior approval is obtained from
the Office of the CIO. If approved, scanning must be restricted to authorized and registered IP
addresses only, and conducted by authorized personnel only;
    (3) The Office of the CIO shall ensure that all networks and systems are monitored 24x7
with authorized tools (such as network based intrusion detection and prevention systems) and
personnel to detect system anomalies or security events; and
   (4) Passwords and SNMP community names may not be sent in clear text over open
networks. All devices must use authorized encryption for access authorization to the state
network. Access to the DMZ applications is exempt from this requirement.
--
     History: Adopted on July 12, 2017. Amended on July 14, 2023.
     URL: https://nitc.nebraska.gov/standards/8-402.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
