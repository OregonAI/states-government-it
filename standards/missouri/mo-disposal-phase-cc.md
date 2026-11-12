---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-disposal-phase-cc
title: Disposal Phase
doc_type: standard
citation: 'Security Domain Compliance Component: Disposal Phase'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-System-Life-Cycle-Disposal-Phase.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 7ef1e5b75d7a575164f69797dfcee870a896b4861d21e80e484492b22c57815b
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

# Disposal Phase (Security Domain Compliance Component: Disposal Phase)

## At a glance

Row 'Disposal Phase' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/disposal-phase-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Under Review, not Approved, with Date Approved / Rejected 02/13/2025. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                       COMPLIANCE COMPONENT

                                                             DEFINITION
Name                   Disposal Phase
                       The disposal phase ensures the appropriate sanitization of agency information. Sanitization
Description            is the process used to remove data from information systems and media such that there is
                       reasonable assurance that it cannot be retrieved or reconstructed.
                       The disposal phase is essential to prevent the inadvertent release of information and/or
Rationale
                       software.
                            • Protects sensitive information from disclosure.
Benefits
                              •   Adheres to copyright, statutory, and regulatory requirements.

                                         ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name            Security
Specify the Discipline Name        Management Controls
Specify the Technology Area
                                   System Life Cycle Security
Name
Specify the Product
Component Name

                                                  COMPLIANCE COMPONENT TYPE
Document the Compliance
                                   Guideline
Component Type
Component Sub-type

                                                COMPLIANCE DETAIL
                                       1. Types of Media
                                              •     Hard Copy Media are physical representations of information, most
                                                    often associated with paper printouts and can be disposed of by either
                                                    incineration or shredding (provided the shredded material is of
                                                    appropriate size according to agency requirements).
                                              •     Electronic media includes, but is not limited to, the following:
                                                        o   Hard disk drives
                                                        o   Solid state drives
State the Guideline, Standard                           o   USB drives
or Legislation                                          o   Fax machines
                                                        o   Printers
                                                        o   Scanners
                                                        o   Mobile devices (cellphones, tablets, etc.)
                                                        o   Memory cards

                                              •     Official electronic records shall be properly archived or disposed using
                                                    agency approved methods.
                                              •     Obsolete, surplus or decommissioned media containing agency data
                                                    shall be overwritten, degaussed or destroyed.

   •   A record shall be kept of who, when, and how sanitization or disposal
       actions were implemented on all electronic media and the final
       disposition of such media shall be maintained within the agency for an
       appropriate length of time.
   •   If the sanitization status of electronic media is unknown, it shall be
       considered not to have been overwritten, degaussed or destroyed.
   •   The information owner shall be responsible for backing up any data to
       be retained before allowing the media to be disposed.
2. Types of Sanitization - Clear, Purge, and Destroy are actions that can be
   taken to sanitize media. The categories of sanitization are defined as
   follows:
   •   Clear applies logical techniques to sanitize data in all user-
       addressable storage locations for protection against simple non-
       invasive data recovery techniques; typically applied through the
       standard Read and Write commands to the storage device, such as by
       rewriting with a new value or using a menu option to reset the device
       to the factory state (where rewriting is not supported).
   •   Purge applies physical or logical techniques that render Target Data
       recovery infeasible using state of the art laboratory techniques.
   •   Destroy renders Target Data recovery infeasible using state of the art
       laboratory techniques and results in the subsequent inability to use the
       media for storage of data.

3. Overwriting Electronic Media

   •   Overwriting electronic media should only be used if destroying or
       degaussing is deemed impractical by appropriate authorities.
   •   If damaged electronic media inhibits the overwriting process, the
       media shall be physically destroyed or degaussed.
   •   Overwriting software shall provide the capability to:
           o   Purge all data or information, including the O/S, from the
               physical or logical drives.
           o   Overwrite all sectors, blocks, tracks, and slack or unused
               space on the entire medium.
           o   Individually wipe RAID controlled hard drives.
           o   Verify that all data has been removed from the entire
               electronic media.
           o   Provide the user with validation that the procedure was
               completed properly.

   •   Overwriting software that merely reformats or repartitions a hard drive
       is not acceptable.
   •   The overwriting process shall be performed at least three times before
       verifying the media is sanitized.
4. Destroying Damaged Electronic Media
   • Electronic media may be physically destroyed by one of the following
      methods:
       o   Disintegrate, pulverize, melt, incinerate or shred the media so that
           it cannot be re-used as a functioning device.
5. Degaussing Electronic Media

                                         •     The degausser shall be rated sufficient for the media.
                                         •     Shielding materials may be removed from the hard drive and magnetic
                                               platters may be removed from the hard drive housing before
                                               degaussing.
                                         •     Individuals performing the degaussing function shall be properly
                                               trained.
                                This document will be reviewed annually or as needed.
     Document Source            NIST SP 800-88 Guidelines for Media Sanitization, Rev. 1
     Reference #                (www.csrc.nist.gov/publications/nistpubs);
                                                  Compliance Sources
                                National Institute of
                                Standards and Technology                           http://csrc.nist.gov/
Name                                                                Website
                                (NIST), Computer Security
                                Resource Center (CSRC)
Contact Information             inquiries@nist.gov
Name                                                                Website
Contact Information

                                                     KEYWORDS
                                Wipe, erase, clean, expunge, obliterate, purge, surplus, confidential, sanitize,
List Keywords
                                shred, degauss

                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight          Sunset
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
Provide the Current Status          In Development            Under Review               Approved          Rejected

                                                       AUDIT TRAIL
Creation Date                   07/22/2004                    Date Approved / Rejected     02/13/2025

    Reason for Rejection
Last Date Reviewed         01/28/2025   Last Date Updated   02/13/2025
    Reason for Update      Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
