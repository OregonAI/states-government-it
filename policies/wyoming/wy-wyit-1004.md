---
schema_version: 1
corpus: states-government-it
jurisdiction: wyoming
id: wy-wyit-1004
title: Web Standards & Compliance
doc_type: policy
citation: WyIT 1004
authority_level: ''
issuing_body: Wyoming Department of Enterprise Technology Services (Office of the Chief Information Officer)
source_url: https://drive.google.com/uc?export=download&id=15Sw5dao9X2gDcgyashsqIByXPEROHPfl
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 7e04fdf49cb696a600fdbd546e3686833777eec5d9fa568c621b5fa176283260
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

# Web Standards & Compliance (WyIT 1004)

## At a glance

WyIT 1004, Web Standards & Compliance: a statewide policy in the Enterprise Technology Services policy library. Per the Applicability section of the file it applies to all Executive Branch agencies, boards and commissions staff and to consultants, affiliates and temporary employees.

## Full text

                WEB STANDARDS AND COMPLIANCE
                                           WyIT - 1004

  PURPOSE: To define Americans with Disabilities Act (ADA) accessibility requirements
  for agency websites and non-mapping web applications; conditions for using links to
  vendors, private sector businesses, and other non-government entities; applicable
  settings within State websites; supported technologies for deploying agency websites
  and web applications; and the conditions for use of audio, video, and image file types in
  agency websites.

  I.   APPLICABILITY

       This policy applies to all Executive Branch agencies, boards, and commissions staff
       (collectively referred to as “agencies”). This policy is also applicable to consultants,
       affiliates, and temporary employees.

 II.   DEFINITIONS

       All definitions for this policy are located in the Policy Dictionary.

III.   EXCEPTIONS

       Any exceptions provided to the following policy must abide by WyIT - 3002 -
       Security Exception Request policy.

IV.    ADA COMPLIANCE

       Provide reasonable steps to accommodate ADA compliance for all websites and
       web applications. Accommodations should always be taken to provide website and
       web application content in an alternate accessible format in the event ADA
       requirements cannot be met.

                                                                               WyIT 1004          Page 1

 V.    ADVERTISING LINKS

       A. Allowable Uses of Commercial Links

            ● The link is required under a software license or copyright agreement, and the
              software is an integral part of the website and/or web application.
            ● When an organization has a defined ongoing business or a functional
              relationship with the State entity and that requires a link.
            ● The citizens of Wyoming would see direct value from the link. This does not
              include temporary business partnerships such as professional services
              contracts.
            ● The link is for a specific product or technology required to access data or
              functionality on the website or web application, for example, Adobe Acrobat
              Reader.
            ● The link provides site security information to validate Secure Sockets Layer
              (SSL) Certificates from the certificate provider.
            ● Links to city, county, or federal websites.

       B. Required Disclaimer

            ● “By using this website, you acknowledge that the State of Wyoming does not
              endorse any of the sites or services that may be referenced on or linked to
              on this site. The State of Wyoming will not be responsible or liable for those
              sites' content or any loss occasioned by any such content. Other Internet
              sites or services may have privacy policies or security that differ from the
              privacy policy or security of the State of Wyoming.”

VI.    PUBLIC FACING STATE WEBSITES

       A.   Requirements

            ●   Citizen Information,
            ●   Business Information,
            ●   Government Information,
            ●   Visitor Information, and
            ●   Wyoming Attorney General’s Privacy Policy.

VII.   WEBSITE & WEB APPLICATION REQUIREMENTS

                                                                         WyIT 1004             Page 2

        All websites and web applications must at a minimum be World Wide Web
        Consortium (W3C) , http://www.w3.org/standards/, compliant as a requirement for
        rendering web pages in a variety of web browsers.

VIII.   WEB TRANSPORT LAYER (TLS) SECURITY CERTIFICATES

        A. Any web site or web application that requires authentication through the use of
           user IDs, passwords, pin numbers, etc. must use TLS encryption on the pages
           utilizing authentication.

        B. Any sensitive data transmitted over the internet must use TLS. Sensitive
           information may include:

           ● Social Security Number, Employer Identification Number, or other account
             identifiers; or
           ● Date of birth; or
           ● Phone number for a person or business; or
           ● Street address for a person or business; or
           ● Employment and wage information; or
           ● Health information; or
           ● Other information defined by law as confidential, sensitive, or non-public
             information

        C. At a minimum, web pages providing user authentication using TLS must display
           the certificate vendor’s secure site seal on the login page.

        D. Only valid third-party TLS certificates can be used on public access pages that
           require TLS.

        E. Intranet pages that require TLS can use either third-party TLS certificates, or
           internally generated certificates.

        F. Must use current and non-deprecated encryption algorithms to ensure robust
           security and protect against known vulnerabilities.

 IX.    WEB DOMAIN NAMING

        A. All new state agency internet and intranet websites must use wyo.gov as the
           URL suffix if they are supported on the state’s primary Domain Name Server
           (DNS).

                                                                       WyIT 1004             Page 3

     B. Existing state agency internet and intranet websites can still use one of the
        following suffixes:

        ●   wyo.gov → e.g. ets.wyo.gov
        ●   wy.gov → e.g. dot.wy.gov
        ●   wyoming.gov → e.g. doe.wyoming.gov
        ●   wyoming.us → e.g. dfs.wyoming.us
        ●   state.wy.us → e.g. gf.state.wy.us
        ●   .edu → e.g. wy.edu. Wcc.edu

     C. The suffixes below are acceptable for public state agency websites, but will not
        be supported in the state’s primary Domain Name Server (DNS). It is the
        responsibility of the state agency to either manage their own DNS to support
        these suffixes or have the domain names supported outside the state’s DNS
        server.

        ● .org

     D. A website developed and hosted outside the State of Wyoming infrastructure
        can be moved into the State of Wyoming infrastructure using a supported
        domain name suffix.

X.   WEB COOKIE USE

      A.      A visitor to a state web site should not be required to accept a cookie in
              order to view public information.

      B.      The use of persistent cookies should be avoided. If used, they should
              contain a unique name identifying the site or application.

      C.       Cookies must not store confidential information unless they are
               encrypted.

REFERENCES

     ● Wyoming §§ 40-21-101 — 40-21-119

     ● IRS Publication 1075, Safeguards for Protecting Federal Tax Returns and Return
       Information

     ● Health Insurance Portability and Accountability Act (HIPAA)

                                                                       WyIT 1004           Page 4

    ● Minimum Acceptable Risk Standards for Exchanges (MARS-E) 2.0 Framework

    ● Family Education Rights Privacy Act (FERPA)

    ● Payment Card Industry – Data Security Standards (PCI-DSS)

    ● Criminal Justice Information Services (CJIS)

    ● Children’s Online Privacy Protection Act (COPPA)

SUPERSEDED POLICIES: This policy supersedes the policies listed below.

   ● 03300-P010, Web Domain Naming Policy, dated September 27, 2016

   ● 03500-P013, Web Cookie Use Policy, dated May 20, 2016

                                                                  WyIT 1004    Page 5

                         DOCUMENT HISTORY

                           ORIGINAL SUBMISSION
 SUBMITTED           SUBMITTED       APPROVED            APPROVED BY            EFFECTIVE
    ON                  BY              BY                 DATE(S)                DATE

June 2024        ETS Governance,   Public Comment        06/14/2024 -        July 2024
                 Risk and          Period                06/28/2024
                 Compliance

                                    REVISIONS
  REVISION            REVISED        APPROVED            APPROVED BY            EFFECTIVE
    DATE                BY              BY                 DATE(S)                DATE

November 2024    ETS Governance,   State Chief           September 2016      November 2024
                 Risk and          Information Officer   May 2016
                 Compliance
                                                         (See ‘Superseded
                                                         Policy Above)

                                     REVIEWS
            REVIEW                     LAST                                NEXT
             DATE                  REVIEWED BY                          REVIEW DATE

                                                                            WyIT 1004        Page 6

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
