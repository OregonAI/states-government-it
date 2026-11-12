---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-digital-signature-cc
title: Digital Signature
doc_type: standard
citation: 'Security Domain Compliance Component: Digital Signature'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-DigitalSignatures.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: f3978a7e7d676d25c4ed58faa1a5f71511ff426a4c04bc3b0b70b84e422333d9
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

# Digital Signature (Security Domain Compliance Component: Digital Signature)

## At a glance

Row 'Digital Signature' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/digital-signature-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status both Under Review and Approved marked, with Date Approved / Rejected 04/13/2004. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                     COMPLIANCE COMPONENT

                                                       DEFINITION
Name                  Digital Signature
                      The digital signature is based on Public Key Infrastructure (PKI) and is a result of a cryptographic
                      operation that guarantees signer authenticity, data integrity and non-repudiation of signed documents.
Description           The digital signature cannot be copied, tampered or altered. In addition, because they are based on
                      standard PKI technology, digital signatures made w ithin one application can be validated by others
                      using the same applications.
                      The purpose of a digital signature is to provide a means for an entity to bind its identity to
Rationale
                      data, and to detect unauthorized modifications to data.
                      • Digital signatures eliminate the need for transmitting passwords for authentication,
                          which reduces the threat of their compromise
                      • Using a private key to generate digital signatures for authentication prevents an attacker
                          from using the same information to masquerade as another entity and authenticate
                          repeatedly.
Benefits
                      • Digital signatures provide security for electronic mail, electronic funds transfer (EFT),
                          electronic data interchange (EDI), software distribution, data storage, and other
                          applications that require data integrity assurance and data origin authentication.
                      • Digital signatures provide a cost savings by eliminating the need to print and store hard
                          copies.

                                       ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name         Security
Specify the Discipline Name     Technical Controls
Specify the Technology Area
                                Cryptography
Name
Specify the Product
Component Name

                                           COMPLIANCE COMPONENT TYPE
Document the Compliance
                                Guideline
Component Type
Component Sub-type

                                                 COMPLIANCE DETAIL
                                •  There are three algorithms suitable for digital signature generation and
                                   verification:
                                        o Digital Signature Algorithm (DSA)
                                        o Rivest-Shamir-Adleman, a reversible Digital Signature Algorithm
State the Guideline, Standard                (RSA)
or Legislation                          o Elliptic Curve Digital Signature Algorithm (ECDSA)
                                • Digital signatures require a Public Key Infrastructure (PKI)
                                • Users must guard against the unauthorized acquisition of their private keys,
                                   because the security of a digital signature system is dependent on maintaining
                                   the confidentiality of users' private keys
                                NIST SP 800-135 Rev. 1, Recommendation for Existing
Document Source Reference #
                                Application-Specific Key Derivation Functions

                                                 Compliance Sources
                                National Institute of                             www.csrc.nist.gov/publications/
                                Standards and Technology                          fips/index.html
Name                            (NIST), Computer                   Website        http://csrc.nist.gov/publications/nistp
                                Security Resource Center                          ubs/800-135-rev1/sp800-135-
                                (CSRC)                                            rev1.pdf
Contact Information             inquiries@nist.gov
Name                                                               Website
Contact Information

                                                        KEYWORDS
                                Public key, private key, PKI, DSA, RSA, ECDSA, authenticate, integrity, electronic
List Keywords
                                funds transfer (EFT), electronic data interchange (EDI), Cryptography

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight           Sunset
     Sunset Date

                                           COMPONENT SUB-CLASSIFICATION
Sub-Classification           Date                         Additional Sub-Classification Information
    Technology Watch
    Variance
    Conditional Use

                                     Rationale for Component Classification
Document the Rationale for
Component Classification
                                                     Migration Strategy
Document the Migration
Strategy
                                               Impact Position Statement
Document the Position
Statement on Impact

                                                     CURRENT STATUS
Provide the Current Status          In Development            Under Review               Approved          Rejected

                                                        AUDIT TRAIL
Creation Date                   04/13/2004                    Date Approved / Rejected     04/13/2004
     Reason for Rejection
Last Date Reviewed              02/26/2015                    Last Date Updated            7/15/2015
     Reason for Update          Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
