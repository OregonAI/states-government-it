---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-version-control-and-hosting
title: Version Control and Hosting Standard
doc_type: standard
citation: OMES Version Control and Hosting Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/version-control-hosting.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 6b9e475e3a096e6173c9d86755a724b5ac3311beaa8b3eba4cec7bd72aae4bf9
effective_date: '2022-04-13'
source_version: Last revised 04/12/2022
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Version Control and Hosting Standard (OMES Version Control and Hosting Standard)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document defines and outlines the procedures software developers should use when contributing code to custom software developed by OMES.

## Full text

                          Version Control and Hosting Standard

Introduction
Version control, also known as source code control or just source control, relates to the need to
manage the change history of source code within a system over time. All OMES custom source
code must be version controlled and it is the developer’s responsibility to ensure this is the case
for all code they work with or for which they are responsible. All OMES source code should also
use Git and be hosted in GitHub.

Purpose
This document defines and outlines the procedures software developers should use when
contributing code to custom software developed by OMES.

Definitions
COBOL - Common Business Oriented Language.

Standard
   • Azure DevOps.
          o Agencies within the State of Oklahoma use Azure DevOps for software project
             and enhancement management, scrum team collaboration and automated
             building and released custom software. Agencies use GitHub for source code
             hosting. All customer application source code uses Git for version control and is
             hosted in GitHub unless an exception waiver and approval has been obtained.
   • Git.
          o Agency custom development Git is the default choice. Git works well with agile
             project development and the continuous integration/continuous deployment tool
             within Azure DevOps and other Microsoft development tools. Git tools outside of
             Microsoft tools are supported.
   • File base.
          o In some situations, it may be difficult to store source code in Git (i.e. COBOL as
             part of a mainframe system or Microsoft Access applications.) In this case, Git
             offers large file storage support options.
   • GitHub visibility.
          o GitHub repositories must be private or internal and only shared with contributors.
             A repository with an internal visibility designation can be viewed by all members
             of the enterprise while private visibility is only within the agency organization. The
             continuous integration/continuous deployment tool within Azure DevOps can
             connect to repositories hosted on GitHub.
   • Alternate repository hosting system.
          o If Git is not available for version control or host repositories on GitHub, additional
             approval is needed from leadership.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§
34.11.1 and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended
standards policies and standards at any time. Compliance is expected with all published policies
and standards, and any published amendments thereof. Employees found in violation of this
standard may be subject to disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases
and projects to enable the chief information officer to assess the needs and capabilities of state
agencies as well as streamline and consolidate systems to ensure that the state delivers
essential public services to its citizens in the most efficient manner at the lowest possible cost to
taxpayers.

References
   • Agile project development.
   • Azure DevOps.
   • Azure pipelines documentation.
   • Git.
   • Git large file storage.
   • GitHub.
   • Setting repository visibility.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 04/13/2022         Review cycle: Annual
 Last revised: 04/12/2022           Last reviewed: 04/04/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
