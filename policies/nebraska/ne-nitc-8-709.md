---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-709
title: 8-709. Logging; application logging review and monitoring.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-709
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-709.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: dec067128a974ff1a38a39b74095c4c57a7cd4204d8c477958595d5f5c8a5924
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

# 8-709. Logging; application logging review and monitoring. (NITC Technical Standards and Guidelines 8-709)

## At a glance

NITC Technical Standards and Guidelines section 8-709, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                              Nebraska Information Technology Commission
                                                                         Technical Standards and Guidelines

8-709. Logging; application logging review and monitoring.
    All state applications must provide logging for security events. Application logs are
invaluable data for identifying security incidents, monitoring policy violations, establishing
baselines, providing information about problems and unusual conditions, contributing additional
application-specific data for incident investigation which is lacking in other log sources, and
helping defend against vulnerability identification and exploitation through attack detection.
   Application logging content must be part of the overall system analysis and design activity,
and should consider:
     (1) Application process startup, shutdown, or restart;
     (2) Application process abort, failure, or abnormal end;
     (3) Significant input and output validation failures;
    (4) Business process monitoring (e.g., activity abandonment, transactions, connections,
information requests);
     (5) Audit trails (e.g., data addition, modification and deletion, data exports);
     (6) Performance monitoring (e.g., data load time, page timeouts);
     (7) Compliance monitoring and regulatory, legal, or court ordered actions;
     (8) Authentication and authorization successes and failures;
     (9) Session management failures;
   (10) Use of higher-risk functionality (e.g., addition or deletion of application credentials,
changes to privileges, assigning users to tokens, adding or deleting tokens, submission of user-
generated content - especially file uploads); and
     (11) Suspicious, unacceptable or unexpected behavior.
    Application logs must be reviewed at least monthly. Corrective actions to address application
deficiencies must be managed through the application development process or the applicable
corrective action planning process.
--
     History: Adopted on July 12, 2017.
     URL: https://nitc.nebraska.gov/standards/8-709.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
