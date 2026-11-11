---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-dbs-014
title: Database Support in Cloud Services
doc_type: standard
citation: TS-DBS-014
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1hgnj6YC3CyjrbXKvoOn5_EwJTJ_WH2oZ
source_format: pdf
retrieved: '2026-11-11'
source_sha256: d5e89e01ed831488eac010f5c32cab86ed44c2489ffe79b0aba61bd46bc41b2a
effective_date: '2022-11-01'
source_version: 4.0, last updated 07-01-2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DBS-014: Database Support in Cloud Services'', links this file as https://drive.google.com/file/d/1hgnj6YC3CyjrbXKvoOn5_EwJTJ_WH2oZ/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1hgnj6YC3CyjrbXKvoOn5_EwJTJ_WH2oZ
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Database Support in Cloud Services (TS-DBS-014)

## At a glance

OIT technical standard TS-DBS-014 (Data and Databases): Database Support in Cloud Services. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DBS-014: Database Support in Cloud Services
  Document ID                     TS-DBS-014
  Title                           Database Support in Cloud Services
  Executive Sponsor               Database Services Management, DBS Manager
  Issuing Authority               Governor's Office of Information Technology (OIT)
  Applies to                      OIT and OIT supported agencies; employees of OIT, agencies
                                  supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Instrument Type                 Standard
  Version                         4.0
  Effective Date                  11-01-2022
  Last Updated                    07-01-2026

Purpose
OIT is statutorily mandated to provide IT support and services to the State and its stakeholders in the
most effective and efficient manner possible (as defined by C.R.S. 24-37.5). To satisfy the
stakeholder needs surrounding OIT supported databases and their versions, the following is submitted
as the standard for specifications, methodologies and practices to provide the service.
The purpose of this document is to communicate the standards that the Governor's Office of
Information Technology (OIT) has developed with the intent of providing enterprise standard
configurations for Database Support in Cloud Services. Standards are based on a best-of-value
decision assessment involving multifarious factors, such as stakeholder needs, hardware
configurations that are serviced and supported by OIT, as well as operational and security best
practices guidelines.
The ultimate purpose of the Database Support in Cloud Services is to describe the minimum
requirements for designing, installing, securing, monitoring, maintaining, protecting, and
decommissioning any OIT supported Database environment.

Scope
These standards apply to OIT and OIT supported agencies. This Standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to
enforce technology standardization and assist in making the usage, support, and/or purchase of
technologies more consistent and efficient.
Additionally, the standards assigned and prescribed by this document, instituted for use by the
approval of the OIT Architecture Review Board (ARB), should be used to govern purchase and
deployment decisions deemed as “go-forward” or “net-new” strategies or implementations, and are

                                                                                           Page 1 of 5

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
For the purpose of enforcement, this standard is rated CAT 1 according to the Enforcement Category
Chart.

Roles and Responsibilities
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
Database Services Management
   ●    Responsible for enforcement and approval of changes of policies, standards, guidelines,
        procedures.

Database Services Database Administrator (DBA)
   ●    Responsible for knowing and adhering to policies, standards, guidelines, procedures as part of
        job description.
All OIT staff are responsible to be aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

Standards
Goals
   ●    Ensure Database Services is able to provide support, patching, upgrades and installations
        specific to database platforms, versions, and environments in the Cloud environment.
                                                                                            Page 2 of 5

Process
  ●   Cloud database operations, support and maintenance including any database categorized as
      Database as a Service (DBaaS) must meet the following criteria:
          ○   Any database request for installation, upgrade or maintenance must be initiated by
              Database Services.
          ○   The Database Services team will manage, support, secure, and optimize database
              operations in the cloud environment.
          ○   Any vendor supported cloud database must comply with the OIT Database Services
              standards.
  ●   Installing and upgrading database platforms and tools includes but is not limited to
      infrastructure as code to build any database instance using terraform, ansible or any other
      automation tool, subject to the following rules:
          ○   If a DevOps pipeline is in use to build out the database infrastructure, at least two
              members from the database services team must approve the change before any
              deployments can proceed.
          ○   If the installation is done through the console or CLI via infrastructure as code i.e.
              Terraform, the database services team must approve Azure DevOps Pull Requests or
              console work before being implemented.
  ●   Initial system storage and capacity planning requirements must follow this rule:
          ○   Allocating initial system storage, capacity planning and future storage requirements
              for the database system as per the sizing requirements of the agency must be
              approved by Database Services.
  ●   Database Patching guidelines are defined below:
          ○   The scheduling, testing and applying of database patches will be performed by
              database services.
  ●   Database users and security maintenance regulations are outlined below:
          ○   Database users and security maintenance will be done by the database services team
              including the creation and maintenance of any RDS cloud administrator accounts. The
              master account and password can not be given to any individual outside of the
              Database Services Team.
          ○   Controlling, monitoring, auditing user access, and enforcing password requirements to
              the database will be done by using least privilege as per the requirements listed in TS-
              DBS-006: Database Security. Password rotation should be used when possible as
              defined in the CISP.
  ●   Supported Database Versions must conform to enterprise standards:
          ○   Any cloud database supported by Database Services must be in the approved supported
              database versions listed in TS-DBS-001 Supported Databases and Versions.
  ●   Database Related Services are managed as follows:
          ○   Any database related services in the Cloud such as DMS etc. will be initiated and
              managed by Database Services and initial provisioning will be done through Terraform.
          ○   The creation and support of database maintenance jobs will be managed by Database
              Services.
  ●   Database Backup and Recovery operational standards include:
          ○   Backing up, restoring and maintaining database backups is the responsibility of the
              Database Services team.

                                                                                            Page 3 of 5

          ○   If using an RDS or a managed instance, all databases in the instances will be restored
              regardless of the number of databases.
   ●   Cloud Database Inventory tracking operations require:
          ○   Database services will update and maintain inventories for all OIT managed databases
              in the cloud infrastructure.
   ●   Database User Administration guidelines are governed by separate authority:
          ○   Database user creation and maintenance is defined in the database standard TS-DBS-
              008: Database User Administration.
   ●   Additional Support and Services provisions consist of:
          ○   Monitoring and optimizing database performance by using and maintaining any cloud
              provided tools such as performance insight and cloud watch.
          ○   Maintaining archived data.
          ○   Ensuring compliance with database vendor license agreements.
          ○   Contacting database vendors for technical support (if required). This would include
              support accounts with any Cloud provider.
          ○   Incident triage.

Requirements
   ●   Cloud technology infrastructure choices must align with organizational requirements:
          ○   Database Services will be involved in Cloud selection and database platform
              preferences.

Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of and approved by the “Owner of Standard” listed in
Section 3 (Roles and Responsibilities) of this document.
Requests may be acquired by completing the “EXCEPTION REQUEST to Technical Standard” form and
including the completed form (including all signatures) along with other documentation required as
part of standard procedures when executing a technology procurement or service deployment.

References
OIT documents and policies
   ●   State of Colorado Style Library
   ●   TS-OEA-001: Technology Accessibility for Persons with Disabilities
   ●   Enforcement Category Chart
   ●   Colorado Information Security Policies (CISPs)

State documents and policies
   ●   Colorado Brand Guidelines
   ●   C.R.S. 24-37.5-101, et seq.
   ●   OIT DBS Database Software Management Policy

Third party resources
   ●   My Oracle Support
                                                                                            Page 4 of 5

   ●   Microsoft Support
   ●   AWS Support (access through the AWS account)

Definitions
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
EA: Enterprise Application development group responsible for application development.
CLI: Command line interface
Database Instance: Any isolated database provided in cloud services that are available by AWS,
Microsoft Azure, and the Google platform.
OEA (Office of Enterprise Architecture): The Office of Enterprise Architecture was formed as an
office under OIT by Governor's Rule 8 CCR 1501-7.
OIT (Office of Information Technology): The Governor's Office of Information Technology was
created and governed by C.R.S. 24-37.5, et seq.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification for granting the exception. Typically an exception request is
subject to review and approval by an authority in the area.

                                                                                            Page 5 of 5

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DBS-014: Database Support in Cloud Services', links this file as https://drive.google.com/file/d/1hgnj6YC3CyjrbXKvoOn5_EwJTJ_WH2oZ/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1hgnj6YC3CyjrbXKvoOn5_EwJTJ_WH2oZ (the source URL above).
