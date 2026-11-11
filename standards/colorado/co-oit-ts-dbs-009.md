---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-dbs-009
title: Database Decommissioning
doc_type: standard
citation: TS-DBS-009
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1BaeEhbDk7w9s-k_ZYOs3FpuyUeNBFP-D
source_format: pdf
retrieved: '2026-11-11'
source_sha256: cc807bc2535b553e5d390f259b773fc672d2a590223e9ccfc447860cdd84d23e
effective_date: '2018-05-19'
source_version: 6.0, last updated 07-01-2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-009: Database Decommissioning'', links this file as https://drive.google.com/file/d/1BaeEhbDk7w9s-k_ZYOs3FpuyUeNBFP-D/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1BaeEhbDk7w9s-k_ZYOs3FpuyUeNBFP-D
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

# Database Decommissioning (TS-DBS-009)

## At a glance

OIT technical standard TS-DBS-009 (Data and Databases): Database Decommissioning. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-009: Database Decommissioning
  Document ID                    TS-DBS-009
  Title                          Database Decommissioning
  Executive Sponsor              Database Services Management, DBS Manager
  Issuing Authority              Governor's Office of Information Technology (OIT)
  Applies to                     OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and
                                 vendors contracted by OIT or its stakeholders.
  Instrument Type                Standard
  Version                        6.0
  Effective Date                 05-19-2018
  Last Updated                   07-01-2026

Purpose
This standard is issued under the authority of the Governor's Office of Information Technology
(OIT)(C.R.S. 24-37.5, et seq.), Office of Enterprise Architecture (Rule 8 CCR 1501-7).
The purpose of this document is to communicate the standards that the Governor's Office of
Information Technology (OIT) has developed in order to provide enterprise standard configurations
for Database Decommissioning. Standards are based on a best-of-value decision assessment involving
multiple factors, such as stakeholder needs, hardware configurations that are serviced and supported
by OIT, as well as operational and security best practices guidelines.

Scope
These standards apply to OIT, state agencies as defined in C.R.S. 24-37.5-101(28) and vendors
contracted by OIT or its stakeholders as a means to enforce technology standardization and assist in
making the usage, support, and/or purchase of technologies more consistent and efficient.
The standards assigned and prescribed by this document, instituted for use by the approval of the
OIT Architecture Review Board (ARB), should be used to govern purchase and deployment decisions
deemed as “go-forward” or “net-new” strategies or implementations, and are not intended for use
as retroactively enforceable mandate or policy for immediate conformance (especially in cases
where cost implications may be prohibitive). This standard shall in no way require OIT to support any
products and services not approved by OIT.
For the purpose of enforcement, this standard is rated CAT 2 according to the Enforcement Category
Chart.

                                                                                          Page 1 of 4

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

Database Services Management
   ●   Responsible for enforcement and approval of changes of policies, standards, guidelines,
       procedures.

Database Services Database Administrator
   ●   Responsible for knowing and adhering to policies, standards, guidelines, procedures as part of
       the job description.

Additional Assignments
All OIT staff are responsible to be aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

Standards
   ●   Decommissioning of production databases requires business approval and an approved Service
       Hub Change ticket.
   ●   Decommissioning of non-production databases does not require business approval but does
       require an EA manager approved ServiceHub Change Request ticket.
   ●   ServiceHub Change Requests will require the following information:
          ○   Decommissioning date and time
          ○   Specific database servers on which databases reside
          ○   Specific database instances in which databases reside
          ○   Specific databases to be decommissioned
   ●   Databases to be decommissioned will be made unavailable to users on date and time of
       decommissioning and prior to archive and backup.
   ●   A consistent backup will be performed at the decommission time and date.
   ●   Database backups will be stored in the designated storage area for 30 days.

                                                                                          Page 2 of 4

   ●   DBS will submit a Server Decommission Request form to the Server Team if the last database
       on the server is decommissioned.

Variance and Exception Process
Requests for variances from any provisions with this Standard must be requested using the Technical
Standard End User Exception Request Procedure.
The purpose of the Exception Request process is to address business or technical reasons for the
inability to adhere to one or more requirements in this standard.
Requests for exceptions should include compensating controls, that is, processes, technologies, or
procedures proposed used to mitigate any deviation from the standard requirement. The Secure
Configuration Exception Request form, Secure Configuration Exception Request (template effective
17-May-2024) DO NOT EDIT - MAKE A COPY.docx must be submitted to oit_ciso@state.co.us.
Exception requests will be processed and recommended for approval, conditional approval, or denial.

References
OIT documents and policies
   ●   Colorado Information Security Policies (CISPs)
   ●   Enforcement Category Chart

Definitions
Standard: A rule that specifies a particular course of action or response to a given situation.
Standards are mandatory directives to carry out management's policies and are used to measure
compliance with policies. Standards serve as specifications for the implementation of policies and
are designed to promote implementation of high-level organization policy rather than to create new
policy in themselves.
Database Management system (DBMS): A software application that interacts with end-users, other
applications, and the database itself to capture and analyze data.
Database Server: A virtual or physical server capable of running the DBMS software.
Database Instance: A set of background database processes/threads and a shared memory, which is
memory that is shared across those threads/processes running on a single database server.
Production Database: State Agency database used for production purpose to conduct State business.
Non-Production Database: State Agency database used for non-production purpose such as
development, testing, staging, demonstration or training.
Backup: A restorable set of data.
Archive: A restorable set of data created for long term storage.
User: Employees of OIT and supported State agencies, and their respective stakeholders that use DBS
supported databases.
Servicehub Ticket: Service ticket entered through the online OIT Servicehub Desk Management.
EA: Enterprise Application development group responsible for application development.
Designated Storage Area: Device space reserved for hosting database backups and archives.

                                                                                          Page 3 of 4

OEA (Office of Enterprise Architecture): The Office of Enterprise Architecture was formed as an
office under OIT by Governor's Rule 8 CCR 1501-7.
OIT (Office of Information Technology): The Governor's Office of Information Technology was
created and governed by C.R.S. 24-37.5, et seq.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification for granting the exception. Typically an exception request is
subject to review and approval by an authority in the area.

                                                                                            Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-009: Database Decommissioning', links this file as https://drive.google.com/file/d/1BaeEhbDk7w9s-k_ZYOs3FpuyUeNBFP-D/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1BaeEhbDk7w9s-k_ZYOs3FpuyUeNBFP-D (the source URL above).
