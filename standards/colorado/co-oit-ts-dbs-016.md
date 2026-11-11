---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-dbs-016
title: Database Developer Service
doc_type: standard
citation: TS-DBS-016
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1VczQsyv5dEB0U5zBa8jKZzX0K4djI_bj
source_format: pdf
retrieved: '2026-11-11'
source_sha256: d25f903610a8e8bfd9de0048794e96b0442df515a907a9dfcc88667dc3ab925f
effective_date: '2026-07-01'
source_version: 4.0, last updated 07-01-2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-016: Database Developer Service'', links this file as https://drive.google.com/file/d/1VczQsyv5dEB0U5zBa8jKZzX0K4djI_bj/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1VczQsyv5dEB0U5zBa8jKZzX0K4djI_bj
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

# Database Developer Service (TS-DBS-016)

## At a glance

OIT technical standard TS-DBS-016 (Data and Databases): Database Developer Service. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-016: Database Developer Service
  Document ID                     TS-DBS-016
  Title                           Database Developer Service
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
stakeholder needs surrounding OIT supported databases, the following is submitted as the standard
for specifications, methodologies, and practices to provide the service.
The purpose of this document is to communicate the standards that the Governor's Office of
Information Technology (OIT) has developed with the intent of providing enterprise standard
configurations for Database Developer Service. Standards are based on a best-of-value decision
assessment involving multifarious factors, such as stakeholder needs, hardware configurations that
are serviced and supported by OIT, as well as operational and security best practices guidelines.
The ultimate purpose of the Database Developer Service is to describe the minimum requirements for
designing, installing, securing, monitoring, maintaining, protecting, and decommissioning any OIT
supported environment.

2. Scope
These standards apply to OIT and OIT supported agencies. This Standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to
enforce technology standardization and assist in making the usage, support, and/or purchase of
technologies more consistent and efficient.
Additionally, the standards assigned and prescribed by this document, instituted for use by the
approval of the OIT Architecture Review Board (ARB), should be used to govern purchase and
deployment decisions deemed as “go-forward” or “net-new” strategies or implementations, and are

                                                                                            Page 1 of 4

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
For the purpose of enforcement, this standard is rated CAT 2 according to the Enforcement Category
Chart.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●    Chairs and conducts business of the Architecture Review Board (ARB).
   ●    Update effective date and/or last review date.
   ●    Publish the ARB approved Standard to the OIT public facing website.

Architecture Review Board (ARB)
   ●    Engage stakeholders and subject matter experts to determine standard.
   ●    Review/Approve Standard (this document).

Database Services Management - DBS Manager
   ●    Owner of Standard.
   ●    Engage stakeholders and subject matter experts to determine standard.
   ●    Update document standards and version number.
   ●    Present to the Architecture Review Board for approval and adoption.

Additional Assignments
All OIT staff are responsible to be aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Goals
   ●    The Database Development Service ensures that customer databases are built consistently,
        securely, and accessible to the required application and approved users. This includes
        implementing requested changes by creating and modifying database Data Definition
        Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL) objects,
        Data Query Language (DQL), and Transaction Control Language (TCL), adding new data points
        and establishing new security protocols to secure data as well as troubleshooting.

                                                                                            Page 2 of 4

Process
   ●   Database Object Creation and Maintenance: Database Services will be responsible for the
       creation, update and maintenance of DDL including but not limited to tables, indexes, views,
       stored procedures, functions, packages, and triggers.
   ●   Database Development and Maintenance: Any database development and database code
       maintenance will be initiated by the business and worked by database services.
   ●   Database DevOps: Any and all database code will be created, reviewed and maintained in a
       version control system. (Refer to Database DevOps process)
   ●   Developer Database Privileges: Any developer outside of database services will be granted
       DML privileges of “select”, “update”, “insert”, and “delete” to development databases unless
       an exception is given needing a higher level of database access. All DDL changes will be
       completed by the Database Services team.
   ●   Database Architecture and Design: Database Services will design the database structure and
       system requirements including the data infrastructure to effectively store the data to be
       accessed from both internal and external sources. Database Services will analyze the business
       requirements and produce the data structure to meet these needs including data analysis and
       effective data flow throughout the system.
   ●   Supported Database Versions: Any database development supported by Database Services
       must be in the approved supported database versions listed in TS-DBS-001 Supported
       Databases and Versions.
   ●   Database User Administration: Database user creation and maintenance is defined in the
       database standard TS-DBS-008 Database User Administration.
   ●   Database Users and Security Maintenance: Controlling, monitoring, auditing user access, and
       enforcing password requirements to the database will be done by using least privilege as per
       the requirements listed in TS-DBS-006: Database Security.
   ●   Additional Database Developer Support and Services:
          ○   Database optimization
          ○   Query optimization
          ○   Working with large databases and datasets
          ○   Index maintenance
          ○   Performance Tuning
          ○   ORM Model development and troubleshooting

Requirements
   ●   Database Services will be involved in any new or existing development activity requiring
       database access and support.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of and approved by the “Owner of Standard” listed in
Section 3 (Roles and Responsibilities) of this document.
Requests may be acquired by using the “How-to Guide for Secure Configuration Exception Requests
or Policy Exception Requests in ServiceHub” and including the completed policy exception number
along with other documentation required as part of standard procedures when executing a
technology procurement or service deployment.

                                                                                          Page 3 of 4

6. References
OIT documents and policies
   ●   Colorado Information Security Policies (CISPs)
   ●   Enforcement Category Chart
   ●   TS-DBS-001 Supported Databases and Versions
   ●   TS-DBS-006: Database Security
   ●   TS-DBS-007: Database Software Management

State documents and policies
   ●   Colorado Brand Guidelines

7. Definitions
Standard: A rule that specifies a particular course of action or response to a given situation.
Standards are mandatory directives to carry out management's policies and are used to measure
compliance with policies. Standards serve as specifications for the implementation of policies and
are designed to promote implementation of high-level organization policy rather than to create new
policy in themselves.
Production Database: State Agency database used for production purpose to conduct State business.
Non-Production Database: State Agency database used for non-production purpose such as
development, testing, staging, demonstration or training.
Business: Employees of supported State agencies, and their respective stakeholders that use DBS
supported databases.
DDL: Data Definition Language
DML: Data Manipulation Language
DCL: Data Control Language
DQL: Data Query Language
TCL: Transaction Control Language
Database Object: A data structure used in a database to either store or reference data.
ORM: Object Relational Model
OEA (Office of Enterprise Architecture): The Office of Enterprise Architecture was formed as an
office under OIT by Governor's Rule 8 CCR 1501-7.
OIT (Office of Information Technology): The Governor's Office of Information Technology was
created and governed by C.R.S. 24-37.5, et seq.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification for granting the exception. Typically an exception request is
subject to review and approval by an authority in the area.

                                                                                            Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-016: Database Developer Service', links this file as https://drive.google.com/file/d/1VczQsyv5dEB0U5zBa8jKZzX0K4djI_bj/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1VczQsyv5dEB0U5zBa8jKZzX0K4djI_bj (the source URL above).
