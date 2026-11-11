---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-dbs-005
title: Database Backup and Recovery
doc_type: standard
citation: TS-DBS-005
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1Q-Qtsqn3--v-HPcRQ0j7gHKlU7WTLydn
source_format: pdf
retrieved: '2026-11-11'
source_sha256: aee4ee02bfb0479182568d94d5636cc1261f77271e04152f67901da0ad40383d
effective_date: '2021-01-28'
source_version: 4.0, last updated 07/01/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-005: Database Backup and Recovery'', links this file as https://drive.google.com/file/d/1Q-Qtsqn3--v-HPcRQ0j7gHKlU7WTLydn/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1Q-Qtsqn3--v-HPcRQ0j7gHKlU7WTLydn
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

# Database Backup and Recovery (TS-DBS-005)

## At a glance

OIT technical standard TS-DBS-005 (Data and Databases): Database Backup and Recovery. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-005: Database Backup and Recovery
  Document ID                    TS-DBS-005
  Title                          Database Backup and Recovery
  Executive Sponsor              Database Services Management, DBS Manager
  Issuing Authority              Governor’s Office of Information Technology (OIT)
  Applies to                     OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and
                                 vendors contracted by OIT or its stakeholders.
  Instrument Type                Standard
  Version                        4.0
  Effective Date                 01/28/2021
  Last Updated                   07/01/2026

Purpose
This standard is issued under the authority of the Governor's Office of Information Technology
(OIT) (C.R.S. 24-37.5, et seq.) and the Office of Enterprise Architecture (Rule 8 CCR 1501-7).
It communicates the standards OIT has developed for database backup and recovery in all
database environments on DBS-supported database platforms.
Standards are based on a best-of-value decision assessment involving multiple factors, such as
stakeholder needs, hardware configurations serviced and supported by OIT, and operational
and security best practices.

Scope
These standards apply to OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and
vendors contracted by OIT or its stakeholders, as a means to enforce technology
standardization and assist in making the usage, support, and/or purchase of technologies
more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern
purchase and deployment decisions deemed “go-forward” or “net-new”, and are not intended
as a retroactively enforceable mandate for immediate conformance, especially where cost
implications may be prohibitive. This standard shall in no way require OIT to support any
products and services not approved by OIT.
For the purpose of enforcement, this standard is rated CAT 1 according to the Enforcement
Category Chart.

                                                                                   Page 1 of 3

Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.

Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews/approves the Standard (this document).

Database Services Management - DBS Manager
   ●   Owner of Standard.
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Updates document standards and version number.
   ●   Presents to the Architecture Review Board for approval and adoption.

DBS Team
   ●    Performs all database-related installations, migrations, upgrades, patching, and
        administration of databases on the database server.
    ● Ensures data and database structures are backed up, stored on secure storage,
        accessible only to authorized personnel, and can be recovered when required.
    ● Ensures production database backups are kept separate from non-production database
        backups.
    ● Manages database user security on supported database platforms.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and
its purposes of authority and governance in support of OIT's statutorily mandated mission in
service of Colorado State Government affairs.

Standards
   ●   DBS will be responsible for the backup and recovery of all DBS-supported databases.
   ●   Database backup, archival, and retention will follow federal statutes, state statutes,
       and business requirements.
   ●   In the absence of any of the above retention policies, DBS will retain backups for a
       maximum of 30 days.
   ●   Additional levels of database backup, retention, and recovery, as requested by the
       data owner, will be reviewed by DBS.

Variance and Exception Process
Requests for variances from any provision of this standard must be requested using the
Technical Standard End User Exception Request Procedure.
The Exception Request process addresses business or technical reasons for the inability to
adhere to one or more requirements in this standard. Requests for exceptions should include
compensating controls — processes, technologies, or procedures proposed to mitigate any
deviation from the standard requirement. Use the Secure Configuration Exception Request

                                                                                     Page 2 of 3

form; see the How-to Guide for Secure Configuration Exception Requests or Policy Exception
Requests in ServiceHub. Exception requests will be processed and recommended for approval,
conditional approval, or denial.

References
   ●   OIT documents and policies
   ●   State of Colorado Style Library
   ●   TS-OEA-001: Technology Accessibility for Persons with Disabilities
   ●   Enforcement Category Chart
   ●   State documents and policies
   ●   Colorado Brand Guidelines
   ●   C.R.S. 24-37.5-101, et seq.
   ●   CISP-001: Access Control
   ●   TS-CISO-001: Data Security Categorization
   ●   TS-INF-003: Identity and Access Administration

Definitions
   ●   Standard: A rule that specifies a particular course of action or response to a given
       situation. Standards are mandatory directives to carry out management's policies and
       are used to measure compliance with policies.
   ●   DBS: Database Services
   ●   DBA: Database Administrator
   ●   System Administrator or SysAdmin
   ●   CIS: Center for Internet Security
   ●   CISO: Chief Information Security Officer
   ●   OEA (Office of Enterprise Architecture): Formed as an office under OIT by Governor's
       Rule 8 CCR 1501-7.
   ●   OIT (Office of Information Technology): Created and governed by C.R.S. 24-37.5, et
       seq.
   ●   Exception request: A document requesting an exception to a recognized standard,
       requiring a business or technical justification for granting the exception, subject to
       review and approval by an authority in the area.

                                                                                   Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-005: Database Backup and Recovery', links this file as https://drive.google.com/file/d/1Q-Qtsqn3--v-HPcRQ0j7gHKlU7WTLydn/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1Q-Qtsqn3--v-HPcRQ0j7gHKlU7WTLydn (the source URL above).
