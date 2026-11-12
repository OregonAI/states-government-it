---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-8-604
title: 8-604. Application development.
doc_type: policy
citation: NITC Technical Standards and Guidelines 8-604
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/8-604.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: fbf3fcf305c41ae4219af9f69173e99359356e8dfcb6cbc610a7a51031bd2f53
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

# 8-604. Application development. (NITC Technical Standards and Guidelines 8-604)

## At a glance

NITC Technical Standards and Guidelines section 8-604, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102), in the Information Security Policy of chapter 8, whose scope is all IT systems for which the state has administrative responsibility (8-102).

## Full text

                                                           Nebraska Information Technology Commission
                                                                      Technical Standards and Guidelines

8-604. Application development.
    The following standards are required to be followed for agency developed application
software that create, process, or store HIGH IMPACT or MODERATE IMPACT data:
    (1) The agency must establish an application change management processes with assigned
responsibilities to ensure all changes to applicable application software are approved and
documented. Change management teams will include appropriate application development staff
and appropriate staff to represent state information security requirements;
   (2) The change management processes may vary depending on the data application size and
configuration, however all processes must include formal procedures with tools to support the
documentation, review and approval for each change request;
    (3) The change management processes must retain a documented history of the change
process as it passes through the application development life cycle with documentation securely
stored for audit purposes. Documentation should address a review of the following: change
summary, justification, and timeline; functionality, regression, integrity, and security test plans
and results; security review and impact analysis; documentation and baseline updates; and
implementation timeline and recovery plans;
    (4) Changes to software applications must be controlled and production installations must be
made by personnel assigned to update production libraries. Mechanisms to maintain and ensure
the integrity of the application code must be implemented;
    (5) Changes to production libraries should not be the same personnel who made the
application changes unless documented procedures are in place which ensure the confidentiality,
integrity, and availability of the data maintained in the production library;
    (6) Application development changes that impact agency IT infrastructure must be submitted
to the Infrastructure Change Control Team for review, approval, and implementation;
    (7) The security requirements of new applications must be established, documented and
tested prior to their acceptance and use. The agency information security officer must ensure that
acceptance criteria are utilized for new applications and upgrades. Acceptance testing must be
performed to ensure security requirements are met prior to the application being migrated to the
production environment;
     (8) All applications are required to maintain up-to-date documentation that includes an
assessment of security threats and impacts, and a detailed description of the data handling with
its accurate classification;

    (9) Applications that provide user interfaces must have an appropriate warning banner
displayed, applicable to the data being accessed (e.g., PHI, FTI, PII);
    (10) Application credentials, where possible, should be inherited from the state managed
authentication source. If that is not possible, credentials should have the same level of
management and approval as other agency access credentials; and
    (11) Applications must be configured such that HIGH IMPACT or MODERATE IMPACT
data will be encrypted when transmitted outside the agency internal network.
--
     History: Adopted on July 12, 2017. Amended on July 14, 2023.
     URL: https://nitc.nebraska.gov/standards/8-604.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
