---
schema_version: 1
corpus: states-government-it
jurisdiction: hawaii
id: hi-std-ets-508-01
title: Secure Device Standards
doc_type: standard
citation: ETS Doc No. 508.01
authority_level: ''
issuing_body: Office of Enterprise Technology Services, Department of Accounting and General Services
source_url: https://ets.hawaii.gov/ets-doc-no-508-01-secure-device-standards/
source_format: html
retrieved: '2026-11-11'
source_sha256: 40b77f2ce2f841e233ad3308effa89fa2bd85042c7051e5e83d89c56c02053d3
effective_date: '2017-12-01'
source_version: ''
status: current
content_mode: verbatim
conversion_notes: 'Text taken from the library page the Office of Enterprise Technology Services lists
  for this document: the page title, the header block and each table row (cells separated by '' | '').
  The page''s menus, footer and the link to a PDF copy are removed.'
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

# Secure Device Standards (ETS Doc No. 508.01)

## At a glance

The minimum device standards table (operating system support, updates, device management, passwords, biometrics, multi-factor authentication, firewall, screen lock, encryption, endpoint protection, jailbroken devices). Effective December 1, 2017, revision September 18, 2018. Text taken from the library row's own page. The PDF that page offers ('Download this Standard as a PDF', https://ets.hawaii.gov/wp-content/uploads/2018/10/ETS-Policy-No.-508.01-Secure-Device-Standards-20180918.pdf) was fetched and DIFFERS: its Device passwords row says 'Desktop/Laptop: 10 characters' where the page says '14 characters'; OWNER DECISION which copy is of record (see left_out).

## Full text

ETS DOC NO. 508.01: SECURE DEVICE STANDARDS
STATE OF HAWAII
Office of Enterprise Technology Services Policy No. 508.01
Secure Device Standards
Effective Date: December 1, 2017
Revision No./Date: September 18, 2018
Category | Minimum Standard | Comments
Operating Systems | Operating systems must have mainstream support by the vendor | This is typically the current or immediately prior generation, i.e., “N-1” (e.g., Windows 8 and 10)
Operating system and application updates | Enabled | When manual updates are required, reasonable effort should be made to stay current
Device management platform compatibility | Microsoft Intune (if supported) | Mobile device management software with enabled remote location and erase services
Device passwords | Desktop/Laptop: 14 characters; Mobile device: 6 characters; All passwords must be unique |
Device biometric security | Acceptable (provided the overriding device password meets standard above) | Examples of biometrics include thumbprint and facial recognition
Multi-factor authentication (MFA) | Enabled for remote access | Also known as 2-factor authentication and login verification
Host-based firewall | Enabled on the endpoint (if supported) | Also known as a personal firewall
Screen lock | Manual and auto screen lock functionality enabled (users must manually lock device screen when intentionally leaving the device unattended, in addition to enabling auto screen lock timer); Desktop/Laptop: Auto lock after 15 minutes; Mobile device: Auto lock after 5 minutes | Device shall require reentry of password or biometrics after specified time
Full-Device/Disk encryption | AES 128-bit or higher (if supported) | Effective immediately for existing devices, if supported, and all NEW devices, without exception; Effective July 1, 2018, for all devices
Device endpoint protection | Anti-Malware/Virus enabled and updating regularly (excluding Apple iOS) |
“Jailbroken” or “rooted” devices | Prohibited | Jailbreaking or rooting refers to mechanisms that involve overriding manufacturer controls and permissions

## Curator notes

Text taken from the library page the Office of Enterprise Technology Services lists for this document: the page title, the header block and each table row (cells separated by ' | '). The page's menus, footer and the link to a PDF copy are removed.
