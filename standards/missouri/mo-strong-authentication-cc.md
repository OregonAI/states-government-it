---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-strong-authentication-cc
title: Strong Authentication
doc_type: standard
citation: 'Security Domain Compliance Component: Strong Authentication'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-StrongAuthentication092705ARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: f10d0b6b9e260192e3042a551812cb4bc02e7d332941188dbba8e16015de68dc
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

# Strong Authentication (Security Domain Compliance Component: Strong Authentication)

## At a glance

Row 'Strong Authentication' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/strong-authentication-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with no Date Approved / Rejected printed. The index lists it as an approved standard.

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
Name                   Strong Authentication
                       Strong Authentication is the requirement to use multiple factors to verify the
Description            identity of a user accessing networks and/or applications, as opposed to the
                       typical method which requires only one factor of authentication.
                       Strong authentication provides additional assurance that the user is who they say
Rationale
                       they are and the data they send to you is authentic.
                       Strong authentication counters the weaknesses inherent in typical, one-factor
                       authentication methods because they are:
                          •   Harder to duplicate,
                          •   Cannot be re-generated,
Benefits                  •   Cannot be easily guessed,
                          •   Cannot be re-used, or are
                          •   Physically stored independently from the other factor of authentication,
                              thereby deterring simultaneous use by an unauthorized user.

                       Strong authentication increases the feasibility of using single sign-on (SSO).
                                   A
                                   ASSSSO
                                        OCCIIA
                                             ATTEED
                                                  DAARRC
                                                       CHHIITTEEC
                                                                CTTU
                                                                   URREE LLEEVVEELLSS
List the Domain
                       Security
Name
List the Discipline
                       Technical Controls
Name
List the Technology
Area Name
List Product
Component Name
                                    C
                                    COOM
                                       MPPLLIIA
                                              ANNC
                                                 CEE C
                                                     COOM
                                                        MPPO
                                                           ONNEEN
                                                                NTT TTYYPPEE
Document the
Compliance             Guideline
Component Type
Component Sub-
type
                                            C
                                            COOM
                                               MPPLLIIA
                                                      ANNC
                                                         CEE D
                                                             DEETTA
                                                                  AIILL
                       The three factors of authentication for users are:

                          1. Something they know, for example:
                             • Password
State the Guideline,
                             • Personal Identification Number (PIN)
Standard or
Legislation                  • Personal Question (such as your favorite color)
                          2. Something they have, for example:
                             • Token
                             • Certificate
                             • Smartcard

                            • Magnetic Stripe/Credit/Debit Card
                            • One-time Pad
                            • Proximity Card
                         3. Something they are, for example:
                            • Fingerprint
                            • Retinal Scan
                            • Voice Scan
                            • Facial Scan

                      Strong Authentication must use two different factors from the list above. For
                      example, one password they know plus one token they have. It must not use two
                      of the same type of factor, for instance, a password and a personal question.

                      Cookies are not an acceptable authentication factor.

                      Strong Authentication must be implemented when:
                         • Users access the private network from public connections, such as the
                             Internet
                         • Applications perform transactions involving CONFIDENTIAL or financial
                             information via the Internet
                         • Administrators remotely manage security devices
                         • Password policies cannot be enforced

                      Strong Authentication should be implemented when:
                         • CONFIDENTIAL information is accessed within the internal network
                         • Administrators remotely manage servers and network devices

                      Strong Authentication methods must lock the user account, and require
                      administrator intervention or a waiting period of at least 30 minutes, after a
                      minimum of 5 failed authentication attempts.
Document Source
                      N/A
Reference #
                                       Standard Organization
Name                                                     Website
Contact Information
                                           Government Body
                      National Institute of Standards and                             http://csrc.nist.gov/
Name                  Technology (NIST), Computer Security         Website
                      Resource Center (CSRC)
Contact Information   inquiries@nist.gov
Name                                                               Website
Contact Information
                                                K
                                                KEEYYW
                                                     WOOR
                                                        RDDS
                                                           S
                      Password, One-Time, Token, Certificate, Bio-Metric, Smartcard, advanced
List all Keywords
                      authentication, two-factor, Single Sign On, SSO, cookies, transaction, PIN
                                    C
                                    COOM
                                       MPPO
                                          ONNEEN
                                               NTT C
                                                   CLLA
                                                      ASSS
                                                         SIIFFIIC
                                                                CAATTIIO
                                                                       ONN
Provide the
                        Emerging            Current           Twilight       Sunset
Classification

                            Rationale for Component Classification
Document the
Rationale for
Component
Classification
                                     Conditional Use Restrictions
Document the
Conditional Use
Restrictions
                                            Migration Strategy
Document the
Migration Strategy
                                         Impact Position Statement
Document the
Position Statement
on Impact
                                             C
                                             CUUR
                                                RRREEN
                                                     NTT S
                                                         STTA
                                                            ATTU
                                                               USS
Provide the Current
                        In Development       Under Review       Approved         Rejected
Status)
                                                A
                                                AUUD
                                                   DIITT TTR
                                                           RAAIILL
                                                                     Date Accepted /
Creation Date         05/12/05                                                           09-27-2005
                                                                     Rejected
    Reason for
Rejection
Last Date Reviewed                                                   Last Date Updated
    Reason for
Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
