---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-nys-s16-001
title: New York State Universal Web Navigation
doc_type: standard
citation: NYS ITS Standard NYS-S16-001
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/new-york-state-universal-web-navigation
source_format: pdf
retrieved: '2026-11-11'
source_sha256: f77ba2b9adbac74bbbbf4a59d0f6ef87ca390241a0338d521387e8b385c46a88
effective_date: null
source_version: 'Updated: 01/15/25'
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
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# New York State Universal Web Navigation (NYS ITS Standard NYS-S16-001)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Web/Digital Government, Statewide Policies' on the listing. The listing prints original publication 04/15/2016 and last modified 01/15/2025.

## Full text

                                                     State Capitol P.O. Box 2062
                                                       Albany, NY 12220-0062
                                                           www.its.ny.gov

       New York State Information                                        No: NYS-S16-001
         Technology Standard

                       IT Standard                                       Updated: 01/15/25

                                                                         Issued By: NYS Office of Information
       New York State                                                    Technology Services (ITS)

       Universal Web                                                     Owner: Office of Digital Transformation /
                                                                         NYS Design System Team

         Navigation

1.0 Purpose and Benefits
   The purpose of this mandatory technology standard is to define a Universal Navigation
   to be used for all New York State government entities’ public websites and web
   applications.

2.0 Authority
   Section 103(10) of the State Technology Law provides the Office of Information
   Technology Services (“ITS”) with the authority to establish statewide technology
   policies, including technology and security standards. Section 2 of Executive Order No.
   117 1, established January 2002, provides the State Chief Information Officer with the
   authority to oversee, direct and coordinate the establishment of information technology
   policies, protocols and standards for State government, including hardware, software,
   security and business re-engineering. Details regarding this authority can be found in

   1
    All references to Executive Order 117 refer to that which was originally issued by Governor George E. Pataki on January 28, 2002
   and continued by Executive Order 5 issued by Governor Eliot Spitzer on January 1, 2007, Executive Order 9 issued by Governor
   David A. Patterson on June 18, 2008, and Executive Order 2 issued by Governor Andrew M. Cuomo on January 1, 2011 and
   Executive Order 6 issued by Governor Kathy Hochul on October 8, 2021.

   NYS ITS Policy, NYS-P08-002 Authority to Establish State Enterprise Information
   Technology (IT) Policy, Standards and Guidelines.

3.0 Scope
   This policy applies to all “State Entities” (SE), defined as “State Government” in
   Executive Order 117 or “State Agencies” as defined in Section 101 of the State
   Technology Law. This includes employees and all third parties (such as local
   governments, consultants, vendors, and contractors) that use or access any Information
   Technology (IT) Resource for which the SE or ITS has administrative responsibility ,
   including systems managed or hosted by third parties on behalf of the SE or ITS. While
   an SE may adopt a different policy/standard, it must include the requirements set forth
   in this one. Where a conflict exists between this policy/standard and an SE’s
   policy/standard, the more restrictive policy will take precedence.

4.0 Information Statement
   The New York State Universal Navigation provides a consistent visual identity, with
   support for search and translation functionality, across all NYS websites.

   The Universal Navigation includes header and footer elements for use on SE public
   websites. The Universal Navigation must be included on all SE public websites and web
   applications as defined below.

   4.1 New York State Universal Navigation

   The official embeddable code and implementation instructions are available in the
   “Universal Navigation (Next)” repository on the New York State GitHub account.
   Detailed guidelines and instructions for implementing the Universal Navigation are
   included in the repository and should be considered an extension of this standard. This
   repository also contains guidance, frequently asked questions, demos, and other
   resources to support implementation.

   For scenarios where a website cannot use the standard embedded implementation of
   the Universal Navigation, an exception request must be submitted to the ITS Design
   System Team using the Universal Navigation (UNav) Intake Form. This ensures that
   express permission is provided for exceptions and a record of sites not using the embed
   is maintained.

   4.2 Universal Navigation Size

   The Universal Navigation must extend the full width of a web page with no gaps between
   elements and the browser or application window edges unless a specific exception is
   approved in writing. Responsive design techniques are used to scale appropriately for

   NYS-S16-001                                                                    Page 2 of 5

different devices, including desktops, tablets, and mobile phones, provided the site or
application is also designed responsively.

4.3 Universal Navigation Design

The Universal Navigation is designed to blend with NYS websites and web applications
and cannot be altered visually or functionally, except for the approved settings available
through configuration options that are defined in the technical documentation. Any other
modifications require an approved exception. Existing websites should continue to
follow the established NYS Branding Guidelines.

4.4 Placement of the Universal Navigation

The Universal Navigation must appear at the top of every page on the SE’s public
websites and web applications. Nothing should appear above the Universal Navigation
in the browser or application window. Additional edits cannot be made to alter the
appearance of the Universal Navigation, including additional links. No elements of the
native webpage or application should overlap the container element of the Universal
Navigation.

4.5 Intranet and Non-Public Facing Sites or Applications

While not required, intranet websites, extranets, and other non-public facing sites or
applications may include the Universal Navigation if it enhances the user experience.

4.6 Functionality and Updates to the Universal Navigation

Functionality of the Universal Navigation should be tested in a development
environment before deploying. If problems arise when implementing the standard
version, check the repository for troubleshooting guidance and support resources.

Updates to the Universal Navigation occur periodically. In general, a testing period will
precede the official deployment of updates. Development teams should test updates to
the Universal Navigation in development environments and submit problems or
concerns through the UNav Intake Form.

4.7 Including Accessibility Features

The Universal Navigation is designed to work with various accessibility requirements. A
“skip to content” or “skip to navigation” link can be used at the top of a webpage to aid
visitors using screen readers or with limited motor abilities.

When possible, a “skip to content” link should:

NYS-S16-001                                                                       Page 3 of 5

          1. Remain hidden from normal view until engaged, with no space between the
             Universal Navigation header element and the top of the web page or
             application.

          2. Act as the initial link for screen readers.

          3. Appear when common accessibility practices are engaged.

   4.8 Domain and Encryption Requirements

   The Universal Navigation includes messaging that explains how to identify an official
   ny.gov website by both the .gov domain and HTTPS encryption. This is an emerging
   pattern for official websites at all levels of government.

   The Universal Navigation may ONLY be used on websites or applications with a ny.gov
   domain that are secured with HTTPS encryption. Existing websites or applications that do
   not meet these requirements and have the Universal Navigation embedded on their
   websites must either be compliant by March 15, 2025 or request an exemption from the
   ITS Design System Team. Technical measures may be implemented after this date to
   prevent non-compliant sites from embedding the Universal Navigation script.

   Websites or web applications that are unable to meet these requirements cannot use the
   embedded version of the Universal Navigation. However, a modified, recreated version of
   the navigation bar may be permitted under certain circumstances. To request an
   exception, submit a request to the ITS Design System Team via the UNav Intake Form.

5.0 Compliance
   This standard shall take effect upon publication. Compliance is required with all
   enterprise policies and standards. ITS may amend its policies and standards at any
   time; compliance with amended policies and standards is required.

   If compliance with this standard is not feasible or technically possible, or if deviation
   from this standard is necessary to support a business function, SEs shall request an
   exception through the ITS Design System Team’s exception process via the UNav
   Intake Form.

   ITS may also assess SE compliance with this standard. To accomplish this assessment,
   ITS may issue, from time to time, requests for information to SEs, which will be used to
   develop any reporting requirements as may be requested by the NYS Chief Information
   Officer, the Executive Chamber, or Legislative entities.

6.0 Definitions of Key Terms

   NYS-S16-001                                                                      Page 4 of 5

   Except for terms defined in this policy, all terms shall have the meanings found in the
   ITS Glossary.

7.0 Contact Information
     Submit all inquiries & requests for future enhancements regarding this standard to:

                                  NYS Design System
                            Office of Digital Transformation
                                Reference: NYS-S16-001
                     NYS Office of Information Technology Services
                          State Capitol, ESP, P.O. Box 2062
                                    Albany, NY 12220

                 Inquiries may also be directed to DesignSystem@its.ny.gov.

    The State of New York Enterprise IT Policies may be found at the following website:
                                https://its.ny.gov/policies

8.0 Revision History
   This policy should be reviewed consistent with the requirements set forth in ITS-P24-
   003 Process for Establishing Information Technology Polices, Standards and
   Guidelines.

    Date             Description of Change                            Reviewer
    April 15,2016    Original Policy issued to replace NYS-S05-001    WebNY
                     State Common Web Banner
    01/25/2025       Updated to include *.ny.gov and HTTPS            NYS Design
                     requirement, revision to scope and authority,    System Team
                     cursory review to remaining document.

9.0 Related Documents
   New York State GitHub Repository for the updated Universal Navigation:
   https://github.com/ITS-HCD/unav-next

   NYS-S16-001                                                                    Page 5 of 5

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
