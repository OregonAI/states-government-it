---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-domain-name
title: Domain Name Policy & Procedure
doc_type: policy
citation: MaineIT Domain Name Policy & Procedure
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/DomainNamePolicyProcedure.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: ad4b0adb4976becf32699119b00545dccd4259d1312c7464a78055bbad699dfd
effective_date: null
source_version: 'Latest Revision: 21 August 2026'
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
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Domain Name Policy & Procedure (MaineIT Domain Name Policy & Procedure)

## At a glance

Instructions for the use of domain names on the Worldwide Web by the Executive Branch and other Maine government entities operating under Maine.Gov, with the workflow for working with the CIO on domain names.

## Full text

                                Maine State Government
                      Dept. of Administrative & Financial Services
                        Office of Information Technology (OIT)

                     Domain Name Policy & Procedure
1.0.   Purpose
1.1.   This document provides the instructions for the use of domain names on the
       Worldwide Web by the Executive Branch of Maine State Government, and Other
       Government Entities in Maine who seek to operate under Maine.Gov. It also includes
       the workflow for interfacing with the CIO re: domain names, and instructions for
       domain sunset and redirection.

2.0.   Background
2.1.   Since 1985, web addresses that end in DotGov (.Gov) has provided the official
       Internet presence for governmental entities in the United States. The U.S. General
       Services Administration (GSA) administers the DotGov namespace.

2.2.   Since 2002, Maine.Gov has been the primary namespace for Maine State
       Government. Over the two-plus decades of its life, Maine.Gov has built a solid brand-
       recognition with the citizens of Maine, visitors to Maine, and the myriad partners of
       Maine State Government. Interacting with the Maine.Gov namespace assures
       citizens, visitors, and partners that they are indeed transacting with an official
       Maine State Government Entity.

2.3.   Maine.Gov is the ‘one-stop shop’ for all online services of Maine State Government. It
       is a readily-identifiable brand, with a unified look and feel, thereby ensuring the
       highest adoption of Maine State Government services. Further, funneling state
       government services through Maine.Gov is also the most scalable and cost-effective
       option. Incidentally, over the years, the Maine.Gov portal has also received
       numerous awards, accolades, and commendations for innovation and usability.

2.4.   Unmanaged use of domain names may result in damage to the reputation of a
       government, as well as regulatory penalties. This includes spoofed and/or hijacked
       sites, inappropriate content, Cybersecurity breaches, privacy violations, expiration,
       squatting, and theft of domains, as well as a general suspicion re: the identity and
       motivation of the party behind such a domain.

3.0.   Definitions
3.1.   Commercial Domain: In the context of this Policy, a catch-all term for all domains
       outside the DotGov namespace.

                                        Page 1 of 9

                           Domain Name Policy & Procedure

3.2.   DNS Mail Exchange (MX) Record: A Domain Name System record that directs email to a
       mail server and indicates how email messages should be routed in accordance with the
       Simple Mail Transfer Protocol (SMTP).

3.3.   Domain: A region of jurisdiction in the Internet for naming assignment. The domain
       name system is hierarchical. The root is the highest level, followed by the top-level
       domain, then the second-level domain, then the third level domain, etc. For the
       domain Dept.Maine.Gov, Dept is the third-level domain, Maine is the second-level
       domain, Gov is the top-level domain, and the "." is the root.

3.4.   InforME: Information Resource of Maine. Defined in 1 MRSA, Chapter 14, §533. 1
       Operates the Maine.Gov portal.

3.5.   Namespace: If one picks a spot in the hierarchical domain tree, then the namespace
       is everything that is taxonomically below it. Thus, Maine.Gov is in the DotGov
       namespace; whereas Megis.Maine.Gov is in the Maine.Gov namespace.

3.6.   Registrar: An entity that can register, and maintain, domain names.

4.0.   Applicability
4.1.   This Policy governs all domain usage by the Executive Branch of Maine State
       Government, including its departments, agencies, and boards, irrespective of any
       hosting and/or branding particularities.

4.2.   This policy also governs the domain usage by Other Government Entities in Maine,
       but only to the extent they seek to operate under the Maine.Gov namespace. These
       Other Government Entities in Maine fall under three broad categories:
       4.2.1. The Maine State Legislature, the Judiciary, the Attorney General, the
              Secretary of State, the State Treasurer, and the Department of Audit;
       4.2.2. Semi-Autonomous State Agencies: An agency created by an act of the Maine
              Legislature, that is not a part of the Legislature, Executive Branch, the
              Judiciary, the Attorney General, the Secretary of State, the State Treasurer,
              and the Department of Audit. Examples: Maine Health Data Organization,
              Maine Public Utilities Commission, Finance Authority of Maine, etc.; and
       4.2.3. The various local, municipal, city, and county governments in Maine.

4.3.   These Other Government Entities in Maine may exercise a choice re: their domain
       usage. They may choose to operate under the Maine.Gov namespace, where such
       usage is subject to this Policy, and they must coordinate with OIT. For any DotGov
       domain outside the Maine.Gov namespace, they coordinate directly with
       DotGov.Gov 2 (GSA), and this Policy does not apply. They may also choose to operate
       in the Commercial namespace, and, again, this Policy does not apply. Purely for the

1 https://legislature.maine.gov/statutes/1/title1sec533.html
2 https://dotgov.gov

                                        Page 2 of 9

                           Domain Name Policy & Procedure

       purpose of illustration, here are some examples from each of these three categories.
       This is not an exhaustive enumeration.

       4.3.1. Examples of Other Government Entities in Maine operating under the
              Maine.Gov namespace:
              •     Legislature.Maine.Gov
              •     Courts.Maine.Gov
              •     Maine.Gov/SOS
              •     MHDO.Maine.Gov
              •     Alna.Maine.Gov
              •     Appleton.Maine.Gov
              •     Cushing.Maine.Gov
              •     Harpswell.Maine.Gov
              •     Union.Maine.Gov
              •     Washington.Maine.gov

       4.3.2. Examples of Other Government Entities in Maine operating directly under the
              DotGov namespace, outside the Maine.Gov namespace:
              •     BangorMaine.gov
              •     PortlandMaine.gov
              •     Waterville-Me.Gov

       4.3.3. Examples of Other Government Entities in Maine operating within the
              Commercial namespace, i.e., outside the DotGov namespace:
              •    TownOfAlbionMaine.com
              •    BiddefordMaine.org
              •    JeffersonMaine.org

4.4.   Native-American Sovereign Nations in Maine coordinate directly with the
       Department of the Interior’s Bureau of Indian Affairs for their domain usage. This
       Policy does not apply.

5.0.   Responsibilities
5.1.   Chief Information Officer (CIO):
       5.1.1. Responsible for maintaining, and enforcing, this Policy. GSA’s Final Rule on
               DotGov 3 (41 CFR Part 102-173, 28 Marcy 2003), grants the authority for
               state-level DotGov domains to the Governor, or the highest-ranking
               information technology official.
       5.1.2. OIT is the Registrar of the all DotGov names under Maine.Gov, as well as any
               second-level DotGov domain used by the Executive Branch.

5.2.   InforME: The Registrar of Commercial Domains.

3 https://www.federalregister.gov/documents/2003/03/28/03-7413/federal-

management-regulation-internet-gov-domain
                                        Page 3 of 9

                            Domain Name Policy & Procedure

5.3.   Management of Executive Branch Entities:
       5.3.1. Adhere to this Policy.
       5.3.2. Defray any initial and recurring domain registration costs associated with
              executing this Policy.
       5.3.3. The Agency Web Coordinator, if present, represents the Agency interests in
              this matter. In the absence of an Agency Web Coordinator, an empowered
              representative of the Commissioner fulfills that role.
       5.3.4. Reach out to Enterprise.Architect@Maine.Gov re: any domain issue as early
              as possible in a program, or initiative’s, lifecycle. Continue to work with the
              Enterprise Architect until the resolution of this matter. The Enterprise
              Architect consults with the CIO, and represents the CIO’s position back to the
              applicant.

5.4.   Management of Other Government Entities seeking to operate under the Maine.Gov
       namespace:
       5.4.1. Adhere to this Policy.
       5.4.2. Defray any initial and recurring domain registration costs associated with
              executing this Policy.
       5.4.3. The applicant representing the Other Government Entity must be
              empowered by their executive management to represent their interests in
              this matter to the CIO. Other than the highest-ranking elected or nominated
              official of the Other Government Entity, other possible applicants include
              their direct deputy/proxy, the Chief Information Officer, the Chief Marketing
              Officer, et al.
       5.4.4. Reach out to Enterprise.Architect@Maine.Gov re: any domain issue as early
              as possible in a program, or initiative’s, lifecycle. Continue to work with the
              Enterprise Architect until the resolution of this matter. The Enterprise
              Architect consults with the CIO, and represents the CIO’s position back to the
              applicant.

6.0.   Directives
6.1.   All entities under the DotGov namespace must comply with the Federal
       requirements (the full list is available at DotGov.Gov). The following two
       requirements deserve special mention:
       6.1.1. Advertisements: A Maine.Gov domain may not be used to advertise private
               individuals, firms, or corporations, or to imply in any manner that the
               government favors any specific commercial product or service.
       6.1.2. Campaign Information: No campaigning can be done with DotGov domains.
               The Maine.Gov site may not be directly linked to, or refer to, sites created or
               operated by a campaign, or any campaign entity.

6.2.   Names requested must comply with the following two Suitability criteria,
       adjudicated by the CIO:

                                         Page 4 of 9

                            Domain Name Policy & Procedure

       6.2.1. Applicability: Is the requested domain intrinsically related to the core
              mission of the requesting entity? Any domain name that poses a potential for
              conflict with another government entity is not likely to be approved.
       6.2.2. Impact: Maine.Gov is intended as a positive space for all parties to partake of
              Maine State Government services. Names that detract from the brand’s
              appeal are not likely to be approved.

6.3.   By default, domains are intended to serve long-term, essential business functions of
       a government entity. However, under exceptional circumstances, the CIO may
       entertain domain requests for limited-time, ad-hoc campaigns, or projects, or
       events. Should such be the case, applicants must furnish the appropriate
       justification.

6.4.   Domain Names must comply with the following Construction criteria:
       6.4.1. No blank space
       6.4.2. Only letters, numbers, and dashes
       6.4.3. A domain name cannot start or end with a dash.
       6.4.4. A domain name will be as short as reasonably possible.
       6.4.5. A domain name will be easily understood by the citizens, visitors, and
              partners of Maine State Government.
       6.4.6. Unless widely understood, a domain name will avoid the use of abbreviations
              (acronyms and initialisms) as much as possible.
       6.4.7. A domain name will be based upon the most generally accepted meaning of
              the specific words that make up the requested name.

6.5.   The second level domain Maine.Gov is intended exclusively for the State Executive
       Branch. Executive Branch Entities must align their domain names according to the
       following format:
       6.5.1. Path Level: Conforms to one of two forms. Maine.Gov/Dept/Service is
              targeted at the department’s constituents and/or business partners, but not
              necessarily of interest to the citizenry at-large. Whereas, Maine.Gov/Service
              is targeted primarily at the interests of the citizenry at-large. The Service
              name is subject to the Suitability and Construction criteria stated above. For
              further details, please contact the Enterprise Architect.
       6.5.2. Third Level or Higher: Occasionally, for technical reasons, a server (but not a
              branding URL) must be assigned a unique name. In such cases, the name is
              either Server.Dept.Maine.Gov, or Server.Maine.Gov. The branding URL still
              conforms to the previous item, but redirects to the server in this item.
       6.5.3. Networking Infrastructure: The name of a networking equipment is
              Device.Net.Maine.Gov.
       6.5.4. Applications hosted by OIT: The naming for applications hosted by OIT
              conforms to one of these two forms: Gateway.Maine.Gov/App or
              Portal.Maine.Gov/App.
       6.5.5. State Secure Public Portal: The State secure public portal is branded as
              Public.Maine.Gov.

                                        Page 5 of 9

                                     Domain Name Policy & Procedure

           6.5.6. Other-Party Mail Relay Services: For other-party mail-relay services, the
                  format of the DNS MX record is mail-#.maine.gov, where the # is a mapping
                  of that other-party service. The corresponding fully qualified email format is
                  established in section 5.1.5. of the Global Address List Standard 4.

6.6.       Use of Commercial Domains by Executive Branch Entities must be avoided in all but
           exceptional circumstance. The CIO demands significant justification to permit such
           usage.
           6.6.1. Historically, the prime driver for a Commercial Domain by the Executive
                  Branch has been the perception in certain quarters that non-State branding
                  would improve acceptance of State services by certain cohorts, or
                  demographics, or interest groups. However, empirical evidence refutes such
                  a perception. All available traffic analysis indicates that citizens, visitors, and
                  partners overwhelmingly use Maine.Gov to consume State services.
           6.6.2. Because they are leased rather than purchased, Commercial Domains are
                  subject to squatting and theft. Therefore, the following best-practices must
                  be followed:
                  6.6.1.1. Registrations and renewals of all Commercial Domains must be
                           performed by InforME.
                  6.6.1.2. Leases must be acquired for a minimum of three years.
           6.6.2. If a Commercial Domain is approved, Executive Branch entities are strongly
                  encouraged to redirect, or host an alias, to a Maine.Gov-derived site.
           6.6.3. The remaining term of subscription to a Commercial Domain must never fall
                  below one year, unless the domain is intended to be retired within that year.
           6.6.4. The usage of all Commercial Domains must be re-evaluated at each renewal
                  via the waiver process.

6.7.       All the stipulations enumerated above for Commercial Domains by the Executive
           Branch also applies toward any second-level DotGov domain other than Maine.Gov.

6.8.       Domains for Other Government Entities in Maine operating under the Maine.Gov
           namespace are subject to the following rules of Construction:
           6.8.1. The third-level domain name must uniquely represent the name of the entity.
           6.8.2. For cities and towns, the most obvious choice is their own names.
                  Abbreviations are discouraged for city and town names. At the discretion of
                  the relevant local authority, the word “city” or “town” may be included as
                  well.
           6.8.3. In case a county shares the same name as a city within the State, the third-
                  level domain of the county must explicitly include the word “county” within
                  the name.
           6.8.4. Abbreviations are acceptable for the third-level domain names of Semi-
                  Autonomous State Agencies, as long as such abbreviations are widely
                  understood by the citizenry. An example is MHDO for the Maine Health Data

4
    https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/GALStandard.pdf

                                                    Page 6 of 9

                            Domain Name Policy & Procedure

              Organization. Any abbreviation that precipitates ambiguity or confusion is
              not likely to be approved.
       6.8.5. By default, only one third-level domain may be requested per entity. Which
              means that, any administrative division, or program, or initiative, under that
              entity must be accommodated by extending the URL to the right. For example
              City.Maine.Gov/Library. This is as opposed to the City requesting both
              City.Maine.Gov and CityLibrary.Maine.Gov. However, the CIO may entertain
              exceptions for compelling business reasons.

6.9.   While each domain engagement is unique, in general, a domain name application
       includes the following elements. While not all the information may be available at
       the inception of a request, it still remains in the best interests of the applicant to
       include as much of this information as possible while reaching out to the Enterprise
       Architect.
       6.9.1. Requested domain name
       6.9.2. Purpose of the domain, including, if appropriate, an explanation why
              Maine.gov fails to serve this purpose
       6.9.3. Date needed by
       6.9.4. Projected lifespan of the domain
       6.9.5. Server address to which the domain name will point
       6.9.6. Any special instructions, such as virtual domain, aliasing etc.

6.10. Sometimes, it is necessary to cite or embed external links within a Maine State
      Government webpage. This requirement can be subdivided into two categories,
      enumerated below.
      6.10.1. Sponsored External Links: This is where the Maine State Government entity
              has deliberately selected a vendor/partner to provide a specific service,
              most likely through a contract, and endorses said vendor/partner for that
              specific service. In such a case, the destination service/site of the trusted
              partner must be annotated in a clear and conspicuous manner with the text,
              “Trusted Partner of the Maine State Government,” and contain a bi-
              directional link to the Maine.gov homepage.
      6.10.2. Informational External Link: This is where the Maine State Government
              entity provides an external link purely for informational purposes. There
              does not exist any contractual arrangement between the Maine State
              Government entity and the external party. Neither is there any implication
              of endorsement of that external party by Maine State Government. In such a
              case, the link must be annotated with the text, “Link purely for informational
              purposes. The department (or, the State of Maine) does not vouch for the
              contents.”

6.11. When a migration of a domain is necessary, the three-phase process outlined below
      will be followed.
      6.11.1. The first phase is primarily about migrating the intellectual assets, and
               consists of both technical and administrative tasks:
               6.11.1.1. Cease all public advertisement of the retiring URL.
                                        Page 7 of 9

                            Domain Name Policy & Procedure

               6.11.1.2. Implement a physical migration (or porting) of the intellectual
                         assets (including source code, documents, media contents, etc.)
                         from the retiring hosting underlayment to the target hosting
                         underlayment.
       6.11.2. The second phase is about creating a transparent alias for the retiring URL,
               and is exclusively technical:
               6.11.2.1. Switch the retiring URL to resolve to the target URL. Thus, during
                         this second phase, the retiring URL shall reduce to a transparent
                         alias for the target URL. This must be done in a manner to retain
                         the search engine ranking of the legacy URL.
              6.11.2.2. It is reasonable to expect technical issues to surface during this
                        phase, which must be addressed on a case-by-case basis. At the end
                        of the second phase, there shall not exist any outstanding technical
                        issues in the performance of the underlying target URL, even
                        though visitors and users to the retiring site will still be afforded
                        the illusion of the retiring URL.
       6.11.3. The third phase is mostly about constituent outreach, and, is, therefore,
               mostly administrative:
               6.11.3.1. Withdraw the automated redirection to the target URL in favor of
                         an explicit end-of-life notification on the legacy site.
               6.11.3.2. This end-of-life notice shall:
                         6.11.3.2.1. Request the visitor to change their bookmarks and
                                       reference links;
                         6.11.3.2.2. Prominently display the projected expiration date;
                                       and
                         6.11.3.2.3 Include an explicit link to the target URL that the
                                       visitor will click.
              6.11.3.3. The agency shall notify its constituents of the projected expiration
                         of the legacy URL via all the distribution channels that were used
                         to publicize that legacy URL over its entire lifetime. This may
                         include newspapers, billboards, radio, television, etc.
              6.11.3.4. This third phase is used to build up the search engine ranking of
                         the new URL.
              6.11.3.5. After the expiration date, dismount the legacy site. At this point, it
                         is actually desirable for users to receive a 404 Error message
                         should they attempt to reach the legacy URL.
       6.11.4. The exact time durations of the three phases will vary depending upon
               Agency business constraints and preferences, as well as the technical
               challenges of the migration.

7.     Document Information
7.6.   Initial Issue Date: 1 March 2007
7.7.   Latest Revision: 21 August 2026
7.8.   Point of Contact: PolicyTeam.OIT@Maine.Gov
7.9.   Approved By: Chief Information Officer, OIT

                                         Page 8 of 9

                           Domain Name Policy & Procedure

7.10. Legal Citation: Title 5, Chapter 163: Office of Information Technology 5
7.11. Waiver Process: Waiver Policy 6

5 http://legislature.maine.gov/statutes/5/title5ch163sec0.html
6 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/waiver.pdf

                                        Page 9 of 9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
