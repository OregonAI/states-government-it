---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-hosting-housing
title: Hosting & Housing Policy
doc_type: policy
citation: MaineIT Hosting & Housing Policy
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/HostingHousingPolicy.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 0d1382edb0e9b51112856e1a01ed53d6ff9dea97cefc9aa3e2195fa0b959fd13
effective_date: null
source_version: 'Latest Revision Date: 11 November 2020'
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

# Hosting & Housing Policy (MaineIT Hosting & Housing Policy)

## At a glance

Explains the two ways of using OIT data centers (housing and hosting) and the difference between them.

## Full text

                                  Maine State Government
                        Dept. of Administrative & Financial Services
                          Office of Information Technology (OIT)

                                 Hosting & Housing Policy
1.0.   Purpose
1.1.   OIT offers two distinct flavors of utilizing its data centers: OIT Housing and OIT Hosting. This
       Policy explains the two flavors, and enumerates their difference. A visual representation of
       the network flow is included at the end for further clarification.

2.0.   Definitions
2.1.   Information Assets: The full spectrum of all I.T. products, including business
       applications, system software, development tools, utilities, appliances, etc.

2.2.   OIT Hosting: Full-service, horizontal infrastructure platforms (e.g., Oracle database,
       Microsoft SQL database, Oracle Fusion Java Middleware, Microsoft Internet
       Information Services, VMWare ESxi, etc.) provided by OIT. The implementation of
       OIT Hosting is split between two OIT divisions.

2.3.   OIT Housing: Equipment that resides in an OIT data center, where OIT provides the
       physical security, uninterrupted electricity, climate control, rack space, and Internet
       connectivity (including network segmentation). The OIT Housing Vendor provides
       everything else.

2.4.   OIT Housing Vendor: Commercial party that provides everything else under OIT
       Housing that OIT does not provide.

2.5.   OIT Product Manager: OIT position that provides the single point-of-accountability to the
       customer re: an Information Asset.

3.0.   Applicability
3.1.   This policy applies to:
       3.1.1. All State of Maine personnel, both employees and contractors;
       3.1.2. Executive Branch Information Assets, irrespective of hosting location; and
       3.1.3. Information assets from other Maine State Government branches that use the
              State network.

3.2.   Agency business stakeholders considering OIT Housing must carefully understand the
       division of responsibility between OIT, and the OIT Housing Vendor.

                                            Page 1 of 4

                                  Hosting & Housing Policy

4.0.   Responsibilities
4.1.   OIT: OIT’s responsibility is minimal under OIT Housing, and maximal under OIT
       Hosting.

       4.1.1. For OIT Housing, OIT is only responsible for the following five enumerated
              items, and nothing else:
              4.1.1.1. Physical Security;
              4.1.1.2. Uninterrupted Electricity;
              4.1.1.3.   Climate Control;
              4.1.1.4.   Rack Space; and
              4.1.1.5.   Internet Connectivity (including Network Segmentation).

       4.1.2. For OIT Hosting, in addition to the five items listed above, OIT is also
              responsible for:
              4.1.2.1. Equipment provisioning and maintenance, including patching and
                        administration;
              4.1.2.2.  Equipment life-cycle management, including end-of-life replacement;
              4.1.2.3.  Internal connectivity amongst equipment, as well as external Internet
                        connectivity to ensure agreed-upon performance benchmarks;
              4.1.2.4. Periodic Cybersecurity vulnerability scans, and associated remediation;
              4.1.2.5. Remediations resulting from other-party audit findings;
              4.1.2.6. Policy-driven Change Management;
              4.1.2.7. Policy-driven Incident Management and Response;
              4.1.2.8. Support beyond the scheduled workweek business hours, unless
                        explicitly exempted by other OIT service-level terms and conditions;
              4.1.2.9. Backup & Restoration, and associated Liability;
              4.1.2.10. Business Continuity Planning, Disaster Recovery, and associated Liability;
                        and
              4.1.2.11. Cybersecurity & Privacy, and associated Liability.

4.2.   OIT Product Manager: Advises the Agency business customer re: the distinction between
       OIT Hosting and OIT Housing, as it pertains to the particular Information Asset that they are
       accountable for.

4.3.   OIT Housing Vendor: Responsible for everything beyond the five enumerated items
       provided by OIT, including the following, but not limited to:
       4.3.1. Equipment provisioning and maintenance, including patching and administration;
       4.3.2. Equipment life-cycle management, including end-of life replacement;
       4.3.3. Internal connectivity amongst Housed equipment;
       4.3.4. Periodic Cybersecurity vulnerability scans, and associated remediation;
       4.3.5. Remediations resulting from other-party audit findings;
       4.3.6. Policy-driven Change Management;
       4.3.7. Policy-driven Incident Management and Response;
       4.3.8. Backup & Restoration, and associated Liability;
       4.3.9. Business Continuity Planning, Disaster Recovery, and associated Liability;
       4.3.10. Cybersecurity & Privacy, and associated Liability.

                                           Page 2 of 4

                                  Hosting & Housing Policy

5.0.   Directives
5.1.   The OIT Housing Vendor must follow industry best practices in Cybersecurity & Privacy,
       and minimize any risk to the State network.

5.2.   The OIT Housing Vendor must make Housed equipment available for periodic OIT
       health-checks, to ensure said equipment does not pose a threat to the State network.
       Should any discrepancy be found, the OIT Housing Vendor must remediate such
       discrepancy per OIT instructions, within a timeframe specified by OIT.

5.3.   Should such remediation not be undertaken per OIT instructions, within the specified
       timeframe, then OIT reserves the right to shut down the Housed equipment, and
       terminate the Housing contract with the OIT Housing Vendor.

5.4.   Any configuration change to Housed equipment must be made according to the OIT Change
       Management Policy1. Beyond change management, OIT Housing is considered Remote
       Hosting, and is subject to the Remote Hosting Policy2.

5.5.   All access to Housed equipment by the OIT Housing Vendor must be coordinated through
       the OIT Data Center Director. OIT Housing is best suited for lights-out operations.
       Frequent, unplanned access requests from the OIT Hosting Vendor cannot be
       accommodated.

6.0.   Document Information
6.1.   Initial Issue Date: 11 December 2004
6.2.   Latest Revision Date: 11 November 2020
6.3.   Point of Contact: PolicyTeam.OIT@Maine.Gov
6.4.   Approved By: Chief Information Officer, OIT
6.5.   Legal Citation: Title 5, Chapter 163: Office of Information Technology 3
6.6.   Waiver Process: Waiver Policy4

1 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/change-management-

policy.pdf
2
  https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/remote-hosting-
policy.pdf
3 https://legislature.maine.gov/statutes/5/title5ch163sec0.html
4 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/waiver.pdf

                                          Page 3 of 4

Hosting & Housing Policy

      Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
