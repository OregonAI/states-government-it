---
schema_version: 1
corpus: states-government-it
jurisdiction: nevada
id: nv-sec-s-6-03-02
title: Vulnerability Management
doc_type: standard
citation: S.6.03.02
authority_level: ''
issuing_body: Nevada State Information Security Committee; published by the Governor's Technology Office
  (Office of Information Security and Cyber Defense)
source_url: https://it.nv.gov/siteassets/itnew.nv.gov/content/governance/security/s.6.03.02-vulnerability-management.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 8c60526648853a0a34d4d9d750acd06bf85b69e1e3d87dd2daae5ef07aade4e6
effective_date: '2021-09-01'
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

# Vulnerability Management (S.6.03.02)

## At a glance

Listed on the Governor's Technology Office page 'Security Policies, Standards & Procedures' (https://it.nv.gov/governance/security-policies-standards--procedures/) as 'S.6.03.02 Vulnerability Management - Effective 09/01/2021'. NAC 242.110 adopts the State Information Security Policies, Standards and Procedures by reference and binds every executive-branch agency, state employee and contractor with access to state information to them. Minimum vulnerability management requirements for technology assets.

## Full text

                                     State of Nevada
                               Information Security Committee

                                             Standard
Document ID       Title                                            Revision      Effective Date        Page
  S.6.03.02       Vulnerability Management                             A            9/01/2021         1 of 3

1.0   PURPOSE
      This standard establishes the minimum requirements for vulnerability management on technology
      assets, including both Operating System (OS) and non-OS software, as required to implement
      the CIS Controls v7.1.

2.0   SCOPE
      This standard applies to all state agencies and authorized users meeting the criteria identified in
      the State Information Security Program Policy, Section 1.2, Scope and Applicability.

3.0   EFFECTIVE DATES
      This standard becomes effective at the time of approval of the State Chief Information Officer
      (CIO).

4.0   RESPONSIBILITIES
      The agency head and appointed Information Security Officer (ISO) have the responsibility to
      ensure the implementation of and compliance with this standard.

5.0   RELATED DOCUMENTS
      State Information Security Program Policy, 100
      Software Inventory and Control, S.6.02.01
      Software Patch Management, S.6.03.01

6.0   STANDARD
      6.1     Run automated vulnerability scanning tool

              A. Agencies must adopt and implement a Security Content Automation Protocol (SCAP)
                 compliant vulnerability scanning tool in their environment. Agencies should use the
                 state’s enterprise vulnerability management tool, as it meets SCAP requirements and
                 supports compliance with other CIS Controls requirements.
              B. Agencies must have a documented procedure in place for automatically scanning all
                 devices on their network, both managed and unmanaged, on at least a weekly basis.
              C. Vulnerability scans must document a list of all identified potential vulnerabilities on the
                 agency’s systems.
      6.2     Perform authenticated vulnerability scanning

              A. Agencies must implement local scanning agents on each of their devices or configure
                 remote scanners to perform authenticated vulnerability scans of every system on their
                 network. All scans must be performed with the required credentials and elevated
                 privileges to perform authenticated scans.

                                     State of Nevada
                                Information Security Committee

                                              Standard
Document ID       Title                                           Revision      Effective Date         Page
  S.6.03.02       Vulnerability Management                            A            9/01/2021           2 of 3

      6.3     Protect dedicated assessment accounts

              A. Agencies must designate at least one service account as an authorized vulnerability
                 scanning account and provide the account(s) with elevated privileges required on every
                 system they scan.
              B. Agencies must not use authorized vulnerability scanning accounts for any purpose
                 other than official vulnerability scans.
      6.4     Compare back-to-back vulnerability scans

              A. The SCAP compliant vulnerability scanning tool agencies utilize must allow for
                 comparing consecutive months’ vulnerability scan results to show timely remediation of
                 identified vulnerabilities.
              B. Agencies should maintain vulnerability scan results for at least three months to facilitate
                 this comparison.
      6.5     Utilize a risk-rating process

              A. Agencies must adopt a standard, industry-recognized risk-rating methodology, such as
                 the Common Vulnerability Scoring System (CVSS) or similar system, and use it to
                 assign a criticality to each identified vulnerability.
              B. Agencies must prioritize the remediation of identified vulnerabilities based on the
                 criticality assigned by their risk-rating methodology.
              C. Agencies must have a documented process in place detailing their selected risk-rating
                 and prioritization methodologies for vulnerability management.

7.0   DEFINITIONS
      Patch or Update: An improvement to software, including security patches, software updates to
      firmware, cumulative software patches, and other software features.

      Technology Assets: As defined in CIS Controls v7.1, the term “Technology Assets” (also
      referred to therein as “Hardware Technology Assets” or “Hardware Assets”) collectively refers to
      equipment and devices that have the potential to store or process information, whether connected
      to the network or not.

8.0   RESOURCES
      Center for Internet Security (CIS), CIS Controls Guide v7.1

9.0   EXCEPTIONS
      Requests for exception to the requirements of this Information Security Standard must be
      documented, provided to the Office of Information Security (OIS), and approved by the State
      Chief Information Security Officer (CISO).

                                    State of Nevada
                                Information Security Committee

                                            Standard
 Document ID      Title                                            Revision     Effective Date       Page
   S.6.03.02      Vulnerability Management                            A           9/01/2021          3 of 3

Approved By
 Title                                                 Signature                          Approval Date
 State Information Security Committee                  Approved by Committee                     8/26/2021
 State Chief Information Security Officer (CISO)       Signature on File                         8/30/2021
 State Chief Information Officer (CIO)                 Signature on File                         9/01/2021

Document History
 Revision      Effective Date   Change
     A             9/01/2021    Initial release for alignment with CIS Controls v7.1, Control 3 Continuous
                                Vulnerability Management

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
