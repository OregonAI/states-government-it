---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-dbs-001
title: Supported Databases and Versions
doc_type: standard
citation: TS-DBS-001
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1X_deJtmgRMouYfiF-ICbn1nBvgh6DqOv
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 90abc0bfc71a2bee98b59467fa63ca4f76f68d1cdfc7fdc417807289b3f9f36c
effective_date: '2021-07-01'
source_version: '4.01'
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-001: Supported Databases and Versions'', links this file as https://drive.google.com/file/d/1X_deJtmgRMouYfiF-ICbn1nBvgh6DqOv/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1X_deJtmgRMouYfiF-ICbn1nBvgh6DqOv
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Supported Databases and Versions (TS-DBS-001)

## At a glance

OIT technical standard TS-DBS-001 (Data and Databases): Supported Databases and Versions. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-001: Supported Databases and
Versions
  Document ID                    TS-DBS-001
  Title                          Supported Databases and Versions
  Executive Sponsor              Database Services Management, DBS Manager
  Issuing Authority              Governor’s Office of Information Technology (OIT)
  Applies to                     OIT and OIT-supported agencies, including employees of OIT,
                                 agencies supported by OIT, and vendors contracted by OIT or its
                                 stakeholders.
  Instrument Type                Standard
  Version                        4.01
  Effective Date                 07/01/2021
  Last Updated                   Not documented (Draft)

Purpose
OIT is statutorily mandated to provide IT support and services to the State and its
stakeholders in the most effective and efficient manner possible (as defined by C.R.S. 24-
37.5). To satisfy stakeholder needs surrounding OIT-supported databases and their versions,
this document is submitted as the standard for specifications, methodologies, and practices
to provide the service.
This document communicates the standards OIT has developed with the intent of providing
enterprise standard configurations for supported databases and their currently supported
versions, based on a best-of-value decision assessment involving factors such as stakeholder
needs, hardware configurations serviced and supported by OIT, and operational and security
best practices.
The ultimate purpose of this standard is to describe the minimum requirements for database
support for the agencies, ensuring an easily supported environment that eases maintenance
and minimizes style conflicts, while meeting minimum requirements for security and
accessibility for government.

Scope
These standards apply to OIT and OIT-supported agencies. This standard shall be used by
employees of OIT, agencies supported by OIT, and vendors contracted by OIT or its
stakeholders, as a means to enforce technology standardization and assist in making the
usage, support, and/or purchase of technologies more consistent and efficient.
                                                                                  Page 1 of 4

Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern
purchase and deployment decisions deemed “go-forward” or “net-new”, and are not intended
as a retroactively enforceable mandate for immediate conformance, especially where cost
implications may be prohibitive.
Standards are predicated on the assumption that there can be no point of enforcement unless
and until there is an effort to re-procure, renew (contracts), reconfigure (including
upgrades), or redevelop the system. When an investment decision is made to sustain or
improve the system, conformance to existing standards should be part of the assessed level of
effort. For guidance or enforcement in conformance to standards, an email request may be
sent to OIT_OEA@state.co.us with the subject line “Request for Architecture Review:
<projectName/systemName>”.
For the purpose of enforcement, this standard is rated CAT 1 according to the Enforcement
Category Chart.

Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●    Chairs and conducts business of the Architecture Review Board (ARB).
   ●    Updates effective date and/or last review date.
   ●    Publishes the ARB-approved Standard to the OIT public-facing website.

Architecture Review Board (ARB)
   ●    Engages stakeholders and subject matter experts to determine the standard.
   ●    Reviews/approves the Standard (this document).

Database Services Management - DBS Manager
   ●    Owner of Standard.
   ●    Engages stakeholders and subject matter experts to determine the standard.
   ●    Updates document standards and version number.
   ●    Presents to the Architecture Review Board for approval and adoption.

Additional Assignments
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and
its purposes of authority and governance in support of OIT's statutorily mandated mission in
service of Colorado State Government affairs.
   ●    Database Services Management: Responsible for enforcement and approval of changes
        to policies, standards, guidelines, and procedures.
   ●    Database Services Database Administrator (DBA): Responsible for knowing and
        adhering to policies, standards, guidelines, and procedures as part of job description.

Standards
Goals
Ensure Database Services is able to provide support, patches, and upgrades specific to
database platforms, versions, and environments.

Supported Architectures
                                                                                     Page 2 of 4

   ●   Specific supported architectures and versions are maintained in the IAW Technology
       Standards document.
   ●   SQL Server - Current version minus 2 releases.
   ●   Oracle - Current version minus 1 release.
   ●   Informix - Maintain at the level referenced in the IAW Technology Standards
       document.
   ●   AWS Cloud support - MySQL, Aurora DB, SQL Server, Oracle, DynamoDB, PostgreSQL,
       Redshift.
   ●   Azure Power Platform Dataverse.

Requirements
Database Services will be involved in database version selection and database platform
preferences.

Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions
stated within this document must be requested of, and approved by, the “Owner of Standard”
listed under Roles and Responsibilities.
Exception requests may be acquired by completing the “EXCEPTION REQUEST to Technical
Standard” form and including the completed form (with all signatures) along with other
documentation required as part of standard procedures when executing a technology
procurement or service deployment.

References
   ●   OIT documents and policies
   ●   State of Colorado Style Library
   ●   TS-OEA-001: Technology Accessibility for Persons with Disabilities
   ●   Enforcement Category Chart
   ●   IAW Technology Standards
   ●   State documents and policies
   ●   Colorado Brand Guidelines
   ●   C.R.S. 24-37.5-101, et seq.

Definitions
   ●   Production Database: State Agency database used for production purposes to conduct
       State business.
   ●   Non-Production Database: State Agency database used for non-production purposes
       such as development, testing, staging, demonstration, or training.
   ●   Business: Employees of supported State agencies, and their respective stakeholders,
       who use DBS-supported databases.
   ●   SDS: Enterprise Application development group responsible for application
       development.
   ●   OEA (Office of Enterprise Architecture): Formed as an office under OIT by Governor's
       Rule 8 CCR 1501-7.
   ●   OIT (Office of Information Technology): Created and governed by C.R.S. 24-37.5, et
       seq.
                                                                                   Page 3 of 4

●   Exception request: A document requesting an exception to a recognized standard,
    requiring a business or technical justification for granting the exception, subject to
    review and approval by an authority in the area.

                                                                                  Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-001: Supported Databases and Versions', links this file as https://drive.google.com/file/d/1X_deJtmgRMouYfiF-ICbn1nBvgh6DqOv/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1X_deJtmgRMouYfiF-ICbn1nBvgh6DqOv (the source URL above).
