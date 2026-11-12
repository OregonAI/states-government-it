---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4246
title: S4246 – Recent and Historical Digital Imagery
doc_type: standard
citation: ITA Standard S4246
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/S4246-ADA.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 1d3aaa55a3ad5b4e1685c339f9f8cba037d4ecbd5b53f6a03ee386557950ad98
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). Pages 14 of the PDF have no text layer (figures, blank pages or scanned forms) and add no
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

# S4246 – Recent and Historical Digital Imagery (ITA Standard S4246)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4246 outlines procedures for managing recent and historical digital imagery to support accurate geographic and infrastructure data." The last page of the PDF (14) is blank (checked by rendering it), so it is listed as no_text_pages.

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category:    S4246 – Recent and Historical Digital Imagery

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
XI. Revision History

I. DEFINITION

   See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

II. RATIONALE

   A statewide comprehensive, recent and historical, digital georeferenced imagery
   layer is a critical source of information for agriculture and precision farming; taxing
   entities; river and stream resource management; wildlife and habitat management;
   land, rangeland, and forest resources management; natural resources conservation;
   infrastructure and construction management; geologic resource assessment and
   hazard mitigation; flood risk management; water supply; scholarly research and
   analysis; homeland security; public safety and disaster response; business,
   community, and economic development needs; wildfire management, planning, and
   response; urban and regional planning, recreation and more. Many private sector
   and local, state, and federal government agencies have business needs for digital
   georeferenced and historical aerial imagery. The University of Idaho Library is

  meeting these needs by providing a comprehensive web service for publicly
  accessible digital georeferenced imagery collections for Idaho.

  The Recent and Historical Digital Imagery Standard is intended to facilitate the
  integration and sharing of recent and historical imagery, as well as to enhance the
  dissemination and use of other Idaho Framework datasets. This standard does not
  instruct how imagery is collected or designed for internal use.

  This standard was developed by the Imagery Technical Working Group (TWG), a
  subgroup of the Idaho Geospatial Council – Executive Committee (IGC-EC). This
  standard will be reviewed on an annual basis and updated as needed.

III. APPROVED STANDARD(S)

  See Attachment

IV. APPROVED PRODUCTS(S)

  Any software capable of ingesting and displaying an Esri Imagery GeoService or
  Open Geospatial Consortium (OGC) standard that is appropriate for displaying
  imagery.

V. JUSTIFICATION

  A statewide comprehensive, recent, and historical, digital georeferenced imagery
  layer is a critical source of information as stated under “II Rationale”. The standard
  supports the use of imagery in a predictable format, improves collaboration, and
  encourages contributions to this layer.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

  Any software capable of ingesting and displaying an Esri Imagery GeoService or
  Open Geospatial Consortium (OGC) standards appropriate for imagery.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

  Data will be shared in accordance with ITA Standard S4250 –Geographic Information
  System (GIS) Data Sharing Standards.

                                                                                           2

VIII. PROCEDURE REFERENCE
    The format, content, and development of this standard adhere to ITA Policy P5030 -
    Framework Standards, ITA Standard S4250 - Data Sharing Standards and ITA
    Standard S4220 - Geospatial Metadata.

IX. REVIEW CYCLE

     Review will occur at least annually.

X.    CONTACT INFORMATION

     For more information, contact the ITA Staff at (208) 605-4064.

XI. REVISION HISTORY

     07/24/2025 - Revised for ADA compliance

     02/15/2023 – Standard made available for public review and comment.

                                                                                    3

                                   STATE OF IDAHO

   Idaho Recent and Historical Digital Data Exchange
                      Standard
                               Part of the Imagery Theme

                                          Version 1
                                 Effective Month Day, 2023

                     Developed by the Imagery Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4064
 contact@its.idaho.gov

                                                                        4

CONTENTS
1. Introduction to the Recent and Historical Imagery Data Exchange Standard.................6
  1.1. Mission and Goals of the Standard ................................................................................6
  1.2. Relationship to Existing Standards ................................................................................6
  1.3. Description of the Standard ............................................................................................7
  1.4. Applicability and Intended Uses.....................................................................................7
  1.5. Standard Development Process ......................................................................................7
  1.6. Maintenance of the Standard .........................................................................................8
2. Body of the Standard .............................................................................................................8
  2.1. Scope and Content ...........................................................................................................8
  2.2. Need ..................................................................................................................................8
  2.3. Participation in the Standard Development ..................................................................8
  2.4. Integration with Other Standards ..................................................................................9
  2.5. Technical and Operation Context ..................................................................................9
     2.5.1. Data Environment ....................................................................................................9
     2.5.2. Reference Systems ....................................................................................................9
     2.5.3. Global Positioning Systems (GPS) ..........................................................................9
     2.5.4. Interdependence of Themes.....................................................................................9
     2.5.5. Encoding..................................................................................................................10
     2.5.6. Resolution................................................................................................................10
     2.5.7. Accuracy..................................................................................................................10
     2.5.8. Edge Matching........................................................................................................10
     2.5.9. Unique Identifier ....................................................................................................10
     2.5.10.  Attributes.............................................................................................................10
     2.5.11.  Stewardship .........................................................................................................11
     2.5.12.  Records Management and Archiving ...............................................................11
     2.5.13.  Metadata..............................................................................................................11
3. Data Characteristics.............................................................................................................11
  3.1. Minimum Graphic Data Elements ...............................................................................11
  3.2. Optional Graphic Data Elements .................................................................................11
  3.3. Standard Attribute Schema ..........................................................................................12
  3.4. Data Quality ...................................................................................................................12
Appendix A: References................................................................................................................13
Appendix B: Glossary ...................................................................................................................13

                                                                                                                                           5

1. Introduction to the Recent and Historical Imagery Data Exchange
  Standard

  A statewide, comprehensive, recent and historical, digital georeferenced imagery layer is a
  critical source of information for agriculture and precision farming; taxing entities; river and
  stream resource management; wildlife and habitat management; land, rangeland, and forest
  resources management; natural resources conservation; infrastructure and construction
  management; geologic resource assessment and hazard mitigation; flood risk management;
  water supply; scholarly research and analysis; homeland security; public safety and disaster
  response; business, community, and economic development needs; wildfire management,
  planning, and response; urban and regional planning; and recreation and more. Many private
  sector and local, state, and federal government agencies have business needs for digital
  georeferenced recent and historical aerial imagery. The University of Idaho Library is
  meeting these needs by providing a comprehensive web service for publicly accessible digital
  georeferenced imagery collections for Idaho.

  The Recent and Historical Imagery Standard is intended to facilitate the integration and
  sharing of current and historical imagery as well as to enhance the dissemination and use of
  other Idaho Framework datasets. This standard does not instruct how imagery is collected or
  designed for internal use.

  This standard was developed by the Imagery Technical Working Group (TWG), a subgroup
  of the Idaho Geospatial Council – Executive Committee (IGC-EC). This standard will be
  reviewed on an annual basis and updated as needed.

  1.1. Mission and Goals of the Standard

  The Recent and Historical Digital Imagery Standard supports a statewide comprehensive,
  recent, and historical, imagery dataset that is consistent with applicable state and national
  standards. It establishes the minimum attributes and geospatial database schema for the
  Imagery Framework. The Standard will communicate with, and may have similar attributes
  to, other Idaho Framework data standards. It encourages all Idaho-based agencies with
  geospatial imagery data to contribute to Recent and Historical Digital Imagery Framework.

  The layer will be appropriately shared and beneficial to all. The attributes will be general
  enough to incorporate basic information without requiring major changes in internal data
  models. This standard allows for expansion to a more complex data structure and schema.

                                                                                                  6

1.2. Relationship to Existing Standards

This Recent and Historical Digital Imagery Standard relates to existing standards as follows:
Idaho Digital Orthoimagery and Data Exchange Standard for the National Agriculture
Imagery Program (NAIP) Layer. The NAIP layer is included in this data set and the
attributes for both layers served by the University of Idaho is identical.

1.3. Description of the Standard

This standard describes the vision and geospatial data structure of a Recent and Historical
Digital Imagery Framework in the State of Idaho. This standard is devised to be:
    • Simple, easy to understand, and logical
    • Uniformly applicable, whenever possible
    • Flexible and capable of accommodating future expansions
    • Dynamic in terms of continuous review

1.4. Applicability and Intended Uses

This standard applies to recent and historical digital imagery of the Imagery theme of The
Idaho Map (TIM). This layer displays the most recent imagery by default. However, the
layer contains numerous imagery collections for any given area. Therefore, users can display
historical images if desired.

When implemented this standard will enable access and exchange of the data. A predictable
standard will support and improve data collaboration, help identify and report errors in
imagery georectification and/or imagery metadata, and allow agencies to incorporate this
data into their own data products.

This standard does not consider data sharing agreements, contracts, transactions, privacy
concerns, or any other issues relating to the acquisition and dissemination of imagery data.

1.5. Standard Development Process

The Imagery Technical Working Group is a voluntary group of private, city, county, tribal,
state, and federal representatives. In 2022 the Imagery Lead began developing the standard.
This standard was then reviewed and edited by the members of the Imagery Technical
Working Group.

                                                                                               7

   After initial development, the draft standard document was shared with the IGC-EC and IGC
   in accordance with the review and approval process described in ITA Policy P5030 -
   Framework Standards Development.

   1.6. Maintenance of the Standard

   This standard will be revised on an annual basis and in accordance with ITA Policy P5030 -
   Framework Standards Development

2. Body of the Standard

   2.1. Scope and Content

   The scope of the Recent and Historical Digital Imagery Standard is to describe a
   comprehensive recent and historical digital georeferenced imagery layer. The overhead,
   vertical images are acquired from an aircraft or other airborne platforms and represent
   surface conditions at the time the image was acquired. The collections in this layer may be
   either orthorectified or georectified.

   Users should be aware that temporal changes may have occurred since the time the data were
   collected and that some parts of these data may no longer represent actual surface conditions.
   Note that the acquisition date is included in the attribute table. Users should not use these
   data for critical applications without a full awareness of the limitations of these data.

   2.2. Need

   A statewide comprehensive, recent and historical, digital georeferenced imagery layer is a
   critical source of information for agriculture and precision farming; taxing entities; river and
   stream resource management; wildlife and habitat management; land, rangeland, and forest
   resources management; natural resources conservation; infrastructure and construction
   management; geologic resource assessment and hazard mitigation; flood risk management;
   water supply; scholarly research and analysis; homeland security; public safety and disaster
   response; business, community, and economic development needs; wildfire management,
   planning, and response; urban and regional planning; and recreation and more. Many private
   sector and local, state, and federal government agencies have business needs for digital
   georeferenced current and historical aerial imagery. The University of Idaho Library is
   meeting these needs by providing a comprehensive web service for publicly accessible digital
   georeferenced imagery collections for Idaho.

                                                                                                 8

2.3. Participation in the Standard Development

The development of the Recent and Historical Digital Imagery Standard adheres to ITA
Policy P5030 - Framework Standards Development. The Imagery Standard Team tasked
with developing this standard invited input and comments from private, county, state, and
federal organizations through participation in Imagery Technical Working Group meetings.
As the standard is reviewed in accordance with ITA Policy P5030 - Framework Standards
Development requirements, there has been opportunity for broad participation and input by
stakeholders in the development of this standard. The process will be equally broad for input
on updates and enhancements to the standard. As with all Idaho Framework standards,
public review and comments on the standard is encouraged.

2.4. Integration with Other Standards

The Recent and Historical Digital Imagery Standard follows the same format as other Idaho
geospatial framework data standards. The standard may contain some of the same attributes
as other framework standards and may adopt the field name, definition, and domain from the
other standards to promote consistency.

2.5. Technical and Operation Context

   2.5.1. Data Environment

   The data environment is a digital raster with a specific, standardized set of attributes.
   Imagery data shared under this standard must be in a format supporting rasters.

   2.5.2. Reference Systems

   The layer is published in the WGS 1984 Web Mercator coordinate system (WKID 3857).
   Data are not required to be submitted in this coordinate system but must have a defined
   coordinate system with Well Known ID (WKID) clearly described in the metadata.

   2.5.3. Global Positioning Systems (GPS)

   Some data provided may contain geometry from GPS methods, and the provided
   metadata should describe this, if applicable.

                                                                                               9

2.5.4. Interdependence of Themes

Attributes found in the layer are identical to attributes found in the “Idaho Digital
Orthoimagery and Data Exchange Standard for the National Agriculture Imagery
Program (NAIP) Layer” published by the University of Idaho.

2.5.5. Encoding

When data are imported into, and exported from, the layer, encoding will take place to
convert data formats and attributes.

2.5.6. Resolution

No specific requirements for resolution are specified in this standard. Resolution will be
documented in the metadata.

2.5.7. Accuracy

The ground sample distance (GSD), horizontal accuracy, and tonal quality varies by
Collection Name in the layer. Consult the metadata for a given collection to determine
the accuracy.

2.5.8. Edge Matching

No edge matching takes place.

2.5.9. Unique Identifier

The DatasetID is the unique identifier for each data collection or data acquisition

2.5.10. Attributes

Attributes are described in Section 3 of this standard.

                                                                                         10

      2.5.11. Stewardship

      Perpetual maintenance and other aspects of lifecycle management are carried out by
      INSIDE Idaho.

      2.5.12. Records Management and Archiving

      Imagery is served as an Esri Imagery GeoService as well as using Open Geospatial
      Consortium (OGC) standards through INSIDE Idaho's Geospatial Data Clearinghouse
      (INSIDE) housed at the University of Idaho. INSIDE provides access and download
      capability. Data are housed on infrastructure managed by Research Computing and Data
      Services (RCDS) at the University of Idaho.

      2.5.13. Metadata

      The metadata describes the methods attributes associated with individual collections in
      the layer. Metadata conforms to the metadata standards as set out in ITA Standard
      S4220 – Geospatial Metadata

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The geometry of the features in the layer is raster.

   3.2. Optional Graphic Data Elements

   Not applicable.

                                                                                                11

  3.3. Standard Attribute Schema

  Field Name          Data Type     Leng              Description                        Examples
                                     th
OBJECTID              ObjectID                Object ID                1
Shape                 Geometry                Shape                    Polygon
Name                  Text          200       File name of source      m_4111101_ne_12_060_20210621
                                              image.
Category              Integer                 Image record category.   1-Primary. See 1) for complete list of coded
                                                                       values
AcqYearFirst          Integer                 Acquisition Year First   2021
AcqYearLast           Integer                 Acquisition Year Last    2021
Resolution            Integer                 Resolution (cm)          100
ProDef                Integer                 Image Type               2-Natural Color. See2) for complete list of
                                                                       coded values
DatasetID             Integer                 Collection Name          Idaho 2004. Complete list expands as
                                                                       collections are added.
Rectification         Integer                 Rectification            1-Orthorectified. See 31) for complete list of
                                                                       coded values
Constraints           Integer                 Constraints              1-Public. See 4) for complete list of coded
                                                                       values
Source                Integer                 Authoritative source     1-USDA-FSA-APFO See 5) for complete list
                                                                       of coded values
AcqDateFirst          Date                    Acquisition Date First   10/12/2021
AcqDateLast           Date                    Acquisition Date Last    10/12/2021
DownloadURL           Text          256       HTTP Download URL        https://www.northwestknowledge.net/data/do
                                                                       wnload.php?uuid=36022c86-8d03-45ec-
                                                                       a430-3bd9dc69d3eb/8cab7323-08f7-4b86-
                                                                       a755-530d9e626e2b

  1
   ) Coded Values: 0-Unknown, 1-Primary, 2-Overview, 3-Unprocessed Overview, 4-Partial Overview, 5-
  Inactive, 253-Uploaded, 254-Incomplete, 255-Custom
  2
      ) Image Type: 0-Unknown, 1-Black & White, 2-Natural Color, 3-Natural Color + Infrared, 4-Color Infrared
  3
      ) Rectification: 0-Unknown, 1-Orthorectified, 2-Georectified
  4
      ) Constraints: 1-Public, 2-Restricted
  5
   ) Source: 0-Unknown, 1-USDA-FSA-APFO, 2-U.S. Geological Survey, 3- Idaho Department of Water
  Resources, 4-Nez Perce County, 5-Idaho EPSCoR Office, 6-Facilities Services U of I, 7-Kimberly Research and
  Extension Center, 8-City of Moscow, 9-Idaho Transportation Department, 10-Library U of I, 11-City of
  McCall, 12-State of Idaho, 13-Teton County

  3.4. Data Quality

  There are no restrictions on rectification, ground sampling distance, horizontal positional
  accuracy, tonal balance, cloud cover or other characteristics of source imagery.

                                                                                                                  12

Appendix A: References

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/p5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/s4220.pdf

Appendix B: Glossary

See ITA Guideline G105 (ITA Glossary of Terms) for definition

                                                                                           13

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). Pages 14 of the PDF have no text layer (figures, blank pages or scanned forms) and add no text here.
