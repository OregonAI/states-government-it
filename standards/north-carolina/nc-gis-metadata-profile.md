---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-gis-metadata-profile
title: State and Local Government GIS Metadata Profile
doc_type: standard
citation: 'NC GIS standard: State and Local Government GIS Metadata Profile'
authority_level: ''
issuing_body: Geographic Information Coordinating Council (published by NCDIT)
source_url: https://it.nc.gov/documents/files/gicc-smac-state-local-gov-metadata-profile20161230-rev1/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: e68685d91469183a12a3468955853537d214fb57a3a5a6bb5d3765f3da28b2f4
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# State and Local Government GIS Metadata Profile (NC GIS standard: State and Local Government GIS Metadata Profile)

## At a glance

The state and local government metadata profile for geospatial data and services (December 30, 2016 version, adopted November 20, 2014). The standards page lists two files with this content; the other differs only in two web addresses and is left out as a duplicate.

## Full text

North Carolina State and Local
Government Metadata Profile for
Geospatial Data and Services
North Carolina Geographic Information Coordinating Council
Statewide Mapping Advisory Committee
Metadata ad hoc Committee

December 30, 2016 Version

Adopted by the NC Geographic Information Coordinating Council
November 20, 2014

                                                                1|Page

Table of Contents
I.     Introduction .......................................................................................................................................... 3
II.    Acknowledgments ................................................................................................................................ 4
III.   Value of Compliant Metadata............................................................................................................... 5
IV. Geospatial Metadata Standards Used to Develop the Profile .............................................................. 6
V.     Implementing the State and Local Government Metadata Profile ...................................................... 6
VI. Recommendations ................................................................................................................................ 7
VII. NC Geospatial Metadata Profile Elements ........................................................................................... 8
Table 1 - Metadata for Geospatial Data........................................................................................................ 9
Table 2 –Elements Required for Geospatial Services ................................................................................. 14
Appendix 1. Code Lists ................................................................................................................................ 17
Appendix 2: Standard Publications and Related Documents ..................................................................... 23
Appendix 3. Element Xpaths ....................................................................................................................... 25
Appendix 4. ISO Feature Catalog (Entity and Attribute) Information ......................................................... 29

                                                                                                                                               2|Page

I.     Introduction
A geospatial metadata record is information, presented in a standardized format, which
describes a dataset that may represent street centerlines, address points, conservation land, or
other features in a wide range of geographically referenced data. The North Carolina
Geographic Information Coordinating Council (NCGICC) recognized the value of valid metadata
and adopted the Federal Geographic Data Committee (FGDC) Content Standard for Digital
Geospatial Metadata (June 8, 1994).

In recent years, the Statewide Mapping Advisory Committee (SMAC) recognized that most
geospatial data managers lacked the time and resources necessary to learn and apply a
metadata standard. To address the problem of missing or incomplete metadata records among
state and local data publishers, the SMAC chartered an ad-hoc Metadata Committee in October
2012 to “recommend ways to expand and improve geospatial metadata in North Carolina that
are efficient for the data producer and benefit data users in the discovery and application of
geospatial data.” The Metadata Committee developed a new standard for North Carolina and
submitted a draft to SMAC in July 2014. After review and modification by SMAC and standing
committees, in October 2014 SMAC recommended adoption by the Council.

With Council review and final editing, the Council adopted the “State and Local Government
Metadata Profile” as the recommended metadata standard for North Carolina state agencies
and local governments (November 20, 2014). The State and Local Government Metadata Profile
is based on the ISO 191xx suite of geospatial metadata standards. The International
Organization for Standardization (ISO) is the world’s foremost developer of voluntary
international standards with more than 19,500 published standards and 162 member countries.
By adopting the ISO series of standards, state agencies, and local governments ensure that
compliance will allow their metadata to be published and searched in a consistent manner by
agencies, organizations, and individuals throughout the world. This new North Carolina
standard is consistent with a statement on the website of the FGDC:

Most National Spatial Data Infrastructure (NSDI) stakeholders have long utilized the Content
Standard for Digital Geospatial Metadata (CSDGM), which will continue to have a legacy for
many years. International geospatial metadata standards are emerging in the community.
…Since ISO 19115 and the associated standards are endorsed by the FGDC, federal agencies are
encouraged to transition to ISO metadata as their agencies are able to do so. While the
selection of appropriate standards is dependent on the nature of your metadata collection and
publication process, ISO metadata should be considered an option now. It’s recognized that the
transition to ISO metadata will be occurring over the next few years.

                                                                                      3|Page

II.     Acknowledgments
This document was compiled by an ad-hoc committee comprised of metadata and GIS
professionals representing municipal, county, state, and federal organizations. The ad-hoc
committee operated under the supervision of the NCGICC’s Statewide Mapping Advisory
Committee (SMAC1) and was advised by metadata experts from the private sector, Urban and
Regional Information Systems Association (URISA2), Federal Geographic Data Committee
(FGDC)3, and GeoDiscover Alberta4. Primary support and resources were provided by North
Carolina’s Center for Geographic Information and Analysis (NCCGIA5).

        Ad-hoc Committee Members:
        Steve Averett, GISP, Chair, City of Greensboro
        Jeff Essic, North Carolina State University
        David Giordano, North Carolina Center for Geographic Information and Analysis
        Don Kovasckitz, GISP, Lee County Government
        Tim Mulrooney, PhD, North Carolina Central University
        Doug Newcomb, United States Fish and Wildlife Service
        Rachel Trent, North Carolina Department of Cultural Resources
        Carter Vickery, GISP, Wake County Government
        Sarah Wray, GISP, North Carolina Department of Transportation

        Technical Advisors
        Lynda Wayne, GeoMaxim / FGDC
        Chelsea Duncan, North Carolina Department of Transportation
        Ryan Bowe, Urban and Regional Information Systems Association
        Jordan Erker, GeoDiscover Alberta

Maintenance of this document, its related resources, and the specifics of the State and Local
Government Metadata Profile will continue under the direction of NCCGIA. Inquiries should be
directed to NCCGIA staff.

1
  https://it.nc.gov/gicc-statewide-mapping-advisory-committee-smac
2
  http://www.urisa.org
3
  https://www.fgdc.gov
4
  https://geodiscover.alberta.ca/geoportal/catalog/main/home.page
5
  https://it.nc.gov/center-geographic-information-and-analysis-cgia

                                                                                    4|Page

III.       Value of Compliant Metadata
Metadata is a set of information that captures and describes the basic characteristics of a
data set or an information resource. The metadata record describes the ‘who, what, when,
where, why and how’ of the associated data. Geospatial metadata is commonly used to
document geospatial data sets but can also be used to document geospatial resources including
mapping applications, data models, and web based services. Metadata records include core
library catalog elements such as title, abstract, and publication date; geographic elements such
as spatial extents and projection; and database elements such as attribute label definitions and
attribute domain values.

Metadata allows users of geospatial data to find the information and data they need and
determine how best to use it. Metadata facilitates:

Data Management
       •   Preserve data history so the data can be re-used or adapted
       •   Assess the age and character of data holdings to determine which data should be
           maintained, updated, or deleted
       •   Instill data accountability by requiring the producer to state what is known about the
           data and what is not known
       •   Limit data liability by explicitly designating the effective and administrative limits of use
           of the data
Project Management
       •   Plan and document the data types and content needed to support the project
       •   Monitor data development by regular review of the process steps completed and
           recorded within the metadata record
       •   Provide all project participants a common language of attributes and process methods
           and a place to record and share progress
       •   Access the lineage and content of outsourced data production by requiring robust
           metadata as a contract deliverable

Due to the business demands listed above, metadata continues to increase in value. The
proliferation of local governments serving geospatial data as map services extends the use of
geospatial data, but makes it imperative that agencies provide compliant metadata in a global
environment.

                                                                                              5|Page

IV.       Geospatial Metadata Standards Used to Develop the Profile
Given the increasing number of geospatial metadata standards available and the current shift in
the U.S. from the FGDC Content Standard for Digital Geospatial Metadata (CSDGM 1998) to the
ISO 191** suite of metadata standards, this profile was developed to be easily applied to most
geospatial metadata standards. However, the applicability of the profile to these standards is
prioritized as follows:

      •   ISO 19115 and 19115-1 compliance is achieved by the use of all profile-designated
          ‘required’ (green/dark grey) elements
      •   CSDGM compliance is achieved by the use of all profile elements, ‘required’ (green/dark
          grey) and ‘optional’ (tan/light grey) elements.
      •   Compliance with other standards is variable and may require additional elements.

V.        Implementing the State and Local Government Metadata Profile
The adoption of a new ISO based metadata standard offers an opportunity for agencies that do
not currently maintain standardized metadata to engage in compliant practice. Agencies that
currently maintain metadata will have an opportunity to transition from their current CSDGM
template to the current standard allowing them to document additional data resources (map
services, geospatial models, and applications).

Implementing or transitioning metadata standards requires guidance. Several resources (listed
below) have been developed specifically to help define and implement the state and local
government profile:

Table of Metadata Elements
      The table of elements lists and defines the specific mandatory and optional (recommended)
      metadata elements identified by the NC metadata community as necessary for the effective
      discovery and application of geospatial data resources. Metadata records that include all NC
      State and Local Government Profile mandatory elements comply with the minimum
      requirements of both ISO 19115 and ISO 19115-1. Metadata records that include all NC
      State and Local Government Profile elements (required and optional) comply with ISO
      19115, ISO 19115-1, and the FGDC Content Standard for Digital Geospatial Metadata
      (CSDGM).

                                                                                        6|Page

Metadata Implementation Resources
      The North Carolina Center for Geographic Information and Analysis has developed a
      webpage to support implementation of this profile at:

      https://www.nconemap.gov/pages/metadata

      The site will provide key resources including:

         •   The most current version of the NC State and Local Government Metadata Profile
             document.
         •   Example local government metadata records, in both CSDGM and ISO formats, that
             illustrate profile compliant metadata.
         •   Templates (XML documents) that can be ingested into a variety of metadata editors
             to serve as a boilerplate for the creation of a profile compliant metadata record. The
             templates can also be populated with additional content and used as an
             organizational or project-specific template.
         •   Links to available metadata editors and related applications.

      Additional resources can be added to the website as needed and available.

VI.      Recommendations
The Federal Geographic Data Committee (FGDC) currently endorses ISO 19115:2003 -
Geographic information -- Metadata and is expected to endorse the March 2014 update, ISO
19115-1:2014 Geographic Information – Metadata – Part1: Fundamentals once adopted by the
American National Standards Institute (ANSI). The FGDC strongly encourages agencies and
National Spatial Data Infrastructure (NSDI) Stakeholders to transition from the former federal
geospatial metadata standard, Content Standard for Digital Geospatial Metadata (CSDGM), to
the ISO 191** suite of standards.

In an effort to comply with international standards and federal guidelines, the NCGICC
recommends North Carolina state agencies and local governments adopt the ISO compliant
NC State and Local Government Metadata Profile for cataloging all geospatial data and
resources. The resources contained in this document are intended to assist agencies and local
governments with the initial implementation of metadata and the conversion from CSDGM for
those who currently use the prior standard.

                                                                                         7|Page

VII. NC Geospatial Metadata Profile Elements
Table 1 - Metadata for Geospatial Data provides a list of metadata elements considered
minimal documentation for the discovery, maintenance, and application of geospatial data. For
each element, a domain for values is specified and best practices are provided to guide users in
the effective use of the metadata element.

Table 2 - Metadata for Geospatial Services provides a list of metadata elements considered
minimal documentation for the discovery, maintenance, and application of geospatial services.
Services are applications that store, distribute, view, manipulate or otherwise utilize geospatial
data such as:

   •   Geospatial data catalogs such as data.NCOneMap.gov
   •   Geospatial community workspaces such as the national Geospatial Platform
   •   Web-mapping applications
   •   Online data viewers and processors

To apply this profile to your geospatial metadata, users should:

   1. Open a new or existing metadata record in the application that you use to create and/or
      edit metadata.
   2. Identify the table below that is relevant to the resource for which you are creating the
      metadata.
      • If you are creating metadata for a geospatial data resource, use Table 1. Metadata
          for Geospatial Data
      • If you are creating metadata for a geospatial service, use Table 2. Metadata for
          Geospatial Services
   3. As you work down the table, line by line:
      • Find the metadata element in your metadata editor that corresponds to the
          metadata element listed in the profile.
      • Address all required elements.
      • If using the CSDGM standard, also address the ‘Optional/CSDGM’ elements.
   4. Populate the elements based on the best practices guidance provided for each element

   To facilitate metadata creation, users are strongly encouraged to develop an organizational
   metadata template by importing one of the NC State and Local Government Metadata
   Profile templates provided at https://www.nconemap.gov/pages/metadata and editing it
   to include organizational information (contacts, distribution methods, liability statements,
   etc.).

                                                                                        8|Page

Table 1 - Metadata for Geospatial Data
Legend:
   NC Profile and ISO required
   Optional and/or CSDGM required

Element             Data Type          NC Best Practice
Title               Free text         • Provide a descriptive, unique, name to convey the nature of the data.
                                        At a minimum, address: what, where and when.
                                      • Avoid acronyms and abbreviations that are not commonly understood
                                        though a filename or other identifying reference can be included in
                                        addition to the descriptive content.
                                         Example: Environmental Sensitivity Index (ESI) Scrub-Shrub and Wetlands,
                                         Geographic, Wilmington NC, NAD83, North Caroline Department of
                                         Environment and Natural Resources (NCDENR) 2001 [esi_scrub-
                                         shrub_wetland_NCDENR_2001]
Publication Date    Date             • Provide the date that the data was published or otherwise finalized.
                                     • Additional, optional, dates can be included to specify the date when
                                       the data was first created, a revision date or the other date type as
                                       specified by the Date Type Code described below
                                     • Format = YYYY-MM-DD or YYYYMMDD.
                                       If the day is not known, use YYYY-MM.
                                       If the month is not known, use YYYY.
                                       If the date is not known, use ‘unknown’ in CSDGM and, in ISO, employ
                                       the xml attribute nilReason as a means of entering text in a date only
                                       field, e.g. <date nilReason="unknown"/>
                                     • Do not specify a range of dates for the publication date, e.g. YYYY-
                                       YYYY.
                                     • Do not use YYYYMM because it is indistinguishable from the incorrect,
                                       but still used, YYMMDD.
Date Type           Date Type Code = • ISO metadata only – no need to specify if using CSDGM
                    ‘publication’    • Used to designate the type of each Date listed
                                     • A ‘publication’ Date is required
Responsible Party   Free text        • Provide the Organization Name of the agency that serves as legal
Organization                           custodian of the data
Name                                 • Additional, optional, Responsible Party (name or organization) can be
                                       included to specify:
                                          - a secondary or more specific office or staff position that serves
                                             as a point of contact for questions about the data
                                             (role=pointOfContact)
                                          - collaborating organizations/agencies, vendors who created the
                                             data, entities that distribute the data, individuals or agencies
                                             that have processed the data, and other responsible parties.
                                     • Spell out acronyms and include sufficient information, e.g. parent
                                       organizations or state, to uniquely identify the Responsible Party.

                                                                                                            9|Page

Element             Data Type           NC Best Practice
                                         Examples:
                                         “North Carolina Dept. of Transportation (NCDOT), Division of Highways,
                                         Technical Services “
                                         “Wake County NC, Geographic Information Services Division”
Responsible Party   Role Code =        • ISO metadata only – no need to specify if using CSDGM
Role                ‘custodian’ or     • Used to designate the specific role of each Responsible Party listed
                    ‘pointOfContact’   • A ‘custodian’ and/or ‘pointOfContact’ is required
Online Linkage      URL                • Provide a URL address that provides access, preferably direct access,
                                         to the data
                                       • NC OneMap geoportal requires an online linkage to the data
Abstract            Free text          • Provide a description of the data content and features including data
                                         application (GIS, CAD, image, etc.), geographic coverage, time period
                                         of content, and special data characteristics, limitations and
                                         information that will aid data consumers in determining if the data is
                                         relevant to their intended application.
                                       • List most important information first as some applications will display
                                         only first 150 – 200 characters of the abstract.
Status              Progress Code      • Indicate the status of the data, e.g. completed, ongoing, planned, etc.
                                       • Indicate ‘completed’ if the data is finalized and not continually
                                         updated.
                                       • Indicate ‘onGoing’ if the data is being actively and continually
                                         updated.
Maintenance and     Maintenance        • Indicate the value in the Code List that best describes how often the
Update Frequency    Frequency Code       data is updated
                                       • If the status of the data is ‘completed’:
                                         - Indicate ‘asNeeded’ if staff are available to make as-needed
                                            changes (e.g., to correct errors)
                                         - Indicate ‘notPlanned’ if staff do not foresee making any changes.
                                       • If the status of the data is ‘onGoing’:
                                         - Indicate the most applicable value to describe the known frequency
                                            of planned updates
                                       • If the frequency of updates is not amongst the Code List values, e.g.
                                         every two months, indicate ‘periodic’
Theme Keywords      Free text          • Provide a robust set of descriptive theme-related keywords
                    &                  • Include broad and specific-terms, e.g. ‘wetlands’, ‘salinity’
                    Keyword Type       • Select terms from relevant standardized vocabularies/thesauri when
                    Code = ‘theme’       possible
                                       • If using CSDGM, include one or more ISO Topic Categories
Use Constraints     Free text          • Indicate any restrictions associated with using the data.
                                        Examples:
                                        • ‘The locations in this data were not surveyed and should not be used for
                                           legal purposes’
                                        • ‘Although these data have been processed successfully on a computer
                                           system at NCDEQ, no warranty expressed or implied is made regarding the
                                           accuracy or utility of the data on any other system or for general or
                                           scientific purposes, nor shall the act of distribution constitute any such

                                                                                                            10 | P a g e

Element             Data Type           NC Best Practice
                                            warranty. It is also strongly recommended that careful attention be paid to
                                            the contents of the metadata file associated with these data to evaluate
                                            data set limitations, restrictions, or intended use. NC DEQ shall not be held
                                            liable for improper or incorrect use of the data described and/or
                                            contained herein’
Topic Category      Topic Category     • Indicate one or more high-level subjects., as specified by the Topic
                    Code                 Category Code List
                                       • If using the CSDGM, include one or more topic categories as theme
                                         keywords and specify the theme keyword thesaurus as ‘ISO Topic
                                         Categories’
Geographic          Latitude /         • Document each: east, west, north, and south coordinate pairs
Extent: Bounding    Longitude          • Format = decimal degrees
Box                 coordinate pairs     -90.0 < latitude < 90.0; -180.0 < longitude < 180.0
Temporal Extent     Date               • Indicate the date(s) for the content of the data. This value, typically
of Data Content                          corresponds to the collection, vs. the publication, of the data
                                       • This may be a:
                                         - single date, e.g. YYYY-MM-DD, YYYY-MM, or YYYY
                                            series of dates, e.g. YYYY-MM-DD, YYYY-MM-DD, YYYY-MM-DD)
                                         - range of dates as illustrated below:
                                            <extent>
                                             <TimePeriod >
                                              <beginPosition>2003-01-18
                                              </beginPosition>
                                              <endPosition> indeterminatePosition="now"
                                              < endPosition />
                                             </gml:TimePeriod>
                                            </gmd:extent>
Feature Catalogue   Free text          • Not required for imagery
(Entities and                          ISO
Attributes)                            • ISO feature catalog information (entities and attributes) information
                                          can be documented within the metadata record, referenced as a
                                          standalone external resource, or indicated as internal to the dataset
                                       • If included within the core record, utilize elements from the ISO
                                          19110 Feature Catalog standard
                                       • If referencing an external resource, the information may be in any
                                          format though use of ISO 19110 is highly encouraged.
                                       • See Appendix 5 for more information about documenting features
                                       CSDGM
                                       • If your dataset features are documented separately as a content
                                          specification (doc, pdf, etc.), data dictionary (xls, mdb, etc.), or other,
                                          provide an:
                                          - Entity/Attribute Overview Description to describes the key features
                                            and
                                          - Entity/Attribute Detail Citation with a link to the external
                                            documentation

                                                                                                               11 | P a g e

Element             Data Type           NC Best Practice
Process             Free text          • Provide a description of how the data were created and indicate
Description                               source data used, where applicable
                                       • This is a repeatable element so can be used to provide a single,
                                          compiled description or a series of process step descriptions
Spatial Reference   Free text          ISO
Information                            • Provide a Spatial Reference System Identifier (SRID) from
                                          authoritative source such as the European Petroleum Survey Group
                                          (EPSG), More information at http://spatialreference.org/
                                       CSDGM
                                        Provide one of the following:
                                        • Geographic Latitude & Longitude Resolutions, Coordinate Units
                                        • Map Projection Name, Parameters, Coordinate Resolution
                                        • Grid Coordinate System Name, Parameters, Coordinate Resolution
                                        • Local Description, Parameters, Coordinate Resolution
Metadata            Date               • Indicate the date that the metadata record was created
Creation Date
Metadata Contact    Free text          • Provide the Organization Name of the agency that serves as the point
Name                                     of contact for the metadata record
Metadata Contact    Role Code =        • Used to designate the specific role of each Responsible Party listed
Role Code           pointOfContact     • A Metadata Contact ‘pointOfContact’ is required

Optional and/or CSDGM Required Elements
Purpose            Free text       • Explain why the data was created. This element can provide critical
                                     context for data that was created for a specific use and may not be
                                     appropriate for other, or more general, use
Currentness        Free text       • Indicate if the Time Period of Content references that actual ‘ground
Reference                            condition’ during the time or some, later, ‘publication date’, e.g. the
                                     actual date of capture of an orthophoto or the delivery date for the
                                     orthophoto collection (publication)
Browse Graphic     Free text       • Provide a name for an available browse graphic image
Filename                           • For best results size the graphic at 200 pixels by 133 pixels, and save it
(thumbnail)                          as a PNG, JPEG, or GIF
Browse Graphic     Free text       • Provide a description of the graphic
File Description
Browse Graphic     Free text       • Indicate the browse graphic file type, e.g. PNG, JPEG, or GIF
File Type
Theme Keyword      Free text       • Recommended if any standardized vocabulary is associated with one
Thesaurus                            or more theme keywords, e.g. ’Cowardin Wetland Classification’,
                                     ‘GCMD Science Keywords’
                                   • If no standardized vocabulary was used Thesaurus Name = ‘none’
                                   • Note that thesauri are not limited to formal ‘thesauri” and should
                                     include informal information documents and publications
                                   • Thesaurus requires a ‘date’ and a ‘date type’ in ISO 19115. No
                                     thesaurus date/date type is required for CSDGM and ISO 19115-1

                                                                                                       12 | P a g e

Element               Data Type         NC Best Practice
Place Keyword         Free text        • Provide a robust set of descriptive place-related keywords
                      &                • Include broad and specific-terms, e.g. ‘North Carolina’, ‘Madison
                      Keyword Type       County’, ‘Marshall’
                      Code = ‘place’   • Include relevant regional references, e.g. ‘Appalachia’, ‘Piedmont’
Place Keyword         Free text        • Indicate the standardized vocabulary associated with one or more
Thesaurus                                place keywords, e.g.’ Geographic Names Information System (GNIS)’,
                                         ‘North Carolina Gazetteer’
                                       • Note that thesauri are not limited to formal ‘thesauri” and should
                                         include informal information documents and publications
                                       • Thesaurus requires a ‘date’ and a ‘date type’ in ISO 19115. No
                                         thesaurus date/date type is required for CSDGM and ISO 19115-1
Access                Free text        • Indicate any restrictions and legal prerequisites for accessing the
Constraints                              data, e.g. environmentally sensitive information, personal data,
                                         intellectual property
Logical               Free text        • Provide a description of any assessment performed to test the fidelity
Consistency                              of the data attributes (database QA/QC) or the data structure
Report                                   (topological checks, i.e. RMS error)
Completeness          Free text        • Provide a description of the omissions and selection criteria used to
                                         develop or generalize the data
                                         Examples:
                                         “Federal Lands excluded”
                                         “Municipalities are defined as having populations >2500”
Process Date          Date             • Provide a date for the process. This can be a single, multiple or range
                                         of dates or ‘unknown’ or ‘not complete’
                                       • Date format YYYYMMDD
Metadata Contact      Free text        • Provide the address information for the Metadata Contact
Address (Type,
City, State, Postal
Code)
Metadata Contact      Free text        • Indicate the ten-digit phone number at which the Metadata Contact
Telephone                                can be reached.
Metadata              Free text        • Indicate the metadata standard to which the metadata record is in
Standard Name                            compliance.
                                         Examples:
                                         “ISO 19115”, ‘ISO 19115-1”, or “ISO 19115-2”
                                         “FGDC Content Standard for Digital Geospatial Metadata (CSDGM)”
Metadata              Free text        • Indicate the version of the metadata standard used
Standard Version                         Examples:
                                         “ISO 19115:2003/Cor 1:2006”
                                         “FGDC-STD-001-1998”

                                                                                                           13 | P a g e

 Table 2 –Elements Required for Geospatial Services
 Legend:
    NC Profile and ISO required
    Optional and/or CSDGM required

 Element             Data Type           NC Best Practice
Service Specific Elements
 Metadata Scope       Metadata Scope     • Indicate that the metadata record applies to a ‘service’ (ISO assumes
                      Code = ‘service’     the metadata is for a dataset unless otherwise specified)
                                         • If using CSDGM, indicate ‘service’ as the Geospatial Data Presentation
                                           Form
 Service Type        Free text           • The type of service that is being documented. No code list yet exists
                                           but OGC service types include: WMS, WFS, CSW, WCS, WMTS, KML
                                           and REST. Other free text values are permitted
                                         • If using CSDGM, add the service type to the ‘service’ value in
                                           Geospatial Data Presentation Form
Additional Required Elements
 Title               Free text        • Provide a descriptive, unique, name to convey the nature and content
                                        of the service
                                      • Avoid acronyms & abbreviations if not commonly used
                                        Example:
                                        US National Wetlands Inventory (NWI) Map Server.
 Publication Date    Date             • Provide the date that the service was published or otherwise made
                                        available.
                                      • Format = YYYY-MM-DD or YYYYMMDD.
                                        If the day is not known, use YYYY-MM.
                                        If the month is not known, use YYYY.
                                        If the date is not known, use ‘unknown’ in CSDGM and, in ISO,
                                        employ the xml attribute nilReason as a means of entering text in a
                                        date only field, e.g.
                                           <date nilReason="unknown"/>
                                      • Do not specify a range of dates for the publication date, e.g. YYYY-
                                        YYYY.
                                      • Do not use YYYYMM, which because it is indistinguishable from the
                                        incorrect, but still used, YYMMDD.
 Date Type           Date Type Code = • ISO metadata only – no need to specify if using CSDGM
                     publication      • Used to designate the type of each Date listed
                                      • A ‘publication’ Date is required
 Responsible Party   Free text        • Provide the Organization Name of the agency that manages the
 / Originator                           service
                                      • Additional, optional, Responsible Parties can be included to specify:
                                        - a secondary or more specific office or staff position that serves as a
                                           point of contact for questions about the service
                                        - collaborating organizations/agencies, vendors who contribute to or
                                           help to manage the service.

                                                                                                         14 | P a g e

Element             Data Type           NC Best Practice
                                       • Spell out acronyms and include sufficient information, e.g. parent
                                         organizations or state, to uniquely identify the Responsible Party.
                                          Examples:
                                          “North Carolina Dept. of Transportation (NCDOT), Division of Highways,
                                          Technical Services”
Responsible Party   Role Code =        • ISO metadata only – no need to specify if using CSDGM
Role                ‘custodian’ or     • Used to designate the specific role of each Responsible Party listed
                    ‘pointOfContact’   • A ‘custodian’ or ‘pointOfContact’ is Responsible Party required.
Online Linkage      URL                • Provide a URL address that provides access, preferably direct access,
                                         to the service
                                       • NC OneMap geoportal requires an online linkage to the service
Online Function     Function Code       • ISO metadata only – no need to specify if using CSDGM
Code                                    • Used to designate the specific function of the Service Online
                                            Resource
Abstract            Free text          • Provide a description of the service content, extent, and key
                                         operating features. Include information about how the data are
                                         organized, formatted, and distributed, e.g. tiles, collections, zip, tiff,
                                         etc.
                                       • List most important information first as some applications will display
                                         only first 150 – 200 characters of the abstract.
Theme Keywords      Free text          • Provide a robust set of descriptive theme-related keywords
                                       • Include broad and specific-terms, e.g. ‘wetlands’, ‘salinity’
                                       • Select terms from relevant standardized vocabularies/thesauri when
                                         possible
                                       • If using CSDGM, include one or more ISO Topic Categories
Use Constraints     Free text          • Indicate any restrictions associated with using the service
                                         Examples:
                                         ‘The locations in this data were not surveyed and should not be used for
                                         legal purposes’
                                       • ‘Although these data have been processed successfully on a computer
                                         system at NCDEQ, no warranty expressed or implied is made regarding the
                                         accuracy or utility of the data on any other system or for general or scientific
                                         purposes, nor shall the act of distribution constitute any such warranty. It is
                                         also strongly recommended that careful attention be paid to the contents of
                                         the metadata file associated with these data to evaluate data set limitations,
                                         restrictions or intended use. NC DEQ shall not be held liable for improper or
                                         incorrect use of the data described and/or contained herein’
Geographic          Latitude /         • Document each: east, west, north, and south coordinate pairs
Extent: Bounding    Longitude          • Format = decimal degrees
Box                 coordinate pairs      -90.0 < latitude < 90.0; -180.0 < longitude < 180.0
Metadata            Date                Indicate the date that the metadata record was created
Creation Date
Metadata Contact    Free text        • Provide the Organization Name of the agency that serves as the point
Name                                   of contact for the metadata record.
Metadata Contact    Role Code =      • Used to designate the specific role of each Responsible Party listed
Role Code           ‘pointOfContact’ • A Metadata Contact ‘pointOfContact’ is required.

                                                                                                                15 | P a g e

Element               Data Type    NC Best Practice
Purpose               Free text   • Explain why the service was created and the intended use and user
                                    community. This element can provide critical context for data that
                                    was created for a specific use and may not be appropriate for other,
                                    or more general, use.
Currentness           free text   • Indicate if the Time Period of Content references that actual ‘ground
Reference                           condition’ during the time or some, later, ‘publication date’, e.g. the
                                    actual date of capture of an orthophoto or the delivery date for the
                                    orthophoto collection (publication)
Theme Keyword         Free text   • Indicate any standardized vocabulary associated with one or more
Thesaurus                           theme keywords, e.g. ’Cowardin Wetland Classification’, ‘GCMD
                                    Science Keywords’
                                  • If no standardized vocabulary was used Thesaurus Name = ‘none’
                                  • Note that thesauri are not limited to formal ‘thesauri” and should
                                    include informal information documents and publications
                                  • ISO 19115 requires a Thesaurus ‘date’ and a ‘date type’. No thesaurus
                                    date/date type is required for CSDGM and ISO 19115-1
Place Keyword         Free text   • Optional but recommended
                                  • Provide a robust set of descriptive place-related keywords
                                  • Include broad and specific-terms, e.g. ‘North Carolina’, ‘Madison
                                    County’, ‘Marshall’
                                  • Include relevant regional references, e.g. ‘Appalachia’, ‘Piedmont’
Place Keyword         Free text   • Optional and recommended if standardized vocabulary used
Thesaurus                         • Indicate any standardized vocabulary associated with one or more
                                    theme keywords, e.g. ’Cowardin Wetland Classification’, ‘GCMD
                                    Science Keywords’
                                  • If no standardized vocabulary was used Thesaurus Name = ‘none’
                                  • Note that thesauri are not limited to formal ‘thesauri” and should
                                    include informal information documents and publications
                                  • Thesaurus requires a ‘date’ and a ‘date type’ in ISO 19115. No
                                    thesaurus date/date type is required for CSDGM and ISO 19115-1
Access                Free text   • Indicate any restrictions and legal prerequisites for accessing the
Constraints                         service, e.g. environmentally sensitive information, personal data,
                                    intellectual property
Metadata Contact      Free text   • Provide the address information for the Metadata Contact
Address (Type,
City, State, Postal
Code)
Metadata              Free text   • Indicate the metadata standard to which the metadata record is in
Standard Name                       compliance.
                                    Examples:
                                    ‘ISO 19115’, ‘ISO 19115-1’, or ‘ISO 19115-2’
                                  • ‘FGDC Content Standard for Digital Geospatial Metadata (CSDGM)’
Metadata              Free text   • Indicate the version of the metadata standard used
Standard Version                    Examples:
                                    “2003/Cor.1:2006”
                                  • “1998:Version 2”

                                                                                                      16 | P a g e

Appendix 1. Code Lists
The following is a subset of code lists and values relevant to the NC Metadata Profile. NOAA provides a
full ISO 19115 and 19115-2 code list at:
https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115_and_19115-2_CodeList_Dictionaries
Some Code Lists are expanded in ISO 19115-1 and will be updated when the standard is approved for
use.

Date Type Code
Online Function Code
Role Code
Topic Category Code
Progress Code
Keyword Type Code
Maintenance Frequency Code
Metadata Scope Code

********************************************************************************
Date Type Code (Date Type element)
 DateType Code                  Description

 creation                       when the resource was brought into existence

 publication                    when the resource was issued

 revision                       when the resource was improved or amended

Online Function Code (Function element)
 Online Function Code           Description

 download                       online instructions for transferring data from one storage device to
                                another

 information                    online information about the resource

 offlineAccess                  online instructions for requesting the resource from the provider

 order                          online order process for obtaining the resource

 search                         online search interface for seeking out information about the resource

                                                                                                    17 | P a g e

Role Code (Responsible Party Role element)
Responsible Party Role Code   Description

custodian                     party that accepts accountability and responsibility for the data and
                              ensures appropriate care and maintenance of the resource

pointOfContact                party who can be contacted for acquiring knowledge about or
                              acquisition of the resource

Topic Category Code (Topic Category element)
Topic Category Code                 Description                                 Examples
farming                             rearing of animals and/or cultivation of    agriculture, irrigation,
                                    plants.                                     aquaculture,
                                                                                plantations, herding,
                                                                                pests and diseases
                                                                                affecting crops and
                                                                                livestock
biota                               flora and/or fauna in natural               wildlife, vegetation,
                                    environment.                                biological sciences,
                                                                                ecology, wilderness,
                                                                                sealife, wetlands,
                                                                                habitat
boundaries                          legal land descriptions.                    political and
                                                                                administrative
                                                                                boundaries
climatologyMeteorologyAtmosphere    processes and phenomena of the              cloud cover, weather,
                                    atmosphere.                                 climate, atmospheric
                                                                                conditions, climate
                                                                                change, precipitation
economy                             economic activities, conditions and         production, labour,
                                    employment.                                 revenue, commerce,
                                                                                industry, tourism and
                                                                                ecotourism, forestry,
                                                                                fisheries, commercial
                                                                                or subsistence
                                                                                hunting, exploration
                                                                                and exploitation of
                                                                                resources such as
                                                                                minerals, oil and gas
elevation                           height above or below sea level.            altitude, bathymetry,
                                                                                digital elevation
                                                                                models, slope, derived
                                                                                products
environment                         environmental resources, protection         environmental
                                    and conservation.                           pollution, waste
                                                                                storage and
                                                                                treatment,
                                                                                environmental impact
                                                                                assessment,

                                                                                                 18 | P a g e

                                                                         monitoring
                                                                         environmental risk,
                                                                         nature reserves,
                                                                         landscape
geoscientificInformation    information pertaining to earth sciences.    geophysical features
                                                                         and processes,
                                                                         geology, minerals,
                                                                         sciences dealing with
                                                                         the composition,
                                                                         structure and origin of
                                                                         the earth s rocks, risks
                                                                         of earthquakes,
                                                                         volcanic activity,
                                                                         landslides, gravity
                                                                         information, soils,
                                                                         permafrost,
                                                                         hydrogeology, erosion
health                      health, health services, human ecology,      disease and illness,
                            and safety.                                  factors affecting
                                                                         health, hygiene,
                                                                         substance abuse,
                                                                         mental and physical
                                                                         health, health services
imageryBaseMapsEarthCover   base maps.                                   land cover,
                                                                         topographic maps,
                                                                         imagery, unclassified
                                                                         images, annotations
intelligenceMilitary        military bases, structures, activities.      barracks, training
                                                                         grounds, military
                                                                         transportation,
                                                                         information collection
inlandWaters                inland water features, drainage systems      rivers and glaciers, salt
                            and their characteristics.                   lakes, water utilization
                                                                         plans, dams, currents,
                                                                         floods, water quality,
                                                                         hydrographic charts
location                    positional information and services.         addresses, geodetic
                                                                         networks, control
                                                                         points, postal zones
                                                                         and services, place
                                                                         names
oceans                      features and characteristics of salt water   tides, tidal waves,
                            bodies (excluding inland waters).            coastal information,
                                                                         reefs
planningCadastre            information used for appropriate actions     land use maps, zoning
                            for future use of the land.                  maps, cadastral
                                                                         surveys, land
                                                                         ownership

                                                                                          19 | P a g e

society                  characteristics of society and cultures.   settlements,
                                                                    anthropology,
                                                                    archaeology,
                                                                    education, traditional
                                                                    beliefs, manners and
                                                                    customs, demographic
                                                                    data, recreational
                                                                    areas and activities,
                                                                    social impact
                                                                    assessments, crime
                                                                    and justice, census
                                                                    information
structure                man-made construction.                     buildings, museums,
                                                                    churches, factories,
                                                                    housing, monuments,
                                                                    shops, towers
transportation           means and aids for conveying persons       roads,
                         and/or goods.                              airports/airstrips,
                                                                    shipping routes,
                                                                    tunnels, nautical
                                                                    charts, vehicle or
                                                                    vessel location,
                                                                    aeronautical charts,
                                                                    railways
utilitiesCommunication   energy, water and waste systems and        hydroelectricity,
                         communications infrastructure and          geothermal, solar and
                         services.                                  nuclear sources of
                                                                    energy, water
                                                                    purification and
                                                                    distribution, sewage
                                                                    collection and
                                                                    disposal, electricity
                                                                    and gas distribution,
                                                                    data communication,
                                                                    telecommunication,
                                                                    radio, communication
                                                                    networks
extraterrestrial         region more than 100 km above the          space, planets
                         surface of the earth
disaster                 information related to disasters           site of the disaster,
                                                                    evacuation zone,
                                                                    disaster prevention
                                                                    facility, disaster relief
                                                                    activities

                                                                                       20 | P a g e

Progress Code (Status element)
Progress Code          Description

completed              production of the data has been completed

historicalArchive      data has been stored in an offline storage facility

obsolete               data is no longer relevant

onGoing                data is continually being updated

planned                fixed date has been established upon or by which the data will be created
                       or updated

required               data needs to be generated or updated

underDevelopment       data is currently in the process of being created

Keyword Type Code (Keyword element)
Keyword Type Code      Description

discipline             identifies a branch of instruction or specialized learning

place                  identifies a location

stratum                identifies the layer(s) of any deposited substance

temporal               identifies a time period

theme                  identifies a subject or topic

                                                                                           21 | P a g e

Maintenance Frequency Code (Maintenance and Update Frequency element)
Maintenance      Description
Frequency Code

continual        data is repeatedly and frequently updated

daily            data is updated each day

weekly           data is updated on a weekly basis

fortnightly      data is updated every two weeks

monthly          data is updated each month

quarterly        data is updated every three months

biannually       data is updated twice each year

annually         data is updated every year

asNeeded         data is updated as deemed necessary

irregular        data is updated in intervals that are uneven in duration

notPlanned       there are no plans to update the data

unknown          frequency of maintenance for the data is not known

Metadata Scope Code (for Services only)
Maintenance      Description
Scope Code       Default value is ‘dataset’. Must specify if scope is service or other: attribute,
                 feature type, model, etc.

service          information applies to a capability which a service provider entity makes available to a
                 service user entity through a set of interfaces that define a behavior such as a use case

                                                                                                    22 | P a g e

Appendix 2: Standard Publications and Related Documents

ISO 191** Suite of Standards
   •   General information about the ISO geospatial metadata standards
       https://www.fgdc.gov/metadata/csdgm-standard

   Formal Publications
   Note: ISO/ANSI standards are available by purchase only. Look for the less costly ‘INCITS’
   publication/versions of the standards. Agencies are encouraged to make agency-wide purchases that
   will facilitate access to the standard across the organization.

   •   ISO 19115:2003 Geographic Information – Metadata
       Initial ISO geospatial metadata standard
       http://webstore.ansi.org/RecordDetail.aspx?sku=INCITS%2fISO+19115-2003
       and 2006 addendum
       https://www.iso.org/obp/ui/#iso:std:iso:19115:ed-1:v1:cor:1:v1:en

   •   ISO 19115-1:2014 Geographic Information – Metadata – Part1: Fundamentals
       2014 update to the ISO 19115 standard
       http://webstore.ansi.org/RecordDetail.aspx?sku=ISO+19115-1%3a2014

   •   ISO 19115-2:2009 Geographic information - Metadata - Part 2: Extensions for imagery and
       gridded data
       2009 extension to the ISO 19115 standard for imagery, gridded and collection-level data
       http://webstore.ansi.org/RecordDetail.aspx?sku=INCITS%2fISO+19115-2-2009%5b2009%5d

   •   ISO 19110:2005 Geographic information -- Methodology for feature cataloguing
       Current ISO standard for documenting entity/attributes
       http://webstore.ansi.org/RecordDetail.aspx?sku=INCITS%2FISO+19110-2005

   •   ISO 19119:2005 Geographic information – Services
       http://webstore.ansi.org/RecordDetail.aspx?sku=INCITS%2fISO+19119-2005
       and 2008 amendment
       http://webstore.ansi.org/RecordDetail.aspx?sku=ISO+19119%2fAmd1%3a2008

                                                                                        23 | P a g e

Federal Geographic Data Committee Content Standard for Digital Geospatial
Metadata (CSDGM)
   Note: The CSDGM standard and resources can be downloaded for free.

   •   General information about the CSDGM standard
       https://www.fgdc.gov/metadata/csdgm-standard
   •   FGDC Content Standard for Digital Geospatial Metadata, Vers. 2
       The technical publication of the 1998 version of the FGDC CSDGGM metadata standard
       https://www.fgdc.gov/standards/projects/metadata/base-metadata/v2_0698.pdf
   •   FGDC Content Standard for Digital Geospatial Metadata, Vers. 2 Workbook
       A user-friendly guide to and representation of the publication of the 1998 version of the FGDC
       CSDGGM metadata standard
       https://www.fgdc.gov/metadata/documents/workbook_0501_bmk.pdf
   •   FGDC Metadata Quick Guide – guidance on writing quality metadata
       https://www.fgdc.gov/metadata/documents/MetadataQuickGuide.pdf

                                                                                           24 | P a g e

Appendix 3. Element Xpaths
Metadata elements often repeat at different locations within a metadata record. ‘Title’, for example,
may apply to the data sets being document (Identification Information), a source data set being
documented (Lineage), or to a web service that provides visualization or access to the dataset
(Distribution). As such, the following ‘xpaths’ are provided to specify the location, and context, of the
required element.

  ISO Xpath              CSDGM Xpath

Required Metadata Elements for the Documentation of Datasets
Title
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.citation/CI_Citation.title
metadata/idinfo/citation/citeinfo/title
Publication Date
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.citation/CI_Citation.date/C
I_Date.date
metadata/idinfo/citation/citeinfo/pubdate
Date Type
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.citation/CI_Citation.date/C
I_Date.dateType
CSDGM (n/a)
Responsible Party Organization Name
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.pointOfContact/CI_Respon
sibleParty.organisationName
metadata/idinfo/citation/citeinfo/origin
Responsible Party Role
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.pointOfContact/CI_Respon
sibleParty.role
CSDGM (n/a)
Online Linkage
preferred:
MD_Metadata/MD_Distribution.transferOptions/MD_DigitalTransferOptions.onLine/CI_OnlineResource
.linkage/
or
MD_Metadata/MD_Distributor.distributorContact/CI_ResponsibleParty.contactInfo/CI_Contact.onlineR
esource/CI_OnlineResource (note that this xpath will change in ISO 19115-1)

optionally:
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.pointOfContact/CI_Respon
sibleParty.contactInfo/CI_Contact.onlineResource/CI_OnlineResource.linkage
citation/CI_Citation.citedResponsibleParty/ (note that this xpath will change in ISO 19115-1)
preferred:
metadata>distinfo>storder>digform>digtoption>onlinopt>networka>networkr
optionally:
metadata>idinfo>citation>citeinfo>onlink

                                                                                                25 | P a g e

Online Function Code
choose xpath above.../CI_OnlineResource.function
CSDGM (n/a)
Abstract
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.abstract
metadata/idinfo/description/abstract
Status
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.status/MD_ProgressCode
metadata/idinfo/status/progress
Maintenance and Update Frequency
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.resourceMaintenance/MD
_MaintenanceInformation.maintenanceAndUpdateFrequency/MD_MaintenanceFrequencyCode
metadata/idinfo/status/update
Theme Keywords
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.descriptiveKeywords/Md_
Keywords.keywords
… MD_Keywords.Type/MD_KeywordTypeCode = ‘Theme’
metadata/idinfo/keywords/theme/themekey
Topic Category
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.topicCategory/MD_TopicC
ategoryCode
provide Topic Category as Theme Keyword
Geographic Extent Bounding Box
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.extent/EX_Extent.geograp
hicElement/EX_GeographicBoundingBox
and
eastBoundLongitude & westBoundLongitude & northBoundLatitude & southBoundLatitude
metadata>idinfo>spdom>bounding
and
westbc & northbc & eastbc & southbc
Temporal Extent of Data Content
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.extent/EX_Extent.tempora
lElement/EX_TemporalExtent.extent
metadata>idinfo>timeperd>timeinfo
Feature Catalogue (Entities and Attributes)
MD_Metadata.content/MD_ContentInformation/MD_FeatureCatalogDescription.featureCatalogCitation
or
MD_Metadata.content/MD_ContentInformation/MD_FeatureCatalog.featureCatalog
MD_CoverageDescription, or MD_ImageDescription
metadata>eainfo
Process Description
MD_Metadata.dataQualityInfo/DQ_DataQuality.lineage/LI_Lineage.processStep/LI_ProcessStep.descrip
tion
metadata/dataqual/lineage/procstep/procdesc
Spatial Reference Information
MD_Metadata.referenceSystemInfo/MD_ReferenceSystem.referenceSystemIdentifier
metadata/spref

                                                                                     26 | P a g e

Metadata Creation Date
MD_Metadata.dateStamp
metadata/metainfo/metd
Metadata Contact Name
MD_Metadata.contact/CI_ResponsibleParty.organizationName
metadata/metainfo/metc/cntinfo/cntorgp/cntorg
Metadata Contact Role Code
MD_Metadata.contact/CI_ResponsibleParty.role
(n/a)

Optional Metadata Elements for the Documentation of Datasets
Purpose
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.purpose
metadata/idinfo/description/purpose
Browse Graphic Filename (thumbnail)
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.graphicOverview/Md_Bro
wseGraphic.fileName
metadata/idinfo/browse/browsen
Browse Graphic File Description
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.graphicOverview/Md_Bro
wseGraphic.fileDescription
metadata/idinfo/browse/browsed
Browse Graphic File Type
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.graphicOverview/Md_Bro
wseGraphic.fileType
metadata/idinfo/browse/browset
Theme Keyword Thesaurus
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.descriptiveKeywords/Md_
Keywords.ThesaurusName
metadata/idinfo/keywords/theme/themekt
Place Keyword
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.descriptiveKeywords/Md_
Keywords.keywords AND Md_Keywords.Type/MD_KeywordTypeCode = ‘Place’
metadata/idinfo/keywords/theme/placekey
Place Keyword Thesaurus
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.descriptiveKeywords/Md_
Keywords.ThesaurusName
metadata/idinfo/keywords/theme/placekt
Access Constraints
MD_Metadata/MD_Identification.indentificationInfo/MD_DataIdentification.resourceConstraints/MD_C
onstraints.accessConstraints
metadata/idinfo/citation/citeinfo/accconst
Currentness Reference
(n/a)
metadata>idinfo>timeperd>current

                                                                                    27 | P a g e

Process Date
MD_Metadata.dataQualityInfo/DQ_DataQuality.lineage/LI_Lineage.processStep/LI_ProcessStep.dateTi
me
metadata/dataqual/lineage/procstep/procdate
Logical Consistency Report
MD_Metadata.dataQualityInfo/DQ_DataQuality.report/DQ_LogicalConsistency
metadata/dataqual/logic
Completeness
MD_Metadata.dataQualityInfo/DQ_DataQuality.report/DQ_Completeness
metadata/dataqual/complete
Metadata Contact Address (Type, City, State, Postal Code)
MD_Metadata.contact/CI_ResponsibleParty.contactInfo/CI_Contact.address/CI_Address.city &
administrativeArea & postalCode
metadata/metainfo/metc/cntinfo/cntaddr/addrtype
and
metadata/metainfo/metc/cntinfo/cntaddr/city & state & postal
Metadata Contact Telephone
MD_Metadata.contact/CI_ResponsibleParty.contactInfo/CI_Contact.phone/CI_Telephone.voice
metadata/metainfo/metc/cntinfo/cntvoice
Metadata Standard Name
MD_Metadata.metadataStandardName
metadata/metstdn
Metadata Standard Version
MD_Metadata.metadataStandardVersion
metadata/metstdv

Additional Elements Required for the Documentation of Services
Metadata Scope
MD_Metadata.hierarchyLevel/MD_ScopeCode
metadata/idinfo/citation/citeinfo/geoform
Service Type
MD_Metadata/MD_Identification.indentificationInfo/SV_ServiceIdentification.serviceType
metadata/idinfo/citation/citeinfo/geoform

                                                                                         28 | P a g e

Appendix 4. ISO Feature Catalog (Entity and Attribute) Information
Features (entities) can be documented in ISO 19115/-1 with far more flexibility than the CSDGM. The
ISO standard provides for the documentation of a feature catalog (entities, attribute labels, definitions,
values, etc.) using either the related ISO 19110 Feature Catalog standard or other feature
documentation such as data dictionaries, data content publications, etc.

Use of ISO 19110 is preferable as it is a standardized representation of the information and, as a
standalone metadata component, a single Feature Catalog record can be applied to multiple datasets,
i.e. document once, use it many. If the dataset features are documented using a different standard or
format, you have the flexibility of referencing the current documentation with the option to transform
the information to ISO 19110 format at a later time.

ISO 19115/-1 also provides flexibility in how you relate the Feature Catalog information to the core
metadata record. Options include:

    •   Document your feature information within the ISO 19115/-1 core metadata record using
        elements from ISO 19110
    •   Provide a reference (Citation) for/to a stand-alone Feature Catalog, or other feature
        documentation
            o If the stand-alone record is an ISO 19110 Feature Catalog record, it can be incorporated
                into the metadata record at any time
            o The advantage of maintaining the Feature Catalog as a separate record is that the
                information is updated and maintained at a central location. This is a benefit for those
                datasets that actively access the most current version of the feature when used. It is not
                appropriate for static datasets that incorporated the feature at some earlier time.
    •   Indicate if the feature information is part of the actual data set.

                                                                                               29 | P a g e

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
