---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-message-authentication-cc
title: Message Authentication
doc_type: standard
citation: 'Security Domain Compliance Component: Message Authentication'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-MessageAuthentication03-23-07ARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: e38f8ef97843290b1a26af9eafdc6c91e2c80501f32efd5ae47af1eb37769f15
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

# Message Authentication (Security Domain Compliance Component: Message Authentication)

## At a glance

Row 'Message Authentication' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/message-authentication-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 03/23/2007. The index lists it as an approved standard.

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
Name                   Message Authentication
                       Message authentication is a technique used to detect unauthorized changes to,
Description            or corruption of, the contents of a transmitted electronic message.
                       Provides a means to validate the integrity of information transmitted over or
Rationale              stored in an unsecured environment.
                       Provides:
                           •    Non-Repudiation
Benefits                                 o   When the system provides data integrity a receiver can be
                                             sure of both the sender's identity and that he is receiving the
                                             data that sender meant to send.

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
List the Technology Area Name   Identification and Authentication
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
                                            CCOOM
                                                MPPLLIIA
                                                       ANNC
                                                          CEE D
                                                              DEETTA
                                                                   AIILL
                                Message authentication must be considered for applications where there is a
                                security requirement to protect the integrity of the message content such as:

                                    •     Electronic funds transfer
                                    •     Specifications
                                    •     Contracts
                                    •     Proposals
State the Guideline, Standard
or Legislation                      •     Other similar electronic data exchanges of high importance

                                An assessment of security risks should be carried out to determine if
                                message authentication is required and to identify the most appropriate
                                method of message authentication.

                                Recommended methods of message authentication

                               Non-repudiation
                               Non-repudiation should be used where it is necessary to resolve disputes of
                               authenticity such as dispute involving the use of a signature on an electronic
                               contract or payment.

                               Digital Signatures
                               Digital signatures provide a means of protecting the authenticity and
                               integrity of electronic documents.
                                   • They can be used in electronic commerce where there is a need to
                                       verify who signed an electronic document and check whether the
                                       contents of the signed document have been changed. (See Digital
                                       Signatures CC).

                               These services are based on the use of encryption and digital signature
                               techniques (see Cryptography TA).

                               Note: Message authentication is not designed to protect the contents of a
                               message from unauthorized disclosure.
Document Source Reference #
                                            Standard Organization
                               SP 800-63; FIPS 201,
                               FIPS 198, SP 800-61, ISO
Name                                                            Website
                               17799-2000 (E)

Contact Information
                                              Government Body
                               National Institute of
                               Standards and Technology
                                                                            http://csrc.nist.gov/
Name                           (NIST), Computer                 Website
                               Security Resource Center
                               (CSRC)
Contact Information            inquiries@nist.gov
                                                 KKEEYYW
                                                       WOORRD
                                                            DSS
                               Encryption, non-repudiation, digital signature, cryptography, validate,
List all Keywords
                               integrity.
                                     C
                                     COOM
                                        MPPO
                                           ONNEEN
                                                NTT C
                                                    CLLA
                                                       ASSSSIIFFIIC
                                                                  CAATTIIO
                                                                         ONN
Provide the Classification       Emerging             Current             Twilight      Sunset
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
Creation Date                 01/04/2007                   Date Accepted / Rejected   03/23/2007
    Reason for Rejection
Last Date Reviewed                                         Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
