---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-secret-key-cryptography-cc
title: Secret Key Cryptography
doc_type: standard
citation: 'Security Domain Compliance Component: Secret Key Cryptography'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-CryptoSecretKeyCryptography041304ARCapp.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 2f107c4400e1b0a9a64e9ea7cfca0c59e37e69f1a1c5fe23f212884e64e1ff74
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

# Secret Key Cryptography (Security Domain Compliance Component: Secret Key Cryptography)

## At a glance

Row 'Secret Key Cryptography' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/secret-key-cryptography-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 4/13/04. The index lists it as an approved standard.

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
Name                   Secret Key Cryptography
                       Secret Key Cryptography, also known as Symmetric Key, is a cryptographic
Description            method where a single key is shared between the sender and recipient, or is
                       implemented by a single user.
Rationale              Secret Key Cryptography enables confidentiality and integrity.
                           •    Secret Key Cryptography is generally faster than Public Key
                                Cryptography because it has a higher rate of data throughput and uses
                                shorter keys, and is most often used for encrypting data.
                       Notes:
                          • Secret key distribution is prone to interception and/or disclosure, which
                              can lead to impersonation and/or unauthorized disclosure or modification
                              of the data.
Benefits                  • Secret Key management is more difficult than Public Key because the
                              keys must be changed frequently, and there are many more keys to be
                              managed.
                          • Secret key encryption does not support strong authentication and non-
                              repudiation because both parties share the same key. Therefore, it is
                              possible for one party to create a message with the shared secret key
                              and falsely claim it had been sent by the other party.
                          • Streaming cipher algorithms (such as RC4) are susceptible to
                              compromise and are not recommended.
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
                                •    There are two algorithms suitable for Secret Key Cryptography:
                                        o Triple Data Encryption Standard (3DES)
State the Guideline, Standard           o Advanced Encryption Standard (AES)
or Legislation                  •    Approved key length for Secret Key shall be at least:
                                        o 168-bits for 3DES
                                        o 192-bits for AES

                               (All found at www.csrc.nist.gov)
                               NIST Special Publication 800-12, An Introduction to Computer Security:
                                   The NIST Handbook (Oct 1997)
Document Source Reference #    NIST SP 800-21, Guideline for Implementing Cryptography in the
                                   Federal Government (Nov 1999)
                               NIST Federal Information Processing Standards (FIPS) 197, Advanced
                                   Encryption Standard (AES) (Nov 2001)
                                             Standard Organization
Name                           NIST                                Website        www.csrc.nist.gov
Contact Information            inquiries@nist.gov
                                                  Government Body
                               National Institute of
                               Standards and Technology
                                                                                  www.csrc.nist.gov/publications/
Name                           (NIST), Computer                    Website
                                                                                  fips/index.html
                               Security Resource Center
                               (CSRC)
Contact Information            inquiries@nist.gov
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
List all Keywords              AES, 3DES, RC4, symmetric key, block cipher, stream cipher, algorithm
                                      C
                                      COOM
                                         MPPO
                                            ONNEEN
                                                 NTT C
                                                     CLLA
                                                        ASSSSIIFFIIC
                                                                   CAATTIIO
                                                                          ONN
Provide the Classification       Emerging                Current                Twilight         Sunset
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
Provide the Current Status)      In Development          Under Review           Approved         Rejected
                                                   A
                                                   AUUD
                                                      DIITT TTRRA
                                                                AIILL
Creation Date                  04/13/2004                   Date Accepted / Rejected       4/13/04
     Reason for Rejection
Last Date Reviewed                                          Last Date Updated
     Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
