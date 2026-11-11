---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-ciso-007
title: Server Hardening
doc_type: standard
citation: TS-CISO-007
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1WCUaREXTATjTdKIUll9vwRi25z3Tej-2
source_format: pdf
retrieved: '2026-11-11'
source_sha256: d8dfa3ac43796ac9276a7173eecfef2ec3dbbe94aeb75d330a14d0e505a1b1c2
effective_date: '2026-04-28'
source_version: 1.0, last updated 05/05/2026
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads 'TS-CISO-007 Server Hardening', links this file as https://drive.google.com/file/d/1WCUaREXTATjTdKIUll9vwRi25z3Tej-2/view?usp=sharing;
  the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1WCUaREXTATjTdKIUll9vwRi25z3Tej-2
  (the source URL above).
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

# Server Hardening (TS-CISO-007)

## At a glance

OIT technical standard TS-CISO-007 (Information Security): Server Hardening. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-CISO-007: Server Hardening
  Document ID                       TS-CISO-007
  Title                             Server Hardening
  Executive Sponsor                 Jill Fraser, Chief Information Security Officer
  Issuing Authority                 Governor’s Office of Information Technology (OIT)
  Applies to                        All servers deployed or managed by the Governor's Office of
                                    Information Technology (OIT) for all supported agencies,
                                    including new servers, existing servers previously deployed at an
                                    agency, domain and non-domain servers, and virtual and physical
                                    servers.
  Instrument Type                   Standard
  Version                           1.0
  Effective Date                    04/28/2026
  Last Updated                      05/05/2026

Purpose
This standard is issued under the authority of the Governor's Office of Information Technology
(OIT) (C.R.S. 24-37.5, et seq.) and the Office of Enterprise Architecture (Rule 8 CCR 1501-7).
It defines requirements for securely configuring and hardening State server infrastructure to
improve its defense and sustainability.

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
This standard applies to all servers deployed or managed by OIT for all supported agencies,
including:
   ●      New servers
   ●      Existing servers that were previously deployed at an agency
   ●      Domain and non-domain servers
   ●      Virtual and physical servers

                                                                                      Page 1 of 3

Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.

Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine standards.
   ●   Reviews/approves the Standard (this document).

Server Support
   ●   Implements server hardening procedures on all in-scope servers and maintains records
       thereof.
   ●   Supports and documents this Standard and the server hardening process.

Vendors and Additional Staffing
   ●   Comply with this Standard through all phases of work involving in-scope servers.
   ●   Provide compliance reporting on request from OIT.

Standards
Server Hardening
   ●   Refer to and implement current Center for Internet Security (CIS) benchmarks for all
       in-scope servers.
Server hardening will be achieved by:
   ●   Using the Server Hardened VM Template.
   ●   Applying local security policies and default domain GPOs.
   ●   Applying a Linux Server Hardened template and/or the applicable Red Hat security
       baseline.
   ●   Allowing for current application-specific approved exceptions.
   ●   Allowing for current enterprise exceptions.

Communication and Documentation
Server hardening process documentation will be stored in the ServiceHub knowledge base.

Change Management
Changes to servers must be made in accordance with the OIT Change Management policy.

Policy Exception Requests
Requests for variances from any provisions within this Standard must be submitted via a Policy
Exception Request.

                                                                                   Page 2 of 3

Server Benchmark Review
The Server Support team will, on a quarterly basis:
   ●   Review latest server benchmarks and implement any needed changes to the domain
       GPOs, local security policies, and VM templates.
   ●   Review Enterprise exceptions and determine if any can be remediated or need to be
       re-submitted to the Office of Security Administration for another one-year exception.
   ●   Address the OS patches that need to be applied to virtual templates.

Exceptions and Variance
All exceptions must be documented, justified, and approved by the State of Colorado's Chief
Information Security Officer (CISO) or other designated authority. Compensating controls must
be documented, implemented, and maintained.

Compliance
The State of Colorado's Chief Information Security Officer (CISO) or other designated authority
will monitor and advise on compliance with this standard.

References
   ●   Center for Internet Security
   ●   Common Vulnerability Scoring System (CVSS)
   ●   IRS Safeguards Program, CJIS Security Policy, SSA Secure Info Systems, HIPAA/HiTECH,
       and other applicable regulations
   ●   CFR § 229.106 (Item 106) Cybersecurity

Definitions
   ●   Change: The addition, modification, or removal of anything that could have an effect
       on IT services.
   ●   Change management: The structured practice of controlling and communicating
       modifications within the IT environment.
   ●   CIS: Center for Internet Security.
   ●   Group Policy Object (GPO): A virtual collection of policy settings.
   ●   HIPAA/HiTECH: Health Information Portability and Accountability Act; Health
       Information Technology for Economic and Clinical Health.

                                                                                   Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-CISO-007 Server Hardening', links this file as https://drive.google.com/file/d/1WCUaREXTATjTdKIUll9vwRi25z3Tej-2/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1WCUaREXTATjTdKIUll9vwRi25z3Tej-2 (the source URL above).
