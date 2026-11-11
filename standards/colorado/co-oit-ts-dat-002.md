---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-dat-002
title: Secure File Transfer
doc_type: standard
citation: TS-DAT-002
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1ni1lYNPNWeTgdX2dsEJb0xqQCdw0h6gu
source_format: pdf
retrieved: '2026-11-11'
source_sha256: ac61ea0b49c16b8244cb02c1b300c332ffa201ac383df2cf3dee8b714a332776
effective_date: '2015-08-20'
source_version: 4.0, last updated 04/15/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DAT-002: Secure File Transfer'', links this file as https://drive.google.com/file/d/1ni1lYNPNWeTgdX2dsEJb0xqQCdw0h6gu/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1ni1lYNPNWeTgdX2dsEJb0xqQCdw0h6gu
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

# Secure File Transfer (TS-DAT-002)

## At a glance

OIT technical standard TS-DAT-002 (Data and Databases): Secure File Transfer. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DAT-002: Secure File Transfer
  Document ID                    TS-DAT-002
  Title                          Secure File Transfer
  Executive Sponsor              Chief Data Officer (CDO)
  Issuing Authority              Governor’s Office of Information Technology (OIT)
  Applies to                     OIT and OIT-supported agencies, including employees of OIT,
                                 agencies supported by OIT, and vendors contracted by OIT or its
                                 stakeholders.
  Instrument Type                Standard
  Version                        4.0
  Effective Date                 08/20/2015
  Last Updated                   04/15/2026

1. Purpose
OIT is statutorily mandated to provide IT support and services to the State and its
stakeholders in the most effective and efficient manner possible (as defined in C.R.S. 24-
37.5). To satisfy stakeholder needs surrounding Data and Integrations Services, this document
is submitted as the standard for Secure File Transfer and Point-to-Point Integrations.
This document communicates the standards OIT has developed with the intent of providing
enterprise standard configurations for Secure File Transfer, based on a best-of-value decision
assessment involving factors such as stakeholder needs, hardware configurations serviced and
supported by OIT, and operational and security best practices.
The ultimate purpose of this standard is to describe the minimum requirements for designing,
installing, securing, monitoring, maintaining, protecting, and decommissioning Secure File
Transfer and Point-to-Point Integrations.

2. Scope
These standards apply to OIT and OIT-supported agencies. This standard shall be used by
employees of OIT, agencies supported by OIT, and vendors contracted by OIT or its
stakeholders, as a means to enforce technology standardization and assist in making the
usage, support, and/or purchase of technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern
purchase and deployment decisions deemed “go-forward” or “net-new”, and are not intended
as a retroactively enforceable mandate for immediate conformance, especially where cost
implications may be prohibitive.

                                                                                   Page 1 of 3

Standards are predicated on the assumption that there can be no point of enforcement unless
and until there is an effort to re-procure, renew (contracts), reconfigure (including
upgrades), or redevelop the system. For guidance or enforcement in conformance to
standards, an email request may be sent to OIT_OEA@state.co.us with the subject line
“Request for Architecture Review: <projectName/systemName>”.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.

Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews/approves the Standard (this document).

Chief Data Officer (CDO)
    ● Owner of Standard.
    ● Engages stakeholders and subject matter experts to determine the standard.
    ● Updates document standards and version number.
    ● Presents to the Architecture Review Board for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and
its purposes of authority and governance in support of OIT's statutorily mandated mission in
service of Colorado State Government affairs.

4. Standards
The following solutions represent the current technologies supported by the CDO for
implementing Secure File Transfer service standards.

File Transfer Systems
   ●   Automic Automation: A single point of automation across mainframe, distributed, and
       cloud platforms.
   ●   MOVEit: Provides secure collaboration and automated file transfers of sensitive data
       with advanced workflow automation capabilities without the need for scripting
       (MOVEit Automation and MOVEit Transfer).
   ●   TIBCO Managed File Transfer (MFT): Used for secure file transfers between the State
       of Colorado and the Social Security Administration (SSA).
   ●   Informatica Data Integration: Used for ETL data movement from transactional to
       analytical systems.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions
stated within this document must be requested of, and approved by, the “Owner of Standard”
listed under Roles and Responsibilities.

                                                                                      Page 2 of 3

Requests may be submitted through ServiceHub by following the applicable How-to Guide and
including the completed form (with all signatures) along with other documentation required
as part of standard procedures when executing a technology procurement or service
deployment.

6. References
   ●   OIT documents and policies - all staff shall comply with all other OIT policies as
       published (see OIT Plaza - Policies); in the event of any perceived conflict, OIT Policies
       shall preside.
   ●   State documents and policies - Colorado Information Security Policies (CISPs)
   ●   Third-party resources - IRS Publication 1075 (requirements for secure file transfer)

7. Definitions
   ●   Managed File Transfer (MFT): Refers to the automated movement of digital content
       between two information systems, supported by an intermediate MFT service. At a
       minimum, any MFT system shall: enable encrypted transport of content across the
       network using a minimum strength of AES-128; establish security access between the
       two systems; support scheduled transfers; log the activity and results of all transfers,
       including detailed logging of exceptions; and provide notifications about selected
       results to identified users. Any MFT shall not store content for more than thirty days
       absent an approved exception. When content must move to an external system
       without a secure connection, the MFT shall transfer the content to a secure repository
       for independent retrieval.
   ●   sFTP (Secure File Transfer): A network protocol providing file access, transfer, and
       management over any reliable data stream, conforming to IETF definitions, usable as
       an extension of SSH version 2.0, secure file transfer over TLS (v1.2 or greater), and
       transfer of management information in VPN applications.
   ●   Standard: A rule that specifies a particular course of action or response to a given
       situation. Standards are mandatory directives to carry out management's policies and
       are used to measure compliance with policies.
   ●   OEA (Office of Enterprise Architecture): Formed as an office under OIT by Governor's
       Rule 8 CCR 1501-7.
   ●   OIT (Office of Information Technology): Created and governed by C.R.S. 24-37.5, et
       seq.
   ●   Exception request: A document requesting an exception to a recognized standard,
       requiring a business or technical justification for granting the exception, subject to
       review and approval by an authority in the area.

                                                                                     Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DAT-002: Secure File Transfer', links this file as https://drive.google.com/file/d/1ni1lYNPNWeTgdX2dsEJb0xqQCdw0h6gu/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1ni1lYNPNWeTgdX2dsEJb0xqQCdw0h6gu (the source URL above).
