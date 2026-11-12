---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-304
title: 8-304. Privileged access accounts.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-304
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-304.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 5d015ca39861132a6d53ee643ef7fbb504e827f1426fd8709a16f9044d301481
effective_date: null
source_version: History through November 10, 2022
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

# 8-304. Privileged access accounts. (NITC Technical Standards and Guidelines 8-304)

## At a glance

NITC Technical Standards and Guidelines section 8-304, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                          Nebraska Information Technology Commission
                                                                     Technical Standards and Guidelines

8-304. Privileged access accounts.
    Privileged access accounts include administrator accounts, embedded accounts used by one
system to connect to another, and accounts used to run service programs. These accounts are
used by systems and personnel to access sensitive files, execute software, load and configure
policies and configuration settings, and set up or maintain accounts.
   Due to the elevated access levels these accounts typically have, the following standards and
procedures must be followed to minimize the risk of incidents caused by these accounts:
   (1) All privileged access accounts must be assigned to an individual with an approved
business need for the privileged access. These accounts must not be shared;
   (2) All privileged access accounts must use OCIO-approved multi-factor authentication
where technically possible;
   (3) Service accounts must not be used to interactively log in to a system or resource;
    (4) Default administrator accounts must be renamed, removed or disabled. Default passwords
for renamed or disabled default administrator accounts must be changed;
    (5) Default system account credentials for hardware and software must be either disabled, or
the password must be changed. Use of anonymous accounts is prohibited, and unassigned
accounts must be assigned to an individual prior to use. When no longer needed, the account
must be disabled. At all times, the state requires individual accountability for use of privileged
access accounts;
    (6) Privileged access accounts must have enhanced activity logging enabled and reviewed at
least quarterly;
   (7) Privileged access through remote channels will be allowed for authorized purposes only
and must include multi-factor authentication;
   (8) Passwords for these accounts must be changed every 60 days;
   (9) The password change process must support recovery of managed systems from backup
media. Historical passwords should remain accessible in a history table in the event that they are
needed to activate a backup copy of a system; and
   (10) Privileged access accounts must be approved, provisioned, and maintained by the
Office of the CIO.
   Exceptions to this policy may be granted by the state information security officer.

--
     History: Adopted on July 12, 2017. Amended on March 10, 2022 and November 10, 2022.
     URL: https://nitc.nebraska.gov/standards/8-304.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
