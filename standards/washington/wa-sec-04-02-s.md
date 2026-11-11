---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-sec-04-02-s
title: Media Sanitization and Disposal Standard
doc_type: standard
citation: WaTech Standard SEC-04-02-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2024-08/SEC-04-02-S%20Media%20Sanitization%20and%20Disposal%20Standard.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 94edbb9031ccb411d6b65e17d8e4628b757cb0b58b73f0d50130ae0672bca4af
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

# Media Sanitization and Disposal Standard (WaTech Standard SEC-04-02-S)

## At a glance

Item of the WaTech policy library, chapter '4. IT Security' (listed as type Standards). Listed at https://watech.wa.gov/policies/media-sanitization-and-disposal-standard.

## Full text

SEC-04-02-S                                                                                                    Replaces:
State CIO Adopted: June 8, 2023                                                           IT Security Policy 141.10 (8.3)
TSB Approved: June 8, 2023                                                                          December 11, 2017
Sunset Review: June 8, 2026

           MEDIA SANITIZATION AND DISPOSAL STANDARD
See Also:
RCW 43.105.054 WaTech Governance.
RCW 43.105.020 (22) “State agency”.
RCW 43.105.052 Powers and duties of agency—Application to higher education, legislature, and judiciary.
RCW 52.105.450 Office of Cybersecurity

    1. Agencies must establish formal storage media sanitization and disposal
       procedures to render the stored data unusable, whether the storage media is
       reused or destroyed. At a minimum, agencies must:

            a. Ensure that users and custodians of information are aware of its sensitivity
                and the basic requirements for media sanitization and secure disposal in
                accordance with applicable standards and policies. This includes but is not
                limited to hard drives, solid state drives, removable drives, mobile devices,
                scanners, copiers, printers, paper copies, and pictures.

           b. Ensure staff responsible for data disposal are trained in records retention
               requirements and to perform and attest to media sanitization functions.
               Agencies may use service providers for destruction purposes provided that
               the information remains secure until the destruction is completed. The
               service providers must follow this standard. Agencies must ensure that
               maintenance or contractual agreements are in place and are sufficient in
               protecting the confidentiality of the system media and information
               commensurate with the information classification standards.

            c. Ensure that media sanitization and disposal documentation is protected
                against unauthorized access.

            d. Ensure media containing information is protected against unauthorized
                access, misuse, or corruption from the time it is removed from operational
                status to the time it is sanitized or disposed, whether within the agency or
                outside the agency’s physical boundaries.

    2. Agencies must select from three types of sanitization methods: clear, purge, and
       physical destruction. For more detail refer to Appendix A of NIST 800-88.

                                                                                                                   1

   The following table depicts the three types of sanitization methods and the
   impact of each method.
  Sanitization
    Method                 Appropriate Use                          Description
 Clear            If the media will be reused and      Clearing information is a level of
                  will not be leaving the entity’s     media sanitization that would
                  control.                             protect the confidentiality of
                                                       information. Simple deletion of
                                                       items would not suffice for clearing.
                                                       Clearing must not allow information
                                                       to be retrieved by data, disk, or file
                                                       recovery utilities.

 Purge            If the media will be reused and      Protects confidentiality of
                  leaving the entity’s control.        information against an attack
                                                       through either degaussing or a
                                                       three-pass wiping procedure
                                                       compliant with NIST 800-88.

 Physical         If the media will not be reused at   Intent is to destroy the media.
 Destruction      all.                                 Physical destruction may be
                                                       accomplished by shredding,
                                                       pulverization or other means that
                                                       ensure the media can never be re-
                                                       used. Disposal of physically
                                                       destroyed media must be
                                                       conducted in accordance with the
                                                       Responsible Recycling (R2)
                                                       standard, the e-Stewards Standard,
                                                       or some other environmentally
                                                       responsible way.

3. Agencies must work with the information owner to select the sanitization method
   based on the categorization of the data stored on that media. See SEC-08-01-S
   Data Classification Standard.
         a. Category 1 – Public Information
                 i. If this media will be reused and will not leave agency control, this
                    media must be cleared.
                 ii. If this media will be reused and will leave agency control, this
                     media must be purged.
         b. Category 2 – Sensitive Information
                 i. If this media will be reused and will not leave agency control, this
                    media must be cleared.

                                                                                                2

                ii. If this media will be reused and will leave agency control, this
                    media must be purged.
               iii. If this media will not be reused, it must be destroyed.
         c. Category 3 – Confidential Information
                i. If this media will be reused and will not leave agency control, the
                   media can be cleared.
                ii. If this media will be reused and will leave agency control, the
                    media must be purged.
               iii. If this media will not be reused, it must be destroyed.
         d. Category 4 – Confidential Information Requiring Special Handling
                i. If this media will be reused and will not leave agency control, the
                   media can be cleared.
                ii. If this media will be reused and will leave agency control, the
                    media must be sanitized per the special handling requirements
                    commensurate with category 4 data.
               iii. If this media will not be reused, it must be destroyed.

4. Agencies must maintain records that document all media disposal activities and
   protect them from unauthorized access. Records for disposed media must
   include:

      a. Information about the media (type, serial number, other unique identifiers).

      b. The category of data contained on the media.

      c. The destination of the media (if known).

      d. The date the media was sanitized.

      e. The person performing the activity.

      f. The method used to render all data unusable (e.g. software tool used or
          physical destruction of the media).

      g. The signature of the person responsible for ensuring that all data on the
          storage media has been rendered unusable.

5. Agencies must test at least 10% of its sanitized media to assure that proper
   protection is maintained.

                                                                                         3

REFERENCES

  1.  Definition of Terms Used in WaTech Policies and Reports.
  2.  NIST 800-88 Guidelines for Media Sanitization
  3.  State Government Records Retention Schedules - WA State Archives - WA
      Secretary of State
  4. Definition of Terms Used in OCIO Policies
  5. Responsible Recycling (R2) standard
  6. What's the e-Stewards Standard? - e-Stewards
  7. SEC-08-01-S Data Classification Standard
  8. NIST Cybersecurity Framework Mapping:
  • Protect.Data Security-3 (PR.DS-3): Assets are formally managed throughout
     removal, transfers, and disposition.
  • Protect.Information Protection Processes and Procedures-6 (PR.IP-6): Data is
     destroyed according to policy.

CONTACT INFORMATION

  •    For questions about this policy, please email the WaTech Policy Mailbox.

                                                                                   4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
