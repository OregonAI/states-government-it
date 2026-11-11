---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-ea-02-04-s
title: 'Enterprise Service: Workforce Identity and Access'
doc_type: standard
citation: WaTech Standard EA-02-04-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2026-04/EA-02-04-S-EnterpriseServiceStandard-WorkforceIdentityandAccess.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: bf068a620a5e49a7d22deefd79ac8881b7080d81ef335c30abdf85fa9f8139cd
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

# Enterprise Service: Workforce Identity and Access (WaTech Standard EA-02-04-S)

## At a glance

Item of the WaTech policy library, chapter '3. Enterprise Architecture' (listed as type Standards). Listed at https://watech.wa.gov/policies/enterprise-service-workforce-identity-and-access.

## Full text

EA-02-04-S                                                                                                                Replaces:
State CIO Adopted: 4/9/2026                                                                                       EA183.20.10 (4.1.1)
TSB Approved: 4/9/2026                                                                                                 July 10, 2008
Sunset Review: 4/9/2028                                                                                                    EA185.10
                                                                                                                       June 6, 2016

                                 WORKFORCE IDENTITY AND ACCESS
                                  ENTERPRISE SERVICE STANDARD
See Also:
RCW 43.105.054 WaTech Governance; (2) “electronic information sharing and access”
RCW 43.105.020 Definitions
RCW 43.105.265 (1) Enterprise Strategy
RCW 43.105.450 (3)(a) “establish security standards and policies to protect the state's information technology systems and
infrastructure”

   1. PURPOSE
        This standard establishes the statewide service capability, Workforce Identity and Access,
        as an enterprise service under EA-02 – Establishing an Enterprise Service Policy. A
        Washington state agency must not adopt a service with similar capabilities unless it has an
        approved waiver or exemption (see Section 5).

   2. SCOPE
        1. Workforce Identity and Access must be used for authentication and authorization of
           workforce identities across all platforms and hosting models.
        2. The scope of this standard does not include anonymous or public-facing systems with
           no workforce identity.

   3. APPLICABILITY
        1. This standard applies to all Washington State agencies and their organizational users,
           including employees, contractors, partners, and vendors accessing internal state
           resources.

   4. ENTERPRISE SERVICE CAPABILITIES
        The Workforce Identity and Access enterprise service designation encompasses the
        following capabilities:
             1. Centralized Workforce Authentication and Authorization – provides a shared,
                enterprise-managed directory service for workforce identities and devices, enabling
                consistent authentication and authorization across on-premises, cloud, and hybrid
                environments. Supports role-based access, group-based controls, and policy-driven
                enforcement.
             2. Federated Identity and Single Sign-On (SSO) – enables secure single sign-on for
                workforce users by federating enterprise identity credentials to trusted internal,

                                                                                                                                 1

        cloud, and partner applications. Reduces credential sprawl while enforcing
        enterprise authentication policies across service boundaries.
     3. Cloud-Based Identity and Access Management – delivers centralized, cloud-enabled
        identity services that manage workforce access to applications and resources
        regardless of hosting model. Supports modern authentication, conditional access,
        multi-factor authentication, and lifecycle management aligned with zero trust
        principles.
     4. Hybrid Directory Extension for Cloud Workloads – extends enterprise directory and
        authentication services into cloud environments to support workloads that require
        domain-based identity, policy enforcement, and device authentication. Enables
        consistent identity controls for cloud-hosted infrastructure while maintaining
        enterprise governance.
     5. Delegated Administration and Operational Governance – provides delegated, role-
        based administrative capabilities that allow agencies to manage workforce identities
        within enterprise-defined guardrails. Supports visibility, auditing, and standardized
        operational controls while preserving centralized governance and compliance.

5. WAIVERS AND EXEMPTIONS TO THIS STANDARD
  In accordance with POL-01-02-S Technology Policy and Standard Waiver Request Standard,
  agencies may qualify for a waiver or exemption from compliance with this standard.
  Agencies may request an exemption for situations that meet one of the following criteria:
     1. Privileged or Bootstrap Accounts that are used only for recovery or provisioning.
     2. Legacy or Air-Gapped Systems including:
            a. State-owned legacy systems lacking modern identity integration capabilities
               (e.g., mainframe systems without Single Sign-On (SSO) interfaces).
            b. Air-gapped or out-of-band managed systems where integration is technically
               infeasible.
        Legacy or Air-Gapped Systems must adhere to security requirements, including SEC-
        04-08-S Unsupported Technology Retirement.
     3. Temporary use or proof-of-concept (POC) applications with all of the following
        attributes:
            a. Duration of less than six months
            b. Non-production environment and data (this exemption will not carry over to
               production deployment)
     4. Accessibility and Accommodation Tools, such as applications required for
        accessibility or reasonable accommodation (e.g., screen readers or text-to-speech
        tools) that do not support enterprise SSO.

                                                                                            2

       5. Vendor-Managed SaaS Applications with limited scope and all of the following
          attributes:
              a. Serve fewer than 10 users with no opportunity to grow beyond 25 users in the
                  future
              b. Do not integrate with any other systems
              c. Handle only Category 1 or Category 2 data
              d. Are not used to support mission-critical or business-essential functions
       6. Legal or Regulatory Systems, including federal or external systems requiring
          mandated credentials, or that do not support Security Assertion Markup Language
          (SAML) or OpenID Connect (OIDC) integrations.
       7. Multi-jurisdictional, regional, or community collaborations that require use of their
          own authentication.

REFERENCES
   1. Service Catalog Page: Workforce Identity and Access
   2. Definition of Terms Used in Policies and Reports
   3. MGMT-01-01-S – Technology Portfolio Foundation – Application Standard
   4. POL-01-01-PR – Technology Policies and Standards Waiver Procedure
   5. POL-01-02-S – Technology Policy and Standard Waiver Request Standard
   6. SEC-02-01-S – Application Security Standard
   7. SEC-04-08-S – Unsupported Technology Retirement
   8. SEC-06 – Access Control Policy
   9. SEC-06-01-S – Identification and Authentication Security Standard
   10. SEC-11-01-S – Risk Assessment Standard

CONTACT INFORMATION
For questions about this standard, contact the WaTech policy mailbox.

                                                                                              3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
