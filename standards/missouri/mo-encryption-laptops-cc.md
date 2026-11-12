---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-encryption-laptops-cc
title: Encryption for Laptops
doc_type: standard
citation: 'Security Domain Compliance Component: Encryption for Laptops'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-EncryptionForLaptops09-28-2011ARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: b5d4767e7cd39c141c6a28c11cf39bf77e88fe16fefda8ad1d3318258f7bf6a2
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

# Encryption for Laptops (Security Domain Compliance Component: Encryption for Laptops)

## At a glance

Row 'Encryption for Laptops' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/encryption-laptops-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 09/28/2011. The index lists it as an approved standard.

## Full text

                                        COMPLIANCE COMPONENT

                                                        DEFINITION
Name                  Encryption for Laptops
                      Encryption for Laptops is securing laptop hard drives to ensure the confidentiality, integrity
Description
                      and availability of both data and applications.
                      In case of theft, loss or unauthorized use of the laptop, encryption prevents the compromise
                      of the agency data and network.
Rationale
                      The specific intent is to compensate for the lack of physical security controls when the
                      laptop is removed from the agency location or control.
                      Encrypted laptops:
                             Prevent compromise of agency information
Benefits
                             Safeguard the agency and state network from unauthorized activity
                             Meets the agency’s statutory and fiduciary responsibilities

                                          ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name            Security
Specify the Discipline Name        Technical Controls
Specify the Technology Area
                                   Remote Access Controls
Name
Specify the Product
Component Name

                                              COMPLIANCE COMPONENT TYPE
Document the Compliance
                                   Guideline
Component Type
Component Sub-type

                                                 COMPLIANCE DETAIL
                                The encryption methodology must have all of the following features, at
                                a minimum:
                                       Operational on a local, single machine without connectivity to the
                                        agency’s network.
                                       Boot-time authentication that requires the user to authenticate
                                        when the computer is started.
                                       Full-disk encryption that requires all drives and data are fully
                                        encrypted.
                                       Recovery after authentication failure, which is a challenge-
                                        response facility that permits the user, with the assistance of a
                                        system administrator, to regain access to a protected machine.
                                             o    Note that the challenge-response process is sensitive and
                                                  should be handled accordingly.
State the Guideline, Standard          Encrypts upon hibernation, requiring the user to re-authenticate
or Legislation                          when restarting the machine.
                                       User can not turn encryption off.
                                       All data encryption is automatic and transparent to the user.
                                       Encryption overhead is minimal with little or no noticeable impact
                                        on system performance.

                                The following features should be included:
                                       Two-factor authentication.
                                       Software deployment tools automatically install and configure for
                                        systems based on your security policies.
                                       Ability to encrypt any type of drive attached to the laptop.
                                            o    Ability to access encrypted drive when attached to other
                                                 devices.

Document Source Reference #

                                                 Compliance Sources
                                National Institute of
                                Standards and Technology
                                (NIST), Computer Security
                                Resource Center (CSRC)                          http://csrc.nist.gov/
Name                                                              Website
                                Special Publication 800-111,
                                Guide to Storage Encryption
                                Technologies for End User
                                Devices, November 2007
Contact Information             inquiries@nist.gov
                                Laptop Encryption ITPS -
Name                                                              Website       www.oa.mo.gov
                                001
Contact Information

                                                     KEYWORDS
List Keywords                   Password, authentication, two-factor, biometric, token, full disk.

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight       Sunset
     Sunset Date

                                           COMPONENT SUB-CLASSIFICATION
 Sub-Classification          Date                          Additional Sub-Classification Information
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
Provide the Current Status          In Development            Under Review               Approved       Rejected

                                                       AUDIT TRAIL
Creation Date                   11/28/2006                    Date Approved / Rejected     09/28/2011
     Reason for Rejection
Last Date Reviewed              01/27/2011                    Last Date Updated            01/27/2011
     Reason for Update          Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
