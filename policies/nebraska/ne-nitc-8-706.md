---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-706
title: 8-706. Logging; auditable events.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-706
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-706.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: c49dc33890555cffc3c0c7aaea9511375f72e3e96e922561d98a0b66e79561c3
effective_date: null
source_version: History through July 12, 2017
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

# 8-706. Logging; auditable events. (NITC Technical Standards and Guidelines 8-706)

## At a glance

NITC Technical Standards and Guidelines section 8-706, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                         Nebraska Information Technology Commission
                                                                    Technical Standards and Guidelines

8-706. Logging; auditable events.
    Security safeguard regulations require logging and reviewing events that are determined to
have a moderate or above level of risk. Auditable events may be incorporated into system auto
logs and change management documents. The following events should be logged and reviewed
on a weekly basis:
   (1) Log on and off the system;
   (2) Change of password;
   (3) All system administrator commands, while logged on as system administrator;
   (4) Switching accounts or running privileged actions from another account (e.g., Linux/Unix
SU or Windows RUNAS);
   (5) Creation or modification of super-user groups;
    (6) Subset of security administrator commands, while logged on in the security administrator
role;
   (7) Subset of system administrator commands, while logged on in the user role;
   (8) Clearing of the audit log file;
   (9) Startup and shutdown of audit functions;
   (10) Use of identification and authentication mechanisms (e.g., user ID and password);
   (11) Change of file or user permissions or privileges (e.g., use of suid/guid, chown, su);
  (12) Remote access outside of the corporate network communication channels (e.g.,
modems, dedicated VPN) and all dial-in access to the system;
   (13) Changes made to an application or database by a batch file;
   (14) Application-critical record changes;
   (15) Changes to database or application records, where the application has been bypassed to
produce the change (via a file or other database utility);
   (16) All system and data interactions concerning FTI;
   (17) Additional platform-specific events, as defined by agency needs or requirements;
   (18) Detection of suspicious or malicious activity such as from an intrusion detection or
prevention system (IDS/IPS), anti-virus system, or anti-spyware system; and

   (19) Physical entrance or access to secured and restricted areas or facilities where system
and network infrastructure reside.
--
     History: Adopted on July 12, 2017.
     URL: https://nitc.nebraska.gov/standards/8-706.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
