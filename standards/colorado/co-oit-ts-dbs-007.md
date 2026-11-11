---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-dbs-007
title: Database Software Management
doc_type: standard
citation: TS-DBS-007
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1zSCjDtsmi0g0rommDx0oHz5_5364dySs
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 4300063a87006ac3ded223d49deeac74427cf64a8aafb667e71b639e0c0d99c5
effective_date: '2026-07-01'
source_version: 4.0, last updated 07-01-2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-007: Database Software Management'', links this file as https://drive.google.com/file/d/1zSCjDtsmi0g0rommDx0oHz5_5364dySs/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1zSCjDtsmi0g0rommDx0oHz5_5364dySs
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

# Database Software Management (TS-DBS-007)

## At a glance

OIT technical standard TS-DBS-007 (Data and Databases): Database Software Management. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-007: Database Software Management
  Document ID                     TS-DBS-007
  Title                           Database Software Management
  Executive Sponsor               Database Services Management, DBS Manager
  Issuing Authority               Governor's Office of Information Technology (OIT)
  Applies to                      OIT and OIT supported agencies; employees of OIT, agencies
                                  supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Instrument Type                 Standard
  Version                         4.0
  Effective Date                  07-01-2026
  Last Updated                    07-01-2026

1. Purpose
OIT is statutorily mandated to provide IT support and services to the State and its stakeholders in the
most effective and efficient manner possible (as defined by C.R.S. 24-37.5). To satisfy the
stakeholder needs surrounding Database Software Management, the following is submitted as the
standard for OIT Database Services to provide the service.
The purpose of this document is to communicate the standards that the Governor's Office of
Information Technology (OIT) has developed with the intent of providing enterprise standard
configurations for Database Software Management. Standards are based on a best-of-value decision
assessment involving multifarious factors, such as stakeholder needs, hardware configurations that
are serviced and supported by OIT, as well as operational and security best practices guidelines.
The ultimate purpose of the Database Software Management Standard is to describe the minimum
requirements for designing, installing, securing, monitoring, maintaining, protecting, and
decommissioning any OIT supported DBMS environment.
The purpose of this policy is to document the scope of responsibilities of OIT Database Services (DBS)
to ensure appropriate database software management in order to maintain and secure the database
environments on DBS supported database platforms.

2. Scope
These standards apply to OIT and OIT supported agencies. This Standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to
enforce technology standardization and assist in making the usage, support, and/or purchase of
technologies more consistent and efficient.

                                                                                            Page 1 of 4

Additionally, the standards assigned and prescribed by this document, instituted for use by the
approval of the OIT Architecture Review Board (ARB), should be used to govern purchase and
deployment decisions deemed as “go-forward” or “net-new” strategies or implementations, and are
not intended for use as retroactively enforceable mandate or policy for immediate conformance
(especially in cases where cost implications may be prohibitive).
Any/all standards are predicated with the assumption that there can be no point of enforcement
unless and until there is an effort to re-procure, renew (contracts), reconfigure (including upgrades),
or redevelop the system. At any time that a decision is made to make an investment of resources in
sustaining or improving the system, conformance to existing standards should be part of the assessed
level of effort for that investment activity. For guidance (or enforcement) in conformance to
standards during any of these types of activities, an email request may be sent to
OIT_OEA@state.co.us with the subject line “Request for Architecture Review:
<projectName/systemName>”
This standard applies to OIT DBS database administrators, OIT system administrators, and database
users.
For the purpose of enforcement, this standard is rated CAT 1 according to the Enforcement Category
Chart.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Update effective date and/or last review date.
   ●   Publish the ARB approved Standard to the OIT public facing website.

Architecture Review Board (ARB)
   ●   Engage stakeholders and subject matter experts to determine standard.
   ●   Review/Approve Standard (this document).

Database Services Management - DBS Manager
   ●   Owner of Standard.
   ●   Engage stakeholders and subject matter experts to determine standard.
   ●   Update document standards and version number.
   ●   Present to the Architecture Review Board for approval and adoption.

Additional Assignments
DBS Team
   ●   Performs all database related installations, migrations, upgrades, patching and administration
       of database on the database server.
   ●   Ensures that the data and the database structures are backed up, stored on secure storage,
       accessible only to authorized personnel and could be recovered when required.
   ●   Ensures that production database environments are kept separate from non-production
       environments.
   ●   Manages database user security on supported database platforms.
   ●   Audits database activity in accordance with recommended security settings contained in the
       CIS database benchmark for the appropriate platform and version of database software.
                                                                                            Page 2 of 4

SA Team
   ●   Performs operating system or other server related software installations, upgrades and
       patching.
   ●   Provides access for DBS database administrators to the “super user” (root) account on OIT
       supported Linux environments and Local Administrator account privileges on Windows
       environments.
   ●   Manages OS user security on DBS supported database servers on behalf of the DBS.

Database User
   ●   Requests access for only data or functionality required to perform their job duties.
All OIT staff are responsible to be aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Database Software Management
   ●   It is the policy of OIT DBS that DBS will be responsible for and perform all Database related
       installations, migrations, upgrades, patches and administration of database binaries on the
       database server.
   ●   It is the policy of OIT DBS that DBS is not responsible for, nor will perform operating system or
       other server related software upgrades or patches. However, DBS will be responsible for
       evaluation, coordination, and approval of any software upgrades on database servers.
   ●   It is the policy of OIT DBS that non-database software not directly supporting database
       operations is not permitted on database servers.
   ●   It is the policy of OIT DBS that new database installations, upgrades and migrations will follow
       the most recent Major Release supported and approved by DBS when appropriate to the client
       environment.
   ●   It is the policy of OIT DBS that major releases will be maintained with the second most recent
       Maintenance Release Number when appropriate.
   ●   It is the policy of OIT DBS that production database software and patches will be applied
       when available after appropriate evaluation in the non-production database environments by
       DBS.
   ●   It is the policy of OIT DBS that all new installations, releases, and upgrades will pass User
       Acceptance Testing (UAT) prior to being deployed in a production environment.
   ●   It is the policy of OIT DBS that all production database installations will reside on isolated
       server environments from non-production database, application, backup, redundancy and
       other related products unless required.
   ●   It is the policy of OIT DBS that only Database Services approved client database software
       installations will be supported.

5. Compliance
All DBS team staff, OIT SA Team staff, and database users must comply with this policy in order to
secure, access, store data, and maintain database servers. Non-compliance of this policy may result
in corrective action.

                                                                                              Page 3 of 4

6. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of and approved by the “Owner of Standard” listed in
Section 3 (Roles and Responsibilities) of this document.
Requests may be acquired by completing the “EXCEPTION REQUEST to Technical Standard” form and
including the completed form (including all signatures) along with other documentation required as
part of standard procedures when executing a technology procurement or service deployment.

7. References
OIT documents and policies
   ●   CISP-003 Information Technology Security Risk Management Policy
   ●   Enforcement Category Chart
   ●   TS-INF-003: Identity and Access Administration

Third-party resources
   ●   CIS Benchmarks
   ●   CIS Oracle Database 12c Benchmark v3.0.0
   ●   CIS Oracle Database 19c Benchmark v1.0.0
   ●   CIS Microsoft SQL Server Benchmark

8. Definitions
Standard: A rule that specifies a particular course of action or response to a given situation.
Standards are mandatory directives to carry out management's policies and are used to measure
compliance with policies. Standards serve as specifications for the implementation of policies and
are designed to promote implementation of high-level organization policy rather than to create new
policy in themselves.
DBS: OIT Database Services Team
SA: OIT Server or System Administration Team
CIS: Center for Internet Security
CISO: Chief Information Security Officer
OEA (Office of Enterprise Architecture): The Office of Enterprise Architecture was formed as an
office under OIT by Governor's Rule 8 CCR 1501-7.
OIT (Office of Information Technology): The Governor's Office of Information Technology was
created and governed by C.R.S. 24-37.5, et seq.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification for granting the exception. Typically an exception request is
subject to review and approval by an authority in the area.

                                                                                            Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-007: Database Software Management', links this file as https://drive.google.com/file/d/1zSCjDtsmi0g0rommDx0oHz5_5364dySs/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1zSCjDtsmi0g0rommDx0oHz5_5364dySs (the source URL above).
