---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-sec-04-03-s
title: Configuration Management Standard
doc_type: standard
citation: WaTech Standard SEC-04-03-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2024-08/SEC-04-03-S%20Configuration%20Management%20Standard.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 656ba3d14afde1e4577827141e6d7f8ae811f2c7bafec100169c0b8a9c58f2a9
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters).
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

# Configuration Management Standard (WaTech Standard SEC-04-03-S)

## At a glance

Item of the WaTech policy library, chapter '4. IT Security' (listed as type Standards). Listed at https://watech.wa.gov/policies/configuration-management-standard.

## Full text

SEC-04-03-S                                                                                                   Replaces:
State CIO Adopted: August 11, 2023                                             IT Security Standard 141.10 (5.1.1, 5.6.2)
TSB Approved: September 14, 2023                                                                   December 11, 2017
Sunset Review: September 14, 2026

               CONFIGURATION MANAGEMENT STANDARD
See Also:
RCW 43.105.054 WaTech Governance
RCW 43.105.052 Powers and duties of agency—Application to higher education, legislature, and judiciary.
RCW 43.105.020 (22) “State agency”
RCW 43.105.450 Office of Cybersecurity
SEC-11-01-S Information Security Risk Assessment Standard
NIST 800-37r2 Risk Management Framework
NIST 800-128 Guide for Security-Focused Configuration Management

    1. Agencies must create a configuration baseline for all systems that would impact
       the agency’s security posture as part of the agency’s security program:

            a. Develop, document, and maintain under configuration control, a
                current baseline configuration of information systems referencing
                the Center for Internet Security (CIS) benchmarks, and/or vendor-
                provided secure baseline configuration requirements. See the SEC-
                04 Asset Management Policy.

                     i. If CIS benchmarks and/or vendor-provided secure baseline
                        configuration requirements are not available, the agency must
                        develop, document, and maintain a secure configuration for
                        the solution and may consult with WaTech.

                     ii. WaTech will offer additional guidance and services for
                         securing endpoints using CIS benchmarks. Agencies must
                         utilize the Endpoint Detection Response (EDR) solution where
                         applicable.

            b. Define, document, approve, and enforce physical and logical access
               restrictions associated with changes to the information system
               baseline configurations. Identify, document, and approve any
               deviations from established configuration. See SEC-06 Access Control
               Policy.

            c. Retain one previous version of baseline configurations of information
                systems to support rollback.

                                                                                                                   1

        d. Monitor and control changes to the configuration settings in
           accordance with the SEC-04-03-S Change Management Policy.

        e. Review and update the baseline configurations annually or after
            changes to that baseline.

2. Agencies must exercise configuration change control for all systems that would
   impact the agency’s security posture:

        a. Determine the types of changes to the information system that affect its
            configuration and their potential impacts. Configuration change control
            documentation must be handled, at minimum, as category 3 information.

        b. Test, validate, and document the proposed information system
            configuration change prior to implementation. This must include
            identification of potential security impacts.

        c. Document configuration change decisions associated with the
            information system.

        d. Implement approved configuration changes to the information
            system.

        e. Retain records of configuration changes for the period of one year
            after the date of the change according to the required retention
            period. See GS 14020 Rev 1. State Government General Retention
            schedules v.6.1.

        f. Perform an annual internal review of configuration changes to ensure
            compliance with internal change management processes.

3. Agencies must configure all information systems that would impact the agency’s
   security posture to provide only business-related capabilities and prohibit the
   use of functions, ports, protocols, and/or services that are not required for
   business functions.

REFERENCES

   1.   Definition of Terms Used in WaTech Policies and Reports.
   2.   Center for Internet Security (CIS) benchmarks.
   3.   SEC-04 Asset Management Policy.

                                                                                      2

  4.   SEC-06 Access Control Policy.
  5.   SEC-04-03-S Change Management Policy.
  6.   GS 14020 Rev. 1 State Government General Records Retention Schedule
       v.6.1.
  7.   NIST Cybersecurity Framework Mapping:
          a. Detect.Anomalies and Events (DE.AE-1): A baseline of network
              operations and expected data flows for users and systems is
              established and managed.
          b. Protect.Information Protection Processes and Procedures
              (PR.IP-1): A baseline configuration of information
              technology/industrial control systems is created and
              maintained incorporating security principles (e.g.,
              concept of least functionality).
          c. Protect.Information Protection Processes and
              Procedures (PR.IP-2): A System Development Life
              Cycle to manage systems is implemented.
          d. Protect.Protective Technology (PR.PT-3): The principle
              of least functionality is incorporated by configuring
              systems to provide only essential capabilities.

CONTACT INFORMATION

  •    For questions about this policy, please email the WaTech Policy Mailbox.
  •    For questions about risk assessments and management, please email
       the Risk Management Mailbox.

                                                                                  3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
