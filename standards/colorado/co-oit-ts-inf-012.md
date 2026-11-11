---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-012
title: Multifunction Device/Printer Configuration Standard
doc_type: standard
citation: TS-INF-012
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1N6IDIt62AR5tNpaUzvKgfVOnMTifypmM
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 5a6093ebc2b16f2b07fb6619aed6c538f015ab3d8ba92adba9292bf865fc16bd
effective_date: '2025-01-29'
source_version: 3.0, last updated 10/16/2025
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-012: Multifunction Device/Printer Configuration'', links this file as https://drive.google.com/file/d/1N6IDIt62AR5tNpaUzvKgfVOnMTifypmM/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1N6IDIt62AR5tNpaUzvKgfVOnMTifypmM
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

# Multifunction Device/Printer Configuration Standard (TS-INF-012)

## At a glance

OIT technical standard TS-INF-012 (Infrastructure): Multifunction Device/Printer Configuration Standard. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-012: Multifunction Device/Printer
Configuration Standard
  Document ID                    TS-INF-012
  Title                          Multifunction Device/Printer Configuration Standard
  Executive Sponsor              Deskside Services Management Team (DSS)
  Issuing Authority              Office of Information Technology (OIT)
  Applies to                     OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and
                                 vendors contracted by OIT or its stakeholders.
  Tier                           Standard
  Version                        3.0
  Effective Date                 01/29/2025
  Last Updated                   10/16/2025

1. Purpose
This standard is issued under the authority of the Governor's Office of Information Technology (OIT)
(C.R.S. 24-37.5, et seq.) and the Office of Enterprise Architecture (Rule 8 CCR 1501-7). It
communicates the standards OIT has developed to provide enterprise standard configurations for
multifunction printer (MFP) devices, based on a best-of-value decision assessment involving
stakeholder needs, hardware configurations serviced and supported by OIT, and operational and
security best practices.
The ultimate purpose of this standard is to describe the minimum requirements for designing,
installing, securing, monitoring, maintaining, protecting, and decommissioning multifunction printer
devices.

2. Scope
These standards apply to OIT, state agencies as defined in C.R.S. 24-37.5-101(28), and vendors
contracted by OIT or its stakeholders, as a means to enforce technology standardization and assist in
making the usage, support, and/or purchase of technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

                                                                                           Page 1 of 3

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Deskside Services Management Team (DSS)
   ●   OIT Owner of Standard; updates document standards and version number.
   ●   Presents to the Architecture Review Board for approval and adoption.
Secure Office Print Ecosystem (SOPE) - Manager
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Engages with the DSS Team to provide updates to the standard before revision.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
MFP Technical Controls
   ●   Network Access: The MFP device must not be accessible from the open, untrusted internet.
   ●   Hard Drive Encryption: MFPs must support encryption — TLS 1.2 or greater for data in transit,
       and AES-256 for data at rest.
   ●   Device Security Configuration: Must comply with the CIS Benchmark for Printing Devices and
       current data classifications (FTI, HIPAA, etc.).
   ●   Administrative Security: Administrative web servers must be hardened, password protected,
       and patched regularly (at least every 90 days).
   ●   USB Usage: Restricted to approved devices, authorized via the SOPE management exception
       request form.
   ●   Network Placement: Must be on an approved and managed dedicated print VLAN.
   ●   Logging: Print spooler logging of all submitted requests must be enabled and logs reviewed
       regularly.
   ●   Data Wipe: The MFD must securely auto-wipe all data nightly at the agency-specific assigned
       time.
   ●   Wi-Fi Capability: The Wi-Fi capability on MFPs must be disabled.
   ●   Document Security: Must be capable of password protecting documents and data.
   ●   Energy Efficiency: Must be energy efficient or Energy Star compliant.
   ●   Bi-Directional Communication: Must be configured to disable bi-directional communication to
       external networks.
The following protocols must be disabled on all MFPs: AMF; AirPrint; Bluetooth; FTP; HTTP; IPP; IPP
Fax Out; IPPS; Kerberos; LLMNR; Mopria Discovery; MDNS; NetBIOS; NPAP; NFC; NTP; POP3; Proxy

                                                                                           Page 2 of 3

Server; Remote Services; Secure Web Scan; SIEM (direct protocol); SLP; SMB (all versions); Telnet;
TFTP (configuration file); Thin Print Client; Universal Print; Web Scan; Wi-Fi Direct; WINS; WSD; and
XMLNT.

5. Exceptions and Variance
Requests for variances from any provision of this standard must be requested following the Secure
Configuration Exception Request process. The Exception Request process addresses business or
technical reasons for the inability to adhere to one or more requirements. Requests must include
compensating controls.
The Secure Configuration Exception Request form must be submitted to oit_ciso@state.co.us (the
form may be requested by emailing DPA_idscopiers@state.co.us). Exception requests will be
processed and recommended for approval, conditional approval, or denial.

6. References
   ●   CISP-001 IT Access Control Management and User Security
   ●   CISP-003 IT Audit Log Management & Accountability
   ●   CISP-005 Secure Configuration of IT Assets & Software
   ●   CISP-009 Information System Maintenance
   ●   CISP-014 IT Service Provider Management
   ●   CISP-019 Continuous IT Vulnerability Management & Patching
   ●   CIS Printing Devices Benchmark
   ●   Secure Configuration Exception Request

7. Definitions
Multifunction printer (MFP): An all-in-one office machine that incorporates the functionality of
multiple devices in one.
Virtual local area network (VLAN): Any broadcast domain that is partitioned and isolated in a
computer network at the data link layer.
Wi-Fi: Any wireless local area network (WLAN) product based on IEEE 802.11 standards.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification, subject to review and approval by an authority in the area.

                                                                                           Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-012: Multifunction Device/Printer Configuration', links this file as https://drive.google.com/file/d/1N6IDIt62AR5tNpaUzvKgfVOnMTifypmM/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1N6IDIt62AR5tNpaUzvKgfVOnMTifypmM (the source URL above).
