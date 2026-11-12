---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s3550
title: S3550 – Network Connectivity and Transport – Structured Cabling
doc_type: standard
citation: ITA Standard S3550
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s3550-ADA.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 581a577cff950cedc28c245c4d84f7caad6816b78bbc726e934bc5b5cf8f057e
effective_date: '2002-04-24'
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# S3550 – Network Connectivity and Transport – Structured Cabling (ITA Standard S3550)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '3000 - Network and Telecommunications, Standards', a standard. The library's own summary: "ITA Standard S3550 establishes guidelines for structured cabling systems in state agencies, ensuring reliable and efficient network connectivity and transport."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S3000 NETWORK AND
TELECOMMUNICATIONS

Category:     S3550 – NETWORK CONNECTIVITY AND TRANSPORT – STRUCTURED
              CABLE IDENTIFICATION

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

   Structured cabling is a standards-based approach to cable plant installation (inside
   wiring) within a facility or group of buildings. Cable identification refers to the unique
   informational naming of every cable.

II. RATIONALE

   Idaho State Agencies utilize a broad diversity of devices that need to be connected via a
   common physical infrastructure. An industry recognized standards-based installation and
   management approach results in uniform wiring at different locations, improved
   management of building space resources and reduced costs for wiring installation,
   support and management.

III. APPROVED STANDARD(S)

   1. ANSI/TIA/EIA 568, Commercial Building Telecommunications Cabling Standard
      (most current version);

   2. ANSI/TIA/EIA 569, Commercial Building Standard for Telecommunication Pathways
      and Spaces (most current version); and

   3. ANSI/TIA/EIA 606, Administration Standard for the Telecommunication Infrastructure
      of Commercial Buildings (most current version).

S3550 – Network Connectivity and Transport – Structured Cable Identification           Page 1 of 8

IV. APPROVED PRODUCT(S)

   Standards-based

V. JUSTIFICATION

   The Electronics Industry Association (EIA) and Telecommunications Industry Association
   (TIA) standards are the primary international standard for structured cabling systems.
   These standards have also been fully or partially included in the National Electrical Code
   (NEC), American National Standards Institute (ANSI), the National Electrical
   Manufacturers Association (NEMA), and Underwriters Laboratories (UL).

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

   Increased network data traffic and application demands continue to drive the need for
   adequate and reliable wiring in state facilities. Agencies should require electrical,
   telecommunications or wiring contractors to adhere to these standards for cable plant
   installation. Agencies should also ensure that premises wiring installations conform to
   any applicable electrical, fire, or safety code. It is also important to carefully consider the
   physical, logical, and network security implications of the deployment and maintenance
   of structured cabling.

   This policy does not require recabling existing installations to conform to newer
   standards, but supports recabling to the latest standards when dictated by safety,
   operational or business considerations.

   Cable naming standards are intended to follow the TIA-EIA 606-A standard. For
   additional detail, refer to sections 5.1.2 Horizontal Link Identifier, 6.1.1 Building
   Backbone Cable Identifier and 7.1.2 Campus Backbone Cable Identifier in the TIA-EIA-
   606-A definitions document.

   1) State of Idaho Identification format for the Campus and Backbone Cable
      Identifier:
         a) CCC-BBB-TS1F(D)/CC-BBB- TS2F(D)-NN.dd, Where:
                  i) CCC= 3 Alpha Campus Identifier. Identifiers are listed in item (e)
                       below. Intra-campus cabling does not require the Campus
                       Identifier.
                  ii) BBB= Building Identifier, 3 Alpha. The Building Identifier will be
                       included in all backbone cable records and labeling. Identifiers are
                       listed in item (f) below.
                  iii) TS1, TS2 = Telecommunications Space Identifier, 2 to 4 Alpha
                  iv) F=Floor, 1-2 Numeric
                  v) D= Direction, Optional (North, South, East, West)
                  vi) NN = Number of the cable between the two spaces, 2 numeric,
                       fixed

S3550 – Network Connectivity and Transport – Structured Cable Identification           Page 2 of 8

                 vii) dd = Numeric identifier for each strand (fiber) or pair (copper) in
                      the cable.
           b) Each cable shall be uniquely identified. The Campus, Building or
              Telecommunications Space (TS) with the lesser alpha-numeric identifier
              shall be listed first. Both ends of each cable will be identified identically.
           c) Note: Capitol does not follow convention. Per the standard, EFNO should
              actually have been designated EFGN for Telecommunications Entrance
              Facility, Garden Level, North side.
           d) Examples:
             CAP-EFNO/CAP-EFNO1-01
             Capitol Building, Telecommunications Entrance Facility CONNECTS THE
             Capitol Building, Telecommunications Entrance Facility Cage 1, Cable 01.
             This is the first identified cable between the two points. The cable is
             identified with this ID at both ends.
             CAP-EFNO1/CAP-EFNO2-01
             Capitol Building, Telecommunications Entrance Facility Cage 1
             CONNECTS THE Capitol Building, Telecommunications Entrance Facility
             Cage 2, Cable 01. This is the first identified cable between the two points.
             The cable is identified with this ID at both ends.
             PTC-ELB/JRW-TR5-02
             PTC Building, Electrical Room, Basement CONNECTS THE JRW
             Building, Telecommunications Room, 5th Floor, Cable 02. This is the
             second identified cable between the two points. The cable is identified with
             this ID at both ends.

           e) Campus Identifiers:
             Campus                      Identifier                  Location
             Capitol Mall                CPM                         Boise
             ISP Campus                  ISP                         Meridian
             ITD Campus                  ITD                         Boise
             Old Pen Campus              PEN                         Boise
             Orchard Campus              ORC                         Boise

           f) Building Identifiers:
            Address1                           Address2        City            Building ID
            1299 N ORCHARD ST                  STE 110         BOISE           COR
            1215 W STATE ST                                    BOISE           SIF
            317 W MAIN ST                                      BOISE           IAB
            3311 W STATE ST                                    BOISE           ITD
            450 W STATE ST                                     BOISE           PTC
            607 N 8TH ST                                       BOISE           PER
            650 W STATE ST                                     BOISE           LBJ
            700 S CLEARWATER LN                                BOISE           IIC
            700 S STRATFORD DR                                 MERIDIAN        ISP

S3550 – Network Connectivity and Transport – Structured Cable Identification           Page 3 of 8

            Address1                           Address2        City            Building ID
            700 W STATE ST                                     BOISE           JRW
            800 E PARK BLVD                                    BOISE           TAX
            1455 N ORCHARD                                     BOISE           PTV
            325 W STATE ST                                     BOISE           LIB
            514 W JEFFERSON ST                                 BOISE           ANN
            4040 W GUARD ST                    BLDG 600        BOISE           BHS
            304 W STATE ST                                     BOISE           ALX
            700 W JEFFERSON ST                 CAPITOL         BOISE           CAP
                                               BUILDING
            500 STATE ST                       ITD Fiber       BOISE           SPL
                                               Vault at 5th
                                               and State
            550 W STATE ST                                     BOISE           GAR
            472 W WASHINGTON ST                                BOISE           PUC
            502 N 4th ST                                       BOISE           DPW
            451 W STATE ST                                     BOISE           JSC
            304 N 8th ST                                       BOISE           BOR

           g) Space Identifiers:
            ID_Code    ID Description                                             ID_Type
            BRG        Bridge                                                     Pathway
            BRG        Bridge                                                     Spaces
            CER        Common Equipment Room                                      Spaces
            CO         Central Office                                             Spaces
            CTR        Common Telecommunications Room                             Spaces
            DBL        Direct buried locale                                       Pathway
            DBL        Direct buried locale                                       Spaces
            DM         Demarcation (NI)                                           Spaces
            EF         Entrance Facility. This is where                           Spaces
                       telecommunications links first terminate within the
                       building. All other telecommunications rooms
                       should be designated TR
            EL         Electrical Room                                            Spaces
            EN         Entrance                                                   Pathway
            EN         Entrance                                                   Spaces
            ER         Equipment Room. Use when identifying rooms                 Spaces
                       that have a mix of telecommunications, computing
                       and other equipment.
            HH         Handhole                                                   Spaces
            HH         Handhole                                                   Pathway
            MH         Maintenance hole                                           Pathway
            MH         Maintenance hole                                           Spaces
            NOC        Network Operations Center                                  Spaces
            PE         Pedestal                                                   Pathway

S3550 – Network Connectivity and Transport – Structured Cable Identification           Page 4 of 8

            ID_Code       ID Description                                        ID_Type
            PE            Pedestal                                              Spaces
            RT            Rooftop                                               Spaces
            RT            Rooftop                                               Pathway
            SML           Submerged locale                                      Pathway
            SML           Submerged locale                                      Spaces
            SPS           Service Provider Space                                Spaces
            SR            Switch Room                                           Spaces
            SRV           Server Room                                           Spaces
            STAR          Logical center of the data network                    Spaces
            SZ            Serving Zone                                          Spaces
            TN            Tunnel                                                Pathway
            TN            Tunnel                                                Spaces
            TPP           Telephone pole                                        Spaces
            TPP           Telephone pole                                        Pathway
            TR            Telecommunications Room. Use when identifying         Spaces
                          rooms that have ONLY telecommunications
                          equipment.
            VL            Vault                                                 Pathway
            VL            Vault                                                 Spaces
            WS            Workstation location                                  Spaces
            WTRS          Wireless Transmission and Reception Space             Spaces

2) State of Idaho Identification format for the Horizontal Link Cable Identifier:
   A horizontal link identifier, unique within the building, shall be assigned to each
   horizontal link and to its elements.

   A horizontal link identifier shall have a format of fs-an, where,
           a) fs = the Telecommunications Space (TS) identifier
           b) a = one or two alpha characters uniquely identifying a single patch panel,
              a group of patch panels with sequentially numbered ports, an IDC
              connector (punch-down block), or a group of IDC connectors, serving as
              part of the horizontal cross-connect
           c) n = two to four numeric characters designating the port on a patch panel,
              or the section of an IDC connector on which a four-pair horizontal cable is
              terminated in the TS.
   All horizontal link identifiers in a single infrastructure should have the same format where
   possible. The recommended format, to accommodate the majority of systems, is fs-
   annn. See annex A for examples.

   For a copper horizontal link, the elements include:
      1) the connecting hardware, e.g., patch panel port or the section of an IDC
          connector (punch-down block) terminating a four-pair horizontal cable
      2) a four-pair horizontal cable
      3) a telecommunications outlet/connector terminating a four-pair horizontal
          cable in the work area

S3550 – Network Connectivity and Transport – Structured Cable Identification             Page 5 of 8

       4) if a consolidation point (CP) is present:
               a) the segment of four-pair horizontal cable extending from the TS to the
                  CP connecting hardware
               b) the CP connecting hardware or section of an IDC connector
                  terminating a four-pair horizontal cable
               c) the segment of four-pair horizontal cable extending from the CP
                  connecting hardware to the outlet/connector, if present
               d) if a MUTOA (Multi-User Telecommunications Outlet Assembly) is
                  present, a telecommunications outlet/connector in the MUTOA

For an optical fiber horizontal link, the elements include:
      1) a pair of optical fiber terminations on a patch panel in the TS
      2) a pair of optical fibers in a cable
      3) a pair of optical fiber terminations in the work area
      4) a telecommunications outlet/connector terminating a pair of optical fibers in
          the work area
      5) if a consolidation point (CP) is present:
          a) the segment of optical fiber cable extending from the TS to the CP
              connecting hardware
          b) the CP connecting hardware or section terminating a pair of optical fibers
          c) the segment of optical fiber cable extending from the CP connecting
              hardware to the outlet/connector, if present
          d) if a MUTOA is present, a telecommunications outlet/connector in the
              MUTOA

The pair of optical fiber terminations may be two simplex connectors or one duplex
connector, and includes adapters, if present.

When consolidation points are used, some elements of the horizontal link may not be
installed initially. All elements shall be labeled at the time they are installed.

In class 1 systems only, the fs portion of the horizontal link identifier may be omitted from
labels. The full horizontal link identifier is the recommended format.

In the TS, each patch panel port or section of IDC connector shall be labeled with the an
portion of the identifier. This requirement may be met by labeling a patch panel with the a
portion of the identifier, and each port with the n portion. The port numbers marked on a
patch panel by its manufacturer may be used as the n portion. Similarly, an IDC connector
or group of IDC connectors may be labeled with the a portion of the identifier, and the
section of an IDC connector terminating a four-pair horizontal cable labeled with the n
portion.

Each end of a horizontal cable shall be labeled within 300 mm (12 in) of the end of the cable
jacket with the horizontal link identifier, which shall be visible on the exposed part of the
cable jacket. This shall include each cable end in the TS, at the work area, and at a CP, if
present.

S3550 – Network Connectivity and Transport – Structured Cable Identification         Page 6 of 8

In the work area, each individual telecommunications outlet/connector shall be labeled with
the horizontal link identifier. The labeling shall appear on the connector, faceplate, or
MUTOA, in a way that clearly identifies the individual connector associated with the
particular identifier.

A horizontal cable containing more than one horizontal link, such as a hybrid cable
containing multiple four-pair sub-units or an optical fiber cable with four or more optical
fibers, shall be identified with the lowest alpha-numeric horizontal link identifier of the four-
pair sub-units or pairs of optical fiber in the cable. See annex A.1 for examples.

3) Horizontal link records.

   Horizontal link records shall contain the following information:
   a) horizontal link identifier (primary indexing identifier, e.g., 1A-A47)
   b) cable type (e.g., 4-pair, UTP, category 5e, plenum)
   c) location of telecommunications outlet/connector (room, office, or grid location)
   d) outlet connector type (e.g., 8-position modular, T568A, category 5e)
   e) cable length (e.g., 51m/166ft)
   f) cross-connect hardware type (e.g., 48-port modular patch panel, T568A,
      category 5e)
   g) service record of link (e.g., passed category 5e at installation 1/12/01, re-
      terminated and re-tested at cross-connect 4/22/01 due to broken wire)

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

   There are no emerging trends and architectural directions for this standard.

VIII. PROCEDURE REFERENCE

   Network Connectivity and Transport – Structured Cabling used on the State of Idaho’s
   Wide Area Network must comply with the Department of Administration’s “P3020 –
   Connectivity and Transport Protocols.”

IX. REVIEW CYCLE

   Twelve (12) Months

X. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

S3550 – Network Connectivity and Transport – Structured Cable Identification            Page 7 of 8

REVISION HISTORY

   07/01/13 – Changed “ITRMC” to “ITA”.

   10/01/10 – Cable naming standards added

   6/16/09 – Added Emerging Trends and Architectural Directions and Procedure
             Reference to this standard; changed the layout and deleted Timeline

   9/13/06 – Section VIII, Review Cycle, updated to reflect 12-month review rather than 6-
             month review. Warranted due to well established industry standard with
             language in the state standard that allows automatic accommodation to
             updates to the industry standard.

   7/20/05 – Revised to remove references to outdated revisions, allowing the State to
             automatically remain current with the industry.

              Effective Date:        April 24, 2002

S3550 – Network Connectivity and Transport – Structured Cable Identification     Page 8 of 8

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
