---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-002
title: End User Enterprise Software
doc_type: standard
citation: TS-INF-002
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=14RJ3WNgjAkNgsZ804AUdkKWnrCMP9YyS
source_format: pdf
retrieved: '2026-11-11'
source_sha256: db2dc751a3a47cb660836969fb7a611f53f7154b90a7f3cb4770b3209b265b75
effective_date: '2015-05-28'
source_version: 4.0, last updated 07/17/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-002: End User Enterprise Software'', links this file as https://drive.google.com/file/d/14RJ3WNgjAkNgsZ804AUdkKWnrCMP9YyS/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=14RJ3WNgjAkNgsZ804AUdkKWnrCMP9YyS
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# End User Enterprise Software (TS-INF-002)

## At a glance

OIT technical standard TS-INF-002 (Infrastructure): End User Enterprise Software. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-002: End User Enterprise Software
  Document ID                      TS-INF-002
  Title                            End User Enterprise Software
  Executive Sponsor                Deskside Support Services, Enterprise Deskside Support Services
                                   Manager
  Issuing Authority                Office of Information Technology (OIT)
  Applies to                       Any software configurations for end-user PC/client x86 and x64-
                                   based hardware purchased and supported by OIT and OIT-
                                   supported agencies (per C.R.S. Title 24, Article 37.5).
  Tier                             Standard
  Version                          4.0
  Effective Date                   05/28/2015
  Last Updated                     07/17/2026

1. Purpose
The purpose of this document is to communicate the standards that the Governor's Office of
Information Technology (OIT) has developed with the intent of providing enterprise standard
software configurations for end-user PC/client x86-based hardware. Standards are based on a best-
of-value decision assessment involving multivariate factors, such as state employee needs, hardware
configurations that are serviced and supported by OIT, as well as operational and security best
practices guidelines.

2. Scope
These standards apply to any software configurations for end-user PC/client x86 and x64-based
hardware purchased and supported by OIT and OIT-supported agencies (per state statute Article 37.5
Title 24). This standard shall be used by employees of OIT, agencies supported by OIT, and vendors
contracted by OIT or its stakeholders, as a means to enforce technology standardization and assist in
making the usage, support, and/or purchase of technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●      Chairs and conducts business of the Architecture Review Board (ARB).

                                                                                           Page 1 of 3

   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Deskside Support Services - Enterprise Deskside Support Services Manager
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Updates document standards and version number.
   ●   Presents to the Architecture Review Board for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
These standards define the minimum version in use for all enterprise software deployed to end-user
workstations as defined in TS-INF-001, to provide consistently productive deployments, security
practices, and support across the agencies.
Operating System (OS)
   ●   Microsoft Windows 10 Enterprise (exception only)
   ●   Microsoft Windows 11 Enterprise
Productivity Suite
   ●   Microsoft Office 2016 or later versions supported by Microsoft (end of life for Office 2016 and
       Office 2019 is August 2025).
   ●   Microsoft Apps 365 (as-needed basis). MS OneDrive, OneNote, Yammer, and Teams are
       excluded in lieu of standard Google offerings.
   ●   Google Workspaces (formerly Google Apps for Government), latest version — includes email,
       calendar, docs, sheets, forms, presentations, sites, drawings, Google Drive, Google Keep,
       Google Meet, and Google Chat.
Browser
   ●   Chrome, latest major version
   ●   Microsoft Edge, latest major version
Endpoint Security
   ●   CrowdStrike, latest version (anti-malware, threat intelligence, local firewall security)
   ●   Tenable, latest version (compliance, vulnerability scanning, and security hardening)
   ●   Microsoft BitLocker (drive encryption)
   ●   Microsoft LAPS
PDF Reader
   ●   Adobe Reader, latest major version
Other Utility Software
   ●   Java Runtime Environment, latest version
                                                                                            Page 2 of 3

   ●   Cisco AnyConnect (exception only), Secure Access (formerly NetMotion), and Global Protect
       (NGVPN) VPN
   ●   Webex

5. Variance and Exception Process
   ●   Legacy operating systems: New computers being rolled out should not have older OS versions
       than listed in Section 4. Old Windows versions can only remain on systems identified and
       approved using the Security Exception Request Form.
   ●   Apple macOS: Recognized as a supported but non-standard product; exists as an exception
       requiring manager sign-off.
   ●   Chrome OS: Recognized as a supported but non-standard exception requiring manager sign-
       off; any Chrome OS devices must have an enterprise license for Google Management.
   ●   Any variances to the standards in Section 4 must be requested using the Security Exception
       Request Form.
   ●   Freeware and/or open-source software may only be installed on systems identified and
       approved using the Security Exception Request Form.

6. References
   ●   Office of Information Security Policies
   ●   Security Exception Request Form
   ●   OIT Technical Standard End User Computer Equipment, TS-INF-001

7. Definitions
Enterprise Software: The default software programs loaded onto all PC/Client computers regardless
of agency.
Operating System (OS): The most defining characteristic of a PC/Client user environment, providing
the visual interface for an end user to do their work.
PC/Client: Any workstation device that can be described as a Desktop, Laptop, or Tablet.
x86 / x32 / x64: Microprocessor family based on Complex Instruction Set Computing (CISC)
architecture, commonly sourced from Intel and AMD by OEM suppliers.
Freeware: Applications offered at no cost in lieu of licensed software. Because it may be
copyrighted, reuse in programming may not be permitted.
Open Source: Software released under a license granting users rights to use, study, change, and
distribute the software and its source code, for any purpose.

                                                                                            Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-002: End User Enterprise Software', links this file as https://drive.google.com/file/d/14RJ3WNgjAkNgsZ804AUdkKWnrCMP9YyS/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=14RJ3WNgjAkNgsZ804AUdkKWnrCMP9YyS (the source URL above).
