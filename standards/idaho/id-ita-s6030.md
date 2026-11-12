---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s6030
title: S6030 – Identity and Authentication
doc_type: standard
citation: ITA Standard S6030
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s6030.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 16c9de69926f94fbdf5d2548e3ad7b7c8bcc34ebac1c7ba60f85b5f0d710aeda
effective_date: '2021-12-14'
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

# S6030 – Identity and Authentication (ITA Standard S6030)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '6000 - Security, Standards', a standard. The library's own summary: "ITA Standard S6030 defines identity and authentication requirements to safeguard system access, ensure user verification, and uphold cybersecurity across agencies."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S6000 SECURITY

Category:     S6030 – IDENTITY AND AUTHENTICATION

CONTENTS:
I.   Definition
II. Rationale
III. Approved Standard(s)
IV. Procedure Reference
V. Review Cycle
VI. Contact Information
     Revision History

I. DEFINITIONS

   See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

II. RATIONALE

   A vital element for the proper protection of an enterprise and its assets is a strong
   identity management and authentication program. The objective of this standard is to
   provide basic authentication requirements, based on published industry best practices,
   that form a solid foundation for current and future identity and access management (IAM)
   strategies.

   This standardizes addresses and outlines mandatory risk and privilege-based
   authentication management including password complexity, length, acceptable use,
   augmentation of multi-factor authentication (MFA), and verifier minimum requirements.

III. APPROVED STANDARD(S)

   1. All accounts, devices, and services must be protected from unauthorized access and
      use with, at a minimum, a username and password that meets the mandatory length
      and complexity requirements described herein.
   2. All passwords must:
          a. Be eight (8) characters or longer
          b. Contain at least one (1) uppercase letter
          c. Contain at least one (1) lowercase letter
          d. Contain at least one (1) numeric or symbol character
          e. Not be the same as any of the last 24 passwords
   3. All passwords for user accounts with elevated privileges must meet complexity
      requirements and contain at least 15 characters.

S6030 – Identity and Authentication                                             Page 1 of 3

   4. Service accounts and built-in accounts (e.g. local administrator, super administrator,
       etc.) must meet complexity requirements and contain at least 20 characters.
   5. Passwords on legacy systems, such as mainframes or other antiquated systems
       incompatible with requirements 2-4, must be the maximum allowable length and
       contain as many complexity elements as possible. These passwords on legacy
       systems should also be considered for more frequent changes as a compensating
       control for their weak authentication capabilities.
   6. User accounts and passwords must uniquely identify an individual and are only for
       this assigned individual’s use. Sharing of user account credentials and passwords is
       prohibited.
   7. All users are responsible for the protection of their user accounts and must take all
       reasonable measures to protect them from disclosure or misuse.
   8. Upon the separation of any user, for voluntary or involuntary reasons, all accounts
       the user had access to must be disabled and undergo an immediate authenticator
       reset to maintain account integrity.
   9. All user accounts with elevated privilege must be protected with multi-factor
       authentication (MFA). Per CIS Critical Security Controls v7, control 16.3, all accounts
       must be protected with MFA. While other CIS controls specify MFA, control 16.3 is
       the most comprehensive.
   10. User accounts must lock out after a maximum of five (5) failed authentication
       attempts within 15 minutes. Locked user accounts must be manually re-enabled by
       an approved IT technician, by way of a self-service solution, or automatically unlock
       after 15 minutes. Locked privileged accounts must not automatically unlock and are
       only to be unlocked by an approved IT technician or self-service solution.
   11. Agencies may implement a self-service solution for non-privileged accounts to unlock
       or reset their account, or to manage their multi-factor authenticators. Self-service
       authentication solutions should use multi-factor authentication wherever possible.
   12. Except service accounts and privileged accounts, all accounts will have mandatory
       password changes performed every 90 days or if suspected compromised, whichever
       is soonest. Service accounts will have passwords changes performed every 24
       months or if suspected compromised, whichever is soonest. Privileged accounts will
       have password changes performed every 60 days or if suspected compromised,
       whichever is soonest.
   13. Certificate-based authenticators must be reissued at least every 24 months.
   14. All sensitive network devices and servers to include switches, routers, and
       particularly domain controllers will be protected with MFA.
   15. Password management solutions will be used to contain and manage all enterprise
       sensitive passwords when feasible.
   16. Verifiers must permit a password at least 64 characters in length.
   17. Verifiers must permit use of ASCII and Unicode characters, including space
       characters.
   18. Verifiers must only handle passwords in hashed or encrypted form using approved
       security functions, per FIPS 140-2 Annex A.

IV. PROCEDURE REFERENCE

S6030 – Identity and Authentication                                                Page 2 of 3

   •   ITA Policy P4503 (Identity and Access Management)
   •   ITA Policy P4130 (Information Systems Classification Policy)
   •   IRS Publication 1075 (Tax Information Security Guidelines for Federal, State, and
       Local Agencies)
   •   NIST Special Publication 800-63-3 (Digital Identity Guidelines)
   •   NIST Internal Report 7298r2 (Glossary of Key Information Security Terms)
   •   NIST FIPS Publication 140-2 (Security Requirements for Cryptographic Modules)
   •   CIS Critical Security Controls v7

V. REVIEW CYCLE

   Twelve (12) Months

VI. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

REVISION HISTORY

   Effective Date: 12/14/2021

S6030 – Identity and Authentication                                              Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
