---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-nys-s13-003
title: Sanitization Secure Disposal
doc_type: standard
citation: NYS ITS Standard NYS-S13-003
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/sanitization-secure-disposal
source_format: pdf
retrieved: '2026-11-11'
source_sha256: dcce752b83350aa5ef9ecbefbf70b8ea08f01f5014770d6bc9f0cf77bf3a7416
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Sanitization Secure Disposal (NYS ITS Standard NYS-S13-003)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Cybersecurity, Statewide Policies' on the listing. The listing prints original publication 10/18/2013 and last modified 06/10/2025.

## Full text

                                                   State Capitol P.O. Box 2062
                                                     Albany, NY 12220-0062
                                                         www.its.ny.gov

               New York State
                                                                   No: NYS-S13-003
      Information Technology Standard

                         IT Standard:                              Updated: 06/10/2025

                                                                   Issued By: NYS Office of Information
           Sanitization/Secure                                     Technology Services
                Disposal                                           Owner: Chief Information Security Office

    1.0 Purpose and Benefits
       Information systems capture, process, and store data and other information using a wide
       variety of media, including paper. This information is not only located on the intended storage
       media but also on devices used to create, process, or transmit this information. These types
       of media may require special consideration around their sanitization and/or secure disposal
       to mitigate the risk of unauthorized disclosure of information and to ensure its confidentiality .

    2.0 Authority
       Section 103(10) of the State Technology Law provides the Office of Information Technology
       Services (ITS) with the authority to establish statewide technology policies, including
       technology and security standards. Section 2 of Executive Order No. 117 1, established
       January 2002, provides the State Chief Information Officer with the authority to oversee,
       direct and coordinate the establishment of information technology policies, protocols, and
       standards for State government, including hardware, software, security, and business re-
       engineering. Details regarding this authority can be found in NYS ITS Policy, NYS-P08-002
       Authority to Establish State Enterprise Information Technology (IT) Policy, Standards and
       Guidelines.

    3.0 Scope

1
 All references to Executive Order 117 refer to that which was originally issued by Governor George E. Pataki on January 28,
2002 and continued by Executive Order 5 issued by Governor Eliot Spitzer on January 1, 2007, Executive Order 9 issued by
Governor David A. Patterson on June 18, 2008, Executive Order 2 issued by Governor Andrew M. Cuomo on January 1, 2011 and
Executive Order 6 issued by Governor Kathy Hochul on October 8, 2021.
       NYS-S1 3 -00 3                                                                                    Page 1 of 27

   This standard applies to all “State Entities” (SE), defined as “State Government” in
   Executive Order 117 or “State Agencies” as defined in Section 101 of the State
   Technology Law. This includes employees of the SE and ITS and all third parties (such
   as local governments, consultants, vendors, and contractors) that use or access any
   Information Technology (IT) Resource for which the SE or ITS has administrativ e
   responsibility, including systems managed or hosted by third parties on behalf of the SE
   or ITS. While an SE may adopt a different standard, it must include the requirements set
   forth in this one. Where a conflict exists between this standard and an SE’s standard, the
   more restrictive policy will take precedence.

   This standard covers all media containing SE information regardless of the classification
   of the information stored or its format or location, including that which is held by third
   parties on behalf of the SE. Electronic media may be contained in or be a part of personal
   or laptop computers, printers, scanners, fax machines, mobile devices, copiers, or other
   devices which may allow temporary or permanent storage of information.

4.0 Information Statement

   NYS-P03-002 Information Security Policy requires that information be properly managed
   from its creation, through authorized use, to proper disposal. To that end, SEs must
   ensure that users and custodians of information are aware of its sensitivity and the
   requirements for media sanitization and secure disposal. The three methods of
   sanitization are Clear, Purge, and Destroy (See Table 1 below). The method of
   sanitization and/or secure disposal is related to an information’s classification and SE’s
   are reminded that they must classify information according to the NYS-S14-002
   Information Classification Standard. Before a SE takes an action to initiate the
   sanitization or secure disposal of a device, it should first consult with the SE Legal
   Counsel to ensure all records retention and legal preservation obligations are met.

   The SE must ensure that its entire workforce, including property management and
   custodial staff, are made aware of the media sanitization and secure disposal process to
   establish proper accountability for all information. Further, the SE must ensure that
   confidential material is destroyed only by authorized and trained personnel, whether in-
   house or contracted, using methods outlined in this standard.

   The SE may use contractors to sanitize media provided that the information remains
   secure until the sanitization is completed. The contractors must follow this standard. The
   SE must ensure that maintenance or contractual agreements are in place and are
   sufficient to protect the confidentiality of the system media and information commensurate
   with the information’s classification.
   Methods of Media Sanitization

   Table 1 below gives a general explanation of the options for sanitization. Recommended
   sanitization techniques for specific types of media are outlined in Appendix A - Minimum
   Sanitization Recommendations.

   NYS-S1 3 -00 3                                                               Page 2 of 27

 Method Description
 Clear  One method to sanitize media is to use software or hardware products to
        overwrite user-addressable storage space on the media with non-sensitiv e
        data, using the standard read and write commands for the device. This
        process may include overwriting not only the logical storage location of a
        file(s) (e.g., file allocation table) but also should include all user-addressable
        locations. The security goal of the overwriting process is to replace Target
        Data with non-sensitive data. Overwriting cannot be used for media that are
        damaged or not rewriteable and may not address all areas of the device
        where sensitive data may be retained. The media type and size may also
        influence whether overwriting is a suitable sanitization method. For example,
        flash memory-based storage devices may contain spare cells and perform
        wear levelling, making it infeasible for a user to sanitize all previous data
        using this approach because the device may not support directly addressing
        all areas where sensitive data has been stored using the native read and
        write interface.

                 The Clear operation may vary contextually for media other than dedicated
                 storage devices, where the device (such as a basic cell phone or a piece of
                 office equipment) only provides the ability to return the device to factory state
                 (typically by simply deleting the file pointers) and does not directly support
                 the ability to rewrite or apply media-specific techniques to the non-volatile
                 storage contents. Where rewriting is not supported, manufacturer resets and
                 procedures that do not include rewriting might be the only option to Clear
                 the device and associated media. These still meet the definition for Clear as
                 long as the device interface available to the user does not facilitate retrieval
                 of the Cleared data.

 Purge           Some methods of purging (which vary by media and must be applied with
                 considerations described further throughout this document) include
                 overwrite, block erase, and Cryptographic Erase, through the use of
                 dedicated, standardized device sanitize commands that apply media-
                 specific techniques to bypass the abstraction inherent in typical read and
                 write commands.

                 Destructive techniques also render the device Purged when effectively
                 applied to the appropriate media type, including incineration, shredding,
                 disintegrating, degaussing, and pulverizing. The common benefit across all
                 these approaches is assurance that the data is infeasible to recover using
                 state of the art laboratory techniques. However, bending, cutting, and the
                 use of some emergency procedures (such as using a firearm to shoot a hole
                 through a storage device) may only damage the media as portions of the
                 media may remain undamaged and therefore accessible using advanced
                 laboratory techniques.

NYS-S1 3 -00 3                                                                          Page 3 of 27

                       Degaussing renders a legacy magnetic device purged when the strength of
                       the degausser is carefully matched to the media coercivity. Coercivity may
                       be difficult to determine based only on information provided on the label.
                       Therefore, refer to the device manufacturer for coercivity details.
                       Degaussing should never be solely relied upon for flash memory-based
                       storage devices or for magnetic storage devices that also contain non-
                       volatile non-magnetic storage. Degaussing renders many types of devices
                       unusable (and in those cases, degaussing is also a destruction technique).

       Destroy There are many different types, techniques, and procedures for media
               destruction. While some techniques may render the Target Data infeasible
               to retrieve through the device interface and unable to be used for
               subsequent storage of data, the device is not considered destroyed unless
               Target Data retrieval is infeasible using state of the art laboratory
               techniques.

                           •   Disintegrate, Pulverize, Melt, and Incinerate. These sanitization
                               methods are designed to completely destroy the media. They are
                               typically carried out at an outsourced metal destruction or licensed
                               incineration facility with the specific capabilities to perform these
                               activities effectively, securely, and safely.
                           •   Shred. Paper shredders can be used to destroy flexible media such
                               as diskettes once the media are physically removed from their outer
                               containers. The shred size of the refuse should be small enough that
                               there is reasonable assurance in proportion to the data
                               confidentiality that the data cannot be reconstructed. To make
                               reconstructing the data even more difficult, the shredded material
                               can be mixed with non-sensitive material of the same type (e.g.,
                               shredded paper or shredded flexible media).

                 The application of destructive techniques may be the only option when the
                 media fails and other Clear or Purge techniques cannot be effectively
                 applied to the media, or when the verification of Clear or Purge methods fails
                 (for known or unknown reasons).
Table 1. Sanitization Methods (from NIST 800-88, Rev. 1, Guidelines for Media Sanitization)
Sanitization Decision Process

      The sanitization decision process starts with the classification of the information, as
      defined in the NYS-S14-002 Information Classification Standard. Once the classification
      category is evaluated, the SE can determine the appropriate sanitization method of
      specific media in accordance with Appendix A. The Information Owner must determine
      the type of sanitization to be used, and such decision must be approved by the SE
      Sanitization methods not specified in Appendix A may be suitable as long as they are
      verified and found satisfactory by the SE.

      Disposal without sanitization should be considered only if information disclosure would
      have no impact on organizational mission, would not result in damage to organizational
      assets, would not result in financial loss or harm to any individuals, and would not violate
      any federal or state laws, rules, regulations, or standards.
      NYS-S1 3 -00 3                                                                      Page 4 of 27

The classification of the information, along with internal environmental factors, should
drive the decisions on how to deal with the media as shown in Figure 1 below. The key is
to first consider the security categorization of the information and then apply additional
factors (see Figure 1 below) including but not limited to: whether the media be processed
in a controlled area and whether a sanitization process should be conducted within the
organization or outsourced.

Figure 1: Sanitization and Disposition Decision Flow
(from NIST 800-88, Rev. 1, Guidelines for Media Sanitization)

The cost versus benefit of a sanitization process should also be understood prior to a final
decision. SEs can always increase the level of sanitization applied if that is reasonable
and indicated by an assessment of the existing risk. For example, even though Clear or
Purge may be the recommended solution, it may be more cost-effective (considering
training, tracking, and verification, etc.) to destroy media rather than use one of the other
options. SEs cannot decrease the level of sanitization required. If the SE has not identified
the classification of information on media, the disposition must follow the sanitization
method for the highest information classification rating.
Control of Media

A factor influencing an SE sanitization decision is who has control and access to the
media. This aspect must be considered before media leaves organizational control.
Media control may be transferred when media are returned from a leasing agreement or
are being donated or resold to be reused outside the organization. The following are
examples of media control:
NYS-S1 3 -00 3                                                                  Page 5 of 27

Under SE Control:

     •    Media being turned over for maintenance is still considered under SE control if
          contractual agreements are in place with the SE and the contractor that specifically
          provide for the protection of confidential information.
     • Maintenance being performed on an SE’s site, under the SE’s supervision, by a
          maintenance provider is also considered under the control of the SE.

Not Under SE Control:

     •    Media that are being exchanged for warranty, cost rebate, or other purposes and
          where the specific media will not be returned to the SE are considered to be out of
          SE control.

     •    Important Note: As data and assets of various types and classifications are
          established or migrated into the Cloud infrastructures of third-party hosting
          partners, this standard will continue to apply. If data classified as “High” is to be
          stored with a Cloud Solution Provider (CSP), the physical data storage must be
          destroyed after use, and the SE would need to ensure that the destruction was
          completed by the CSP, and that proof of destruction was provided at that time.
Reuse of Media

SEs should consider the cost versus benefit of reuse. It may be more cost-effective
(considering training, tracking, and verification, etc.) to destroy media rather than use one
of the other sanitization options.

Validation

SEs must test a representative sampling of media for proper sanitization to ensure that
proper protection is maintained.

Verification of Equipment
If the SE is using sanitization tools (e.g., a degausser), the SE must have procedures to
ensure that the tools are operating effectively.
Verification of Personnel Competencies

SEs must ensure that equipment operators are properly trained and competent to perform
sanitization functions.

Document

SEs must maintain a record of their sanitization to document what media were sanitized,
when and how they were sanitized, and the final disposition of the media.

NYS-S1 3 -00 3                                                                   Page 6 of 27

5.0 Compliance
   This standard shall take effect upon publication. Compliance is required with all enterprise
   policies and standards. ITS may amend its policies and standards at any time; compliance
   with amended policies and standards is required.

   If compliance with this standard is not feasible or technically possible, or if deviation from
   this policy is necessary to support a business function, State Entities shall request an
   exception through the Chief Information Security Office exception process.

6.0 Definitions of Key Terms

   Except for terms defined in this policy, all terms shall have the meanings found in
   http://www.its.ny.gov/glossary.

7.0 Contact Information

           Submit all inquiries and requests for future enhancements to the policy owner
                                                  at:

                               Chief Information Security Office
                                    Reference: NYS-S13-003
                       NYS Office of Information Technology Services
                                   31 British American Blvd.,
                                       Latham, NY 12110
                                     Telephone: (518) 242-
                                           5200 Email:
                                       CISO@its.ny.gov
    Statewide technology policies, standards, and guidelines may be found at the following
                  website: its.ny.gov/policies

8.0 Revision History
   This standard document should be reviewed consistent with the requirements set forth in
   ITS-P24-003 Process for Establishing Information Technology Policies, Standards, and
   Guidelines.

       Date            Description of Change                             Reviewer
       10/18/2013      Original Standard Release; replaces ITS S06-      Thomas Smith, Chief
                       006 Media Disposal and Sanitization               Information Security
                                                                         Officer

   NYS-S1 3 -00 3                                                                   Page 7 of 27

       10/17/2014   Added reference to NYS-P03-002 Information     Deborah A.
                    Security Policy                                Snyder, Chief
                                                                   Information
                                                                   Security Officer
       06/26/2017   Updated to reference most recent version of    Deborah A. Snyder,
                    the NIST guidelines, contact information and   Chief Information
                    rebranded.                                     Security Officer
       02/07/2020   Update to Authority, Scope and Contact         Karen Sorady, Acting
                    Information                                    Chief Information
                                                                   Security Officer
       05/20/2021   Updated Scope language                         Karen Sorady, Chief
                                                                   Information Security
                                                                   Officer
       11/23/2021   Update to guidance regarding Media             Karen Sorady, Chief
                    Sanitization requirements for Cloud Services   Information Security
                                                                   Officer
       06/10/2025   Added Appendix A, which covers media           Chris DeSain, Chief
                    sanitization methods for various types of      Information Security
                    media, and other minor wording changes         Officer

9.0 Related Documents

   NIST 800-88, Rev. 1, Guidelines for Media Sanitization
   NYS-S14-002 Information Classification Standard
   NYS-P03-002 Information Security Policy

   NYS-S1 3 -00 3                                                           Page 8 of 27

Appendix A – Minimum Sanitization Recommendations
The technique for sanitizing media varies based upon the type of media being sanitized.
The types of media are listed below with the recommended sanitization technique(s) as
found in NIST 800-88, Rev. 1, Guidelines for Media Sanitization, Appendix A - Minimum
Sanitization Recommendations. Some sanitization procedures feature additional optional
methods. The choice regarding whether to apply the optional components depends on
the level of classification of the data and assurance of correct implementation of the non-
optional portion of the sanitization procedure.

 Hard Copy Storage Sanitization
 Paper and Microforms
 Clear               N/A, see Destroy.
 Purge               N/A, see Destroy.
 Destroy             Destroy paper using cross-cut shredders which produce
                     particles that are 1 mm x 5 mm (0.04 in. x 0.2 in.) in size (or
                     smaller) or pulverize/disintegrate paper materials using
                     disintegrator devices equipped with a 3/32 in. (2.4 mm) security
                     screen. Destroy microforms (microfilm, microfiche, or other
                     reduced image photo negatives) by burning.
 Notes               When material is burned, residue must be reduced to white ash.

 Networking Devices Sanitization
 Routers and Switches
 Clear               Perform a full manufacturer’s reset to reset the router or switch
                     back to its factory default settings.
 Purge               See Destroy. Most routers and switches only offer capabilities
                     to Clear (and not Purge) the data contents. A router or switch
                     may offer Purge capabilities, but these capabilities are specific
                     to the hardware and firmware of the device and should be
                     applied with caution. Refer to the device manufacturer to
                     identify whether the device has a Purge capability that applies
                     media-dependent techniques (such as rewriting or block
                     erasing) to ensure that data recovery is infeasible, and that the
                     device does not simply remove the file pointers.
 Destroy             Shred, Disintegrate, Pulverize, or Incinerate by burning the
                     device in a licensed incinerator.
 Notes               For both Clear and (if applicable) Purge, refer to the
                     manufacturer for additional information on the proper
                     Sanitization procedure. Network Devices may contain
                     removable storage. The removable media must be removed
                     and sanitized using media-specific techniques.

NYS-S1 3 -00 3                                                                Page 9 of 27

 Mobile Device Sanitization
 (If a device has removable storage – first check for encryption and unencrypt if so –
 then remove the removable storage prior to sanitization)
 Apple iPhone and iPad
 (Current generation and future iPhones and iPads)
 Clear               Select the full sanitize option (typically in the ‘Settings > General
                     > Reset > Erase All Content and Settings’ menu). (The
                     sanitization operation should take only minutes as
                     Cryptographic Erase is supported. This assumes that
                     encryption is on, and that all data has been encrypted.)
                     Sanitization performed via a remote wipe should be treated as
                     a Clear operation, and it is not possible to verify the sanitization
                     results.
 Purge               Select the full sanitize option (typically in the ‘Settings > General
                     > Reset > Erase All Content and Settings’ menu). (The
                     sanitization operation should take only minutes with
                     Cryptographic Erase being supported. This assumes that
                     encryption is on, and that all data has been encrypted.)
 Destroy             Shred, Disintegrate, Pulverize, or Incinerate by burning the
                     device in a licensed incinerator.
 Notes               Following the Clear/Purge operation, manually navigate to
                     multiple areas of the device (such as browser history, files,
                     photos, etc.) to verify that no personal information has been
                     retained on the device. Before sanitizing the device, ensure that
                     the data is backed up to a safe place. Current iPhones have
                     hardware encryption – turned on by default.
 Blackberry
 (Back up data on device before sanitization)
 Clear               BB OS 7.x/6.x - Select Options > Security Options > Security
                     Wipe, making sure to select all subcategories of data types for
                     sanitization. Then type “blackberry” in the text field, then click
                     on “Wipe” (“Wipe Data” in BB OS 6.x) BB OS 10.x (Decrypt
                     media card before continuing) Select Settings, Security and
                     Privacy, Security Wipe. Type “blackberry” in the text field, then
                     click on “Delete Data”. The sanitization operation may take as
                     long as several hours depending on the media size. Sanitization
                     performed via a remote wipe should be treated as a Clear
                     operation, and it is not possible to verify the sanitization results.
 Purge               BB OS 7.x/6.x - Select Options > Security > Security Wipe, then
                     make sure to select all subcategories of data types for
                     sanitization. Then type “blackberry” in the text field, then click
                     on “Wipe” (“Wipe Data” in BB OS 6.x). For BB OS 10.x Select
NYS-S1 3 -00 3                                                                   Page 10 of 27

                    Settings> Security and Privacy>Security Wipe. Type
                    “blackberry” in the text field, then click on “Delete Data”. The
                    sanitization operation may take as long as several hours
                    depending on the media size.
 Destroy            Shred, Disintegrate, Pulverize, or Incinerate by burning the
                    device in a licensed incinerator.
 Notes              Following the Clear/Purge operation, manually navigate to
                    multiple areas of the device (such as browser history, files,
                    photos, etc.) to verify that no personal information has been
                    retained on the device. Centralized management (BES) allows
                    for device encryption. Refer to the manufacturer for additional
                    information on the proper sanitization procedure, and for details
                    about implementation differences between device versions and
                    OS versions. Proper initial configuration using guides such as
                    the Defense Information Systems Agency (DISA) Security
                    Technical Implementation Guides (STIGs) helps ensure that
                    the level of data protection and sanitization assurance is as
                    robust as possible. If the device contains removable storage
                    media, ensure that the media is sanitized using appropriate
                    media dependent procedures.
 Devices running the Google Android OS
 (Connect to power before starting encryption)
 Clear              Perform a factory reset through the device’s settings menu. For
                    example, on Samsung Galaxy S5 running Android 4.4.2, select
                    settings, then, under User and Backup, select Backup and
                    reset, then select Factory data reset. For other versions of
                    Android and other mobile phone devices, refer to the user
                    manual. Sanitization performed via a remote wipe should be
                    treated as a Clear operation, and it is not possible to verify the
                    sanitization results.
 Purge              The capabilities of Android devices are determined by device
                    manufacturers and contractors. As such, the level of assurance
                    provided by the factory data reset option may depend on
                    architectural and implementation details of a particular device.
                    Devices seeking to use a factory data reset to purge media
                    should use the eMMC Secure Erase or Secure Trim command,
                    or some other equivalent method (which may depend on the
                    device’s storage media). Some versions of Android support
                    encryption and may support Cryptographic Erase. Refer to the
                    device manufacturer (or contractor, if applicable) to identify
                    whether the device has a Purge capability that applies media-
                    dependent sanitization techniques or Cryptographic Erase to
                    ensure that data recovery is infeasible, and that the device does
                    not simply remove the file pointers.
 Destroy            Shred, Disintegrate, Pulverize, or Incinerate by burning the
                    device in a licensed incinerator.
NYS-S1 3 -00 3                                                               Page 11 of 27

 Notes             Proper initial configuration using guides such as the DISA
                   STIGs helps ensure that the level of data protection and
                   sanitization assurance is as robust as possible. Following the
                   Clear or (if applicable) Purge operation, manually navigate to
                   multiple areas of the device (such as browser history, files,
                   photos, etc.) to verify that no personal information has been
                   retained on the device. When in doubt, check device manual or
                   call tech support. For both Clear and Purge, refer to the
                   manufacturer for additional information on the proper
                   sanitization procedure.
 Windows Phone OS 7.1/8/8.x
 (Centralized management may be needed for encryption)
 Clear             Select the Settings option (little gear symbol) from the live tile
                   or from the app list. On the “Settings” page, scroll to the bottom
                   of the page and select the “About” button. In the about page,
                   there will be a reset your phone button at the bottom of the
                   page. Click on this button to continue. Choose Yes when you
                   see the warning messages. Please note that after the process
                   is completed, all your personal content will disappear.
                   Sanitization performed via a remote wipe should be treated as
                   a Clear operation, and it is not possible to verify the sanitization
                   results.
 Purge             The capabilities of Windows Phone devices are determined by
                   device manufacturers and contractors. As such, the level of
                   assurance provided by the factory data reset option may
                   depend on architectural and implementation details of a
                   particular device. Devices seeking to use a factory data reset to
                   purge media should use the eMMC Secure Erase or Secure
                   Trim command, or some other equivalent method (which may
                   depend on the device’s storage media). In some environments,
                   Windows Phone devices may support encryption and may
                   support Cryptographic Erase. Refer to the device manufacturer
                   (or contractor, if applicable) to identify whether the device has
                   a Purge capability that applies media-dependent sanitization
                   techniques or Cryptographic Erase to ensure that data recovery
                   is infeasible, and that the device does not simply remove the
                   file pointers.
 Destroy           Shred, Disintegrate, Pulverize, or Incinerate by burning the
                   device in a licensed incinerator.
 Notes             Following the Clear/Purge operation, manually navigate to
                   multiple areas of the device (such as browser history, files,
                   photos, etc.) to verify that no personal information has been
                   retained on the device. Before sanitizing your device, ensure
                   that you back up your data to a safe location. Refer to the
                   manufacturer for proper sanitization procedure, and for details
                   about implementation differences between device versions and
NYS-S1 3 -00 3                                                                Page 12 of 27

                     OS versions. Proper initial configuration using guides such as
                     the DISA STIGs helps ensure that the level of data protection
                     and sanitization assurance is as robust as possible.
 All other mobile devices
 (This includes cell phones, smart phones, PDAs, tablets, and other devices not
 covered in the preceding mobile categories)
 Clear               Manually delete all information, then perform a full
                     manufacturer’s reset to reset the mobile device to factory state.
                     Sanitization performed via a remote wipe should be treated as
                     a Clear operation, and it is not possible to verify the sanitization
                     results.
 Purge               See Destroy. Many mobile devices only offer capabilities to
                     Clear (and not Purge) the data contents. A mobile device may
                     offer Purge capabilities, but these capabilities are specific to the
                     hardware and software of the device and should be applied with
                     caution. The device manufacturer should be referred to in order
                     to identify whether the device has a Purge capability that
                     applies media-dependent techniques (such as rewriting or
                     block erasing) or Cryptographic Erase to ensure that data
                     recovery is infeasible, and that the device does not simply
                     remove the file pointers.
 Destroy             Shred, Disintegrate, Pulverize, or Incinerate by burning the
                     device in a licensed incinerator.
 Notes               Following the Clear or (if applicable) Purge operation, manually
                     navigate to multiple areas of the device (such as call history,
                     browser history, files, photos, etc.) to verify that no personal
                     information has been retained on the device. For both Clear and
                     (if applicable) Purge, refer to the manufacturer for proper
                     sanitization procedure.

 Equipment Sanitization
 (This includes copy, print, fax, and multifunction machines)
 Office Equipment
 Clear               Perform a full manufacturer’s reset to reset the office equipment
                     to its factory default settings.
 Purge               See Destroy. Most office equipment only offers capabilities to
                     Clear (and not Purge) the data contents. Office equipment may
                     offer Purge capabilities, but these capabilities are specific to the
                     hardware and firmware of the device and should be applied with
                     caution. Refer to the device manufacturer to identify whether
                     the device has a Purge capability that applies media-dependent
                     techniques (such as rewriting or block erasing) or
                     Cryptographic Erase to ensure that data recovery is infeasible,
                     and that the device does not simply remove the file pointers.
NYS-S1 3 -00 3                                                                  Page 13 of 27

                     Office equipment may have removable storage media, and if
                     so, media-dependent sanitization techniques may be applied to
                     the associated storage device.
 Destroy             Shred, Disintegrate, Pulverize, or Incinerate by burning the
                     device in a licensed incinerator.
 Notes               For both Clear and (if applicable) Purge, manually navigate to
                     multiple areas of the device (such as stored fax numbers,
                     network configuration information, etc.) to verify that no
                     personal information has been retained on the device. For both
                     Clearing and (if applicable) Purge, the ink, toner, and
                     associated supplies (drum, fuser, etc.) should be removed and
                     destroyed or disposed of in accordance with applicable law,
                     environmental, and health considerations. Some of these
                     supplies may retain impressions of data printed by the machine
                     and therefore could pose a risk of data exposure and should be
                     handled accordingly. If the device is functional, one way to
                     reduce the associated risk is to print a blank page, then an all-
                     black page, then another blank page. For devices with
                     dedicated color components (such as cyan, magenta, and
                     yellow toners and related supplies), one page of each color
                     should also be printed between blank pages. The resulting
                     sheets should be handled at the confidentiality of the Office
                     Equipment (prior to sanitization). Note that these procedures do
                     not apply to supplies such as ink/toner on a one-time use roll,
                     as they are typically not used again and therefore will not be
                     addressed by sending additional pages through the equipment.
                     They will, however, still need to be removed and destroyed.
                     Office Equipment supplies may also pose health risks and
                     should be handled using appropriate procedures to minimize
                     exposure to the print components and toner. For both Clear and
                     (if applicable) Purge, refer to the manufacturer for additional
                     information on the proper sanitization procedure.

 Magnetic Media Sanitization
 Removable Magnetic Media (Floppy Disks and Magnetic Disks)
 (Magnetic Disks may be flexible or fixed)
 Clear               Overwrite media by using organizationally approved software
                     and perform verification on the overwritten data. The Clear
                     pattern should be at least a single write pass with a fixed data
                     value, such as all zeros. Multiple write passes or more complex
                     values may optionally be used.
 Purge               Degauss in an organizationally approved degausser rated at a
                     minimum for the media.
 Destroy             Incinerate floppy disks and diskettes by burning in a licensed
                     incinerator or Shred.
NYS-S1 3 -00 3                                                                Page 14 of 27

 Notes             Incinerate floppy disks and diskettes by burning in a licensed
                   incinerator or Shred.
                   Degaussing magnetic       disks   typically   renders   the   disk
                   permanently unusable.
 Reel and Cassette Format Magnetic Tapes
 Clear             Re-record (overwrite) all data on the tape using an
                   organizationally approved pattern, using a system with similar
                   characteristics to the one that originally recorded the data. For
                   example, overwrite previously recorded sensitive VHS format
                   video signals on a comparable VHS format recorder. All
                   portions of the magnetic tape should be overwritten one time
                   with known non-sensitive signals. Clearing a magnetic tape by
                   re-recording (overwriting) may be impractical for most
                   applications since the process occupies the tape transport for
                   excessive time periods.
 Purge             Degauss the magnetic tape in an organizationally approved
                   degausser rated at a minimum for the media.
 Destroy           Incinerate by burning the tapes in a licensed incinerator or
                   Shred.
 Notes             Preparatory steps for Destruction, such as removing the tape
                   from the reel or cassette prior to Destruction, are unnecessary.
                   However, segregation of components (tape and reels or
                   cassettes) may be necessary to comply with the requirements
                   of a Destruction facility or for recycling measures.
 ATA Hard Disk Drives
 (This includes PATA, SATA, eSATA, etc.)
 Clear             Overwrite media by using organizationally approved and
                   validated overwriting technologies/methods/tools. The Clear
                   pattern should be at least a single write pass with a fixed data
                   value, such as all zeros. Multiple write passes or more complex
                   values may optionally be used.
 Purge             1. Use one of the ATA Sanitize Device feature set commands,
                   if supported, to perform a Sanitize operation. One or both of the
                   following options may be available:
                       a. The overwrite EXT command. Apply one write pass of a
                   fixed pattern across the media surface. Some examples of fixed
                   patterns include all zeros or a pseudorandom pattern. A single
                   write pass should suffice to Purge the media. Optionally:
                   Instead of one write pass, use three total write passes of a
                   pseudorandom pattern, leveraging the invert option so that the
                   second write pass is the inverted version of the pattern
                   specified.
                      b. If the device supports encryption and the technical
                   specifications described in this document have been satisfied,
NYS-S1 3 -00 3                                                              Page 15 of 27

                 the Cryptographic Erase (also known as CRYPTO SCRAMBLE
                 EXT) command. Optionally: After Cryptographic Erase is
                 successfully applied to a device, use the overwrite command (if
                 supported) to write one pass of zeros or a pseudorandom
                 pattern across the media. If the overwrite command is not
                 supported, the Secure Erase or the Clear procedure could
                 alternatively be applied following Cryptographic Erase.
                 2. Use the ATA Security feature set’s SECURE ERASE UNIT
                 command, if support, in Enhanced Erase mode. The ATA
                 Sanitize Device feature set commands are preferred over the
                 over the ATA Security feature set SECURITY ERASE UNIT
                 command when supported by the ATA device.
                 3. Cryptographic Erase through the Trusted Computing Group
                 (TCG) Opal Security Subsystem Class (SSC) or Enterprise
                 SSC interface by issuing commands as necessary to cause all
                 MEKs to be changed (if the requirements described in this
                 document have been satisfied). Refer to the TCG and device
                 manufacturers for more information. Optionally: After
                 Cryptographic Erase is successfully applied to a device, use the
                 overwrite command (if supported) to write one pass of zeros or
                 a pseudorandom pattern across the media. If the overwrite
                 command is not supported, the Secure Erase or the Clear
                 procedure    could    alternatively  be     applied    following
                 Cryptographic Erase.
                 4. Degauss in an organizationally approved automatic
                 degausser or disassemble the hard disk drive and purge the
                 enclosed platters with an organizationally approved degaussing
                 wand.
 Destroy         Shred, Disintegrate, Pulverize, or Incinerate by burning the
                 device in a licensed incinerator.
 Notes           Verification must be performed for each technique within Clear
                 and Purge, except degaussing. The assurance provided by
                 degaussing depends on selecting an effective degausser,
                 applying it appropriately and periodically spot checking the
                 results to ensure it is working as expected.
                 When using the three pass ATA sanitize overwrite procedure
                 with the invert option, the verification process would simply
                 search for the original pattern (which would have been written
                 again during the third pass).
                 The storage device may support configuration capabilities that
                 artificially restrict the ability to access portions of the media as
                 defined in the ATA standard, such as a Host Protected Area
                 (HPA), Device Configuration Overlay (DCO), or Accessible Max
                 Address. Even when a dedicated sanitization command
                 addresses these areas, their presence may affect the ability to
                 reliably verify the effectiveness of the sanitization procedure if
NYS-S1 3 -00 3                                                              Page 16 of 27

                    left in place. Any configuration options limiting the ability to
                    access the entire addressable area of the storage media should
                    be reset prior to applying the sanitization technique. Recovery
                    data, such as an OEM-provided restoration image may have
                    been stored in this manner, and sanitization may therefore
                    impact the ability to recover the system unless reinstallation
                    media is also available.
                    When Cryptographic Erase is applied, verification must be
                    performed prior to additional sanitization techniques (if
                    applicable), such as a Clear or Purge technique applied
                    following Cryptographic Erase, to ensure that the cryptographic
                    operation completed successfully. A quick sampling verification
                    as described in NIST 800-88, Rev. 1, Guidelines for Media
                    Sanitization, Section 4.7, Verify Methods should also be
                    performed after any additional techniques are applied following
                    Cryptographic Erase.
                    Not all implementations of encryption are necessarily suitable
                    for reliance upon Cryptographic Erase as a Purge mechanism.
                    The decision regarding whether to use Cryptographic Erase
                    depends upon verification of attributes previously identified in
                    this guidance and in NIST 800-88, Rev.1, Guidelines for Media
                    Sanitization, Appendix D.
                    Given the variability in implementation of the ATA Security
                    feature set SECURITY ERASE UNIT command, use of this
                    command is not recommended without first consulting with the
                    manufacturer to verify that the storage device’s model-specific
                    implementation meets the needs of the organization.
                    This guidance applies to Legacy Magnetic media only, and it is
                    critical to verify the media type prior to sanitization. Note that
                    emerging media types, such as HAMR media or hybrid drives
                    may not be easily identifiable by the label. Refer to the
                    manufacturer for details about the media type in a storage
                    device.
                    Degaussing the media in a storage device typically renders the
                    device unusable.
 SCSI Hard Disk Drives
 (This includes Parallel SCSI, Serial Attached SCSI (SAS), Fibre Channel, USB
 Attached Storage (UAS), and SCSI Express Partial sanitization is not supported in
 this section)
 Clear              Overwrite media by using organizationally approved and
                    validated overwriting technologies/methods/tools. The Clear
                    procedure should consist of at least one pass of writes with a
                    fixed data value, such as all zeros. Multiple passes or more
                    complex values may optionally be used.
 Purge              1. Apply the SCSI SANITIZE command, if supported. One or

NYS-S1 3 -00 3                                                                Page 17 of 27

                 both of the following options may be available:
                     a. The OVERWRITE service action. Apply one write pass of
                 a fixed pattern across the media surface. Some examples of
                 fixed patterns include all zeros or a pseudorandom pattern. A
                 single write pass should suffice to Purge the media. Optionally:
                 Instead of one write pass, use three total write passes of a
                 pseudorandom pattern, leveraging the invert option so that the
                 second write pass is the inverted version of the pattern
                 specified.
                    b. If the device supports encryption, the CRYPTOGRAPHIC
                 ERASE service action. Optionally: After Cryptographic Erase is
                 successfully applied to a device, use the overwrite command (if
                 supported) to write one pass of zeros or a pseudorandom
                 pattern across the media. If the overwrite command is not
                 supported, the Clear procedure could alternatively be applied.
                 2. Cryptographic Erase through the TCG Opal SSC or
                 Enterprise SSC interface by issuing commands as necessary
                 to cause all MEKs to be changed. Refer to the TCG and vendors
                 shipping TCG Opal or Enterprise storage devices for more
                 information. Optionally: After Cryptographic Erase is
                 successfully applied to a device, use the overwrite command (if
                 supported) to write one pass of zeros or a pseudorandom
                 pattern across the media. If the overwrite command is not
                 supported, the Clear procedure could alternatively be applied.
                 3. Degauss in an organizationally approved automatic
                 degausser or disassemble the hard disk drive and purge the
                 enclosed platters with an organizationally approved degaussing
                 wand. The degausser/wand should be rated sufficient for the
                 media.
 Destroy         Shred, Disintegrate, Pulverize, or Incinerate by burning the
                 device in a licensed incinerator.
 Notes           Verification must be performed for each technique within Clear
                 and Purge as described in NIST 800-88, Rev. 1, Guidelines for
                 Media Sanitization, Section 4.7, Verify Methods, except
                 degaussing. The assurance provided by degaussing depends
                 on selecting an effective degausser, applying it appropriately
                 and periodically spot checking the results to ensure it is working
                 as expected.
                 When using the three pass SCSI sanitize overwrite procedure
                 with the invert (also known as complement) option, the
                 verification process would simply search for the original pattern
                 (which would have been written again during the third pass).
                 While it is widely accepted that one pass of overwriting should
                 be sufficient for Purging the data, the availability of a dedicated
                 command that incorporates the ability to invert the data pattern
                 allows an efficient and effective approach that mitigates any
NYS-S1 3 -00 3                                                             Page 18 of 27

                    residual risk associated with variations in implementations of
                    magnetic recording features across device manufacturers.
                    The storage device may support configuration capabilities that
                    artificially restrict the ability to access portions of the media,
                    such as “SCSI mode parameter block descriptor’s NUMBER OF
                    LOGICAL BLOCKS field (accessible with the SCSI MODE
                    SENSE and MODE SELECT commands”. Even when a
                    dedicated sanitization command addresses these areas, their
                    presence may affect the ability to reliably verify the
                    effectiveness of the sanitization procedure if left in place. Any
                    configuration options limiting the ability to access the entire
                    addressable area of the storage media should be reset prior to
                    applying the sanitization technique.
                    When Cryptographic Erase is applied, verification must be
                    performed prior to additional sanitization techniques (if
                    applicable), such as a Clear or Purge technique applied
                    following Cryptographic Erase, to ensure that the cryptographic
                    operation completed successfully. A quick sampling verification
                    as described in NIST 800-88, Rev. 1, Guidelines for Media
                    Sanitization, Section 4.7, Verify Methods should also be
                    performed after any additional techniques are applied following
                    Cryptographic Erase.
                    Not all implementations of encryption are necessarily suitable
                    for reliance upon Cryptographic Erase as a Purge mechanism.
                    The decision regarding whether to use Cryptographic Erase
                    depends upon verification of attributes previously identified in
                    this guidance and in NIST 800-88, Rev. 1, Guidelines for Media
                    Sanitization, Appendix D.
                    This guidance applies to Legacy Magnetic media only, and it is
                    critical to verify the media type prior to sanitization. Note that
                    emerging media types, such as HAMR media or hybrid drives
                    may not be easily identifiable by the label. Refer to the
                    manufacturer for details about the media type in a storage
                    device.
                    Degaussing the media in a storage device typically renders the
                    device unusable.

 Peripherally Attached Storage Sanitization
 External Locally Attached Hard Drives
 (This includes, USB, Firewire, etc. Treat eSATA as ATA Hard drive)
 Clear              Overwrite media by using organizationally approved and tested
                    overwriting technologies/methods/tools. The Clear pattern
                    should be at least a single pass with a fixed data value, such as
                    all zeros. Multiple passes or more complex values may
                    alternatively be used.
NYS-S1 3 -00 3                                                                Page 19 of 27

 Purge             The implementation of External Locally Attached Hard Drives
                   varies sufficiently across models and vendors that the issuance
                   of any specific command to the device may not reasonably and
                   consistently assure the desired sanitization result. When the
                   external drive bay contains an ATA or SCSI hard drive, if the
                   commands can be delivered natively to the device, the device
                   may be sanitized based on the associated media specific
                   guidance. However, the drive could be configured in a vendor-
                   specific manner that precludes sanitization when removed from
                   the enclosure. Additionally, if sanitization techniques are
                   applied, the hard drive may not work as expected when
                   reinstalled in the enclosure. Refer to the device manufacturer to
                   identify whether the device has a Purge capability that applies
                   media-dependent techniques (such as rewriting, block erasing,
                   Cryptographic Erase, etc.) to ensure that data recovery is
                   infeasible, and that the device does not simply remove the file
                   pointers.
 Destroy           Shred, Disintegrate, Pulverize, or Incinerate by burning the
                   device in a licensed incinerator.
 Notes             Verification as described in NIST 800-88, Rev. 1, Guidelines for
                   Media Sanitization, Section 4.7, Verify Methods must be
                   performed for each technique within Clear and Purge.
                   Some external locally attached hard drives, especially those
                   featuring security or encryption features, may also have hidden
                   storage areas that might not be addressed even when the drive
                   is removed from the enclosure. The device vendor may
                   leverage proprietary commands to interact with the security
                   subsystem. Please refer to the manufacturer to identify whether
                   any reserved areas exist on the media and whether any tools
                   are available to remove or sanitize them, if present.

 Optical Media Sanitization
 CD, DVD, BD
 Clear             N/A
 Purge             N/A
 Destroy           Destroy in order of recommendations:
                   1. Removing the information-bearing layers of CD media using
                   a commercial optical disk grinding device. Note that this applies
                   only to CD and not to DVD or BD media.
                   2. Incinerate optical disk media (reduce to ash) using a licensed
                   facility.
                   3. Use optical disk media shredders or disintegrator devices to
                   reduce to particles that have nominal edge dimensions of 0.5
                   mm and surface area of 0.25 mm2 or smaller.
NYS-S1 3 -00 3                                                              Page 20 of 27

 Flash Memory-Based Storage Devices Sanitization
 ATA Solid State Drives (SSDs)
 (This includes PATA, SATA, eSATA, etc.)
 Clear             1. Overwrite media by using organizationally approved and
                   tested overwriting technologies/methods/tools. The Clear
                   procedure should consist of at least one pass of writes with a
                   fixed data value, such as all zeros. Multiple passes or more
                   complex values may alternatively be used. Note: It is important
                   to note that overwrite on flash-based media may significantly
                   reduce the effective lifetime of the media and it may not sanitize
                   the data in unmapped physical media (i.e., the old data may still
                   remain on the media).
                   2. Use the ATA Security feature set’s SECURITY ERASE UNIT
                   command, if supported.
 Purge             1. Apply the ATA sanitize command, if supported. One or both
                   of the following options may be available:
                      a. The block erase command. Optionally: After the block
                   erase command is successfully applied to a device, write binary
                   1s across the user addressable area of the storage media and
                   then perform a second block erase.
                       b. If the device supports encryption, the Cryptographic Erase
                   (also known as sanitize crypto scramble) command. Optionally:
                   After Cryptographic Erase is successfully applied to a device,
                   use the block erase command (if supported) to block erase the
                   media. If the block erase command is not supported, Secure
                   Erase or the Clear procedure could alternatively be applied.
                   2. Cryptographic Erase through the TCG Opal SSC or
                   Enterprise SSC interface by issuing commands as necessary
                   to cause all MEKs to be changed. Refer to the TCG and vendors
                   shipping TCG Opal or Enterprise storage devices for more
                   information. Optionally: After Cryptographic Erase is
                   successfully applied to a device, use the block erase command
                   (if supported) to block erase the media. If the block erase
                   command is not supported, Secure Erase or the Clear
                   procedure could alternatively be applied.
 Destroy           Shred, Disintegrate, Pulverize, or Incinerate by burning the
                   device in a licensed incinerator.
 Notes             Verification must be performed for each technique within Clear
                   and Purge as described in NIST 800-88, Rev. 1, Guidelines for
                   Media Sanitization, Section 4.7, Verify Methods.
                   When Cryptographic Erase is applied, verification must be
                   performed prior to additional sanitization techniques (if
                   applicable), such as a Clear or Purge technique applied
NYS-S1 3 -00 3                                                               Page 21 of 27

                   following Cryptographic Erase, to ensure that the cryptographic
                   operation completed successfully. A quick sampling verification
                   as described in NIST 800-88, Rev. 1, Guidelines for Media
                   Sanitization, Section 4.7, Verify Methods should also be
                   performed after any additional techniques are applied following
                   Cryptographic Erase.
                   The storage device may support configuration capabilities that
                   artificially restrict the ability to access portions of the media as
                   defined in the ATA standard, such as a Host Protected Area
                   (HPA), Device Configuration Overlay (DCO), or Accessible Max
                   Address. Even when a dedicated sanitization command
                   addresses these areas, their presence may affect the ability to
                   reliably verify the effectiveness of the sanitization procedure if
                   left in place. Any configuration options limiting the ability to
                   access the entire addressable area of the storage media should
                   be reset prior to applying the sanitization technique. Recovery
                   data, such as an OEM-provided restoration image may have
                   been stored in this manner, and sanitization may therefore
                   impact the ability to recover the system unless reinstallation
                   media is also available.
                   Not all implementations of encryption are necessarily suitable
                   for reliance upon Cryptographic Erase as a Purge mechanism.
                   The decision regarding whether to use Cryptographic Erase
                   depends upon verification of attributes previously identified in
                   this guidance and in NIST 800-88, Rev. 1, Guidelines for Media
                   Sanitization, Appendix D.
                   Given the variability in implementation of the Enhanced Secure
                   Erase feature, use of this command is not recommended
                   without first referring the manufacturer to identify that the
                   storage device’s model-specific implementation meets the
                   needs of the organization.
                   Whereas ATA Secure Erase was a Purge mechanism for
                   magnetic media, it is only a Clear mechanism for flash memory
                   due to variability in implementation and the possibility that
                   sensitive data may remain in areas such as spare cells that
                   have been rotated out of use.
                   Degaussing must not be solely relied upon as a sanitization
                   technique on flash memory-based storage devices or on hybrid
                   devices that contain non-volatile flash memory storage media.
                   Degaussing may be used when non-volatile flash memory
                   media is present if the flash memory components are sanitized
                   using media-dependent techniques.
 SCSI Solid State Drives (SSSDs)
 (This includes Parallel SCSI, Serial Attached SCSI (SAS), Fibre Channel, USB
 Attached Storage (UAS), and SCSI Express)

NYS-S1 3 -00 3                                                                Page 22 of 27

 Clear           Overwrite media by using organizationally approved and tested
                 overwriting technologies/methods/tools. The Clear procedure
                 should consist of at least one pass of writes with a fixed data
                 value, such as all zeros. Multiple passes or more complex
                 values may alternatively be used.
                 Note: It is important to note that overwrite on flash-based media
                 may significantly reduce the effective lifetime of the media and
                 it may not sanitize the data in unmapped physical media (i.e.,
                 the old data may still remain on the media).
 Purge           1. Apply the SCSI SANITIZE command, if supported. One or
                 both of the following options may be available:
                    a. The BLOCK ERASE service action.
                   b. If the device supports encryption, the CRYPTOGRAPHIC
                 ERASE service action.
                    Optionally: After Cryptographic Erase is successfully applied
                 to a device, use the block erase command (if supported) to
                 block erase the media. If the block erase command is not
                 supported, the Clear procedure could alternatively be applied.
                 2. Cryptographic Erase through the TCG Opal SSC or
                 Enterprise SSC interface by issuing commands as necessary
                 to cause all MEKs to be changed. Refer to the TCG and vendors
                 shipping TCG Opal or Enterprise storage devices for more
                 information. Optionally: After Cryptographic Erase is
                 successfully applied to a device, use the block erase command
                 (if supported) to block erase the media. If the block erase
                 command is not supported, the Clear procedure is an
                 acceptable alternative.
 Destroy         Shred, Disintegrate, Pulverize, or Incinerate by burning the
                 device in a licensed incinerator.
 Notes           Verification must be performed for each technique within Clear
                 and Purge as described in NIST 800-88, Rev. 1, Guidelines for
                 Media Sanitization, Section 4.7, Verify Methods.
                 The storage device may support configuration capabilities that
                 artificially restrict the ability to access portions of the media,
                 such as SCSI mode select. Even when a dedicated sanitization
                 command addresses these areas, their presence may affect the
                 ability to reliably verify the effectiveness of the sanitization
                 procedure if left in place. Any configuration options limiting the
                 ability to access the entire addressable area of the storage
                 media should be reset prior to applying the sanitization
                 technique.
                 When Cryptographic Erase is applied, verification must be
                 performed prior to additional sanitization techniques (if
                 applicable), such as a Clear or Purge technique applied
                 following Cryptographic Erase, to ensure that the cryptographic
NYS-S1 3 -00 3                                                             Page 23 of 27

                 operation completed successfully. A quick sampling verification
                 as described in NIST 800-88, Rev. 1, Guidelines for Media
                 Sanitization, Section 4.7, Verify Methods should also be
                 performed after any additional techniques are applied following
                 Cryptographic Erase.
                 Not all implementations of encryption are necessarily suitable
                 for reliance upon Cryptographic Erase as a Purge mechanism.
                 The decision regarding whether to use Cryptographic Erase
                 depends upon verification of attributes previously identified in
                 this guidance and in NIST 800-88, Rev. 1, Guidelines for Media
                 Sanitization, Appendix D.
                 Degaussing must not be performed as a sanitization technique
                 on flash memory-based storage devices.
 NVM Express SSDs
 Clear           Overwrite media by using organizationally approved and tested
                 overwriting technologies/methods/tools. The Clear procedure
                 should consist of at least one pass of writes with a fixed data
                 value, such as all zeros. Multiple passes or more complex
                 values may alternatively be used.
 Purge           1. Apply the NVM Express Format command, if supported. One
                 or both of the following options may be available:
                    a. The User Data Erase command.
                     b. If the device supports encryption, the Cryptographic Erase
                 command. Optionally: After Cryptographic Erase is successfully
                 applied to a device, use the User Data Erase command (if
                 supported) to erase the media. If the User Data Erase
                 command is not supported, the Clear procedure could
                 alternatively be applied.
                 2. Cryptographic Erase through the TCG Opal SSC or
                 Enterprise SSC interface by issuing commands as necessary
                 to cause all MEKs to be changed. Refer to the TCG and vendors
                 shipping TCG Opal or Enterprise storage devices for more
                 information. Optionally: After Cryptographic Erase is
                 successfully applied to a device, use the User Data Erase
                 command (if supported) to erase the media. If the User Data
                 Erase command is not supported, the Clear procedure is an
                 acceptable alternative.
 Destroy         Shred, Disintegrate, Pulverize, or Incinerate by burning the
                 device in a licensed incinerator.
 Notes           Verification must be performed for each technique within Clear
                 and Purge.
                 When Cryptographic Erase is applied, verification must be
                 performed prior to additional sanitization techniques (if
                 applicable), such as a Clear or Purge technique applied
                 following Cryptographic Erase, to ensure that the cryptographic
NYS-S1 3 -00 3                                                            Page 24 of 27

                    operation completed successfully. A quick sampling verification
                    as described in NIST 800-88, Rev. 1, Guidelines for Media
                    Sanitization, Section 4.7, Verify Methods should also be
                    performed after any additional techniques are applied following
                    Cryptographic Erase.
                    Not all implementations of encryption are necessarily suitable
                    for reliance upon Cryptographic Erase as a Purge mechanism.
                    The decision regarding whether to use Cryptographic Erase
                    depends upon verification of attributes previously identified in
                    this guidance.
                    Degaussing must not be performed as a sanitization technique
                    on flash memory-based storage devices.
 USB Removable Media
 (This includes Pen Drives, Thumb Drives, Flash Memory Drives, Memory Sticks,
 etc.)
 Clear              Overwrite media by using organizationally approved and tested
                    overwriting technologies/methods/tools. The Clear pattern
                    should be at least two passes, to include a pattern in the first
                    pass and its complement in the second pass. Additional passes
                    may be used.
 Purge              Most USB removable media does not support sanitize
                    commands, or if supported, the interfaces are not supported in
                    a standardized way across these devices. Refer to the
                    manufacturer for details about the availability and functionality
                    of any available sanitization features and commands.
 Destroy            Shred, Disintegrate, Pulverize, or Incinerate by burning the
                    device in a licensed incinerator.
 Notes              For most cases where Purging is desired, USB removable
                    media should be Destroyed.
 Memory Cards
 (This includes SD, SDHC, MMC, Compact Flash Memory, Microdrive, MemoryStick,
 etc.)
 Clear              Overwrite media by using organizationally approved and tested
                    overwriting technologies/methods/tools. The Clear pattern
                    should be at least two passes, to include a pattern in the first
                    pass and its complement in the second pass. Additional passes
                    may be used.
 Purge              N/A
 Destroy            Shred, Disintegrate, Pulverize, or Incinerate by burning the
                    device in a licensed incinerator.
 Embedded Flash Memory on Boards and Devices
 (This includes motherboards and peripheral cards such as network adapters or any
 other adapter containing non-volatile flash memory)
NYS-S1 3 -00 3                                                               Page 25 of 27

 Clear           If supported by the device, reset the state to original factory
                 settings.
 Purge           N/A If the flash memory can be easily identified and removed
                 from the board, the flash memory may be Destroyed
                 independently from the disposal of the board that contained the
                 flash memory. Otherwise, the whole board should be
                 Destroyed.
 Destroy         Shred, Disintegrate, Pulverize, or Incinerate by burning the
                 device in a licensed incinerator.
 Notes           While Embedded flash memory has traditionally not been
                 specifically addressed in media sanitization guidelines, the
                 increasing complexity of systems and associated use of flash
                 memory has complementarily increased the likelihood that
                 sensitive data may be present. For example, remote
                 management capabilities integrated into a modern motherboard
                 may necessitate storing IP addresses, hostnames, usernames
                 and passwords, certificates, or other data that may be
                 considered sensitive. As a result, for Clearing, it may be
                 necessary to interact with multiple interfaces to fully reset the
                 device state. When this concept is applied to the example, this
                 might include the BIOS/UEFI interface as well as the remote
                 management interface.
                 As with other types of media, the choice of sanitization
                 technique is based on environment-specific considerations.
                 While the choice might be made to neither Clear nor Purge
                 embedded flash memory, it is important to recognize and
                 accept the potential risk and continue to reevaluate the risk as
                 the environment changes.

 RAM and ROM-Based Storage Device Sanitization
 Dynamic Random Access Memory (DRAM)
 Clear           Power off device containing DRAM, remove from the power
                 source, and remove the battery (if battery backed).
                 Alternatively, remove the DRAM from the device.
 Purge           Power off device containing DRAM, remove from the power
                 source, and remove the battery (if battery backed).
                 Alternatively, remove the DRAM from the device.
 Destroy         Shred, Disintegrate, or Pulverize.
 Notes           In either case, the DRAM must remain without power for a
                 period of at least five minutes.
 Electronically Alterable PROM (EAPROM)
 Clear           Perform a full chip Purge as per manufacturer’s data sheets.
 Purge           Perform a full chip Purge as per manufacturer’s data sheets.
NYS-S1 3 -00 3                                                            Page 26 of 27

 Destroy         Shred, Disintegrate, or Pulverize.
 Electronically Erasable PROM (EEPROM)
 Clear           Overwrite media by using organizationally approved and
                 validated overwriting technologies/methods/tools.
 Purge           Overwrite media by using organizationally approved and
                 validated overwriting technologies/methods/tools.
 Destroy         Shred, Disintegrate, Pulverize, or Incinerate by burning the
                 device in a licensed incinerator.

NYS-S1 3 -00 3                                                       Page 27 of 27

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
