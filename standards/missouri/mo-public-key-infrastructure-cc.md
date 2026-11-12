---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-public-key-infrastructure-cc
title: Public Key Infrastructure
doc_type: standard
citation: 'Security Domain Compliance Component: Public Key Infrastructure'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-CryptoPublicKeyInfrastructure041304ARCapp.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 75a23e52c5615247c5f4a0c47fe615331e5584e914e2aad0cf68b89d76f0f03a
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

# Public Key Infrastructure (Security Domain Compliance Component: Public Key Infrastructure)

## At a glance

Row 'Public Key Infrastructure' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/public-key-infrastructure-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 4/13/04. The index lists it as an approved standard.

## Full text

                                             C
                                             Coom
                                                mpplliiaannccee C
                                                                Coom
                                                                   mppoonneenntt

                                                    D
                                                    DEEFFIIN
                                                           NIITTIIO
                                                                  ONN
Name                   Public Key Infrastructure (PKI)
                       Public Key Infrastructure (PKI) is a cryptography method that provides a
                       mathematical identification of a specific resource. In public key systems, there
Description
                       are two encryption keys: a public key and a private key. The public key is
                       different from the private key, but they are mathematically related.
Rationale              PKI enables confidentiality, authentication, digital signatures, and integrity.
                           •    Provides a means of identification and authentication
                           •    Provides non-repudiation (entity integrity)
                           •    Provides confidentiality
                           •    Provides data integrity
Benefits
                           •    Provides the means to read encrypted documents through key recovery
                           •    PKI is best suited for a multi-user environment
                           •    Greater ease of distributing encryption keys

                                    A
                                    ASSSSO
                                         OCCIIA
                                              ATTEED
                                                   DAARRC
                                                        CHHIITTEEC
                                                                 CTTU
                                                                    URREE LLEEVVEELLSS
List the Domain Name            Security
List the Discipline Name        Technical Controls
List the Technology Area Name   Cryptography
List Product Component Name
                                      C
                                      COOM
                                         MPPLLIIA
                                                ANNC
                                                   CEE C
                                                       COOM
                                                          MPPO
                                                             ONNEEN
                                                                  NTT TTYYPPEE
Document the Compliance
                                Guideline
Component Type
Component Sub-type
                                              C
                                              COOM
                                                 MPPLLIIA
                                                        ANNC
                                                           CEE D
                                                               DEETTA
                                                                    AIILL
                                •    Functional elements of a public key infrastructure should include:
                                        1. A Certification Authority (CA) which confirms the identities of
                                            parties sending and receiving communications. The CA also
                                            issues and processes Certificate Revocation Lists (CRLs),
                                            which are lists of certificates that have been revoked.
                                        2. Registration Authorities which are entities trusted by the CA
                                            to register or vouch for the identity of users to a CA.
State the Guideline, Standard           3. Repositories which are databases of active digital certificates
or Legislation                              for a PKI system.
                                        4. Archives which store and protect sufficient information to
                                            determine if an inactive digital signature on a document
                                            should be trusted.
                                        5. PKI users.
                                •    Certificates must adhere to the IETF (Internet Engineering Task
                                     Force) X.509 standard.

                               •   Each entity in an authentication exchange must use an approved
                                   digital signature algorithm to generate and/or verify digital
                                   signatures (see the MAEA Digital Signatures Compliance
                                   Component).

                               •   There are two algorithms suitable for asymmetric key certificate
                                   generation and verification:
                                        o     Rivest-Shamir-Adleman, a reversible Digital Signature
                                              Algorithm (RSA).
                                        o     Elliptic Curve Digital Signature Algorithm (ECDSA).
                               •   Encryption key length shall be at least 512-bits for RSA and ECDSA.

                               •   Public key certificates must be generated prior to the authentication
                                   exchange.

                               •   Public key certificates must be readily accessible to any entity that
                                   wishes to authenticate another entity.

                               •   Organizations may either purchase a PKI product and become their
                                   own Certification Authority or subscribe to a PKI service.

                               •   A private key must remain accessible only to its owner.

Document Source Reference #
                                               Standard Organization
                               NIST SP 800-12 and 800-                        http://csrc.nist.gov/publication
Name                                                              Website
                               32                                             s/
Contact Information
                                                 Government Body
                               National Institute of
                               Standards and Technology
                                                                              http://csrc.nist.gov
Name                           (NIST), Computer                   Website
                               Security Resource Center
                               (CSRC)
Contact Information            inquiries@nist.gov
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
List all Keywords              Asymmetric, Digital Signature, RSA, ECDSA, elliptic curve, key length
                                      C
                                      COOM
                                         MPPO
                                            ONNEEN
                                                 NTT C
                                                     CLLA
                                                        ASSSSIIFFIIC
                                                                   CAATTIIO
                                                                          ONN
Provide the Classification         Emerging             Current             Twilight      Sunset
                                   Rationale for Component Classification
Document the Rationale for
Component Classification
                                            Conditional Use Restrictions
Document the Conditional Use
Restrictions

                                                 Migration Strategy
Document the Migration
Strategy
                                         Impact Position Statement
Document the Position
Statement on Impact
                                            C
                                            CUURRRREEN
                                                     NTT SSTTA
                                                             ATTU
                                                                USS
Provide the Current Status)     In Development          Under Review           Approved     Rejected
                                                  A
                                                  AUUD
                                                     DIITT TTRRA
                                                               AIILL
Creation Date                 04/13/2004                   Date Accepted / Rejected   4/13/04
    Reason for Rejection
Last Date Reviewed                                         Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
