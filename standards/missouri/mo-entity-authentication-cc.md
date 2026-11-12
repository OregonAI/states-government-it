---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-entity-authentication-cc
title: Entity Authentication
doc_type: standard
citation: 'Security Domain Compliance Component: Entity Authentication'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-EntityAuthentication03-23-07ARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 388c85798f3b5842753ebdb33165baa2d478f2e15032b77b07959ce5ed2f549c
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

# Entity Authentication (Security Domain Compliance Component: Entity Authentication)

## At a glance

Row 'Entity Authentication' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/entity-authentication-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 03/23/2007. The index lists it as an approved standard.

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
Name                   Entity Authentication
                       Entity Authentication is the process by which an agent in a distributed system
Description            gains confidence in the identity of a communication partner.
                       Ensure that only authenticated entities have the capability to be connected to an
                       agency network.
Rationale
                       To address several threats, including but not limited to masquerade, password
                       compromise, replay attacks and the signing of pre-defined data.
                       •   A means to ensure users are who they say they are
                       •   Verify the user who attempts to perform functions in a system is in fact the
Benefits                   user who is authorized to do so
                       •   Provides a measure of non-repudiation

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
                                              C
                                              COOM
                                                 MPPLLIIA
                                                        ANNC
                                                           CEE D
                                                               DEETTA
                                                                    AIILL
                                User identification and authentication should have a unique identifier
                                (user ID) for their personal and sole use so that activities can
                                subsequently be traced to the responsible individual.

                                User IDs and passwords should not be shared. (See Password Controls
                                CC).

State the Guideline, Standard      •     There are various authentication procedures, which can be used
or Legislation                           to substantiate the claimed identity of a user.
                                                o User IDs with passwords are a very common way to
                                                   provide authentication
                                                o The same can also be achieved with cryptographic
                                                   means and authentication protocols
                                                o Objects such as tokens or smart cards that users
                                                   possess
                                                o Biometric authentication technologies that use the

                                                  unique characteristics or attributes of an individual
                               A combination of technologies and mechanisms securely linked will
                               result in stronger authentication
Document Source Reference #
                                             Standard Organization
                               FIPS PUB 196                                       http://csrc.nist.gov/publication
Name                                                               Website
                                                                                  s/fips/fips196/fips196.pdf
Contact Information
                                                  Government Body
                               National Institute of
                               Standards and Technology
                                                                                  http://csrc.nist.gov/
Name                           (NIST), Computer                    Website
                               Security Resource Center
                               (CSRC)
Contact Information            inquiries@nist.gov
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
List all Keywords              Password, user ID, identification, authorization, access.
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
Creation Date                  01/11/2007                   Date Accepted / Rejected       03/23/2007
     Reason for Rejection
Last Date Reviewed                                          Last Date Updated
     Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
