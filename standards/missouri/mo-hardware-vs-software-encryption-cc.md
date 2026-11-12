---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-hardware-vs-software-encryption-cc
title: Hardware vs Software Encryption
doc_type: standard
citation: 'Security Domain Compliance Component: Hardware vs Software Encryption'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-CryptoHardwarevsSoftwareEncryption041304ARCapp.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: d5e6d01dc3bdc748824f7cfaa3703d1d543b7237530154332c0ad8179626691b
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

# Hardware vs Software Encryption (Security Domain Compliance Component: Hardware vs Software Encryption)

## At a glance

Row 'Hardware vs Software Encryption' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/hardware-vs-software-encryption-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 4/13/04. The index lists it as an approved standard.

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
Name                   Hardware vs. Software Encryption
                       Encryption processing (coding or decoding) on the host and/or client system can
Description            take place by one of two methods: (1) software using shared processor, or (2)
                       dedicated or auxiliary hardware.
                       A decision on where encryption should take place is needed before deploying an
                       application that requires encrypted transport or storage. Cost, performance,
Rationale
                       support, and perceived success of the business application will hinge on the
                       analysis used to determine encryption processing capacity needs and methods.
                          • A suitable analysis on encryption method (hardware vs. software) can
                              avert scalability issues. Scalability problems often lead to costly
                              hardware, software, or infrastructure solutions to remedy the problem.
Benefits                   •    Knowledge of the business application and target audience help staff
                                determine scalability needs and the supporting technology base.
                           •    Each approach (hardware vs. software) has unique benefits with relation
                                to cost and support when deployed properly.
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
                                General Encryption Statements
                                    •     Encrypted transmissions are processing-intensive functions on
                                          the client and/or server endpoints
                                    •     Encrypted storage is a processing-intensive function on the
                                          system side issuing the “save” for the data in question.
State the Guideline, Standard       •     The processing load increases with greater key length and more
or Legislation                            complex algorithm.
                                Software-based Encryption
                                    •     Software-based encryption is normally performed using existing
                                          processing capacity in the client/host system.
                                    •     Software encryption shares processing resources with all other
                                          programs/processes on the system, which could impact

                                     performance of all other functions of the system.
                                 •   Scalability problems may necessitate additional processors in the
                                     system, or multiple systems to meet scalability needs.
                                 •   In small application environments (a single workstation or a
                                     server with few concurrent users), software-based encryption is
                                     normally the most cost-effective approach.
                              Distribution
                                 •   The information protected with encryption shall be transmitted
                                     over a different communication channel than the keys used to
                                     govern the encryption process.
                                 •   Private and secret encryption keys transmitted over
                                     communication lines shall be sent in encrypted form with one of
                                     the following key exchange algorithms:
                                     •   RSA
                                     •   Elliptic Curve
                                     •   Diffie-Hellman
                              Hardware-based Encryption

                                 •   Hardware encryption is normally performed by dedicated
                                     hardware in the client/host system.
                                 •   Hardware encryption has minimal impact on other
                                     programs/processes because it uses separate processing
                                     resources.
                                 •   Scalability is normally achieved by adding more components to
                                     an existing device.
                                 •   Hardware-based encryption normally provides much greater
                                     throughput capacity and speed in large-scale environments.
                                 •   In medium and larger environments, hardware-based encryption
                                     is normally the most scalable, cost-effective solution.

                              www.cisco.com
Document Source Reference #
                              www.microsoft.com

                              Search criteria: hardware-based encryption
                                          Standard Organization
Name                                                      Website
Contact Information
                                             Government Body
                              National Institute of
                              Standards and Technology                http://csrc.nist.gov/
                              (NIST), Computer
Name                          Security Resource Center    Website     http://www.bxa.doc.gov/encry
                              (CSRC); U.S. Department                 ption/
                              of Commerce, Bureau of
                              Industry and Security

Contact Information            inquiries@nist.gov
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
List all Keywords              Encryption, scalability
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
