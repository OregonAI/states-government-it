---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s4210
title: S4210 – Single Zone Coordinate System for GIS Data
doc_type: standard
citation: ITA Standard S4210
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s4210.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: b35f23f11ca33de21b30cb22cba295483b61570156c4658942a8bed245bc83df
effective_date: '2005-07-20'
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

# S4210 – Single Zone Coordinate System for GIS Data (ITA Standard S4210)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '4000 - Information and Data, Standards', a standard. The library's own summary: "ITA Standard S4210 establishes a single zone coordinate system for GIS data, ensuring uniformity and accuracy in geospatial data across state agencies."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S4000 INFORMATION AND DATA

Category:     S4210 – SINGLE ZONE COORDINATE SYSTEM FOR GIS DATA

CONTENTS:
I.    Definitions
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

I. DEFINITIONS

   See ITA Guideline G105 (ITA Glossary of Terms) for definitions.

II. RATIONALE

   GIS data for statewide coverage is best represented by a single-zone system. Idaho
   State Plane Coordinate System divides Idaho into three zones. Under the UTM system,
   Idaho is bisected into two zones. IDTM projects the State in a single zone. IDTM was
   implemented with a horizontal datum of NAD27 (North American Datum of 1927). North
   American Datum of 1983 (NAD83) is based on a more accurate earth-model than is
   NAD27 and its modernization. NAD83 is more compatible with modern survey methods,
   which use the Global Positioning System (GPS).

III. APPROVED STANDARD(S)

   1. Projection Name – Idaho Transverse Mercator NAD83 (IDTM83);

   2. Units – Meters;

   3. Datum – NAD83;

   4. Vertical Datum – NAVD88;

   5. Scale Factor – .99960;

S4210 – Single Zone Coordinate System for GIS Data                            Page 1 of 3

   6. Central Meridian – -114°00’00”;

   7. Latitude of Origin – 42°00’00”;

   8. False Easting – 2500000; and

   9. False Northing – 1200000.

IV. APPROVED PRODUCT(S)

   There are no approved products for this standard.

V. JUSTIFICATION

   IDTM was developed for use in Idaho to have the whole State under one projection for
   statewide data. Using the NAD83 datum supports consistency with: 1) federal, local, and
   tribal partners; 2) original intent of the IDTM projection; and 3) geometric improvements in
   the NAD83 datum. The False Northing and False Easting parameters were chosen so as
   to 1) avoid confusion between IDTM and IDTM83 coordinates, and 2) avoid confusion
   between the projections’ respective False Northing and False Easting coordinates.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

   IDTM has been in use in Idaho using NAD27 Datum since 1994. GIS data using the
   IDTM projection with the NAD27 datum will need to be “re-projected” to convert to the
   new projection parameters of IDTM83. It is the preferred projection for data exchange,
   and is appropriate for statewide applications.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

   There are no emerging trends and architectural directions for this standard.

VIII. PROCEDURE REFERENCE

   ITA Standard S4210 (Single Zone Coordinate System for GIS Data) used on the State of
   Idaho’s Wide Area Network (WAN) must comply with ITA Policy P1070 (Geographic
   Information Systems (GIS)).

IX. REVIEW CYCLE

   Twelve (12) Months

X. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

S4210 – Single Zone Coordinate System for GIS Data                                  Page 2 of 3

REVISION HISTORY
   5/6/19 –  Removed individual definitions and replaced with reference to ITA
             Guideline G105 (ITA Glossary of Terms)

    7/01/13 –    Changed “ITRMC” to “ITA”.

    2/2/11 –     Title changed from “Projection”, also 4000 group title changed from “GIS
                 (Geographic Information Systems) Data”

    6/16/09 –    Added Approved Products, Emerging Trends and Architectural Directions,
                 and Procedure Reference to this standard and deleted Timeline.

    3/7/07 –     Review cycle adjusted to 12 months.

         Effective Date: July 20, 2005

S4210 – Single Zone Coordinate System for GIS Data                               Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
