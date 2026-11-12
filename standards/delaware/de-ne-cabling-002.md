---
schema_version: 1
corpus: states-government-it
jurisdiction: delaware
id: de-ne-cabling-002
title: Structured Cabling System Standards and Specifications for State-Managed Facilities
doc_type: standard
citation: DTI Standard ID NE-Cabling-002
authority_level: ''
issuing_body: Delaware Department of Technology and Information (DTI)
source_url: https://webfiles.dti.delaware.gov/pdfs/pp/CablingAndWiringStandard.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: f06e3959546697c0437553ed0d990b25f2900da847705dd7cf6582c1ee1ffea8
effective_date: '2008-07-21'
source_version: Revision 8 (reviewed 1/29/2021)
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

# Structured Cabling System Standards and Specifications for State-Managed Facilities (DTI Standard ID NE-Cabling-002)

## At a glance

Item of the DTI Standards and Policies library, section 'Network': a standard (the library lists it as 'Cabling and Wiring Standard') of the Delaware State-Wide Information Technology and Architecture Standards (Domain: Network and Storage; Discipline: Cabling).

## Full text

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

         Standard ID:        NE-Cabling-002
                  Title:     Structured Cabling System Standards and Specifications for State-
                             Managed Facilities
 Revision Number:            8

               Domain:       Network and Storage
           Discipline: Cabling
              Effective: 7/21/2008
               Reviewed: 1/29/2021
         Approved By: Chief Information Officer
                Sponsor: Chief Operating Officer

      A. Authority: Title 29 Chapter 90C Delaware Code, §9004C – General Powers, duties and
         functions of DTI “2) Create, implement and enforce statewide and agency technology solutions,
         policies, standards and guidelines, including as recommended by the CIO”

      B. Applicability: Applies to all State of Delaware communications and computing resources. DTI is
         an Executive Branch Agency and has no authority over the customers in Legislative and Judicial
         Branches, as well as Local Education Agencies, and other Federal and Local Government
         entities that use these resources. However, all users, including these entities, must agree to
         abide by all policies, standards promulgated by DTI as a condition of funding, access and
         continued use of these resources.
      C. Purpose: Cable configuration and installation is critical to providing connectivity in State buildings.
         This standard provides guidance for the design and installation of cabling. This standard provides
         guidance and requirements for data, voice, and CATV structured cabling systems and support
         infrastructure in all State owned and leased facilities and buildings.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directed to dti_tasc@delaware.gov

Page 1 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                            TECHNOLOGY AND ARCHITECTURE STANDARDS

Table of Contents
PART 1 Scope...................................................................................................................................... 3
PART 2 Process ................................................................................................................................... 3
PART 3 Executive Summary............................................................................................................... 3
PART 4 Objective................................................................................................................................ 4
PART 5 Credits.................................................................................................................................... 5
PART 6 Introduction............................................................................................................................ 5
PART 7 Procedures.............................................................................................................................. 8
PART 8 Horizontal Distribution System ............................................................................................. 9
PART 9 Communications/Data Rooms/Closets (General)................................................................ 11
PART 10 MDF & IDF Product Specifications .................................................................................. 25
PART 11 Information Outlets............................................................................................................ 37
PART 12 Cable Routing Systems...................................................................................................... 42
PART 13 Cabling-General................................................................................................................. 43
PART 14 Horizontal CABLING - Category 6 UTP Data ................................................................. 44
PART 15 Vertical Distribution Systems............................................................................................ 47
PART 16 Campus Cabling................................................................................................................. 50
PART 17 Patch Cables....................................................................................................................... 51
PART 18 Fire Stop - Penetration Sealant .......................................................................................... 55
PART 19 Testing ............................................................................................................................... 55
PART 20 Appendix A – Communications Planning Checklist ........................................................ 60
PART 21 Appendix B - Cable Installation Checklist ........................................................................ 61
PART 22 Appendix C - Quality Assurance ....................................................................................... 62
PART 23 Appendix D - Codes, Regulations and Standards.............................................................. 63
PART 24 Appendix E - Warranty...................................................................................................... 63
PART 25 Appendix F - Bid/Quote Response Format ....................................................................... 63
PART 26 Appendix G - Outside - DELDOT Specific Requirements - Traffic
Construction…................................................................................................................................... 65
PART 27 Appendix H - Certified Contractor List............................................................................. 69
PART 28 Appendix I – Approved Equivalent Vendors…………………………………………….70

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 2 of 69               8/9/2016                   11:54:59 AM                       CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

PART 1          SCOPE
       A.      Areas Covered: This standard covers the best practices and installation requirements for Voice,
               Data, CATV cabling and support structures including conduits and raceways, Voice and Data
               rooms and closets.
       B.      Environments: This standard applies to all State owned and leased building and office spaces. It
               is concerned with all Data, Voice and CATV cabling projects, whether they are for new
               construction or revisions additions and upgrades to existing systems.

PART 2          PROCESS
       A.      Adoption: These standards have been adopted by the Department of Technology and
               Information (DTI) through the Technology and Architecture Standards Committee (TASC) and are
               applicable to all Information Technology use throughout the State of Delaware.
       B.      Revision: Technology is constantly evolving; therefore, the standards will need to be regularly
               reviewed. It is the intent of the TASC to review each standard annually. The TASC is open to
               suggestions and comments from knowledgeable individuals within the State, although we ask that
               they be channeled through your Information Resource Manager (IRM).
       C.      Contractors: Contractors or other third parties are required to comply with these standards when
               proposing technology solutions to DTI or other State entities. Failure to do so could result in
               rejection of the proposed technology solution. For further guidance, or to seek review of a
               component that is not rated below, contact the TASC at dti_tasc@delaware.gov.
       D.      Implementation responsibility: DTI and/or the organization’s technical staff will implement
                these best practices during the course of normal business activities, including business case
                review, architectural review, project execution and the design, development, or support of
                systems.
       E.      Enforcement: DTI will enforce these best practices during the course of normal business
               activities, including business case and architectural review of proposed projects and during the
               design, development, or support of systems. These best practices may also be enforced by
               others during the course of their normal business activities, including audits and design reviews.
       F.      Contact us: Any questions or comments should be directed to dti_tasc@delaware.gov.

PART 3           EXECUTIVE SUMMARY
Because of ever-advancing Industry Standards and new Alliances between Cable and Hardware
Manufactures and Vendors, this document seeks to enhance and clarify the State of Delaware’s wiring and
cabling standards and specifications for Structured Cabling Systems. Approved Contractors under State of
Delaware Contract No. GSS16441-DATA_CBL are required to adhere to these specifications and
standards.
The structured cabling system will support Voice, Data, and imaging applications within State-owned and -
leased office facilities. This document describes the Structured Cabling System requirements to be met in
the proposals for Communications cabling by Vendors and Contractors. These requirements encompass all
materials, design, engineering, installation, supervision, and training services for a Structured Cabling
System.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 3 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

The following are examples of the Structured Cabling Systems that can be bid for new construction and
whole building renovations, in which case all building structured cabling wiring is replaced. The choice of a
Structured Cabling System is not limited to the Vendors or Manufactures listed below. The Channel
Solutions shall be bid when possible. If a Link solution is bid the State Contact, PM, or DTI (Department of
Technology and Information) must authorize the installation.

In new construction projects, the default cabling infrastructure shall be Category 6 unless specified
otherwise. Where building renovations and additions do not require the removal of the existing structured
cabling system, the existing cabling in conjunction with new cabling should maintain the system warranties. If
the existing structured cabling system is not Category 5e or better, it must be upgraded to CAT6 or better
with a matching patch panel.

•        Hubbell Premise Wiring
•        Ortronics
•        Panduit
•        Systimax

    A.    Terms and Conditions of Bids/quotes
           1. An approved Contractors bid submittal should be based on the materials, systems, equipment,
              and Standards described in this document and in the bid response format of the attached
              example. Refer to Appendix G. All bids must be submitted in accordance with the specifications
              and information contained herein, as well as with any addenda, if required.
           2. The bid package shall be accompanied by a presale warranty commitment, binding the
              Installation Contractor and Manufacturer to the customer-selected extended warranty package
              and adhere to the Additional Terms and Conditions as described in Delaware Contract No.
              GSS16441-DATA_CBL.
           3. At any point in time, should you require clarification or have any questions pertaining to the
              content of this document, please call The State of Delaware Department of Technology and
              Information (DTI). 302-739-9500

PART 4           OBJECTIVE
This document has been developed as a source of information to assist in the design, implementation and
maintenance of Voice, Data and Broad Band communications systems. It contains standards and
specifications which guide users through structured cabling system design, planning, and installation.
To maximize the usefulness of this document, access to the various TIA/EIA (Telecommunications Industry
Association/Electronic Industries Alliance), IEEE (Institute of Electrical and Electronics Engineers), BICSI,
(Building Industry Consulting Service International), NEC (National Electrical Code), NFPA (National Fire
Protection Association) Communications Standards, and implementation and installation Manuals for further
reference is required. This document assumes that users have communications knowledge and training in all
aspects of design, implementation, installation, and testing of a Voice/Data communications system.

This document does not address safety issues associated with use. It is the individual’s responsibility to use
established and appropriate safety and health practices and to determine the applicability of all regulations.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 4 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

PART 5         CREDITS
Communications Cabling Construction
Developed by:
State of Delaware Department of Technology & Information
801 Silver Lake Blvd. Dover, DE
19904
The content of this document is drawn from experience, as well as other documents
and manuals, including the following:
• NEC 2011/2013 Code book
• NFPA-70 Publications
• TIA/EIA Communications Building Wiring Standards
• IEEE Publications & Standards
• BICSI Communications Distribution Design and Installation Publications
• MOTOROLA R56 Standards and Guideline for Communications
• Various Manufactures Publications and Requirements

PART 6         INTRODUCTION
Any Structured Universal Cabling System installed for the Agencies of the State of Delaware is designed to
meet known and anticipated technology needs within the State. An advanced building cabling system
provides for more than communication services; it provides an infrastructure for an institution’s entire
communications network. Instead of being a basic utility, it is as important as the high-tech systems that
transmit signals over it and is an integral component of the State’s overall information network.
These designs provide a universal and flexible cabling system for workstations, conference rooms, and
laboratories. Today’s cabling system must be multi- functional and provide service for telephones,
computers, fax machines, LANs, WANs, broad band fiber optic and coaxial systems (CATV, SATV, CCTV.),
Data Centers, computer-aided design workstations, Audio Video systems (AV), and other technologies. For
a cabling system to be capable of meeting today’s technology and institutional demands, it must have high
bandwidth capacity and transmission speed while being extremely flexible.
This wiring architecture incorporates the applicable ANSI/EIA/TIA standards, BICSI guidelines and the latest
technologies. This cabling distribution plan can integrate all types of systems from a variety of vendors. The
design uses a subsystem approach, which allows for changes in the system without affecting other parts of
the system. The Main Distribution Frame (MDF) and Intermediate Distribution Frame (IDF) Room equipment
racks are designed to allow for growth, and the cable routing is accomplished through the provision of cable
trays, conduits, sleeves, raceways, and cable hangers where required. Ease of administration and
recordkeeping for moves and changes is readily apparent, as is the flexibility that a structured cabling
system provides.
The wiring medium for the Communications Cable Network consists of Category 6+– 6a 24AWG Unshielded
Twisted Pair (UTP) for station cabling and multi pair twisted copper for backbone cabling to support low-
speed voice or Data, Category 6+ or 6a for high speed LAN technologies, and 50/125 micron multi-mode
fiber optic cable and 50/125 micron multi-mode as well as single mode 8.3/125 micron for even higher
bandwidth requirements. The unshielded twisted pair (UTP) Category 6+ or 6a LAN cables can support Data
transmission rates of 100, 250 and 500 up to 1000Mb/Sec respectively according to EIA/TIA Standards and
manufacturers’ specifications.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 5 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

These leading edge components, combined with the open wiring architecture, provide the technology,
flexibility, and modularity that allow the system to grow and change to meet changing needs.
The central distribution location of the system is the Fiber Optic, coaxial and Copper Main Distribution Frame
(MDF) located within the centrally located MDF/IDF Room of each building. Various fiber optic, coaxial and
copper riser cables terminate on the MDF and extend to the Communications Rooms/Closets (IDFs) located
throughout the buildings. Each building typically has one MDF/IDF Room and a varying number of IDF
rooms/closets dictated by the horizontal station cabling limitation of 100 meters for high performance cable.
The distance from the information outlet to the termination within the IDF is limited to 90 meters (the
permanent link). The IDF room/closet houses the Intermediate Distribution Frame (IDF), Copper and Fiber
Optic IDF Patch Panels, Local Area Network (LAN) equipment, and other electronics. Both the riser cables
and the horizontal station cables feeding the floor’s workstations information outlets terminate in the IDF on
Data patch panels, Voice 110 hardware, and Fiber Optic Patch Panels. These termination points act as the
cross-connect point between the MDF and the floor that is being served. Large floors are divided into zones,
via an imaginary line (within 90 meters of the respective IDF), with each zone being served by its respective
IDF room/closet. (See figure 1)
Each work area and workstation is served by an information outlet, which provides the jacks for plugging in
telephones, computers, broad band coaxial systems, fax machines, modems, and other devices at the
desktop. The information outlets are served by varying sets of cables consisting of fiber optic and copper
technologies, which originate in the IDF Room. IDF outlets are typically displayed as varying types of
triangles (shaded, half-shaded, etc.) on blueprints. (See figure 2)
A subsystem architectural approach, using the latest technologies, provides a comfortable level of assurance
that the system will support new applications and industry standards as they emerge.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 6 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

FIGURE 1

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 7 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

FIGURE 2

PART 7         PROCEDURES
Designing a cable system for an institution involves various organizations and individuals and requires a
great deal of coordination. Once an institution is designated for wiring, AutoCAD drawings of the floor plans
need to be acquired. AutoCAD is a type of computer aided drafting (CAD) format. These files are plotted and
converted to blueprints that serve as the working drawings for site surveys and engineering purposes. Based
on interviews with the agency's staff and Technical Coordinator will draw triangles on the drawing displaying
the locations that information outlets are to be located. Also, tentative locations for the Communications/Data
rooms/closets will be marked on the drawings. This information will be approved by the institution’s officials
and sent to the engineering team.
The engineers will survey the building—floor plans for new construction—and evaluate the communications
rooms/closets, plan cable routing, and review the information outlet locations. The necessary adjustments
will be made during the site survey, and the engineer will leave the site with the proper approvals from the
agency's management if there are major changes such as room relocations.
The engineering team will then design the cable system for the building. The end product will be submitted to
the agency's Technical Coordinator for comment and/or revision. If no adjustments are necessary, the
blueprints are issued to the contractor for construction.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 8 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

PART 8          HORIZONTAL DISTRIBUTION SYSTEM
The horizontal structured cable plant is the portion of the communications wiring system that extends from
the information outlet to the Communications/Data room/closet.

A.    Horizontal Distribution System General
      1. The horizontal distribution system includes the:
         • Information outlet at the workstation
         • Cables connecting the workstation to the Communications/Data room/closet
         • Intermediate routing and distribution systems
      2. The horizontal distribution system should be configured in a star topology. All communications
         outlets within a work area should be connected to a single Communications/Data room/closet, as
         defined by the zone concept.
      3. This infrastructure must serve all of the Communications requirements of the agency or owner.

      4. Communications applications served by the horizontal system can include:
            •   Voice (e.g., telephones)
            •   Data (e.g., terminal connectivity, modems, etc.)
            •   Local area networks (e.g. Ethernet)
            •   Audio & Video (e.g., CATV, video conferencing and security monitoring)
            •   Graphics & Imaging
      5. When designing a horizontal distribution system, include capacity to satisfy long- term
         requirements as well as initial plans. Ensure that the distribution system has the flexibility to
         accommodate necessary moves, additions, changes, and system growth.
      6. After construction, the horizontal distribution system is typically difficult to access. Therefore the
         time, effort, coordination, and skills required for changes can be extremely costly. In addition,
         access to the horizontal distribution system frequently causes disruption to the user community.

      7. All Horizontal Workstation Communications and broad band coaxial system cabling will be "home-
         run" from the information outlet location to the termination point within the corresponding IDF or
         MDF/IDF room.

      8. Horizontal cable paths will be in a "streets and avenues" manner, typically following main
         walkways.

      9. Horizontal cables are to be fastened onto hangers five feet apart with all cables bundled with tie
         wraps, and are to have a small amount of slack visible.

      10. Cables must be supported by its own support system and not rest on any structures or the hung
          ceiling. Cables are not to be fastened to ducts, pipes, conduits, or any other existing structures.
          Cable bundles should be secured to the slab overhead to avoid any conflict with or EMI from
          flexible electrical conduits, transformers, motors, etc. (Follow the TIA-EIA 569-D.2 Pathways
          requirements)

      11. Some cabling shall run to workstation and other outlets through cavities in the dry wall and
          openings in sheet metal or wooden studs within the dry wall construction. The sheet metal studs
          will not have gaskets for this purpose, so it is the Contractor's responsibility to exercise extreme
          care in snaking cable through these areas, so as to avoid damage to the cable jacketing.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 9 of 69            8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      12. The building's horizontal wiring plan is to be installed on all floors from the information outlet to the
          termination point within the associated IDF Room.

      13. Horizontal cable will be installed onto “J” hooks (similar to B-Line BCH series) or equivalent in the
          ceiling or tops of walls near ceiling. Cables are to be fastened to “J” hooks or equivalent every 5
          feet. The cable contractor is to provide and furnish the “J” hooks.

      14. All station cable (horizontal) and tie cables that run from relay racks to the wall- mounted frames
          are to be plenum-rated.

B.    Horizontal Communications Cable Specification

     1.    For each type of information outlet indicated on the attached drawings, the contractor shall furnish
           all of the following equipment, install it in the correct configuration, and test it.

     2.    All cabling, outlets, and termination patch panels used for the Category 6+ -6A data system must
           be provided by a single manufacturer and shall be certified as part of the 25 year minimum
           warranty- Where the installer chooses to use one (1) manufacturer for cabling and a different
           manufacturer for the outlets and termination patch panels for the Category 6+ -6A data system,
           the two (2) manufacturers must prove to have compliant interconnecting hardware and shall be
           certified as part of the 25 year minimum warranty.

     3.    All Category 6+ and 6a UTP & Fiber cabling is to be handled and terminated in accordance with
           the Manufacturer’s Premises Communications Application and Installation Guide.

     4.    In addition to the above manufacturer’s standards, all applicable ANSI/TIA/EIA-568-C Category
           6 and Fiber Optic Cable standards are to be strictly adhered to.

     5.    The fiber optic cable is to be terminated on both ends with an LC type connector on the patch
           panels.

     6.    The contractor is to use Plenum cable for all station 4-pair copper, coaxial, and 2-strand fiber
           cabling.

     7.    Plan routes to ensure that the proposed route on the plans falls within the EIA/TIA distance
           limitations (90 meters after termination) for horizontal cabling.

     8.    Cables serving information outlets that cannot be routed down wall cavities will be enclosed in
           latching surface-mount raceways, anchored (not with adhesives) to walls. Contractor will provide
           all raceway fittings to allow for level and plumb routes from ceiling to information outlet. Proper fill
           ratios must be observed. Contractor may reference the manufacturer’s catalogs or specifications
           for correct fittings and fill ratios. Contractor must use all accessory fittings required in order to build
           a neat and functional installation. This same method will apply to routing horizontal cables to
           workstation outlets where ceilings are not accessible.

     9.    The RG-6U Plenum Cable and the RG11U Plenum Cable are to be terminated with F type
           connector or connectors. The RG6U Coaxial Station cabling will be terminated onto a rack or wall-
           mounted “F” Connector Patch Panel located in the IDF Room.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 10 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      10. The IDF Room side of the Category 6+ – 6a four-pair cables serving a standard outlet will be
          punched down on individual 110 (Category 6+–6a) modular patch panels, 568B wired. The
          patch panels will be mounted in the relay racks within the IDF rooms.

      11. The contractor is to install a 2U wire management panel between all patch panels and above the
          first panel as well as one below the last panel.

      12. In locations that have wall-mounted racks, the rack should be hinged to swing out to access the
          back of patch panels with associated cable management.

      13. Contractor is to label both the front and the rear of the patch panels. The terminations are to follow
          this sequence: Workstation 001A, 001B, 002A, 002B. It is acceptable to change numbering for
          floor or closet designation.

 C.    Zones
       1. A zone is a contiguous area in which all horizontal wiring is homed to a single communications
          closet within 90 meters from the IDF.

       2. To maintain an orderly, understandable wiring system, it is imperative that the horizontal
          distribution system be structured in zones.

       3. Within a zone, all communications wiring is run to a single communications closet.

       4. Other zones use different Communications/Data rooms/closets. Cross-zone horizontal wiring is
          prohibited. Connections between zones are provided via the vertical distribution system.

PART 9          COMMUNICATIONS/DATA ROOMS/CLOSETS (GENERAL)
The Communications/Data room/closet is a concentration point for communications and LAN services. In
this room, premise wiring and cabling are terminated and cross-connected. In addition, active networking
devices such as switches are placed here. Communications/Data rooms/closets provide a safe area for
housing distribution cabling, premise equipment, and termination fields. These rooms/closets are a focal
point for communications services.
In addition to supporting in-house connectivity, the MDF Communications/Data room/closet often provides a
termination point for the local telephone company. The entrance facility, or demarcation point (de-mark), is
the location where outside communications services, such as copper telephone lines, fiber optic Data
circuits, and CATV, are delivered to the building. Typically, distribution of communications services within the
building originates at this point and is the responsibility of the owner.
Special considerations must be given when providing the building entrance pathways for the copper, fiber
optic, and coaxial cables that service providers will install in to the building de-mark. It is the owner’s
responsibility to provide this pathway into the building. Contact DTI for standards and specifications for
building entrances.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 11 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

The following section details the basic requirements for a Communications/Data room/closet. It may be used
to assist in:
                •   Designing new Communications/Data rooms/closets
                •   Assessing and refining existing Communications/Data rooms/closets to support evolving
                             communications requirements.

 A.    Design Guidelines
       The suggested building practices put forth in this section are recommendations and are subject to field
       conditions and budget constraints. Local building and electrical codes, practices and requirements
       may supersede the guidelines presented in this section.
      1.    Sizing of Communications/Data rooms/closets
            • The Communications/Data room/closet must have enough space to support required
               communications systems, including projected growth.
            • The existing system is likely to be replaced in the future
            • A new system may, require more (or less) space
            • The existing system and a new system may need to coexist during a cut-over
       2. Location of Communications/Data rooms/closets
          • Communications/Data rooms/closets should be situated so as to minimize the length and the
             quantity of cable runs needed for the distribution systems.
          • The maximum horizontal distribution cable distance must be less than 90 meters (295 ft.),
             independent of media type. This distance represents the cable length from the mechanical
             termination of the media in the Communications/Data room/closet to the outlet in the work area.
             This is known as the permanent link.
          • Vertical (backbone) distribution system distance limitations vary and are dependent upon
             media, topology, and facility issues.

       3. Unacceptable locations for Communications/Data rooms/closets:
          • Anywhere water vapor exists, such as boiler rooms, washrooms, or janitor's closets.
          • Spaces with corrosives, explosives, and combustibles, including acid, ammonia, chlorine,
            oxygen, and petroleum vapors.
          • Spaces containing steam pipes, drains, or clean-outs.
          • Areas with high traffic volumes (for security reasons, as well as to minimize the risk of
            inadvertent damage) unless separately enclosed.
          • Areas of high electromagnetic interference (EMI) or radio frequency interference (RFI). Both
            adversely affect system performance and reliability.
 B.    General Room Requirements

       1. Electrical
          • All active Communications, Data and Video systems have specific electrical power
             requirements. Plan electrical service to ensure smooth installation, reliable service, and
             compliance with manufacturers' warranties. Be sure to consider equipment manufacturer's
             specifications, National Electric Code (NEC) requirements, State and local codes, ordinances,
             and requirements.

            • Electrical devices capable of causing line transients, such as fans, pencil sharpeners, radios,
              calculators, and lights, must be separated electrically from the Communications equipment. To

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 12 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                accomplish this, all Communications and Data equipment requires separate electrically isolated
                ground circuits and/or building grounding. The outlets on these circuits should be labeled
                and/or color coded. Frequently, orange-colored wall outlets are used to identify power sources
                used for computing and communications equipment. Utility outlets are also needed in the
                Communications/Data room/closet for tools, test sets, and other equipment.
            • Each Communications/Data room/closet shall have one 110V, 15 Amp electrical convenience
              outlet and one 110V, 20 Amp dedicated-circuit isolated-ground electrical outlet for the
              electronic equipment. This is a minimum requirement based on the typical current draw of the
              networking equipment to be placed. The ground for the equipment outlet should be an isolated
              ground where possible to avoid line transients. The 110V 20 Amp dedicated circuit isolated
              ground electrical outlet(s) should be mounted in convenient location to facilitate the use of the
              shortest equipment power cords. The recommended location is at the top of the rack or on the
              ladder tray.

            • All electrical isolated ground outlets serving Communications and Data equipment must be
              attached to non-switched circuits to prevent inadvertent equipment shutdown. It is also
              recommended that they be on a UPS and/or generator if available.

       2. Grounding
          • Most Communications and Data equipment requires bounding and grounding of equipment
            cabinets. Do not use plumbing or conduit (EMT) fixtures as a ground source. Grounding shall
            meet the NEC and EIA/TIA requirements and practices except where other authorities or codes
            impose more stringent requirements or practices. (Refer to NEC Chapter 2 article 250 and
            Chapter 8 Communications Systems, TIA/EIA Standard J-STD-607-D and Motorola R56
            Standards and Guideline for Communication site).

            • In addition to protecting personnel and equipment from hazardous voltages, the grounding
              system may reduce the effect of electromagnetic interference (EMI) throughout the structured
              cable plant. Improper grounding can result in induced currents that disrupt Communications
              circuits.

            • Ensure that the installation conforms with applicable regulations and practices

            • Ensure that each Communications/Data room/closet has an appropriate ground buss bar

            • Ensure that grounding is available for cross-connect frames, patch panel racks, Telephone and
              Data equipment, as well as testing and maintenance equipment

       3. Space
          • A distance of three feet is the preferred clearance from the front, back, and side of a relay rack.

            •   If there are space constraints, it is acceptable to provide a minimum of two feet of clearance on
                one rack side for access and a minimum of two feet of front and back clearance for cross-
                connect fields, patch panels, etc. If possible, locate sleeves, cores, slots, and/or conduits
                together in one area to maximize usable wall space.

       4. Rooms/Closets Sizing

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 13 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            •   Determine the number of relay racks required for the termination of patch panels and electronic
                equipment. Assume that free-standing relay racks will be installed and provide three feet of
                space on all sides of each.

            •   Determine the amount of wall space that will be required for the installation of termination
                equipment. A minimum of four feet should be used as a criterion.

            • Determine if the plywood backboard will be furred-out. This equals approximately 4” of space
              taken from the room.

            •   Take into account the door swing if the door opens into the room. Ideally the door should open
                out from the room.

            •   Determine how much space any sleeves, conduits, or other equipment require.

            •   Determine the size of the room by constructing a diagram, to sale, of all of these components,
                taking into account all the walkways and door swings.

            • If a very small number of information outlets are being installed, the minimum size a closet can
              be is 4’ wide and 3’ deep. This assumes a 4’ X 8’X 3/4” plywood backboard, one wall-mounted
              relay rack that has a fiber optic patch panel, copper patch panels, coax patch panel, LAN hubs
              and ground buss bar. It is recommended to install plywood on all walls, from the floor to the
              ceiling.

       5. Structural Walls
          • Extend from the floor to the deck above (fire wall)

           •    Be securely fastened to the floor and the deck above

           •    Conform to national and local construction guidelines

       6. Wall Linings
          • Each Communications/Data room/closet will contain a minimum of one furred-out or flush sheet
            of plywood (4’ X 8’) mounted on the wall.

           •    It is recommended to install plywood floor to ceiling on all walls.

           •    Securely fasten the plywood to wall framing members to ensure that it can support any
                attached equipment.

           • The plywood is to be 3/4”, A/C grade, and fire-retardant.

           •    All plywood backboards are to be mounted smooth side out and painted white at time of
                installation, prior to installation of equipment onto the plywood.

       7. Floor Finish
          • Keep dust to a minimum in Communications/Data rooms/closets.

           •    Anti-static Asphalt Tile, Linoleum Tile, or Sealed Concrete is acceptable floor finishes.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 14 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       8. Ceilings and Doors
          • Dropped ceiling height should be at least nine feet from the finished floor to provide adequate
            space for equipment cabinets and suspended cable trays. Some equipment may require
            additional height, depending on the manufacturer's specifications. Avoid installing false ceilings
            in small closets.

           •    Overhead ceiling vents should be centrally located to maximize air distribution and
                maintenance access. Avoid placing overhead ceiling vents directly over suspended racks and
                equipment cabinets.

           •    All ceiling vents should have diffusers (vent manifolds) securely installed.

           •    Design doorways with minimum measurements of 36 inches wide. Hinge the doors to open
                outward.

           •    All Communications/Data rooms/closets should have door locks and a minimum number of
                windows, if any. Closets should be kept locked. Provide keys to select personnel who are on-
                site continuously.

       9. Lighting
          • Within ceilings, position light fixtures at least eight feet above the finished floor.

           •    Indirect (reflected) lighting is not recommended.

           •    If possible, minimize heat and glare by using fluorescent light fixtures with protective covers
                instead of incandescent fixtures.

           •    Do not place light fixtures where the light may be blocked or filtered.

           •    Typically, light fixtures should not be directly above or within 12 inches of cabling, equipment
                cabinets, termination frames or other free-standing equipment.

           •    Install light fixtures on power circuits separate from those used for communications equipment.

       10. Communication/Data Room/Closet Environment
           • Manufacturers of most hardware recommend a room environment consisting of a temperature
             between 72–75° Fahrenheit and a 45–50% humidity level.

           • It is recommended that temperature swings do not exceed 10° and humidity remain within a
             ±5% range.

 C.    MDF Requirements
       An MDF Room is a specialized communications closet that may house major communications
       systems, such as a communications processor, switch and routing equipment. The MDF Room is
       generally considered to be distinct from an IDF Room because of the complexity of the equipment it
       contains.
       A typical Main Distribution Frame (MDF) Room is composed of a wall-mounted plywood backboard
       and relay racks designed for mounting termination equipment and electronics (see Figure 3). Most

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 15 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       MDFs within the building cabling system also serve as an IDF. This is accomplished by providing
       separate relay racks for each and delineating the wall-mounted frame’s 110 blocks for Station cabling
       (see Figure 4 and Figure 5).

       FIGURE 3

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 16 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       FIGURE 4

       FIGURE 5

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 17 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       1. MDF/IDF Room Equipment Enclosures
          • Any MDF/IDF Rooms located in rooms that are shared with space used for any other purpose
            should have wire mesh cages or sheetrock walls around the Communications equipment, or
            the equipment should be installed in a lockable cabinet.

       2. Environment
          • Environmental control equipment must function properly at all times. If the building system
            cannot ensure continuous operation on weekends and holidays, provision of stand-alone
            control units for the MDF/room and IDF room/closet is necessary.

            • Within the MDF room and IDF room/closet, temperature should not vary by more than 5°F, and
              humidity must not vary by more than 10%. Measure temperature and humidity five feet above
              the finished floor in the center of the communications room/closet.

       3. Local Exchange Carrier (LEC)
          • Placement of Communications equipment may be influenced by vendors and service providers.
            For instance, the LEC (local phone company) may decide to terminate the Central Office (CO)
            service directly into the equipment space provided or request termination space other than that
            offered by the customer. If they request termination at a point other than that requested by the
            customer, the LEC should provide reasonable explanation.

           •    The LEC, CATV, and most service providers will require a conduit entrance in to the building to
                provide their service. The minimum requirements are two (2) four- inch conduits for the LEC
                and one (1) four-inch conduit for each other service provider, unless they specify otherwise in
                writing.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 18 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           • It is critical that the high speed Data line, TLS – Canoga Perkins and Fiber Optics be located in
             the MDF room. This will ensure security and simplify troubleshooting.

           •    The LEC may also need space for distribution systems terminations (either horizontal or
                vertical) and patch cable terminations.

       4. Other Equipment Vendors
          • As with the local phone company (LEC), it is vital to consult with all Communications equipment
            manufacturers for their specific space and operational requirements, such as the telephone
            system and Data LAN/WAN equipment provider.

       5. Relay Racks
          • Each MDF will contain a minimum of one 19”W X 7’H Relay Rack onto which the fiber
            optic/copper patch panels and Data electronics are mounted.

           • The relay racks should have a minimum of 42 rack units of mounting space on standard 19”
             wide rails.

           •    In some cases the relay racks are wall-mounted and in others they are free-standing two- or
                four-post racks. It must be determined which type of rack is required, based on field conditions,
                equipment manufacturer's requirements, and space allocated.

           •    All racks are to be grounded and bolted to each other as well as to the slab or wall.

           •    The rack should have vertical and horizontal cable management to accommodate routing of
                patch cords.

           • There should be a minimum distance of 48” to be maintained from three sides of the rack.

           •    The relay rack specifications and associated components should meet the requirements of the
                equipment that will be installed in it.

           • It should be at a minimum 84” tall with 6” rails, with 19” equipment mounting space and vertical
             and horizontal wire management.

           •    Manufactured by Hubbell of Eaton/B-Line, Panduit or approved equivalent

       6. Wall-mounted Relay Racks
          • The rack is to be securely fastened to the wall behind it and attached to the ladder rack above.

           •    The rack should be sized to accommodate the equipment to be installed in it, with vertical and
                horizontal jumper management.

           •    Manufactured by Hubbell of Eaton/B-Line, Panduit or approved equivalent

       7. Communications Cabinets
          • All communications cabinets are to be grounded to the grounding and bounding system and
            bolted to each other and to the slab.

           •    Each communications cabinet is to be installed with its side to an adjacent wall. Three feet of
                clearance around the cabinet is recommended and the cabinets must have front and rear
These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 19 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                 access.

       8. Data Equipment Cabinets
          • Data equipment cabinets should conform to the State Data Center Standard as follows:
                Cabinet size                30”Wx44.30’Dx79.’H
                Rack units                  42 rack units for equipment mounting
                Mounting rails              two pair 19" adjustable depth universal mounting
                Mesh steel doors            single front and split rear with locking handles
                Vertical cable              trough, rings or VeLCro tie downs or combination of, mountable
                management                  left or right side
                PDU mounting                space to mount two horizontal PDU closest to equipment
                                            mountable top or bottom, together or separate
                PDU Metering                Managed or Metered PDU’s to display Amperage, Voltage

                Side panels                 removable, solid, both sides
                Top                         solid with cabling access opening capabilities
                Bottom if required          solid with cabling access opening capabilities

            •    Cabinet should have grounding, bounding and anti-tip capabilities that can be added when
                 required.
            •    Approved cabinet Manufacturer: Eaton Wrightline RS Series or approved equal

       9. Cable Trays
          • Between the relay rack and the wall-mounted frame, a 12” cable tray (center-rail systems are
            not permitted), with a 4" load depth and 6" rung spacing is to be installed suspended from a
            ceiling support structure, mounted to the relay rack and the wall.

           •     Do not attach any cable tray to a suspended ceiling grid.

           •     An open wire basket cable tray system is acceptable for cable support.

           •     Approved manufacturer: Cooper B-Line part # FT4X12X10 or approved equal

       10. MDF Room Electrical Requirements
           • Each room shall have a minimum of one duplex dedicated 20 Amp isolated ground circuit and
             one shared 20 Amp circuit.

           •     Larger equipment loads may require additional circuits.

 D.    IDF Room Requirements
       Each IDF Rooms within a building supports all connections in single, contiguous area (zones). Cross-
       zone wiring is not to be installed from user workstations. Connections between zones are made
       through backbone wiring systems, which link the IDF Rooms to the MDF. A typical Intermediate
       Distribution Frame (IDF) Room is composed of a wall-mounted plywood backboard and relay racks
       designed for mounting termination equipment and electronics.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 20 of 69            8/9/2016               11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       FIGURE 6

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 21 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       FIGURE 7

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 22 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       FIGURE 8

      1.   Number of IDF Communications/Data rooms/closets within a building
           • Each floor should have at least one IDF Communications/Data room/closet.

           •    Wiring workstations to IDF Communications/Data rooms/closets on different floors is not a
                preferred practice but can be done if no alternative exists.

           •    If possible, IDF Telecommunication Closets should be positioned toward the center of the

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 23 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                building (usually the core area) and stacked vertically, when possible, in multi-story buildings.

      2.   Plywood Backboard
           • Each IDF Room will contain a minimum of one 4’ X 8’ sheet of plywood flush- mounted on the
              wall.

           •    Securely fasten the plywood to wall-framing members to ensure that it can support attached
                equipment.

           • The plywood is to be 3/4”, A/C grade and fire retardant.

           •    All plywood backboards are to be mounted smooth side out and painted with white fire
                retardant paint at time of installation and prior to installation of equipment onto the plywood.

      3.    IDF Room Equipment Enclosures
            • Any IDF Rooms located in rooms that are share space used for any other purpose should have
               wire mesh cages or sheetrock walls around the Communications equipment.
      4.   Relay Racks
           • Each MDF will contain a minimum of one 19”W X 7’H Relay Rack onto which the fiber
             optic/copper patch panels and Data electronics are mounted.

           • The relay racks should have a minimum of 42 rack units of mounting space on standard 19”
             wide rails.

           •    In some cases the relay racks are wall-mounted and in others they are free-standing two- or
                four-post racks. It must be determined which type of rack is required, based on field conditions,
                equipment manufacturer's requirements, and space allocated.

           •    All racks are to be grounded and bolted to each other as well as to the slab or wall.

           •    The rack should have vertical and horizontal cable management to accommodate routing of
                patch cords.

           •    The relay rack specifications and associated components should meet the requirements of the
                equipment that will be installed in it.

           • It should be at a minimum 84” tall with 6” rails, with 19” equipment mounting space and vertical
             and horizontal wire management.

           •    Manufactured by Hubbell of Eaton/B-Line, Panduit or approved equivalent

      5.   Wall-Mounted Relay Racks
           • The rack is to be securely fastened to the wall behind the rack and attached to the ladder rack
             above.

           •    The rack should be sized to accommodate the equipment to be installed in it, with vertical and
                horizontal jumper management.

           •    Manufactured by Hubbell of Eaton/B-Line, Panduit or approved equivalent

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 24 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      6.    Communications Cabinets

            •   All communications cabinets are to be grounded to the grounding and bounding system, bolted
                to each other and to the slab.

            •    Each communications cabinet is to be installed with its side to an adjacent wall.

            •   Three feet of clearance around the cabinet is recommended, and the cabinets must have
                front and rear access.

       7.   Cable Trays
            • Between the relay rack and the wall-mounted frame, a 12” cable tray (no center rail
              systems), with a 4" load depth and 6" rung spacing is to be installed suspended from a
              ceiling support structure, mounted to the relay rack and the wall.

            •   Do not attach cable trays to the suspended ceiling grid.

            •   An open wire basket cable tray system is acceptable for cable support.

            •   Manufactured by Hubbell of Eaton/B-Line, Panduit or approved equivalent

       8.   IDF Room Electrical Requirements
            • Each Communications/Data room/closet shall have one 110V, 15 Amp electrical
               convenience outlet and one 110V, 20 Amp dedicated–circuit, isolated-ground electrical outlet
               for the electronic equipment.

            •   This is a minimum requirement based on the typical current draw of the networking
                equipment to be placed.

            •   The ground for the equipment outlet should be isolated where possible to avoid line transients.

            •   The 110V 20 Amp dedicated-circuit, isolated-ground electrical outlets should be mounted
                in convenient location to facilitate the use of the shortest equipment power cords.

            •   The recommended location is at the top of the rack or on the ladder tray.

            •   All electrical isolated ground outlets serving Communications and Data equipment must
                be attached to non-switched circuits to prevent inadvertent equipment shutdown.

            •   It is also recommended that they be on a UPS and/or generator if available.

PART 10          MDF & IDF PRODUCT SPECIFICATIONS
A.    Category 6 Patch Panels
      In new construction projects, the default cabling infrastructure shall be Category 6 unless specified
      otherwise.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 25 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

       1.    Category 6 Patch Panel Requirements
             • Category 6 patch panels shall be standard 8-position, RJ-45 style, un-keyed, in 48-
               port configurations.

             • Panel frames shall be 14-gage steel with rolled edges top and bottom for proper stiffness.

            • Panel design shall incorporate plastic push-fasteners to permit hands-free positioning onto
              standard EIA-310-D 19” mounting rails.

            • Panels shall accommodate a minimum of 24 ports for each rack mount unit (1 RMU = 1.75 in.).

            • Panels shall be designed for 4-pair, 100 ohm balanced unshielded twisted pair (UTP) cable.

            • Panels shall terminate 26-22 AWG solid conductors, with maximum insulation diameter of
              0.050 in.

            • Panels shall have attached wiring instruction labels to permit either T568A or T568B wiring
              configurations.

            • Panels shall have individual port identification numbers on the front and rear of the panel.

            • Panel adapter modules shall be 110-style termination with tin lead solder plated IDC contacts.

            • Printed circuit boards shall be fully enclosed front and rear for physical protection.

            • Panel contacts shall withstand a minimum of 2000 mating cycles with an FCC 8-position RJ-45
              plug, without degradation of electrical or mechanical performance.

            • Panel contacts shall be constructed of Beryllium copper for maximum spring force and
              durability.

            • Contact plating shall be a minimum of 50 micro-inches of hard gold in the contact area over 50
              micro-inch of nickel.

            • Panel termination method shall follow the industry standard 110 IDC punch-down, using a
              standard 110 impact termination tool.

            • Panels shall be compatible with a 4-pair multi-punch impact termination tool designed
              specifically for the purpose. Bending or other damage to the panel using a multi-pair punch tool
              shall not occur.

            • IDC contact termination towers shall have tapered pair-splitting features to aid wire insertion
              and minimize pair un-twist.

            • IDC contacts shall be Phosphor Bronze with 100 micro-inch tin lead 60/40 plating over nickel.

            • Panels shall not require special cords or special installation requirements.

            • Panel ports shall accept optional hinged dust covers and port identification icon buttons.

            • Space above the adapter ports shall be available for additional labeling per ANSI/TIA/EIA-606-
              A.

            • Category 6 panels shall be backward compatible with existing Category 3, 5, and 5e cabling
              systems for fit, form, and function.
These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 26 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Panels shall accept a clip-on rear cable management support bar to provide cable strain relief.

      2.    Category 6 Patch Panel Performance Requirements
            • All transmission performance parameters shall be independently verified by a UL or ETL third
              party testing organization.

            • Category 6 panels shall meet or exceed Category 6 transmission requirements for connecting
              hardware, as specified in ANSI/TIA/EIA-568-C.2 Transmission Performance Specifications for
              4-Pair 100 ohm Category 6 Cabling.

            • The manufacturer shall provide Category 6 component compliance certificates from third party
              testing organizations upon request.

            • Panels shall be UL LISTED 1863 and CSA certified.

            • Panels shall support 4PPOE IEEE 802.3bt Power specification to 1.5 times the rated current
              limits with no degradation of performance or materials.

            • Panel contacts shall withstand a minimum of 2000 mating cycles with an FCC 8-position RJ-45
              plug, without degradation of electrical or mechanical performance.

            • Panels shall be third party verified, error free Gigabit Ethernet performance to IEEE 802.3
              standard.

            • Category 6 panels shall meet the current draft 10 Gb/s performance requirements of IEEE
              802.3an and TSB-155, for a maximum 55-meter channel length. Conditions of requirement No.
              10 above apply.

      3.    Acceptable Manufacturers:

            • Hubbell Premise Wiring.
              The Hubbell products listed in the table below comply with all requirements specified in this
              document

             HUBBELL                       Description
             CATALOG NUMBER
             P6E48U                        NEXTSPEED® Category 6 Patch Panel, 48-Ports
             PCBLMGT                       Rear Cable Management Bar

            • Or approved equal of: Ortronics, Panduit, Systimax.
      4.    Category 6 Patch Panel Installation Requirements
            • Horizontal and backbone cabling of the proper category shall be fully deployed into the TR, TE,
              or ER according to applicable codes and standards.

            • Cable slack, service loops, bend radii, and pathway fill ratio shall comply with applicable codes
              and standards.

            • Racks, cabinets, enclosures, and metallic cable pathways shall be bonded to an approved
              ground according to ANSI-J-STD-607-A.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 27 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Cable ends for termination shall be clean and free from crush marks, cuts, or kinks left from
              pulling operations.

            • Properly mount patch panels into the designated rack, cabinet, or bracket locations with the
              #12-24 screws provided.

            • Terminate cables into the patch panel according to manufacturer’s instructions.

            • To maximize transmission performance, maintain wiring pair twists as close as possible to the
              point of termination.

            • The length of wiring pair un-twist in each termination shall be less than 0.5 inches (13 mm).

            • Horizontal or backbone cables extending from the panel terminations shall maintain a minimum
              bend radius of at least 4 times the cable diameter.

            • Cable terminations shall have no tensile or bending strain on panel IDC contacts in each
              installed location.

            • Panels shall be properly labeled on front and back with the cable number and port connections
              for each port.

B.    Fiber Enclosures, Adapter Plates, Connectors

      1.    Fiber Adapter Enclosure Requirements
            • Enclosure design shall be a modular, rack-mounted, powder coated formed cold rolled steel
               enclosure with a removable front cover, rear panel, top panel, and slide-out inner tray.

            • Each basic unit delivered shall consist of: (1) enclosure assembly, (2) mounting brackets, (6)
              cable ties, (5) snap-in cable clips (4) #12-24 mounting screws, (1) adhesive grid label, (4)
              adhesive cable clips, (2) Velcro cable ties, (3) label holders, and (1) splice tray stud, wing nut,
              and spacer.

            • Material shall be as follows:

                  a. Enclosure, panels and tray: 16 gauge cold rolled steel (CRS)

                  b. Mounting brackets: 14 gage CRS

                  c.   Front cover: Acrylic (Plexiglas)

            • Basic dimensions of the enclosures shall be approximately 17” wide by 12” deep.

            • Enclosures shall be available in heights of 3.5” (2 RMU), 5.25” (3 RMU), and 7” (4 RMU)
              versions.

            • Finish shall be black durable powder coat on all surfaces.

            • Front door shall be Lexan plastic, hinged at the bottom, with a cap-plugged hole to accept an
              optional lock. Front door shall also be removable in the fully open position by sliding left off the
              mounting pins.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 28 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Front door shall be secured in the closed position with magnetic quick-release latches.

            • Top cover shall be removable in the forward direction, without fasteners, to provide access to
              the connector field. Top panel shall also have knockouts for backbone cable entry.

            • Rear panel shall be removable without fasteners.

            • Enclosure shall be equipped with panel-mounting brackets assembled for 19” rack mounting,
              compliant to ANSI/EIA-310-D.

            • Panel mounting brackets shall be configurable to either 19” or 23” racks.

            • Enclosure chassis shall have two mounting bracket locations for either flush mount or center
              mount on the rack.

            • Rear of enclosure shall have two knockouts, top and bottom, for backbone cable entry and
              internal routing.

            • Front of enclosure chassis shall have side cutouts for patch cord entry into, and exit from the
              enclosure.

            • Inner tray shall slide out in the forward direction by releasing the lever-action quick-release
              latches. Tabs in the chassis shall engage with slots in the inner tray in the outward position to
              prevent tray from falling out.

            • Inner tray shall have rear-located knockouts to match rear chassis knockouts.

            • Inner tray panel mounting posts shall accept modular adapter panels, in high- or low-density
              versions. Adapter panels shall be available in singlemode.

            • Splice tray mounting boss shall also accept a stud for mounting blown fiber adapter brackets.

            • Inner tray shall have clips for cable ties, and holes to accept snap-in cable clips, front and rear,
              for complete cable management of patch cords and distribution cable strands.

            • Inner tray shall have rear cable tie-down features to accept various diameter backbone cables
              entering the enclosure.

      2.    Fiber Adapter Panels Requirements
            • Fiber adapter panels shall be a modular, quick-fastening steel plate, powder coated to match
               the enclosure finish.

            • Fiber adapter panels shall have pre-installed LC fiber adapters, available in low- or high-density
              multi-mode or single-mode applications.

            • Each individually bagged unit delivered shall consist of: (1) fully assembled adapter panel, with
              push-pull fasteners pre-installed.

            • Adapter panels shall be constructed of 16 gauge cold rolled steel.

            • Finish shall be black durable powder coat on all surfaces.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 29 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Basic dimensions of the FSP panels shall be 5.10” length by 1.10” wide.

            • Panels shall have two pre-installed, push-pull type quick-release fasteners for quick snap-in
              installation. Push-pull fasteners shall have an industry standard center distance of 4.65”.

            • Panels shall be suitable for mounting either vertically or horizontally.

            • Panels shall be available in with LC adapters with precision ceramic alignment sleeves.

            • All fiber adapters installed in FSP panels shall have dust caps installed.

            •   Panels shall be available in low-density and high-density adapter patterns.

      3.    Fiber Connector Requirements
            • Please note OM4 minimum standard

                           i. Internal Building Installation

                                     1. Each IDF will connect back to the MDF with 12 strands of OM4 SM fiber.

                          ii. External Building/Campus Installation

                                   1. Buildings less than 1640ft/500m shall use a mix of OM4/Single Mode fiber.

                                   2. Installation distances GREATER than 1640ft/500m require use of Single
                                       Mode fiber exclusively.

            • Connector basic design shall be a factory pre-polished LC optical fiber connector with a
              zirconium ceramic ferrule. Integral with the connector body is a wedge-activated fiber clamping
              mechanism to secure the inserted fiber into a mechanical splice with the factory installed
              cleaved fiber stub. Index-matching gel is supplied factory-injected into the cleaved fiber stub
              splice to optimize transmission performance. Connector attachment is achieved without tools,
              by inserting a field-cleaved optical fiber and then extracting the disposable clamp wedges from
              the connector body.

            • Each basic connector unit delivered shall consist of: (1) connector body with disposable clamp
              wedge, (1) strain relief boot, and (1) plastic dust cap.

            • Connector termination method shall utilize an industry standard multi-layer strip tool and bare
              fiber cleave tool as the only field tools required.

            • LC connectors shall have features to enable field verification using a Visual Fault Locator (VFL)
              during termination.

            • Connector materials shall be designed with thermal stability to comply with environmental
              requirements of ANSI/TIA/EIA-568-B.3 and TeLCordia GR-1081-CORE.

            • Singlemode pre-polished fiber connector materials shall be as follows:

                  a. Ferrule: zirconium ceramic

                  b. LC inner body: thermally stable injection molded thermoplastic

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 30 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                  c.   Dust Cap: nylon or PVC

                  d. Strain relief boot: UL94-V0 molded PVC

            • Pre-polished LC connectors shall require no field polishing.

            • colors for specific applications, as designated below:

            • Pre-polished OM4 LC connectors shall require no adhesives for termination.

            • LC connector internal fiber clamping mechanism shall firmly secure both the inserted glass
              fiber and the 900 micron buffer layer of the inserted fiber for maximum strain relief.

            • All standard mating and interface dimensions for LC connectors shall comply with
              ANSI/TIA/EIA-604-10 (FOCIS 10).

            • Ferrule outside diameter for LC singlemode connectors shall be 1.2483mm to 1.2497mm.

            • LC ferrule tip shall have a PC spherical radius of approximately 7.0 mm radius for
              singlemode versions.

            • Delivered connectors shall be individually bagged with the dust cap installed to protect from
              contamination.

            • Delivered connectors shall have the disposable clamp activation wedge element pre-installed
              onto the connector body.

            • Connector design and termination technique shall be independent of cable type or
              manufacturer, and shall be compatible for either 900 micron buffer or 250 micron buffer
              distribution cables.

            • LC connector strain relief boot shall be a TeLCordia style slotted design for maximum
              flexural strain relief.

            • Strain relief boot shall be yellow for singlemode.

            • LC connectors shall be available individually bagged in packs of 12.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 31 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Pre-polished LC fiber connectors, when properly installed onto qualified cable, shall meet the
              10 Gb/s Ethernet performance requirements of IEEE802.3.

            • Pre-polished LC fiber connectors, properly installed onto qualified cable, shall exceed the
              mechanical and environmental performance requirements of ANSI/TIA/EIA-568-C.3, Annex ‘A’.

            • Pre-polished LC fiber connectors, properly installed onto qualified cable, shall exceed the
              mechanical and environmental performance requirements of TeLCordia GR-1081-CORE.

            • Qualification test data shall be available from the manufacturer upon request.

      4.    Acceptable Manufacturers:

            • Hubbell Premise Wiring.
              The Hubbell products listed in the table below comply with all requirements specified in this
              document

             HUBBELL                       Description
             CATALOG NUMBER
             FCR2U6SP                      Fiber Enclosure - 2U Rack Mount Fiber Enclosure, Accepts 6
                                           Adapter Panels
             FCR2U9SP                      Fiber Enclosure - 2U Rack Mount Fiber Enclosure, Accepts 9
                                           Adapter Panels
             FCR3U12SP                     Fiber Enclosure - 3U Rack Mount Fiber Enclosure, Accepts 12
                                           Adapter Panels
             FCR4U15SP                     Fiber Enclosure - 4U Rack Mount Fiber Enclosure, Accepts 15
                                           Adapter Panels

             FSPLCDM6AQ                    Fiber Adapter Panel - 6 LC Duplex, Aqua for MM – Phosphor
                                           Bronze Sleeves
             FSPLCDS6                      Fiber Adapter Panel - 6 LC Duplex, Blue for SM – Zirconia
                                           Ceramic Sleeves
             FSPLCQS3                      Fiber Adapter Panel - 6 LC Quad Blue for SM – Zirconia Ceramic
                                           Sleeves

                FCLC900K50GM12             Fiber Connector - LC, MM, 50/125um, OM4 – Aqua, Box of 12

             FCLC900KSM12                  Fiber Connector - LC, SM, 9/125 UPC – Blue Box of 12

            • Or approved equal of: Ortronics, Panduit, Systimax.
      5.    Fiber Installation Requirements
            • For FCR-series enclosures, remove top and rear covers, and front door.

            • Punch out the desired knockouts for cable entry.

            • Using proper method, pull cables into cabinet through the desired knockout entry location.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 32 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Strip the outer sheath and sub sheaths of the fiber cable to provide at least (2) meters service
              loop of the individual buffered fiber strands.

            • Anchor the outer cable sheath into the rear channel of the inner tray using the cable ties
              provided. Note: in FCR-series enclosures, leave enough slack in the main cable to allow free
              motion of the inner tray fully outward. Remove cable entry knockouts as required.

            • Installed copper and fiber cabling shall be properly strain relieved. Cable service coil, bend
              radius, and pathway fill ratio shall comply with applicable codes and standards.

            • Use the plastic adhesive-backed clips provided to form the fiber strands into a large service coil
              on the surface of the inner tray. For FCR-series enclosures, be sure the inner tray has full
              mobility in and out, with no cable kinks or snags.

            • Close inner tray and front cover, and lock the quick-release fasteners.

            • Install LC fiber adapter panels by firmly using push fasteners to lock in place.

            • Leave dust caps installed in the fiber adapter plates until connector termination is performed.

            • Follow manufacturer’s termination instructions for pre-polished connectors as specified

            • Uncoil the 900-micron buffered strands of cable from the service loop and set-up for
              termination.

            • Un-package the connector, and leave dust cap installed. Firmly press downward on the
              connector wedge tab to fully seat clamp wedges.

            • Slide the strain relief boot onto the fiber strand before stripping.

            • Using a fiber strip tool, strip buffered fiber completely to approx. 1.0” of exposed glass fiber.

            • CAUTION: Do not nick or Scrape the glass fiber with the strip tool.

            • Wipe the glass fiber firmly with an alcohol wipe. Always use 99.9% pure reagent grade alcohol
              for fiber cleaning.

            • Mark the 900 micron buffer layer from the strip-off point per instructions.

            • Insert the fiber into the cleave tool and cleave the fiber to the specified length from the end of
              the 900 micron buffer layer. Always keep the cleave tool clean.

            • CAUTION: Always dispose of glass fiber waste in an approved container.

            • Gently insert the cleaved fiber into the connector body. Rotate connector slightly during
              insertion to fully seat the fiber into the internal splice.

            • Hold the seated fiber in place using slight force to form a bow in the fiber.

            • Υ CAUTION: Do not allow the installed fiber to slip backward.

            • While holding the fiber seated, squeeze the wedge holder device to activate the clamp, and

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 33 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                  then slip the wedge holder off the connector body. Dispose the wedge holder.

               • Remove the connector dust cap and inspect the ferrule tip. A 400X microscope is
                 recommended. View of the polished fiber should be a smooth round circle with no scratches,
                 pits, cracks or chips. Use a lint-free wipe to clean off any contamination.

               • CAUTION: Do not view ends of live fibers, with or without a microscope.

               • Plug the connector into the proper adapter panel and proceed with the next connector. Leave
                 dust cap installed if the connector is not mated.

C.    Racks, Horizontal & Vertical Managers

      1. Equipment Racks Requirements
         • Racks shall be a structural aluminum construction, having two 6-inch deep rails.

           •     Racks shall feature universal side mounting hole pattern for vertical cable managers.

           •     Racks shall feature a weight load capacity of 1,000 lbs. when properly secured to the floor.

           •     Each basic rack delivered shall consist of: (2) vertical rails, (2) base angles, (1) assembly
                 hardware kit, (2) top angles, and (20) #12-24 dog point machine screws for panel mounting.

           •     Racks shall be available in either for 19-inch standard rack configurations.

           •     Tapped holes in the front and rear vertical rails for mounting of panels shall be #12-24 thread
                 size. Powder coat shall not interfere with thread fit.

           •     Standard rack heights of 8 ft (96 in)

           •     Racks with heights of 8 ft shall have a capacity of 51 rack mount units

           •     Rack base angles shall be pre-drilled for floor mounting, and for assembly to vertical rails.

      2. Horizontal Managers Requirements
         • Horizontal Managers shall be 19”W, 3.5”H

           •     Horizontal managers shall be 16ga. Cold rolled steel construction with (6) pass thru holes, and
                 (7) Front mounted 3.5” steel rod D-Rings.

           •     Horizontal managers shall have hinged Aluminum front cover to conceal patch cords.

      3. Vertical Managers Requirements
         • Vertical cable managers shall be 14”D, 10”W

           •     Vertical cable managers shall feature a steel rod construction for increased air flow.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 34 of 69            8/9/2016               11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           •        Vertical cable managers shall feature a solid aluminum door that is designed to open left or
                    right and swing out of way for cable management.

           •        Vertical cable managers shall feature power strip mounting brackets on rear of manager.

           •        Vertical cable manager shall accept and include (16) 3" black cable management spools.

      4. Acceptable Manufacturers:

               • Hubbell Premise Wiring.
                 The Hubbell products listed in the table below comply with all requirements specified in this
                 document
               • Cooper B-Line.
                 The Cooper B-Line products listed in the table below comply with all requirements specified in
                 this document

                   HUBBELL                 Description
                   CATALOG NUMBER
                   HPW84RR19D              84”H, 6”D Equipment Rack
                   HM24C                   2U Horizontal Manager w/ 3.5” Front rings and cover
                   VM1013                  Vertical Cable Manager, 14”D, 10”W, with door & cable spools

                   B-Line CATALOG          Description
                   NUMBER
                   SB55608419U6            84”H, 6”D Equipment Rack
                   SB87019S2FB             2U Horizontal Manager w/ 3.5” Front rings and cover
                   SB860810S084            Vertical Cable Manager, 14”D, 10”W, with door & cable spools

               •    Or approved equal of: Ortronics, Systimax,
               •
D.    Category 5e-110 Termination Blocks

      1.       110 Termination Block Requirements
               • Category 5e-110 wiring blocks shall be available in 50-pair, 100-pair and 300-pair capacities,
                  with or without detachable standoff legs.

               • Wiring blocks shall be available as kits that include wiring blocks, label strips, and the
                 appropriate quantity of connecting blocks for termination to full capacity.

               • Connecting blocks shall accommodate a 5-pair punch-down tool designed specifically for the
                 purpose of Category 5e termination.

               • Wiring blocks and connecting blocks shall be constructed of UL94-V0 rated high-impact flame-
                 retardant polycarbonate blend thermoplastic.

               • Wiring blocks shall accept 26-22 AWG solid or stranded conductors

               • Wiring blocks shall accept conductor insulation diameters of .050 in to .070 in maximum.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 35 of 69              8/9/2016             11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Wiring blocks and connecting blocks shall have a temperature rating of 14 °F to 140°F with up
              to 95% non-condensing humidity.

            • Wiring blocks shall have through-openings to permit rear cable entry and direct routing to each
              point of termination.

            • Connecting blocks shall connect to the wiring block with a locking force of 35 Lb minimum.

            • Connecting blocks shall withstand a minimum of 200 re-terminations without degradation to
              electrical or mechanical performance.

            • IDC contact termination towers on the connecting blocks shall have tapered pair-splitting
              features to aid wire insertion and minimize pair un-twist. IDC towers shall also have high-
              definition color-coding.

      2.    110 Termination Block Performance Requirements
            • A UL or ETL third party testing organization shall independently verify all Category 5e
               transmission performance parameters.

            • Category 5e-110 termination blocks shall meet or exceed Category 5e transmission
              requirements for connecting hardware, as specified in ANSI/TIA/EIA-568-B.2.

            • The manufacturer shall provide Category 5e component compliance certificates from third party
              testing organization upon request.

            • 5e-110 termination blocks shall be UL LISTED 1863.

            • 5e-110 termination blocks shall exceed IEEE 802.3 DTE Power specification to 4 times the
              rated current limits with no degradation of performance or materials.

            • 5e-110 termination blocks shall be third party verified, error free Gigabit Ethernet performance
              to IEEE 802.3 standard.

            • 5e-110 termination blocks shall meet or exceed the 4-connector channel performance
              requirements of Category 5e, per the ANSI/TIA/EIA-568-B.2.

      3.    Acceptable Manufacturers:

            • Hubbell Premise Wiring.
              The Hubbell products listed in the table below comply with all requirements specified in this
              document

             HUBBELL                       DeLCription
             CATALOG NUMBER
             110BLK50FTK5                  110 Field Termination Kit, 5e-110/50-pair with 5-Pair Conn. Blocks
             110BLK100FTK5                 110 Field Termination Kit, 5e-110/100-pair with 5-Pair Conn.
                                           Blocks
             110BLK300FTK5                 110 Field Termination Kit, 5e-110/300-pair with 5-Pair Conn.
                                           Blocks

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 36 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

               • Or approved equal of: Ortronics, Panduit, Systimax, Leviton
      4.       110 Installation Requirements
               • Follow manufacturer’s instructions.

               • Mount 5e-110 wiring blocks in the desired location.

               • Route cables through the openings in the wiring block base.

               • Terminate UTP cables to the 5e-110 block according to manufacturer’s instructions, using the
                 connecting blocks and proper termination tool.

               • To maximize transmission performance, maintain wiring pair twists as close as possible to the
                 point of termination.

               • The length of wiring pair un-twist in each termination shall be less than 0.5 inches (13 mm).

               • Cables extending from the block terminations shall maintain a minimum bend radius of at
                 least 4 times the cable diameter.

               • Cable terminations shall have no tensile or bending strain on IDC contacts after termination.
                 Note: Use the appropriate cable management hardware to relieve cable strain and control
                 bend radius.

PART 11              INFORMATION OUTLETS – DATA & VOICE
 A work area has at least one standard Information Outlet consisting of two Data RJ45 jacks. All of the
 RJ45 jacks shall be Category 6 unless otherwise specified are wired according to the 568B standard.

           ▪     DATA & VOICE Cabling Requirement LCenarios
                 •    DATA PC & VOIP Telephony INFORMATION OUTLET
                      ♦   2x DATA RJ45 CAT 6 Jacks per Information Outlet
                      ♦   No Traditional Voice Wiring Required
                 •    DATA PC & TDM/Digital or Analog Phones/PBX
                      ♦   2x DATA RJ45 CAT 6 Jacks per Information Outlet

A.    Information Outlet Locations
      1. The location of the information outlets is dependent on the environment in which the outlets will be
          installed. An office environment certainly is different than a laboratory, training room, or
          manufacturing area. If the outlets are to be wall- mounted, the bottom of the outlet is to be located
          15” above of the finished floor under normal conditions. However, there are many exceptions to this
          rule. If there is existing equipment that does not allow for this, such as a credenza or countertop,
          the outlet must be placed at a height appropriate to the situation.
      2. Locate the outlet where it is closest to the equipment and people it will serve. Keep in mind that the
         cord from the outlet to the device can be a trip hazard or may span across doors. In an office

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 37 of 69             8/9/2016              11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           environment, each desk or workstation should have an information outlet. If a particular area has a
           series of fax machines or modems, then additional outlets should be installed. The number of jacks
           in an outlet is standard, so to maintain the standard, additional information outlets of the same
           configuration should be installed; do not install non-standard outlets.
      3. Computer laboratories or training rooms require a large amount of connectivity in odd locations.
         Power poles are one solution as is the use of surface-mounted raceway or floor-mounted boxes.
         Each situation is different and must be considered individually. Again, standards are to be
         maintained in outlet configurations.
      4. When locating an outlet, consideration should be given to the route the cable must take to the
         information outlet. If the outlet is to be installed on a masonry wall and surface-mount raceway is
         used for cable routing, the location of the outlet may be more dependent on the path available
         down or across the wall than where the equipment is located. Each location must be looked at
         individually to determine if the route to the desired outlet location is possible.
      5. Wall-mounted outlets should not be located on heating units, equipment or ductwork. They are
         always to be located on either a gypsum, sheetrock, or masonry wall.
      6. A description of the information outlet configurations follows:
           •    Standard Office Information Outlets consist of: as detailed on the drawings attached to the
                contract, the contractor will install and terminate (3) four-pair, one UTP Category 6+ or 6a
                for Data cables onto individual RJ45 female jacks.
           •    Computer Laboratory or Training Room Information Outlets: as indicated on the attached
                drawings, the contractor will install and terminate the designated series of four-pair UTP
                Category 6+ or 6a cables onto individual RJ45 jacks. The number of cables and jacks vary
                from two to eight, depending upon the furniture configuration and number of PCs to be served.

B.    Category 6 Jacks
      In new construction projects, the default cabling infrastructure shall be Category 6 unless specified
      otherwise.

      1. Category 6 Jack Requirements
         • Jacks shall be standard 8-position, RJ-45 style, un-keyed, FCC compliant.

           •    Jacks shall be designed for 4-pair, 100 ohm balanced unshielded twisted pair (UTP) cable.

           •    Each jack shall be single unit construction, with snap – fit to industry standard keystone
                opening (.760” x .580”).

           •    Jack housings shall fully encase and protect printed circuit boards and IDC fields.

           •    Modular jack contacts shall accept a minimum of 2000 mating cycles without degradation of
                electrical or mechanical performance.

           •    Jack contacts shall be constructed of Beryllium copper for maximum spring force and durability.

           •    Contact plating shall be a minimum of 50 micro-inches of hard gold in the contact area over 50
                micro-inch of nickel.

           •    Jack termination method shall follow the industry standard 110 IDC punch-down

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 38 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           •    Jacks shall be compatible with a 4-pair single punch impact tool designed specifically for the
                purpose.

           •    IDC contact termination towers shall have tapered pair-splitting features to aid wire insertion
                and minimize pair un-twist.

           •    Jacks shall terminate 26-22 AWG solid or stranded conductors.

           •    Jacks shall terminate insulated conductors with outside diameters up to .050”.

           •    Jacks shall not require special cords, specialty tools or special installation requirements.

           •    Jacks shall include a translucent stuffer cap for wire retention and to permit visual inspection.

           •    Stuffer cap shall have retention snaps to assure conductor strain relief.

           •    Jacks shall accept FCC compliant 6 position plugs.

           •    Jacks shall accept optional hinged dust covers.

           •    Jacks shall be compatible with ANSI/TIA/EIA-606-A color code labeling.

           •    Jacks shall accept snap-on icons for specific identification.

           •    Jacks shall be available in various colors to meet specific customer applications.

           •    Jacks shall have attached wiring instruction labels to permit either T568A or T568B wiring
                configurations.

           •    Category 6 jacks shall be backward compatible with existing Category 3, 5, and 5e cabling
                systems for fit, form, and function.

      2. Category 6 Jack Performance Requirements
         • All transmission performance parameters shall be independently verified by a UL or ETL third
            party testing organization.

           •    Category 6 jacks shall exceed Category 6 transmission requirements for connecting hardware,
                as specified in ANSI/TIA/EIA-568-B.2-1, Transmission Performance Specifications for 4-Pair
                100 ohm Category 6 Cabling.

           •    Category 6 jacks shall exceed 10 Gb/s transmission requirements for connecting hardware,
                under the constraints of ANSI/TIA-TSB-155 (current draft).

           •    The manufacturer shall provide Category 6 component compliance certificates from third party
                testing organization upon request.

           •    Jacks shall be UL LISTED 1863 and CSA certified.

           •    Jacks shall exceed IEEE 802.3 DTE Power specification to 4 times the rated current limits with
                no degradation of performance or materials.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 39 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           •      Jacks shall be third party verified, error free Gigabit Ethernet performance to IEEE 802.3
                  standard.

           •      Jacks shall exceed 4 Gb/s data transmission capacity within the bandwidth of 1 – 250 MHz
                  when configured in a 4-connector channel.

           •      Jacks shall exceed the 4-connector channel performance requirements of Category 6, per the
                  ANSI/TIA/EIA-568-B.2-1 standard.

           •      Jacks shall exceed the 4-connector Category channel performance requirements for 10 Gb/s
                  transmission over Category 6, according to TIA/TSB-155 (current draft).

           •      The 4-connector channel test configuration shall utilize Category 6 patch panels and Category
                  6 patch cords, from the same manufacturer, with qualified Category 6 cable.

      3. Acceptable Manufacturers:

               • Hubbell Premise Wiring.
                 The Hubbell products listed in the table below comply with all requirements specified in this
                 document

                HUBBELL                    Description
                CATALOG NUMBER
                HXJ6xx                     NEXTSPEED® Category 6 Jack

                xx = Jack color. Replace xx with “W” for White, “BK” for Black, “B” for Blue, “GY” for Gray, “GN”
                    for Green, “OW” for Office White, “OR” for Orange, “R” for Red, “Y” for Yellow. Refer to
                    project drawing for color applications.
               • Or approved equal of: Ortronics, Panduit, Systimax.
      4. Category 6 Jack Installation
         • Horizontal cabling of the proper category shall be fully deployed from the TR or TE to each wall
            plate location according to applicable codes and standards.

           •      Cable slack, service coil, bend radii, and pathway fill ratio shall comply with applicable codes
                  and standards.

           •      Metallic horizontal cable pathways shall be bonded to an approved ground according to ANSI-
                  J-STD-607-A.

           •      Cable ends for termination shall be clean and free from crush marks, cuts, or kinks left from
                  pulling operations.

           •      Terminate jacks according to manufacturer’s instructions.

           •      To maximize transmission performance, maintain wiring pair twists as close as possible to the
                  point of termination.

           •      The length of wiring pair un-twist in each termination shall be less than 0.5 inches (13 mm).

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 40 of 69            8/9/2016               11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           •    Jacks shall be properly mounted in plates, frames, or housings with stuffer cap fully installed
                over IDC contacts.

           •    Horizontal cables extending from mounted jacks shall maintain a minimum bend radius of at
                least 4 times the cable diameter.

           •    Cable terminations shall have no tensile or bending strain on IDC contacts after assembly of
                faceplate or housing to the wall outlet.

           •    Jacks shall be tested as part of the installed horizontal cabling system, with faceplates
                assembled complete and properly mounted.

           •    Each link or channel in the horizontal cabling system shall be identified and tested individually,
                using an industry standard level III tester with correct settings.

           •    Each jack shall be tested as part of the horizontal channel or link for the parameters listed
                below.

C.    Face Plates

      1. Face Plate Requirements
         • Faceplates shall be constructed of high impact, UL94 V-0 rated thermoplastic.

           •    Faceplates shall be 2.75" W x 4.5" H (69.8 mm x 114.3 mm) for single gang and 4.5” X 4.5”
                (114.3 X 114.3 mm) for double gang.

           •    Port size in each faceplate shall be industry standard vertical keystone opening size (.760” x
                .580”).

           •    Faceplates shall accept Hubbell XJ-series UTP jacks and Snap-Fit fiber optic, audio, and video
                modules for multimedia applications.

           •    Faceplates shall provide for ANSI/TIA/EIA-606-A compliant workstation outlet labeling.

           •    Faceplates shall be provided with clear plastic and color-matched label field covers.

           •    Color-matched blank Snap-Fit modules shall be available separately to fill unused ports and
                openings as required.

           •    Two #6-32 pan head Phillips/slotted mounting screws shall be included with each single gang
                faceplate.

           •    Four #6-32 pan head Phillips/slotted mounting screws shall be included with each double gang
                faceplate.

           •    Jacks and Snap-Fit modules shall snap firmly into rear of faceplate and position flush to outer
                plate surface.

           •    Faceplates shall be compatible with standard NEMA openings and boxes.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 41 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           •      Faceplates shall be compatible with raceway fittings, surface mount boxes, service fittings,
                  flush mount boxes and drywall rings.

      2. Acceptable Manufacturers:

               • Hubbell Premise Wiring.
                 The Hubbell products listed in the table below comply with all requirements specified in this
                 document

                HUBBELL                  Description
                CATALOG NUMBER
                IFP11xx                  1-Gang, 1-Port IFP Face Plate
                IFP12xx                  1-Gang, 2-Port IFP Face Plate
                IFP13xx                  1-Gang, 3-Port IFP Face Plate
                IFP14xx                  1-Gang, 4-Port IFP Face Plate
                IFP16xx                  1-Gang, 6-Port IFP Face Plate
                IFP26xx                  2-Gang, 6-Port IFP Face Plate
                IFP29xx                  2-Gang, 9-Port IFP Face Plate
                IFP212xx                 2-Gang, 12-Port IFP Face Plate
                xx = Face Plate color. Replace xx with “W” for White, “BK” for Black, “GY” for Gray, “OW” for
                    Office White, to project drawing for color applications.

               • Or approved equal of: Ortronics, Panduit, Systimax.

PART 12            CABLE ROUTING SYSTEMS
Each cable routing system has advantages and disadvantages. Particular systems are favored for a variety
of reasons, including architectural considerations, appearances, cost, local ordinances, and material
concerns.
Various means of distributing cable from Communications/Data rooms/closets to the user work areas are
identified in the following:

A.    Ceiling Distribution System
      A distribution system within an accessible area above a false ceiling. This could either be a plenum
      area (where there is no enclosed system for cable routing) or an overhead conduit system (which has
      defined areas of access and routes).

B.     “J” Hooks
      Where not installed in conduits, cable trays, or other supporting devices, the horizontal wiring plan is to
      be installed onto “J” hooks or an acceptable equivalent from the information outlet to the termination
      point within the IDF or MDF/IDF room. The “J” hooks are to be installed a maximum of five feet apart
      and fastened to the ceiling or the top of the walls near the ceiling. The cables are to be tie-wrapped to
      the “J” hooks, without crimping the sheath. The cable contractor is to furnish and install the “J” hooks.
      Cooper B-Line BCM 21, 32, and 64 are acceptable.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 42 of 69            8/9/2016               11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

C.    Sleeves and Conduits
      1. The use of conduits and sleeves within a building is common for the transport of communications
          cable. Conduits and sleeves are to be sized and routes are to be planned within and between
          buildings in order to route the cable plant from the MDF to IDF and IDF to Information Outlet, and to
          accommodate any additional cabling required. The sizing of the conduits and sleeves is to be
          based on the number of cables, the location and environment surrounding the sleeve or conduit,
          and acceptable conduit fill levels, which are typically 40%. All conduits are to be installed with the
          appropriate sweep to maintain the required bend radius for copper and fiber optic cable. All sleeves
          and conduits are to be installed with bushings and suspended according to building industry
          standards.
      2. The following are guidelines to use in determining where sleeves and conduits are to be installed
         but does not limit nor identify all areas or situations where sleeves and conduits will be required.
           •    All masonry walls that have cables passing through them are to have sleeves installed.
           •    Gymnasiums and athletic areas are to have conduits installed to house cables passing through
                the area.
           •    Each MDF and IDF Room is to have sleeves installed to contain the large number of cables
                exiting the room. Conduits are to be installed in areas where cables extend from one building to
                another via covered or enclosed bridges and corridors.

      3. Cable routing is to follow a “streets and avenues” path in corridors where possible. However, there
         are a number of reasons for exceptions. In some cases, the corridors do not allow cables to be run
         because of architectural constraints or inaccessible ceilings. Also, in order to maintain the 90-meter
         standard for Category 6 cabling, some cables need to be run separately and diagonally to isolated
         information outlets. Throughout all runs, the contractor is to maintain EIA/TIA standards regarding
         the proximity of communications cabling to high voltage cabling, motors, transformers, fluoreLCent
         lighting, ballasts, etc.

PART 13          CABLING-GENERAL

A.    All cable shall meet the requirements of the NEC, except where other authorities or codes impose a
      more stringent requirement or practice. Codes, such as the NEC, do not normally include transmission
      performance requirements. This section specifies the essential media transmission characteristics. It is
      advisable to consult standards associated with the planned service or equipment to determine any
      specific media limitations.
B.    Contractor is to take all necessary precautions to assure that the maximum tensile load and minimum
      bend radius of all cables (fiber and copper) are not exceeded. When terminating Category 5e & 6 cable,
      care should be taken to maintain pair twists up to the termination point and not more than 0.5" of the
      cable pairs shall be untwisted. It is preferred that the cable sheath is also not removed more than 0.5"
      from the termination point. Tie wraps are to be hand-tightened on cables and are not to crimp the
      sheath. Contractor is responsible for protecting all connectorized cables from damage by other
      contractors at the information outlet before and after installation of the outlet faceplates.

C.    All riser and station cable installed is to be plenum-rated cable. The fluoropolymer resin that insulates
      Category 6+ plenum cables is engineered as a fire safety innovation. The NEC requires that all cable
      installed in plenum spaces and not encased in conduit must have certain fire resistance and low
      smoke producing characteristics. Not only are such cables highly resistant to fire but they also produce
      very little smoke.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 43 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                             DELAWARE STATE-WIDE INFORMATION
                                                       TECHNOLOGY AND ARCHITECTURE STANDARDS

 D.     All new Voice cabling will be terminated onto Category 6 RJ45 Patch Panels. The fiber optic cabling
        will be terminated onto fiber distribution panels with LC connectors.

 E.     Cables shall be terminated on the appropriate unassigned (vacant) portions of the wall-mounted Main
        and Intermediate Distribution Frames or Patch Panels and run as uninterrupted conductor sections to
        the Information Outlets. All cable terminations shall be made uniformly in sequence, commencing with
        termination of the first cable pair on the first connection points in the upper left-hand corner of each
        block.
 F.     Minimum separation distances between pathways and power wiring of 480 V or less are shown in Table
        1, below.

           Table 1 Separation of Communications Pathways from <= 480V Power Lines
                                                            Minimum Separation Distances
                                              Condition  < 2 kVA      2-5 kVA     > 5 kVA
      Unshielded power lines or electrical equipment     127 mm       305 mm      610 mm
      in proximity to open or nonmetal pathways.           (5 in)      (12 in)     (24 in)
      Unshielded power lines or electrical equipment      64 mm       152 mm      305 mm
      in proximity to a grounded metal conduit           (2.5 in)       (6 in)     (12 in)
      pathway
      Power lines enclosed in a grounded metal            76 mm       152 mm
      conduit (or equivalent- shielding) in proximity to   (3 in)       (6 in)
      a grounded metal conduit pathway.

              All cabling shall be at least:
              •   12” from high voltage lighting and fluorescent fixtures
              •   72” from transformers and motors

 PART 14          HORIZONTAL CABLING - CATEGORY 6 UTP DATA
 All riser and station cable installed is to be plenum-rated cable.

A.     Category 6+ 100 OHM balanced UTP Cable Requirements
        In new construction projects, the default cabling infrastructure shall be Category 6 unless specified
        otherwise.

        1. Cable construction shall be four twisted pairs of 23 AWG insulated solid conductors, with a ripcord,
           surrounded by a tight outer jacket.
        2. All 4 pairs will have a cross-hair (X) physical separator between the pairs.
        3. Conductor diameters shall be 0.0224” ± .0003” solid copper.
        4. Conductor insulation diameter shall be 0.039” ± .0005” fluoro copolymer.
        5. Outer jacket diameter shall be 0.235” ± .008” low smoke PVC, with a nominal wall thickness of
           0.015”.
        6. Ripcord shall be directly underneath the outer jacket.
        7. Cable shall be marked every 2 ft including
           • Cable Manufacturer
           • Cable Description

 These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
 Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
 should be directedto dti_tasc@delaware.gov

 Page 44 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                             DELAWARE STATE-WIDE INFORMATION
                                                       TECHNOLOGY AND ARCHITECTURE STANDARDS

           • Month and Year of manufacture.
           • Job number.
       8. UL, ETL, or CSA agency certification or verification markings shall be marked on the cable jacket
           according to the certifying agency’s requirements.
       9. Color coding of the pairs shall be as follows:
           • Pair 1: White/Blue; Blue
           • Pair 2: White/Orange; Orange
           • Pair 3: White/Green; Green
           • Pair 4: White/Brown; Brown
       10. Cable shall be supplied in 1000 ft spools or 1000 ft Reelex boxes.

 B.    Category 6 100 OHM balanced UTP Cable Performance Requirements
       1. All transmission performance parameters shall be independently verified by a UL or ETL third party
           testing organization.
       2. Cable shall exceed Category 6 transmission requirements specified in ANSI/TIA/EIA-568-B.2-1,
           and shall be tested through 550 MHz.
       3. Worst-case cable performance shall be +8.0 dB headroom over current TIA/EIA and ISO standards
           limits for NEXT and PSNEXT loss, and ELFEXT and PSELFEXT loss.
       4. Insertion loss shall be 3.0% lower than standard Hubbell Category 6+ plenum and riser
           cables described in Section 27 15 13.
       5. Worst case electrical performance characteristics shall be as follows:
           • Characteristic Impedance: 100 + 15 (1.0-100 MHz) 100 + 20 (101-250MHz)
           • Maximum Conductor Resistance: 9.38 /100 Meters @ 20°C
           • Maximum Resistance Unbalance: 3%
           • Maximum Mutual Capacitance:             5.6 nF/100 Meters @ 1 kHz
           • Maximum Capacitance Unbalance: 330 pF/100 Meters
           • Maximum Delay Skew:            25 ns/100 Meters
       6. The manufacturer shall provide Category 6 component compliance certificates from third party
           testing organization upon request.
       7. Cable shall be UL and C(UL) listed.
       8. Cable shall exceed IEEE 802.3af DTE Power specification to 4 times the rated current limits with no
           degradation of performance or materials.
       9. Cable shall be third party verified, error free Gigabit Ethernet performance to IEEE 802.3ab.
       10. Cable shall exceed the requirements of TIA/TSB-155: 10 Gb/s Ethernet Operation over 55 Meters
           Channel Length.
       11. Cable shall meet or exceed the 4-connector channel performance requirements of Category 6, per
           the ANSI/TIA/EIA-568-B.2-1 standard.
       12. The 4-connector channel test configuration shall utilize Category 6 jacks and patch panels, with
           Category 6 patch cords, from the same manufacturer, with pre-qualified Category 6+ cable.

B.2. Minimum Cable Performance:
      13. All measurements are at 250MHz
          • Insertions Loss: 32.7dB
          • NEXT: 41.4dB
          • ACR:8.6dB
          • ELFEXT: 23dB
          • Return Loss: 17.5dB

 These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
 Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
 should be directedto dti_tasc@delaware.gov

 Page 45 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

C.    Acceptable Manufacturers:

      1. Hubbell Premise Wiring
         The Hubbell products listed in the table below comply with all requirements specified.

           HUBBELL                  Description
           CATALOG NUMBER
            C6SPxx                   NEXTSPEED Category 6 550 MHz – Plenum Spool
            C6RPxx                   NEXTSPEED Category 6 550 MHz – Plenum REELEX
            xx = Cable color. Replace xx with “W” for White, “GY” for Gray, “B” for Blue, “Y” for Yellow. Refer
                to project drawing for color applications.

       2. Or approved equal of: Berk-Tek, Systemax, Panduit

D.    Category 6+ 100 OHM balanced UTP Cable Installation Requirements
      1. Pull cable into conduits, or place into raceway or cable tray as specified. Do not exceed 25 Lb. pull
          force per cable. Use appropriate lubricants as required to reduce pulling friction.
      2. All exposed wiring shall be installed in surface raceway.
      3. All wiring above ceilings or below access floors shall be installed in cable tray or open-top cable
          hangers.
      4. Cable slack and service loops shall be stored properly above the ceiling or under the access floor.
          A “figure-eight” service loop is recommended for Category 6 cabling to reduce EMI coupling.
      5. Pathway fill ratio in conduit, tray, raceway, etc. shall not exceed 40% of pathway cross-sectional
          area.
      6. Installed cable bend radius shall be greater than 4X cable diameter. Avoid kinking or twisting the
          cable during installation.
      7. Do not over-tighten cable ties, and do not use staples or clamps to anchor cables. Velcro straps are
          recommended.
      8. Recommended spacing of cable supports above the ceiling shall be 48”.
      9. Maintain the following clearances from EMI sources:
          • Power cable: 6 in.
          • Florescent lights: 12 in.
          • Transformers and electrical service enclosures: 36 in.
      10. Communications cabling that must cross power cables or conduit shall cross at a 90-degree angle,
          and shall not make physical contact.
      11. Length of each horizontal cable run from the TR to the wall outlet shall not exceed 90 meters.
      12. Leave sufficient slack for 90 degree sweeps at all vertical drops.
      13. Do not install cable in wet areas, or in proximity to hot water pipes or boilers.
      14. Cable ends for termination shall be clean and free from crush marks, cuts, or kinks left from pulling
          operations.
      15. Installed cable jackets shall have no abrasions with exposed conductor insulation or bare copper
          ‘shiners”. The installer is responsible to replace damaged cables.
      16. Horizontal cables extending from mounted jacks or panels shall maintain a minimum bend radius of
          at least 4 times the cable diameter.
      17. Firestop all cable penetrations through fire-rated barriers per local codes.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 46 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

PART 15          VERTICAL DISTRIBUTION SYSTEMS

A.    Riser Connectivity and Cable General

      1. The cabling system shall use a fiber/copper riser cable system between the IDF rooms and the
         MDF within the building.

      2. Copper Voice/Data Riser shall be 25-pair Category 3 plenum Copper Riser Cables Installed
         between each IDF and the MDF as indicated in the attached riser drawings. These cables are to be
         terminated onto the 110 termination blocks on the wall-mounted or rack-mounted frames in the IDF
         Rooms and MDF Room.
      3. Fiber Riser shall be 12-strand single mode fiber optic cable is to be installed between each IDF and
         the MDF Room as indicated in the drawings. These cables are to be terminated onto fiber optic
         patch panels located in the relay racks in each of the IDF rooms and the MDF Room. The 12-
         strand single mode fiber cable is to be connectorized with LC connectors on both ends.

      4. A plenum coaxial cable is to be installed from the MDF Head-End Room to the various IDF Rooms
         within the building. The cable is to be fastened to the wall- mounted plywood backboard in each
         floor’s IDF and MDF Room with 15 feet of slack neatly coiled, tie wrapped, and left dead-ended.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 47 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

B.    Fiber Backbone Distribution cable: indoor, non-armored

      1. Fiber Backbone Distribution cable Requirements
         • Optical Fiber Indoor Distribution Cable shall be constructed with 12 optical fibers, each coated
             with a 900 micron color-coded PVC tight buffer, surrounded by an aramid yarn strength
             member, Armored, and a single outer jacket with the appropriate flame rating.
         • Fiber cables shall be a non-metallic construction, OFNP (Plenum FT-6) flame rating.
         • Cable markings shall repeat every meter, and shall have at minimum the following information:
             a. Sequential length indicator marking (meters)
             b. Manufacturer’s name and catalog number
             c. Lot number, traceable back to the fiber draw lot
             d. Date of Manufacture
             e. Fiber type: (OM4 and singlemode)
             f. Cable rating (OFNR, OFNP, etc.)
             g. Applicable TeLCordia, TIA, IEC, and ICEA standard references and appropriate
                   UL/CSA agency listings
         • Cable jacket color shall be yellow for Singlemode 8.3/125 micron fiber.
         • Buffer position color codes shall conform to standard ICEA and TIA-598 conventions as
             follows:1-Blue, 2-Orange, 3-Green, 4-Brown, 5-Slate, 6-White, 7-Red, 9-Yellow, 10-Voilet, 12-
             Aqua.
         • Optical fiber in any cable construction shall be enhanced performance, bend-insensitive type.
         • Singlemode cables shall perform at minimum to the attenuation, bandwidth, and
             distance application parameters in the table below.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 48 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                             DELAWARE STATE-WIDE INFORMATION
                                                       TECHNOLOGY AND ARCHITECTURE STANDARDS

                    Fiber Gigabit and 10 Gigabit Ethernet Application Chart
                                            Max                                  1 GbE Distance           10 GbE
                          Wavelength        Attenuation        Bandwidth         (m) @                    Distance (m)
 Fiber Type               (nm)              (dB/km)            (MHz●Km)          850/1300nm               @ 1300nm
 SM 8.3 μm (OS2)          1310/1550          0.5/0.5           >25000            5000/-                   10,000/40,000

           •    Optical fiber cables as supplied shall meet or exceed the applicable IEC 60793-1 qualification
                test requirements for optical, geometry, mechanical, and environmental parameters as
                specified, and tested in accordance with TIA/EIA-455.

      2. PERFORMANCE REQUIREMENTS
         • For installed fiber cables, all fiber strands shall pass insertion loss and return loss in
            accordance with test methods ANSI/TIA/EIA-526-14 for multimode cables.
         • Installed fiber cables shall exceed all currently ratified bandwidth-distance- application
            performance parameters for IEEE 802.3ae (10 GbE) and for IEEE 802.3ba (40/100 GbE)
         • Plenum cables shall be rated UL NFPA-262/UL910/CSA FT-6

      3. Acceptable Manufacturers:

           •    Hubbell Premise Wiring or pre-approved equal.
                The Hubbell products listed in the table below comply with all requirements specified in this
                document

               HUBBELL                     Description
               CATALOG NUMBER
               HFCD15012PS                 Fiber Optic Cable – 12 Strand SM 8.3 μm (OS2), Plenum, Armored,
                                           yellow

           •    Or approved equal of: Panduit, Berk-Tek

      4. Fiber Backbone Distribution cable: indoor, non-armored Installation Requirements
         • Prior to cable deployment, backbone pathways (conduit, tray, raceway, wire basket, etc.) for
             cable routing shall be permanently installed in compliance with contract documents, and
             applicable codes and standards.
         • Racks, cabinets or enclosures into which cables are to be routed shall be permanently installed
             in compliance with contract documents, and applicable codes and standards.
         • Optical fiber cables shall be deployed using the proper pulling grip or apparatus attached to the
             exposed cable strength member. Contact the cable manufacturer regarding permissible
             methods for cable pulling. Never pull directly on the fiber strands of an optical fiber cable.
         • Cables shall not exceed minimum bend radius limits or maximum pulling loads during or after
             installation. Avoid crushing or abrasion of the cable jacket during installation.
         • Installed cables shall be fully supported and strain relieved from pulling on terminated
             connections. Apply wire ties loosely and avoid crushing or clamping cables with excessive

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 49 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                force.
           •    All non-armored fiber optic riser cables are to be installed in plenum inner-duct. Fibers in inner-
                duct or armored plenum riser fiber serving as riser cables are to be installed according to the
                attached riser drawing. Contractor to size the inner-duct for each cable run. Multiple fiber optic
                cables can occupy an individual inner-duct when non-armored fiber is not used.

PART 16           CAMPUS CABLING

A.    Outside Plant Cabling

      1. The contractor is to follow the drawings regarding the installation of outside plant (OSP) cabling to
         buildings remote from the main building, such as portable rooms, trailers, other small buildings, etc.
         Many remote buildings can be served by conduits underneath or within ceilings of protected
         overhangs and bridges.
      2. The contractor is to furnish and install outside plant cables and associated protector blocks, splice
         cases, and grounding where applicable in an approved manner.

      3. The contractor will be responsible for obtaining all required right-of-way easements and permits
         before any excavation on the property begins.

      4. All existing facilities in the area of excavation will be located and marked with paint, stakes, or flags
         before any excavation.

      5. Outside plant optical fiber cable shall be 50/125 laser-optimized singlemode strands loose-buffer
         tube water- blocking for outside plant application.

      6. Outside plant copper cable will be solid insulated conductors 24 AWG with gel-filled core in 25-, 50-,
         or 100-pair increments.

      7. RG-11 coaxial cable rated for OSP use will be used between buildings. Outside plant cables are to
         be routed aerially, underground, or buried by designed. Contractor may provide recommendations
         as to cable routing for approval.

      8. Where noted, the contractor is to use aerial plant cabling between buildings. In cases where cables
         are attached to poles or buildings, aerial spans are not to exceed 100 ft from the last pole to the
         building, using slack span construction (no guying at either end). EIA/TIA guidelines and NEC code
         are to be strictly adhered to for separation and clearances from power lines and traffic.

      9. Underground Cable is to be enclosed in conduit buried at least 24 inches below ground surface. In
         situations where fiber optic cables will be used, inner-ducts will be placed inside conduits to ensure
         physical protection for the cable. Proper fill ratios must be observed as well as proper bend radius.
         Metal sleeves through the foundation will be used to prevent conduit shearing. Sleeves must
         extend from inside the foundation wall to a minimum of 12”. The end of the conduit within the
         building must be securely fastened to withstand the placing of cable. Sleeves are to be sealed with
         plugs or sealant. Conduit must be bounded and grounded in compliance with EIA/TIA and NEC
         requirements.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 50 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      10. Minimum depth of trench should allow for 24 inches of cover from top of cable to final grade. Upon
          refilling the trench, the soil must be tamped to prevent sunken trench appearance. Conduit sleeves
          will be used for penetrations through foundation walls, using the same guidelines as for
          underground cable. OSHA regulations concerning shoring requirements must be followed during all
          phases of buried cable installation. Contractor must install buried cable so as to meet minimum
          separation distances from adjacent structures (power, gas, water, etc.) To minimize the chance of
          accidental dig-up, contractor will install detectable warning tape a minimum 18 inches above cable.
      11. Multi-pair protector blocks shall be installed to provide protection from voltage surges and sneak
          current. The protector panel shall be equipped with 110 wiring block and solid state protector
          unit’s type 4C, and others depending on the situation. Project Manager will coordinate with
          contractor. Protector panels shall be installed within 50 feet of each outside plant cable building
          entry point. Protector panels must be grounded and bounded to the building grounding system.

      12. Splice cases shall be provided and installed at both ends of outside plant cables. Splice cases shall
          be used for cable transition from to inside plant cables.
          • Fiber optic splice cases shall be designed to seal, bind, anchor, and protect cable splices and
              transition points from outside plant to inside plant cables. The case shall be fully equipped with
              a suitable splice kit for the fiber quantities specified.
          • Copper splice case shall be designed for use with non-pressurized cable. The case shall be of
              a durable fire-retardant material, single piece with a hinged cover. The case shall be equipped
              with a cable entrance end plates assembly of adequate size to accommodate entering and
              exiting cables, ground straps, and all necessary termination, mounting hardware.

      13. Pedestal/Cabinet shall have a heavy gauge galvanized steel housing or equivalent and be weather-
          resistant for the termination of copper and fiber optic cables. It shall be equipped with ground bar,
          protector blocks, and adequate space for splice cases to accommodate transition of cables into or
          out of the cabinet. Pedestal/Cabinet size dependent upon each situation.
      14. All OSP cables will be grounded according to EIA/TIA and NEC standards and codes.
      15. Contractor is to install a RG-11U Plenum Coaxial cable between the existing CATV Head-End
          Location and the MDF Room when indicated in the attached drawings. Not all buildings have a
          CATV Head-End, but if it exists, it will be noted on the attached drawings. These cables are not to
          be terminated, but must be neatly coiled and tie-wrapped with 40 feet of slack cable remaining at
          each end.

PART 17          PATCH CABLES
A.    Patch cables should meet the minimum performance requirements specified for each system. This
      requirement specifically prohibits the use of flat, non-twisted (also known as "silver satin") cords for
      Data or local area network applications. However, "silver satin" patch cables are acceptable for use in
      telephone systems.
B.    The contractor shall provide two Category 6 Patch Cords for each end of each standard outlet for
      horizontal LAN connectivity. The cords are to be of varying lengths based on the patch panel,
      electronics equipment, and work area configurations. The quantity and lengths are to be documented
      and agreed upon, and the owner or Project Manager is to sign for them upon acceptance. These cords
      are to be stored in the MDF or IDF room for which they are designated.
C.    The contractor is to provide dual LC to LC Patch Cords for connectivity for ports or equipment served

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 51 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      by the fiber patch panel. The cords are to be of varying lengths based on the patch panel and
      electronics equipment configurations. These cords are to be stored in the MDF or IDF room for which
      they are designated.

D.    Fiber Patch Cords

      1. Fiber Patch Cord Requirements
             Provide factory-made, dual LC to LC fiber cables in 1-Meter lengths for every fiber cable
             installed.
             LC Optical fiber patch cords shall be constructed with aramid-reinforced PVC loose-jacket
             duplex cable, with optical fibers having a 900-micron PVC buffer coating diameter. Optical fiber
             used in 10 GbE patch cords shall be laser optimized 50 or OS2 singlemode, per ANSI/TIA/EIA-
             492AAAC, with no substitutes.
             50 micron core optical fiber within the patch cord cable shall be graded index type in
             accordance with ANSI/TIA/EIA-492AAAC, with the following specifications:
             a. Core diameter: 50 +/-3.0 microns, or 8.3 micron for singelmode
             b. Cladding diameter: 125 +/- 2.0 microns
             c. Core/cladding concentricity: less than 3.0 microns
             d. Core non-circularity: 6% maximum
             e. Proof test: 100 kpsi
             f.    Effective modal bandwidth: 5700 MHz•km
             g. Coating diameter: 245 +/-15 microns
             h. Buffer diameter: 900 microns nominal
             Connector terminations on each end of the fiber patch cord shall be heat-cured epoxy type with
             a machine polish, inspected 100% for polish quality and mated-pair insertion loss.
             Epoxy volume within each connector shall be sufficient to properly surround and strain relieve
             the fiber and buffer layer at the buffer/fiber transition inside the connector body.
             Optical fiber patch cords shall be supplied in a sealed plastic bag with dust caps installed on
             each end, with insertion loss test results included.
             Optical fiber patch cords shall be available in standard lengths of 1, 2, 3, and 5 meters.
             Optical fiber patch cords shall be manufactured with industry standard LC or LC connector
             terminations on each end.
             Factory mounted connectors on each end of the patch cords shall comply with the applicable
             ANSI/TIA/EIA-604 Inter-mateability standard.
             Buffered fiber strands within the cable jacket shall be surrounded by aramid (Kevlar) material
             serving as a strength member.
             The aramid (Kevlar) strength member shall be mechanically secured at each connector to
             provide tensile strain relief of the optical fiber.
             Additional strain relief of the buffered fiber shall result from crimping the rear of the connector
             during termination.
             Duplex fiber patch cords shall be a zip-cord cable construction with jacket cross-section
             dimensions of 3.0 mm X 6.0 mm for LC style.
             Duplex fiber patch cords shall have reverse-pair polarity according to ANSI/TIA/EIA-568-B.3
             and TIA/EIA-TSB-125.
             Cable jacket shall be marked with the cable manufacturer, UL Optical Fiber Non-Metallic Riser
             rating (Type OFNR) designation, lot number, and fiber core/cladding diameter designation.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 52 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                Fiber A-B polarity shall be clearly marked on each end of duplex patch cords.
                Optical fiber patch cord jacket color shall be aqua blue, specifically for 50 micron laser
                optimized singlemode fiber cables.
                Fiber patch cord connector materials shall be as follows:
                a. LC Ferrules: zirconium ceramic
                b. LC housings: injection molded thermoplastic
                c. Dust Cap: nylon or PVC
                d. Strain relief boot: UL94-V0 molded PVC
                e. Strain relief boot on all connectors shall be beige.
                f.   LC connector outer housing shall be beige.

      2. Fiber Patch Cord Performance Requirements
         • 50 micron laser optimized and singlemode patch cords shall have a maximum mated-pair
             insertion loss of 0.60 dB per end, with a minimum return loss of –20 dB.
             Fiber patch cords shall exceed 10 Gigabit Ethernet performance requirements of IEEE 802.3
             standard.
         • Fiber patch cords shall exceed the mechanical reliability requirements for tensile, flex, twist and
             impact as specified in ANSI/TIA/EIA-568-B.3, Annex ‘A’.
         •   Fiber patch cords shall exceed the environmental reliability requirements for high/low
             temperature and humidity as specified in ANSI/TIA/EIA-568-B.3, Annex ‘A’.

      3. Acceptable Manufacturers:

            • Hubbell Premise Wiring.
              The Hubbell products listed in the table below comply with all requirements specified in this
              document

             HUBBELL CATALOG                Description
             NUMBER
             DFPCLCLCFyySM                  LC-LC Optical Fiber Patch cords, OS2-SM, yellow

             (yy=length-1,2,3,5m)

            • Or approved equal of: Ortronics, Panduit, Systimax.

E.    Category 6 Patch Cords
      In new construction projects, the default cabling infrastructure shall be Category 6 unless specified
      otherwise.

      1. Category 6 Patch Cord Requirements
            The contractor shall provide two Category 6 Patch Cords for each end of each standard outlet
            for horizontal LAN connectivity. The cords are to be of varying lengths based on the patch
            panel, electronics equipment, and work area configurations. The quantity and lengths are to be
            documented and agreed upon, and the owner or Project Manager is to sign for them upon
            acceptance. These cords are to be stored in the MDF or IDF room for which they are
            designated.
            Category 6 patch cords shall be constructed with a clear polycarbonate plug and boot having
            vertically staggered, trifurcated contacts, each having 50 micro-inches of gold plating.
            Plug dimensions and function shall comply with FCC 47, Part 68.5.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 53 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                Patch cords shall have a snag-less feature, integral to the strain relief boot on each end.
                Patch cords shall be constructed with category 6 patch cable, with 24 AWG 7/32 tinned copper
                stranded conductors, each insulated with polyethylene, and overall jacket with UL flame-
                retardant PVC.
                Patch cords shall be manufactured using a T568B wiring format, and shall function suitably for
                either T568A or T568B wiring schemes.
                Patch cords shall be available in the following colors: black, blue, gray, yellow, orange, red,
                green, white, and purple. Custom lengths and colors shall be available with a delivery lead-
                time quotation.
                Standard patch cord lengths shall range from1 ft. to 20 ft.
                Category 6 patch cords shall be backward compatible with existing Category 5 and 5e cabling
                systems for fit, form, and function.

      2. Category 6 Patch Cords
            All transmission performance parameters shall be independently verified by a UL or ETL third
            party testing organization.
            Category 6 patch cords shall be channel performance balanced with Hubbell category 6 jacks,
            patch panels, and punch-down blocks.
            Category 6 patch cords shall meet or exceed Category 6 component transmission requirements
            for connecting hardware, as specified in ANSI/TIA/EIA-568-B.2-1 standard.
            The manufacturer shall provide Category 6 component compliance certificates from third party
            testing organization upon request.
            Patch cords shall be cUL and UL LISTED 1863.
            Patch cords shall exceed IEEE 802.3 DTE Power specification to 4 times the rated current
            limits with no degradation of performance or materials.
            Patch cords shall be third party verified, error-free Gigabit Ethernet performance to IEEE 802.3
            standard.
         • Jacks shall exceed 4 Gb/s data transmission capacity within the bandwidth of 1 – 250 MHz
            when configured in a 4-connector channel.
            Category 6 patch cords shall meet or exceed the 4-connector channel transmission
            performance requirements of Category 6, per ANSI/TIA/EIA-568-C.2 standard.
            The 4-connector channel test configuration shall utilize Category 6 patch panels, blocks, and
            jacks,

      3. Acceptable Manufacturers:

            • Hubbell Premise Wiring.
              The Hubbell products listed in the table below comply with all requirements specified in this
              document

             HUBBELL                       Description
             CATALOG NUMBER
             HC6xx01                       Category 6 Patch Cord, 1FT
             HC6xx03                       Category 6 Patch Cord, 3FT
             HC6xx05                       Category 6 Patch Cord, 5FT
             HC6xx07                       Category 6 Patch Cord, 7FT
             HC6xx010                      Category 6 Patch Cord, 10FT
             HC6xx15                       Category 6 Patch Cord, 15FT

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 54 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

             HC6xx20                  Category 6 Patch Cord, 20FT
             HC6xx25                  Category 6 Patch Cord, 25FT
             xx = Cable Color. Replace xx with “W” for White, “BK” for Black, “B” for Blue, “GY” for Gray, “GN”
                 for Green, “P” for Purple, “OR” for Orange, “R” for Red, “Y” for Yellow. Refer to project
                 drawing for color applications.

            • Or approved equal of: Ortronics, Panduit, Systimax.

PART 18          FIRE STOP - PENETRATION SEALANT
A.    Provide fire-resistant silicone foam fill to restore fire ratings to all wall, floor, or ceiling penetrations.
      Foam must be UL classified and meet NEC and local code.
B.    All penetrations through fire-rated floors and walls shall be sealed to prevent the passage of smoke,
      fire, toxic gas, or water. The fire rating of the penetration seal shall be at least that of the floor or wall
      into which it is installed, so that the original fire rating of the floor or wall is maintained as required by
      Article 300-21 of the National Electric Code.
C.    No flammable material may be used to line the chase of the hole in which the fire stop material is to be
      installed.
D.    When damming materials are to be left in place after the seal is complete, then all such materials shall
      be non-flammable.
E.    The sealant shall be poured into the hole after each cable has been spread to allow a minimum of ½" of
      foam to flow between them. No cables may be touching each other, because contact between cables
      could allow voids to form in the fire stop.
F.    If plastic cartridges are used for smaller installations, the chemical components of the foam shall be pre-
      measured within the cartridges to ensure the proper ratios.
G.    The sealant shall remain resilient and pliable to allow for the removal and/or addition of cable without
      the necessity of drilling holes. It shall adhere to itself perfectly to allow any and all repairs to be made
      with the same material. It shall allow for vibration, expansion, and/or contraction of anything passing
      through the penetration without affecting the seal, or cracking, crumbling, and spalling.
H.    When sealant is injected into a penetration, the foam shall expand to surround all the items within the
      penetration at that time and be fire resistant, maintaining the pass-minute rating.. No heat shall be
      required to further expand the foam to block the passage of fire and smoke or water.
I.    The foam sealant material shall have been subjected to fire exposure testing in accordance with
      standard time-temperature curve in the Standard, UL, ASTM E
J.    119, and NJPA 251. The foam fire-stop material shall also have been subjected to the hose stream test
      in accordance with UL 10B.

PART 19          TESTING

A.    General Test Procedures
      1. Before an application for final acceptance of the work will be considered, all tests stated within this
         section shall be satisfactorily completed. The communications work shall include miLCellaneous
         tasks, (e.g., removal of panel trims, junction, and pull box covers) deemed necessary to
         demonstrate compliance with the requirements of the Communications specifications, as well as
         cable and equipment manufacturers’ recommended installation procedures.

      2. Upon completion of testing and problem resolution, all connections must be 100% error free: “Error

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 55 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

           free" is defined to mean the item meets all the manufacturers' specifications and recommendations
           as published in their latest manufacturing manuals for proper installation and testing. In addition,
           each item must conform with all other related industrial practices and standards, Building Trades,
           and Electrical and Communications Industry Standards and Practices.

      3. Upon successful completion of each item of testing, the Contractor shall issue in writing a certificate
         of compliance, along with the test results, to the Project Manager. All failed CAT-6 – 6a cables
         and/or Fiber strands shall be clearly labeled and identified as defective, with the type of defect (i.e.
         open ring side, grounded tip, short, excessive loss, etc.) identified.

      4. The Contractor will attempt to remedy any defective copper cable pair or Fiber cable strand and
         specify in the documentation the location of the problem as identified during the testing procedures.
         The Fiber trouble location and identification must be completed with an OTDR.

B.    Copper Cable Test Procedures
      1. Contractor must complete cable system performance verifications on all copper and fiber cable as
         specified below and provide the test results to the owner or project manager. Category 6 – 6a
         cable must meet or exceed all manufacturer’s and EIA/TIA standards for performance and
         installation. Fiber cable must also meet or exceed all manufacturer’s and EIA/TIA standards for
         performance and installation.

      2. All copper and fiber optic testing documentation is to be submitted on a CD, as well as 8.5” x 11”
         hard copies.

      3. At a minimum, in addition to any other required testing, the Contractor shall conduct and report on
         the following tests of copper cabling after the installation is complete:
            • MDF-to-IDF tests of all new riser pairs installed under this contract, to determine continuity,
                shorts, crossed pairs, correct pinning, and grounds.
            • IDF (110 frame or patch panels)–to-information outlet tests of all new cable pairs installed
                under this contract, to determine continuity, shorts, crossed pairs, correct pinning, and grounds.
            • The coaxial cable is to be tested from the MDF Room to the IDF Room and from the IDF Room
                to the coax outlet. Contractor is to test for continuity, shorts, and grounds.
            • The horizontal Category 6+ – 6a cabling, installed from the IDF Room to the Information Outlet
              at the workstation, is to be manufacturer certified and warranted for Category 6+ – 6a
              compliance. All manufacturers’ performance certificates and extended warranties are to be
              provided to the owner or project manager upon completion of the testing and manufacturer
              certification. Contractor is to present copies of certificates identifying the contractor as a current
              certified VAR for the selected cabling system and therefore, qualified to install a certified cable
              plant.
            • All category 6+ – 6a cabling is to be tested end–to-end and documented for Category 6+ – 6a
              compliance at all frequencies up to and including 250MHz for 6 – 6a. Such testing is to comply
              with the procedures and standards outlined by the cable manufacturer and EIA/TIA TSB - 67
              concerning testing of Category 6+ – 6a cable plant.
            • A certified Cat 6+ –6a testing system is to be used for such testing to insure that cable pairs are
              defect free. "Defect free" for the copper cable is defined as a copper pair not having any pair
              reversals, split pairs, shorts or opens. Test results shall be provided to the Owner or Project
              Manager within 2 days after testing or 5 days prior to the Owner connecting electronic
              equipment onto the cable network, whichever is sooner. The contractor must also provide

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 56 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                testing summary reports of all category 6+ – 6a cables including run numbers, and pass/fail
                results with respect to length, impedance, DC resistance, mutual capacitance, attenuation,
                NEXT loss, and active ACR. The contractor must also provide spreadsheet analysis of the
                linearly dependent parameters of length, DC resistance, mutual capacitance, and attenuation;
                the field measured values shall be compared to the specifications values on one spreadsheet.
            •   In the event that a CAT 6+ – 6a cable fails to perform to the manufacturer's specifications, the
                Contractor will, at the owner’s request, remove the cable and replace it with a new cable,
                replacing the defective cable at no additional expense to the owner.
            •   End-to-end testing is required for every RJ-45 connection. An owner's representative may
                accompany the Contractor’s staff to witness the end-to-end testing. End-to-end testing is
                defined herein as testing all cabling links to the very last termination point. The Contractor is
                required to supply sufficient quantities of two-way radios and test equipment to ensure that the
                tests are completed accurately and expeditiously.
            •   The Owner, DTI, or Project manager may conduct performance tests of transport electronics
                connected to the cabling system. Successful equipment performance tests do not relieve the
                Contractor from the specified testing, repair, and documentation requirements.
            •   The Contractor shall provide to the Owner or Project Manager with copies of all copper-cable
                test results.

C.    Fiber Optic Cable Test Procedures
      1. All fiber optic cable and associated equipment lateral, and vertical riser cabling must be thoroughly
          tested. The fiber cable will be accepted only after each strand is tested in accordance with the
          specifications defined herein. All strands are to be tested and found to be 100% acceptable.
      2. The Contractor shall test all cables, connectors, associated equipment, and hardware furnished by
         the Contractor upon receipt of same as defined herein.

      3. As a minimum, the Contractor shall test, as described below, all optical fiber cable strands installed
         within the scope of this proposal:
            • Fully test complete links only. Piecemeal testing is not acceptable.
            • Perform end-to-end, bi-directional attenuation (loss) test for each fiber strand at 1310 and
              1550 for singelmode. Conduct tests in accordance with EIA/TIA-526-14, Method B and with
              test instrument manufacturer's published instructions.
              a. Demonstrate that measured link loss does not exceed the expected value
                   based on the number of mated connector pairs, the connector's published loss
                   per mated pair, and the cable's published loss based on distance.
              b. Strands whose measured attenuation falls outside the acceptable range shall
                   be subject to further inspection and testing to determine the nature of the
                   fault. At a minimum, an OTDR shall be used to: determine the true loss for
                   each connector pair and the exact length of the fiber, and to identify the
                   presence of any core damage.
              c. Riser end-to-end testing of individual optical fibers is considered to be from
                   the MDF Room to the IDF Rooms distribution panels on each floor.
              d. Horizontal end-to-end testing of individual optical fibers is considered to be
                   from each floor’s IDF Room’s Fiber Distribution Panels to the Information
                   Outlet.
            • Faults related to connectors shall be corrected and the fiber re-tested as stated above until
              acceptable attenuation measurements are received.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 57 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

            • Where defects are found to be inherent in the fiber itself, notify the Project Manager in writing.
                Upon obtaining approval by the Project Manager, replace any cable having fewer than the
                manufacturer's guaranteed number of serviceable fibers.
            •   Remove all newly installed defective cables from pathways. Do not abandon cables in place.
            •   All test results and corrective procedures are to be documented and submitted as a
                spreadsheet, and digitally on a USB thumb drive to State/DTI within five (5)
                working days of test completion.
            •   Considering that the fiber cable plant is to be certified, each test report form shall provide at
                least the following information:
                a. Project name
                b. Contractor's name
                c. Date(s) of preparation and of testing
                d. Fiber type, strand count, connectors and patches
                e. Designated cable number (regardless of whether only one cable of each type is present)
                     and individual fiber numbers
                f. Make, model, serial number, and date of last calibration of test equipment used
                g. Name of test crew foreman
                h. Test results: Calculated maximum link loss, length of run, OTDR, and also
                i. Power Meter-measured link loss for each fiber, pass/fail result, and comments.
            •   In addition to the tests specified above, the Contractor shall be present while the Owner or
                Project Manager conducts performance tests of the transport electronics connected to the
                cabling system; the contractor shall conduct on- the-spot cable tests and effect cable plant
                repairs as necessary. Successful equipment performance tests do not relieve the Contractor
                from the specified testing, repair, and documentation requirements.

            • Recommended test equipment:
                 a. Optical fiber power meter and Light Source: OS-100D Light Source, or equivalent.
                 b. TDR: Tektronix TFP2 FiberMaster, Laser Precision TD-2000 or equivalent with 850nm and
                    1300nm emitter modules and hard copy printout, or equivalent.
                 c. Optical fiber inspection scope: Cambridge Instruments 10x fiber scope, or equivalent.
            • The Contractor shall provide copies of all fiber and copper cable test results to the Owner or
                Project Manager.
            • All fiber optic cabling (workstation and riser) is to be installed in a manner that complies with
                and allows Owner to receive the manufacturer’s extended warranty. The contractor is to be
                certified and authorized to provide the extended warranty. A manufacturer's extended warranty
                is to be provided, through the contractor, upon completion of the testing and manufacturer’s
                certification. Contractor is to present copies of certificates identifying the contractor as a current
                certified VAR and therefore, qualified to certify and install the cable plant.
            • The Owner and Project Manager reserves the right to observe any or all portions of the testing.
                Notification of testing is at least three days prior to start of testing.

D.    Replacement
      Any fiber strand, connector, block, or module installed by the Contractor that fails to meet
      the loss budget, or that tests below the manufacturer's standards, shall be replaced at no
      additional cost to the owners or State/DTI. The replacement cable, connector, or part shall
      be tested after repairs have been made to verify compliance. Only equipment that meets

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 58 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      the installation requirements stated herein shall meet the system’s acceptance
      requirements.

E.    Source Manufacturing/Quality Control
      Cables that are supplied by the Contractor, and test outside of the factory test data by a
      margin of 10 percent on loss, may be deemed non-usable and returned to the manufacturer
      for replacement.

F.    Physical Inspection
      Prior to conducting any transmission testing, the following visual inspections will be performed:
      1. Verify that all cable has been installed in full compliance with the proposal specifications.

      2. Check for physical damage to the Fiber Distribution Panels and termination hardware.

      3. Check that all cabling is properly jacketed, installation properly labeled at both ends of the cable,
         inner-duct and termination hardware is completed in all IDFs and the MDF Room.

      4. Verify that all cable bends are within the manufacturer's specified bend radius.

      5. Verify that all cabinets and racks (which require grounding) are properly grounded and comply with
         the National and Local Electrical Codes and State Standards for grounding.

      6. Verify that the cables are properly approved and structurally supported for termination.

      7. Verify that all Delaware Fire Code requirements have been met and satisfied.

G.    DOCUMENTATION
      Proper labeling and documentation will allow a technician to quickly trace a particular cable link and will
      significantly reduce the time and costs of moves, additions, changes, and troubleshooting. Both labeling
      and documentation depend on the use of a system-wide coding LCheme that will identify and locate
      each component of the wiring system and allow all components to be linked in a logical fashion.
      There are three components of wiring system documentation:
      1. Labeling Communications/Data room/closet termination areas aids in identifying the source and
         function of a circuit.
      2. A labeling scheme simplifies the documentation process.
      3. “As built” documents provide a permanent record of the communications infrastructure. These
         documents are a critical management resource. As a result, it is imperative that "as built"
         documentation be prepared as part of the communications infrastructure project. In addition, these
         documents must be kept current throughout the system's life cycle.

H.    Termination Blocks
      Labels on the connecting hardware should be coded based on the function of the terminated wiring.
      Colored designation strips are typically provided with a termination block.

I.    Cable and Information Outlet Identification

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 59 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      The Contractor shall furnish and install cable tags labeled with identifying cable numbers mutually
      agreed upon with contractor and the Owner or Project Manager.
      1. The Contractor shall clearly and consistently mark the appropriate designation strip labels on all
         termination hardware mutually agreed upon with the Owner or Project Manager. Contractor will
         submit a sample of all designation labels for approval before installation.
      2. The Contractor shall affix outlet identification labels, machine printed or typed, with identifying cable
         numbers as shown on the attached drawings.
      3. Subsequent to pulling and terminating cables, the Contractor shall place the appropriate cable tags
         within six (6) inches of each end of each copper cable and eighteen (18) inches of each optical fiber
         cable end.
      4. If the cable tape becomes illegible or is removed at any time during the job, the
      5. Contractor shall immediately replace it with a duplicate preprinted cable tag.
      6. The Contractor shall provide the Owner or Project Manager with a listing of all cable identification
         numbers, keyed to cable types.
      7. Contractor will label each information outlet with the following labeling scheme: If the 1st floor IDF
         closet “A” is the origination point of the cable feeding workstation “007” the following is the
         configuration of the label to be installed:
                       Floor- IDF Closet - Information Outlet Number
                       Example: 1A-007
      8. Contractor will submit for approval a sample of all information outlet designation labels.

J.    “As-Built” Documentation
      Maintaining records and documents is the most important portion of the administration of a
      communications infrastructure. Maintenance and moves, additions, and changes can become very
      difficult if a current set of records and documents is not maintained. In fact, isolation and resolution of
      problems are often delayed because configuration information is either unavailable or outdated.
       Subsequent to the installation and prior to acceptance, the Contractor shall prepare and issue As-Built
       drawings, in an AutoCAD format, that shall reflect the lengths of cables installed and the actual
       manner and conditions of installation, including all deletions from, additions to, or departures from the
       contract documents. These documents are to include the information outlet station numbers and cable
       routing where they vary from the original plan. A copy of these documents will be stored in the MDF,
       with a master copy located at the Owner or Project Manager.

K.    Cable Management System
      Wiring and equipment relationships must be maintained in a database or spreadsheet (depending on
      their complexity). The best approach is to use a third- party vendor's application for tracking cable
      management. These records contain comprehensive information about the users' communications
      configuration. The information will be very valuable in the support of long-term user-community
      communications requirements.

PART 20          APPENDIX A – COMMUNICATIONS PLANNING CHECKLIST

A.    Space allocation for Communications/Data room/closets

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 60 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

      1. Based on a number of factors, including the:
            •   Type of equipment to be installed
            •   Size of the phone and data termination backboards
            •   Access to floor cores and conduits
            •   Cable tray requirements
            •   Location, size, and swing of the Communications/Data room/closet door(s)
      2. Square footage is not as important as the actual floor dimensions and the placement of the
         equipment. It is possible to design around some obstacles and still have a functional facility. For
         instance, an oblong room is not as desirable as a square room having the same square footage.
      3. The criteria for establishing the size of a Communications/Data room/closet and determining
         whether or not it is functionally acceptable are complex. Answering the following questions is the
         first step in determining the long-term feasibility of a communications room or closet:
            • What will be the closet’s primary function: phone, data, or combined services?
            • Where is it located in proximity to serviced workstations, network rooms, and other
                Communications/Data rooms/closets?
            • What type of equipment is going to be in the room/closet?
            • Is it wall- and/or rack-mounted?
            • How much equipment will be put in the room/closet? What are the dimensions of those
                devices?
            • What are their environment requirements?
            • Based on the type(s) of equipment going into the room/closet, what is the installation,
                maintenance, and operator work space required around the equipment?
            • Can the equipment be attached securely to the structure?
            • What cable types are being used? What are the cable separation requirements? Where are the
                cables terminated within the closet?
            • Does equipment mounted in the closet require an open space? Is there any other device
                needing clear space?
            • Is the room/closet securable? Do other entities need access to the space? What are their
                space requirements?
            •   What size is the door? Does it swing in or out? Can the door be modified?
            •   Is power available? Can it support the room/closet electrical requirements? Can it be modified?
            •   Does the room need air conditioning? Does it ventilate well? Can it be modified?
            •   Where are the floor cores and the ceiling access points for conduits?
            •   Are there expansion requirements? Can the expansion requirements be accommodated by the
                room/closet size? Can the closed be enlarged at a later date?

PART 21           APPENDIX B - CABLE INSTALLATION CHECKLIST

 A. Check Local Building Codes
    The requirements stipulated by Section 800 of the National Electrical Code for Communications cable
    installations produce an orderly installation. However, it is important to consult your building inspector to
    determine whether there are special local requirements. Strapping requirements depend upon the
    building's design, State and Local Standards, and codes. Terminations can be made in standard
    junction boxes.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 61 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

 B. Coordinate with Other Contractors
    Plan to install the cabling system in new buildings after the power wiring, air- handling ducts, and ceiling
    supports have been installed, but before the ceiling tiles are in place. This will prevent damage to the
    cable system during construction.

 C. Plan the Job
    On a blueprint, mark all terminations and desired routings, if known, to accommodate future building
    modifications.
 D. Label the Cables
    Label each cable reel and its free end according to the termination locations marked on your blueprint.

 E. Pull Cable into Place
    Deliver the cable from the bottom of each reel, making sure not to kink, crush, or pinch the cable. Pull
    groups of cables to a logical point and then fan out to the individual termination points. Arrange the
    cables neatly so they are easily identifiable for relocation. Separate the Communications cables from
    other cables by at least six inches and avoid sharp edges, tight bends, and locations that would subject
    the cable to abrasion, corrosion, or moisture. According to the National Electrical Code, low-voltage
    cables cannot share a tray with power cables. Running signal cables close to power cables may also
    cause hum pickup. If in doubt about cable locations, consult the standards or the Owner.
 F. Remove Slack
    Remove slack in lines by pulling the cables back to the wiring room and by adjusting their ceiling
    location as needed.
 G. Label and Cut
    Label each cable and then cut it off, making sure to leave enough cable to reach the termination panel.
 H. Tie Cables Together
    Use cable ties to bundle and secure parallel runs together. Place the ties at intervals sufficient to
    prevent sagging and to maintain neatness. Distances between ties may vary from six inches to four
    feet, depending on the size of the cables.

 I.   Strap the Cable
      Use straps to fasten the tied cable bundles to hangers at 4-foot or other appropriate intervals. The
      distance between hangers will vary from 3 to 20 feet, depending upon the strapping surface, the type
      and number of cables in each bundle, State and Local Standards, and codes. Make sure to support the
      cables with hangers rather than pipes, conduit, or other structures in the building plenum. If space
      permits, use existing hangers; otherwise, install new ones. Do not use straps that are too small for the
      cable diameter because they can cut or pinch the cable insulation.

 J.   Inspect the Job
      Be sure that the cables are not resting on false ceilings or near electrical fixtures or sagging more than
      three inches from the point of the tie wrap.

PART 22           APPENDIX C - QUALITY ASSURANCE

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 62 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

 A. All materials used shall bear the Underwriters' Laboratory, Inc. label, provided a standard has been
    established for the material in question.
 B. All products and materials shall be new and unused, clean, and free of defects, damage, and corrosion.

PART 23          APPENDIX D - CODES, REGULATIONS AND STANDARDS
 A. All installations and equipment shall be in compliance with, equal to or exceed the minimum
    requirements of OSHA, NEC, NEMA, IEEE, SAME, ANSI, UL, EIA, TIA recommendations and the
    rules, regulations and requirements of the Federal Communications Commission.
 B. The installation shall comply fully with all applicable Local, County and State of
 C. Delaware laws and ordinances, regulations, and codes.
 D. Local electrical and building codes in Delaware may be more restrictive than national codes,
    recommendations or practice. Follow the most restrictive code or recommendations.
 E. Should any change in plans or Specifications be required to comply with governmental regulations, the
    Contractor shall notify the Owner or Project Manager at the time of submitting the construction
    schedule.

PART 24         APPENDIX E - WARRANTY
Besides the manufacturer’s extended warranty the Contractor shall submit a single Guarantee stating that all
portions of the work are in accordance with Contract requirements and guaranteeing all work against faulty
and improper material and workmanship, including work and materials of all subcontractors, manufacturers,
suppliers, and sub trade specialists, for a period of twenty-five (25) years from date of final acceptance by
the project manager, State/DTI, and Owner. Where guarantees or warranties for longer terms are provided,
such longer terms shall apply. Within 24 hours after notification, the Contractor shall correct any deficiencies
that occur during the guarantee period at no additional cost to Owner, all to the satisfaction of the Project
Manager and or Owner.
When installed by a Certified Installer and used in a Structured Cable System, the manufacturer’s extended
warranty shall cover the installation for a period of 25 years against defects in material and workmanship. It
shall also guarantee that it will support any current and future applications designed for Data transmission
over the 100/500MHz link/channel, as defined in TIA/EIA 568A Communications Standard.
All move, add and change (MAC) activity shall be covered by the warranty provided it is performed by a
Certified Installer.

PART 25           APPENDIX F - BID/QUOTE RESPONSE FORMAT

A.    Proposal identification number or control number. This number will be used as a reference for this
      individual proposal and will facilitate coordinating multiple bids or quotes for the same location or job
      site.
B.    Requesting State Agency and Contact name, phone number and address. This should be the name of
      the State agency requesting the quote or bid and that agency’s contact person’s phone number(s) and
      address.
C.    Building or office location address. This address should be the actual location of the job site. This
      address should include the floor numbers, if more than one story, and building numbers or names, if
      more than one building is involved.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 63 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

D.    Total Cost of Bid/Proposal. This dollar amount should include the total material and labor cost. The
      material and labor cost should be stated separately and then totaled. Also state whether or not labor
      costs are based on prevailing wage standards or not.

           Example:
            Material                  $3,500.00
            Labor Prevailing          $2,750.00
            Total                     $6,250.00

E.    Scope of Work. This section should be a written description of the work to be performed. It should be
      function-specific.
           Example:
            • Install, terminate both ends, test, and label XX work area locations consisting of one Voice and
                two Data CAT6 cables and CAT6 568-B RJ45 jacks.
            • Install one Voice cable from the Communications Closet to the Fir/Security Alarm Panel
                location.
            • Provide and install a 100-pair plenum-rated riser cable from the boiler room to the main
                communications closet and terminate on 110 type wall mount hardware.
            • Provide and install 7’ relay racks and CAT6 patch panels.
F.    Material
      The material should be and itemized list with manufacturer's name and part numbers, including all piece
      parts and quantity of each. Total man hours to complete the job should be included as an item in the list.

           Hubbell Cable                         Blue         C6RPB                          2,800 ft
           Hubbell Cable                         White        C6RPW                          2,000 ft
           Hubbell Jack Single                                HXJ6xx                            14 ea
           Hubbell Jack Double                                HXJ6xx                            14 ea
           Hubbell 110 block                                  30200007                           1 ea
           Hubbell Panel P6E48U                               951044344                          1 ea
           CIRCA protector panel                              1880ECAS1-100G                     2 ea
           1 pair fuse CIRCA                                  4B1E                            200 ea
           etc.
           etc.
           etc.
           Labor Man Hours                                                                      72 hr

      G. Warranty
         This should include the name of the manufacturer from which the State will receive the warranty
         and the type and length of the warranty or warranties provided with the cabling solution that is
         proposed. 25 years is required.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 64 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

PART 26   APPENDIX G – OUTSIDE PLANT – DELDOT SPECIFIC REQUIREMENTS –
TRAFFIC CONSTRUCTION

      A. DELDOT FIBER INSTALLATION OVERVIEW
            • Varied Distances
                  o 200 ft -65km
            • Locations
                  o Highways/Roadway
                  o Buried conduit
                  o Pole Line
            • Typical installation methodology & work to include
                  o Backhoe work
                  o Trenching/directional boring
                  o conduit
                  o hand holes
                  o Vaults
            • DelDot Mandated Safety standards
                  o OSHA – Occupational Safety & Health Administration
                  o All Delaware road work safety requirements shall be in accordance with the DelDOT
                       Manual on Uniform Traffic Control Devices (MUTCD) for Streets and Highways –
                       Part 6 Temporary Traffic Control.
            • DelDot Project Initiation Timeframes
                  o Safety is priority one for all DelDOT projects – no road work will not be authorized
                       without following the proper safety precautions and DelDOT safety approval. It
                       some situations, DelDOT requires 2 week notice prior allowing road work to begin.
      B. Deldot Singlemode Fiber Specifications & Purchasing requirements
                •   All fiber and splicing work must meet/exceed specification of Standards Bodies:
                          o ANSI -American National Standard Institute
                          o EIA/TIA -Electronic Industries Associations/Telecommunications Industry
                              Association
                                  ▪ Structured cabling systems for commercial buildings
                          o NECA - National Electrical Contractors Association
                          o BICSI – Building Industry Consulting Services Internation
                          o State of Delaware and Local standards & code
                          o ANSI TIA/EIA 758 (latest reference) Outside Plant Customer Owned
                              Telecommunications Standard
                •   Fiber Cable Certification
                        o Vendors must provide documentation, on a per job basis, written certification that all
                            cables and services supplied as a result of this solicitation meet all current
                            applicable ANSI EIA/TIA specifications and BICSI Guidelines
                        o Testing methodology per section “Deldot Fiber Testing Requirements”
                        o In order to adhere to warranty specifications and to standardize on cable
                            specifications, the Delaware Department of Transportation has standardized on
                            Corning fiber optic cable, which requires installation by a Corning EWP (Extended
                            Warranty Program) Partnering Company. Also accepted are Sumitomo, Hubbell,
                            and Fiber Connections.
      C. DelDot Fiber Testing Procedure and Minimum Accepted results
            • Single Mode Fiber
                    o Maximum Bend Radius
                            ▪ Conductive cable - 15 times the cable’s outside diameter when being pulled
                            ▪ Nonconductive cable – 10 times the cable’s outside diameter when under no

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 65 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

                                     load and 20 times the outside diameter when being pulled
                        o    Fiber Connector Type
                                 ▪ LC connectors – DOT standard is LC only
                        o    OTDR Testing & Results
                                 ▪ Anritsu –CMA 5000 or equivalent
                                 ▪ Power meter – Corning OTS 600 Series Power Meter & Light Source or
                                     Equivalent
                                 ▪ Maximum Loss
                                          • Optical fiber attenuation factor 1.5 dB/km standard limit, (e.g., TIA-
                                             568-C.3)
                                          • Connector Coupling loss .75 dB/pair standard limit, (e.g., TIA-568-
                                             C.3)
                                          • Fiber splice insertion loss .03 dB standard limit (e.g., TIA-568-C.3)
                                 ▪ Utilize an optical fiber link transmission performance calculation worksheet
                                     to determine acceptable loss within specified run
                        o    Splicing Requirements
                                 ▪ Fusion splice according to the manufacturer’s instructions.
                                 ▪ Secured by a splice closure containing splice trays in groups of 12 or 24
                                     fiber
                                 ▪ DelDOT has standardized on the 3M Brand splice cases.
                        o    Termination
                                ▪ Rack mounted enclosures are primary in the fiber hub and facilities and
                                    mounted on 19 Inch Racks
                                ▪ Pre-terminated Zuse Panel from Corning, Sumitomo, Hubbell or
                                    equivalent are used for device termination
                                ▪ Wall mounted enclosures with Rack mounted patch panels are used only
                                    when specified by the Fiber Committee.
                                ▪ DelDOT has standardized on Corning components for patch panels,
                                    enclosures and all related equipment or similar products from
                                    Sumitomo, Hubbell, or Fiber Connections equivalent.
                                ▪ Factory terminated duplex jumpers comply with optical fiber performance
                                    specifications of applicable standards (i.e., ANSI/TIA-568-C.3)
                        o    Administration
                                ▪ Adherence to the Outside Plant Fiber Optic Naming Convention provided by
                                    DelDOT Document available upon request.
                                ▪ Deliverables – this document is attached, please reference ####.
      D. Outside Plant Pathway
                •   Construction Of Outside Plant Pathway
                           o Shall be in accordance with ANSI TIA/EIA 758 (latest reference) and BICSI
                                Outside Plant-Customer Owned Manual and Telecommunication Distribution
                                Methods Manual.
                           o Maintenance Hole (Manhole) access – OSHA trained Confined space training
                           o The department requirements contact to One Call before any digging.

                •   Inner duct
                            o Qty 4 – 1” corrugated inner duct is required within 4” PVC or HDPE conduit with
                               a pull cords and 12 gauge solid tracer wire
                            o All inner ducts will be sealed with rubber inner duct plugs
                •   Conduits
                           o       All Conduit installed unless otherwise designated is 4 inch
                           o       Inside buildings, cabinets, Hubs, Telephone pole, Signal Poles or Maintenance
                                   holes and hand holes, end of conduits are to be sealed with rubber conduit
                                   plugs, water plug or duct sealer.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 66 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

        E. Product Substitution

                •   All items or services delivered during the life of the contract shall be of the same type and
                    manufacture as specified or accepted as part of the State’s contract.
                •   The Dept. of Transportation can change specification or vendors of equipment as a benefit
                    to the state.
                •   Vendors are encouraged to offer any like substitute product (s), either generic or brand
                    name for evaluation especially if an opportunity for cost savings to the state exists. The state
                    requires the submissions in writing with specifications and/or product samples for evaluation
                    prior to any approvals being granted.
        F. Highway Safety

                        •    Safety is priority one for all DelDOT projects – no road work will not be authorized
                             without following the proper safety precautions and DelDOT safety approval. It
                             some situations, DelDOT require 2 week notice prior allowing road work to begin.

 Deliverables and long term administration of the Fiber Optic Program for Delaware
                           Department of Transportation
The department of Transportation uses federal funds to provide most of the fiber requirements throughout
the state of Delaware. Because the FHWA has more stringent requirements about the use of federal funds,
the Department of Transportation Fiber Committee has put together a tasking and processing method that
covers the requirements of federal reporting, Federal Audits as well as state audits. These additional
deliverables are added to the cost of implementation and are covered as a line item in the proposals.
Fiber Tasks for the Department of Transportation

    -     The process for fiber implementation starts with the design phase and can take years to implement
          or even get funded. Starting at the design level, the department’s fiber committee helps to insure
          that all the designs cover the fiber requirements as they pertain to the department’s overall strategic
          plan. It also considers ease of repair, ease of redirection and cost.
    -     The fiber contractor is responsible for providing quotes for specific requirements as determined by
          the department’s fiber committee and the engineering department. The requests come in a formal
          packet that has a logical design, the footages and parts to be used for the implementation. The fiber
          contractor produces a quote in the format dictated by the department which includes a narrative of
          the request and a spreadsheet break out of the components to be used - to include all parts being
          used and the labor it will take to produce this final product. Examples may be requested if
          necessary.

    -     Once the Quote is received it is processed with the department’s final design and then awaits
          funding. In some instances this may be weeks. In some instances this funding may never occur.
Fiber Contractors Role

    -     The contract as stated above will provide the department with quotes for specific tasks. When given
          a Notice to Proceed from the Departments Fiber Committee the task is deemed funded and the work
          will be schedule as described in the sections above.
    -     There are several different scenarios that drive the department’s fiber program and requires flexibility
          on the Fiber contractor’s part. Some of these issues are discussed below in more detail. The use of
          sub-contracts, the need for minor underground construction, tasks that encompass a fair amount of
          safety requirements due to the location of the sites that are being worked. I.E. I95, SR1 and bridge

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 67 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

         work. As a rule most conduits and underground will be in place when the task is requested. There
         are times when that is not the case and underground construction will be required. Most of the time
         we are working outside but occasionally we will need to terminate and facilitate indoor facilities
         throughout the state.
Emergency Requirement

    -    Daytime call out is a common emergency where the fiber optic in the state has been impacted or
         severed by construction from the department or from a third party. There are times when it is
         considered an emergency when the fiber that was close to a project is not impacted, but discovered
         that it needs to be pulled out of the way and then re-instated. These types of call-outs are less
         frequent but not uncommon.
    -    Night Time and weekend call outs usually happen for some of the same reason, and can include
         weather events that cut the fiber or a tree falling, etc.. There are a few scenarios where this type of
         call-out is necessary.

    -    The fiber contractor must be able to be in contact with the representative from the state within a two
         hour time frame, 24 hours a day, seven days a week. The department also expects the contractor to
         be on site with their equipment, in four hours.
Deliverables

         Logical Drawing vs. As Built. As a deliverable of a finalized task, the department requires what we
call a logical. These are in Visio format and are incorporated into the master documentation of the
departments overall fiber documentation. These are not to scale, but do require more detail from a fiber
perspective than an as-built. As-builts, we consider to be markups of the original designs with field notes
that show any deviation from the original task/ proposal. We do not require a formal as-built but we are not
always able to inspect every aspect of the task. If the fiber contractor discovers that the field work deviates
from the design, this should be reflected in the field notes, and if easier to explain, in a drawing or a markup
of the logical or the as-built.
Note: Incorporation of Logical Drawings – The department’s fiber committee will review the logical, provide
the quality control function, ask for more detail or clarification if needed, and incorporate the final product into
the corridor of the state road information system.
     - GPS information – is required from the fiber vendor. This information should be provided to the
         department in an .mdb format, and include all information as it pertains to the conduit, the fiber, the
         compass direction, the wells, and intelligent devices. The department will provide the data dictionary
         for the collection of this information.

The department uses Trimble handhelds for the collection of the data in conjunction with Pathfinder and
TerraSync software by Tremble. Both the GPS unit and the software necessary to use it, including the
pathfinder licenses and TerraSync licenses, are the responsibility of the contractor.
    -    ODTR information is provided to the state in the deliverable package and will be reviewed during the
         quality control process. Failures of fiber strands, for any reason, in the field are unacceptable unless
         otherwise directed by the fiber committee.

    -    Power Meter Data is provided to the state in the deliverable package and will be reviewed during the
         quality control process. Failures of fiber strands, for any reason, in the field are unacceptable unless
         otherwise directed by the fiber committee.
    -    Packing Slips – all equipment bought for a specific task will have packing slips. The department is
         required to collect and store copies of these slips for the purpose of audit. Any deliverables
         packages that do not contain all of the deliverable elements will be rejected.

    -    Warranty Information – all warranty information as it pertains to the purchases of equipment for a specific
         task will be provided to the state in this deliverable package. This is to include the Corning, Sumitomo or
         Hubbell Cabling System, 25 Year guarantee for all projects.

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 68 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

    -    Field Notes and Drawings will be digitized/ scanned and provided in the deliverable package.

    -    Final inspection – although this is not a physical deliverable, no deliverable package will be
         considered for payment or quality review until a final walk through has taken place.
Deliverable Review

    -    Fiber Committee Review – all deliverables go through the fiber committee for final review and quality
         control.
    -    If there are any omissions or information needs to be clarified or re-surveyed, the committee will
         provide the vendor with the request and the payment/ invoice will be put on hold until the requested
         information is re-submitted.

    -    Once the new information has been received the fiber committee will review the information and
         process payment if all deliverables meet the department’s requirements.
Final Documentation Submission
    -    Media
            o Directory Structure – all deliverables will be provided to the state in a directory structure
               provided by the department’s Fiber Committee.
            o The information can be provided on a CD/DVD or Jump drive, which will be filed with the
               invoice information and not be returned.
    -    Invoice
             o Submission – Invoice submission should be to the chair of the department’s fiber committee
             o Payment – payments are processed when all deliverables are met unless otherwise
                 designated by the department’s fiber committee
             o Re-submission – in some cases there is a need to request a re-submission due to cost
                 changes or LCope changes. All changes in invoicing should have a valid change
                 request deLCribing the need for the change in LCope or cost. These forms are
                 generated by the department’s fiber committee and signed by the fiber contractor.
Invoicing
    - Once the department’s fiber committee has processed the deliverables and the invoice has been
        checked for accuracy, the invoice is submitted for payment by the department’s fiber committee
        chair.
    - All information is filed and stored for review both physically and electronically.

PART 27           APPENDIX H - CERTIFIED CONTRACTOR LIST

 Certified Contractor List (search for GSS21441A-DATA_CBL)

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directedto dti_tasc@delaware.gov

Page 69 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

                                                            DELAWARE STATE-WIDE INFORMATION
                                                      TECHNOLOGY AND ARCHITECTURE STANDARDS

PART 28           APPENDIX I – Approved Equivalent Vendors
26P

Approved Vendors
   • Belden
   • Mohawk

PART 29           Development and Revision History
26P

  Date                     Revision
  1/29/2021                Rev 8 – current version
  11/1/2024                Rev 8 - Removed references to the Technology Investment Council and
                           added a clarification in the Process section

These standards are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture Standards
Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any questions or comments
should be directed to dti_tasc@delaware.gov

Page 70 of 69           8/9/2016                11:54:59 AM                   CablingandWiringStandard-State.doc

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
