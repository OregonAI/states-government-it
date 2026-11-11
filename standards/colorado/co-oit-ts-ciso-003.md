---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-ciso-003
title: Remote Access Standard v2026
doc_type: standard
citation: TS-CISO-003
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1Zs7LcaUgYk4yw8UJl3IPgxRe143sn6n4
source_format: pdf
retrieved: '2026-11-11'
source_sha256: f73e58043f6a80306a27cac39b7b14dc33a17722b61857a98cbfe82a8d7ced8f
effective_date: '2026-01-31'
source_version: 4.0, last updated 05/14/2026
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads 'TS-CISO-003 Remote Access Standard v2026', links this file as https://drive.google.com/file/d/1Zs7LcaUgYk4yw8UJl3IPgxRe143sn6n4/view?usp=sharing;
  the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1Zs7LcaUgYk4yw8UJl3IPgxRe143sn6n4
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

# Remote Access Standard v2026 (TS-CISO-003)

## At a glance

OIT technical standard TS-CISO-003 (Information Security): Remote Access Standard v2026. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-CISO-003: Remote Access Standard
  Document ID                    TS-CISO-003
  Title                          Remote Access Standard v2026
  Executive Sponsor              Jill Fraser, Chief Information Security Officer
  Issuing Authority              Governor’s Office of Information Technology (OIT)
  Applies to                     All state government agencies, employees, contractors, vendors,
                                 and external users who access state government information
                                 systems and applications, regardless of location or device,
                                 including all applications, hosting environments, and physical and
                                 connected technologies.
  Instrument Type                Standard
  Version                        4.0
  Effective Date                 01/31/2026
  Last Updated                   05/14/2026

Purpose
This standard defines security requirements for remote access to State information systems
and applications, including on-premises and cloud environments. It supports compliance with
the Colorado Information Security Policies (CISPs).

Scope
This standard applies to all state government agencies, employees, contractors, vendors, and
external users who access state government information systems and applications, regardless
of location or device. This includes all applications and hosting environments, and access to
physical and connected technologies.

Requirements
The appropriate Remote Access standard requirements are listed below. Additional
requirements must be implemented based on the regulated data type(s).

Remote Access Methods
The following methods, with the stated restrictions, are allowed:
 Device Type             Access Method/Protocol    Requirement
 State-Managed Devices   State-managed VPN         Must adhere to all applicable state security
                         (client-to-site)          standards and configurations. Any endpoints
                                                   that connect to internal resources must use

                                                                                     Page 1 of 2

 Device Type              Access Method/Protocol       Requirement
                                                       the approved state client-to-site (individual)
                                                       VPN.
 External/Edge Networks   State-approved site-to-      Must use the state-approved site-to-site VPN
                          site VPN                     to connect to any internal state resources.
 Non-State-Managed        State-managed Virtual        Must connect to a virtual desktop solution
 Devices                  Desktop Solution             managed by the state.

Security Requirements
 Requirement               Detail
 Strong Authentication     All external remote access connections shall require multi-factor
                           authentication (MFA) (e.g., username/password + hardware token,
                           biometric authentication).
 Session Management        Enforcing strong session IDs, timeouts, and locks.
 Least Privilege           Remote access users shall only be granted the minimum necessary
                           privileges to perform their job duties.
 Data Encryption           All data transmitted over the remote access connection shall be
                           encrypted using strong encryption protocols.

Data Handling
Remote access users shall adhere to all applicable data security policies and standards,
including data classification, handling, and storage requirements.

Exceptions
All exceptions must be documented, justified, and approved by the State of Colorado's Chief
Information Security Officer (CISO) or other designated authority. Compensating controls must
be documented, implemented, and maintained.

Compliance
The Information Security Office will monitor and advise on compliance with this standard.

                                                                                           Page 2 of 2

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-CISO-003 Remote Access Standard v2026', links this file as https://drive.google.com/file/d/1Zs7LcaUgYk4yw8UJl3IPgxRe143sn6n4/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1Zs7LcaUgYk4yw8UJl3IPgxRe143sn6n4 (the source URL above).
