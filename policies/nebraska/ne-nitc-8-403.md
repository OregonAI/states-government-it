---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-403
title: 8-403. Network architecture requirements.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-403
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-403.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: e8d5c0066137450c41b37e9424b2a17326c3d1b86fb7822d2b95b1bacbafd663
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

# 8-403. Network architecture requirements. (NITC Technical Standards and Guidelines 8-403)

## At a glance

NITC Technical Standards and Guidelines section 8-403, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                                    Nebraska Information Technology Commission
                                                                               Technical Standards and Guidelines

8-403. Network architecture requirements.
     The following are network architecture requirements:
    (1) All devices that store, access, or process HIGH IMPACT or MODERATE IMPACT
information must not reside in the public tier, and must be protected by at least two firewalls.
Firewalls must be placed at perimeter locations so that all critical systems are protected by
multiple firewalls and monitoring systems;
   (2) All publicly accessible devices must be located in an access-controlled environment, and
access credentials must be managed by authorized personnel;
    (3) All network devices that contain or process HIGH IMPACT or MODERATE IMPACT
data must be secured with a password-protected screen saver that automatically locks the session
after no more than 15 minutes of inactivity;
    (4) Devices that include native host-based firewall software in the operating system must
have the firewall activated and properly configured, unless the active firewall software
compromises the usability of critical applications, or lessens the posture of other security
systems;
    (5) The state network will have an annual verification of all open ports, protocols, and
services for publicly accessible systems;
    (6) Any requests for public IP addresses or for additional open ports must be approved by the
state information security officer;
   (7) Staff will follow approved change control and configuration management procedures for
network devices. Patches and hot-fixes recommended by network hardware or software vendors
must be installed as soon as practical after testing; and
    (8) Services and applications that will not be used must be disabled or removed if such action
will not negatively impact operations. Protocols such as telnet, VNC, RDP, or others that do not
actively support approved encryption should only be used if they are performed over a secondary
encryption channel, such as SSL or IPSEC.
--
     History: Adopted on July 12, 2017. Amended on July 14, 2023.
     URL: https://nitc.nebraska.gov/standards/8-403.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
