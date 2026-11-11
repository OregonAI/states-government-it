---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-nys-s15-002
title: Vulnerability Management
doc_type: standard
citation: NYS ITS Standard NYS-S15-002
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/vulnerability-management
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 2d785c815a0bdd847178f10173961c07b74efff9e281dbb44bf67a41d8c7291a
effective_date: null
source_version: 'Updated: 02/29/2024'
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

# Vulnerability Management (NYS ITS Standard NYS-S15-002)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Cybersecurity, Statewide Policies' on the listing. The listing prints original publication 01/16/2015 and last modified 02/29/2024.

## Full text

                                               State Capitol P.O. Box 2062
                                                 Albany, NY 12220-0062
                                                     www.its.ny.gov

          New York State
 Information Technology Standard                          No: NYS-S15-002

                 IT Standard:                             Updated: 02/29/2024

                                                          Issued By: NYS Office of Information
           Vulnerability                                  Technology Services
           Management                                     Owner: Chief Information Security Office

1.0 Purpose and Benefits
   Vulnerability scanning is a process by which vulnerabilities are identified. Vulnerability
   Management (VM) is a process by which the vulnerabilities identified through scanning
   are tracked, evaluated, prioritized, and managed until the vulnerabilities are remediated
   or otherwise appropriately resolved. VM ensures that appropriate actions are taken to
   reduce the risk of compromise to the confidentiality, integrity, and availability of
   Information Technology (IT) Resources.
   New York State (NYS) utilizes manual and automated tools to scan systems, computing
   and network devices, web applications, application code and application programming
   interfaces (APIs). The results of these scans help inform management and system
   administrators of known and potential vulnerabilities.

2.0 Authority
   Section 103(10) of the State Technology Law provides the Office of Information
   Technology Services (ITS) with the authority to establish statewide technology policies,
   including technology and security standards. Section 2 of Executive Order No. 117 1,
   issued January 2002, provides the State Chief Information Officer with the authority to
   oversee, direct and coordinate the establishment of information technology policies,
   protocols and standards for State government, including hardware, software, security and

   1
    All references to Executive Order 117 refer to that which was originally issued by Governor George E. Pataki
   on January 28, 2002 and continued by Executive Order 5 issued by Governor Eliot Spitzer on January 1, 2007,
   Executive Order 9 issued by Governor David A. Patterson on June 18, 2008, Executive Order 2 issued by
   Governor Andrew M. Cuomo on January 1, 2011 and Executive Order 6 issued by Governor Kathy Hochul on
   October 8, 2021.

   business re-engineering. Details regarding this authority can be found in NYS ITS Policy,
   NYS-P08-002 Authority to Establish State Enterprise Information Technology (IT) Policy,
   Standards and Guidelines.

3.0 Scope
   This standard applies to all “State Entities” (SE), defined as “State Government” in
   Executive Order 117 or “State Agencies” as defined in Section 101 of the State
   Technology Law. This includes employees and all third parties (such as local
   governments, consultants, vendors, and contractors) that use or access any Information
   Technology (IT) Resource for which the SE or ITS has administrative responsibility,
   including systems managed or hosted by third parties on behalf of the SE or ITS. While
   an SE may adopt a different policy/standard, it must include the requirements set forth in
   this one. Where a conflict exists between this policy/standard and an SE’s
   policy/standard, the more restrictive policy will take precedence.
   This standard applies to all systems, web applications, source code, and APIs developed,
   maintained, or operated by, or on behalf of, all SEs.

4.0 Information Statement
   All systems, source code, and web applications must be scanned for vulnerabilities per
   the NYS-P03-002 Information Security Policy. In addition, each must be inventoried and
   have an individual or group assigned responsibility for maintenance and administration.
   4.1    Types of Scans
   The type of vulnerability scan appropriate for a given IT Resource depends on its type
   (i.e., hardware, software, source code, API) and location (i.e., internal or external to the
   SE’s network). The table below lists the types of vulnerability scans required by this
   standard.
   4
     Type                                    Description
     External Infrastructure Scan            Scans of the perimeter of SE networks or any
                                             externally available hosted infrastructure to
                                             identify potential vulnerabilities in Internet
                                             accessible IT infrastructure.
     Internal Infrastructure                 Scans of IT infrastructure on SE protected
     Scan                                    networks or any hosted infrastructure to
                                             identify potential vulnerabilities.
     Unauthenticated Web Application         Unauthenticated scans of SE externally
     Scan                                    facing production web applications identify
                                             security vulnerabilities that can be found
                                             without authenticated credentials.

   NYS-S15-002
                                                                                   Page 2 of 8

 Type                                      Description
 Authenticated Web Application             Authenticated scans of SE web applications
 Scan                                      identify security vulnerabilities for each level
                                           of access available within the web
                                           application.
 Application Source Code Analysis          Scans of application source code run during
                                           development, or when necessary for change
                                           control, to identify problems in the code that
                                           could cause potential vulnerabilities.

4.2    Scanning
SEs are responsible for confirming that vulnerability scans are conducted and
successfully completed. SEs must use a scanning tool approved by the SE’s
ISO/designated security representative. Approved scanning tools must be able to provide
remediation suggestions and be able to associate a severity value to each vulnerability
discovered based on the relative impact of the vulnerability to the affected IT Resource.
Scan reports are classified with a minimum of moderate confidentiality and moderate
integrity, per the NYS-S14-002 Information Classification Standard, and should be
protected as such.
Network and system administrators must provide sufficient access and configuration
information to allow the approved vulnerability scanning tool to scan all services provided
by the system. No devices connected to the network shall be specifically configured to
block approved vulnerability scanning from an authorized scanning tool.
Scans must be performed within the system development life cycle (see NYS-S13-001
SSDLC Standard) while in pre-production environments, when deployed to the production
environment, and periodically thereafter as specified below:
4.2.1 Pre-production scans occur prior to the move of the system, source code, or web
      application to the production environment:

              •   All systems must undergo an authenticated internal infrastructure scan,
                  where technically feasible, before being deployed to the production
                  environment. Any infrastructure vulnerability discovered must be
                  remediated, determined to be a false positive, or deemed an insignificant
                  risk by the SE ISO/designated security representative prior to the system
                  being deployed for intended use.
              •   When source code is available, scan of the source code should be
                  conducted throughout the development process. Applications must
                  undergo source code scanning before the application moves to
                  production and between environments if there has been a change to
                  source code.

NYS-S15-002
                                                                                 Page 3 of 8

              •   Web applications that require authentication must undergo an
                  authenticated scan before being deployed to the production
                  environment or into an environment that is externally accessible. When
                  authentication is required to access the application, scans must run with
                  authenticated access at each access level (e.g., user, admin) supported
                  by the application, except where limitations in the scanning tool and/or
                  application prevent authenticated scanning, in order to determine if
                  vulnerabilities exist in the different functionality of the application
                  accessible by each access level. Any web application vulnerability
                  discovered must be remediated or determined to be a false positive or
                  insignificant risk by the SE ISO/designated security representative prior
                  to the web application being placed into the production environment.
              • Any system, source code, or web application deployed to its production
                  environment with un-remediated vulnerabilities must have a formal
                  remediation plan and the documented approval of the SE executive
                  responsible for risk management, or their designee.
4.2.2 Implementation scans occur the first time a system or web application is moved to
      its production environment:

              •   Systems must be scanned immediately upon being placed into the
                  production environment with an authenticated internal infrastructure
                  scan, where technically feasible. If the system is accessible from the
                  Internet or an external network, then the system must be scanned with
                  an external infrastructure scan.

              •   Web applications must be scanned within the first month of being placed
                  into the production environment. An authenticated web application scan
                  is required if feasible, but at minimum an unauthenticated web
                  application scan is required. Sensitivity and criticality of the application
                  must be considered when determining the schedule for the initial
                  implementation scan.
4.2.3 Recurring Scans: After the initial scan in the production environment, the frequency
      of scans must occur according to the system or application’s risk rating (see Table
      2).

              •   When performing internal infrastructure scans on systems built using a
                  shared image, such as workstations, scans may be run on a sampling
                  of systems, but the sample set must vary from scan to scan.

              •   Web applications in production are required to undergo recurring scans.
                  At minimum, web applications in production are required to undergo
                  recurring unauthenticated application scans.

NYS-S15-002
                                                                                  Page 4 of 8

              •   All vulnerabilities found during scans must be addressed as per the
                  remediation section below.
4.3     Determine Risk Rating and Frequency of Scans
The risk that vulnerabilities pose to systems and applications is based on the likelihood
of a vulnerability being exploited and the impact if the confidentiality, integrity, or
availability of the SE’s information assets were compromised. The likelihood of a
vulnerability being exploited increases in direct relation to the systems or application’s
accessibility from other systems.
The impact of a vulnerability to a SE’s information asset is based on that asset’s
information classification (see NYS-S14-002 Information Classification Standard). The
SE must consider the impact (i.e., high, moderate, or low) of a compromise to the
confidentiality, integrity, and availability of that asset. The highest impact level identified
must be used when determining the overall risk rating, per the table below.

                                   Table 2: RISK RATING

                                                       Exposure
 Impact
                        Systems with no         Systems with network        System that is
 (Confidentiality,      network                 connectivity to             publicly
 Integrity,             connectivity to         production data (not        available from
 Availability)          production data         Internet facing)            the Internet

 High                   Moderate                High                        High

 Moderate               Low                     Moderate                    High

 Low                    Low                     Low                         High

The minimum frequency of scans is dependent on the risk rating. All systems and
applications that are publicly available from the Internet are considered High risk
regardless of their impact rating because they represent a potential entryway to an SE’s
internal network. Systems and applications without a risk rating must be scanned as if
they had a risk rating of “High” until they are rated.

                          TABLE 3: FREQUENCY OF SCANS

                  Risk Rating                                    Frequency

                                   Infrastructure scans

NYS-S15-002
                                                                                   Page 5 of 8

  High                                            Monthly

  Moderate                                        Quarterly

  Low                                             Semi-annually

                                 Web Application Scans

  High                                            Monthly or after significant change

  Moderate                                        Quarterly

  Low                                             Semi-Annually

 4.4     Remediation
 Vulnerabilities discovered during scans must be remediated based on the systems or
 application’s risk rating (see Table 2) and vulnerability severity identified by the scanning
 tool as per the table below.

                              TABLE 4: REMEDIATION TIMEFRAMES
  Risk Rating                              Vulnerability Severity
(from Table 2)      Critical      High           Moderate               Low
                                                                 At the discretion of
                  Resolved in  Resolved in                             the SE
                                              Resolved in 90
       High       15 calendar  30 calendar                        ISO/designated
                                              calendar days
                     days         days                                 security
                                                                   representative
                                                                 At the discretion of
                  Resolved in  Resolved in                             the SE
                                             Resolved in 180
  Moderate        30 calendar  90 calendar                        ISO/designated
                                              calendar days
                     days         days                                 security
                                                                   representative
                                            At the discretion of At the discretion of
                  Resolved in  Resolved in        the SE               the SE
       Low       120 calendar 180 calendar   ISO/designated       ISO/designated
                     days         days            security             security
                                              representative       representative
 Individuals performing vulnerability scans are required to notify the SE ISO/designated
 security representative within an expedited timeframe upon i scan completion of new
 vulnerabilities discovered and at least monthly of un-remediated vulnerabilities on
 systems or applications that are running in production. Validation testing must be done to
 verify the remediation was successful.

 NYS-S15-002
                                                                                  Page 6 of 8

   SE ISOs/designated security representatives must notify SE management of any un-
   remediated vulnerabilities not addressed in the timeframes prescribed in this standard.
   That risk must then be communicated to the appropriate parties.

5.0 Compliance
   This standard shall take effect upon publication. Compliance is required with all ITS
   policies and standards. ITS may amend its policies and standards at any time; compliance
   with amended policies and standards is required.
   If compliance with this standard is not feasible or technically possible, or if deviation from
   this policy is necessary to support a business function, State Entities shall request an
   exception through the Chief Information Security Office exception process.

6.0 Definitions of Key Terms
   Except for terms defined in this policy, all terms shall have the meanings found in
   http://www.its.ny.gov/glossary.

7.0 Contact Information
      Submit all inquiries and requests for future enhancements to the policy owner at:
                           Chief Information Security Office
                                Reference: NYS-S15-002
                     NYS Office of Information Technology Services
                         1220 Washington Avenue, Building 5
                                    Albany, NY 12242
                               Telephone: (518) 242-5200
                                Email: CISO@its.ny.gov

       Statewide technology policies, standards, and guidelines may be found at the
                       following website: https://its.ny.gov/policies

8.0 Revision History
   This policy document should be reviewed consistent with the requirements set forth in
   NYS-P08-002 Authority to Establish State Enterprise Information Technology (IT)
   Policy, Standards and Guidelines.

    Date              Description of Change                               Reviewer
    01/16/2015        Original Standard Issued                            Deborah A.
                                                                          Snyder, Deputy
                                                                          Chief Information
                                                                          Security Officer

   NYS-S15-002
                                                                                     Page 7 of 8

    Date            Description of Change                         Reviewer
    03/10/2017      Update to Scope, contact information and      Deborah A.
                    rebranding                                    Snyder, Deputy
                                                                  Chief Information
                                                                  Security Officer
    05/04/2021      Updated remediation timelines, Scope and      Karen Sorady,
                    Authority, and minor wording changes          Chief Information
                                                                  Security Officer
    05/19/2021      Updated Scope language                        Karen Sorady,
                                                                  Chief Information
                                                                  Security Officer
    02/29/2024      Updated Purpose and Benefits language, other Chris DeSain,
                    re-wording throughout Section 4.0 Information Chief Information
                    Statement                                     Security Officer

9.0 Related Documents
   NYS-S15-001 Patch Management Standard
   NYS-S14-002 Information Classification Standard
   National Institute of Standards and Technology, Special Publication 800-40, Guide to
   Enterprise Patch Management Technologies
   US Department of Homeland Security Binding Operational Directive 19-02:
   Vulnerability Remediation Requirements for Internet-Accessible Systems

   NYS-S15-002
                                                                               Page 8 of 8

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
