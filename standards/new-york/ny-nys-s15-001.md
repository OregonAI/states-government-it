---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-nys-s15-001
title: Patch Management
doc_type: standard
citation: NYS ITS Standard NYS-S15-001
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/patch-management
source_format: pdf
retrieved: '2026-11-11'
source_sha256: f2cdc17516b7c4fe7fb3b877f5b937fcae1a1858a3e0b25c4125d7e14112ce3d
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

# Patch Management (NYS ITS Standard NYS-S15-001)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Cybersecurity, Statewide Policies' on the listing. The listing prints original publication 01/16/2015 and last modified 04/29/2025.

## Full text

                                                          State Capitol P.O. Box 2062
                                                            Albany, NY 12220-0062
                                                                www.its.ny.gov

                New York State
                                                                           No: NYS-S15-001
       Information Technology Standard

                            IT Standard:                                   Updated: 04/29/2025

                                                                           Issued By: NYS Office of Information
             Patch Management                                              Technology Services

                                                                           Owner: Chief Information Security Office

 1.0 Purpose and Benefits

         The purpose of this standard is to ensure systems and applications are consistently
         maintained and fully up to date with the most current security configurations. Systems and
         applications are updated via the security patch management (patch management)
         process. Patch management is a practice designed to proactively prevent the exploitation
         of Information Technology (IT) vulnerabilities that exist within an organization. By applying
         security related patches to applicable IT systems, the expected result is reduced time and
         money spent dealing with exploits by reducing or eliminating the related vulnerability.

 2.0 Authority
        Section 103(10) of the State Technology Law provides the Office of Information
        Technology Services (ITS) with the authority to establish statewide technology policies,
        including technology and security standards. Section 2 of Executive Order No. 117 1,
        established January 2002, provides the State Chief Information Officer with the authority
        to oversee, direct and coordinate the establishment of information technology policies,
        protocols and standards for State government, including hardware, software, security and
        business re-engineering. Details regarding this authority can be found in NYS ITS Policy,

1 All references to Executive Order 117 refer to that which was originally issued by Governor George E. Pataki on January 28, 2002 and
continued by Executive Order 5 issued by Governor Eliot Spitzer on January 1, 2007, Executive Order 9 issued by Governor David A. Patterson on
June 18, 2008, Executive Order 2 issued by Governor Andrew M. Cuomo on January 1, 2011 and Executive Order 6 issued by Governor
Kathy Hochul on October 8, 2021.

NYS-S15-001                                                                                                                    Page 1 of 7

      NYS-P08-002 Authority to Establish Enterprise Information Technology Policies,
      Standards, and Guidelines

 3.0 Scope
       This standard applies to all “State Entities” (SE), defined as “State Government” entities in
       Executive Order 117 or “State Agencies” as defined in Section 101 of the State Technology
       Law. This includes employees and all third parties (such as local governments,
       consultants, vendors, and contractors) that use or access any Information Technology (IT)
       resource for which the SE or ITS has administrative responsibility, including systems
       managed or hosted by third parties on behalf of the SE or ITS. While an SE may adopt a
       different standard, it must include the requirements set forth in this one. Where a conflict
       exists between this standard and a SE’s standard, the more restrictive requirement will
       take precedence.

 4.0 Information Statement
      The NYS-S15-002 Vulnerability Management Standard should be followed for
      requirements on addressing non-patched vulnerabilities.

      1.   SEs are responsible for ensuring that an individual or group is overseeing patch
           management for any given system throughout its lifecycle. That individual or group
           may be within IT operations.
      2. If patch management is outsourced, service level agreements must be in place that
           meet or exceed the requirements of this standard and outline responsibilities for
           patching. If patching is the responsibility of the third party, SEs must verify that the
           patches have been applied.
      3. A process must be in place to manage patches. This process must include the
           following:

              •   Monitoring security sources (see Exhibit 1) for vulnerabilities, patch and non-
                  patch remediation, and emerging threats.
              •   Overseeing patch distribution, including verifying that a change control
                  procedure is being followed.
              •   Testing for stability and deploying patches.
              •   Using an automated centralized patch management distribution tool, whenever
                  technically feasible, which:
                     o Maintains a database of patches.
                     o Deploys patches to endpoints.
                     o Verifies installation of patches.
      4. Appropriate separation of duties must exist so that the individual(s) verifying patch
           distribution is not the same individual(s) who is distributing the patches.

NYS-S15-001                                                                                Page 2 of 7

      5. As per the NYS-P03-002 Information Security Policy, all SEs must maintain an
         inventory of IT resources. Patch management must incorporate all the SE’s installed IT
         resources.
      6. Patch management must be prioritized based on the severity of the vulnerability that
         the patch addresses. In most cases, severity ratings are based on the Common
         Vulnerability Scoring System vulnerability, and a CVSS of 0.1-3.9 is considered a low
         impact vulnerability.
               •   The NYS Chief Information Security Office (CISO) may deem any vulnerability to
                   be high impact, regardless of CVSS score, based on a NYS specific analysis.
      7. The impact to the SE's information assets is based on the asset's information
         classification as per the NYS-S14-002 Information Classification Standard. The
         patching process must follow the timeline contained in the tables below:

                                        TABLE 1: RISK RATING
                                                            Exposure

              Impact
                                    Systems with         Systems with             System
              (Confidentiality,
                                    no network           network                  that is
              Integrity,            connectivity to      connectivity to          publicly
              Availability          production           production data          available
                                    data                 (not internet            from the
                                                         facing)                  internet

          High                      Moderate             High                     High

          Moderate                  Low                  Moderate                 High

          Low                       Low                  Low                      High

NYS-S15-001                                                                               Page 3 of 7

                                       TABLE 2: PATCH TIMEFRAMES

                                           Vulnerability Severity

         Risk               Critical         High              Moderate
                                                                                  Low
         Rating             (CVSS            (CVSS             (CVSS
         (from                                                                    (CVSS score
                            score 9.0-       score 7.0-        score 4.0-
         Table 1)                                                                 0.1-3.9)
                            10.0)            8.9)              6.9)
                                                                                  At the
                                                                                  discretion of
                                                                                  the
                            15 calendar      30 calendar       90 calendar
         High                                                                     ISO/designat
                            days             days              days
                                                                                  ed security
                                                                                  representativ
                                                                                  e

                                                                                  At the
                                                                                  discretion of
                                                               180                the
                            30 calendar      90 calendar
         Moderate                                              calendar           ISO/designat
                            days             days
                                                               days               ed security
                                                                                  representativ
                                                                                  e

                                                               At the             At the
                                                               discretion of      discretion of
                            120              180               the                the
         Low                calendar         calendar          ISO/designa        ISO/designat
                            days             days              ted security       ed security
                                                               representati       representativ
                                                               ve                 e

       8. If patching cannot be completed in the timeframe listed in the table above,
          compensating controls must be put in place within the timeframes above and the CISO
          exception process must be followed.
       9. If a patch requires a reboot for installation, the reboot must occur within the timeframes
              outlined above.

 5.0 Compliance
       This standard shall take effect upon publication. Compliance is required with all ITS
       policies and standards. ITS may amend its policies and standards at any time;
       compliance with amended policies and standards is required.
       If compliance with this standard is not feasible or technically possible, or if deviation from

NYS-S15-001                                                                                   Page 4 of 7

       this standard is necessary to support a business function, State Entities shall request an
       exception through the Chief Information Security Office exception process.

 6.0 Definitions of Key Terms
       Except for terms defined in this policy, all terms shall have the meanings found in
       http://www.its.ny.gov/glossary.

 7.0 Contact Information
              Submit all inquiries and requests for future enhancements to the policy owner at:
                                  Chief Information Security Office
                                       Reference: NYS-S15-001
                            NYS Office of Information Technology Services
                                      31 British American Blvd.,
                                           Latham, NY 12110
                                      Telephone: (518) 242-5200
                                       Email: CISO@its.ny.gov

        Statewide technology policies, standards, and guidelines may be found at the following
                                  website: https://its.ny.gov/policies

 8.0 Revision History
      This standard should be reviewed consistent with the requirements set forth in ITS-
      P24-003 Process for Establishing Information Technology Policies, Standards and
      Guidelines.
        Date                Description of Change                       Reviewer
        01/16/2015          Original Standard Release                   Deborah A. Snyder,
                                                                        Deputy Chief
                                                                        Information Security
                                                                        Officer
        02/25/2017          Update to Scope, contact information        Deborah A. Snyder,
                            and rebranding                              Deputy Chief
                                                                        Information Security
                                                                        Officer
        09/11/2018          Scheduled review – minor changes to         Deborah A. Snyder,
                            Authority, Scope, and title of office       Chief Information
                                                                        Security Officer
        05/04/2021          Updated impact and patch timeframes         Karen Sorady, Chief
                            based on Federal guidance.                  Information Security
                                                                        Officer

NYS-S15-001                                                                                 Page 5 of 7

        05/19/2021       Updated Scope language                      Karen Sorady, Chief
                                                                     Information Security
                                                                     Officer
        04/29/2025       Scheduled review – minor changes to         Chris DeSain, Chief
                         document, updated Scope Statement           Information Security
                                                                     Officer

 9.0 Related Documents
      NIST SP 800-40 Rev. 4, Guide to Enterprise Patch Management Planning: Preventive
      Maintenance for Technology

       Common Vulnerability Scoring System

       National Vulnerability Database Vulnerability Severity Rankings

       Department of Homeland Security (DHS) Cybersecurity and Infrastructure Security
       Agency (CISA) Binding Operational Directive (BOD) 19-02

       NYS-S15-002 Vulnerability Management Standard

NYS-S15-001                                                                            Page 6 of 7

        Exhibit 1: SAMPLE SECURITY SOURCES FOR VULNERABILITY/PATCH/THREAT
        INFORMATION
        •   NYS Cyber Security Operations Center (includes feeds from MS-ISAC)
                  •       CISA Known Exploited Vulnerabilities Catalog
                  •       MS-ISAC Advisory
        •   Vendor websites/notification lists
        •   BugTraq
        •   Vulnerability Scanners
        •   Penetration Tests
        •   National Vulnerability Database

NYS-S15-001 – Exhibit 1                                                          Page 7 of 7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
