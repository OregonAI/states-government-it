---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-mgmt-01-01-g
title: Application Guidelines
doc_type: policy
citation: WaTech Guideline MGMT-01-01-G
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2024-02/Standard%20Application%20Guidelines%20Update%202023.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 4f2ea19a87ac19afee451c5ca51fb633f0b25fd82ca7d3e4d0595a2c9870eb16
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
- oversight
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Application Guidelines (WaTech Guideline MGMT-01-01-G)

## At a glance

Item of the WaTech policy library, chapter '2. Management & Governance' (listed as type Guidelines). Listed at https://watech.wa.gov/policies/application-guidelines.

## Full text

MGMT-01-01-G Version 7.1                                                                           Replaces:
State CIO Adopted: June 8, 2023                                                  112.10 Guidelines (Version 6)
TSB Approved: June 8, 2023                                                                    August 1, 2022
Sunset Review: June 8, 2026

                                      APPLICATION GUIDELINES

 See Also:
 RCW 43.105.054 OCIO Governance
 RCW 43.105.205 (3) Higher Ed
 RCW 43.105.020 (22) “State agency”

 Application Definition:
 The definition of ‘Application’ we are electing to follow is specific to the state of
 Washington and was approved through WaTech’s IT Enterprise Governance
 Framework.
 Application – A computer program or solution designed to fulfill one or more
 business functions. They manage data to allow lines of business, IT departments,
 and/or external business customers/partners to provide a service, complete a task,
 connect with others, execute a process, or deliver an outcome. They may be custom
 developed, open source or purchased such as a commercial off the shelf (COTS),
 Software as a Service (SaaS), or Platform as a Service (PaaS).
 Application Guidelines:
 1. List applications as required by Technology Portfolio Foundation 112
    except for:
               a. Social media applications, unless used for data collections such
                  as surveys.
 2. Websites are our first and most vital opportunity to reach those who
    use agency services. How to register agency websites, webpages and
    related content:
               a. Agencies should list each website as an individual entry. Input the
                  website URL as the application name, the content management system
                  (CMS) as the key technology, and the hosting platform as the cloud
                  service provider.
 3. How to register IT applications used by the IT department. All applications
    used to deliver services should be registered on your application inventory. Since
    IT applications are used by IT departments to deliver services to your customers,
    include utility applications and web-based management consoles used to
    support IT services such as network, security, servers, storage, etc.
 4. How to register Platform as a service (PaaS) or low-code applications. Include
    distinct rows for the PaaS solution and the applications developed on a PaaS or
                                                                                               1

   low- code platform.
   Example 1: an agency has developed two applications on a Salesforce platform.
        a. The agency should include an entry for Salesforce. Input “PaaS” as
            the Type of Application within the inventory. Input “Salesforce” as
            the Manufacturer/Vendor & Cloud Service Provider.
         b. The agency should also include 2 entries for the individual
            applications that were configured on Salesforce. Input “Application
            on PaaS” as the Type of Application. Input “Salesforce” as the Key
            Technology, Manufacturer/Vendor & Cloud Service Provider.
   Example 2: an agency within the M365 enterprise shared tenant has developed
   two applications with Microsoft Power Apps.
         a. The agency should include an entry for “Microsoft 365 – G5" and
            follow guideline #6 below.
         b. The agency should also include 2 entries for the individual
            applications that were configured on Power Apps. Input “Application
            on PaaS” as the Type of Application. Input “M365 Power Apps” as the
            Key Technology, “Microsoft” as the Manufacturer/Vendor, and
            “WaTech” as the Cloud Service Provider.
5. How to register large non-PaaS applications that have a collection of
   components or modules. It is recommended that agencies report at the
   highest level or parent application. Agencies have discretion to optionally
   identify the associated components or child applications to further support
   portfolio management or refine their Technology Business Management
   (TBM) business costing.
   For agencies wanting to report modules or components of large applications:
         a. Include distinct rows for the parent application and each module
            or component.
         b. It is recommended to use a naming convention to easily identify
            all application entries. Ex: “Family Abbrev. – Module 1 name”,
            “Family Abbrev. – Module 2 name”, etc.
         c. For each module or component, use the “Relationship to other
            Apps” column to identify the parent or application family.
6. How to register desktop productivity software:
         a. Agencies that have moved to Microsoft 365 G5 licensing need to only
            list the productivity software one time in their inventory. Agencies
            should list a single entry for “Microsoft 365 – G5” and still include the
            version information. Input “SaaS” as the Type of Application within the
            inventory. Note: Agencies in the shared tenant are at G5 licensing; G5

                                                                                        2

             includes Office Pro Plus applications such as Excel, Word, Outlook,
             Power BI, Intune, SharePoint, Teams, Teams Telephony, etc.
          b. Agencies should list Microsoft add-on services that require an
             additional license (not part of the G5 license) such as Project,
             Dynamics, and Visio, as separate line items in their inventory and
             include the version information.
          c. Agencies that still have Microsoft on-premises applications should
             include separate line items in their inventory for each software. Ex:
             Microsoft Project Pro 2013, Microsoft Visio Pro 2016, Microsoft SQL
             Server, Microsoft Server 2016, Microsoft Access. The agency should
             still include the version information.
7. How to register enterprise central service applications such as AFRS, HRMS,
   TEMS, etc.
          a. Agencies owning enterprise central service applications will need to
             include the application in their agency portfolio submittal. Ex: The office
             of financial management (OFM) owns the enterprise application HRMS
             and should list it in their inventory.
          b. Agencies using the enterprise central service applications do not need
             to list the application in their portfolio. Ex: The remaining agencies
             using the enterprise application HRMS do not need to list it in their
             inventory.
8. Associating infrastructure items to applications is a foundational step
   to portfolio management and establishing/maintaining a configuration
   management database (CMDB).
          a. Agencies are asked to list all infrastructure unique identifiers associated
             with the application. This is accomplished by entering each
             infrastructure unique identifier in the “Relationship to other infrastructure
             items” columns.
          b. If the application is associated with more than 20 infrastructure
             items, agencies are asked to add additional columns to
             accommodate.

9. Automating Decision-Making System (ADS) Definition Guidance:

          a. Document link to help determine if a system in your application
             inventory is an Automated Decision-Making System (ADS).

10. How long to keep retired applications in your inventory. Agencies only need to
    include retired applications on their inventory for one (1) year following the
    retirement date as noted in your inventory.

                                                                                           3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
