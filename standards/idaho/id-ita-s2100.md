---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s2100
title: S2100 – Operating Systems
doc_type: standard
citation: ITA Standard S2100
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s2100.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 0866e46ce7fe948ad69edcc67b38eda8f646b3e6ae35fcf4e727b0bf435401f6
effective_date: '2001-10-17'
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# S2100 – Operating Systems (ITA Standard S2100)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '2000 - Software - Desktop, Notebook, and Mobile Devices, Standards', a standard. The library's own summary: "ITA Standard S2100 standardizes operating systems for desktops and notebooks, ensuring consistency, stability, and reduced support costs."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS S2000 – SOFTWARE – DESKTOP &
NOTEBOOK

Category:    S2100 – OPERATING SYSTEM (OS) – Desktop & Notebook

CONTENTS:
I.    Definition
II. Rationale
III. Approved Standard(s)
IV. Approved Product(s)
V. Justification
VI. Technical and Implementation Considerations
VII. Emerging Trends and Architectural Directions
VIII. Procedure Reference
IX. Review Cycle
X. Contact Information
      Revision History

I. DEFINITION

   Operating system (OS) - The software that controls all internal operations on a desktop
   or notebook computer. This includes video display actions; reading and writing from both
   memory and storage devices; transferring information to attached printers;
   communicating with other networked devices; and inputting from keyboard, mouse, and
   screen.

II. RATIONALE

   In a client/server environment, speed, memory, and a stable operating platform become
   increasingly important. Support of the desktop and notebook operating systems
   constitutes a large portion of Idaho's cost for supporting its technology infrastructure.
   The more desktop operating systems supported, the higher the State's costs for
   technology infrastructure support. Standardizing on fewer operating systems greatly
   simplifies technical support requirements and contributes directly to significantly lower
   support expenses. In addition, Windows XP will no longer be supported by Microsoft in
   April 2014 so it will not receive any updates or patches, leaving it open to vulnerabilities.

III. APPROVED STANDARD(S)

   Graphical User Interface (GUI) for Intel-compatible platform.

S2100 – Operating System (OS) – Desktop & Notebook                                    Page 1 of 4

IV. APPROVED PRODUCT(S)

   1. Microsoft Windows vendor supported versions (Latest service pack release).

V. JUSTIFICATION

   Graphical user interfaces offer significant advantages and ease of use, reduced training
   requirements, and improved user productivity. While Microsoft Windows is a proprietary
   operating system, it dominates the desktop and notebook computer OS market and has
   become a de facto standard.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

   For the desktop workstation OS, Windows is the stated long-term architectural direction
   as the enterprise standard for State agencies. It is mandatory that agencies upgrade
   from Windows XP prior to the end of support date April 8, 2014. . Bypassing Windows
   Vista and upgrading directly to a later, supported version of Windows is recommended.

   In the event that an Agency is unable to meet the April 2014 date and needs to continue
   using Windows XP, the system(s) running XP must meet the following criteria to remain
   in their environment:

       1. The system(s) running Windows XP must be air gapped where they are physically
          isolated and unable to communicate with the agency network, state network or
          the internet. OR

       2. VLAN the XP machine(s) to an separate zone with a firewall in front of them and
          allow access only to the internet OR

       3. Purchase extended Windows XP support from Microsoft OR

       4. Remove users from Local Administrator group on the XP machine AND
            a. Install a supported AV client on the XP system AND
            b. Remove internet access to the system AND
            c. Remove all email access to the system including an agencies Exchange or
               GroupWise, Gmail, Yahoo mail or any other internet email application AND
            d. If the agency is unable to upgrade any XP machine within 30 days after the
               End Of Life date:
                   i.  A Formal Exemption Request, as defined in the ITA Policy P1010,
                       shall be submitted and approved.
                  ii.  The agencies security coordinator must be notified that there are
                       existing unsecured computer(s) or network(s) still running Windows
                       XP in their environment.

S2100 – Operating System (OS) – Desktop & Notebook                               Page 2 of 4

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

   The use of more than one (1) operating system further complicates the acquisition
   strategy and technical support for the desktop environment in State government, so
   agencies are encouraged to standardize on one (1) version of the operating system.
   The move to upgrade the OS requires careful testing and planning within a formal
   transition strategy.

   Agencies should begin to review and plan for a later, supported version of Windows OS,
   which are currently available as well as planning for Operating Systems that will be End
   Of Life in the future. This planning process should include comprehensive application
   testing, image building, and pilot deployments.

VIII. PROCEDURE REFERENCE

IX. REVIEW CYCLE

   Six (6) Months

X. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

REVISION HISTORY

4/15/2014 -      Added additional criteria in section VI to include sub-sections 2-4

11/7/2013 –      Removed specific references to any approved Operating System as long
                 as the OS is vendor supported and must be patched and updated
                 regularly. Removed references to mobile devices. Made upgrading from
                 XP mandatory unless they met the criteria that allows XP to remain in their
                 environment.

7/01/2013 –      Changed “ITRMC” to “ITA”.

12/09/2009 –     Update standard to remove Windows 2000 and add Windows Vista
                 and Windows 7. Update to remove Windows Mobile from the standard.

6/16/09 –        Deleted Timeline from this standard.3/7/2007 – Changed the reference to
                 Windows Vista to show that it is now available and to encourage agencies
                 to begin planning for a Vista deployment. Added reference to Windows
                 Mobile 2006 for mobile devices.

11/15/2006 –     Added a reference to Windows Vista in the “Emerging Trends and
                 Architectural Directions” section.

S2100 – Operating System (OS) – Desktop & Notebook                                     Page 3 of 4

9/21/2005 –      Added references to mobile devices to the Technical and Implementation
                 Considerations and in the Emerging Trends and Architectural Directions
                 recommending Microsoft Windows Mobile 2003 as the OS that agencies
                 should consider due to the close integration with the standard desktop and
                 notebook standard. Mobile device use is growing rapidly in agencies and the
                 use of one operating system will simply support within the agencies.

8/25/2004 –      Removed Microsoft Windows 98 and NT from list of approved products.
                 With Microsoft’s announcement of the discontinuance of its “mainstream
                 support phase” for Windows 98 and Windows NT 4.xx as of June 30, 2002,
                 and “end of life” for Windows NT 3.5x as of December 31, 2002, it is time for
                 agencies to move off these operating systems. It is also important from both
                 an improved functionality and security perspective to transition to the
                 remaining ITRMC approved products as soon as possible.

                 Effective Date: October 17, 2001

S2100 – Operating System (OS) – Desktop & Notebook                                 Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
