---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4232
title: S4232 – Parcel Data Exchange
doc_type: standard
citation: ITA Standard S4232
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/S4232_Parcel_Data_Exchange_Update3_4_2026.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 7f2b54e50605d37282266df589972861c26910cf324a7cd95fb9a26830ddcd31
effective_date: '2024-11-20'
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

# S4232 – Parcel Data Exchange (ITA Standard S4232)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4232 standardizes the exchange of parcel data, ensuring accurate and efficient property information sharing across state agencies."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category: S4232 – Idaho Parcel Data Exchange Standard

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

A statewide Parcel Framework is a critical source of information for resource land
management, community and economic development needs, infrastructure
maintenance, research and analysis, homeland security, business location intelligence,
public safety, and more. Many private sector and public sector entities have business
needs for Parcel Framework.

III. APPROVED STANDARD(S)

   See Attachment

IV. APPROVED PRODUCT(S)

Please refer to S4250

V. JUSTIFICATION

Experience in other states and countries have demonstrated that accessiblestatewide
cadastral information is key to realizing gains in economic development, public safety,
government efficiency, and citizen empowerment. This standard is to aggregate this
data to the State level.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

This standard requires a minimum of information to share and integrate parcel
information. This standard provides for two levels of sharing: basic information to the
public and enhanced information to governments. Few jurisdictions will have difficulty
implementing the standard if they have GIS capability.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

Data will be shared in accordance with ITA Standard S4250 – Geographic Information
System (GIS) Data Sharing Standards. Furthermore, with continued use and
improvements to “Open Data Portals” it will be easier to publish parcels as an Esri Map,
or REST service through an Open Data Portal

VIII. PROCEDURE REFERENCE

   The format, content and development of this standard adhere to Policy P5030 -
   Framework Standards, ITA Standard S4250 – GIS Data Sharing Standards and ITA
   Standard S4220 - Geospatial Metadata.

IX. REVIEW CYCLE

   Review of this standard will occur at least annually.

X. CONTACT INFORMATION

   For more information, contact the ITA Staff (208) 605-4000.

REVISION HISTORY
Parcels Standard                                                                          2

   11/21/2024 – Standard Presented to the IGC-EC; Updated Standard to reflect new

   attributes.

   07/22/2021 – Updated Standard to reflect new standard attributes and new

   processes.

   05/06/2019 – Removed individual definitions and replaced with reference to ITA

   Guideline G105 (ITA Glossary of Terms)

   07/01/2013 – Changed “ITRMC” to “ITA”.

          Effective Date: May 1,2011

Parcels Standard                                                                    3

                                  STATE OF IDAHO

                     Idaho Parcels Data Standard
                               Part of the Parcels Theme

                                         Version 2.3
                                Effective November 20, 2024

                     Developed by the Parcels Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4000
contact@its.idaho.gov

Parcels Standard                                                        4

CONTENTS
1. Introduction to the Parcel Data Exchange Standard ........................................................ 6
  1.1. Mission and Goals of the Standard............................................................................... 6
  1.2. Relationship to Existing Standards .............................................................................. 6
  1.3. Description of the Standard .......................................................................................... 6
  1.4. Applicability and Intended Uses ................................................................................... 7
  1.5. Standard Development Process..................................................................................... 7
  1.6. Maintenance of the Standard ........................................................................................ 8
2. Body of the Standard ............................................................................................................ 8
  2.1. Scope and Content.......................................................................................................... 8
  2.2. Need ................................................................................................................................. 8
  2.3. Participation in the Standard Development ................................................................ 9
  2.4. Integration with Other Standards ................................................................................ 9
  2.5. Technical and Operation Context................................................................................. 9
     2.5.1. Data Environment................................................................................................... 9
     2.5.2. Reference Systems ................................................................................................... 9
     2.5.3. Global Navigation Satellite System (GNSS) ....................................................... 10
     2.5.4. Interdependence of Themes ................................................................................. 10
     2.5.5. Encoding ................................................................................................................ 10
     2.5.6. Resolution .............................................................................................................. 10
     2.5.7. Accuracy ................................................................................................................ 10
     2.5.8. Edge Matching ...................................................................................................... 10
     2.5.9. Unique Identifier ................................................................................................... 11
     2.5.10.  Attributes ........................................................................................................... 11
     2.5.11.  Stewardship........................................................................................................ 11
     2.5.12.  Records Management and Archiving .............................................................. 11
     2.5.13.  Metadata ............................................................................................................ 11
3. Data Characteristics ........................................................................................................... 11
  3.1. Minimum Graphic Data Elements.............................................................................. 11
  3.2. Optional Graphic Data Elements................................................................................ 12
  3.3. Standard Attribute Schema ........................................................................................ 12
  3.4. Data Quality .................................................................................................................. 15
Appendix A: References .............................................................................................................. 15
Appendix B: Glossary .................................................................................................................. 16

Parcels Standard                                                                                                                             5

1. Introduction to the Parcel Data Exchange Standard

   A statewide Parcel Framework is a critical source of information for resource land
   management, community and economic development needs, infrastructure maintenance,
   research and analysis, homeland security, business development, public safety, and more.
   Many local, state, and federal government agencies and private sector companies have
   business needs for Parcel data.

   A Parcel standard is intended to facilitate integration and sharing of up-to-date parcel data
   and enhance the dissemination and use of parcel information. This standard does not instruct
   on how parcel databases are designed for internal use.

   This standard was developed by the Parcel Technical Working Group (TWG), a subgroup of
   the Idaho Geospatial Council – Executive Committee. This standard will be reviewed on a
   annual basis and updated as needed.

   1.1. Mission and Goals of the Standard

   The Idaho Parcel Data Exchange Standard supports a statewide Parcel Framework dataset
   that is consistent with applicable state and national standards. It establishes the minimum
   attributes and geospatial database schema for the Parcel Framework Layers that will be part
   of The Idaho Map (TIM). This standard encourages all Idaho-based agencies with geospatial
   parcel data to contribute to the Parcel Framework.

   The Parcel Framework will be appropriately shared and beneficial to all. The fields in the
   Parcel Data Exchange Standard will be general enough to incorporate basic information
   without requiring major changes in internal data models. This standard allows for expansion
   into a more complex data structure and schema.

   1.2. Relationship to Existing Standards

   This Parcel Data Exchange Standard relates to various other current standards as follows:
   The Parcel Data Exchange standard follows the same format as other Idaho geospatial
   framework data standards. The Parcel Data Exchange standard may contain some of the same
   attributes as other framework standards and may adopt the field name, definition, and domain
   from the other standards to promote consistency.

   •   ITA Standard S4231 – Structures and Landmarks Data Exchange. Structures and
       Landmarks are tied to a specific parcel.
Parcels Standard                                                                                 6

   •   ITA Standard S4233 – Hydrography Data Exchange. Many parcel boundaries are
       delineated by rivers or streams.
   •   ITA Standard S4234 – Control Point Standard. Control points support mapping the
       true location of parcel polygons.

   1.3. Description of the Standard

   This standard describes the vision and geospatial data structure of a Parcel Framework in the
   state of Idaho. This standard is devised to be:
        • Simple, easy to understand, and logical
        • Uniformly applicable, whenever possible
        • Flexible and capable of accommodating future expansions
        • Dynamic in terms of continuous review

   This standard acknowledges the fact that there is a balance between the effort and
   technological skill to collect and standardize parcel data, versus the number and types of
   attributes available in it for use by parcel data consumers.

   1.4. Applicability and Intended Uses

   This standard applies to the Parcels element of The Idaho Map (TIM).

   When implemented, it will enable access to geographic and attribute information about Idaho
   parcels and improvements built on those parcels. It will increase interoperability between
   automated geographic information systems and enable sharing and efficient transfer of
   information for aggregation. Further, it will encourage partnerships between government, the
   private sector, and the public to avoid duplication of effort and ensure effective management
   of information resources. It will help improve parcel data quality as errors are identified and
   resolved.

   This standard does not consider data sharing agreements, contracts, transactions, privacy
   concerns, or any other issues relating to the acquisition and dissemination of Parcel data.

   1.5. Standard Development Process

   The Parcel Technical Workgroup, a sub-committee under the IGC-EC, is a voluntary group
   of private, city, county, tribal, state, and federal representatives. In 2020, the Parcel Chair
   called for a few volunteers to work on updating the 2012 Parcel Exchange Standard.

Parcels Standard                                                                                     7

   To assess parcel use in Idaho, as well as capabilities and attributes of parcel producers, a
   survey was sent out. As part of the survey 25 respondents identified themselves as “parcel
   consumers” and used the survey to gauge the need for various attributes associated with
   parcel data. Feedback and ratings collected were used to update the 2012 Parcel Data
   Exchange Standard.

   Additionally, reflection on the 2012 standard, and how it may have contributed to the lack of
   progress in the development of a statewide parcel dataset resulted in some of the attributes
   being simplified in the 2021 standard and additional attributes being added in the 2024
   updated standard.

   1.6. Maintenance of the Standard

   This standard will be revised as needed and in accordance with ITA Policy (P5030) -
   Framework Standards Development.

2. Body of the Standard

   2.1. Scope and Content

   The scope of the Parcel Data Exchange Standard is to describe a statewide layer which
   identifies the physical locations and attributes of parcels in Idaho. This standard describes
   three different layers: a polygon layer depicting parcel boundaries, point depicting parcel
   centroids and a table displaying Improvements from the Counties Computer Assisted Mass
   Appraisal System(s). Both polygon and point layer have associated attributes that apply to
   the parcel layer. In contrast, one parcel can contain many improvements and to facilitate the
   one-to-many relationship, attributes associated with a single improvement are stored separately
   in an improvements table.

   2.2. Need

   Parcels are a key dataset needed for resource land managers, community and business
   development needs, infrastructure maintenance, research, homeland security, public safety,
   and more. This standard provides the foundation to aggregate parcel data for centralized
   access and stewardship information.

Parcels Standard                                                                                  8

   2.3. Participation in Standard Development

   The development of the Parcel Data Exchange Standard adheres to ITA Policy (P5030) -
   Framework Standards Development. The Parcel Standard Team tasked with developing this
   standard represents private, county, state, and federal organizations. As the standard is
   reviewed in accordance with ITA Policy (P5030) requirements, there will be an opportunity
   for broad participation and input by stakeholders in the development of this standard. The
   process will be equally broad for input on updates and enhancements to the standard. As with
   all Idaho Framework standards, public review and comments on the Parcel Data Exchange
   Standard are encouraged.

   2.4. Integration with Other Standards

   The Parcel Data Exchange Standard follows the same format as other Idaho geospatial
   framework data standards. The parcel standard may contain some of the same attributes as
   other framework standards and may adopt the field name, definition, and domain from the
   other standards to promote consistency. However, because parcel data is created by county
   assessors to aid the valuation of properties, its attributes such as addresses may not be
   consistent with address fields in other standards.

   2.5. Technical and Operation Context

       2.5.1. Data Environment

       The data environment is a digital model, containing closed vector polygons and vector
       points with a specific, standardized set of attributes pertinent to the Parcel Framework.
       Parcel data shared under this standard must be in a format supporting closed vector
       polygons.

       2.5.2. Reference Systems

       The Parcel Framework will be published in the Idaho Transverse Mercator (IDTM)
       NAD83 coordinate system, which is the State of Idaho’s single zone coordinate system.
       Data is not required to be submitted in the IDTM coordinate system but must have a
       defined coordinate system clearly described in the metadata.

Parcels Standard                                                                                   9

       2.5.3. Global Navigation Satellite System (GNSS)

       Some data provided might contain data collected using GNSS methods such as GPS
       methods, and the provided metadata should describe this, if applicable. However, geometry
       from a GPS is not required to meet this standard.

       2.5.4. Interdependence of Themes

       Parcel geometry may be coincident with other framework data, such as cadastral
       reference, hydrography, roads, and structures. Currently there is no enforcement of
       coincidence or topology relationships between Parcel Framework and other Idaho
       Framework elements.

       2.5.5. Encoding

       When data is imported into and exported from the Parcel Framework, encoding will take
       place to convert data formats and attributes.

       2.5.6. Resolution

       No specific requirements for resolution are specified in this standard. Resolution will be
       documented in the metadata.

       2.5.7. Accuracy

       No specific requirements for accuracy are specified in this standard. Accuracy will be
       documented in the metadata.

       2.5.8. Edge Matching

       No edge matching between jurisdictions is required

Parcels Standard                                                                                10

       2.5.9. Unique Identifier

       There is no requirement for a permanent unique identifier specific to each parcel feature.
       However, it is recommended that users use the Parcel Identification Number in
       combination with the Steward, i.e., County name.

       2.5.10. Attributes

       Attributes for parcel point and polygon layers, as well as the improvement table are
       described in Section 3 of this standard.

       2.5.11. Stewardship

       Perpetual maintenance and other aspects of lifecycle management are essential to Parcel
       Framework. Details of stewards, their roles and responsibilities, and processes are set
       forth in a Parcel Framework Stewardship Plan and related documents.

       2.5.12. Records Management and Archiving

       Details of records management and archiving for Parcel Framework should be set forth in
       a Parcel Framework Stewardship Plan and related documents.

       2.5.13. Metadata

       The Parcel Framework metadata will describe the methods used to aggregate the
       individual parcel data contributions, processes or crosswalks performed, definition of
       attributes, and other required information. This metadata will conform to metadata
       standards as set out in ITA Standard S4220 - Geospatial Metadata) and accompany any
       files exchanged under this Standard.

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The parcel standard consists out of three separate datasets described as follows:

Parcels Standard                                                                                11

   1. Closed vector polygon dataset referred to as “Parcels Layer” that reflect the parcel
      boundary and includes attributes that apply to the entire parcel.
   2. A point vector dataset, referred to as “Parcel Centroids Layer” reflect the calculated
      centroid of a vector parcel boundary polygon. Centroids are calculated mathematically
      using Esri software. For those polygons whose centroid falls outside the parcel polygon,
      the centroid has been forced to move inside the parcel using the “Inside” option in the
      tool (for more information see Feature To Point (Data Management)—ArcGIS Pro |
      Documentation). The Parcel Centroids datasetincludes attributes that apply to the entire
      parcel.
   3. A non-spatial table with improvement information referred to as “Improvement
      Table”.

   3.2. Optional Graphic Data Elements

   Not applicable.

   3.3. Standard Attribute Schema

3.3.1 Attributes for Parcel Polygon and Parcel Centroid Layers

  Field Name            Alias       Data     Leng              Description                Examples
                                    Type      th
 PARCEL_ID         Parcel           Text     50       The unique identifier for that     R3085100110
                   Identification                     parcel is used by the source.
                   Number
 STEWARD           Data Steward     Text     20       The source that created the        Canyon
                                                      polygon and can answer             County
                                                      questions about the history,
                                                      geometry and attribution of it.
 UPDATED           Data Extract     Date              The data the data was shared       5/5/2021
                   Date                               (i.e., data is corrected as of…)
 WEBSITE           Website          Text     255      The URL for public internet        https://
                                                      site for further information, if   adacountyid.g
                                                      available                          ov/assessor/
 FIPS              FIPS Code        Text     5        The Federal Information            16001
                                                      Processing Standards (FIPS)
                                                      code for State and County.
 ASR_ACRRES Legal Acres             Double   Prec:    Acreage as determined by           10.5
                                             12       deed or another instrument
                                             Scale:   that describes the outside of a
                                             4        parcel.

Parcels Standard                                                                                     12

 LAT_DD            Latitude         Double    Prec:    Latitude of the centroid, in    42.15685
                                              8        WGS84 expressed in decimal
                                              Scale:   degrees
                                              5
 LONG_DD           Longitude        Double    Prec:    Longitude of the centroid, in   -116.12545
                                              10       WGS84 expressed in decimal
                                              Scale:   degrees
                                              6
 IDTM_N            Northing         Integer            Y Coordinate of the Centroid.   1219601
                                                       Northing expressed in IDTM
                                                       83 (Meters)
 IDTM_E            Easting          Integer            X Coordinate of the Centroid.   2327704
                                                       Easting expressed in IDTM 83
                                                       (Meters)
 OWNER1            Owner            Text      100      Owner of Parcel                 John Smith
 OWNER2            Owner            Text      100      Owner of Parcel                 Mary Smith
 PUBLIC_STD        Standardized     Text      7        Standardized name of public     Bureau of
                   Public Agency                       agency, e.g. BLM becomes        Land
                                                       Bureau of Land Management       Management
 MAIL_ADD1         Mailing          Text      100      Mailing Address of Owner        1234 S Paper
                   Address 1                                                           Road
 MAIL_ADD2         Mailing          Text      100      Additional Mailing address of   APT 5C
                   Address 2                           owner
 MAIL_CITY         Mailing City     Text      100      Mailing City of Owner           Anaktuvuk
                                                                                       Pass
 MAIL_STATE        Mailing State    Text      2        Mailing State of Owner          AK
 MAIL_ZIP          Mailing Zip      Text      10       Mailing U.S. zip code of        99721
                                                       owner
 MAIL_CNTR         Mailing          Text      100      Mailing Country of Owner        USA
 Y                 Country
 SITE_ADD          Situs Address    Text      100      Site Address of Property        6789 W
                                                                                       Stapler Ave
 SITE_CITY         Situs City       Text      100      City of Property                Boise
 SITE_ZIP          Situs Zip Code   Text      10       Zip Code of Property            83702
 ASR_CATS          Assessment       Text      5        Categories of Property used     12,18,34
                   Categories                          for assessment and taxation.
 LGL_DESCR         Legal Land       Text      512      Property Description            LT 3, BLK 5
                   Description                                                         COPPER
                                                                                       SUB
 VAL_LAND          Value of Land    Long               Gross Land Value of all land    100,000
                                    Integer            inside a parcel (i.e., before the
                                                       deductions of any exemptions)
 VAL_IMPVTS        Value of All     Long               Gross Value Combined value 200,000
                   Improvements     Integer            of all improvements inside a
                                                       parcel (i.e., before the
                                                       deductions of any exemption)
 VAL_TOTAL         Total Value      Long               Gross Total Value (i.e., before 300,000
                                    Integer            the deduction of any
                                                       exemption)

Parcels Standard                                                                                      13

 HOME_EXMP         Homeowners     Boolea                Is there a homeowner’s               True
 T                 Exemption      n                     exemption on this property?
 GIS_ACRES         Computed       Double       Prec:    Acreage as calculated by GIS         11
                   Acres                       12       using the parcel polygon
                                               Scale:   boundary
                                               2

3.3.2 Attributes for Improvement Information Table

 Field Name          Alias      Data      Length                Description                  Examples
                                Type
 PARCEL_ID     Parcel           Text      50            The unique identifier for that   R2085100110
               Identification                           parcel is used by the source.
               Number
 STEWARD       Data Steward     Text      20            The source that created the      Canyon County
                                                        polygon and can answer
                                                        questions about the history,
                                                        geometry and attribution of
                                                        it.
 UPDATED       Data Extract     Date                    The date the data was shared     5/5/2021
               Date                                     (i.e., data is correct as of…)
 WEBSITE       Website          Text      255           The URL for public internet      https://
                                                        site for further information,    adacountyid.gov
                                                        if available                     /assessor/
 YEAR_BLD      Year Built       Integer                 Year Built                       1992
 IMP_TYPE      Improvement      Text      2             Improvement Type (i.e., LR,      RP
               Type                                     MH, RP, etc.)
 IMP_DESCR     Improvement      Text      100           Improvement Description          Mobile Home
               Description                              (i.e., Dwelling, Mobile
                                                        Home, Pavement, etc.)
 EFF_YR_BL     Effective        Integer                 Effective Year Built             1955
 D             Year Built
 TOT_SQFT      Total Square     Integer                 Total Square Feet                2,100
               Feet
 EST_VAL       Estimated        Integer                 Estimated Value                  1,250,000
               Value
 NUM_STOR      Number of        Double                  Number of Stories                2
 Y             Stories
 NUM_BATH      Number of        Double                  Number of Bathrooms              2.5
               Bathrooms
 NUM_BED       Number of        Double                  Number of Bedrooms               2.5
               Bedrooms
 GARAGE_Y      Presence of a    Text      1             Presence of a Garage             Y
 _N            Garage
 SQFT_FLR_     Square Feet      Integer                 Square Feet First Floor          1500
 1             First Floor
 SQFT_FLR_     Square Feet      Integer                 Square Feet Second Floor         600
 2             Second Floor

Parcels Standard                                                                                        14

 SQFT_BSM       Square Feet     Integer               Square Feet Basement       1100
 NT             Basement
 HEAT_TYPE      Type of         Text      50          Type of Heating            Central Gas
                Heating
 FIRPLC_Y_      Presence of a   Text      5           Presence of a Fireplace    Y
 N              Fireplace
 NUM_FIREP      Number of       Integer               Number of Fireplaces       2
 L              Fireplace(s)

   3.4. Data Quality

   Data quality considerations for Parcels include:
   a) All attribute tables, i.e., those included with the polygon and centroid parcel layers, as
      well as the improvement table should at the very least include a PARCEL_ID,
      STEWARD and UPDATED date. The attributes for WEBSITE and FIPS will be added
      by data aggregator.
   b) All parcel polygons should close.
   c) All centroids should be located into the polygon on which the centroid is based.
   d) Parcel boundary shapes are generated by individual counties and the data quality
      depends on the procedures in place at the county where a parcel resides.
   e) Topology rules, either within a county or between counties, are encouraged but not
      enforced. Therefore, it is possible that parcels overlap within or between counties.

Appendix A: References

Federal Geographic Data Committee (FGDC), Subcommittee on Cadastral Data, May 2008.
Cadastral Data Content Standard for the National Spatial Data Infrastructure,Version 1.4.
https://www.fgdc.gov/standards/projects/cadastral/cadastral-data-standard-v1-4.pdf

Environmental Systems Research Institute (ESRI). Internet. http://www.esri.com

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/p5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/s4220.pdf

FGDC Cadastral Subcommittee Outreach Web site. Cadastral Data Standards and Guidelines.
Cadastral Subcommittee — Federal Geographic Data Committee (fgdc.gov)

Parcels Standard                                                                               15

Appendix B: Glossary

See ITA Guideline G105 - (ITA Glossary of Terms) for definitions.

Parcels Standard                                                    16

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
