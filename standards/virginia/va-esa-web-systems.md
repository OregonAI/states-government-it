---
schema_version: 1
corpus: states-government-it
jurisdiction: virginia
id: va-esa-web-systems
title: Web Systems
doc_type: standard
citation: 'EA requirements document: Web Systems'
authority_level: ''
issuing_body: Virginia Information Technologies Agency (VITA)
source_url: https://www.vita.virginia.gov/media/vitavirginiagov/it-governance/ea/pdf/Web-Systems.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: c27831b136ddd1c58738603c7b9b4d42d34121b94a2cc718026f61e5692c48f6
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
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Web Systems (EA requirements document: Web Systems)

## At a glance

Item of VITA's Enterprise Architecture page, group 'ESA - Enterprise Solutions Architecture Requirements': an EA requirements document under the Enterprise Architecture Standard (EA225), whose requirement statements are mandatory for executive branch agencies. The PDF prints: EA Standard (EA-225) ESA Web Systems, Version 2.0, May 5, 2025.

## Full text

  Commonwealth of Virginia
Enterprise Architecture Standard (EA-225)

 Enterprise Solutions Architecture [ESA]
                     Web Systems

 vita.virginia.gov                 May 5, 2025

ESA Web Systems                               Version 2.0                                       5/5/2025

Revision History

                                Web System Requirements: Version History
 Revision      Date              Description
 1.0           9/6/2022          Initial document created
 1.1           9/12/2022         Updated for comments from DBVI
 1.2           10/11/2022        Updated for comments from VITA
 1.3           10/27/2022        Updated for additional comments from VITA
 1.4           2/6/2023          Amended per public comment feedback
 1.5           2/8/2023          Amended per VITA CIO feedback
 1.6           3/30/2023         Amended WEB-154 to clarify the use of CAPTCHA
 1.7           2/1/2024          Updated languages and numbering
 1.8           4/23/2024         Updated to reflect new requirements from ADA Title II
 1.9           5/28/2024         Amended per public comment feedback
 2.0           5/5/2025          Administrative Changes: Amended to reflect new domain naming
                                 requirements

Review Process
This requirements document was posted on the Virginia Information Technologies Agency’s (VITA)
Online Review and Comment application (ORCA). All agencies, stakeholders, and the public were
encouraged to provide their comments through ORCA. All comments were evaluated, and individual
commenters were notified of action(s) taken.

Requirements and agency Exceptions
The requirements included within this document are mandatory. Agencies deviating from these
requirements must request an exception for each desired deviation, and receive an approved enterprise
Architecture Exception via Archer, prior to developing, procuring, or deploying such technology, or not
complying with a requirement specified in this document. The instructions for completing and submitting
an exception request are contained within the Commonwealth Enterprise Architecture Policy.

Glossary
As appropriate, terms and definitions used in this document are in the COV ITRM IT Glossary. The COV
ITRM IT Glossary is available on the VITA website.

                                             Page 2 of 23

ESA Web Systems                                                                                      Version 2.0                                                                                                  5/5/2025

Contents
  Introduction ................................................................................................................................................................................................................. 4
  Purpose ......................................................................................................................................................................................................................... 4
  Scope.............................................................................................................................................................................................................................. 4
  Authority ....................................................................................................................................................................................................................... 4
  Solution Business Requirements ...................................................................................................................................................................... 5
  Domain Naming ..........................................................................................................................................................................................................7
  Design/Architecture ................................................................................................................................................................................................. 8
  Accessibility ............................................................................................................................................................................................................... 10
  Availability/Performance ...................................................................................................................................................................................... 17
  Capacity ....................................................................................................................................................................................................................... 17
  Continuity ................................................................................................................................................................................................................... 18
  Integration/Interoperability ............................................................................................................................................................................... 18
  Technology ................................................................................................................................................................................................................. 18
  Security ....................................................................................................................................................................................................................... 18
  Definitions .................................................................................................................................................................................................................. 19

                                                                                                   Page 3 of 23

ESA Web Systems                                 Version 2.0                                        5/5/2025

Introduction
                                            Vision & Strategy
                                                  Vision
 Commonwealth of Virginia (COV) Workers shall create and maintain web-based content for the citizens
 of the Commonwealth in a manner that is accessible, consistent, creative, and secure.
                                                 Strategy
 Objective 1     To produce a consistent and homogenous appearance for COV web systems across all
                 Commonwealth agency websites
 Objective 2     To produce web content that is accessible by all citizens of the Commonwealth
 Objective 3     To establish a sense of authenticity through consistency in domain naming, ensuring
                 citizens that information being provided comes from a trusted source
 Objective 4     To ensure that COV web systems are secure from harm against cybersecurity attacks

Purpose
The intent of this standard is to guide the management, development, purchase, and use of web system
resources within COV. This standard encompasses and replaces the previous Website Topic Report
released on September 21, 2017.
For further information on the perspectives identified in this document, please reference the VITA
Enterprise Architecture Standard (EA-225).

Scope
This standard is applicable to all Commonwealth agencies (hereinafter collectively referred to as
"agencies") that are responsible for the management, development, purchase and use of information
technology resources in the Commonwealth of Virginia and applies to all COV web systems.
This standard does not apply to research projects, research initiatives, or instructional programs at public
institutions of higher education.
In addition to the requirements below all COV IT technology solutions comply with the standards found
on VITA’s Policies, Standards & Guidelines.

Authority
Code of Virginia, §2.2-2007          Powers of the CIO

Code of Virginia, §2.2-2007.1        Additional duties of the CIO relating to information technology
                                     planning and budgeting

Code of Virginia, §2.2-2009(A)       Additional duties of the CIO relating to security of government
                                     information

Code of Virginia, §2.2-2012(A)       Additional powers and duties related to the procurement of
                                     information technology

U.S. Access Board                    ICT Accessibility 508 Standards

                                               Page 4 of 23

ESA Web Systems                                  Version 2.0                                         5/5/2025

Solution Business Requirements
      VITA
      WEB-01      VITA shall define and maintain a Commonwealth of Virginia Design System (COV Design
                  System)1 as a guide for COV web systems that shall include:
                  •    Branded template framework
                  •    Website components
                  •    Software Resources
                  •    Commonwealth Banner
                  •    Best Practice Guidelines
      WEB-02      VITA shall define design principles to be employed in the development of COV web
                  systems. These shall include guidance for the device independent responsive display of
                  COV content across a broad range of form factors, to make these systems consistent
                  and homogenous in appearance across the Commonwealth agency portfolio.
      WEB-03      VITA shall create and maintain the design system resource for COV web systems to
                  utilize.
      WEB-04      VITA shall calculate peak load for new COV web systems prior to launch.
      WEB-05      VITA shall create and maintain an implementation schedule for the adoption of the
                  requirements identified in this standard.
      WEB-06      VITA shall conduct accessibility and vulnerability scans for COV web systems.

      COV Agencies
      WEB-07      All Commonwealth of Virginia agencies shall use the COV Design System for web
                  systems.
                  COV intranets and Private Authenticated Web Applications shall conform to the
                  Accessibility and Security sections below but are not required to follow any other
                  requirements in this standard.
      WEB-08      All agencies shall adhere to VITA-defined design principles and guidance for the
                  development of COV web systems.
      WEB-09      All agencies shall identify to VITA a point of contact who serves as the responsible party
                  for each COV web system.
      WEB-10      All agencies shall adhere to the published implementation schedule for the adoption of
                  the requirements identified in this standard.
      WEB-11      COV web systems shall not display advertisements or commercial banners unless
                  authorized by COV or the agency.
      WEB-12      Agencies shall annually provide output from compliance tools in Archer that attest to the
                  following, to confirm adherence with the requirements contained in this standard:
                  •    Application of COV Design System Styles, Components, and Templates
                  •    Accessibility testing
                  •    Performance testing
                  •    Security scans
                  •    Penetration testing

1
    developer.virginia.gov

                                                Page 5 of 23

ESA Web Systems                                  Version 2.0                                        5/5/2025

                 •   Technology requirements
      WEB-13     Agencies shall comply with the Code of Virginia, § 2.2-3803 (B) and at a minimum:
                 •   Develop an Internet privacy policy and an Internet privacy policy statement that
                     explains the policy to the public2
                 •   Tailor the policy and the statement to reflect the information practices of the
                     individual agency
                     The Internet Privacy Policy and Internet Privacy Policy Statement shall address:
                 •   What information, including personally identifiable information, shall be collected if
                     any
                 •   Whether any information shall be automatically collected simply by accessing the
                     website and, if so, what information
                 •   Whether the website automatically places a computer file, commonly referred to as a
                     cookie, on the Internet user's computer and, if so, for what purpose
                 •   How the collected information is being used or shall be used.
                     o   A prescribed procedure for an individual to learn the purpose for which
                         information has been recorded and particulars about its use and dissemination
                     o   A clearly prescribed and uncomplicated procedure for an individual to correct,
                         erase or amend inaccurate, obsolete, or irrelevant information
      WEB-14     Agencies that maintain exclusions to WEB-07, including those systems identified as
                 exempt in the Code of Virginia, § 2.2-3802, shall state those exclusions in their policy.
      WEB-15     Agency Internet Privacy Policy Statements shall identify that any personal information
                 that is collected and retained is maintained in compliance with the Code of Virginia, §§
                 2.2-3800 and 2.2-3803.
      WEB-16     Agency Internet Privacy Policy Statements shall inform users that information collected
                 on this site may be provided to anyone that requests it under the Virginia Freedom of
                 Information Act.
      WEB-17     COV web systems shall provide a conspicuous link for their agency’s Internet Privacy
                 Policy Statement that shall be displayed per the directives of the COV Design System.
      WEB-18     All agency COV web systems shall have a web policy that shall include the following:
                 •   Disclaimer – a statement that indemnifies the commonwealth from responsibility for
                     third party or externally linked content
                 •   Link policy – a policy stating the criteria that allows a link to be placed on the site
                 •   FOIA – a statement that explains the agency’s Freedom of Information Act policies
                     and contacts
      WEB-19     Agencies shall develop and post on their COV web systems a language translation policy
                 that states the level of support for language translation on agency web systems.
                 •   Agencies that rely on AI translation services such as Google Translate shall
                     incorporate the Automated Translation Disclaimer into the Language Translation
                     Policy
      WEB-20     COV web systems shall provide language translation where required by applicable law or
                 where appropriate to achieve other business objectives.
                 •   Agencies providing content for which a high degree of accurate translation is
                     essential shall consider engaging professional language translation services.

2
    An example of an agency privacy policy may be found on the VITA website.

                                                Page 6 of 23

ESA Web Systems                                   Version 2.0                                      5/5/2025

               •   Where feasible, web systems should provide for machine translation in the top languages
                   of the Commonwealth: English, Spanish, Chinese (Traditional and Simplified), Korean,
                   Arabic, Vietnamese, Tagalog, Urdu, French, and Hindi3.

Domain Naming
      Government Internet domain naming identifies and implements standardized naming conventions to
      aid in developing statewide electronic directories and reducing overhead and administrative costs.
      Consistency in domain naming also conveys a sense of authenticity to a consumer, that the
      information being provided comes from a trusted source.
      Domains and sub-domains of other domains are often referred to by level. The levels of a domain
      name are numbered from right to left. Using the sample domain name department.oaa.virginia.gov
      the levels are as follows:
                   •   first-level          gov
                   •   second-level         virginia
                   •   third-level          agency acronym
                   •   fourth-level         agency discretion
      Fourth-level names may include the web system name, activity name, or department name.
                   Example
                   • department.oaa.virginia.gov

      WEB-21       All agencies and boards in the Commonwealth except for institutions of higher education
                   shall use the virginia.gov domain name. This requirement does not preclude agencies
                   from possessing other domain names for which they separately register and accept full
                   responsibility.
                   Any Commonwealth entity seeking to implement domain names that deviate from this
                   standard shall require that an Enterprise Architecture exception be granted before the
                   domain name can be created.
                   Any COV entity seeking to implement domain names that deviate from this standard
                   must ensure consistency, security, and brand alignment for Virginia agency websites.

                   Alternate URLs may be used alongside (agency).virginia.gov URLs only under specific,
                   justified business conditions and must satisfy the following conditions:
                           a.   Public Engagement – The alternate URL supports a statewide initiative or
                                public-facing campaign that requires a distinct, memorable web address for
                                accessibility and outreach.

                           b. Operational Necessity – The agency operates a specialized service or web
                              application that requires a non-standard domain due to technical or vendor-
                              related constraints.
                                  Example: agencymuseum.org

                           c.   Interagency Collaboration – The alternate URL facilitates a multi-agency
                                partnership where branding must remain neutral to represent multiple
                                stakeholders.

3
    Source: DataUSA: Virginia

                                                 Page 7 of 23

ESA Web Systems                              Version 2.0                                          5/5/2025

             All alternate URLs must be pre-approved by the Virginia IT Agency (VITA) via an EA
             exception.

             Agencies must provide a business justification demonstrating alignment with the above
             conditions.

             Alternate URLs must redirect users to the corresponding virginia.gov domain when
             feasible.

             Branded domain names are acceptable but must have a redirect from a properly formed
             virginia.gov address.
             All legacy domain names that do not comply with the standard will be grandfathered but
             must redirect to a properly formed DNS name. All new domain names must comply on
             creation.
             Domain names produced COTs or SaaS solutions where the resulting URL is not under
             COV control are excluded from this requirement.
   WEB-22    Domain Names are to be composed of alphabetic characters and numbers. Upper/lower
             case is transparent. Hyphens (dashes) are allowed but may not be used at the beginning
             or end of a domain name. Within a domain name spaces, the underscore, and special
             characters are not permitted. Special characters include but are not limited to: ! @ # $ % ^
             &*()?”
   WEB-23    The name of an agency of the Commonwealth of Virginia will be at the third level and will
             consist of the official agency acronym/abbreviation.
             Examples
             • vita.virginia.gov
             • doa.virginia.gov
   WEB-24    Fourth Level Domain Names – The fourth level of the virginia.gov domain will be used to
             further subdivide the entities established at the third level. Since many organizations
             exist at several levels of government, their location within this hierarchy will allow citizens
             to distinguish between them. Fourth level names are generally at the discretion of the
             requesting agency. The examples below are offered as a guideline to encourage a
             generally accepted and recognizable naming convention.
             Examples of Departments or Activities of Executive Branch Agencies
             • license.dwr.virginia.gov
             • eva.dgs.virginia.gov
   WEB-25    Agencies shall provide annually to VITA a list of all first level domains registered on
             domains.dotgov.gov or other private registrars, including non-government top-level
             domains such as .com, .us, and .org.
   WEB-26    Agencies with public DNS entries must classify those entries in Archer as one of the
             following types:
             •    Web site
             •    Web application
             •    Administrative entry

Design/Architecture
   WEB-27    All agencies shall display the Commonwealth Banner unaltered and as defined by the
             COV Design System.

                                             Page 8 of 23

ESA Web Systems                              Version 2.0                                       5/5/2025

   WEB-28    COV web systems shall provide an agency site search box which shall appear on every
             page and shall be displayed per the directives of the COV Design System.
   WEB-29    COV web systems shall include a sitemap to enable search engines to crawl a website
             more efficiently. Examples will be provided in the COV Design System.
   WEB-30    COV web systems shall ensure that each page shall have a footer containing, at a
             minimum, the following information:
             •    Agency name
             •    Copyright information
             •    Text or an approved icon link stating Web Accessibility Initiative (WAI) compliance.
             •    Link to the agency’s Internet Privacy Policy Statement.
             •    Link to FOIA Information
             •    Translation Disclaimer
             •    Other items as defined by the COV Design System
   WEB-31    COV web systems shall provide a Contact Us page that shall include, at a minimum, the
             agency’s:
             •    Mailing address
             •    FAX number, if available
             •    Phone number, including a toll-free number and/or, TTY number if available
             •    Email link or contact form to an agency contact
             The Contact Us page shall be accessible from the page footer.
             Note     Agencies should employ generic email addresses and avoid associating agency
                      contact links to specific individuals.
   WEB-32    COV web systems shall ensure that all public content posted shall be searchable and
             discoverable through the public search engines appearing on the COV Search Engine
             Technology Roadmap.
   WEB-33    Agencies shall audit COV web systems search results relevant to their agency name and
             content on a semi-annual basis.
   WEB-34    COV web systems that shall retain function in offline or low-bandwidth instances shall be
             implemented as Progressive Web Applications.
   WEB-35    COV web systems shall support Dark Mode to conserve the battery life of Organic Light-
             Emitting Diode (OLED) screen devices and for users with visual sensitivity to bright
             screens.
   WEB-36    COV platform web systems, including Commercial Off-the-Shelf (COTS) systems, shall
             support white-labelling for seamless use of Commonwealth Branding as defined by the
             COV Design System.
   WEB-37    COV web systems shall employ web analytics to track, analyze, and report on web
             system traffic. Analytics reporting shall be available to VITA for review.
   WEB-38    Agencies shall submit their COV web systems for architecture review in Archer for the
             requirements covered in this standard prior to their initial release, and on subsequent
             release of architecturally significant changes. Agencies shall use VITA approved
             reporting tools for accessibility scoring, Performance scoring, and Vulnerability scans.
             Artifacts for architecture review shall include:
             •    Accessibility scoring, targeting a minimum 86% accessibility compliance
             •    Policy review, to ensure compliance with website design requirements
             •    Performance scoring, targeting 90% or better

                                            Page 9 of 23

ESA Web Systems                              Version 2.0                                       5/5/2025

              •   Vulnerability scans, ensuring compliance with Commonwealth Security Standards

Accessibility
   These accessibility requirements were derived from and conform to Web Content Accessibility
   Guidelines (WCAG) 2 Level AA.
   WEB-39     COV web systems shall provide needed accessibility information that shall be displayed
              per the directives of the COV Design System, so that the user shall have immediate
              knowledge as to how to best navigate the website.
   WEB-40     COV web systems shall support high-contrast colors for users with low vision and
              graphical rendering of audio cues for users with hearing disabilities.
   WEB-41     COV web systems shall include information in text when the color of words, backgrounds,
              or other content is used to convey information.
   WEB-42     COV web systems shall ensure that hyperlinks are easily identifiable through non-color
              means, including both default and hover states.
              Note    The easiest and most conventional way to signify links is underlining.
   WEB-43     COV web systems shall ensure that required fields and fields with errors must include
              some non-color way to identify them.
   WEB-44     COV web systems shall organize pages using properly nested HTML headings.
   WEB-45     COV web systems shall use Accessible Rich Internet Applications (ARIA) to enhance
              accessibility only when HTML is not sufficient.
              Note    Use caution when providing ARIA roles, states, and properties.
   WEB-46     COV web systems shall use ARIA landmarks and labels to identify regions of a page.
   WEB-47     COV web systems shall programmatically indicate required fields using the required or
              aria-required attributes.
   WEB-48     COV web systems shall follow corresponding ARIA authoring practices for tooltips:
              •   Tooltips are displayed and disappear via keyboard focus and removal of focus and by
                  the mouse events - mousing over and mousing out
              •   Tooltip never receive focus, focus stays on the owning element
              •   Tooltips can be hidden with the Escape key
              •   Tooltips are only hidden via JavaScript and CSS selectors, when JavaScript is not
                  available the tooltip is shown
   WEB-49     When visible text alone is not sufficient to convey meaning, COV web systems shall use
              advanced techniques to provide additional meaning, such as ARIA attributes, screen
              reader only text, or the title attribute.
   WEB-50     COV web systems shall identify errors using aria-invalid.
   WEB-51     When providing inline help text, COV web systems shall use aria-describedby to
              associate the help text with the input.
   WEB-52     When creating a custom interactive widget, COV web systems shall consult the ARIA
              Authoring Practices Document. COV web systems shall use ARIA labels, descriptions,
              roles, states, and properties to expose information about the component.
   WEB-53     COV web systems shall use ARIA live regions or ARIA alerts to convey a status message
              to screen reader users.

                                           Page 10 of 23

ESA Web Systems                               Version 2.0                                         5/5/2025

   WEB-54    COV web systems shall ensure that status messages can be programmatically
             determined through role or properties, such that they can be presented to the user by
             assistive technologies without receiving focus, in content implemented using markup
             languages.
   WEB-55    COV web systems shall reserve tables for tabular data, use table headers appropriately,
             and use table captions.
   WEB-56    COV web systems shall ensure all content does not restrict its view and operation to a
             single display orientation, such as portrait or landscape, unless a specific display
             orientation is essential.
             Note Examples where a particular display orientation may be essential are a bank
             check, a piano application, slides for a projector or television, or virtual reality content
             where content is not necessarily restricted to landscape or portrait display orientation.
   WEB-57    COV web systems shall not automatically play audio on pages.
   WEB-58    COV web systems shall provide an easy way to disable the audio and adjust the volume
             where audio is provided.
   WEB-59    COV web systems shall ensure that text, including images of text, have a contrast ratio of
             at least 4.5:1. For text and images of that is at least 24px and normal weight or 19px and
             bold, use a contrast ratio that is at least 3:1.
   WEB-60    COV web systems shall ensure a color contrast of at least 3:1 for custom states of
             elements where they appear, such as hover, active, or focus.
   WEB-61    COV web systems shall ensure that visual presentations of the following must have a
             contrast ratio of at least 3:1 against adjacent colors:
             •    User interface components (except for inactive components or when the appearance
                  of the component is determined by the user agent)
             •    Graphical objects that are required to understand the content, except when that
                  particular presentation of objects is essential to the information being conveyed
             .
   WEB-62    COV web systems shall avoid the use of images of text except in cases such as logos.
   WEB-63    COV web systems shall provide responsive stylesheets such that content can be
             presented without loss of information or functionality, and without requiring scrolling in
             two dimensions (horizontal and vertical) for:
             •    Vertical scrolling content at a width equivalent to 320 CSS pixels (equivalent to a
                  starting viewpoint of 1280 CSS pixels wide at 400% zoom)
             •    Horizontal scrolling content at a heigh equivalent to 256 CSS pixels (equivalent to a
                  starting viewpoint height of 1024 CSS pixels at 400% zoom)

             Note     This does not apply to content that requires two-dimensional layout for usage or
                      meaning such as maps and diagrams, video, games, presentations, and data
                      tables.
   WEB-64    For content that appears on hover and focus COV web systems shall ensure that the
             content:
             •    Is dismissible with the escape key
             •    Can be hovered over
             •    Remains available unless it is dismissed, it is no longer relevant, or the user removes
                  hover and focus

                                            Page 11 of 23

ESA Web Systems                               Version 2.0                                           5/5/2025

   WEB-65    COV web systems shall ensure that content that appears on hover or focus should not
             obscure other content unless it presents a form input error. or can be dismissed with the
             escape key.
   WEB-66    COV web systems shall ensure pointer hover or keyboard focus triggers additional
             content to become visible and then hidden when the following are true:
             •    A mechanism is available to dismiss the additional content without moving pointer
                  hover or keyboard focus unless the additional content communicates an input error
                  or does not obscure or replace other content
             •    If pointer hover can trigger the additional content, then the pointer can be moved over
                  the additional content without the additional content disappearing
             •    The additional content remains visible until the hover or focus trigger is removed, the
                  user dismisses it, or its information is no longer valid

             Note This rule does not apply to the visual presentation of additional content that is
             controlled by the user agent.

   WEB-67    COV web systems shall ensure that entering/exiting a menu or combo box, or moving
             among open web pages on a website, does not cause the user to lose focus.
   WEB-68    COV web systems shall ensure that all functionalities shall be available to a keyboard
             without requiring specific timing of keystrokes unless the functionality cannot be
             provided by a keyboard alone.
   WEB-69    COV web systems shall ensure that items on the page do not automatically move, blink,
             scroll, or update, including carousels. Exceptions to this requirement shall provide a way
             to pause, stop, or hide the moving, blinking, scrolling, or updating.
   WEB-70    COV web systems shall not provide any content that flashes more than three times in any
             1-second period.
   WEB-71    COV web systems shall create a logical tab order through links, form controls, and
             interactive objects.
   WEB-72    When inserting content into the DOM COV web systems shall insert the content
             immediately after the triggering element or use scripting to manage focus in an intuitive
             way. When triggering dialogs and menus, those elements shall follow their trigger in the
             focus order in an intuitive way. When content is dismissed or removed, COV web systems
             shall place focus back on the trigger.
   WEB-73    COV web systems shall ensure that the purpose of each link can be determined from the
             link text alone, or from the link text and the containing paragraph, list item, or table cell, or
             the link text and the title attribute.
   WEB-74    COV web systems shall include at least two of the following:
             •    List of related pages
             •    Table of contents
             •    Site map
             •    Search
             •    List of all pages
   WEB-75    COV web systems shall ensure that on each page, headings, landmark labels, and form
             labels are unique unless the structure provides adequate differentiation between them.
   WEB-76    COV web systems shall provide keyboard focus styles that are highly visible, and make
             sure that a visible element has focus at all times when using a keyboard. COV web
             systems shall not rely on browser default focus styles.

                                             Page 12 of 23

ESA Web Systems                              Version 2.0                                       5/5/2025

   WEB-77    COV web systems shall require that all functionality using multipoint or path-based
             gestures for operation, be operated with a pointer input that operates with one point of
             contact with the screen without a path-based gesture, unless a multipoint or path-based
             gesture is essential.
             Note This rule does not apply to actions that are required to operate the user agent or
             assistive technology.
   WEB-78    COV web systems shall ensure that for functionality that can be operated using a pointer
             input that operates with one point of contact with the screen, at least one of the following
             must be true:
             •    The event that occurs when the trigger stimulus of the pointer is depressed is not
                  used to execute any part of the function
             •    Completion of the function on the event that occurs when the trigger stimulus of a
                  pointer is released, and a mechanism is available to abort the function before
                  completion or to undo the function after completion
             •    The function on the event that occurs when the trigger stimulus of a pointer is
                  released reverses any outcome of the preceding event that occurs when the trigger
                  stimulus of the pointer is depressed
             •    Completion of the function on the event that occurs when the trigger stimulus of the
                  pointer is depressed is essential. Functions that emulate a keyboard or numeric
                  keypad key press are considered essential

             Note This rule does not apply to actions that are required to operate the user agent or
             assistive technology.

   WEB-79    COV web systems shall avoid triggering functionality on down-events, such as
             onmousedown, and prefer events such as onclick instead. Functions triggered by an up
             event such as onmouseup shall provide a way to abort or undo the function.
   WEB-80    COV web systems shall avoid activating functionality through motion, such as shaking a
             phone. If motion triggers functionality, COV web systems shall provide a way to disable
             the motion trigger and provide an alternative way to activate the functionality.
             Functionality that can be operated by device motion or user motion can also be operated
             by user interface components and responding to the motion can be disabled to prevent
             accidental actuation, except when:
             •    The motion is used to operate functionality through an accessibility-support interface
             •    The motion is essential for the function and doing so would invalidate the activity

   WEB-81    When the focus changes or when a user inputs information or interacts with a control,
             COV web systems shall not:
             •    Cause a change in page content
             •    Spawn a new browser window
             •    Submit a form
             •    Cause further change in focus
             •    Cause any other change that disorients the user
             When an input causes such a change, the user shall be informed ahead of time.
   WEB-82    COV web systems shall ensure that when components are repeated across web page,
             they should appear in the same relative order regarding other repeated components on
             each web page where they appear.

                                           Page 13 of 23

ESA Web Systems                              Version 2.0                                        5/5/2025

   WEB-83    COV web systems shall ensure that when a navigation menu is presented on multiple
             pages, the links shall appear in the same order on each page.
   WEB-84    COV web systems shall ensure that when components have the same functionality
             across several web pages, the components are labeled consistently on each page.
   WEB-85    COV web systems shall visually indicate required fields in the form's instructions or form
             labels and shall not indicate required fields via CSS alone.
   WEB-86    COV web systems shall make errors easy to discover, identify, and correct.
   WEB-87    COV web systems shall use semantic, descriptive labels for inputs.
   WEB-88    COV web systems shall visually position labels in a consistent way that makes
             associating labels with form controls easy and shall not rely on placeholder text in lieu of
             an HTML label.
   WEB-89    COV web systems shall provide text instructions at the beginning of a form or set of
             fields that describes the necessary input.
   WEB-90    COV web systems shall ensure the purpose of each input field collecting information
             about the user can be programmatically determined when:
             •    The input field serves a purpose identified in the following list defined by the WCAG.
             •    The content is implemented using technologies with support for identifying the
                  expected meaning for form input data.
             Note         An element is considered programmatically determined when software from
                          author-supplied data provided in a way that different software used to
                          retrieve and view web content, including assistive technologies, can extract
                          and present this information to users in different modalities such as markup
                          languages.
   WEB-91    When an input error is detected and suggestions for correction are known, COV web
             systems shall provide suggestions for fixing the submission. Refer to the COV Design
             System for examples of error handling.
   WEB-92    COV web systems shall provide easy ways to confirm, correct, or reverse a user action
             where a mistake would cause a serious real-world consequence, such as submitting
             financial data, entering into a legal agreement, submitting test data, or making a
             transaction.
   WEB-93    COV web systems shall ensure that all img tags have alt attributes.
   WEB-94    When short alt text is sufficient to describe an image, COV web systems shall provide the
             short text via the image's alt attribute.
   WEB-95    When short text alternative is not sufficient to describe an image, such as in a chart,
             graph, or diagram, COV web systems shall provide short text via the image's alt attribute
             and include a long description in nearby text.
   WEB-96    If an image or icon is used as a button or link, COV web systems shall ensure the image
             has a text alternative sufficient to describe the purpose of the button or link.
   WEB-97    For images that are decorative, used for formatting, or contain content already conveyed
             in text, COV web systems shall have a null alt attribute or shall be implemented as CSS
             background images.
   WEB-98    When iframes are employed in COV web systems they shall have descriptive titles and
             include the sandbox attribute.

                                            Page 14 of 23

ESA Web Systems                              Version 2.0                                        5/5/2025

   WEB-99     COV web systems shall minimize the number of adjacent links to the same destination by
              combining adjacent images and text into a single link, rather than creating a separate link
              for each element.
   WEB-100    COV web systems shall use semantic markup to designate headings, lists, figures, and
              emphasized text.
   WEB-101    When the appearance of text conveys meaning, COV web systems shall use appropriate
              semantic markup.
   WEB-102    COV web systems shall avoid emulating links and buttons.
              •   Use the a and button tags appropriately
              •   Avoid using a tags for buttons
              •   Avoid using div, or span tags for links or buttons
   WEB-103    COV web systems shall avoid using whitespace characters for layout purposes.
   WEB-104    COV web systems shall ensure that the source order presents content meaningfully.
              When the page is viewed without styles, all content on the page shall still appear in a
              meaningful and logical order.
   WEB-105    COV web systems shall not identify content based on its color, size, shape, position,
              sound, or other sensory characteristics.
   WEB-106    COV web systems shall not convey information solely through icons or symbols.
   WEB-107    When a form field asks for information about the user and if there is an appropriate
              HTML autocomplete attribute COV web systems shall include that autocomplete
              attribute.
   WEB-108    COV web systems shall ensure that there is no loss of content or functionality when text
              resizes.
   WEB- 109   COV web systems shall ensure that content implemented using markup languages that
              support the following text style properties below, should ensure no loss of content or
              functionality occurs by setting all of the following and by changing no other style
              property:
              •   Line height to at least 1.5x the font size
              •   Spacing following paragraphs to at least 2x the font size
              •   Letter spacing to at least 0.12x the font size
              •   Word spacing to at least 0.16x the font size
              Note        This does not apply to human languages and scripts that do not make use of
                          one or more of these text style properties in written text.
   WEB-110    COV web systems shall define texts and text containers in relative units (percents, ems,
              rems) rather than in pixels.
   WEB-111    COV web systems shall avoid using pixels for defining the height and spacing, such as
              height or line height, of text boxes.
   WEB-112    COV web systems shall avoid implementing access keys. When access keys and other
              keyboard shortcuts are implemented, they shall not interfere with existing browser and
              screen reader provided shortcuts.
   WEB-113    COV web systems shall avoid relying exclusively on pointer-driven events, such as
              onmouseover, to provide functionality when scripting. Generally, such functionality will
              also require scripting for keyboard operability.

                                            Page 15 of 23

ESA Web Systems                              Version 2.0                                        5/5/2025

   WEB-114   COV web systems shall avoid using scripts to remove focus from an element until the
             user moves focus manually.
   WEB-115   COV web systems shall ensure keyboard focus is never trapped on an element without an
             obvious way to move focus out of the element. COV web systems shall ensure the user
             can move focus to and from all focusable elements using a keyboard only.
   WEB-116   COV web systems shall ensure if a keyboard shortcut is implemented in content using
             only letters (including upper- and lower-case), punctuation, numbers, or symbol
             characters, then at least one of the following must be true:
             •    A mechanism is available to turn the shortcut off
             •    A mechanism is available to remap the shortcut to include one or more non-printable
                  keyboard keys
             •    The keyboard shortcut for a user interface component is only active when that
                  component has focus
   .
   WEB-117   COV web systems shall not require time limits to complete tasks unless necessary. If a
             time limit is necessary, the time limit should be at least 20 hours, or it can be extended,
             adjusted, or disabled.
   WEB-118   COV web systems shall provide a link to skip to the main content as the first focusable
             link on the page.
   WEB-119   COV web systems shall ensure each web page has a title tag that is descriptive,
             informative, and unique.
   WEB-120   COV web systems shall avoid using tab index values greater than 0.
   WEB-121   COV web systems shall ensure that for user interface components with labels that
             include text or images of text, the name contains the text that is presented visually. A
             best practice is to have the text of the label at the start of the name.
   WEB-122   COV web systems shall ensure that when a visual label is present for an interactive
             element, such as a link or form control, the accessible name of the element should
             contain the visual label.
   WEB-123   COV web systems shall provide a lang attribute on the page's html element. If a portion
             of the page is in a different language, use the lang attribute on that part.
   WEB-124   COV web systems shall validate all page HTML and avoid significant validation / parsing
             errors.
   WEB-125   COV web systems shall avoid creating custom widgets when HTML elements already
             exist.
   WEB-126   For pre-recorded audio without video, COV web systems shall provide a descriptive
             transcript that includes dialogue and all other meaningful sound.
   WEB-127   For pre-recorded video without audio, COV web systems shall provide a text alternative or
             audio descriptions that provide the same information presented.
   WEB-128   COV web systems shall provide captions for prerecorded audio content in non-live
             synchronized media.
   WEB-129   For non-live video, COV web systems shall provide a descriptive transcript or an audio
             description.
   WEB-130   COV web systems shall provide captions for live audio and video.

                                            Page 16 of 23

ESA Web Systems                               Version 2.0                                     5/5/2025

   WEB-131   COV web systems shall ensure that videos should include radio style narration so that
             content makes sense if someone is consuming just the audio track and include any text
             elements in the narration.
   WEB-132   COV web systems shall ensure that instruction in the operation of an accessible video
             player is available before the video is encountered.
   WEB-133   COV web systems shall ensure that video can be started and stopped, paused, and
             repeated through keyboard access.

Availability/Performance
   WEB-134   Agencies, in consultation with VITA, shall conduct user population analysis to identify the
             potential volume of traffic.

 WEB-135     COV web systems shall meet the following minimum performance budget:
              Metric                              Budget
              First Contentful Paint (FCP)        0–1800 milliseconds
              Speed index                         3.4–5.8 seconds
              Largest Contentful Paint (LCP)      0–2500 milliseconds
              Time to Interactive (TTI)           3.8–4.8 seconds
              Cumulative Layout Shift (CLS)       0–0.1 seconds
              Total Blocking Time (TBT)           200-600 milliseconds

   WEB-136   COV web systems which have higher performance requirements than those identified in
             WEB-135 shall define those requirements in a performance budget.
   WEB-137   VITA shall provide a performance testing service for COV web systems.
   WEB-138   COV web systems shall engage in performance testing prior to production deployment to
             confirm the system’s expected behavior.
   WEB-139   COV web systems shall be monitored for performance in production according to the
             minimum performance budget or agency-defined performance budget as appropriate.
   WEB-140   Providers of COV web system monitoring services shall triage, escalate, and report
             disruptions in performance.
   WEB-141   VITA shall provide a service to conduct traffic analysis of COV web systems to identify
             changes in user population and traffic patterns.
   WEB-142   Agencies shall conduct semi-annual traffic analysis of COV web systems.
   WEB-143   Agencies shall bi-annually load test web systems using synthetic requests which
             simulate estimated peak load.

Capacity
   WEB-144   Agencies shall create and maintain capacity plans for data storage required by COV web
             systems.
   WEB-145   COV web systems shall have sufficient infrastructure resources to support their
             predicted volume of traffic and storage, based on the performance profile identified in
             WEB-135, including additional headroom to address spikes in traffic.

                                             Page 17 of 23

ESA Web Systems                                   Version 2.0                                         5/5/2025

Continuity
      WEB-146     COV web systems shall be categorized as one of the following:
                  •   Mission critical
                  •   Business critical
                  •   Non-critical
      WEB-147     Mission critical COV web systems shall:
                  •   Be deployed in a highly available configuration
                  •   Have an RTO and RPO of less than 15 minutes
                  •   Subscribe to Disaster Recovery services4
      WEB-148     Business critical COV web systems shall have an RTO of 4 hours and an RPO of 4 – 24
                  hours.
      WEB-149     Non-critical COV web systems shall have an RTO of 24 hours and an RPO of 25 – 48
                  hours.

Integration/Interoperability
      WEB-150     COV web systems shall be fully functional on approved web browsers identified in the
                  EUC Browser Technology Roadmap and shall display and operate in a consistent manner.

Technology
      WEB-151     COV web systems shall be tested for functionality on approved web browsers prior to
                  each production deployment.
      WEB-152     COV web systems shall use permalinks to ensure the long-term viability of links.
      WEB-153     Approved COV web browsers shall be configured to allow automated web page
                  translation.

Security
      WEB-154     COV web systems shall be subject to periodic automated security scans to confirm
                  robustness against cybersecurity attack. 5 Systems must engage in the following tests
                  prior to each production deployment and shall not be released with critical security
                  defects identified as High.
                  •   Static Security Analysis Testing
                  •   Software Composition Analysis
                  •   Dynamic Analysis Security Testing
      WEB-155     Providers of COV web vulnerability services shall stay attuned to changes in the threat
                  landscape and shall escalate and report on all new threats requiring immediate attention
                  to VITA.
      WEB-156     COV web systems shall have ad-hoc security scans performed when new exploits or
                  vulnerabilities are identified by VITA and shall place priority on the remediation of all
                  defects identified as High within 30 days of detection.

4
    See VITA Service Catalog offering Disaster Recovery (Server).

                                                 Page 18 of 23

ESA Web Systems                                  Version 2.0                                       5/5/2025

    WEB-157     COV web systems shall be subject to annual penetration testing and shall place priority
                on the remediation of all critical defects identified by such tests within 30 days of
                detection.
    WEB-158     Public facing COV web systems shall employ Web Application Firewalls.
    WEB-159     Web systems that require authentication must employ accessible captcha to confirm
                that a user is a human.
    WEB-160     Web systems that present online forms must employ accessible captcha for submission.

Definitions
As appropriate, terms and definitions used in this document are included in the COV ITRM IT Glossary.

Architectural significance              A concern, problem, or system element that has a wide impact
                                        on the structure of a system, or on its important quality
                                        properties such as performance, scalability, security, reliability, or
                                        evolvability.

Accessible Rich Internet Applications   A technical specification published by the World Wide Web
(ARIA)                                  Consortium (W3C) that specifies how to increase the
                                        accessibility of web pages dynamic content, and user interface
                                        components developed with Ajax, HTML, JavaScript, and related
                                        technologies.
                                        See Accessible Rich Internet Applications (WAI-ARIA) 1.2.

Business critical                       Business processes or systems that are essential for an agency
                                        to keep running, for which an outage produces significant
                                        disruption to the agency's mission. They are core to the agency’s
                                        function, but which are not necessary to ensure immediate
                                        survival during outages and other disasters.

Captcha                                 A type of challenge–response test used in computing to
                                        determine whether the user is human in order to deter bot
                                        attacks and spam.
                                        Any public, indexable website deployed on behalf of the
Citizen Facing Website                  Commonwealth.

COV web system                          Any web system created by, or on behalf of, a Commonwealth
                                        agency that is deployed on COV-based infrastructure, hosted on
                                        a media platform, or is downloadable for installation on smart
                                        devices, including:
                                            •     Web applications created by agency development teams
                                                  or 3rd party vendors
                                            •     Web sites created on platform systems6
                                            •     Low-code/No-Code applications7
                                            •     Web apps for smart devices
                                            •     Web-based desktop systems8

6
  Examples include systems such as T4, Oracle Financials, or Salesforce.
7
  Examples include systems such as Microsoft Power Apps or AWS Honeycode.
8
  Examples include systems constructed in the manner of Microsoft Teams or Slack.

                                                Page 19 of 23

ESA Web Systems                            Version 2.0                                        5/5/2025

Cumulative Layout Shift (CLS)        A measure of the largest burst of layout shift scores for every
                                     unexpected layout shift that occurs during the entire lifespan of
                                     a page.

Dark mode                            A color scheme that uses light-colored text, icons, and graphical
                                     user interface elements on a dark background. It is often
                                     discussed in terms of computer user interface design and web
                                     design.

Design System                        A set of interconnected patterns and shared practices coherently
                                     organized. Design systems aid in digital product design and
                                     development of products such as applications or websites. They
                                     may contain, but are not limited to, pattern libraries, design
                                     languages, style guides, coded components, brand languages,
                                     and documentation.

Document Object Model                The data representation of the objects that comprise the
                                     structure and content of a document on the web.

Dynamic Analysis Security Testing
                                     A runtime analysis of an application that is live in an environment
                                     to scan link, images, line of text and code to identify
                                     vulnerabilities.

First Contentful Paint (FCP)         Measures the time from when the page starts loading to when
                                     any part of the page's content is rendered on the screen.

Form factor                          A hardware design aspect that defines and prescribes the size,
                                     shape, and other physical specifications of components,
                                     particularly in electronics.
                                     Examples of different smart device form factors include:
                                     •   Laptops
                                     •   Smartphones
                                     •   Tablets
General Authenticated Web Application An application that is used by Commonwealth Employees and
                                      the public.

Hypertext Markup Language (HTML)     The standard markup language for documents designed to be
                                     displayed in a web browser.

Hypertext Transfer Protocol (HTTP)   An application layer protocol in the Internet protocol suite model
                                     for distributed, collaborative, hypermedia information systems. It
                                     is the foundation of data communication for the World Wide
                                     Web.

Hypertext Transfer Protocol Secure   An extension of HTTP which uses encryption for secure
(HTTPS)                              communication over a computer network.

Largest Contentful Paint (LCP)       Reports the render time of the largest image or text block visible
                                     within the viewport, relative to when the page first started
                                     loading.

Layout shift                         Any time a visible element changes its position from one
                                     rendered frame to the next.

                                          Page 20 of 23

ESA Web Systems                             Version 2.0                                       5/5/2025

Mission critical                      A business process or system that must function continuously
                                      for an agency to be successful, for which the impact of an
                                      outage is immediate and catastrophic to the agency's mission.

Non-critical                          A business processes or system for which an outage will not
                                      significantly affect an agency's mission.

Organic Light-Emitting Diode (OLED)   A light-emitting diode (LED) in which the emissive
                                      electroluminescent layer is a film of organic compound that
                                      emits light in response to an electric current. OLEDs are used to
                                      create digital displays in devices such as television screens,
                                      computer monitors, and portable systems such as smartphones
                                      and handheld game consoles.

Performance Budget                    A collection of limits imposed on a defined set website metrics
                                      that describe expected performance.

Permalink                             A URL that is intended to remain unchanged for many years into
                                      the future, yielding a hyperlink that is resistant to link rot

Platform web system                   Any web system that provides enterprise-level capabilities for
                                      large-scale or multitenant implementations, including human
                                      resource management systems (HRMS), Financial Management
                                      Solutions (FMS), supply chain management (SCM), customer
                                      relationship management (CRM), enterprise performance
                                      management (EPM), and Content Management Systems (CMS).

Private Authenticated Web Application An application that is used exclusively by Commonwealth
                                      Employees.

Progressive Web Application (PWA)     A type of application software delivered through the web, built
                                      using common web technologies including HTML, CSS,
                                      JavaScript, and WebAssembly. They employ an architectural
                                      approach called the App Shell Model where service workers
                                      store the Basic User Interface or shell of the responsive web
                                      design web application in the browser's offline cache, allowing
                                      the PWA to maintain native-like use with or without web
                                      connectivity.

RPO                                   The measurement of the point in time to which data must be
                                      restored to resume processing transactions. Directly related to
                                      the amount of data that can be lost between the point of
                                      recovery and the time of the last data backup.

RTO                                   The period in which systems, applications or functions must be
                                      recovered after an outage.

Semantic markup                       The use of a markup language such as HTML to convey
                                      information about the meaning of each element in a document
                                      through proper selection of markup elements, and to maintain
                                      complete separation between the markup and the visual
                                      presentation of the elements contained in the document.

Smart device                          An electronic device capable of connecting to a network, or to
                                      other devices, via wireless communication protocols, and which
                                      can operate interactively and autonomously to some extent. It

                                           Page 21 of 23

ESA Web Systems                            Version 2.0                                         5/5/2025

                                     includes devices that exhibit some properties of ubiquitous
                                     computing, such as artificial intelligence.
                                     Smart devices support a variety of form factors, a range of
                                     properties pertaining to ubiquitous computing and to be used in
                                     three main system environments: physical world, human-
                                     centered environments, and distributed computing
                                     environments.
                                     Several notable types of smart devices are:
                                     •   Laptops
                                     •   Smartphones
                                     •   Tablets & Phablets
                                     •   Smartwatches
                                     •   Smart vehicles

Software Composition Analysis        Analysis of open-source libraries included in applications for
                                     security flaws and vulnerabilities.

Speed index                          A measure of how quickly content is visually displayed during
                                     page load on a web system.

Static Security Analysis Testing     Analysis of application code for security flaws and vulnerabilities
                                     without execution of that code.

Time to Interactive (TTI)            A measure of how much time passes before the page is fully
                                     interactive, which means:
                                     • First Contentful Paint (FCP) is complete.
                                     • No long JavaScript tasks happened within the last 5
                                         seconds.
                                     • No more than two in-flight GET requests are occurring at the
                                         same moment.
Total Blocking Time (TBT)            Measures the total amount of time that a page is blocked from
                                     responding to user input, such as mouse clicks, screen taps, or
                                     keyboard presses. The sum is calculated by adding the blocking
                                     portion of all long tasks between First Contentful Paint and Time
                                     to Interactive.

Web Accessibility Initiative (WAI)   An initiative of the World Wide Web Consortium (W3C) that
                                     develops standards and support materials for the understanding
                                     and implementation of accessibility in web systems.

Web Application Firewall             Protects web applications by filtering and monitoring HTTP
                                     traffic between a web application and the Internet. It typically
                                     protects web applications from attacks such as cross-site
                                     forgery, cross-site-scripting (XSS), file inclusion, and SQL
                                     injection, among others.

Web system                           Any system that delivers content between a web-client and
                                     webserver using HTTP as the underlying communication
                                     standard, including HTTP and HTTPS.
                                     Note
                                     All COV infrastructure is bound by security standards SEC-
                                     501/SEC-520/SEC-530 which contain the control SC-8

                                          Page 22 of 23

ESA Web Systems         Version 2.0                                        5/5/2025

                  Transmission Confidentiality and Integrity for the encryption of
                  data in transit requiring HTTPS.

White-labelling   A white-label product is a product or service produced by one
                  company that other companies rebrand to make it appear as if
                  they had made it. The name derives from the image of a white
                  label on the packaging that can be filled in with the marketer's
                  trade address

                       Page 23 of 23

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
