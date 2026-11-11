---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-dbs-017
title: DBMS Software Installation
doc_type: standard
citation: TS-DBS-017
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1naTGRqt5_QHzzAW8Z8MXje3m-eZSA4Fj
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 601deacfd7f847efc2edbce4bf464a79b11d808801c166c1d5374991fc482450
effective_date: '2023-06-01'
source_version: 4.0, last updated 07-01-2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-017: DBMS Software Installation'', links this file as https://drive.google.com/file/d/1naTGRqt5_QHzzAW8Z8MXje3m-eZSA4Fj/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1naTGRqt5_QHzzAW8Z8MXje3m-eZSA4Fj
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

# DBMS Software Installation (TS-DBS-017)

## At a glance

OIT technical standard TS-DBS-017 (Data and Databases): DBMS Software Installation. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-017: DBMS Software Installation
  Document ID                    TS-DBS-017
  Title                          DBMS Software Installation
  Executive Sponsor              Database Services Management, DBS Manager
  Issuing Authority              Governor's Office of Information Technology (OIT)
  Applies to                     OIT and OIT supported agencies; OIT DBS database
                                 administrators, OIT System administrators, and database users.
  Instrument Type                Standard
  Version                        4.0
  Effective Date                 06-01-2023
  Last Updated                   07-01-2026

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
For the purpose of enforcement, this standard is rated CAT 1 according to the Enforcement Category
Chart.

                                                                                          Page 1 of 3

Roles and Responsibilities
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

Agency
   ●   Work with the DBA Team to establish the purpose and requirements for each request.
   ●   Obtain all necessary SQL Server and other licenses.
   ●   Establish data classification and retention requirements.

Enterprise Applications
   ●   Work with the DBA Team to provide information about the application or applications that
       will be utilizing the Database environment(s).

DBS Team
   ●   Best practices of database installation will be adhered to based on platform specific database
       technology.

Additional Assignments
All OIT staff are responsible to be aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.
Database Services Database Administrator (DBA) is responsible for knowing and adhering to policies,
standards, guidelines, procedures as part of job description.

Standards
   ●   Create a baseline server configuration to optimize data availability, security, data recovery.
   ●   New database installations and migrations will follow the most recent Major Release
       supported and approved by DBS when appropriate to the client environment.
   ●   Adhere to best practices for installation of the database platform for the specific
       environment.
   ●   Any request to procure or deploy technology that is a variance to the standards and provisions
       stated within this document must be requested of and approved by the “Owner of Standard”
       listed in Roles and Responsibilities of this document.
                                                                                             Page 2 of 3

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
OIT documents and policies
   ●   Colorado Information Security Policies (CISPs)
   ●   TS-CISO-001 Data Security Categorization
   ●   Enforcement Category Chart

Definitions
Authorization: The action or fact of authorizing or being authorized; or a document giving
permission or authority.
Database: A collection of tables, stored procedures, views, indexes, constraints, jobs that contain
and manage a discrete set of data, i.e. for a single application.
Database Environment: A single installation of the Database software.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification for granting the exception. Typically an exception request is
subject to review and approval by an authority in the area.
OEA (Office of Enterprise Architecture): The Office of Enterprise Architecture was formed as an
office under OIT by Governor's Rule 8 CCR 1501-7.
OIT (Office of Information Technology): The Governor's Office of Information Technology was
created and governed by C.R.S. 24-37.5, et seq.
Standard: A rule that specifies a particular course of action or response to a given situation.
Standards are mandatory directives to carry out management's policies and are used to measure
compliance with policies. Standards serve as specifications for the implementation of policies and
are designed to promote implementation of high-level organization policy rather than to create new
policy in themselves.

                                                                                            Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-017: DBMS Software Installation', links this file as https://drive.google.com/file/d/1naTGRqt5_QHzzAW8Z8MXje3m-eZSA4Fj/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1naTGRqt5_QHzzAW8Z8MXje3m-eZSA4Fj (the source URL above).
