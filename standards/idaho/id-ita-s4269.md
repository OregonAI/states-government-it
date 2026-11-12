---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4269
title: S4269 – Public Land Survey System Data Exchange
doc_type: standard
citation: ITA Standard S4269
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/10/S4269-ADA.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 9fbf7d047d506e2e830acf188e3dc642292cf482049b7b3b5bf2a070b7bd458c
effective_date: '2025-03-03'
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

# S4269 – Public Land Survey System Data Exchange (ITA Standard S4269)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4269 defines Idaho’s statewide PLSS data layer, ensuring accurate control points for consistent mapping, land, and infrastructure data."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category:    S4269 – Public Land Survey System Data Exchange

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
      Revision History

I. DEFINITION

   See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

II. RATIONALE

   A statewide Public Land Survey System (PLSS) data layer and data standard, which
   is part of the Cadastral Reference data theme, is a critical source of information for
   control points. The PLSS representation based on those control points are a
   foundational dataset on which most other datasets (parcels, boundaries, roads, etc.)
   are built on, or referenced to. Accurate control and subsequent accurate PLSS data
   ensures that all other datasets based on this foundation are spatially accurate and
   line up with each other. This dataset and the standards describing this dataset
   benefit all users of spatial data including, but not limited to, agencies dealing with
   real estate, agriculture, government, boundaries, and transportation. Standardized
   PLSS data supports those groups by providing an authoritative understanding of the
   dataset and access to PLSS data in an Idaho specific view.

III. APPROVED STANDARD(S)

  See Attachment

IV. APPROVED PRODUCT(S)

  Any GIS software, either desktop or online, capable of processing and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

V. JUSTIFICATION

  A statewide PLSS Data Layer dataset is a critical source of information as stated
  under Part II in this standard. A data exchange standard supports the use of the
  PLSS Data Layer to facilitate a predictable format, improve collaboration and
  encourage use of this dataset.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

  Any GIS Software, either desktop or online, capable of processing and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

  Data will be shared in accordance with ITA Standard S4250 – Geographic
  Information System (GIS) Data Sharing Standards.

VIII. PROCEDURE REFERENCE

  The format, content and development of this standard adhere to ITA Policy P5030 -
  Framework Standards, ITA Standard S4250 - Data Sharing Standards and ITA
  Standard S4220 - Geospatial Metadata.

IX. REVIEW CYCLE

  Review will occur at least annually.

X. CONTACT INFORMATION

  For more information, contact the ITA Staff at (208) 605-4000.

REVISION HISTORY

  03/20/2025 – Standard Presented to the IGC-EC

                                                                                      2

                                  STATE OF IDAHO

    Idaho Public Land Survey System Data Exchange
                        Part of the Cadastral Reference Theme

                                         Version 1
                                  Effective March 3, 2025

               Developed by the Cadastral Reference Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4000
contact@its.idaho.gov

                                                                              3

CONTENTS

1. Introduction to the Public Land Survey System Data Exchange ......................................... 6
     1.1.     Mission and Goals of the Standard ............................................................................. 6
     1.2.     Relationship to Existing Standards ............................................................................. 6
     1.3.     Description of the Standard ......................................................................................... 7
     1.4.     Applicability and Intended Uses.................................................................................. 7
     1.5.     Standard Development Process ................................................................................... 7
     1.6.     Maintenance of the Standard....................................................................................... 8
2.     Body of the Standard ............................................................................................................ 8
     2.1.     Scope and Content ........................................................................................................ 8
     2.2.     Need ................................................................................................................................ 8
     2.3.     Participation in the Standard Development............................................................... 8
     2.4.     Integration with Other Standards............................................................................... 8
     2.5.     Technical and Operation Context ............................................................................... 9
       2.5.1.        Data Environment................................................................................................. 9
       2.5.2.        Reference Systems................................................................................................. 9
       2.5.3.        Global Positioning Systems (GPS)....................................................................... 9
       2.5.4.        Interdependence of Themes ................................................................................. 9
       2.5.5.        Encoding ................................................................................................................ 9
       2.5.6.        Resolution ............................................................................................................ 10
       2.5.7.        Accuracy .............................................................................................................. 10
       2.5.8.        Edge Matching .................................................................................................... 10
       2.5.9.        Unique Identifier................................................................................................. 10
       2.5.10.       Attributes ............................................................................................................. 10
       2.5.11.       Stewardship ......................................................................................................... 10
       2.5.12.       Records Management and Archiving................................................................ 11
       2.5.13.       Metadata .............................................................................................................. 11
3.     Data Characteristics ........................................................................................................... 11
     3.1.     Minimum Graphic Data Elements ............................................................................ 11
     3.2.     Optional Graphic Data Elements .............................................................................. 11
     3.3.     Standard Attribute Schema ....................................................................................... 11
                                                                                                                                                   4

       3.3.1.       Townships ............................................................................................................. 11
       3.3.2.       Sections.................................................................................................................. 12
       3.3.3.       Secondary Divisions ............................................................................................. 12
       3.3.4.       Special Surveys..................................................................................................... 13
       3.3.5.       Meanders .............................................................................................................. 13
   3.4.       Data Quality ................................................................................................................ 13
Appendix A: References .............................................................................................................. 14
Appendix B: Glossary.................................................................................................................. 14

                                                                                                                                               5

1. Introduction to the Public Land Survey System Data Exchange

  A statewide Public Land Survey System (PLSS) data layer and data standard, which is part of
  the Cadastral Reference data theme, is a critical source of information for control points. The
  PLSS representation based on those control points are a foundational dataset on which most
  other datasets (parcels, boundaries, roads, etc.) are built on, or referenced to. Accurate
  control and subsequent accurate PLSS data ensures that all other datasets based on this
  foundation are spatially accurate and line up with each other. This dataset and the standards
  describing this dataset benefit all users of spatial data including, but not limited to, agencies
  dealing with real estate, agriculture, government, boundaries, and transportation.
  Standardized PLSS Data supports those groups by providing an authoritative understanding
  of the dataset and access to PLSS data in an Idaho specific view.

  A PLSS Data Layer Standard is intended to facilitate integration and sharing of up-to-date
  PLSS Layer data and enhance the dissemination and use of PLSS Data Layer information.
  This standard does not instruct on how PLSS Data Layer databases are designed for internal
  use.

  This standard was developed by the Cadastral Reference Technical Working Group, a
  subgroup of the Idaho Geospatial Council – Executive Committee (IGC-EC). This standard
  will be reviewed on an annual basis and updated as needed.

  1.1. Mission and Goals of the Standard

  The PLSS Data Layer Standard supports a statewide dataset that is consistent with applicable
  state and national standards. It establishes the minimum attributes and geospatial database
  schema for the PLSS Data Layer Framework. This standard will communicate with and may
  have similar attributes to other Idaho Framework data standards. It encourages all Idaho-
  based agencies with geospatial PLSS Layer data to contribute to PLSS Data Layer
  Framework.

  The PLSS Data Layer Framework will be appropriately shared and beneficial to all. The
  fields in the PLSS Layer Data Exchange Standard will be general enough to incorporate basic
  information without requiring major changes in internal data models. This standard allows
  for expansion to a more complex data structure and schema.

  1.2. Relationship to Existing Standards

  This PLSS Data Layer Exchange Standard relates to existing standards as follows: Metadata
  is provided in accordance with ITA Standard S4220 - Geospatial Metadata, and this standard
  is created and approved in accordance with ITA Policy P5030 - Framework Standards
                                                                                                 6

Development Policy. PLSS data needs to follow BLM regulations for cadastral surveys
including the Manual for Surveying Instructions (2009), and Specifications for Descriptions
of Land (2017). This PLSS standard is related to any dataset based on PLSS data including
ITA Standard S4235 - Legislative and Congressional Boundaries, ITA Standard S4232 -
Parcel Exchange Standard. The standard is related to the National States Data Infrastructure
Standard for Cadastral Reference. The data is also related to the Multi-State Control Point
(MCPD) Standard.

1.3. Description of the Standard
This standard describes the vision and geospatial data structure of a PLSS Data Layer
Framework in the state of Idaho. This standard is devised to be:
     • Simple, easy to understand, and logical
     • Uniformly applicable, whenever possible
     • Flexible and capable of accommodating future expansions
     • Dynamic in terms of continuous review

1.4. Applicability and Intended Uses

This standard applies to the PLSS Layer element of the Cadastral Reference theme of The
Idaho Map (TIM).

When implemented this standard will enable access to the data. A predictable standard will
support and improve data collaboration, help identify and report errors and allow agencies to
incorporate this data into their own data products.

This standard does not consider data sharing agreements, contracts, transactions, privacy
concerns, or any other issues relating to the acquisition and dissemination of PLSS Layer
data.

1.5. Standard Development Process

The Cadastral Reference Technical Working Group is a voluntary group of private, city,
county, tribal, state, and federal representatives. In 2024 the PLSS Data Layer lead began
developing the standard for the PLSS Layer Framework. This standard was then reviewed
and edited by the members of the Cadastral Reference Technical Working Group.
After initial development the draft standard document was shared with the Idaho Geospatial
Council Executive Committee (IGC-EC) and the Idaho Geospatial Council (IGC) in
accordance with the review and approval process described in ITA Policy P5030 -
Framework Standards Development.

                                                                                               7

   The standard was presented to the IGC-EC in March 2025.

   1.6. Maintenance of the Standard

   This standard will be reviewed annually and in accordance with the ITA Policy P5030 -
   Framework Standards Development.

2. Body of the Standard

   2.1. Scope and Content

   The scope of the PLSS Layer Data Exchange Standard is to describe a statewide layer which
   identifies the physical locations and attributes of PLSS Data Layers in Idaho.

   2.2. Need

   PLSS Data Layers are a key dataset needed for control points, and the PLSS (PLSS)
   representation based on those control points are the most foundational dataset on which most
   other datasets (parcels, boundaries, roads, etc.) are built on, or referenced to. Accurate
   control and subsequent accurate PLSS ensure that all data based on this foundation are
   spatially accurate and line up with each other. This standard provides the foundation to
   aggregate the PLSS Layer data for centralized access and stewardship information.

   Accurate PLSS data is needed to ensure spatial accuracy and alignment of spatial datasets in
   Idaho.

   2.3. Participation in the Standard Development

   The development of the PLSS Layer Data Exchange Standard adheres to the ITA Policy
   P5030 - Framework Standards Development. The Cadastral Reference Standard Team tasked
   with developing this standard invite input and comments from private, county, state, and
   federal organizations. In accordance with ITS Policy P5030 requirements, there will be
   opportunity for broad participation and input by stakeholders in the development of this
   standard. The process will be equally broad for input on updates and enhancements to the
   standard. As with all Idaho Framework standards, public review, and comments on the PLSS
   Layer Data Exchange Standard is encouraged.

   2.4. Integration with Other Standards

   The PLSS Layer Data Exchange Standard follows the same format as other Idaho geospatial
   framework data standards. The PLSS Layer standard may contain some of the same attributes
                                                                                                  8

as other framework standards and may adopt the field name, definition, and domain from the
other standards to promote consistency.

2.5. Technical and Operation Context

   2.5.1. Data Environment

   The data environment is a digital vector polygon with a specific, standardized set of
   attributes pertinent to the PLSS Data Layer Framework. PLSS Layer data shared under
   this standard must be in a format supporting vector polygons.

   2.5.2. Reference Systems

   The PLSS Data Layer Framework will be published in the Idaho Transverse Mercator
   (IDTM) NAD83 coordinate system, which is the State of Idaho’s single-zone coordinate
   system. Data is not required to be submitted in the Idaho Transverse Mercator (IDTM)
   NAD83 coordinate system but must have a defined coordinate system clearly described
   in the metadata.

   2.5.3. Global Positioning Systems (GPS)

   Some data provided might contain data collected using GNSS methods such as GPS, and
   the metadata provided should describe this, if applicable. Geometry from GPS sources is
   not required to meet this standard.

   2.5.4. Interdependence of Themes

   The PLSS Layer has geometry data that should be coincident with other framework data,
   for example, data in the PLSS should be coincident with many Idaho boundary datasets
   (counties, legislative boundaries, roads, parcels, water right PODs and POUs, etc.).

   Attributes found in the PLSS Data Layer are related to the attributes found in some legal
   descriptions in the statewide Parcel Layer, but not all Parcel Layer records rely on PLSS
   data.

   2.5.5. Encoding

   When data is imported into and exported from the PLSS Data Layer Framework,
   encoding will take place to convert data formats and attributes.

                                                                                               9

2.5.6. Resolution

No specific requirements for resolution are specified in this standard. Resolution will be
documented in the metadata.

2.5.7. Accuracy

Per the United States Geological Survey, “PLSS was created to divide parcels of public
land; it is not useful for the accurate location of points and should not be confused with
coordinate systems like latitude/longitude, UTM, or the State Plane Coordinate System”.
Every effort will be made to ensure the most accurate representation of the PLSS grid and
polygons, but there is no definite accuracy standard required.

2.5.8. Edge Matching

Section boundaries need to be edge-matched with aliquot parts or government lots.
Township boundaries need to be edge-matched with section boundaries. Aliquot parts
and government lots need to be edge-matched to each other. Sections need to be edge-
matched with other sections and townships need to be edge-matched with other
townships.

2.5.9. Unique Identifier

The field for Unique Identifier is different for each part of the PLSS Layer as follows:
Townships – PLSSID field
Sections – FIRSTDIVID field
Secondary Division – SECDIVID field
Special Surveys – SURVID field

2.5.10. Attributes

Attributes for public and intergovernmental distribution are described in Section 3 of this
standard.

2.5.11. Stewardship

Perpetual maintenance and other aspects of lifecycle management are essential to PLSS
Data Layer Framework. Details of stewards, their roles and responsibilities, and
processes are set forth, or are being planned to set forth in a PLSS Data Layer Framework
Stewardship Plan and related documents.

                                                                                           10

      2.5.12. Records Management and Archiving

      The source data for the PLSS is provided by the Bureau of Land Management, and state
      specific edits for accuracy are performed by the State of Idaho Data and Spatial Services
      team. These PLSS updates are done in part using the Multi State Control Point Dataset
      hosted by Idaho State University. The dataset will be hosted on ArcGIS Online by the
      State of Idaho.

      2.5.13. Metadata

      The PLSS Data Layer Framework metadata will describe the methods used to update and
      aggregate the individual PLSS Data Layer data contributions, processes or crosswalks
      performed, definition of attributes, and other required information. This metadata will
      conform to the metadata standards as set out in ITA Standard S4220 - Geospatial Metadata.

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The geometry of the features in PLSS Data Layer Framework is vector polygon

   3.2. Optional Graphic Data Elements

   Not applicable.

   3.3. Standard Attribute Schema

   The PLSS dataset consists of 5 different layers:
            1. Townships
            2. Sections
            3. Secondary Divisions
            4. Special Surveys
            5. Meanders

      3.3.1. Townships

  Field Name         Data Type   Length           Description                Examples
 OBJECTID               OID                Object ID                  1
 PLSSID                String       16     Township Label             ID080010N0250E0
 STATEABBR             String        2     State Abbreviation         ID
 PRINMERCD             String        2     Principal Meridian Code    08
                                                                                             11

PRINMER            String         40    Principal Meridian Text     Boise Meridian
TWNSHPNO           String          3    Township Number             01
TWNSHPFRAC         String          1    Township Fraction           0
TWNSHPDIR          String          1    Township Direction          N
RANGENO            String          3    Range Number                25
RANGEFRAC          String          1    Range Fraction              0
RANGEDIR           String          1    Range Direction             E
TWNSHPDPCD         String          1    Township Duplicate          0
TWNSHPLAB          String         20    Township Label              01N 25E
SOURCEDATE         Date            8    Source Date (short)         01/01/2024
                                        Source Doc Link or
SOURCEREF          String         100   Reference                   Source

     3.3.2. Sections

 Field Name    Data Type    Length             Description                   Examples
OBJECTID           OID                  Object ID                   1
FRSTDIVID         String      22        First Division ID           ID080040N0030W0SN010
PRINMERIDIAN      String      08        Prime Meridian              08
TOWNSHIP          String      10        Township                    04N
RANGE             String      10        Range                       03W
SECTION           String       4        Township Range Section      01
SECTIONLAB        String      12        Township Range Section      04N 03W 01
FRSTDIVTXT        String      50        Section Type                Section
LAST_UPDATED      Date                  Record Last Edited Date     7/1/2024

     3.3.3. Secondary Divisions

                  Data
 Field Name                 Length           Description                 Examples
                  Type
OBJECTID           OID                  Object ID                 1
SECDIVID          String      26        Second Division ID        ID080040N0020E0SN300L6
PRINMERIDIAN      String      2         Prime Meridian            08
TOWNSHIP          String      10        Township                  04N
RANGE             String      10        Range                     02E
SECTION           String      4         Township Range Section    30
RNGPARTIAL        String      5         Range Partial             2W
QSEC              String      4         Quarter Section           NW
QQSEC             String      4         Quarter Quarter Section   NE
SECDIVLAB         String      50        Second Division Label     L6 or NENW
                                                                                           12

                                             Secondary Division Type
SECDIVTYP
                      String        2        Code                       A , L, or T
                                             ID Number of all surveys
SURVEYNUMBER
                   String           5        of type                    05
LEGALACRES         Double                    Legal Acres                40.2
GISACRES           Double                    Calculated                 38.7
LAST_UPDATED        Date                     Record Last Edited Date    7/1/2024

     3.3.4. Special Surveys

 Field Name      Data Type      Length             Description                        Examples
OBJECTID            OID                      Object ID                  1
SURVID             String           26       Special Survey ID          ID080460N0040W0SN180N11
SURVTYP            String            2       Survey Type                N
SURVTYPTXT         String           50       Survey Type Text           Townsite Survey
SURVDIVNO          String           50       Survey Number              11
SURVLAB            String           50       Survey Label               N 11
RECRDACRES         String           20       Record Area Text           2671
GISACRES           Double                    Record Area Number         2501.5
LAST_UPDATED        Date                     Record Last Edited Date    7/1/2024

     3.3.5. Meanders

   Field Name           Data Type        Length         Description                   Examples
OBJECTID               OID                           Object ID            1
SURVTYP                String           1                                 W
SURVTYPTXT             String           20           Survey Type Text     Meander

  3.4. Data Quality

  Data quality considerations for PLSS Data Layers include:
     a) All PLSS Data Layers should have PLSS Data Layer IDs.

                                                                                                 13

Appendix A: References

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/P5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/S4220.pdf

Appendix B: Glossary

See ITA Guideline G105 - (ITA Glossary of Terms) for definitions.

                                                                                          14

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
