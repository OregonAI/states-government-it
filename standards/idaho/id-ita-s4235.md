---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4235
title: S4235 – Idaho Legislative and Congressional Districts
doc_type: standard
citation: ITA Standard S4235
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/S4235-ADA.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 549ea33288a974326d5795e633e970aa28c937a9b703d28191ea3cda10f97659
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

# S4235 – Idaho Legislative and Congressional Districts (ITA Standard S4235)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4235 delineates the boundaries for Idaho’s legislative and congressional districts, ensuring accurate representation and governance."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 – INFORMATION AND DATA

Category:    S4235 Idaho Legislative and Congressional Districts Standard

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

   Statewide Idaho Legislative and Congressional District layers are a critical source of
   information for State and Local Government as well as Citizens for determining their
   representative. Many private sector and local, state, and federal government
   agencies have business needs for Idaho Congressional and Legislative District
   Framework layers.

III. APPROVED STANDARD(S)

   See Attachment

IV. APPROVED PRODUCT(S)

   Any GIS Software, either desktop or online, capable of ingesting and displaying
   Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

V. JUSTIFICATION

  A statewide Idaho Congressional and Legislative Districts Framework is a critical
  source of information for many private and public sector entities.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

  Any GIS Software, either desktop or online, capable of ingesting and displaying
  Open Geospatial Consortium (OGC) Web Map Standard (WMS) services.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

  Data will be shared in accordance with ITA Standard 4250 – Enterprise
  Geographic Information System (GIS) Data Sharing Standards.

VIII. PROCEDURE REFERENCE

  The format, content and development of this standard adheres to ITA Policy P5030
  for Framework Standards Development, ITA Standard S4250 Data Sharing
  Standards and ITA Standard S4220 Geospatial Metadata.

IX. REVIEW CYCLE

  Review will occur at least annually.

X. CONTACT INFORMATION

  For more information, contact the ITA Staff at (208) 605-4064.

REVISION HISTORY

  07/24/2025 - Revised for ADA compliance

  02/15/2023 – Standard made available for public review and comment.

                                                                                      2

                                  STATE OF IDAHO

   Idaho Congressional and Legislative Districts Data
                      Standard
                              Part of the Boundary Theme

                                         Version 1
                                       Effective 2023

                    Developed by the Boundary Technical Working Group

Contact
ITA Staff
Office of Information Technology Services
(208) 605-4064
contact@its.idaho.gov

                                                                        3

CONTENTS
1. Introduction to the Idaho Congressional and Legislative Districts Data Standard ....... 5
  1.1. Mission and Goals of the Standard ............................................................................... 5
  1.2. Relationship to Existing Standards .............................................................................. 5
  1.3. Description of the Standard .......................................................................................... 5
  1.4. Applicability and Intended Uses ................................................................................... 6
  1.5. Standard Development Process..................................................................................... 6
  1.6. Maintenance of the Standard ........................................................................................ 7
2. Body of the Standard ............................................................................................................ 7
  2.1. Scope and Content .......................................................................................................... 7
  2.2. Need ................................................................................................................................. 7
  2.3. Participation in the Standard Development ................................................................ 7
  2.4. Integration with Other Standards ................................................................................ 8
  2.5. Technical and Operation Context ................................................................................. 8
     2.5.1. Data Environment................................................................................................... 8
     2.5.2. Reference Systems................................................................................................... 8
     2.5.3. Global Positioning Systems (GPS)......................................................................... 8
     2.5.4. Interdependence of Themes ................................................................................... 8
     2.5.5. Encoding .................................................................................................................. 9
     2.5.6. Resolution ................................................................................................................ 9
     2.5.7. Accuracy .................................................................................................................. 9
     2.5.8. Edge Matching ........................................................................................................ 9
     2.5.9. Unique Identifier ..................................................................................................... 9
     2.5.10.  Attributes ............................................................................................................. 9
     2.5.11.  Stewardship.......................................................................................................... 9
     2.5.12.  Records Management and Archiving .............................................................. 10
     2.5.13.  Metadata ............................................................................................................ 10
3. Data Characteristics ........................................................................................................... 10
  3.1. Minimum Graphic Data Elements.............................................................................. 10
  3.2. Optional Graphic Data Elements................................................................................ 10
  3.3. Standard Attribute Schema......................................................................................... 10
  3.4. Data Quality .................................................................................................................. 11
Appendix A: References .............................................................................................................. 13
Appendix B: Glossary .................................................................................................................. 13

                                                                                                                                             4

1. Introduction to the Idaho Congressional and Legislative Districts Data
  Standard

  Statewide Idaho Legislative and Congressional District layers are a critical source of
  information for State and Local Government as well as Citizens for determining their
  representative. Many private sector and local, state, and federal government agencies have
  business needs for Idaho Congressional and Legislative District Framework layers.

  The Idaho Congressional and Legislative Districts Standard is intended to facilitate
  integration and sharing of up-to-date Idaho Congressional and Legislative District data and
  enhance the dissemination of this information. This standard does not instruct on how Idaho
  Congressional or Legislative District databases are designed for internal use.

  Congressional and Legislative boundary data is developed by the Idaho Legislative Office
  and a Contactor from RDI based on the decennial census conducted by the U.S. Census
  Bureau. The standard was further developed in coordination with the Boundary Technical
  Working Group, a subgroup of the Idaho Geospatial Council – Executive Committee (IGC-
  EC). This standard will be reviewed on an annual basis and updated as needed.

  1.1. Mission and Goals of the Standard

  The Idaho Congressional and Legislative Districts Standard supports a statewide dataset that
  is consistent with applicable state and national standards. It establishes the minimum
  attributes and geospatial database schema for the Idaho Congressional and Legislative
  Districts Framework.

  The Idaho Congressional and Legislative Districts Framework will be appropriately shared
  for the benefit of all. The fields in the Idaho Congressional and Legislative Districts Data
  Standard will be general enough to incorporate basic information without requiring major
  changes the internal data models. This standard allows for expansion to a more complex data
  structure and schema.

  The goal of the standard is to encourage the use of the authoritative dataset created by the
  Idaho Legislative Office and to promote the delivery of this data in a consistent, predictable,
  and standardized format.

  1.2. Relationship to Existing Standards

  This Idaho Congressional and Legislative Districts Standard relates to existing standards as
  follows: Metadata is provided in accordance with ITA Standard S4220 Geospatial

                                                                                                    5

Metadata. Census tracts, block groups and blocks along with 2020 Census population
numbers underlying the Idaho Congressional and Legislative Districts have been collected
using standards established by the U.S. Census Bureau.

1.3. Description of the Standard

This standard describes the spatial and tabular data structure of the two datasets describing
Idaho Congressional and Legislative Districts respectively.

This standard is devised to be:
    • Simple, easy to understand, and logical.
    • Uniformly applicable, whenever possible.
    • Flexible and capable of accommodating future expansions.
    • Dynamic in terms of continuous review.

1.4. Applicability and Intended Uses

This standard applies to the Idaho Congressional and Legislative Districts element of the
Boundary theme of The Idaho Map (TIM).

When implemented, it will enable access to geometry and attribute information about Idaho
Congressional and Legislative Districts. It will increase interoperability between automated
geographic information systems and enable sharing and efficient transfer of information for
aggregation. Further, it will encourage partnerships between government, the private sector,
and the public in order to avoid duplication of effort and ensure effective management of
information resources. It will help improve Idaho Congressional and Legislative Districts
Data quality as errors are identified and resolved.

This standard does not consider data sharing agreements, contracts, transactions, privacy
concerns, or any other issues relating to the acquisition and dissemination of Idaho
Congressional and Legislative Districts Data.

1.5. Standard Development Process

Both the Congressional and Legislative District layers were developed by the Idaho
Commission for Reapportionment using the process described in their Final Report dated
November 10, 2021.
Once the data and report were completed, the Data Standard Creation tool was used to
generate a first draft of the standard. This draft was then further edited by the contractor
supporting redistricting mapping for the Idaho Legislative Office and the Boundary
Technical Working Group.
                                                                                                6

   After initial development the draft standard document was shared with the Idaho Geospatial
   Council Executive Committee (IGC-EC) and the Idaho Geospatial Council (IGC) in
   accordance with the review and approval process described in ITA Policy P5030 Framework
   Standards Development.

   1.6. Maintenance of the Standard

   This standard will be revised on an annual basis and in accordance with the ITA Policy
   P5030 Framework Standards Development.

2. Body of the Standard

   2.1. Scope and Content

   The scope of the Idaho Congressional and Legislative Districts Data Standard is to describe
   two statewide layers which identifies the physical locations and attributes of Idaho
   Congressional and Legislative Districts in Idaho respectively.

   2.2. Need

   Statewide Idaho Legislative and Congressional District layers are a critical source of
   information for State and Local Government as well as Citizens for determining their
   representative. Many private sector and local, state, and federal government agencies have
   business needs for Idaho Congressional and Legislative District Framework layers.

   This standard provides the foundation to aggregate Idaho Congressional and Legislative
   Districts Data for centralized access and stewardship information.

   2.3. Participation in the Standard Development

   The development of the Idaho Congressional and Legislative Districts Data Standard adheres
   to the ITA Policy P5030 Framework Standards Development. The standard is reviewed in
   accordance with ITA Policy P5030 requirements, there was opportunity for broad
   participation and input by stakeholders in the development of this standard. The process will
   be equally broad for input on updates and enhancements to the standard. As with all Idaho
   Framework standards, public review, and comments on the Idaho Congressional and
   Legislative Districts Data Standard is encouraged.

                                                                                                 7

2.4. Integration with Other Standards

The Idaho Congressional and Legislative Districts Data Standard follows the same format as
other Idaho geospatial framework data standards. The Idaho Congressional and Legislative
Districts Standard may contain some of the same attributes as other framework standards and
may adopt the field name, definition, and domain from the other standards to promote
consistency.

Redistricting plans, and thus the resulting geographic dataset, need to follow a number of
Federal and State Constitutional requirements. Those requirements are detailed in the
metadata associated with the spatial layers, as well as in the online redistricting criteria chart.

2.5. Technical and Operation Context

   2.5.1. Data Environment

   The data environment is a digital vector polygon with a specific, standardized set of
   attributes pertinent to the Idaho Congressional and Legislative Districts Framework.
   Idaho Congressional and Legislative Districts Data shared under this standard must be in
   a format supporting vector polygon.

   2.5.2. Reference Systems

   The Idaho Congressional and Legislative Districts Framework will be published in the
   Idaho Transverse Mercator (IDTM) NAD83 coordinate system, which is the State of
   Idaho’s single zone coordinate system. Data is not required to be submitted in the ITDM
   coordinate system but must have a defined coordinate system clearly described in the
   metadata.

   2.5.3. Global Positioning Systems (GPS)

   Some data provided might contain geometry from GPS methods, and the provided
   metadata should describe this, if applicable. However, geometry from a GPS is not
   required to meet this standard.

   2.5.4. Interdependence of Themes

   Idaho Congressional and Legislative Districts geometry may be coincident with other
   framework data, such as Geometry coincident with census 2020 block layer. At this time
   there is no enforcement of coincidence or topology relationships between Idaho
   Congressional and Legislative Districts Framework and other Idaho Framework
   elements.

                                                                                                  8

2.5.5. Encoding

When data is imported into, and exported from, the Idaho Congressional and Legislative
Districts Framework, encoding will take place to convert data formats and attributes.

2.5.6. Resolution

No specific requirements for resolution are specified in this standard. Resolution will be
documented in the metadata.

2.5.7. Accuracy

Data is based on 2020 Census Block level data and follows the accuracy standards laid
out for that dataset.

2.5.8. Edge Matching

No edge matching is required between jurisdictions, or between this and other framework
layers.

2.5.9. Unique Identifier

The DISTRICT attribute which represents the legislative district number or the
congressional district number in the Legislative District and Congressional District,
respectively.

2.5.10. Attributes

Attributes for public and intergovernmental distribution are described in Section 3 of this
standard.

2.5.11. Stewardship

Perpetual maintenance and other aspects of lifecycle management are essential to Idaho
Congressional and Legislative Districts Framework. Details of stewards, their roles and
responsibilities, and processes, are set forth in a Idaho Congressional and Legislative
Districts Framework Stewardship Plan and related documents.

                                                                                             9

      2.5.12. Records Management and Archiving

      Congressional districts boundary lines are drawn every ten years based on the Census
      block data.

      2.5.13. Metadata

      The Idaho Congressional and Legislative Districts Framework metadata will describe the
      methods used to update and aggregate the individual Idaho Congressional and Legislative
      Districts data contributions, processes or crosswalks performed, definition of attributes,
      and other required information. This metadata will conform to the metadata standards as
      set out in ITA Standard S4220 Geospatial Metadata.

3. Data Characteristics

   3.1. Minimum Graphic Data Elements

   The geometry of the features in Idaho Congressional and Legislative Districts Framework is
   vector polygon.

   3.2. Optional Graphic Data Elements

   Not applicable.

                                                                                             10

  3.3. Standard Attribute Schema

  Congressional and Legislative Districts both use the same Schema.

  Field Name           Alias        Data Type     Length                   Description                  Examples
                                                               Legislative or Congressional
                                                                                                           1
DISTRICT       District Number        Text          12         District Number

                                                               Census 2020 Population of Idaho
                                      Long                     used in determining district             919,553
POPULATION     Total Population      Integer                   boundaries
               Non-Hispanic           Long                     Size of Non-Hispanic White
                                                                                                        735,930
NH_WHT         White                 Integer                   population from 2020 Census
               Black or African       Long                     Size of Black or African American         11,407
AP_BLK         American              Integer                   population from 2020 Census
                                                               Size of American Indian and
               American Indian        Long                     Alaska Native population from             35,261
AP_IND         and Alaska Native     Integer                   2020 Census
                                      Long                     Size of Asian population from             21,566
AP_ASN         Asian                 Integer                   2020 Census

               Native Hawaiian                                 Size of Native Hawaiian and Other
               and Other Pacific      Long                     Pacific Islander population from          4,623
AP_HWN         Islander              Integer                   2020 Census
                                      Long                     Size of Hispanic or Latino
                                                                                                        108,783
HISPANIC_O     Hispanic or Latino    Integer                   population from 2020 Census
                                                               Size of population belonging to any
                                                               race not included in any other
                                                                                                         87,880
                                      Long                     attribute in this table from 2020
AP_OTH         Other Race            Integer                   Census
                                                               Ideal population size calculated as
               Ideal Population                 Precision: 7   Idaho’s total population divided by      919,553
IDEAL_VALU     Value                 Double       Scale 1      the number of districts
                                                               Difference between actual
               Deviation from                   Precision: 7   population in a district and the ideal      0
DEVIATION      Ideal Value           Double       Scale 1      population value
               Percent Deviation                Precision: 4   Percent deviation from the ideal
                                                                                                         0.00%
F_DEVIATIO     from Ideal Value      Double       Scale 2      value
                                                               Number of square miles contained
                                                Precision: 7   in a Legislative or Congressional        39,813.30
AREA           Square Miles          Double       Scale 2      District

  3.4. Data Quality

  Data quality considerations for Idaho Congressional and Legislative Districts need to
  conform to Federal and Idaho Constitutional Criteria as highlighted in the Redistricting
  Criteria Chart published by the Idaho Legislative Services Office and The Idaho Commission
  for Reapportionment.

                                                                                                           11

1. Congressional Plan:
      a. U.S. Constitutional Requirements (must be satisfied above all other criteria):
                i. Districts must have a population that is as nearly equal as practicable.
      b. Statutory Requirements (mandatory – must be satisfied above advisory criteria.
          Must be balanced out with each other.
                i. Determine district population using U.S. census date exclusively.
               ii. Avoid county division.
             iii. Include contiguous counties in a district containing more than one county.
              iv. Don’t divide counties to protect political parties or incumbents.
               v. Preserve traditional neighborhoods and communities of interest.
              vi. Retain precinct boundaries.
      c. Statutory Criteria – advisory. Satisfy as possible.
                i. Avoid oddly shaped districts.
               ii. Keep divisions per county to a minimum.
2. Legislative Plan:
      a. U.S. Constitutional Requirements (must be satisfied above all other criteria):
                i. Districts must have substantially equal population.
      b. Idaho Constitutional Criteria (must be satisfied above all statutory criteria)
                i. Include contiguous counties in a district containing more than one county.
               ii. Don’t divide counties, except as necessary to comply with U.S.
                   Constitution
             iii. A county may be divided into more than one district when the districts are
                   wholly contained within that county.
      c. Statutory Criteria – Mandatory. Must be satisfied above advisory criteria. Must be
          balanced with each other.
                i. Determine district population using U.S. census data exclusively.
               ii. Avoid county division.
             iii. Include contiguous counties in a district containing more than one county.
              iv. Don’t divide counties to protect political parties or incumbents.
               v. Preserve traditional neighborhoods and communities of interest.
              vi. Retain precinct boundaries.
             vii. Ensure that districts containing more than one county, or a portion of the
                   county are connected by interstate or by U.S. or state highway.
      d. Statutory Criteria – advisory. Satisfy as possible.
                i. Avoid oddly shaped districts.
               ii. Keep divisions per county to a minimum.

                                                                                          12

Appendix A: References

Idaho Technology Authority (ITA). Information and Data Policy P5000, Category: P5030
Framework Standards Development Policy. https://ita.idaho.gov/psg/p5030.pdf

Idaho Technology Authority (ITA). Enterprise Standards S4000 Geographic Information
Systems (GIS) Data, Category: S4220 Geospatial Metadata. https://ita.idaho.gov/psg/s4220.pdf

Idaho Commission for Reapportionment, Final Report. November 10, 2021.
https://sos.idaho.gov/elections/data/redistricting/2021/Final_Report.pdf

Idaho Commission for Reapportionment, 2021. Legal Criteria for Redistricting Plans.
https://legislature.idaho.gov/wp-
content/uploads/redistricting/2021/Redistricting_Criteria_Chart.pdf

Appendix B: Glossary

See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

                                                                                           13

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
