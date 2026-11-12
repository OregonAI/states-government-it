---
schema_version: 1
corpus: states-government-it
jurisdiction: nevada
id: nv-sec-s-5-04-04
title: Data Security Architecture
doc_type: standard
citation: S.5.04.04
authority_level: ''
issuing_body: Nevada State Information Security Committee; published by the Governor's Technology Office
  (Office of Information Security and Cyber Defense)
source_url: https://it.nv.gov/siteassets/itnew.nv.gov/content/governance/security/FINAL_S_5_04_04_Data_Security_Architecture.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 9f2fc830ce5b9e8c3735e6a0d09e3e9bd70e6ccd86666d220a193d4730d9921f
effective_date: '2020-12-31'
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
- data
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Data Security Architecture (S.5.04.04)

## At a glance

Listed on the Governor's Technology Office page 'Security Policies, Standards & Procedures' (https://it.nv.gov/governance/security-policies-standards--procedures/) as 'S.5.04.04 - Data Security Architecture - Effective 12/31/2020'. NAC 242.110 adopts the State Information Security Policies, Standards and Procedures by reference and binds every executive-branch agency, state employee and contractor with access to state information to them. Minimum security requirements for the architectural protection of IT applications, systems and data.

## Full text

                                      State of Nevada
                                Information Security Committee

                                              Standard
Document ID       Title                                              Revision       Effective Date        Page
  S.5.04.04       Data Security Architecture                             C            12/31/2020         1 of 2

1.0   PURPOSE
      This establishes minimum security requirements for the architectural protection of information
      technology (IT) applications, systems, and data.

2.0   SCOPE
      This standard applies to all state agencies meeting the criteria identified in the State Information
      Security Program Policy, Section 1.2, Scope and Applicability.

3.0   EFFECTIVE DATES
      This standard becomes effective at the time of approval of the State Chief Information Officer
      (CIO).

4.0   RESPONSIBILITIES
      The agency head and appointed Information Security Officer (ISO) have the responsibility to
      ensure the implementation of and compliance with this standard.

5.0   RELATED DOCUMENTS
      State Information Security Program Policy, 100
      Data Sensitivity, S.3.02.01
      Information Security Risk Analysis, S.3.07.01

6.0   STANDARD
      The core component of determining the appropriate security model to utilize is based on the data
      classification of the information being protected, requirements mandated by legal and regulatory
      governance, and the agency’s willingness to accept risk.

      6.1     A risk analysis must be performed and approved by the agency’s ISO before
              implementation of a new service, application, or system.

      6.2     A separate, distinct, and complete security policy filter must be placed between data
              security layers with differing levels of trust. A single security policy filter may not be used for
              multiple data security layers.

      6.3     ISOs are responsible to ensure security policy filters are applied and functioning as
              required to protect State information.

7.0   DEFINITIONS
      Data Security Layers: A security layer consists of a defined set of objects, components, or
      process that require the same level of trust.

      Security Policy Filter: A hardware and/or software component that performs one or more of the
      following functions: (i) content verification to ensure the data type of the submitted content; (ii)
      content inspection, analyzing the submitted content to verify it complies with a defined policy
      (e.g., allowed vs. disallowed file constructs and content portions); (iii) malicious content checker

                                       State of Nevada
                                  Information Security Committee

                                               Standard
 Document ID        Title                                             Revision     Effective Date       Page
   S.5.04.04        Data Security Architecture                           C           12/31/2020         2 of 2

          that evaluates the content for malicious code; (iv) suspicious activity checker that evaluates or
          executes the content in a safe manner, such as in a sandbox/detonation chamber and monitors
          for suspicious activity; or (v) content sanitization, cleansing, and transformation, which modifies
          the submitted content to comply with a defined policy. Some examples include:

              1. Firewalls
              2. Intrusion prevention services or systems
              3. Access control configured to inspect for source host, destination host, and source and
                 destination protocol and ports
              4. Other security appliances specifically designed to inspect all communications between
                 layers

8.0       RESOURCES
          NIST 800-53 Security and Privacy Controls for Federal Information Systems and Organizations
          NIST 800-53, AC-4 Supplemental Guidance on security policy filters

9.0       EXCEPTIONS
          Requests for exception to the requirements of this Information Security Standard must be
          documented, provided to the Office of Information Security (OIS), and approved by the State
          Chief Information Security Officer (CISO).

Approved By
 Title                                                    Signature                           Approval Date
 State Information Security Committee                     Approved by Committee                   11/19/2020
 State Chief Information Security Officer (CISO)          Signature on File                       11/24/2020
 State Chief Information Officer (CIO)                    Signature on File                       11/30/2020

Document History
 Revision       Effective Date    Change
      A              9/06/2018    Initial release
      B             12/26/2018    Renumbering (115 to S.5.04.04) and compliance to ADA standards
      C             12/31/2020    Biennial review for alignment with CIS Controls v7.1, Implementation
                                  Group 1 (IG1)

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
