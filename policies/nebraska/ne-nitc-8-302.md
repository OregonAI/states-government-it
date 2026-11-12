---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-302
title: 8-302. Passwords.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-302
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-302.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 984eec29c22a1a221fad78062ff790efaff25007600b725df65c668569e01c79
effective_date: null
source_version: History through November 8, 2024
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

# 8-302. Passwords. (NITC Technical Standards and Guidelines 8-302)

## At a glance

NITC Technical Standards and Guidelines section 8-302, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                             Nebraska Information Technology Commission
                                                                        Technical Standards and Guidelines

8-302. Passwords.
   (1) Minimum Password Requirements. The following are the minimum password
requirements for state government passwords:
   (a) Must contain a minimum of 12 characters;
    (b) Must contain at least three of the following: (i) at least one uppercase character; (ii) at
least one lowercase character; (iii) at least one numeric character; or (iv) at least one symbol
(!@#$%^&);
   (c) Must expire after 90 days;
   (d) Must have a minimum password age of at least 15 days prior to changing;
   (e) Must use multi-factor authentication;
   (f) Must not repeat any of the passwords used during the previous 366 days;
    (g) Accounts must automatically lock after three consecutive unsuccessful password
attempts;
   (h) Authentication and credentials must be transmitted over secure protocols; and
   (i) Default passwords must be changed before a system is put into production.
   (2) Restricted Account and Service Account Passwords. Non-expiring passwords may be
used for restricted accounts (“RA”) where the end user is not given the password and service
accounts (“SA”) that are used only for machine-to-machine communications. These accounts are
used for programmatic purposes only. For these use cases the following criteria apply:
   (a) Must contain a minimum of 20 characters;
   (b) Must only be used for a single purpose; and
   (c) Must be approved by the state information security officer.
    (3) System Equipment/Device Passwords. Agencies may use non-expiring passwords for
system equipment/devices. It is common for many devices (e.g., IP cameras, HVAC controls) in
today's IT environment to utilize login capabilities to protect the device from unauthorized
access. While many of these devices make use of a user ID and password in a manner like those
found while authenticating a user, the distinction to be made is that the user ID is used to
authenticate the device itself to the system and not a person in which case the following
requirements apply:

     (a) Must contain a minimum of 20 characters; and
     (b) Remote access and administration must use multi-factor authentication.
--
     History: Adopted on July 12, 2017. Amended on July 14, 2023 and November 8, 2024.
     URL: https://nitc.nebraska.gov/standards/8-302.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
