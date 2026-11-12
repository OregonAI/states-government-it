---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4247
title: S4247 – Elevation Data Exchange
doc_type: standard
citation: ITA Standard S4247
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/S4247.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 14fb55a074f324311ab1930b6605cde2fe77656a5fdd956b8bf7dc17e9484f7f
effective_date: '2023-07-20'
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

# S4247 – Elevation Data Exchange (ITA Standard S4247)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4247 establishes protocols for exchanging elevation data, promoting consistency, accuracy, and seamless integration across state agencies."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category:    S4247 – Elevations Layer Data Exchange Standard

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

   A statewide Elevation layer and data standard, which is part of the Elevation data
   theme, is a critical source of information for agriculture and precision farming, natural
   resources conservation, infrastructure and construction management, geologic
   resource assessment as well as hazard mitigation, flood risk management, forest
   resources management, renewable energy resources, river and stream resource
   management, water supply and water quality.

   Standardized elevation data supports those user groups by providing bare-earth
   elevation (point cloud and/or raster) data that has a high spatial resolution and is
   highly precise and accurate. Additionally, derived products such as slope and aspect
   raster datasets are easily generated from the proposed bare-earth elevation dataset.

  Having a unified, single source of such data enables many other types of analysis,
  evaluation, modeling, and planning.

  This data standard supports agencies that collect data and ensures that new
  collections will be compatible with the bare-earth elevation data. Additionally, a
  predictable standard, including a standard schema, will provide the consistency
  needed for use in automated processes, repetitive analyses, and publications.

III. APPROVED STANDARD(S)

  See Attachment

IV. APPROVED PRODUCTS(S)

  Any GIS Software, either desktop or online, capable of ingesting and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

V. JUSTIFICATION

  A statewide Elevation dataset is a critical source of information for a large group of
  users from a variety of industries. A data exchange standard supports the use of
  Elevation in a predictable format, improves collaboration and encourages use of this
  dataset.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

  Any GIS Software, either desktop or online, capable of ingesting and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

  Data will be shared in accordance with Enterprise Standard S4250 – Enterprise
  Geographic Information System (GIS) Data Sharing Standards.

VIII. PROCEDURE REFERENCE

  The format, content, and development of this standard adhere to ITA Policy P5030 -
  Framework Standards, ITA Standard S4250 - Data Sharing Standards and ITA
  Standard S4220 - Geospatial Metadata.

                                                                                       2

IX. REVIEW CYCLE

  Review will occur on an annual basis.

X. CONTACT INFORMATION

  For more information, contact the ITA Staff at (208) 605-4064.

REVISION HISTORY

  07/20/2023 – Standard Presented to the IGC-EC

                                                                   3

                                  STATE OF IDAHO

           Idaho Elevation Data Exchange Standard
                              Part of the Elevation Theme

                                          Version 1
                                   Effective July 20, 2023

                    Developed by the Elevation Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4064
contact@its.idaho.gov

                                                                         4

CONTENTS
1. Introduction to the Elevation Data Exchange Standard ................................................... 6
  1.1. Mission and Goals of the Standard............................................................................... 6
  1.2. Relationship to Existing Standards .............................................................................. 7
  1.3. Description of the Standard .......................................................................................... 7
  1.4. Applicability and Intended Uses ................................................................................... 7
  1.5. Standard Development Process..................................................................................... 7
  1.6. Maintenance of the Standard ........................................................................................ 8
2. Body of the Standard ............................................................................................................ 8
  2.1. Scope and Content .......................................................................................................... 8
  2.2. Need ................................................................................................................................. 8
  2.3. Participation in the Standard Development ................................................................ 8
  2.4. Integration with Other Standards ................................................................................ 9
  2.5. Technical and Operation Context ................................................................................. 9
     2.5.1. Data Environment................................................................................................... 9
     2.5.2. Reference Systems................................................................................................... 9
     2.5.3. Global Positioning Systems (GPS)......................................................................... 9
     2.5.4. Interdependence of Themes ................................................................................. 10
     2.5.5. Encoding ................................................................................................................ 10
     2.5.6. Resolution .............................................................................................................. 10
     2.5.7. Accuracy ................................................................................................................ 10
     2.5.8. Edge Matching ...................................................................................................... 10
     2.5.9. Unique Identifier ................................................................................................... 10
     2.5.10.  Attributes ........................................................................................................... 11
     2.5.11.  Stewardship........................................................................................................ 11
     2.5.12.  Records Management and Archiving .............................................................. 11
     2.5.13.  Metadata ............................................................................................................ 11
3. Data Characteristics ........................................................................................................... 11
  3.1. Minimum Graphic Data Elements.............................................................................. 11
  3.2. Optional Graphic Data Elements................................................................................ 11
  3.3. Standard Attribute Schema..........................................Error! Bookmark not defined.
  3.4. Data Quality .................................................................................................................. 12
Appendix A: References .............................................................................................................. 12
Appendix B: Glossary .................................................................................................................. 12

                                                                                                                                             5

1. Introduction to the Elevation Data Exchange Standard

  A statewide Elevation layer and data standard, which is part of the Elevation data theme, is a
  critical source of information for agriculture and precision farming, natural resources
  conservation, infrastructure and construction management, geologic resource assessment as
  well as hazard mitigation, flood risk management, forest resources management, renewable
  energy resources, river and stream resource management, water supply and water quality.

  Standardized elevation data supports various user groups by providing bare-earth elevation
  (point cloud and/or raster) data that has a high resolution and a high precision. Additionally,
  derived products such as slope and aspect raster datasets are easily generated from the
  proposed bare-earth elevation dataset. Having a unified, single source of such data enables
  many other types of analysis, evaluation, modeling, and planning. This data standard will
  support agencies that collect data, and ensure that new collections will be compatible with
  the bare-earth elevation data. Additionally, a predictable standard, including a standard
  schema, provides the consistency needed for use in automated processes, repetitive analyses,
  and publications.

  The Elevation Standard described in this document is intended to facilitate integration and
  sharing of up-to-date Elevation data and enhance the dissemination and use of Elevation
  information. This standard does not instruct on how Elevation databases are designed for
  internal use or preclude users from using other sources of elevation data.

  This standard was developed by the Elevation Technical Working Group, a subgroup of the
  Idaho Geospatial Council – Executive Committee (IGC-EC). This standard will be reviewed
  on an annual basis and updated as needed.

  1.1. Mission and Goals of the Standard

  The Elevation Standard supports a statewide dataset that is consistent with applicable state
  and national standards. It establishes the minimum attributes and geospatial database schema
  for the Elevation Framework. The Standard will communicate with, and may have similar
  attributes to, other Idaho Framework data standards. It encourages agencies with geospatial
  LiDAR derived elevation data to contribute to the Elevation Framework.

  The Elevation Framework will be appropriately shared and benefit all. The fields in the
  Elevation Data Exchange Standard will be general enough to incorporate basic information
  without requiring major changes in internal data models. This standard allows for expansion
  to a more complex data structure and schema.

                                                                                                6

1.2. Relationship to Existing Standards

This Elevation Exchange Standard is related to the Idaho Statewide LiDAR Plan Version 1.1
and will be related to the LiDAR Raw Point Cloud Data Standard, once this standard has
been developed.

1.3. Description of the Standard

This standard describes the vision and geospatial data structure of an Elevation Framework in
the state of Idaho. This standard is devised to be:

    •   Simple, easy to understand, and logical.
    •   Uniformly applicable, whenever possible
    •   Flexible and capable of accommodating future expansions
    •   Dynamic in terms of continuous review

1.4. Applicability and Intended Uses

This standard applies to the Elevation element of the Elevation theme of The Idaho Map
(TIM).

When implemented, this elevation data standard will enable access to and exchange of these
data. A predictable standard will support and improve data collaboration, enable greater
coordination in collecting updated or missing data, and help identify and report errors. As
well as allow agencies to incorporate these data into their own data products knowing that the
data standard and schema will be consistent over time.

This standard does not consider data sharing agreements, contracts, transactions, privacy
concerns, or any other issues relating to the acquisition and dissemination of Elevation data.

1.5. Standard Development Process

The Elevation Technical Working Group is a voluntary group of private, city, county, tribal,
state, and federal representatives. In 2022, the Elevation Technical Working Group Chair
began developing the standard for the Elevation Framework using the standard development
automation tools developed by the IGC-EC to generate the first draft of the Standard. This
standard was then reviewed and edited by the members of the Elevation Technical Working
Group.
                                                                                                 7

   After initial development the draft standard document was shared with the Idaho Geospatial
   Council Executive Committee (IGC-EC) and the Idaho Geospatial Council (IGC) in
   accordance with the review and approval process described in ITA Policy P5030 Framework
   Standards Development.

   1.6. Maintenance of the Standard

   This standard will be revised on an annual basis and in accordance with ITA Policy P5030 -
   Framework Standards Development.

2. Body of the Standard

   2.1. Scope and Content

   The scope of the Elevation Data Exchange Standard is to describe the format and schema of a
   statewide layer displaying elevations in Idaho, along with its relationship to other existing
   standards and plans.

   2.2. Need

   Elevation data is needed because location based elevation is crucial for agriculture and
   precision farming, natural resources conservation, infrastructure and construction
   management, geologic resource assessment and hazard mitigation, flood risk management,
   forest resources management, renewable energy resources, river and stream resource
   management, water supply and water quality. Additionally, it is needed as a precursor or
   input to other studies and planning activities. These include emergency management,
   transportation infrastructure, natural resources, education, environmental health, and many
   others.

   It is important that these data follow a standard to ensure quality and an understanding of the
   dataset. Additionally, a predictable data format as described in this standard will enable other
   data providers to contribute to this dataset, as well as allow agencies to use this data in
   automated process and models.

   2.3. Participation in the Standard Development

   The development of the Elevation Data Exchange Standard adheres to the the ITA Policy
   P5030 - Framework Standards Development. The Elevation Standard Team tasked with

                                                                                                  8

development, invite input and comments from private, county, state, and federal
organizations. As the standard is reviewed in accordance with Policy P5030 requirements,
there will be opportunity for broad participation and input by stakeholders. The process will
be equally broad for input on updates and enhancements to the standard. As with all Idaho
Framework standards, public review and comment on the Elevation Data Exchange Standard
is encouraged.

2.4. Integration with Other Standards

The Elevation Data Exchange Standard follows the same format as other Idaho geospatial
framework data standards. The Elevation standard may contain some of the same attributes
as other framework standards and may adopt the field name, definition, and domain from the
other standards to promote consistency.

2.5. Technical and Operation Context

   2.5.1. Data Environment

   The data environment is a digital Other with a specific, standardized set of attributes
   pertinent to the Elevation Framework. Elevation data shared under this standard must be
   in a format supporting Others.

   2.5.2. Reference Systems

   The Elevation dataset will be published in the Idaho Transverse Mercator NAD83 spatial
   reference system (EPSG 8826), which is the State of Idaho’s single-zone, statewide
   system. Data is not required to be submitted in the IDTM NAD83 (IDTM83) coordinate
   system but must have a correctly defined spatial reference system clearly described in the
   metadata.

   2.5.3. Global Positioning Systems (GPS)

   Some data provided might contain geometry from GPS methods, and the provided
   metadata should describe this, if applicable. Various, and depends on the collection
   quality, date, and for what agency or standard. Typically, a high-grade onboard INS,
   combined with RTK-GPS ground validation locations in various ecological conditions
   (e.g. vegetated and non-vegetated).
                                                                                             9

2.5.4. Interdependence of Themes

These Elevation data have a geometry that is coincident with other framework data, such
as ridge lines and cliffs. Other datasets should be coincident with some components of
this dataset, such as break lines when the elevation data is of sufficient quality and is
delivered with lidar-derived break lines or similar data source.

2.5.5. Encoding

When data is imported into and exported from the Elevation Framework, encoding will
take place to convert data formats and attributes.

2.5.6. Resolution

Until statewide coverage of same-quality data is achieved, no specific requirements for
resolution are specified in this standard. Resolution will be documented in the metadata.

2.5.7. Accuracy

Until statewide coverage of same-quality data is achieved, no specific requirements for
accuracy are specified in this standard. Accuracy will be documented in the metadata.

2.5.8. Edge Matching

No edge matching is required between jurisdictions, or between this and other framework
layers.

2.5.9. Unique Identifier

A Globally Unique ID (GUID) exists for this dataset. Each unique value identifies a
specific lidar project area of interest (collection area) and is maintained as the dataset is
updated.

                                                                                                10

      2.5.10. Attributes

      Attributes for public and intergovernmental distribution are described in Section 3 of this
      standard.

      2.5.11. Stewardship

      Perpetual maintenance and other aspects of lifecycle management are essential to
      Elevation Framework. Details of stewards, their roles and responsibilities, and processes
      are set forth, or are being planned to set forth in an Elevation Framework Stewardship
      Plan and related documents.

      2.5.12. Records Management and Archiving

      Records are managed and archived at ISU's GIS TReC, as well as partially redundantly at
      Boise State's BCAL group. Originating or funding agencies will maintain internal records
      according to their own protocols.

      2.5.13. Metadata

      The Elevation Framework metadata will describe the methods used to update and
      aggregate the individual Elevation data contributions, processes or crosswalks performed,
      definition of attributes, and other required information. This metadata will conform to the
      metadata standards as set out in ITA Standard S4220 Geospatial Metadata.

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The geometry of the features in Elevation Framework is a raster.

   3.2. Optional Graphic Data Elements

   Not applicable.

   3.3. Standard Attribute Schema
                                                                                               11

     Field Name           Data Type       Length           Description            Examples
                                                         GUID for the data
                                                           collection (i.e.
        GUID                GUID                              "Project")       Adams County 2019
                                                         Elevation for pixel
                             32-bit                      in meters accurate
         Value           floating point     n/a             to 0.05 meter           1065.35

   3.4. Data Quality

   Data quality considerations for elevations include:
       a) All Data Collection efforts or Projects have a unique GUID stored within the dataset.
       b) VRMSE is +/- 0.05 meters

Appendix A: References

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/p5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/s4220.pdf

Elevation Technical Working Group and Idaho Lidar Consortium. 2018. Idaho Statewide Lidar
Plan Version 1.1 Idaho_Statewide_Lidar_Plan_Final_2018.pdf

Appendix B: Glossary

See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

                                                                                                   12

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
