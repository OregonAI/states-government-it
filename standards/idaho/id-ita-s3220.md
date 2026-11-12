---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s3220
title: S3220 – Security – Virtual Private Network
doc_type: standard
citation: ITA Standard S3220
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s3220-1.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 5e2ff364b6031530df5714f5982c3f72137b1886546bfc59e0983fb2424fcc25
effective_date: '2001-10-02'
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

# S3220 – Security – Virtual Private Network (ITA Standard S3220)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '3000 - Network and Telecommunications, Standards', a standard. The library's own summary: "ITA Standard S3220 mandates the use of secure protocols and encryption for virtual private networks to ensure safe and private communication."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS S3000 – NETWORK AND
TELECOMMUNICATIONS

Category:      S3220 – SECURITY – VIRTUAL PRIVATE NETWORK

CONTENTS:

I.    Definition
II. Rationale
III. Approved Standard(s)
IV. Approved Product(s)
V. Justification
VI. Technical and Implementation Considerations
VII. Emerging Trends and Architectural Directions
VIII. Procedure Reference
IX. Review Cycle
X. Contact Information
      Revision History

I. DEFINITION

   See ITA Guideline G105 (Glossary of Terms) for any definitions. G105-ITA Glossary of
   Terms

II. RATIONALE

   There are many business requirements that justify providing logical access to network
   resources, independent of physical topology or location. A VPN implementation can be
   used to fulfill these business requirements while maintaining security standards. Any
   VPN solution must have an architecture that can be implemented within the enterprise
   security policy, including passwords, smart cards, token-based products, directory
   systems (LDAP, etc.), remote access services, and X.509 digital certificates.

III. APPROVED STANDARD(S)

   1. IPsec (IKEv2) for site-to-site VPNs.

   2. TLS-based remote access VPN configured for TLS 1.2/1.3 with AEAD cipher suites
      (AES-GCM/ChaCha20-Poly1305). CBC ciphers are not authorized without a firewall
      exception.

   3. SAML 2.0 for SSO and federated identity with MFA enforced at IdP.

S3220 – Security – Virtual Private Network                                      Page 1 of 3

   4. Zero Trust/SDP/ZTNA patterns for private-app access where feasible.

IV. APPROVED PRODUCT(S)

   Refer to approved state contracts for IT Security Products:
   https://purchasing.idaho.gov/statewide-contracts/

V. JUSTIFICATION

   Products provided in the state contracts are recognized as industry leaders.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

   Enforce MFA for all VPN access with SSO via SAML 2.0 IdP; configure GlobalProtect
   SAML Authentication Profile (GP-SAML-Auth-ID). Require TLS 1.2/1.3 AEAD ciphers;
   IPsec IKEv2 for site-to-site. Default full-tunnel for sensitive workloads; split-tunnel only
   by documented exception. Log authentication events and forward to SIEM, or log
   collector; enforce posture checks; apply formal change control.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

   Zero Trust Architecture (ZTA), SASE/SSE adoption, TLS modernization (TLS 1.3),
   federated authentication (SAML/OAuth/OIDC).

VIII. PROCEDURE REFERENCE

   Pairs with ITS ISPM v4.0 (AC-17 Remote Access, S.IA-01 Authentication, AU-01/06
   Logging, SC-07 Boundary Protection), NIST SP 800-77, NIST SP 800-52 Rev.2, OASIS
   SAML v2.0. CBC cipher use requires approval.

IX. REVIEW CYCLE

   Every 3 years.

X. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

REVISION HISTORY

    05/05/2026 - Updates refine wording, standardize formatting, remove redundant text, and
shift definitions to G105 for a more streamlined VPN standard.

   07/01/13 – Changed “ITRMC” to “ITA”.

   6/16/09 – Deleted Timeline from standard.

S3220 – Security – Virtual Private Network                                             Page 2 of 3

    3/7/07 – Added additional considerations regarding new or replacement remote access
   solutions.

   9/13/06 – Added SSL as an approved standard. Added F5 FirePass as an approved
             SSL product. Updated technical considerations and procedural reference.

   4/25/05 – Added Cisco VPN products.

   8/25/04 – Acknowledged emerging trend of SSL-based VPNs.

               Effective Date:       October 2, 2001

S3220 – Security – Virtual Private Network                                    Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
