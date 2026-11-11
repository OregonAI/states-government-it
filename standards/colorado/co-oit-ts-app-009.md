---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-app-009
title: Continuous Integration Servers (Custom Applications)
doc_type: standard
citation: TS-APP-009
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=14IXmAmcX1WWDqJKIW877DRIAOECZRHtk
source_format: pdf
retrieved: '2026-11-11'
source_sha256: c22fc60265187a041ffc24be3938902ce5f399be3ee3f421212e20dd3152e095
effective_date: '2025-09-02'
source_version: 4.0, last updated 12/09/2025
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-APP-009: Continuous Integration Servers'', links this file as https://drive.google.com/file/d/14IXmAmcX1WWDqJKIW877DRIAOECZRHtk/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=14IXmAmcX1WWDqJKIW877DRIAOECZRHtk
  (the source URL above).'
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

# Continuous Integration Servers (Custom Applications) (TS-APP-009)

## At a glance

OIT technical standard TS-APP-009 (Applications): Continuous Integration Servers (Custom Applications). OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-APP-009: Continuous Integration Servers
(Custom Applications)
  Document ID                     TS-APP-009
  Title                           Continuous Integration Servers (Custom Applications)
  Executive Sponsor               Enterprise Applications, Director of Enterprise Applications
  Issuing Authority               Governor’s Office of Information Technology (OIT)
  Applies to                      OIT and OIT-supported agencies, including employees of OIT,
                                  agencies supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Instrument Type                 Standard
  Version                         4.0
  Effective Date                  09/02/2025
  Last Updated                    12/09/2025

1. Purpose
OIT is statutorily obligated to provide IT support and services to the State and its stakeholders
in the most effective and efficient manner possible (as defined by C.R.S. 24-37.5). This
document is submitted as the standard for the technology, specifications, methodologies, and
practices to provide Continuous Integration and to satisfy stakeholder needs surrounding this
service.
This document defines the standard methods that Enterprise Applications shall use to support
delivery of a Continuous Integration Server (build automation, artifact management,
deployment process management, role-based access, and state authentication constructs)
through the adoption, use, and maintenance of an in-house Continuous Integration Server.
This technical standard is intended to be used as a comparator against proposed future
Continuous Integration Servers. A rational determination of a specific server will enable more
efficient support services and security, provide additional stability across development teams,
improve consistency, and enable automation of common tasks.

2. Scope
These standards apply across OIT and agencies supported by OIT. This standard shall be used
by employees of OIT, agencies supported by OIT, and vendors contracted by OIT or its
stakeholders as a means to enforce technology standardization and assist in making the usage,
support, and/or purchase of technologies more consistent and efficient. This is applicable to
new solutions requested and major changes to existing solutions, developed by OIT staff as
                                                                                   Page 1 of 4

well as vendors developing solutions for which OIT will provide day-forward maintenance and
support.
This document is intended for Enterprise Applications, but applies to any OIT unit providing
these services to customers.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.

Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews/approves the Standard (this document).

Enterprise Applications - Director of Enterprise Applications
    ● Owner of Standard.
    ● Engages stakeholders and subject matter experts to determine the standard.
    ● Updates document standards and version number.
    ● Presents to the Architecture Review Board for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and
its purposes of authority and governance in support of OIT's statutorily mandated mission in
service of Colorado State Government affairs.

4. Standards
Continuous Integration Server Qualification
The CI process must be provided by a product identified in the current OIT Certified Standard
Product for Continuous Integration Servers and provide the following required capabilities:
   ●   Ability to manage scheduled automated builds.
   ●   Ability to manage automated builds based on events such as an update to a code
       branch.
   ●   Easy installation and numerous plugins to support CI pipeline tasks.
   ●   Custom plugin creation abilities.
   ●   Build snapshots.
   ●   Manage (create, store, export, and import) continuous integration pipeline
       configurations.
   ●   Scheduled and automated test execution.
   ●   Ability to create custom scripts (e.g., database migration, sanity tests).
   ●   Securely and automatically pull from code repositories.
   ●   Support scripting to extend the pipeline (e.g., Bash, shell, Perl scripts).
   ●   Built-in, configurable email notifications for events.
   ●   Store states of deployment servers and allow rollbacks.
   ●   Support backups, restores, and disaster recovery.

                                                                                     Page 2 of 4

   ●   Enable a collaborative environment where multiple developers can simultaneously
       contribute to projects and quickly verify results.
   ●   Improved code maintenance with all code centralized in a single location and built by
       a single tool.
   ●   Improve software quality.
   ●   Provide visibility and insight into the health of development efforts in real time.
   ●   Increase awareness and simplify decision making for when to deploy or continue
       testing.

Security Verifiable
Any Continuous Integration Server considered for use in development, deployments, or any
aspect supported by OIT and/or its vendors is required to be compatible and compliant with
security scanning and assurance tools. All Continuous Integration Servers are subject to
vulnerability scanning, assessment, and mitigation prior to approval for deployment to a
production environment.

Portability
Continuous Integration Servers shall be portable due to their collaborative nature and may be
hosted across many platforms, infrastructures, and architectures. Interaction with the server
should be system-agnostic.

Security Frameworks
Continuous Integration Servers must be configurable to prevent common security
vulnerabilities such as unauthenticated access, malicious builds, malicious build agents, and
malicious users. State applications are to comply with the level of security specified in OIT's
Information Security Policies.

Accelerators
Continuous Integration Servers shall offer accelerators such as plugins for build automation,
scheduled job automation features, pipeline creation tools, multi-pipeline capabilities, built-
in support for Version Control, health monitoring tools, and other features for rapid
development and delivery of build automation.

Sustainability
Products and services may be considered sustainable when rationally accounted for from both
a budgetary and staff support perspective, including licensing/maintenance planning and
ongoing lifecycle, security, patching, and support/KLO planning.

Authentication
Continuous Integration Servers shall be able to support authentication with Google and
Microsoft platforms.

5. Variance and Exception Process
Exceptions to any portion of this standard may be requested via the OIT Secure Configuration
Exception Request Form, as posted on OIT Plaza.

                                                                                     Page 3 of 4

6. References
  ●   OIT and Information Security Policies (see OIT Plaza - Policies): This document
      establishes operational standards for OIT. All staff following these standards shall do
      so in compliance with all other OIT policies as published. In the event of any perceived
      conflict, OIT Policies shall prevail.

7. Definitions
  ●   Continuous Integration (CI): The practice of merging working developer copies to a
      shared mainline on frequent intervals.
  ●   Continuous Integration (CI) Server: Provides the functions to support CI technical
      processes.
  ●   Source Code Control: A version control system designed to track changes in source
      code and other text files during software development.

                                                                                   Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-APP-009: Continuous Integration Servers', links this file as https://drive.google.com/file/d/14IXmAmcX1WWDqJKIW877DRIAOECZRHtk/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=14IXmAmcX1WWDqJKIW877DRIAOECZRHtk (the source URL above).
