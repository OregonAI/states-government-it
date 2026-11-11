---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-ea-02-07-s
title: 'Enterprise Service: Customer Identity and Access Management'
doc_type: standard
citation: WaTech Standard EA-02-07-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2026-08/EA-02-07-S_CIAM_Approved20260813.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 405d8eabd43c818bdaaeb1f8ac4cd3f888a883184822bdb9ff00730fb2bdacc3
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
- digital-services
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Enterprise Service: Customer Identity and Access Management (WaTech Standard EA-02-07-S)

## At a glance

Item of the WaTech policy library, chapter '3. Enterprise Architecture' (listed as type Standards). Listed at https://watech.wa.gov/policies/enterprise-service-customer-identity-and-access-management.

## Full text

EA-02-07-S                                                                                   Replaces:
State CIO Adopted: 8/13/2026                                                            EA - 183.20.10
TSB Approved: 8/13/2026                                                                    Section 4.2
Sunset Review: 8/13/2028                                                                 July 10, 2008

                    Customer Identity & Access Management
                       ENTERPRISE SERVICE STANDARD
See Also:
RCW 43.105.006 WaTech Purpose
RCW 43.105.020 Definitions
RCW 43.105.054 WaTech Governance
RCW 43.105.450 State agency information technology security

 1. PURPOSE
 This standard establishes the statewide service capability, Customer Identity & Access
 Management (CIAM), as an enterprise service under EA-02 – Establishing an Enterprise
 Service Policy. Customer Identity & Access Management uses appropriate authentication and
 identity verification methods based on the sensitivity of the information being accessed. It is
 intended to ensure consistent user experience, centralized identity management, and
 improved security across state government
 This requirement covers new solutions and system upgrades that present an authentication
 experience to users. A Washington state agency must not adopt, build, expand, or renew a
 service with similar capabilities unless it has an approved waiver or exemption (see
 Section 5).

 2. SCOPE
 In Scope
 The Customer Identity & Access Management Service capabilities must be used to find and
 authenticate access to state online services, websites, and applications managed by the state
 and serving public users.
 Out of Scope
 This standard does not apply to public interactions conducted directly with third-party
 vendors where agency staff do not have any access to the system and do not have any
 administrative or operational responsibilities. These vendors perform eligibility, application,
 payment, verification, assessment, or similar services and report the outcome to the agency.

 3. APPLICABILITY
 This standard applies to all state agencies (as defined in RCW 43.105.020). This standard
 does not apply to the K-20 network, institutions of higher education, legislature, judiciary, or
 local governments.

                                                                                                    1
 •

4. ENTERPRISE SERVICE CAPABILITIES
The Customer Identity & Access Management enterprise service designation encompasses
the following capabilities:
    1. Single Sign-On (SSO) solution for public users doing business with Washington state.
    2. Multi-Factor Authentication (MFA) to validate that the user controls their identifiers
       (such as email address and phone number).
    3. Identity Verification (IDV) confirms a user’s identity and eligibility before granting
       access to services or sensitive information.

5. WAIVERS AND EXEMPTIONS TO THIS STANDARD
In accordance with POL-01-02-S Technology Policy and Standard Waiver Request Standard,
agencies may qualify for a waiver or exemption from compliance with this standard. Agencies
may request an exemption for situations that meet one of the following criteria.
    1. Vendor-managed SaaS applications with limited scope and all of the following
       attributes:
           a. Do not support mission-critical or business-essential functions
           b. Do not integrate with any other systems
           c. Serve fewer than 10 users with no opportunity to grow beyond 25 users
              in the future
           d. Handle only Category 1 and/or Category 2 data
    2. Temporary use or proof-of-concept (POC) applications with all of the following
       attributes:
           a. Duration of less than six months
           b. Non-production environment and data (this exemption will not carry over to
              production deployment)
    3. Legal or Regulatory Systems (including federal or external systems requiring mandated
       credentials) that do not support Security Assertion Markup Language (SAML) or OpenID
       Connect (OIDC) integrations.
    4. Multi-jurisdictional, regional, or community collaborations that require use of their own
       authentication.

6. AUTHORITY
This standard is issued under the authority of RCW 43.105.054, which grants WaTech
authority to establish statewide technology standards and enterprise services. RCW
43.105.385 establishes WaTech as the central service provider for state agencies, supporting
the delivery of common enterprise technology services. RCW 43.105.450 requires state
agencies to comply with statewide information technology security policies and standards.
Executive Order 25-06 establishes a comprehensive approach to improve customer

                                                                                                2
•

experience throughout state government, emphasizing accessibility, efficiency, effectiveness,
security, simplicity, accountability, and customer satisfaction in government service delivery.

REFERENCES
    1. Service Catalog Page: WA.gov Authentication
    2. Definition of Terms Used in WaTech Policies and Reports
    3. RCW 43.105.006 WaTech Purpose
    4. RCW 43.105.054 WaTech Governance
    5. RCW 43.105.450 State agency information technology security
    6. SEC-08-01-S Data Classification Standard
    7. NIST SP 800-63

CONTACT INFORMATION
For questions about this policy, please email the WaTech Policy Mailbox.

                                                                                              3
•

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
