---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4261
title: S4261 – Landslide Inventory Data Exchange
doc_type: standard
citation: ITA Standard S4261
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/S4261.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 046ef9ca8ff4e4db0a8cacc5992c7479b170147bd344084e9d16987690ab7a5f
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

# S4261 – Landslide Inventory Data Exchange (ITA Standard S4261)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4261 sets procedures for exchanging landslide inventory data, enhancing risk assessment, hazard mapping, and geospatial planning statewide."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category:    S4261 – Landslide Inventory

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

   A statewide landslide inventory layer and data standard, which is part of the Hazards
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

   A statewide landslide inventory dataset is a critical source of information, as stated
   under ‘II. Rationale’ in this standard. A data exchange standard supports the use of
   the landslide inventory dataset to facilitate a predictable format, improve
   collaboration, and encourage the use of this dataset.

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

XI. REVISION HISTORY

   07/20/2023 – Standard Presented to the IGC-EC

Landslide Inventory Standard                                                                2

                                  STATE OF IDAHO

  Idaho Landslide Inventory Data Exchange Standard
                               Part of the Hazards Theme

                                         Version 1
                                  Effective July 20, 2023
                    Developed by the Hazards Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4064
contact@its.idaho.gov

Landslide Inventory Standard                                           3

CONTENTS
1. Introduction to the Landslide Inventory Data Standard .................................................. 6
     1.1.   Mission and Goals of the Standard............................................................................... 6
     1.2.   Relationship to Existing Standards .............................................................................. 6
     1.3.   Description of the Standard .......................................................................................... 7
     1.4.   Applicability and Intended Uses ................................................................................... 7
     1.5.   Standard Development Process..................................................................................... 7
     1.6.   Maintenance of the Standard ........................................................................................ 8
2.     Body of the Standard ............................................................................................................ 8
     2.1.   Scope and Content .......................................................................................................... 8
     2.2.   Need ................................................................................................................................. 8
     2.3.   Participation in the Standard Development ................................................................ 8
     2.4.   Integration with Other Standards ................................................................................ 8
     2.5.   Technical and Operation Context ................................................................................. 9
       2.5.1.      Data Environment................................................................................................... 9
       2.5.2.      Reference Systems................................................................................................... 9
       2.5.3.      Global Positioning Systems (GPS)......................................................................... 9
       2.5.4.      Interdependence of Themes ................................................................................... 9
       2.5.5.      Encoding .................................................................................................................. 9
       2.5.6.      Resolution ................................................................................................................ 9
       2.5.7.      Accuracy ................................................................................................................ 10
       2.5.8.      Edge Matching ...................................................................................................... 11
       2.5.9.      Unique Identifier ................................................................................................... 11
       2.5.10.        Attributes ........................................................................................................... 11
       2.5.11.        Stewardship........................................................................................................ 11
       2.5.12.        Records Management and Archiving .............................................................. 11
       2.5.13.        Metadata ............................................................................................................ 11
3.     Data Characteristics ........................................................................................................... 12
     3.1.   Minimum Graphic Data Elements.............................................................................. 12
     3.2.   Optional Graphic Data Elements................................................................................ 12
     3.3.   Standard Attribute Schema......................................................................................... 12
  3.4. Data Quality .................................................................................................................. 14
Landslide Inventory Standard                                                                                                            4

Appendix A: References .............................................................................................................. 15
Appendix B: Glossary .................................................................................................................. 15

Landslide Inventory Standard                                                                                                            5

1. Introduction to the Landslide Inventory Data Standard

   A statewide landslide inventory is a critical source of information for land managers,
   emergency managers, transportation engineers, developers, and researchers. Those groups
   will benefit from this data because this standard is an authoritative, centralized, statewide
   landslide inventory. Many private sector and local, state, and federal government agencies
   have business needs for landslide inventory data.

   The Landslide Inventory Standard is intended to facilitate the integration and sharing of up-
   to-date landslide data and enhance the dissemination and use of landslide information. This
   standard does not instruct on how the landslide inventory is designed for internal use.

   This standard was developed by the Hazards Technical Working Group, a subgroup of the
   Idaho Geospatial Council – Executive Committee (IGC-EC). This standard will be reviewed
   at least annually and updated as needed.

   1.1. Mission and Goals of the Standard

   The Landslide Inventory Standard supports a statewide dataset that is consistent with
   applicable state and national standards. It establishes the minimum attributes and geospatial
   database schema for the Landslide Inventory Framework. The standard will communicate
   with, and may have similar attributes to, other Idaho Framework data standards. It
   encourages all Idaho-based agencies with geospatial landslide inventory data to contribute to
   the Landslide Inventory Framework.

   The Landslide Inventory Framework will be appropriately shared and beneficial to all. The
   fields in the Landslide Inventory Standard will be general enough to incorporate basic
   information without requiring major changes in internal data models. This standard allows
   for expansion to a more complex data structure and schema.

   1.2. Relationship to Existing Standards

   This Landslide Inventory Standard relates to existing standards as follows:

       •   No other standards apply.

Landslide Inventory Standard                                                                       6

   1.3. Description of the Standard

   This standard describes the vision and geospatial data structure of a Landslide Inventory
   Framework in the state of Idaho. This standard is devised to be:

       •   Simple, easy to understand, and logical
       •   Uniformly applicable, whenever possible
       •   Flexible and capable of accommodating future expansions
       •   Dynamic in terms of continuous review

   1.4. Applicability and Intended Uses

   This standard applies to the landslide inventory element of the Hazards theme of The Idaho
   Map (TIM).

   When implemented, this standard will enable access to and exchange of Idaho’s landslide
   data. A predictable standard will support data collaboration, improve data collaboration, help
   identify and report errors, and allow agencies to incorporate this data into their own data
   products.

   This standard does not consider data sharing agreements, contracts, transactions, privacy
   concerns, or any other issues relating to the acquisition and dissemination of landslide
   inventory data.

   1.5. Standard Development Process

   The Hazards Technical Working Group is a voluntary group of private, city, county, tribal,
   state, and federal representatives. In 2022 the Landslide Inventory Lead began developing the
   standard for the Landslide Inventory Framework using the standard development automation
   tools developed by the IGC-EC to generate the first draft of the standard. This standard was
   then reviewed and edited by the members of the Hazards Technical Working Group.
   After initial development the draft standard document was shared with the Idaho Geospatial
   Council Executive Committee (IGC-EC) and the Idaho Geospatial Council (IGC) in
   accordance with the review and approval process described in ITA Policy P5030 Framework
   Standards Development.

Landslide Inventory Standard                                                                    7

   1.6. Maintenance of the Standard

   This standard will be revised on an annual basis and in accordance with ITA Policy P5030 -
   Framework Standards Development.

2. Body of the Standard

   2.1. Scope and Content

   The scope of the Landslide Inventory Standard is to describe a statewide layer which
   identifies the physical locations and attributes of mapped landslides in Idaho.

   2.2. Need

   Landslide inventory maps are a key dataset needed for land managers, emergency managers,
   transportation engineers, developers, and researchers. This standard provides the foundation
   to aggregate landslide data for centralized access and stewardship information.

   Landslide inventory data is needed because it is intended to be a comprehensive inventory of
   mapped landslides in Idaho. This standard will allow the dataset to be hosted by the multi-
   disciplinary hazards portal hosted by the state.

   2.3. Participation in the Standard Development

   The development of the Landslide Inventory Standard adheres to the ITA Policy P5030 -
   Framework Standards Development. The Hazards Standard Team tasked with development,
   invite input and comments from private, county, state, and federal organizations. As the
   standard is reviewed in accordance with Policy P5030 requirements, there will be
   opportunity for broad participation and input by stakeholders. The process will be equally
   broad for input on updates and enhancements to the standard. As with all Idaho Framework
   standards, public review and comment on the Landslide Inventory Standard is encouraged.

   2.4. Integration with Other Standards

   The Landslide Inventory Standard follows the same format as other Idaho geospatial
   framework data standards. The Landslide Inventory Standard may contain some of the same
   attributes as other framework standards and may adopt the field name, definition, and domain
   from the other standards to promote consistency.

Landslide Inventory Standard                                                                    8

   2.5. Technical and Operation Context

       2.5.1. Data Environment

       The data environment is a digital geodatabase with a specific, standardized set of
       attributes pertinent to the Landslide Inventory Framework. The landslide inventory data
       shared under this standard must be in a format supporting geodatabases.

       2.5.2. Reference Systems

       The Landslide Inventory Framework will be published in the Idaho Transverse Mercator
       NAD83 (IDTM83) coordinate system, which is the State of Idaho’s single-zone
       coordinate system. Data is not required to be submitted in the IDTM83 coordinate system
       but must have a defined coordinate system clearly described in the metadata.

       2.5.3. Global Positioning Systems (GPS)

       Some data provided might contain geometry from GPS methods, and the provided
       metadata should describe this, if applicable.

       2.5.4. Interdependence of Themes

       The Landslide Inventory geometry data is not dependent on other framework data.

       2.5.5. Encoding

       When data is imported into and exported from the Landslide Inventory Framework,
       encoding will take place to convert data formats and attributes.

       2.5.6. Resolution

       No specific requirements for resolution are specified in this standard. Resolution will be
       documented in the metadata.

Landslide Inventory Standard                                                                        9

       2.5.7. Accuracy

       The Landslide Inventory database was compiled from many sources (Lifton et al., 2021).
       The Idaho Geological Survey (IGS) performed an accuracy assessment of the historical
       landslide point data that were incorporated into the database. Each source of landslide
       data used different techniques, scales, and basemaps; an accuracy assessment is needed to
       determine the quality of the data. The assessment involved two parts. First, the maximum
       location uncertainty was calculated for points that were converted from their original
       PLSS locations. Second, 100 random landslide point records were randomly chosen from
       the inventory database to compare to modern satellite imagery to determine the accuracy
       of the original mapping. Each point was reviewed by a geologist to determine if the point
       was located within a real landslide as interpreted from the satellite imagery. Where
       original landslide mapping did not already include a measure of spatial accuracy, IGS
       assigned a qualitative value of “good”, “fair”, or “poor”.

       The original PLSS locations from the previously published landslide inventory define a
       rectangular area within which the landslide is located. When the PLSS locations were
       converted to a modern digital GIS format, each landslide was assigned a latitude and
       longitude coordinate at the centroid of the PLSS township and range in which it was
       originally located. The maximum uncertainty within a full section (1 mile x 1 mile
       square) is 1,138.5 meters. The maximum uncertainty within a quarter-quarter section (¼
       mile x ¼ mile square) is 285 meters (Figure 1).

         Figure 1. Schematic Diagram of Maximum Uncertainty from Center of PLSS Section and ¼-¼ Section.

Landslide Inventory Standard                                                                               10

       2.5.8. Edge Matching

       No edge matching is required between jurisdictions or between this and other framework
       layers

       2.5.9. Unique Identifier

       The unique identifier is IGS_ID, which is a unique reference ID assigned by the Idaho
       Geological Survey for this database.

       2.5.10. Attributes

       Attributes for public and intergovernmental distribution are described in Section 3 of this
       standard.

       2.5.11. Stewardship

       Perpetual maintenance and other aspects of lifecycle management are essential to the
       Landslide Inventory Framework. Details of stewards, their roles and responsibilities, and
       processes are set forth, or will be set forth in a Landslide Inventory Framework
       Stewardship Plan and related documents.

       2.5.12. Records Management and Archiving

       Data are managed by the Idaho Geological Survey and hosted on ArcGIS Online.

       2.5.13. Metadata

       The Landslide Inventory Framework metadata will describe the methods used to update
       and aggregate the individual landslide inventory data contributions, processes or
       crosswalks performed, definition of attributes, and other required information. This
       metadata will conform to the metadata standards as set out in ITA Standard S4220
       Geospatial Metadata.

Landslide Inventory Standard                                                                    11

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The geometry of the features in Landslide Inventory Framework are points and polygons.

   3.2. Optional Graphic Data Elements

   Not applicable.

   3.3. Standard Attribute Schema

   Both the point and polygon representations that make up the landslide inventory have the
   same standard attribute schema.

                      Data
   Field Name                  Length               Description                         Examples
                      Type
                                        Unique reference ID assigned by
 IGS_ID              Text       255                                               LSPY_0001
                                        IGS for this database
 ACT_INACT           Text        20     Active/Inactive landslide                 active/inactive
                                        Latitude of point or centroid of
 LATITUDE            Double      -                                                43.000000
                                        polygon
                                        Longitude of point or centroid of
 LONGITUDE           Double      -                                                -115.000000
                                        polygon
                                        Elevation, in meters, of landslide
 ELEVATION           Long        -      centroid above mean sea level,            750
                                        mapped point or polygon centroid.
                                        Date of last slope failure or
 LS_DATE             Date        -                                                mm/dd/yyyy
                                        movement, if known
                                        County in which landslide occurred.
                                        If landslide overlaps more than one
 COUNTY              Text       255     county, choose the county in which        Ada
                                        the greatest proportion of landslide
                                        occurs
                                        Average slope inclination (measured
                                        in degrees at point or polygon
 SLOPE               Long        -                                                12
                                        centroid) of the slope on which
                                        failure occurred
                                        Azimuth (0-360 degrees) of average
 ASPECT              Long        -      slope direction at point or centroid of   221
                                        polygon
                                        U.S. Climate Divisions extracted
 CLIMATE             Text       255                                               Eastern Highlands
                                        from NOAA
                                        Geologic unit extracted from IGS
 GEOL_UNIT           Text       255                                               QTpms
                                        Geologic Map of Idaho

Landslide Inventory Standard                                                                          12

                   Data
   Field Name                  Length               Description                          Examples
                   Type
                                        Type of material involved in
                                        landslide (e.g., bedrock, debris, talus,   Weak or sensitive
 MATERIAL         Text          255
                                        etc.). Can also be a description of        materials
                                        bedrock lithology, if appropriate
                                        Soil or regolith cover, based on field
 COVER            Text          255     observations or NRCS Soil Survey           2023918
                                        maps (MUKEY)
                                        Type of landslide, as defined by
                                        Varnes (1978) and Cruden and
                                        Varnes (1996). Classification is
 LS_TYPE          Text          255     based on material type (rock, debris,      Earth Slide
                                        or earth) and movement type (fall,
                                        topple, rotational sliding,
                                        translational sliding, and flow).
                                        Maximum downslope length of
 LNGTH            Long           -                                                 1235
                                        landslide, from toe to crown
                                        Maximum width of displaced mass
 WDTH             Long           -                                                 350
                                        perpendicular to length
 AREA_1           Double         -      Area of landslide polygon                  8540.85909026929
 DEEP_SHALL       Text          255     Estimated thickness of landslide           Unknown
                                        Estimate of landslide volume if
 VOL              Long           -      length, width, and thickness are           6524
                                        known
 ACTIVITY         Text          255     Level of activity of slope failure         Ancient
                                        Estimated rate of movement. May
 MOVE_RATE        Text          255     not be possible to determine but note      Seasonal
                                        if known.
                                        Description of how landslide was
                                        located, e.g., aerial stereo               Idaho Geological
 LOC_META         Text          255     photographs, lidar, satellite photos,      Survey mapping
                                        field mapping, etc. If possible, note      methods
                                        the scale of imagery used.
                                        Name of 1:100:000 scale quadrangle
 QUAD_100K        Text          255                                                Sandpoint
                                        map in which landslide is located
                                        Name of 1:24,000 scale (7.5')
 QUAD_24K         Text          255     quadrangle map in which landslide is       Laclede
                                        located
                                        Original source of mapped landslide.
                                                                                   Idaho
                                        If from a published source, cite as
 SOURCE           Text          255                                                Transportation
                                        Breckenridge et al., 2014, for
                                                                                   Department
                                        example.
                                        Unique ID assigned by original
 SOURCE_ID        Text          255                                                39
                                        source
                                        Code for reference to original source
 SOURCE_REF       Text          255     for Adams and Breckenridge (1991)          S29
                                        database
                                        Estimated level of confidence in the
 SPATIAL_ACC      Text          255                                                good
                                        location of landslide
Landslide Inventory Standard                                                                           13

                     Data
   Field Name                  Length              Description                       Examples
                     Type
                                                                               Colluvium with
                                        Additional comments regarding the      subrounded rock
                                        landslide. Can include notes on any    fragments. Appears
                                        additional contributing factors that   to have very recent
 COMMENTS          Text         255
                                        may have influenced slope stability,   shallow slump cut
                                        such as precipitation events or        slope failures that
                                        human slope modification.              could partially fill
                                                                               the ditch.
                                        ITD district in which landslide is
 DISTRICT          Text         255                                            District 6
                                        located
                                        ITD route. For example, “US-95” or
 ROUTE             Text         255                                            US-26
                                        “SH-55”.
                                        Latitude of the start of affected
 START_LAT         Double        -                                             43.237693
                                        roadway
                                        Longitude of the start of affected
 START_LON         Double        -                                             -115.434987
                                        roadway
                                        Latitude of the end of affected
 END_LAT           Double        -                                             43.345728
                                        roadway
                                        Longitude of the end of affected
 END_LON           Double        -                                             -115.425678
                                        roadway
                                        Milepost of the start of affected
 START_MP          Double        -                                             374.1
                                        roadway
                                        Milepost of the end of affected
 END_MP            Double        -                                             374.2
                                        roadway
                                        The side of the roadway affected, as
 AFFECT_SIDE       Text         255                                            Right
                                        measured when looking upstation.
 ROAD_WIDTH        Double        -      Road width                             32
 PSL               Long          -      Posted speed limit                     55
 ADT               Long          -      Average daily traffic                  1900
 PMF               Text         255     Potential for major failures           <Null>
                                        Distance from road to landslide
 DIST_2_SCARP      Long          -                                             127
                                        headscarp
                                        ZIP code provided for interaction
 ZIP               Text          15                                            83554
                                        with TIGER data

   3.4. Data Quality

   Data quality considerations for Landslide Inventory include:
       a) All Landslide Inventory data should have landslide inventory IDs which is shown as
          ‘IGS_ID’ in the attribute schema.

Landslide Inventory Standard                                                                      14

Appendix A: References

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/p5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/s4220.pdf

Lifton, Z.M., Ducar, S.D., and Tate, C.A., 2021, Landslide Inventory Database for Idaho: Idaho
Geological Survey Digital Database 10, https://idahogeology.org/product/DD-10.

Appendix B: Glossary

See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

Landslide Inventory Standard                                                                15

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
