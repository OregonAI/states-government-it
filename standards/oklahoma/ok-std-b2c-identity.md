---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-b2c-identity
title: B2C Identity Standard
doc_type: standard
citation: OMES B2C Identity Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/b2c-identity-standard-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 08a781a7aad44182a5fe929d0e54659058955f67d8a3bb56665e452fb281c5ed
effective_date: '2025-08-21'
source_version: Last revised 08/21/2025
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
- governance
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# B2C Identity Standard (OMES B2C Identity Standard)

## At a glance

A CIO standard in the 'IT Enterprise Governance' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This standard establishes guidelines for implementing B2C identity solutions across State of Oklahoma applications and services. The objective is to normalize identity sources that Oklahoma residents can use to access eligible services across application and agency boundaries, enhancing user experience while maintaining security.

## Full text

                                     B2C Identity Standard

Introduction
B2C applications and processes can vary from agency to agency. This document is designed to
set forth standards for those working with or within the State of Oklahoma when it comes to B2C
technology.

Purpose
This standard establishes guidelines for implementing B2C identity solutions across State of
Oklahoma applications and services. The objective is to normalize identity sources that
Oklahoma residents can use to access eligible services across application and agency
boundaries, enhancing user experience while maintaining security.

Definitions
B2C – business to consumer.

MFA – multi-factor authentication.

Standard
   • Identity platform.
         o State of Oklahoma agencies shall utilize Azure Active Directory B2C as the
             standardized external identity platform for public-facing applications requiring
             user authentication.
   • Required identity fields.
         o All B2C identity implementations must collect and maintain the following
             minimum required fields:
                  First name.
                  Last name.
                  Email address.
                         • Serves as an immutable username.
                         • Email addresses cannot be changed for existing user accounts.
                             Users requiring a new email address must create a new account.
   • Security requirements.
         o Multi-Factor Authentication.
                  MFA security capabilities shall be implemented for all applications.
         o Context-aware security.
                  Implementations should leverage context-aware security features
                     including:
                         • Browser behavior analysis.
                         • Location pattern detection.
                         • Time-based access controls.
                         • Network allow/deny lists.
         o Compliance requirements.
                  All B2C identity implementations must comply with:
                         • Software approval process.
                         • FedRAMP standard.
                                o Via Azure Commercial Cloud deployment.

•   Implementation guidelines.
       o Eligibility criteria.
                Applications must meet the following criteria to utilize the B2C identity
                   standard:
                       • Serve constituents or external partners.
                       • Require user authentication.
                       • Comply with OMES IS policies.
                       • Intend for public or semi-public use.
       o Application metadata requirements.
                Applications integrating with B2C identity shall define:
                       • Redirect URIs and reply URLs.
                       • Client names following standard naming conventions.
                               o <agency-app-lifecycle>
                       • Platform-specific requirements.
                       • User journey flows.
                               o Sign-in, sign-up, etc.
       o Profile data dependencies.
                Applications should not rely solely on B2C identity for comprehensive
                   profile data beyond the required fields. Applications may supplement B2C
                   identity data with their own profile management functionality while using
                   B2C email as the primary identifier.
•   Governance and responsibilities.
       o Governance structure.
                The OMES executive team provides governance oversight for B2C
                   identity standard implementation and compliance.
       o Organizational responsibilities.
                OMES IS Security.
                       • Review and approve applications for B2C directory access.
                       • Ensure compliance with security standards and risk management
                            requirements.
                OMES IS Hosted Services.
                       • Facilitate application onboarding to B2C directory.
                       • Provide technical integration support.
                OMES IS Service Desk.
                       • Provide user support for B2C identity-related issues.
                OMES IS Technology Strategy.
                       • Maintain technical standards and architectural guidance.
                       • Provide strategic planning for B2C identity evolution.
                OMES IS Application Team.
                       • Provide technical integration support for custom flows.
•   Quality Assurance.
       o Testing requirements.
                All B2C identity integrations must undergo validation and testing to
                   ensure proper functionality and security compliance before production
                   deployment.
       o Accessibility.
                B2C identity implementations shall comply with applicable accessibility
                   standards and guidelines.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§
34.11.1 and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended
standards policies and standards at any time. Compliance is expected with all published policies
and standards, and any published amendments thereof. Employees found in violation of this
standard may be subject to disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases
and projects to enable the chief information officer to assess the needs and capabilities of state
agencies as well as streamline and consolidate systems to ensure that the state delivers
essential public services to its citizens in the most efficient manner at the lowest possible cost to
taxpayers.

References
   • Microsoft Azure Active Directory External Identities Documentation.
   • NIST Multi-Factor Authentication Guidelines.
   • OMES IS Software Approval Process.
   • FedRAMP Security Standards.
   • OMES IS Policies and Standards.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: MM/DD/YYYY         Review cycle: Annual
 Last revised: 08/21/2025           Last reviewed: 08/21/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
