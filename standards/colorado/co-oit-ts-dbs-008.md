---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-dbs-008
title: Database User Administration
doc_type: standard
citation: TS-DBS-008
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1QUzqHtirlWGCvbUE3fVqRgkI4DF8iXS7
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 84c3786778b5cf15019d5b46f52e91cfdbd7d199a237c69a22284f2ea9fad825
effective_date: '2021-05-18'
source_version: 4.0, last updated 07-01-2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-008: Database User Administration'', links this file as https://drive.google.com/file/d/1QUzqHtirlWGCvbUE3fVqRgkI4DF8iXS7/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1QUzqHtirlWGCvbUE3fVqRgkI4DF8iXS7
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

# Database User Administration (TS-DBS-008)

## At a glance

OIT technical standard TS-DBS-008 (Data and Databases): Database User Administration. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-008: Database User Administration
  Document ID                      TS-DBS-008
  Title                            Database User Administration
  Executive Sponsor                Database Services Management, DBS Manager
  Issuing Authority                Governor's Office of Information Technology (OIT)
  Applies to                       OIT and OIT supported agencies; OIT DBS database
                                   administrators, OIT System administrators, and database users.
  Instrument Type                  Standard
  Version                          4.0
  Effective Date                   05-18-2021
  Last Updated                     07-01-2026

Purpose
This standard is issued under the authority of the Governor's Office of Information Technology
(OIT)(C.R.S. 24-37.5, et seq.), Office of Enterprise Architecture (Rule 8 CCR 1501-7).

Scope
These standards apply to OIT and OIT supported agencies. This Standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to
enforce technology standardization and assist in making the usage, support, and/or purchase of
technologies more consistent and efficient.
The standards assigned and prescribed by this document, instituted for use by the approval of the
OIT Architecture Review Board (ARB), should be used to govern purchase and deployment decisions
deemed as “go-forward” or “net-new” strategies or implementations, and are not intended for use
as retroactively enforceable mandate or policy for immediate conformance (especially in cases
where cost implications may be prohibitive). This standard shall in no way require OIT to support any
products and services not approved by OIT.
These standards apply to OIT and OIT supported agencies. They are to be used by OIT DBS database
administrators, OIT System administrators and database users.

Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●      Chairs and conducts business of the Architecture Review Board (ARB).
   ●      Update effective date and/or last review date.

                                                                                          Page 1 of 3

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
All OIT staff are responsible to be aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

DBS
   ●   Performs user administration on database platforms supported by DBS.

Business Application Owner
   ●   Provides DBS with predefined user access requirements.

Database User
   ●   Requests access for data or functionality to perform their job duties.

Standards
User Account Administration
   ●   Only OIT DBS database administrators will administer database user accounts.
   ●   Production database access will be granted upon receipt of service tickets from IAM.
   ●   Non-production database access will be granted upon receipt of service tickets.
   ●   User accounts will be password protected.
   ●   User accounts will be audited periodically.

Exceptions and Variance
Requests for variances from any provisions with this Standard must be requested using the Technical
Standard End User Exception Request Procedure.
The purpose of the Exception Request process is to address business or technical reasons for the
inability to adhere to one or more requirements in this standard.
Requests for exceptions should include compensating controls, that is, processes, technologies, or
procedures proposed used to mitigate any deviation from the standard requirement. The Secure
Configuration Exception Request form must be submitted to oit_ciso@state.co.us. Exception requests
will be processed and recommended for approval, conditional approval, or denial.

References
                                                                                          Page 2 of 3

Enforcement Category Chart

Colorado Information Security Policies (CISPs)
   ●   CISP-001 Access Control
   ●   CISP-003 Audit and Accountability
   ●   CISP-005 Configuration Management
   ●   CISP-009 System Maintenance
   ●   CISP-013 Risk Management
   ●   CISP-014 Systems and Services Acquisition
   ●   CSIP-015 System and Communications Protection
   ●   CISP-016 System and Information Integrity
   ●   TS-CISO-001 Data Security Categorization

Definitions
Standard: A rule that specifies a particular course of action or response to a given situation.
Standards are mandatory directives to carry out management's policies and are used to measure
compliance with policies. Standards serve as specifications for the implementation of policies and
are designed to promote implementation of high-level organization policy rather than to create new
policy in themselves.
Business Application Owner: The entity responsible for the business delivery of services, application
functionality, and is the custodian of the application data.
Least Privilege & Zero Trust: Users and applications have the minimal privileges access to data they
require to function properly.
Database User: Unique identifier that accesses the database.
DBS: OIT Database Services group
OEA (Office of Enterprise Architecture): The Office of Enterprise Architecture was formed as an
office under OIT by Governor's Rule 8 CCR 1501-7.
OIT (Office of Information Technology): The Governor's Office of Information Technology was
created and governed by C.R.S. 24-37.5, et seq.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification for granting the exception. Typically an exception request is
subject to review and approval by an authority in the area.

                                                                                            Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-008: Database User Administration', links this file as https://drive.google.com/file/d/1QUzqHtirlWGCvbUE3fVqRgkI4DF8iXS7/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1QUzqHtirlWGCvbUE3fVqRgkI4DF8iXS7 (the source URL above).
