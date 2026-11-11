---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-ciso-005
title: Patch Management Standard
doc_type: standard
citation: TS-CISO-005
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1vxvFKeDJ3g2GpNpr_47Q9oQwMCIqhjOo
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 9b4d54849a45c0d7166a2d00c2aadbe08a61d646dc33a2a1eb1b8dd46095a4fa
effective_date: '2026-01-31'
source_version: 2.0, last updated 05/13/2026
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads 'TS-CISO-005 Patch Management Standard v2026', links this file as https://drive.google.com/file/d/1vxvFKeDJ3g2GpNpr_47Q9oQwMCIqhjOo/view?usp=sharing;
  the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1vxvFKeDJ3g2GpNpr_47Q9oQwMCIqhjOo
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

# Patch Management Standard (TS-CISO-005)

## At a glance

OIT technical standard TS-CISO-005 (Information Security): Patch Management Standard. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-CISO-005: Patch Management Standard
  Document ID                      TS-CISO-005
  Title                            Patch Management Standard
  Executive Sponsor                Jill Fraser, Chief Information Security Officer
  Issuing Authority                Governor’s Office of Information Technology (OIT)
  Applies to                       All state government employees, contractors, vendors, and
                                   external users who access state government information systems
                                   and applications, regardless of location or device, including all
                                   applications, hosting environments, and physical and connected
                                   technologies.
  Instrument Type                  Standard
  Version                          2.0
  Effective Date                   01/31/2026
  Last Updated                     05/13/2026

Purpose
This standard defines security requirements for the timely application of patches and updates
across all State-managed information systems and applications, including on-premises and
cloud environments. It supports compliance with the Colorado Information Security Policies
(CISPs).

Scope
This standard applies to all state government employees, contractors, vendors, and external
users who access state government information systems and applications, regardless of
location or device. This includes all applications and hosting environments, and access to
physical and connected technologies.

Requirements
The appropriate patch management standard requirements are listed below. Additional
requirements must be implemented based on the regulated data type(s).

Vulnerability Scanning
 Requirement              Detail
 Frequency                Vulnerability scans shall be conducted regularly, at least weekly.
 Tools                    Scans shall be conducted using an industry-approved vulnerability
                          scanner.

                                                                                         Page 1 of 2

 Requirement              Detail
 Results                  Scan results must be made available to the appropriate staff.

Patching Timeframes
 Severity Level          System Type          Timeframe                      Configuration
                                                                             Requirement
 Critical, High, and     Servers              Patches applied within 30      All configurations
 Medium                                       days of patch release.         required to make a
                                                                             patch “active” must
                                                                             be fully applied in
                                                                             the same timeframe.
 Critical, High, and     Workstations         Patches pushed to them         —
 Medium                                       within 30 days.
 Low-Severity & Secure   All systems          May be applied on a            —
 Configuration                                scheduled basis or as
                                              resources permit, as
                                              determined by team SOPs.

Exceptions
All exceptions must be documented, justified, and approved by the State of Colorado's Chief
Information Security Officer (CISO) or other designated authority. Compensating controls must
be documented, implemented, and maintained.

Compliance
The Information Security Office will monitor and advise on compliance with this standard.

                                                                                          Page 2 of 2

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-CISO-005 Patch Management Standard v2026', links this file as https://drive.google.com/file/d/1vxvFKeDJ3g2GpNpr_47Q9oQwMCIqhjOo/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1vxvFKeDJ3g2GpNpr_47Q9oQwMCIqhjOo (the source URL above).
