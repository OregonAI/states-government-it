---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-707
title: 8-707. Logging; audit log contents.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-707
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-707.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: b24dab55779b3d538d52856426660355c2a3d14fa5e9b3e4c781729914a27e9b
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

# 8-707. Logging; audit log contents. (NITC Technical Standards and Guidelines 8-707)

## At a glance

NITC Technical Standards and Guidelines section 8-707, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                          Nebraska Information Technology Commission
                                                                     Technical Standards and Guidelines

8-707. Logging; audit log contents.
    Audit logs must contain sufficient information to establish what events occurred, the sources
of the events, and the outcomes of the events. The logs must identify or contain at least the
following elements, or enough information in which to infer the following elements with
reasonable assurance:
   (1) Type of action (e.g., authorize, create, read, update, delete, and accept network
connection);
    (2) Subsystem performing the action (e.g., process or transaction name, process or
transaction identifier);
    (3) Identifiers (as many as available) for the subject requesting the action (e.g., user name,
computer name, IP address, and MAC address). Note that such identifiers should be standardized
to facilitate log correlation;
    (4) Date and time the action was performed, including relevant time-zone information if not
in Coordinated Universal Time;
     (5) Whether the action was allowed or denied by access-control mechanisms;
   (6) Description or reason-codes of why the action was denied by the access-control
mechanism, if applicable; and
   (7) Depending on the nature of the event that is logged, there may be other information
necessary to collect.
--
     History: Adopted on July 12, 2017.
     URL: https://nitc.nebraska.gov/standards/8-707.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
