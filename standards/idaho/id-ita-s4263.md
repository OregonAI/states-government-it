---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4263
title: S4263 – Idaho Dam Inventory
doc_type: standard
citation: ITA Standard S4263
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/S4263-ADA.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 92c81e4fb320fcf0260c346f8aae460801fc67ffbf4188fed7bf3f8b361a47bf
effective_date: '2023-07-20'
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). Pages 13 of the PDF have no text layer (figures, blank pages or scanned forms) and add no
  text here.
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

# S4263 – Idaho Dam Inventory (ITA Standard S4263)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4263 outlines management and data-sharing protocols for the Idaho Dam Inventory, supporting infrastructure assessment and water resource planning." The last page of the PDF (13) is blank (checked by rendering it), so it is listed as no_text_pages.

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category:    S4263 – Dam Inventory Standard

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
XI. Additional Information (if any)
      Revision History

I. DEFINITION

   See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

II. RATIONALE

   A statewide Dam Inventory layer and data standard, which is part of the Hazards
   data theme, is a critical source of information for land managers, emergency
   managers, transportation engineers, developers, and researchers. Standardized
   landslide inventory data supports those groups by providing an authoritative,
   centralized, statewide database.

III. APPROVED STANDARD(S)

   See Attachment

IV. APPROVED PRODUCTS(S)

  Any GIS Software, either desktop or online, capable of ingesting and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

V. JUSTIFICATION

  A statewide Dam Inventory dataset is a critical source of information, as stated
  under ‘II Rationale’ in this standard. A data exchange standard supports the use of
  the Dam Inventory dataset to facility a predictable format, improve collaboration and
  encourage of this dataset.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

  Any GIS Software, either desktop or online, capable of ingesting and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

  Data will be shared in accordance with ITA Standard S4250 –Geographic
  Information System (GIS) Data Sharing Standards.

VIII. PROCEDURE REFERENCE

  The format, content, and development of this standard adhere to ITA Policy P5030 -
  Framework Standards, ITA Standard S4250 - Data Sharing Standards and ITA
  Standard S4220 - Geospatial Metadata.

IX. REVIEW CYCLE

  Review will occur at least annually.

X. CONTACT INFORMATION

  For more information, contact the ITA Staff at (208) 605-4064.

REVISION HISTORY

  07/20/2023 – Standard Presented to the IGC-EC

                                                                                      2

                                  STATE OF IDAHO

                   Idaho Dam Inventory Standard
                                Part of the Other Theme

                                          Version 1
                                   Effective July 20, 2023

                      Developed by the Other Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4064
contact@its.idaho.gov

                                                                       3

CONTENTS
1. Introduction to the Dam Inventory Standard .................................................................... 5
  1.1. Mission and Goals of the Standard............................................................................... 5
  1.2. Relationship to Existing Standards .............................................................................. 5
  1.3. Description of the Standard .......................................................................................... 5
  1.4. Applicability and Intended Uses ................................................................................... 6
  1.5. Standard Development Process..................................................................................... 6
  1.6. Maintenance of the Standard ........................................................................................ 7
2. Body of the Standard ............................................................................................................ 7
  2.1. Scope and Content .......................................................................................................... 7
  2.2. Need ................................................................................................................................. 7
  2.3. Participation in the Standard Development ................................................................ 7
  2.4. Integration with Other Standards ................................................................................ 7
  2.5. Technical and Operation Context ................................................................................. 8
     2.5.1. Data Environment................................................................................................... 8
     2.5.2. Reference Systems................................................................................................... 8
     2.5.3. Global Positioning Systems (GPS)......................................................................... 8
     2.5.4. Interdependence of Themes ................................................................................... 8
     2.5.5. Encoding .................................................................................................................. 8
     2.5.6. Resolution ................................................................................................................ 9
     2.5.7. Accuracy .................................................................................................................. 9
     2.5.8. Edge Matching ........................................................................................................ 9
     2.5.9. Unique Identifier ..................................................................................................... 9
     2.5.10.  Attributes ............................................................................................................. 9
     2.5.11.  Stewardship.......................................................................................................... 9
     2.5.12.  Records Management and Archiving ................................................................ 9
     2.5.13.  Metadata .............................................................................................................. 9
3. Data Characteristics ........................................................................................................... 10
  3.1. Minimum Graphic Data Elements.............................................................................. 10
  3.2. Optional Graphic Data Elements................................................................................ 10
  3.3. Standard Attribute Schema..........................................Error! Bookmark not defined.
  3.4. Data Quality .................................................................................................................. 11
Appendix A: References .............................................................................................................. 11
Appendix B: Glossary .................................................................................................................. 12

                                                                                                                                             4

1. Introduction to the Dam Inventory Standard

  A statewide Dam Inventory is a critical source of information for land managers, emergency
  managers, transportation engineers, developers, and researchers. Those groups will benefit
  from this data because this standard is an authoritative, centralized, statewide landslide
  inventory. Many private sector and local, state, and federal government agencies have
  business needs for landslide inventory data.

  A Dam Inventory Standard is intended to facilitate integration and sharing of up-to-date Dam
  Inventory data and enhance the dissemination and use of Dam Inventory information. This
  standard does not instruct on how Dam Inventory databases are designed for internal use.

  This standard was developed by the Hazards Technical Working Group, a subgroup of the
  Idaho Geospatial Council – Executive Committee (IGC-EC). This standard will be reviewed
  at least annually and updated as needed.

  1.1. Mission and Goals of the Standard

  The Dam Inventory Standard supports a statewide dataset that is consistent with applicable
  state and national standards. It establishes the minimum attributes and geospatial database
  schema for the Dam Inventory Framework. The standard will communicate with, and may
  have similar attributes to, other Idaho Framework data standards. It encourages all Idaho-
  based agencies with geospatial Dam Inventory data to contribute to the Dam Inventory
  Framework.

  The Dam Inventory Framework will be appropriately shared and beneficial to all. The fields
  in the Dam Inventory Data Exchange Standard will be general enough to incorporate basic
  information without requiring major changes in internal data models. This standard allows
  for expansion to a more complex data structure and schema.

  1.2. Relationship to Existing Standards

  This Dam Inventory Exchange Standard relates to existing standards as follows:

         •   No other standards apply.

                                                                                                5

1.3. Description of the Standard

This standard describes the vision and geospatial data structure of a Dam Inventory
Framework in the state of Idaho. This standard is devised to be:

    •   Simple, easy to understand, and logical.
    •   Uniformly applicable, whenever possible
    •   Flexible and capable of accommodating future expansions
    •   Dynamic in terms of continuous review

1.4. Applicability and Intended Uses

This standard applies to the Dam Inventory element of the Hazards theme of The Idaho Map
(TIM).

When implemented, this standard will enable access to, and exchange of, Idaho’s dam data
for both existing use and future planning. A predictable standard will support data
collaboration, improve data collection techniques, help identify and report errors, correct
inaccurate entries, and allow a variety of agencies to incorporate this data into their own data
products with some known level of confidence in the veracity of the product.

This standard does not consider data sharing agreements, contracts, transactions, privacy
concerns, or any other issues relating to the acquisition and dissemination of Dam Inventory
data.

1.5. Standard Development Process

The Hazards Technical Working Group is a voluntary group of private, city, county, tribal,
state, and federal representatives. In 2023, the Dam Inventory Lead began developing the
standard for the Dam Inventory Framework using the standard development automation tools
developed by the IGC-EC to generate the first draft of the Standard. This standard was then
reviewed and edited by the members of the Hazards Technical Working Group.
After initial development, the draft standard document was shared with the Idaho Geospatial
Council Executive Committee (IGC-EC) and the Idaho Geospatial Council (IGC) in
accordance with the review and approval process described in ITA Policy P5030 Framework
Standards Development.

                                                                                               6

   1.6. Maintenance of the Standard

   This standard will be revised on an annual basis and as needed and in accordance with the
   ITA Framework Standards Development Policy (P5030).

2. Body of the Standard

   2.1. Scope and Content

   The scope of the Dam Inventory Data Exchange Standard is to describe a statewide layer
   which identifies the physical locations and attributes of mapped dams in Idaho.

   2.2. Need

   Dam Inventory maps are a key dataset needed for land managers, emergency managers,
   transportation engineers, developers, and researchers. This standard provides the foundation
   to aggregate dam data for centralized access and stewardship information.

   Dam Inventory data is needed because public access to locations of significant land features,
   such a water storage dams, benefits a vast audience; the list is nearly endless.

   2.3. Participation in the Standard Development

   The development of the Dam Inventory Data Exchange Standard adheres to the ITA Policy
   P5030 - Framework Standards Development. The Other Standard Team tasked with
   development, invite input and comments from private, county, state, and federal
   organizations. As the standard is reviewed in accordance with Policy P5030 requirements,
   there will be opportunity for broad participation and input by stakeholders. The process will
   be equally broad for input on updates and enhancements to the standard. As with all Idaho
   Framework standards, public review and comment on the Dam Inventory Data Exchange
   Standard is encouraged.

   2.4. Integration with Other Standards

   The Dam Inventory Data Exchange Standard follows the same format as other Idaho
   geospatial framework data standards. The Dam Inventory standard may contain some of the
   same attributes as other framework standards and may adopt the field name, definition, and
   domain from the other standards to promote consistency.

                                                                                                   7

2.5. Technical and Operation Context

   2.5.1. Data Environment

   The data environment is a digital vector point with a specific, standardized set of
   attributes pertinent to the Dam Inventory Framework. Dam Inventory data shared under
   this standard must be in a format supporting vector points.

   2.5.2. Reference Systems

   The Dam Inventory Framework will be published in the Idaho Transverse Mercator
   NAD83 (IDTM83) coordinate system, which is the State of Idaho’s single-zone
   coordinate system. Data is not required to be submitted in the IDTM83 coordinate system
   but must have a defined coordinate system clearly described in the metadata.

   2.5.3. Global Positioning Systems (GPS)

   Some data provided might contain geometry from GPS methods, and the provided
   metadata should describe this, if applicable.

   2.5.4. Interdependence of Themes

   Dam Inventory geometry data may coincide with other framework data. For example, the
   aerial extent of the dam and the impounded reservoir must coincide exactly to the real
   property on which they both occupy. Vertical layers also must coincide, i.e., height,
   elevation, and bathymetry.

   Attributes found in the Dam Inventory layer are related to the attributes found in the
   elevation data sets.

   2.5.5. Encoding

   When data is imported into and exported from the Dam Inventory Framework, encoding
   will take place to convert data formats and attributes.

                                                                                            8

2.5.6. Resolution

Resolution will be documented in the metadata.

2.5.7. Accuracy

No specific requirements for accuracy are specified in this standard. Accuracy will be
documented in the metadata.

2.5.8. Edge Matching

No edge matching between jurisdictions is required.

2.5.9. Unique Identifier

The unique identifier is DamID, which a computer generated ID that is unique for Idaho.

2.5.10. Attributes

Attributes for public and intergovernmental distribution are described in Section 3 of this
standard.

2.5.11. Stewardship

Perpetual maintenance and other aspects of lifecycle management are essential to Dam
Inventory Framework. Details of stewards, their roles and responsibilities, and processes
are set forth, or are being planned to set forth in a Dam Inventory Framework
Stewardship Plan and related documents.

2.5.12. Records Management and Archiving

Data are managed by the Idaho Department of Water Resources and hosted on ArcGIS
Online.

2.5.13. Metadata

                                                                                            9

          The Dam Inventory Framework metadata will describe the methods used to update and
          aggregate the individual Dam Inventory data contributions, processes or crosswalks
          performed, definition of attributes, and other required information. This metadata will
          conform to the metadata standards as set out in ITA Standard S4220 Geospatial Metadata.

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The geometry of the features in the Dam Inventory Framework is vector point.

   3.2. Optional Graphic Data Elements

   Not applicable.

   3.3. Standard Attribute Schema

                                 Data
          Field Name                       Length            Description                  Examples
                                 Type
                                                      Computer-generated unique
 DamID                          Integer               ID for each dam record         142
 NIDID                          String    20          National Dam ID                ID06064
                                                      Water right number
                                                      associated with dam for
                                                      storage or power purposes;
                                                      if it includes XXX, no water
                                                      right is associated with the   17-2000,
 StateID                        String    20          dam                            27-xx15
 DamName                        String    100         Name of dam                    SMITH POND
                                                                                     REGULATED
                                                                                     NON
 Status                         String    20          Status of dam                  REGULATED
                                                      Year dam construction was
 YearCompleted                  Integer               finished                       1975
                                                      Most recent year dam
                                                      construction was modified
 YearModified                   Integer               from original specifications   2005
                                                      Height of dam in feet
                                                      measured from original
 DamHeight                      Double                ground surface to top          35
                                                      Height in feet from original
                                                      ground surface to pool
 HydraulicHeight                Double                elevation                      29

                                                                                                     10

                              Data
        Field Name                     Length               Description            Examples
                              Type
                                                  Storage in acre feet of the
                                                  impounded water at design
 NormalStorage              Double                pool elevation                 880
                                                  Surface area in acres of
                                                  impounded water at design
 SurfaceArea                Double                pool elevation                 54.00
                                                  Drainage area in square
 DrainageArea               Double                miles above dam location       26.60
                                                  Risk to property               HIGH, LOW,
 DownStreamHazardPotentia                         downstream of dam in event     NOT RATED,
 l                          String     20         of dam failure                 SIGNIFICANT
                                                  Stream on which or nearest
                                                  to which the dam is
 Source                     String     100        constructed                    BIRCH CREEK
 SourceQualifier            String     100        Qualifier to stream            WEST FORK
                                                  Stream is tributary to this
 TributaryOf                String     100        stream                         BEAR RIVER
                                                  Qualifier to TributaryOf
 TributaryOfQualifier       String     100        stream                         SOUTH FORK
                                                  Method used to create the      Digitized, GPS
 DataSource                 String     550        point for the dam’s location   - Downloaded
                                                  Metal tag affixed to the dam
 MetalTagNumber             String     8          or nearby                      A0000111
                                                  Concatenation of Public
                                                  Land Survey
                                                  Township/Range/Section
 TRS                        String     36         the dam is located within      09N42E28
 County                     String     50         County dam in located in       FREMONT
 SpatialDataID              Integer                                              486796

   3.4. Data Quality

   Data quality considerations for Dam Inventory include:
       a) All Dam Inventory should have Dam Inventory IDs.

Appendix A: References

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/P5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
                                                                                              11

Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/S4220.pdf

Idaho Department of Water Resources (IDWR). Dams of Idaho, Status and Downstream Hazard
Potential. https://maps.idwr.idaho.gov/agol/DamsofIdaho/

Appendix B: Glossary

See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

                                                                                          12

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). Pages 13 of the PDF have no text layer (figures, blank pages or scanned forms) and add no text here.
