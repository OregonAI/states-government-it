---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-007
title: Wireless Site Survey
doc_type: standard
citation: TS-INF-007
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1vnoD0Yc8vKJB0uL5Oww9k2dmhhchNNl6
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 66f449aa99f76b23094d8258d88abebfe2f5442bd0a7725aa64ef709d5dc478d
effective_date: '2017-04-20'
source_version: 4.0, last updated 03/10/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-007: Wireless Site Survey'', links this file as https://drive.google.com/file/d/1vnoD0Yc8vKJB0uL5Oww9k2dmhhchNNl6/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1vnoD0Yc8vKJB0uL5Oww9k2dmhhchNNl6
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

# Wireless Site Survey (TS-INF-007)

## At a glance

OIT technical standard TS-INF-007 (Infrastructure): Wireless Site Survey. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-007: Wireless Site Survey
  Document ID                      TS-INF-007
  Title                            Wireless Site Survey
  Executive Sponsor                OIT Network Enterprise Engineering
  Issuing Authority                Office of Information Technology (OIT)
  Applies to                       OIT staff, OIT-supported agencies, and contractors, vendors, and
                                   integrators. Governs all net-new and go-forward wireless
                                   deployments; not retroactively enforceable for legacy systems
                                   unless part of modernization.
  Tier                             Standard
  Version                          4.0
  Effective Date                   04/20/2017
  Last Updated                     03/10/2026

1. Purpose
In accordance with C.R.S. §24-37.5, the Office of Information Technology (OIT) is responsible for
delivering secure, reliable, and efficient IT services to the State of Colorado and its supported
agencies. The purpose of this standard is to define mandatory requirements and engineering
guidance for planning, validating, and documenting wireless network deployments under the OIT
Enterprise Wireless Solution.
Wireless Site Surveys ensure: wireless networks are designed based on measured RF conditions;
Access Point (AP) quantity, type, and placement support coverage, capacity, and performance;
deployments meet operational, security, and environmental constraints; and post-deployment
performance aligns with intended service levels. Both pre-implementation and post-implementation
validation surveys are required.

2. Scope
This standard applies to OIT staff, OIT-supported agencies, and contractors, vendors, and
integrators. It governs all net-new and go-forward wireless deployments and is not retroactively
enforceable for legacy systems unless part of modernization.

3. Roles and Responsibilities
Architecture Review Board (ARB)
   ●      Engages stakeholders and subject matter experts to determine the standard.
   ●      Reviews and approves the Standard (this document).

                                                                                           Page 1 of 3

OIT - Network Enterprise Engineering
   ●   Owner of Standard; responsible for defining and updating the Enterprise wireless standards.
   ●   Subject matter expert in wireless design and architecture.
   ●   Confers with security teams on State security policies.
   ●   Updates the standards to keep up with new wireless technologies, industry trends, and best
       practices.
OIT Staff and Contractors
   ●   All personnel engaged in wireless planning or deployment must be familiar with this standard.
   ●   Apply it during design and deployment, and document compliance or approved exceptions.

4. Standards
Required Survey Types
   ●   Budgetary planning: Predictive survey.
   ●   Pre-install validation: Active survey (required).
   ●   Post-install validation: Active survey (required).
   ●   Security analysis: Passive survey (supplemental).
   ●   Active surveys are mandatory for all enterprise deployments to ensure real RF performance is
       measured.
RF Design Standards
   ●   Frequency Bands: 2.4 GHz and 5 GHz required; 6 GHz included where supported.
   ●   Channelization: 20 MHz baseline; wider channels require justification.
   ●   !"#$%&'$()(*&+&,(-(./0(123(4(-(56(12(789:(;"<=$,(-(./6(123(4(-(>?(12(789:
   ●   Surveys must identify non-Wi-Fi RF sources, neighboring WLAN interference, and channel
       overlap/co-channel contention risks.
Office / Administrative Facilities
   ●   !"#$%&'$(@&%'$+A,(7<'B&C(A+%$B'+D(-(./0(123E(789(-(56(12E(F?GF6H(=$CC("#$%C&IE(I&=J$+(C"AA(K(
       5HE(C&+$B=L(K(5??(3A:
   ●   Conference rooms and training areas must be designed for capacity, not just coverage.
   ●   Band Prioritization: 5 GHz primary; 6 GHz where supported; 2.4 GHz limited to legacy or IoT
       devices.
Healthcare / Hospital Facilities
   ●   Mission-critical, high-interference, device-dense environments.
   ●   7<'B&C(A+%$B'+D(-(./6(123E(789(-(>?(12E(F6G5?H("#$%C&IE(I&=J$+(C"AA(K(FH:
   ●   Consider wet walls, lead shielding, roaming corridors, telemetry, and patient-safe mounting.
Warehouse / Industrial Facilities
   ●   RF-hostile, reflective, and dynamic environments.
   ●   7<'B&C(A+%$B'+D(-(./0(123E(789(-(56(12E(%$+%<$A(K(F6H:
   ●   Account for metal racking, reflections, high ceilings, moving inventory, and directional
       antenna needs.
Post-Installation Acceptance Criteria
                                                                                           Page 2 of 3

   ●   Coverage: All areas meet signal thresholds; no dead zones.
   ●   Performance: Roaming validated; throughput meets design.
   ●   RF Health: Acceptable noise floor; minimal co-channel interference.
   ●   Infrastructure: APs installed per design; cabling labeled and tested.
   ●   Security: SSIDs correct; encryption verified; rogue scan complete.
   ●   Documentation: Final maps; heatmaps; validation report; variances documented.

5. Variance and Exception Process
Deviations require a formal Exception Request with business/technical justification, approved by the
Network Services Manager.

6. References
   ●   C.R.S. §24-37.5
   ●   OIT Enterprise Wireless Standards
   ●   TS-INF-009 Infrastructure as Code Standard

7. Definitions
Active Survey: RF survey where a client associates with APs to measure performance, data rates,
and roaming.
Passive Survey: Listen-only RF scan used for interference or rogue detection.
Predictive Survey: Software modeling based on floor plans without field measurements.
Wireless Access Point (AP): Device providing Wi-Fi connectivity to clients.
Client Device: Laptop, phone, scanner, medical device, or IoT device using Wi-Fi.
Wi-Fi: WLAN technology based on IEEE 802.11 standards.

                                                                                         Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-007: Wireless Site Survey', links this file as https://drive.google.com/file/d/1vnoD0Yc8vKJB0uL5Oww9k2dmhhchNNl6/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1vnoD0Yc8vKJB0uL5Oww9k2dmhhchNNl6 (the source URL above).
