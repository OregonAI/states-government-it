---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-cryptography-cc
title: Cryptography
doc_type: standard
citation: 'Security Domain Compliance Component: Cryptography'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Cryptography.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: e9bb1fb387bc67b3e23931685e13849999bca5e07a67c2c7265abc9318c69ec9
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

# Cryptography (Security Domain Compliance Component: Cryptography)

## At a glance

Row 'Cryptography' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/cryptography-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Under Review, not Approved, with Date Approved / Rejected 02/13/2025. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                       COMPLIANCE COMPONENT

                                                           DEFINITION
Name                   Cryptography
                       Cryptography is the discipline that embodies the principles, means, and methods for the
Description            transformation of data in order to hide their semantic content, prevent their unauthorized
                       use, or prevent their undetected modification.
Rationale              Cryptography provides the necessary security features to protect unsecure data.
                              •   Client authentication
                              •   Data integrity
                              •   Confidentiality
Benefits
                              •   User authentication
                              •   Non-repudiation

                                               ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name            Security
Specify the Discipline Name        Technology Controls
Specify the Technology Area
                                   Cryptography
Name

                                                  COMPLIANCE COMPONENT TYPE
Document the Compliance
                                   Guideline
Component Type
Component Sub-type

                                                    COMPLIANCE DETAIL
                                   The most commonly used encryption protocol is Transport Layer Security
                                   (TLS). HTTPS is Hypertext Transport Protocol integrated with TLS. TLS is
                                   sometimes referred to as TLS/SSL (Transport Layer Security/ Secure Socket
                                   Layer). Encryption should follow the latest standards in NIST and FIPS. Currently
                                   those standards are:

                                       •      When transmitting sensitive or critical information over the web, users shall
                                              use encryption with at least:
                                                  o Advanced Encryption Standard (AES) 256-bit encryption
                                                  o Secure Hash Algorithim-2 (SHA-2)
State the Guideline, Standard
                                                  o Transport Layer Security 1.2 (TLS 1.2)
or Legislation
                                                          • TLS 1.3 would be preferred if available.

                                       •      Any ciphers used should be compatible with minimum TLS 1.2
                                                 o TLS 1.3 would be preferred if available.

                                       •      Cryptography should be used for:
                                                 o Email - Email is inherently unsecure. Cryptography allows the
                                                     user to add a set of security features to email.
                                                 o Stored Data - provides confidentiality and integrity of the data. It
                                                     enables secure labeling, storing, and transferring of data.

                                               o   VPN - A public network such as the Internet accessed by a
                                                   telephone line, cable or DSL, is inherently not secure. A VPN
                                                   enables two or more parties to communicate securely across a
                                                   public network by creating a private connection, or “tunnel,”
                                                   between them.
                                               o   Web Servers - Provides the necessary security features to protect
                                                   the data on web servers that are unsecure.
                                               o   Wireless Communication - There is a need for secure wireless
                                                   access to networks where physical cables are not available and/or
                                                   feasible.
                                               o   Cloud – Authentication to cloud-provided systems and data.

                                This document shall be reviewed annually or as needed.

                                NIST Special Publications 800-52, Rev. 2 – Guidelines for the Selection,
                                Configuration and use of Transport Layer Security (TLS) Implementations;
                                IRS Publication 1075;
Document Source Reference #     NIST SP 800-53, Rev. 5 - Security and Privacy Controls for Information Systems
                                and Organizations
                                FIPS 140-3 – Security Requirements for Cryptographic Modules

                                                   Compliance Sources
                                National Institute of
                                Standards and Technology
Name                            (NIST), Computer                   Website      http://csrc.nist.gov
                                Security Resource Center
                                (CSRC), IRS
Contact Information             inquiries@nist.gov
Name                                                               Website
Contact Information

                                                       KEYWORDS
                                TLS, HTTPS, FTP, SMTP, AES, Digital Signature, SHA-2, SSL, Cryptography,
List Keywords
                                Web Server

                                           COMPONENT CLASSIFICATION
Provide the Classification          Emerging                 Current                Twilight             Sunset
     Sunset Date

                                        COMPONENT SUB-CLASSIFICATION
 Sub-Classification          Date                         Additional Sub-Classification Information
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
Provide the Current Status      In Development          Under Review               Approved       Rejected

                                                   AUDIT TRAIL
Creation Date                07/06/2023                 Date Approved / Rejected     02/13/2025
    Reason for Rejection
Last Date Reviewed           01/28/2025                 Last Date Updated            02/13/2025
    Reason for Update        Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
