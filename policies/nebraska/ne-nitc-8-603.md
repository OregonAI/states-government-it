---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-603
title: 8-603. Separation of test and production environments.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-603
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-603.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 8163c9054a9b871be60d804c4bbc624379293fda4783d8135ef2d3c890fcd9c8
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

# 8-603. Separation of test and production environments. (NITC Technical Standards and Guidelines 8-603)

## At a glance

NITC Technical Standards and Guidelines section 8-603, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                          Nebraska Information Technology Commission
                                                                     Technical Standards and Guidelines

8-603. Separation of test and production environments.
    Development software and testing tools can cause serious problems to the production
environment if separation of these environments does not exist. Separation of the development,
test and production environments is required, either on physically separate machines or separated
by access controlled domains or directories. Processes must be documented and implemented to
govern the transfer of software from the development environment to the production platform.
Each agency must consider the use of a quality assurance environment where user acceptance
testing can be conducted. The following controls must be considered:
    (1) Access to compilers, editors and other system utilities must be removed from production
systems when not required;
   (2) Logon procedures and environmental identification must be sufficiently unique for
production testing and development;
    (3) Access to systems and business applications must be restricted to those individuals who
have a business need to access those resources in the performance of their job responsibilities;
and
    (4) It is recognized that at times, business or technical requirements dictate the need to test
with live data. In those cases, it is mandatory to have approval from the state information
security officer, and to implement production-class controls in the applicable test environment to
protect that information.
--
     History: Adopted on July 12, 2017.
     URL: https://nitc.nebraska.gov/standards/8-603.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
