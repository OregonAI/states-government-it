---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-003
title: Identity and Access Administration
doc_type: standard
citation: TS-INF-003
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1fci7-NXIXTxsADIFTdm6urC7T1ligDRa
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 106726242f0cbe34a427e9c1c8b663d0d49fe31780e93e40ca321ec32bc9726f
effective_date: '2026-02-02'
source_version: 14.0, last updated 09/08/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-003: Identity and Access Administration'', links this file as https://drive.google.com/file/d/1fci7-NXIXTxsADIFTdm6urC7T1ligDRa/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1fci7-NXIXTxsADIFTdm6urC7T1ligDRa
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Identity and Access Administration (TS-INF-003)

## At a glance

OIT technical standard TS-INF-003 (Infrastructure): Identity and Access Administration. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-003: Identity and Access Administration
  Document ID                     TS-INF-003
  Title                           Identity and Access Administration
  Executive Sponsor               Access Control, Manager of Identity and Access Management
  Issuing Authority               Office of Information Technology (OIT)
  Applies to                      OIT and OIT-supported agencies; employees of OIT, agencies
                                  supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Tier                            Standard
  Version                         14.0
  Effective Date                  02/02/2026
  Last Updated                    09/08/2026

1. Purpose
OIT is statutorily obligated to provide IT support and services to the State and its stakeholders in the
most effective and efficient manner possible. To satisfy stakeholder needs surrounding automated
provisioning of employee access, maximizing organizational security, and eliminating excessive
processes and inefficiencies, this document is submitted as the standard in support of an Enterprise
Identity and Access Management System, as also defined in the FY16 Playbook.
This document communicates the standards OIT has developed with the intent of providing an
enterprise standard for onboarding, offboarding, managing access changes, audit and reporting, and
allowing self-managed password resets ("user self-service"), based on a best-of-value decision
assessment involving stakeholder needs and operational and security best practices.
The ultimate purpose of this standard is to decrease the timeframe it takes for employees to obtain
access to necessary applications, platforms, systems, and data throughout their employment
lifecycle, while achieving and maintaining compliance related to user access security and eliminating
common identity access management inefficiencies and redundant processes.

2. Scope
This standard applies to OIT and OIT-supported agencies. It shall be used by employees of OIT,
agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to enforce
technology standardization and assist in making the usage, support, and/or purchase of technologies
more consistent and efficient.

                                                                                             Page 1 of 3

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Access Control - Manager, Identity and Access Management
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Presents to the Architecture Review Board for approval and adoption.
Access Control - Intelligence, Compliance & Governance (ICG)
   ●   Responsible for the renewal of this document on a bi-annual basis.
Access Control - Identity and Access Management Administration
   ●   Responsible for ensuring all user accounts are disabled as soon as the notification is received
       and requested.
   ●   Ensures employee (including contractor, vendor, and intern) user accounts are offboarded
       within 7 calendar days after the request is submitted.
Access Control - Identity and Access Management Application
   ●   Responsible for automatically disabling accounts after 90 days of inactivity.
CISO / Security Architecture
   ●   Contributes to the content of the standard to ensure security alignment.
   ●   Ensures the standard supports the Secure Colorado Strategy and State Cyber Security Policies.
   ●   Ensures security is not sacrificed for standard functionality.
Agency
   ●   Responsible for ensuring all user accounts are disabled as soon as the actual employee leaves
       or termination occurs (including contractors, vendors, and interns).
   ●   Scheduling offboarding within 2 hours after departure.
   ●   Conducting reviews of user account permissions twice a year (June and December).
   ●   Monitoring user accounts at least every 90 days until the automated inactivity process is
       implemented for their agency.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
For the purposes stated and supported in this document, a standard for the practice of Identity and
Access Administration (Identity Governance and Administration – IGA) shall be predicated on the
following technology: Identity and Access Administration: One Identity Manager.

                                                                                            Page 2 of 3

Additionally, the following specifications and capabilities shall be governed and mandated as per this
standard for use within the stated scope:

1. Access Administration
   ●   Approval and authorization: Each request must contain manager approval and system/data
       owner authorization.
   ●   Tracking: Each request must be tracked in the Service Desk and IGA system.
   ●   Audit: Each entitlement must have audit tracking.
   ●   Reporting: User and privileged accounts reported for attestation and recertification.
   ●   Role-Based Access: Least-privilege model.
2. Identity Administration
   ●   Identity synchronization across required systems.
3. Password Management
   ●   Self-managed password resets.
   ●   Service Desk integration with ITSM.
   ●   Secure data access controls beyond native platform.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards within this document
must be requested of, and approved by, the Owner of Standard listed under Roles and
Responsibilities.
Requests to use technology standards other than those described herein shall be submitted in writing
to the Manager, Identity and Access Management, for consideration.

6. References
   ●   AC - Access Control Cyber Pol 102
   ●   AU - Audit & Accountability Cyber Pol 104
   ●   IA - Identification & Authentication Cyber Pol 108
   ●   ITIL Glossary

7. Definitions
Agency: Refers to Public Agencies as defined in C.R.S. § 24-37.5-102(28).
Authentication Credential: A mechanism used to prove identity, such as a password, certificate, or
PIV card.
CIA: Confidentiality, Integrity, and Availability.
Disabling: Temporarily disables a user's accounts in all integrated systems immediately; this action
revokes all network access.
Identity Governance and Administration (IGA): Processes to manage identity and access information
across systems, including lifecycle, provisioning, certification, and governance controls.
Offboarding: Completely removes an individual's access to any agency accounts they have and
schedules the account for permanent removal on the offboarding date at close of business.

                                                                                           Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-003: Identity and Access Administration', links this file as https://drive.google.com/file/d/1fci7-NXIXTxsADIFTdm6urC7T1ligDRa/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1fci7-NXIXTxsADIFTdm6urC7T1ligDRa (the source URL above).
