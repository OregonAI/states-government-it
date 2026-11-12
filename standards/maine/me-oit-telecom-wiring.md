---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-telecom-wiring
title: Telecommunications Facilities and Wiring Specifications
doc_type: standard
citation: MaineIT Telecommunications Facilities and Wiring Specifications
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/WiringSpecs.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: a4e27586e086c7e77f6b387b06b35363c8f4feac8935189c631ae1fe6f9c6f30
effective_date: null
source_version: REVISED JANUARY 2024
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). Pages 45 of the PDF have no text layer (figures, blank pages or scanned forms) and add no
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Telecommunications Facilities and Wiring Specifications (MaineIT Telecommunications Facilities and Wiring Specifications)

## At a glance

OIT Network Services Division specifications for State telecommunications facilities and structured cabling.

## Full text

        STATE OF MAINE
        TELECOMMUNICATIONS
       FACILITIES & WIRING
          SPECIFICATIONS

OFFICE OF INFORMATION TECHNOLOGY(OIT)
   NETWORK SERVICES DIVISION (NSD)

          REVISED JANUARY 2024

      THIS PAGE INTENTIONALLY LEFT BLANK

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     1

         *** PLEASE READ THIS PAGE THOROUGHLY ***

THESE SPECIFICATIONS SHALL APPLY IN ALL INSTANCES WHERE THE STATE OF
MAINE IS, OR MAY BECOME, THE OWNER OF THE PREMISES, OR WHERE THE STATE
OF MAINE IS, OR MAY BECOME, A LESSEE OF THE PREMISES OR A PORTION
THEREOF.

ALL PLANS, SPECIFICATIONS, DRAWINGS, AND TECHNICAL INFORMATION
CONCERNING TELECOMMUNICATIONS MUST BE REFERRED TO, AND APPROVED
BY, THE STATE OF MAINE, OFFICE OF INFORMATION TECHNOLOGY (OIT),
NETWORK SERVICES DIVISION, BEFORE PROCEEDING WITH BIDDING OR
CONSTRUCTION.

ALL STATE-ADMINISTERED PREMISES, TELECOMMUNICATIONS, SWITCHING
SYSTEMS, STATION EQUIPMENT, TERMINAL, TELEPHONY AND COMPUTER
NETWORK DEVICES, WIRING AND THEIR INSTALLATION, SHALL BE PROVIDED BY
THE STATE OF MAINE, OFFICE OF INFORMATION TECHNOLOGY, NETWORK
SERVICES DIVISION. UNLESS OTHERWISE INDICATED OR ARRANGED THROUGH
LEASE OR OTHER AGREEMENT WITH THE STATE, ALL OTHER RELATED PREMISES
WORK SHALL BE THE RESPONSIBILITY OF THE CONTRACTOR AND/OR THE
LESSOR, IN ACCORDANCE WITH THESE SPECIFICATIONS AND OTHER RELATED
PROJECT-SPECIFIC PLANS AND DOCUMENTS APPROVED BY THE OFFICE OF
INFORMATION TECHNOLOGY.

UNDER NO CIRCUMSTANCES SHALL ANY TELECOMMUNICATIONS EQUIPMENT
ROOMS, WIRING CLOSETS, CONDUITS, RACEWAYS, POWER SUPPLIES, WIRING AND
SPECIAL EQUIPMENT BE UTILIZED FOR ANY PURPOSES OTHER THAN APPROVED
TELECOMMUNICATIONS AND OTHER RELATED SERVICES SPECIFICALLY
AUTHORIZED BY THE STATE OF MAINE, OFFICE OF INFORMATION TECHNOLOGY,
NETWORK SERVICES DIVISION.

THE STATE OF MAINE, OFFICE OF INFORMATION TECHNOLOGY, RESERVES THE
RIGHT TO CHANGE ANY OR ALL OF THESE SPECIFICATIONS WITHOUT NOTICE.
IT IS THE RESPONSIBILITY OF OWNERS, ARCHITECTS, CONTRACTORS, OR ANY
OTHERS CONCERNED, TO CONSULT WITH THE OFFICE OF INFORMATION
TECHNOLOGY FOR SPECIFICATION UPDATES, CHANGES AND/OR PROJECT PLAN
DEVELOPMENT.

        STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                   TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                         REV 7.1-01/2024
                                             2

                                TABLE OF CONTENTS

Section A Telecommunications                                                               4

Section B Service Entrance                                                                 14

Section C Telecom Switch Room (MDF)                                                        17

Section D Telecom Wiring Closets (IDF)                                                     23

Section E Basic Cable/Wiring Standards                                                     26

Section F Cable Television (CATV)                                                          31

Section G Paging Systems                                                                   34

Section H Video Systems                                                                    35

Section I Mechanical Equipment                                                             36

Section J Fiber Optic Cable Systems                                                        37

Section K Removal of Old Cable and Facilities                                              41

Section L Cutting and Patching                                                             42

Section M Temporary Utilities                                                              45

Section N Painting and Cleanup                                                             46

Section O Special Services and Facilities                                                  47

Appendix     Jack Wiring and Facilities Diagrams                                           48

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                3

                     SECTION A - TELECOMMUNICATIONS

A.1.   General

       Furnish and install all telecommunications jacks, outlets, conduits, raceways, ducts, cables,
       electrical wiring, electrical outlets, backboards, racks, air conditioning, flooring, sensors,
       alarms, and allied accessories, in accordance with any applicable specifications and
       drawings, and the specifications contained herein. Relocate or remove, as required, any
       existing jacks, outlets, conduits, raceways, ducts, cables, equipment, etc., due to
       architectural changes, or as shown on any applicable drawings, if such materials are not
       reused in the construction, or do not meet the specifications set forth herein.

A.2.   Included and Related Requirements

       Basic telecommunications requirements of this Division shall include, but shall not be
       limited to that which is described in the subsequent sections of this document as follows:

       Included Work

       Section B      Service Entrance
       Section C      Telecom Switch Room (MDF)
       Section D      Telecom Wiring Closets (IDF)
       Section E      Basic Cable/Wiring Standards
       Section F      Cable Television (CATV)
       Section G      Paging Systems
       Section H      Video Systems
       Section I      Mechanical Equipment
       Section J      Fiber Optic Cable Systems

       Related Work

       Section K      Removal of Old Cable and Facilities
       Section L      Cutting and Patching
       Section M      Temporary Utilities
       Section N      Painting and Cleanup
       Section O      Special Services and Facilities

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 4

                     SECTION A - TELECOMMUNICATIONS

A.3.   Definitions

       The following terms are defined as they are used and applied in the text of this document,
       and any accompanying or related text and/or drawings and sketches.

              1. Backboard: A section or sections of wall-mounted plywood, ¾-inch thickness,
                 on which telecommunications devices, fixtures and related equipment will be
                 mounted.

              2. “Category 5E”; “Category 5 Enhanced”: Terms that refer to
                 telecommunications cable, terminating hardware and installation practices that
                 exceed the specifications for “standard” Category 5 cable and terminating
                 hardware, according to EIA/TIA requirements and specifications for such
                 cable, terminating hardware and installation practices.

                  This is cabling standard is deprecated for installation in State owned or leased
                  premises. By current standards, previous Categories are obsolete and are no
                  longer to be installed in State owned or leased premises.

              4. “Category 6”: Terms that refer to telecommunications cable, terminating
                 hardware and installation practices that meet EIA/TIA requirements and
                 specifications for such cable, terminating hardware and installation practices.

                  This is the current general cabling standard for State owned or leased premises.

              5. CATV (Common Antenna Television): An acronym generally used in reference
                 to “cable television” cable, hardware, systems and services.

              6. Certified: Equipment is “certified” if it has been tested and found by a nationally
                 recognized testing laboratory to meet recognized standards, or to be safe for use
                 in a specified manner or application, and bears a label, tag, or other record of
                 such certification.

              7. CLEC (Competitive Local Exchange Carrier): See “LEC”.

              8. Coax; Coaxial Cable: A special two-conductor cable in which there is a solid
                 metallic “inner” or core conductor, covered by a flexible insulating dielectric
                 material over which is placed a tubular solid or woven metallic “outer”
                 conductor which shares a common radial axis with the inner conductor. The
                 outer conductor of the coaxial cable is generally sheathed with a protective
                 PVC, TFE, or polyethylene overall insulation. Associated with the cable is a
                 specific ohmic impedance value, which is a function of the inner and outer
                 conductor diameters and their radial separation through the dielectric. This
                 cable has a relatively wide signal bandwidth.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                5

         SECTION A - TELECOMMUNICATIONS

  9. CMP (Communications Plenum) Cable: An electrical, telecommunications, or
     any other type of cable bearing a special insulation and sheath which conforms
     to NEC and other related safety codes and standards for suppressing the release
     of noxious gas or toxic smoke when such cable is subjected to heat and flames.
     This cable is used in an unprotected environment (not in conduit), within any
     areas used for the ducting or transport of environmental air within or to any
     building or space designed for human occupation (Article 800, National
     Electrical Code).

  10. Conduits: Piping or tubing used to encase telecommunications or other cables.
      There are four basic types of conduit, listed below, which are acceptable in
      specific instances:

                  a. S&D (Soil & Drain), PVC or HDPE (non-metallic);
                  b. Schedule 40 or 80 PVC (non-metallic);
                  c. EMT, a thin walled, steel electrical conduit;
                  d. Rigid, a heavy walled, solid, threaded, steel conduit.

  11. Connecting Block:          A telecommunications industry series of
      telecommunications cable termination/connection “blocks” used to organize,
      terminate and hold twisted pair wires and to provide a “cross-connect” point
      between such termination points of telecommunications cables.

  12. Cover Plate: Also known as “face plate”. A special duplex electrical outlet box
      cover which mounts to the front of such a box, and which is designed to carry
      associated telecommunications outlet modules which ‘snap in” to such plate.
      These plates are typically designed to accommodate 2, 3, 4 or 6
      telecommunications outlet modules.

  13. Demarcation Point: The point at which the RBOC/CLEC/ILEC terminates its
      incoming service facilities within the premises. This may also be referred to as
      “handoff”.

  14. Distribution/Cross Frame: A special frame or backboard which is used to
      receive telecommunications cables from a telecommunication switching system
      and/or incoming lines from the RBOC/CLEC/ILEC, and which facilitates the
      cut-down, termination and connection points of the telecommunications cables
      for distribution to terminal devices.

  15. Duplex Electrical Box: A standard electrical outlet box which is typically
      fastened to a building wall stud for the flush placement of a duplex (2 outlet)
      electrical receptacle. It can also be used to flush mount telecommunications
      jacks and CATV outlets designed to fit into such a box.

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     6

         SECTION A - TELECOMMUNICATIONS

  16. EIA/TIA (Electronics Industry Association/Telecommunications Industry
      Association): A nationally recognized engineering standards body of
      electronics and telecommunications professionals, manufacturers, vendors, and
      end-users, which sets various technical and manufacturing standards and
      specifications for electronic and telecommunications systems and equipment.

  17. Face Plate: See “Cover Plate”.

  18. Fiber Optics (Optical Fiber): In this context, either individual or multiple single-
      mode or multi-mode glass fiber cabling systems, which transport
      telecommunications signals in the form of high frequency light pulses.

  19. Fiber Optic Cable: A special telecommunications cable which contains one or
      more optical glass fibers, each of which is covered with an identifying color-
      coded sheath, and all of which are covered with an overall sheath containing a
      structural strength member of Kevlar or similar material. It generally will
      contain no metallic structure or elements.

  20. Fiber Optic Connector: A connector that is fastened to individual optical fibers
      through adhesive, heat or mechanical means. The connector provides a means
      to couple the optical fiber to termination panels and/or equipment using optical
      fiber interfaces. Fiber optic connectors are found in numerous coupling
      configuration designations such as LC, MTRJ, SC and ST, with LC and SC
      being the predominant couplings for optical fiber cable termination.

  21. Fiber Optic Terminal: A wall or rack mounted enclosure designed for the
      termination of fiber optic cable, and which provides a connection point for
      cross-connecting fibers or for connecting electronic fiber optic
      transmitting/receiving equipment to the fiber optic cable.

  22. Gas Tube Protection: A 3-element gas tube protection device, installed in series
      between the telecommunications cable and the equipment frame, jack or
      telecommunications outlet, and designed to protect the telecommunications
      equipment from electrical surges or spikes entering the telecommunications
      cable system, such as may be encountered during an electrical storm. This type
      of protection device is typically installed on a cable protection terminal in which
      the cable is terminated, on each pair of conductors within the cable that provide
      “POTS”-type service. Because of the higher voltage rating of these devices,
      they should not be used on cable pairs which service digital terminal or
      communications equipment.

  23. Gauge: A term used to describe the physical diameter of a copper wire
      conductor, as defined by American Wire Gauge (AWG) standards.

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     7

         SECTION A - TELECOMMUNICATIONS

  24. Ground: (1) An electrical reference to earth potential; (2) Electrically
      connecting or bonding a conductor or conductive surface, such as
      electrical/electronic equipment frames, equipment racks/shelves, gas tube or
      solid-state protection frames, cable shields, etc. to an electrical ground.

  25. ILEC (Incumbent Local Exchange Carrier): See “LEC”.

  26. Innerduct: A flexible, corrugated polymer tubing, often orange in color, in
      which fiber optic cable is placed. It is used for the separation and protection of
      the fiber optic cable from other cables using the same conduit, raceway, riser
      shaft, etc.

  27. Intermediate Distribution Frame (IDF): In a relatively large building, or a
      building with multiple floors, this is a space, closet, or room where station
      cables will be terminated for a given area within the building. It will also serve
      as a termination point for IDF-to-MDF “riser” cables, including copper, fiber
      optic, and CATV cables. This space, closet or room may also house electronic
      switching, amplification and distribution systems for data LAN’s, video and
      CATV systems. This may also be referred to as “wiring closet”.

  28. Key System (KSU): A relatively small electronic telephone switching system,
      which is typically used in a small office environment, and usually
      accommodates 8 or less RBOC/CLEC/ILEC service lines and 24 or less
      telephone sets. By current standards, KSUs bear limited usage and are
      generally considered obsolete.

  29. Labeled: Equipment is “labeled” if it bears a valid label, seal, or symbol of a
      nationally recognized testing laboratory, such as Underwriters Laboratory, Inc.,
      recognizing its acceptability for the intended uses in these specifications.

  30. LEC (Local Exchange Carrier): The local servicing public telephone or
      telecommunications service company or provider. This may also be referred to
      as CLEC (Competitive LEC) or ILEC (Incumbent LEC).

  31. Listed: Equipment is “listed” if it is of a kind mentioned in any document,
      published by a nationally recognized laboratory which makes periodic
      inspections during production of such equipment, and states that such
      equipment meets nationally recognized standards, or has been tested and found
      safe for use in a specified manner.

  32. Main Distribution Frame (MDF): A space, closet or room which serves as the
      central telecommunications cable and service distribution point for a premises.
      It will generally house the primary telecommunications voice, data, video, fiber
      optic, and CATV switching and distribution systems. It will serve as the
      connection point to RBOC/CLEC/ILEC services, the common termination

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     8

         SECTION A - TELECOMMUNICATIONS

      point for IDF-to-MDF riser cables, including copper, fiber optic, and CATV
      cables, and will be the primary point for inter-building and intra-building cable
      cross-connections. This may also be referred to as “switch room” or “main
      wiring closet”.

  33. POTS: An acronym for “plain old telephone service”, that being the type of
      service typically offered to the general public and having the technical
      characteristics of such service. It may also be referred to as “analog line”.

  34. Power Pole: Typically, a square or rectangular duct associated with modular
      furniture installations, which attaches to and extends vertically from such
      furniture through the ceiling and affords a path for the extension of electrical
      and/or telecommunications cables into such furniture. This may also be
      referred to as “tele-pole” or “com-pole”.

  35. PBX (Private Branch Exchange): A generic term for an electronic
      telecommunication switching system.

  36. Quad Electrical Box: A standard electrical outlet box, which is typically
      fastened to a building wall stud, and is designed for the flush placement of two
      duplex (2-outlet) electrical receptacles. It can be used to flush mount
      telecommunications jacks designed to fit into such a box.

  37. RBOC (Regional Bell Operating Company): An essentially obsolete term used
      to designate the local ILEC, that typically being a descendant of the former Bell
      System, a provider of public telephone/telecommunications services.

  38. Riser Cable: Generally, a telecommunications cable of 25 or more copper pairs
      which runs between and terminates in the IDF and MDF spaces of a premises
      and affords telecommunications service transport between such spaces. It may
      also be referred to as “vertical cable”.

  39. Solid-State Protection: A semiconductor protection device, installed in series
      between the telecommunications cable and the equipment frame, jack or
      telecommunications outlet, and designed to protect the telecommunications
      equipment from electrical surges entering the telecommunications cable
      system, such as may be encountered during an electrical storm. This type of
      protection device is typically installed on a cable protection terminal in which
      the cable is terminated, on each pair of conductors within the cable. Solid-state
      protection devices are available in various voltage ranges and should be selected
      and installed to meet the specific operational parameters of telecommunications
      equipment being attached to the cable, i.e., equipment with “POTS”-type
      (analog) line interfaces or digital line interfaces.

  40. Station Equipment: See “Terminal Devices”.

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     9

         SECTION A - TELECOMMUNICATIONS

  41. Station Cable: Generally, a telecommunications cable of 4 pairs which runs
      between and terminates within the IDF/MDF space and the telecommunications
      jack. This may also be referred to as “station wiring” or “horizontal cable”.

  42. Switch Room: A generic term for a telecommunication switching equipment
      room or space and is usually the room in which the MDF and
      telecommunications switching system and ancillary equipment are located.

  43. Telecommunications Cable: A combination of two or more twisted-pair copper
      wire conductors, which are grouped or bundled in a protective overall jacket or
      sheath. Each conductor is insulated and color coded with a specific colored
      insulating material. Cables containing more than 25 pairs shall be fabricated
      such that specific groups of 25 pairs each, otherwise known as “binder groups”
      are formed and can be recognized as such through industry-standard color
      coding of the groups.

  44. Telecommunications Jack: A fixture which generally combines 2, 3, 4 or 6
      modular telecommunications outlets into a standard duplex electrical box, a
      quad electrical box, a self-contained surface mount fixture, or a portable
      furniture panel fixture. The voice and data outlets are physically similar (8-pin
      modular-style) and other outlets are specific to their function (coaxial, fiber
      optic).

  45. Telecommunications Outlet: An 8-conductor modular-style device which
      terminates the telecommunications station cable at the station end, and allows
      for telecommunications equipment attachment to the station cable via an
      attachment cord. Unless otherwise noted, voice and data outlets shall conform
      to EIA/TIA 568B Category 6 specifications.

  46. Terminal Device: A generic term for a telephone, facsimile, data device, printer,
      or other telecommunications equipment, connected by telecommunications
      cables or wiring.

  47. Transient Voltage Protection:        See “Gas Tube Protection”, “Solid-State
      Protection”.

  48. Twisted-Pair: One pair of single-conductor copper wires, each wire encased in
      its own colored insulation, and twisted around one other in a spiraling fashion
      at no less than six revolutions or 360 degree “twists” per foot of length.
      Insulation material composition and exact twist geometry shall be dictated by
      the EIA/TIA Category certification requirements and cable manufacturing
      methods.

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     10

         SECTION A - TELECOMMUNICATIONS

  49. Uninterruptible Power System (UPS): A special power system installed
      between the commercial electrical source and telecommunications equipment
      which requires uninterrupted electrical power service. These systems are
      generally self-contained with an internal battery array. In normal operation, the
      UPS will condition and pass commercial power to the attached equipment,
      when such power is available and suitable for use. It will switch to internal
      battery power generation upon loss or degradation of the commercial power
      service, all without interruption of power service to the attached equipment.

  50. Voice Over Internet Protocol (VoIP): A telephony service technology whereby
      telephones are connected to the data network rather than through use of legacy
      technologies such as POTS or ISDN. VoIP sets afford the use of the
      desktop/workstation data jack for connectivity of both a telephone and a
      computer workstation through a single data jack, thus, in many cases
      eliminating the requirement for individual voice and data jacks at the
      desktop/workstation.

  51. Whip: Typically, a section of flexible PVC electrical conduit with connector
      fittings, associated with modular furniture installations, which attaches between
      such furniture and a “hard” wall, and affords a path for the extension of
      electrical and telecommunications cables into such furniture.

  52. Wiring Closet: A space, closet, or room where station cabling will be terminated
      for a given area within the building. It will also serve as a termination point for
      IDF-to-MDF “riser” cabling, including copper, fiber optic, and CATV cables.
      This space, closet or room may also house electronic switching, amplification
      and distribution systems for data LAN’s, video and CATV systems. This may
      also be referred to as “IDF”.

  53. 66 Block: An older style twisted-pair cable termination/cross-connect block
      which uses exposed split metal posts or tabs to capture the wire conductor end
      and provide an electrical path to another similar wire conductor, thereby
      facilitating a “cross-connect”. By current standards, 66 blocks bear limited
      usage and are generally considered obsolete.

  54. 110 Block: A newer style twisted pair cable termination/cross connect block
      which uses a series of “captive caps” with integrated recessed conductor tabs.
      The “bottom” of the captive cap terminates the pairs of a given cable into the
      bottom of its conductor tabs. The “top” of the cap provides captive “grooves”
      for the termination or “punch-down” of another cable into the top of its
      conductor tabs, thereby facilitating a “cross-connect”.

  55. 110-JP Block: A specially designed 110-style termination or “punch-down”
      block which has integral 8-conductor modular (RJ-45 style) receptacles to
      facilitate direct connection of data equipment to the block via a “patch cord”.

STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                 REV 7.1-01/2024
                                     11

                     SECTION A - TELECOMMUNICATIONS

                  These blocks are generally used in an IDF, MDF, or a computer/data equipment
                  room where multiple connections are concentrated. Single blocks are typically
                  available with modular receptacle counts of 12 or 36. By current standards, 110-
                  JP blocks are considered obsolete.

              56. Cover: The shortest distance between the top surface of any direct-buried
                  conductor, cable, conduit or other raceway, and the top surface of finished
                  grade, concrete, or similar cover (see NEC 300.5).

              57. APWA: American Public Works Administration. The APWA Uniform Color
                  Code is a universal marking guideline for underground utilities and locators.

A.4.   Product Criteria

       1. Products used in construction projects shall be the standard products of a manufacturer
          regularly engaged in the manufacture of those products.

       2. Unless approved by the Network Services Division, items of equipment shall
          essentially duplicate equipment that has been in satisfactory use in the industry for at
          least five years.

       3. Products shall be supported by a service organization which maintains an adequate
          inventory of repair parts and is located reasonably close to the site.

       4. When two or more units of materials or equipment of the same type or class are
          required, they shall be products of the same manufacturer.

       5. All factory wiring of pre-assembled components shall be accompanied by wiring
          diagrams.

A.5.   Miscellaneous

       1. Safeguarding Materials/Work Areas: Responsibility for the safeguarding, care, and
          protection of all materials and work rests with the contractor until the entire project has
          been completed, tested, and accepted.

       2. Regulatory Requirements: All work shall conform to the requirements of all applicable
          codes, laws, regulations, local ordinances, and contractors shall cooperate with all
          authorities having jurisdiction. Compliance with laws and regulations on this project
          does not relieve the contractor from compliance with more restrictive requirements
          contained in these specifications.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 12

              SECTION A - TELECOMMUNICATIONS

3. Permits, Fees, and Inspections: The contractor shall secure and pay for all permits,
   fees, inspections, street opening charges, “DigSafe” and any fines assessed in
   connection with this project.

4. Warranties: Any manufacturers’ warranties shall be passed on to the owner at the
   completion and acceptance of the project. The Contractor shall warrant all material and
   workmanship to be in compliance with these specifications, according to standards
   acceptable to the Architect/Engineer and/or the industry. The Contractor shall also
   warrant their installations to be free of defects in both materials and workmanship for
   a period of one year, or longer if specifically called for in the general policies section
   of the specifications dealing with the entire project.

    STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
               TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                     REV 7.1-01/2024
                                         13

                         SECTION B - SERVICE ENTRANCE

B.1.   General

       Furnish all labor, materials, equipment, supplies and perform all operations necessary to
       complete the service entrance work, in accordance with the applicable project drawings
       and these specifications. Furnish “as built” telecommunications drawings at the completion
       of the project.

B.2.   Point of Entry

       The entrance to the premises shall be at a point mutually acceptable to the owner and the
       RBOC/CLEC/ILEC, which usually is a point closest to the current facilities of the
       RBOC/CLEC/ILEC.

B.3.   Entrance Methods

       1. Buried: From the designated entrance point of the RBOC/CLEC/ILEC facilities, there
           shall be conduit(s) buried at a minimum cover depth of 24 inches, using Schedule 40
           or 80 PVC pipe. In areas subject to vehicular traffic, the conduit(s) shall be
           encapsulated in concrete to a minimum thickness of 3 inches, running the full length of
           the traffic area. In all areas where public streets are crossed, rigid steel conduits shall
           be used. Trenches shall be backfilled according to NEC 300.5(F); backfill shall be free
           of large rocks, paving materials, cinders, large or sharply angular substances, or
           corrosive material where these materials may damage conduits or cables or prevent
           adequate compaction of fill or contribute to the corrosion of the conduit system. Where
           necessary to prevent physical damage to the conduits and cables, protection shall be
           provided in the form of a 6-inch base layer and a 6-inch top layer of a granular material
           such as sand. Marking tape meeting the APWA Uniform Color Code and appropriately
           labeled, i.e. “Caution Buried Fiber Optic Line, or Caution Buried Telecom Line” shall
           be installed during backfill operations of underground installations. All conduits shall
           be capped after installation to protect them from weather elements and debris. Unless
           otherwise specified, the minimum size and count for building service entrance conduits
           shall be as follows:

                      a. Up to 40,000 sq. ft. floor space, one 4-inch diameter;
                      b. Over 40,000 sq. ft. floor space, two 4-inch diameter.

       2. Aerial: If the electrical power service entrance to the premises is aerial, the
          Architect/Engineer may specify that the telecommunications entrance be aerial as well,
          up to a maximum entrance cable size of two hundred (200) pairs (anything larger shall
          be brought in underground). Any aerial entrance shall be in compliance with
          RBOC/CLEC/ILEC requirements. All aerial telecommunications cables must be at
          least two (2) feet lower than any electrical entrance and shall carry to a standard weather
          head allowing eighteen (18) feet clearance for any vehicular traffic. A minimum 2-inch
          diameter weather head and conduit shall be installed to carry aerial cables into the
          premises.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 14

                        SECTION B - SERVICE ENTRANCE

       In either case, any conduits shall be permitted to have only “long sweep” elbows, with not
       more than 270 degrees of cumulative direction change between any two pulling points
       (conduit ends or pull boxes). Generally, the conduits shall be continuous from the point of
       entry into the telecommunications switch room or other designated demarcation point. If
       the cable run, from the point of building entry into the premises demarcation point, is
       greater than 50 feet, the entrance cable shall be terminated in a suitable location within 50
       feet of the entrance point and a suitable interior cable shall be spliced to it to continue to
       the demarcation point, unless installed in a suitable conduit which is continuous from the
       building penetration point to the telecommunications room, or unless the cable material
       meets applicable codes and standards for open installation within the premises. If the total
       run of the entrance cable exceeds 150 feet, a suitable pull box may be required and shall
       be mounted at the nearest point of entry, inside the building.

       Underground installations shall be locatable. A locator/tracer wire will be required in
       underground installations of non-metallic conduit in the absence of locatable
       communications cable(s). Locator wires shall be orange consistent with APWA Uniform
       Color Code. HPDE innerduct containing a factory installed locator wire will meet this
       requirement when installed in a contiguous run; joints of non-contiguous segments shall
       ensure and maintain the electrical continuity of the locator wire.

       Installations requiring manual installation of a locator wire shall use a wire that is
       appropriate for the conditions. Locator wires installed externally to buried facilities shall
       provide abrasion, crush, and moisture resistance suitable for direct burial applications;
       these wires will typically be a 10, 12, or 14 AWG solid conductor with a HMWPE jacket.
       Locator wires installed internally to the conduit system shall be flexible stranded 14 or 16
       AWG type MTW . A suitable service loop (length) of locator wire shall be left at both ends
       of the conduit system and/or be properly secured.

       A suitable pull (mule) tape or polyline will be installed in all conduit systems (innerduct
       may be ordered with factory pre-installed pull tape/polyline). A suitable length of pull tape
       or polyline shall be left at both ends of the conduit system.

B.4.   Entrance Cable

       The telecommunications entrance cable shall be appropriately sized, twisted pair, gel-
       filled, and specifically designed for underground or exterior usage (REA PE-89 type cable).
       The cable and labor to install it will generally be provided by the RBOC/CLEC/ILEC. It is
       up to the Contractor to make this determination and to provide such cable and installation
       if the RBOC/CLEC/ILEC does not. If the Contractor supplies the entrance cable, it shall
       be 24-gauge (minimum) telecommunications cable.

       In certain instances, fiber optic and CATV entrance cables may be required. Please refer
       to the appropriate sections in this document and any included special attachments for
       details on such requirements.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 15

                        SECTION B - SERVICE ENTRANCE

B.5.   Switch Room Cable Entrance

       The entrance conduit may enter the switch room from either below the floor or through the
       ceiling, or through an exterior wall at an appropriate height. In either case, appropriate
       bushings shall be used in the open ends of the conduit to ensure a smooth edge against the
       cable and shall be properly sealed on both ends to ensure no leakage or penetration of water
       into the switch room. All metallic telecommunications entry conduits shall be bonded to
       the building’s grounding system, in accordance with NEC 770.100 and/or EIA/TIA
       specifications. Since the RBOC/CLEC/ILEC may furnish and install the cable, the
       contractor shall leave a pull rope in the conduit to assist the RBOC/CLEC/ILEC. Entrance
       of the conduit into the switch room should be in a corner location allowing a left to right
       breakdown of the cable onto the backboard(s) provided.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                16

                 SECTION C – TELECOM SWITCH ROOM (MDF)

C.1.   General

       Furnish all labor, materials, equipment, supplies, and perform all operations necessary to
       complete the switch room work, in accordance with the applicable drawings and these
       specifications.

C.2.   Size

       The switch room shall be a secure room, accessible by service technicians from a common
       area (hallway, lobby, etc.), air conditioned, and with a two-hour fire rating. Unless
       otherwise specified and approved, the overall size of the switch room shall generally be as
       follows:

                1. Less than 5,000 sq. ft., switch room of 6 x 6 ft.;
                2. From 5,000 to 10,000 sq. ft., switch room of 6 x 8 ft.;
                3. From 10,000 to 25,000 sq. ft., switch room of 8 x 10 ft.;
                4. From 25,000 to 40,000 sq. ft., switch room of 10 x 12 ft.;
                5. Greater than 40,000 sq. ft. warrants a second wiring closet (in
                support of E911 compliance).

       See section D for further guidance and requirements for additional wiring closets
       and E911 compliance.

       All shall have a minimum floor-to-ceiling height of 8 ft.

C.3.   Lighting

       The switch room shall be fitted with flush or surface-mounted, switched ceiling lights that
       will provide fifty (50) foot-candles at desktop levels in any area of the room. LED lighting
       is now the preferred method.

C.4.   Air Conditioning

       The switch room shall be air-conditioned with positive pressure and fresh air make-up,
       with either its own unit or a dedicated air supply and a return air duct from the room, or
       exhaust louvers with automatic fire dampers which will close in case of fire. Air
       conditioning must be continuous, 24 hours per day, every day. See Section I for size
       estimates. Dedicated split-ductless air conditioning units are now the preferred method of
       cooling telecommunications MDF/IDF spaces. If the switch room is cooled by common
       building HVAC system, the air supply to the room shall be controlled by thermostatic
       control dedicated to the room.

C.5.   Environmental Requirements

       The air supplied to the equipment room must be clean and dry. Temperature must
       be held between 45 degrees and 85 degrees F., with a designed continuous operating
              STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                         TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                               REV 7.1-01/2024
                                                   17

               SECTION C – TELECOM SWITCH ROOM (MDF)

       temperature of 72 degrees F. Relative humidity must be maintained between 20%
       and 80% (non-condensing) with a designed continuous operating level of 45%.

C.6.   Sprinklers/Fire Rating

       If any building specifications and/or safety and fire laws, codes, ordinances or other
       regulations require a fire sprinkler system to be installed in the switch room, then such
       system shall be a dry-charged (pre-action) water system. The floor, ceiling, and walls will
       be constructed to meet the two (2) hour fire rating requirements, including a 36-inch wide,
       solid metal door and frame.

C.7.   Location of Entrance Cable

       Entrance cable conduit shall be brought into one corner of the room that will afford a left-
       to-right breakdown of cables onto backboards mounted on two adjacent walls. In a case
       where there are multiple buildings within the project, two 4-in. diameter conduits shall be
       run from the switch room to either another switch room or wiring closet in the other
       buildings. All telecommunications cable between buildings shall be gel-filled PE-89 type
       twisted-pair, 24-gauge (minimum) cable for analog telephone service and single-mode
       fiber optic or Category 6 of the suitable type for data network service. A pull rope must be
       installed with each cable. Gas tube and/or solid-state protection is required at each end of
       copper cables for all inter-building cables. Cables must be installed without back taps
       (dedicated point-to-point).

C.8.   Cable Sizes

       All twisted-pair telecommunications cables between buildings, and from the
       RBOC/CLEC/ILEC into the switch room (if contractor supplied), shall contain, as a
       minimum size, 24-gauge conductors. In multiple story buildings (three or more floors),
       riser cables from the main switch room (MDF) to remote wiring closets (IDF) shall be 24-
       gauge (minimum) interior cable, ARMM type. Generally, the pair count in any riser cable
       shall be equal to the telecommunications jack count within any area(s) being served by
       such cable, times 4. For example, if there are going to be 20 telecommunications jacks
       installed in an area, a minimum 80-pair count cable is required (20 x 4 = 80). In this case,
       since there is no manufactured 80-pair cable, the next highest standard count cable (100-
       pair) would be installed. Project specifics may relax this requirement if a VoIP telephone
       installation is employed.

C.9.   Backboards

       Backboards shall generally be 4-ft. x 8-ft. x ¾-in. sheets of:

       - A/C grade plywood, painted two coats with fire-retardant paint, or
       - Class A fire-rated plywood of good quality, painted with two coats of a black, medium-
       gray semi-gloss or satin finish latex paint which maintains the aesthetic quality of the room.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 18

              SECTION C – TELECOM SWITCH ROOM (MDF)

      Generally, backboards shall be mounted with the 4-ft. dimension in the vertical, 36-in.
      above finished floor (nominally horizontal).

      The horizontal span of single wall backboards shall be, at most, 1 ft. less than the length of
      the wall on which they are mounted, and as such, backboard shall be horizontally centered
      on the wall, leaving a 6-in. space on either end between the adjacent wall and the end of
      the backboard.

      In multiple wall installations where backboard meet in room corners, the backboards shall
      form a continuous corner surface with no gaps. These backboards will, in part, facilitate
      the construction of the Main Distribution Frame (MDF), and may be referred to as such.

      All backboards shall be securely fastened directly to the finished wall structure, using
      appropriate fasteners for the surface to which such backboards are being fastened. Wall
      surfaces must be finished and painted prior to backboard installation.

C.10. Electrical

      A ground rod, bus or ground cable of minimum size 6 AWG, which is not associated with
      the isolated ground of the electrical service panel, shall be made available near the entrance
      conduit and backboard, to enable the direct grounding of gas tube and solid-state protection
      devices, switching equipment and any ancillary equipment requiring such a ground.

      Duplex electrical outlets shall be provided (flush mounted) below the bottom edge of the
      backboards, and on all other walls, at approximately 72-in. centers (i.e., 2 duplex outlets
      per 8-ft. backboard), with a minimum of 1 outlet per wall. If more than 2 outlets will be
      placed in the room, then there shall be a maximum of two outlets per 20-amp circuit, and
      adjacent outlets shall be on different circuits.

      Network racks shall have four duplex equipment outlets split between two dedicated 20-
      amp circuits. Equipment outlets typically installed in two four-inch “quad” boxes on the
      rear of the right rack vertical wire manager as viewed from the rear (if present).

             For rooms serving 80 to 160 Ethernet jacks, an additional dedicated 125-volt 30-
             amp circuit is also required. Outlet to be L5-30R; outlet typically installed in a four-
             inch box on the rear of the left rack vertical wire manager as viewed from the rear
             (if present).

             For rooms serving over 160 Ethernet jacks, an additional dedicated 250-volt 30-
             amp circuit is also required. Outlet to be L6-30R; outlet typically installed in a four-
             inch box on the rear of the left rack vertical wire manager as viewed from the rear
             (if present).

      Overhead lighting shall be provided sufficient to support easy visual identification of
      telecommunications wiring and to support any telecommunications maintenance activity.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                19

               SECTION C – TELECOM SWITCH ROOM (MDF)

      Lighting operation shall be controlled by switch(es) at the standard height adjacent to the
      strike side of the door, and/or by motion detection.

      Local fire code may require the installation of an emergency electrical switch, near the
      entrance door, which can disable all power in the room.

      NOTE: THE ABOVE REQUIREMENTS ARE GENERAL IN NATURE. THERE MAY
      BE SPECIFIC REQUIREMENTS DUE TO EQUIPMENT CONFIGURATION.
      CONTACT THE STATE OF MAINE, OFFICE OF INFORMATION TECHNOLOGY /
      NETWORK SERVICES DIVISION (207-624-8800) BEFORE SPECIFICATIONS ARE
      WRITTEN.

C.11. Finish

      The switch room floor finish shall be vinyl floor covering (VCT), non-static carpet, or
      sealed (painted) concrete. Walls and ceiling (except “suspended” ceilings) shall be painted
      two coats of satin or semi-gloss paint, in either off-white or light beige color. Doors shall
      open outward. Steel doors and louvers (if any) shall be painted in accordance with the
      general painting section, or as the Architect/Engineer shall direct. Backboards shall be
      covered with two coats of black or medium-gray satin or semi-gloss latex paint.

C.12. Distribution

      There shall be conduits exiting the switch room from a point diagonally across from the
      entrance cable, either through the ceiling or into the floor. The size and number of conduits
      shall be dependent on the total size of the building and the number of associated wiring
      closets (next section). After all cabling is in place, all conduit openings shall be sealed with
      a fire barrier sealant which conforms to electrical codes (such as 3M Fire Barrier Sealer),
      to ensure a positive seal against rodents, moisture, smoke or gas ingress/egress.

      Exit points for horizontal cables, if any, may be full conduits or sleeves through the wall,
      ceiling, floor, or shall otherwise employ an exit method which can be made tight and be
      fire rated where appropriate.

C.13. Telecommunications Jacks

      There shall be a minimum of two telecommunications jacks at the standard electrical outlet
      height, in the approximate location of any work desk that may be placed in the room. The
      jacks shall be wired using the same specifications as for the balance of the premises.

C.14. Keying/Securing

      The switch room entrance door shall be locked. The locks for the switch room (MDF) and
      all other state telecommunications-related rooms, closets, or cabinets within the premises
      shall be keyed identically, and such keys shall be unique from any other lock and key
      combinations present within the premises. In instances where the premises employs
           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                20

              SECTION C – TELECOM SWITCH ROOM (MDF)

      electronic card reader access systems, such entrance control to telecommunications spaces
      is the preferred method.

      Access shall be limited to cleared Network Services employees/contract staff and other
      select, approved individuals with specific ongoing need for access. At no time shall
      telecommunication equipment or terminals be accessible to the public or other, unescorted
      individuals that have not been previously approved as noted above.

C.15. Fire Extinguisher

      There shall be a U.S. DOT (Department of Transportation) approved carbon dioxide (CO2)
      type fire extinguisher bearing a minimum UL (Underwriters Laboratories) rating of 10B:C,
      mounted on the wall or in a recessed cabinet, on the outside of the switch room,
      immediately adjacent to the handle side of the entrance door.

C.16. Equipment Racks & Shelves

      Requirements for electronic equipment racks (relay racks) should be assumed. Specific
      requirements shall be determined and approved by Network Services Division personnel
      prior to any construction.

C.17. Locations

      If the switch room (MDF) is to be used to terminate station (horizontal) cables, it must be
      located so that any telecommunications outlets, whose station cables will terminate directly
      in that room, will be within 295 cable-feet (90 meters) of that room, per EIA/TIA
      specifications for maximum horizontal cable distances.
      Placement of switch rooms, closets, and jacks must be approved by the Office of
      Information Technology, Network Services Division.

C.18. Other Uses

      The switch room and wiring closets shall be solely for the use of telecommunications
      equipment and personnel. They shall not be used as chases for pipes, drains, ducts, conduits
      or wires for other utilities. Any pass-through, or co-location of other systems or utilities
      will require written approval from Network Services Division.

      As with power, boiler and sprinkler rooms, they are utility rooms and not tenant spaces,
      thus shall be considered remote locations controlled by the Network Services Division.
      Access to these rooms is subject to state and federal security requirements, including but
      not limited to specific, relevant background checks.

      No storage of any type or any other use of the room shall be permitted. Authorized
      personnel are to remove prohibited items as part of their duty to maintain a tidy, clean
      and safe workspace.

          STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                     TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                           REV 7.1-01/2024
                                               21

              SECTION C – TELECOM SWITCH ROOM (MDF)

C.19. Co-location of Telecommunications installed and/or maintained by another party

      Network Services may, its discretion, release others to procure and/or provide
      telecommunications and/or network services to fulfill specialized agency needs on a case-
      by-case basis. A specific MOU should be negotiated that articulates exactly what the
      parties will provide, have access to, and support.

      In these scenarios, custom telecommunications rooms and security provisions may be
      necessary to provide layered access to the structured wiring infrastructure. This may be
      accomplished by separate/adjoining rooms, “co-location” cages, individual equipment
      cabinets or other approved means to meet the standards and requirement herein.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                22

                         SECTION D - WIRING CLOSETS (IDF)

D.1.   General

       Furnish all labor, materials, equipment, supplies, and perform all operations necessary to
       complete the wiring closets, in accordance with the applicable drawings and these
       specifications.

D.2.   Size

       A wiring closet(s) shall be a secure room(s), accessible by service technicians from a
       common area (hallway, lobby, etc.) and shall be constructed to meet a one (1) hour fire
       rating. Sizes will vary, depending upon telecommunications requirements, but will roughly
       fall into four categories as follows:

                1. Dedicated room, of dimensions approximately 6 ft. (D) X 6 ft. (W) x 8 ft. (H);
                2. Recessed closet, adjacent to a hallway, fitted with a double access door, with
                   dimensions of approximately 4 ft. (D) X 6 ft. (W) X 8 ft. (H);
                3. Wall access closet, recessed into a hallway or corridor wall, and of dimensions
                   approximately 3 ft. (D) X 4 ft. (W) X 8 ft. (H).
                4. Hubbell REBOX. i.e. RE4X(B).

       Door placement and door swing will affect size requirements.

D.3.   Lighting and Environmental Requirements

       Wiring closets shall be provided with continuous positive ventilation with exhaust through
       door/wall louver(s). Normal building environmental air is sufficient provided it shall be
       clean, dry and free of corrosive fumes or other airborne contaminants, be maintained at a
       temperature between 45 degrees F, and 85 degrees F, and have a humidity content between
       20% and 80% (non-condensing). Equipment in wiring closets may generate approximately
       4,000 BTU/hr. or more (recommend budgeting 100 BTU/hr. per drop for network
       equipment). Lighting which provides 50 foot-candles throughout is also required. Positive
       cooling methods (air conditioning) may be required in larger wiring closet applications.

D.4.   Sprinklers

       If any building specifications and/or safety and fire laws, codes, ordinances or other
       regulations require a fire sprinkler system to be installed in the wiring closet(s), then such
       system shall be a dry-charged (pre-action) water system with pre-action control (smoke +
       heat rate-of rise sensing).

D.5.   General Layout and Location

       All wiring closets shall contain plywood backboards of 3/4-in. thickness and constructed
       in a manner like that detailed in Section C above.

              STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                         TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                               REV 7.1-01/2024
                                                   23

                       SECTION D - WIRING CLOSETS (IDF)

       The incoming conduit from the switch room shall terminate at the left end of the backboard
       in the wiring closet to allow a left to right breakdown of riser cable(s). On the right end of
       the backboard, there shall be conduit exit points for horizontal cable distribution throughout
       the premises. These exit points shall either be full conduits or sleeves through the ceiling,
       floor, or shall otherwise employ an exit method which can be made tight (foam-filled in
       the ends of conduits, sleeves, etc.), and be fire rated where appropriate. Likewise, REBOX
       installs are to include EMT sleeves, either to an accessible ceiling or crawl space below.
       Conduits and sleeves are to have adapters and bushings, or “drive ons”/”bang ons”.
       Sleeves through drop ceilings are to be secured near top and near bottom. Securement may
       be facilitated by the use of Unistrut clamps or stand-off clips.

       In any multiple story building, there shall be a minimum of one wiring closet per floor
       (E911 zone). On any floor of relatively large buildings, there shall be a sufficient number
       of wiring closets strategically placed throughout the floor, which will ensure current and
       future adherence to the (maximum) 295 cable-feet, (90 meter) EIA/TIA specification for
       station-to-IDF (jack to wiring closet) horizontal cable runs. Additionally, floor space shall
       be divided among closets into logical zones for E911 and shall not exceed 40,000 sq. ft.
       each.

       Wiring closets shall be serviced by dedicated copper (ARMM type) and optical fiber riser
       cables from the MDF. Riser cables shall be sized (pair count) according to specifications
       in Section C.

       Location of closets and jacks must be approved by the Office of Information Technology,
       Network Services Division.

D.6.   Electrical

       Each wiring closet shall have a minimum of one convenience wall outlet, and four duplex
       equipment outlets split between two dedicated 20-amp circuits. Equipment outlets typically
       installed in two four-inch “quad” boxes on the rear of the right rack vertical wire manager
       as viewed from the rear (if present).

              For rooms serving 80 to 160 Ethernet jacks, an additional dedicated 125-volt 30-
              amp circuit is also required. Outlet to be L5-30R; outlet typically installed in a four-
              inch box on the rear of the left rack vertical wire manager as viewed from the rear
              (if present).

              For rooms serving over 160 Ethernet jacks, an additional dedicated 250-volt 30-
              amp circuit is also required. Outlet to be L6-30R; outlet typically installed in a four-
              inch box on the rear of the left rack vertical wire manager as viewed from the rear
              (if present).

       Equipment circuit breakers above must be dedicated to telecommunications equipment and
       shall be explicitly marked “VITAL TELECOMMUNICATIONS POWER CIRCUIT /
       TRIP IN EMERGENCY ONLY”.
            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 24

                      SECTION D - WIRING CLOSETS (IDF)

       Overhead lighting shall be provided sufficient to support easy visual identification of
       telecommunications wiring and to support any telecommunications maintenance activity.
       Lighting operation shall be controlled by switch(es) at the standard height adjacent to the
       strike side of the door, and/or by motion detection.

D.7.   Finish

       Finish of closets shall be aesthetically acceptable and comparable to surrounding areas in
       both quality and color. Doors shall open outward. See also section C.11.

D.8.   Keying/Security

       All wiring closet entrance doors shall be lockable. The locks for all wiring closets (IDF)
       and all other state telecommunications-related rooms, closets, or cabinets within the
       premises shall be keyed identically, and such keys shall be unique from any other lock and
       key combinations present within the premises. In instances where the premises employs
       electronic card reader access systems, such entrance control to telecommunications spaces
       is the preferred method.

D.9.   Fire Extinguishers

       Location of fire extinguishers in or near wiring closets shall generally follow the fire and
       safety codes which apply to the general physical area(s) adjacent to the wiring closet.

D.10. Other Uses

       The switch room and wiring closets shall be solely for the use of telecommunications
       equipment and personnel. They shall not be used as chases for pipes, drains, ducts, conduits
       or wires for other utilities. Any pass-through, or co-location of other systems or utilities
       will require written approval from Network Services Division.

       As with power, boiler and sprinkler rooms, they are utility rooms and not tenant spaces,
       thus shall be considered remote locations owned by the Network Services Division. Access
       to these rooms is subject to state and federal security requirements, including background
       checks.

       No storage of any type or any other use of the room shall be permitted. Authorized
       personnel are to remove prohibited items as part of their duty to maintain a tidy, clean
       and safe workspace.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                25

                   SECTION E - BASIC WIRING STANDARDS

E.1.   General

       Architect/designers must work with State of Maine Network Services and designated
       furniture planners and furnish plans for review, plans for construction, and as built plans
       upon completion. Plans shall include jack-to-room schedule(s).

       Contractor to furnish all labor, materials, equipment, supplies and perform all operations
       necessary to complete the telecommunications cable wiring, in accordance with the
       applicable drawings and these specifications. All wiring must also be performed in
       accordance with the National Electric Code and any State or Local Building Codes.

E.2.   Scope; Services

       The total number of cable runs and the sizes of the cables shall be dependent upon the size,
       occupancy, and use of the premises.

       1. All interior cables to the telecommunications jacks (“horizontal cables”), whether
          intended for immediate or future Ethernet use, shall be non-shielded, PVC (non-plenum
          rated) jacketed or TFE/FEP (plenum rated) jacketed, 24 gauge twisted pair cable, with
          a minimum EIA/TIA certification of Category 6 to each of the “data” outlets of each
          telecommunications jack. The data cables shall have an outer jacket that is blue in
          color. “Voice” outlets may be added to the “data” outlets of each telecommunications
          jack to accommodate customer needs. Separate voice cables shall have an outer jacket
          that is gray in color. There shall be no exceptions to cable color code. Note: THE
          SINGLE CATEGORY 6 CABLE STANDARD TO EACH JACK LOCATION IS A
          MINIMUM. ANY DEVIATION FROM THIS STANDARD MUST BE APPROVED
          BY THE NETWORK SERVICES DIVISION.

       2. All such cables shall be connected to or “cut down” on the appropriate outlets and
          terminal blocks, as required herein. The following manufacturer-specific jack hardware
          shall be used, as required by project specifics, for wall-flush, wall-surface or portable
          furniture mount (Lucent/Avaya/CommScope part #s, “equivalent” in subsequent
          language means current CommScope/SYSTIMAX part #). Face plate color exceptions
          for portable furniture applications (color match) may be specified in project-specific
          requirements:

              a. Ivory-colored wall flush-mount face plate, 2-position, M12A-246, or equivalent;
              b. Ivory-colored wall flush-mount face plate, 3-position, M13A-246, or equivalent;
              c. Ivory-colored wall flush-mount face plate, 4-position, M14A-246, or equivalent;
              d. Ivory-colored wall surface-mount box, 2-position, M102SMB-B-246, or
                 equivalent;
              e. Ivory-colored wall surface-mount box, 4-position, M104SMB-A-246, or
                 equivalent;
              f. Ivory-colored modular furniture-mount face plate, 3-position, M13C-246, or
                 equivalent.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                26

            SECTION E - BASIC WIRING STANDARDS

   Each face plate or box shall carry, at a minimum, one orange-colored “snap-in”
   Category 6 modular outlet (data), MPS100E-112 or equivalent, and where required,
   one ivory-colored “snap-in” Category 6 modular outlet (non-VoIP voice) MPS100E-
   246 or equivalent, and unless project specifics dictate otherwise.

3. All 4-pair cables shall be run from the telecommunications jack to the designated IDF
    for any given area within the premises, or MDF (by exception) and each such run shall
    be no longer than 295 cable-feet (90 meters), per EIA/TIA specifications for such
    cables. The cables shall be identified by a jack number and by function (Voice or Data).
    The “voice” cables shall be terminated at the IDF or MDF on “110” termination blocks.
    The “data” cables shall be terminated on Category 6 rack-mounted patch panels, or
    “110-JP” termination blocks in small installations. Where IDF spaces are employed,
    there shall be multi-pair riser cable(s) run from each IDF to the MDF of sufficient total
    pair count to accommodate the total pair count for both voice and data jack terminations
    in each IDF space – or Singlemode in lieu of multi-pair for data. Sufficient cable length
    must be left at all cable ends to allow for the proper dressing and cut down of the cable.
    Riser cables shall be terminated on “110” termination blocks. All cables shall be run
    in one continuous length from the jack to the designated termination point (IDF/MDF),
    with no splices or intermediate terminations in such cables.

4. All riser cables shall be of 24-gauge, sheathed, twisted-pair, color coded and
   appropriately sized (pair count) for the installation. Fiber optics riser cables may also
   be required (see Section J for fiber optics specifications).

5. In all instances where telecommunications cable is run in or through any spaces which
    are used in any way for environmental air, such cable shall be placed in conduit, or the
    cable must be CMP rated (National Electric Code Article 800, Plenum Cable), and shall
    be labeled as such.

6. For cable runs between the switch room and wiring closets, there should be adequate
    backboard space provided for the cables and associated termination hardware (see
    Section C). Both cable ends shall be cut down on termination blocks as specified. All
    cables and pairs must be appropriately labeled.

7. Placement of telecommunications jacks in any building(s) should be determined by the
    following general rule; “Wherever an electrical outlet is located, there shall also be
    located a telecommunications jack, spaced 16 to 24 inches in the horizontal from, and
    at the same vertical height as such electrical outlet. Exceptions are generally as follows:

       a. closets;
       b. restrooms;
       c. mechanical rooms (boiler, pump, generator, etc.);
       d. stairwells and hallways;
       e. any large open interior spaces designed specifically for modular
         furniture installations.

     STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                      REV 7.1-01/2024
                                          27

           SECTION E - BASIC WIRING STANDARDS

   In cases where modular (portable) furniture is to be installed, there shall be, at a
   minimum, one telecommunications jack located within the furniture baseboard, as
   close as possible to each desktop work area or workstation location. Each jack shall
   hold, one Category 6 (data), and optionally one Category 6 (voice) telecommunications
   outlet, unless project specifics dictate otherwise. Ingress/egress of the associated
   telecommunications cables within modular furniture shall be facilitated using a whip
   or a power pole/”tele-pole”, depending upon the specific architectural plan. In the case
   of whip installation from “hard” walls to the modular furniture, there shall be whips
   dedicated to telecommunications cables, and, under no circumstances, shall any
   telecommunications cables share a whip with any electrical or other non-
   telecommunications cables. There shall be duplex or quad electrical boxes installed in
   the hard walls, at the standard electrical outlet height, and at strategic points along such
   walls for connection of the whips to the walls. Such boxes will provide an egress point
   for telecommunications cables which are routed within the wall void from the overhead
   spaces. In-wall conduit from such boxes to the overhead spaces will typically be
   required to afford secure and unobstructed passage of the telecommunications cables
   through the wall void. All in-wall conduits and furniture whips shall be sized
   appropriately to afford a maximum 40% cross-sectional cable loading for the number
   of telecommunications cables required in each such conduit and/or whip. In the case
   of power pole installation from the overhead, it is possible that electrical and
   telecommunications cables might share a common power pole. In these instances,
   electrical and telecommunications cabling within any power pole must be separated by
   a sheath, conduit, compartment, or other method which meets all applicable National
   Electrical Code (NEC) requirements for such installation. The telecommunications
   cable compartment in any such pole shall be sized appropriately to afford a maximum
   40% cross-sectional cable loading for the number of telecommunications cables
   required in each such pole, and such compartment shall not be shared with any non-
   telecommunications cables. In all cases, final count and placement of modular
   furniture telecommunications jacks, power poles and whips shall be determined by the
   floor plan, and with the approval of the owner/tenant and the Office of Information
   Technology, Network Services Division.

   This rule should be carefully scrutinized between architect/owner/tenant, to understand
   the designed use, and possible future use of specialized areas, such as classrooms,
   conference areas, hearing rooms, libraries, etc., and to plan for telecommunications
   jack placement accordingly.

   Any areas such as conference rooms, gymnasiums, armories, or other spaces that might
   be used in an emergency or special situation to support a phone bank, call distribution
   center, or emergency support group should be configured with additional
   telecommunications facilities. The Network Services Division can provide cost
   effective suggestions.

8. All vertical and horizontal cable runs must be independently suspended by approved
    hangers, trays, ducts or raceways. All telecommunications cables must be placed to
    avoid electromagnetic interference caused by electrical/electronic devices, such as
    STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
               TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                     REV 7.1-01/2024
                                         28

                      SECTION E - BASIC WIRING STANDARDS

           florescent light ballasts, electric motors, generators, power supplies, radio transmitters,
           etc.

       9. All jacks must be placed within 295 cable-feet (90 meters) of the switch room or IDF
          in which such wiring terminates, per EIA/TIA specifications for such cables. The
          Network Services Division must review and approve placement of jacks.

       10. All cable installations will be performed in accordance with all installation practices
           and guidelines that are recommended for such installation. All installations shall be
           tested and verified for compliance with all applicable standards for such installation,
           including but not limited to, proper conductor pair polarity, sequence and continuity.
           A complete certification report shall be compiled and submitted to the Network
           Services Division upon the completion of installation and certification testing.

E.3.   Labeling

       1. General: Identification labeling of all installed telecommunications facilities and
          systems shall be specified by the Network Services Division.

       2. Trunk/Riser Cables: All telecommunications trunk and riser cables (copper twisted
          pair, optical fiber, coaxial, etc.) shall carry a unique identification label at both ends of
          each such cable, and related termination hardware shall be labeled likewise. Typical
          labeling should include destination building, strand or pair count, and/or cable number.
          Specific labeling requirements shall be developed for each installation and included in
          work orders.

       Voice/Data Station Jacks, Termination Blocks and Patch Panels: All telecommunications jacks, outlets,
       termination blocks, patch panels or other terminating hardware shall carry a unique, sequential
       identification label for each “circuit” formed by a given cable and its associated outlet, termination block
       position or patch panel port. Telecommunications jack, outlet, termination block and patch panel labeling
       schemes within any building subject to this Specification shall be in keeping with a logical, orderly, and
       sequential layout, based on the architectural floor plans for the building, and all such labeling schemes shall
       be determined and approved by the Network Services Division.
           Telecommunications jacks normally should be numbered sequentially in following
           manner, where:
              - Ethernet Data jacks start with the letter ‘D’, and
              - analog telephone (Voice) jacks start with the letter 'V’
              - followed by the floor number (use ‘0’ for basement level)
              - followed by the three digit sequential serial number

           D1001 would be the first Data jack on the first floor (Data jacks include office jacks,
           modular furniture, IP wall phones, security panel*, PowerLogic, (Aiphone) video
           phones)

           V2010 would be the tenth Voice jack on the second floor (this include fax machines,
           TDDs, elevators, Emergency Call Stations)

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                        29

                     SECTION E - BASIC WIRING STANDARDS

          Additionally, there are two other classes of the Ethernet devices that are typically
          uniquely labeled (without floor designation):

          -     AP011 eleventh AP (Wi-Fi Access Points)
          -     CAM05 fifth camera (typically Fixed Cameras, including elevators, and Pan-tilt
                Cameras)
          -     HVAC connections in state buildings* may or may not be required to run with
                purple cable and labeled different than normal Data jacks with blue cable; consult
                with the Network Service engineer to determine which applies.

          *Note the State of Maine does not provide Internet or telephone service to third party
          building owners or property management entities. Third party (i.e. landlord or
          contractor) installed/owned/operated systems, such as HVAC, security systems,
          computers, elevators, etc. that need communications connectivity will require
          independent service be provided by the third party absent approval in the form of a
          written wavier from this office.

E.4.   Pathways and Conduits

       Pathways and conduits in new construction and remodeling projects shall be included in
       the scope of the project by architects, general contractors, and/or their subcontractors
       where employed.

       Pathways include, but are not limited to cable/ladder trays, sleeves and fire sleeves.
       Consultation with Network Services early in the project will be needed to determine
       where and to what extent these ladders, trays, sleeves and conduits will be required.

       Penetration of walls of exit areas, hallways, etc. shall be done so with a product with an
       appropriate fire rating such as the Hilti (sleave) products, or 3M fire barrier products (i.e.,
       for cable tray penetrations).

       Elevator control cabinets shall have EMT, or other appropriate metallic product provided
       by contractor(s) to bring telecommunications lines out of elevator mechanical rooms to a
       mutually agreeable location(s).

              STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                         TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                               REV 7.1-01/2024
                                                   30

                    SECTION F - CABLE TELEVISION (CATV)

F.1.   General

       Furnish all labor, materials, equipment, supplies and perform all operations necessary to
       complete the cable television work, in accordance with the applicable drawings and these
       specifications. All work must be performed in accordance with the National Electric Code
       and any State and Local Building Codes.

F.2.   Point of Entry

       The CATV service entrance to the premises shall be at a point mutually acceptable to the
       owner and the local CATV service provider. If the signal is to be provided by antenna
       arrangements, then it shall be in accordance with the general architectural plans showing
       that point closest to the area within the premises that is intended to house the receiving or
       “head-end” equipment.

F.3.   Entrance Methods

       1. Buried: From the property line closest to the CATV service provider facilities “drop”,
          there shall be a conduit(s) buried at a minimum depth of 24 inches, using minimum 2-
          inch diameter schedule 40 or 80 PVC pipe. In areas subject to vehicular traffic, the
          conduit(s) shall be encapsulated in concrete to a minimum thickness of 3 inches and
          running the full length of the traffic area. In all areas where public streets are crossed,
          rigid steel conduits shall be used. All conduits shall be capped after installation to protect
          them from weather elements and debris.

       2. Aerial: If the electrical power service entrance and other telecommunications service
          entrances to the premises are aerial, the Architect/Engineer may specify that the CATV
          entrance be aerial as well. Any aerial entrance shall be in compliance with the CATV
          service provider requirements. All aerial CATV cables must be at least three (3) feet
          lower than any electrical entrance and shall carry to a standard weather head allowing
          eighteen (18) feet clearance for any vehicular traffic. A minimum 2-inch diameter
          weather head and conduit shall be installed to carry cables into the premises, and such
          conduit shall be continuous into the switch room or other designated point of termination
          (demarcation point). If the service is via an antenna arrangement on top of the building,
          then a conduit shall be installed from the base of the antenna location to the point of
          termination.

       In either case, any conduits shall be permitted to have only “sweep” elbows and not over
       270 degrees of cumulative directional change between any two cable pulling points.
       Generally, the conduits shall be continuous from the point of entry into the
       telecommunications switch room or other designated demarcation point. If the run, from
       the point of entry into the premises to the demarcation point, is greater than 50 feet, then
       the entrance cable shall be terminated in a suitable location within 50 feet of the entrance
       point and a suitable interior cable shall be spliced to it to continue to the demarcation point,
       unless the entrance cable material meets applicable codes and standards for open
       installation within the premises. If the total “run” of the entrance cable (in conduit) exceeds
            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                  31

                   SECTION F - CABLE TELEVISION (CATV)

       250 feet, then a pull box of sufficient size to accommodate the diameter of the
       telecommunications cable shall be mounted at the nearest point of entry, inside the
       building.

       In all cases, the CATV entrance should parallel the telecommunications entrance if
       possible. These may be instances where the CATV entrance may share a conduit with the
       telecommunications entrance cable, and this will be determined on a “case by case” basis.

F.4.   Entrance Cable

       The CATV entrance cable shall be a 75-ohm coaxial cable, with a physical composition
       and diameter to be determined by the length of the service entrance run and designed for
       underground usage when it is to be used as such. The cable shall be terminated into a
       coaxial grounding block by one of the two following methods:

              1. If the entrance is via underground conduit, then the grounding block shall be
                 located as close as possible to the point of building penetration and shall be
                 grounded to the telecommunications ground or other suitable nearby ground.

              2. If the entrance is aerial, then the grounding block shall be located on the outside
                 of the premises, as close as possible to the point of building penetration and shall
                 be grounded to an outside ground rod.

       In either case, the coaxial cable will then continue to the designated point of termination
       (demarcation point).

F.5.   Location

       Entrance conduit may enter the switch room or designated point of termination from either
       below the floor or through the ceiling. In either case, appropriate bushings shall be used on
       the open ends of the conduit to ensure a smooth edge against the coax and shall be properly
       sealed at both ends to ensure no leakage or penetration of water into the switch room after
       the coax is in place.

       Entrance of the conduit into the switch room or designed point of termination should be in
       a corner location, which will allow a left to right connection of cables to branch extensions
       that will terminate on an associated backboard. This entrance and the location of the
       backboard shall be on a wall location other than those used for telecommunications cable
       and associated frames, blocks or cross-connects.

F.6.   Backboard

       The backboard shall be of the same construction, affixed to the walls, and painted in a
       manner which is consistent with the backboard requirements detailed in other sections of
       this document.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                32

                   SECTION F - CABLE TELEVISION (CATV)

F.7.   Other Runs

       Conduit runs carrying coaxial cables to other areas shall exit the switch room via a sleeved
       conduit(s) (in the same general area as the entrance coax), which shall be sealed in the same
       manner as the end of the telecommunications entrance conduit(s). Coaxial cable runs to
       terminal locations shall either be placed in conduit, or the coaxial cable itself shall be fire
       rated. In those instances where the cables are run in or through any spaces which are used
       in any way for environmental air, it shall be CMP (National Electric Code Article 800,
       Plenum Cable) rated cable, and shall be labeled as such.

F.8.   Identification and Termination

       Cable terminations at the jack or “subscriber” end shall be in standard electrical boxes,
       using standard F-type “feed thru” connector, and will serve as the CATV outlet for the
       connection of television equipment. Each outlet shall be assigned an identification label,
       and such label shall be marked or affixed to the cover plate of the outlet. Each cable shall
       be marked at the switch room, or other designed common termination point, with a tag
       bearing an identifying label which is identical to the one placed or marked on the far end
       of such cable. Unless otherwise specified, the cables shall not be “cut down” or connected
       at the switch room or other designed common termination point but shall be left with
       sufficient length to be affixed to the backboard and properly connected to various CATV
       distribution devices. Unless otherwise specified, all CATV distribution devices shall be
       supplied and installed by the Office of Information Technology, Network Services
       Division.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 33

                          SECTION G - PAGING SYSTEMS

G.1.   General

       Furnish all labor, materials, equipment, supplies and perform all operations necessary to
       complete the paging system work, in accordance with the applicable drawings and these
       specifications. All work must also be done in accordance with the National Electric code
       any State or Local Building Codes.

G.2.   Speakers

       All speaker units shall be listed equipment and installed in accordance with the
       manufacturer’s recommendations. Units shall be installed to afford future access to the
       wiring connections, should the need arise.

G.3.   Wiring

       All wiring shall consist of the manufacturer’s suggested cable. Typically, the cable
       composition will be one (1) shielded pair of 18-gauge copper conductors. A cable shall be
       run to each speaker unit from the switch room, wiring closet or other area which has been
       designated to house the paging system switching and amplification equipment. All wiring
       that is not in conduit must be fire rated, or CMP labeled.

G.4.   Identification

       The speaker end of each cable should be trimmed to length, dressed and affixed to the
       speaker unit. The opposite (switch room) end shall be coiled with sufficient length to allow
       dressing and connection to the switching and amplification equipment and shall be labeled
       in a manner that will identify its associated speaker unit.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                34

                        SECTION H - VIDEO SYSTEMS

ANY REQUIREMENTS FOR VIDEO SYSTEMS WILL BE DEVELOPED SPECIFICALLY
FOR EACH PROJECT REQUIRING SUCH SYSTEMS.

        STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                   TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                         REV 7.1-01/2024
                                             35

                    SECTION I - MECHANICAL EQUIPMENT

I.1.   General

       Furnish all labor, materials, equipment, supplies and perform all operations necessary to
       complete installation of mechanical equipment required for the support of the
       telecommunications infrastructure, in accordance with the applicable drawings and these
       specifications. All work must also be done in accordance with the National Electric code
       any State or Local Building Codes.

I.2.   Air Conditioning

       There shall be a continuously operating, forced air conditioning and ventilation system
       servicing the switch room. Should the existing building system be sized and operated in a
       manner which would allow adequate ventilation and air conditioning of the switch room,
       as required by the telecommunications equipment specifications, then separate feed and
       return air ducts shall be supplied to the switch room from the existing system. Use the
       following guideline for estimating the equipment load:

              4,000 BTU/hr. per 40 data jacks, i.e. 1-40 jacks = 4,000 BTUs, 41-80 jacks = 8,000
                 BTUs, etc. (i.e. 100 BTU/hr. per drop rounded up in multiples of 40 for network
                 equipment)

       All mechanical equipment shall be listed and certified as to its use and application in this
       instance and for this specific use. There shall be labeled fire dampers installed in all duct
       work with a certified fire closing link fuse or other device designed to close off the air flow
       in the event of such a situation.

       In addition to any other installation requirements, the installation of a dedicated air
       conditioning system for switch rooms shall be in accordance with the following:

              1. Should the design call for an independent, dedicated air conditioning unit for the
                 switch room, then such a unit shall be provided. The unit provided shall be of a
                 recognized, listed brand designed for such an application and shall be installed
                 in such fashion as to prevent any possible leakage of water into the switch room.
                 Therefore, if a water-cooled unit is provided, it shall be installed outside the
                 switch room. Should an air-cooled unit be provided, it may be installed within
                 the switch room in a location not directly over the PBX or backboard locations.

              2. Air conditioners must be powered separately from the switch room electrical
                 service.

I.3.   Related Electrical Wiring

       All wiring, circuitry and electrical components shall be UL (Underwriters Laboratories)
       approved and installed in accordance with all codes. All electrical circuits utilized shall be
       protected by a circuit breaker of sufficient size to support the installation.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 36

                  SECTION J - FIBER OPTIC CABLE SYSTEMS

J.1.   General

       Furnish all labor, materials, equipment, supplies and perform all operations necessary to
       complete the installation of fiber optic cable systems, in accordance with the applicable
       drawings and these specifications. All work must be performed in accordance with the
       National Electric Code and any State and Local Building Codes.

       ALL WORK INVOLVING FIBER OPTICS MUST BE APPROVED IN WRITING BY
       THE OFFICE OF INFORMATION TECHNOLOGY, NETWORK SERVICES
       DIVISION.

J.2.   Point of Entry

       The entrance to the premises shall be at a point mutually acceptable to the owner and the
       RBOC/LEC. If cables are to be installed within or between buildings, then such entrances
       shall be in accordance with general architectural and Office of Information Technology,
       Network Services Division plans showing that point closest to the planned location of the
       optical equipment.

J.3.   Entrance Methods

       1. Buried: From the property line closest to the RBOC/CLEC/ILEC facilities, there shall
          be a conduit(s) buried at a minimum depth of 24 inches, using a minimum 2-inch
          diameter schedule 40 PVC pipe. In areas subject to vehicular traffic, the conduit(s) shall
          be encapsulated in concrete to a minimum thickness of 3 inches and running the full
          length of the traffic area. In all areas where public streets are crossed, rigid steel conduits
          shall be used. All conduits shall be capped after installation to protect them from weather
          elements and debris.

       2. Aerial: If the electrical power service entrance and other telecommunications service
          entrances to the premises are aerial, the Architect/Engineer may specify that the fiber
          optic cable entrance be aerial as well. Any aerial entrance shall be in compliance with
          the RBOC/CLEC/ILEC requirements. All aerial fiber optic cables must be at least two
          (2) feet lower than any electrical entrance and shall carry to a standard weather head
          allowing eighteen (18) feet clearance for any vehicular traffic. A minimum 2-inch
          diameter weather head and conduit shall be installed to carry cables into the premises,
          and such conduit shall be continuous into the switch room or other designated point of
          termination (demarcation point).

       In either case, any conduits shall be permitted to have only “long sweep” elbows and not
       more than 270 degrees of directional change between any two cable pulling points.
       Generally, the conduits shall be continuous from the point of entry into the
       telecommunications switch room or other designated demarcation point.

       If the run from the point of entry into the premises to the demarcation point is greater than
       50 feet, then the entrance cable shall be terminated in a suitable location within 50 feet of
            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                  37

                  SECTION J - FIBER OPTIC CABLE SYSTEMS

       the entrance point, and a suitable interior cable shall be spliced to it to continue to the
       demarcation point, unless the cable material meets applicable codes and standards for open
       installation within the premises. If the total “run” of the entrance cable (in conduit) exceeds
       150 feet, then a pull box of sufficient size to accommodate the diameter of the
       telecommunications cable shall be mounted at the nearest point of entry inside the building.

       In all cases, the fiber optic cable entrance should parallel the telecommunications entrance
       if possible. There may be instances where the entrance cable may share a conduit with
       other telecommunications or CATV entrance cables, and this will be determined on a “case
       by case” basis. In any case where a conduit is shared with other cables, an innerduct shall
       be installed in such conduit to carry the fiber optic cable.

J.4.   Fiber Optic Cable

       The fiber optic cable shall be appropriately sized (numbers of fibers) and shall be
       appropriate for its intended installation environment, whether underground, aerial, interior
       (riser), or plenum. Each fiber shall be encapsulated in a color-coded buffer/sheath, and all
       shall be sheathed in an overall jacket of appropriate type for the given installation, and as
       specified by the Network Services Division.

       Specific fiber optic cable type shall be determined by specific project application. Typical
       fiber optic types are 50/125 micron (OM3/OM4 for in-room network applications, i.e. data
       center), 62.5/125 micron (OM1 for fire alarm systems) and 9/125 micron (single mode for
       general horizontal and vertical networking).

       Specific requirements for types of fiber optic cable installations shall be determined on a
       case-by-case basis and approved by the Office of Information Technology, Network
       Services Division.

J.5.   Location

       Entrance conduit may enter the switch room from either below the floor or through the
       ceiling. In either case, appropriate bushings shall be used at the open ends of the conduit
       to ensure a smooth edge against the cable and shall be properly sealed at both ends to ensure
       no leakage or penetration of water into the switch room after the cable is in place. One
       entrance of the conduit into the switch room should be in a corner location, allowing a left
       to right connection to the fiber optic terminal equipment. This entrance and the location of
       the backboard shall be on a wall location other than those used for other
       telecommunications cable and associated frames, blocks or cross-connects.

J.6.   Backboard

       The backboard shall be of the same construction, affixed to the walls, and painted in a
       manner which is consistent with the backboard requirements detailed in other sections of
       this document.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 38

                  SECTION J - FIBER OPTIC CABLE SYSTEMS

J.7.   Cable Ingress/Egress, Termination, Splicing

       Conduit runs carrying fiber optic cables to other areas shall exit the switch room via a
       sleeved conduit(s) (in the same general area as the entrance cable), which shall be sealed
       in the same manner as the end of the telecommunications entrance conduit(s).

       Fiber optic cable runs to terminal locations shall either be in dedicated conduits or placed
       in fiber optic innerduct of dimensions specified by the Network Services Division. Fiber
       optic cable shall terminate in Corning Pretium (PCH), AT&T/Lucent/CommScope
       “Lightguide” or equivalent fiber optic terminals that are approved by the Network Services
       Division.

       Specific termination connector type shall be determined by the Network Services Division
       prior to the commencement of such work. In general, all interior, riser, and intra-campus
       Singlemode shall terminate in duplex LC connectors. Other Singlemode terminations
       remain SC SPC’s unless otherwise dictated by carrier/provider. All new fiber optic
       installations and terminations shall use factory pre-polished “pigtails”, fusion-spliced to
       the cable.

       Fiber termination and splicing is to be performed only with the approval of the Network
       Services Division. Fiber splicing and termination must only be performed by trained
       personnel and must be in accordance with industry accepted fiber splicing methods.

J.8.   Certification and Identification

       All terminated fibers shall be guaranteed by the installer to meet continuity and system
       design loss criteria. Upon completion of the fiber optic cable system installation, each
       terminated fiber of all fiber optic cables shall be tested and certified for continuity and end-
       to-end loss. Supporting documentation which details such test and certification shall be
       submitted to the Office of Information Technology, Network Services Division upon
       completion of the project.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 39

               SECTION
               SECTION J
                       J -- FIBER
                            FIBER OPTIC
                                  OPTIC CABLE
                                        CABLE SYSTEMS
                                              SYSTEMS

  Each fiber optic cable shall be marked at both termination points to clearly identify the
  cable, its strand count, type and termination point(s) in the following format:

     PANEL A   24 SM GREENLAW IDF RM 143.1 RACK IDF A1       SHELF 1 PANEL B           PANEL B: Which fiber splice
                                                                                       panel in the s helf

                                                                  SHELF 1: Which fiber
and type. SM=single          MDF or IDF. If no room number        splice shelf in the rack
mode; MM=multi­              listed then the room has not been
mode. May also be a 6        numbered and there is no room
or a 12 count                nearby that is numbered.

        STATE OF MAINE
                 MAINE// OFFICE OF INFORMATION TECHNOLOGY /I NETWORK SERVICES DIVISION
                   TELECOMMUNICATIONS FACILITIES & WIRING
                                                        WIRING SPECIFICATIONS
                                         REV 7.1-01/2024
                                                   40

       SECTION K - REMOVAL OF OLD CABLE AND FACILITIES

K.1.   General

       Execute all removal of old telecommunications cables, conduits, racks and other facilities
       presently existing within the premises, and which will not be reused in any new installation,
       in accordance with the applicable drawings and these specifications.

K.2.   Inspection

       The Contractor shall inspect existing conditions with the Office of Information
       Technology, Network Services Division to make a determination of what is to be removed
       and which existing conduits, cables, etc., shall be reused.

K.3.   Removal

       Removal shall consist of the disconnection of all wiring and/or cables and their subsequent
       removal by pulling out of conduits, raceways, over ceilings, in crawl spaces or wall
       cavities, removing surface wiring or cable and any related fastening devices wherever
       possible. If old wiring and/or cables should be installed in walls, floors or ceilings in such
       a manner which makes it impossible to remove, then it may be left, with the consent and
       written permission of the Office of Information Technology, Network Services Division.
       Such wire and/or cable shall be cut as close to the surface as possible and the cut ends taped
       to prevent accidental reuse and shall be pushed inside the structure to allow patching and
       refinishing of the remaining holes. In all cases, the removal of telecommunications
       facilities shall be accomplished in a manner which will allow for a clean, clear surface to
       remain, i.e., one which can be patched, restored, and painted to match the surrounding
       conditions without degradation to the premises.

       All items shall be removed from the premises in accordance with the general provisions
       regarding this project, or as the Architect or engineer shall dictate. All waste materials must
       be disposed of in accordance with all applicable local, State, and Federal waste disposal
       regulations.

            STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                             REV 7.1-01/2024
                                                 41

                     SECTION L - CUTTING AND PATCHING

L.1.   General

       Execute cutting, fitting, and patching (including ground excavation and back fill if needed)
       and furnish all labor, materials, equipment, supplies, temporary barricades, and covers for
       equipment/furnishings; and perform all operations necessary to complete the
       telecommunications project, in accordance with the applicable drawings and these
       specifications.

L.2.   Inspection

       The contractor shall inspect conditions, including all elements subject to damage,
       movement, disruption or safety requirements during cutting and patching operations.

L.3.   Acceptance

       The commencement of cutting or patching means the contractor has accepted existing
       conditions.

L.4.   Protection

       Contractor shall provide supports, temporary barricades, covers, or other protective devices
       to ensure protection of other portions of the project from direct, indirect or incidental
       damage.

L.5.   Restoration

       All restoration work shall be accomplished with new materials by the crews or work forces
       performing the original work on this project, whenever possible.

L.6.   Cutting

       All cutting of rigid materials shall be accomplished using metal, wood cutting, or masonry
       saws or core drills. Pneumatic tools shall not be used in occupied buildings without prior
       approval of the owner.

L.7.   Corrosive and Foreign Materials

       Whenever conduits, pipes or wiring traverses through walls, and cannot be closed securely
       for reasons of expansion/contraction, pipe collars shall be used to close the opening as
       much as possible against dust, dirt, corrosive or foreign materials, or for cosmetic purposes

L.8.   Finish

       All finish work shall be smoothed, sanded, fitted and painted or finished to ensure a
       cosmetically acceptable, finished product.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                42

                    SECTION L - CUTTING AND PATCHING

L.9.   Exterior

       Any exterior ground trenching shall be back filled, compacted, and covered to match the
       preexisting conditions (i.e., gravel, crushed stone, hot top, concrete sidewalk, loam and
       sod). When excavating through a hot top area, all cuts shall be “saw cut” and “infrared
       bonding” shall be used when replacing hot top materials.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                43

                     SECTION M – TEMPORARY UTILITIES

M.1.   General

       General Contractor to give Network Services one month notice of pre-
       completion/temporary services, and furnish all necessary labor, materials, equipment,
       supplies and perform all operations necessary to provide temporary heat, lights, power and
       pathways for any telecommunications activities for the duration of the project. Project will
       bear the cost of any products need that are not available in stock.

M.2.   Supervision

       The general contractor shall allow owner/lessee-supervised telecommunications installers,
       technicians, or service personnel, including telecommunications contractor(s) under
       contract to the owner/lessee, to enter the premises and to perform required
       telecommunications installations, repairs, and modifications.

M.3.   Temporary Measures

       All telecommunications activities performed under this section shall be provided with
       temporary heat and toilet/sanitary facilities as deliverable and available to the balance of
       the project, as well as temporary lighting, power outlets and pathways as required, until
       such permanent utilities and fixtures become available for use.

M.4.   Coordination

       Telecommunications contractors and personnel under control of the owner/lessee shall
       coordinate all activities and working hours with the general contractor or subcontractor
       responsible for the completion of the telecommunications portion of this project.

M.5.   Protection

       The general contractor shall take all steps required to secure and protect
       telecommunications equipment, supplies and tools placed on the premises and not part of
       this contract. Such protection shall include, but is not necessarily limited to, security,
       temporary covers, barricades, and space heating.

M.6.   Safety

       Contractors shall provide and install all temporary measures necessary to protect the safety
       of all pedestrian and/or vehicular traffic during any internal or external construction
       activities in which the contractor is engaged. Such safety measures shall include, but shall
       not be limited to warning signs, banners, ribbons, barricades, fences, ropes, reflectors or
       lights. All temporary safety measures installed by the contractor shall be removed when
       work is completed and when no further work area hazards exist. Owner/lessee supervised
       personnel shall follow safety practices established by site contractor/manager; violations
       will be handled in the same manner as the other subcontractors.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                45

                    SECTION N – PAINTING AND CLEANUP

N.1.   General

       Furnish all labor materials, equipment, supplies and perform all operations necessary to
       complete the painting and cleanup of all telecommunications activities, in accordance with
       the applicable drawings and these specifications.

N.2.   Coordination

       The telecommunications contractor(s) shall coordinate with the general contractor for the
       entire project or premises to ensure completion of all work in accordance with these plans
       and specifications.

N.3.   Painting

       Final painting shall be accomplished with color selection being determined either by
       requirements to match existing work, or as directed by the contractor/subcontractor
       responsible for painting and interior finish work for the entire project.

N.4.   Rubbish Removal

       At the completion of the telecommunications work, all trash, scrap materials, broken or
       discarded construction materials, boxes, cartons, scrap wire/cable, empty containers,
       temporary barricades, safety devices, temporary utility connections, shall be removed from
       the work areas or otherwise moved or placed at the direction of the general contractor
       responsible for the total project. All waste materials must be disposed of in accordance
       with all applicable local, State and Federal waste disposal regulations.

N.5.   Cleanup

       All switch rooms, wiring closets, and other areas involved in the scope of the
       telecommunications work shall be vacuumed and/or swept clean, floors moped down, and
       floor finish applied, as required. All hand smudges, paint droppings or other noticeable
       defects that would affect the cosmetic appearance of the project, shall be corrected to the
       satisfaction of the architect, general contractor, and the owner’s representative(s) on the
       project.

N.6.   Equipment Installation

       The installation of permanent electronics should not begin until cleaning as noted above
       has been satisfied. Project Managers and contractors needing service at an earlier date
       should refer to Section M for pre-completion, temporary services.

           STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                      TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                            REV 7.1-01/2024
                                                46

         SECTION O – SPECIAL SERVICES AND FACILITIES

ANY REQUIREMENTS FOR SPECIAL TELECOMMUNICATIONS SERVICES AND/OR
FACILITIES WILL BE DEVELOPED SPECIFICALLY FOR EACH PROJECT REQUIRING
SUCH SERVICES AND/OR FACILITIES.

        STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                   TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                         REV 7.1-01/2024
                                             47

                                       APPENDIX

VOICE / DATA OUTLET WIRING DETAILS (EIA/TIA 568B)                                        I

TYPICAL TELECOMMUNICATIONS MDF/IDF ROOM LAYOUT                                           II

TYPICAL TELECOMMUNICATIONS MDF/IDF EQUIPMENT RACK LAYOUTS                                III

TYPICAL TELECOMMUNICATIONS CONNECTIVITY LOGICAL DIAGRAM                                  IV

         STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                    TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                          REV 7.1-01/2024
                                              48

                                              APPENDIX
                                              APPENDIX

TELECOMMUNICATIONS
TELECOMMUNICATIONS VOICE AND DATA
                   VOICE AND DATA OUTLET
                                  OUTLET WIRING
                                         WIRING CONFIGURATION
                                                CONFIGURATION

                                         EIA/TIA
                                         EIA/TIA 568B
                                                 568B STANDARD
                                                      STANDARD

                                                EIA/TIA T 5 68B Straight Through Diagram

                                                1 �                              Ga 1
                                                2 ■                              ■
                                                3 �                              � 3
                                                4 �                              a
                                                5 �                              a5
                                                6■                               □6
                             RJ-45 JACK         7a                               a7
                       EIA/TIA 568B STANDARD    8 ■                              ■8

      RJ45 Pinout
                                                             Pair 2                        Pair 3
        T-568B

                                                  -xM3 IA I A                  A
                                                                                  Pair 2� Pililr4

          1. White Orarge
          2. Orange
                            5.whae BlLc
                            6 Green
                                                   P3TT7 UL  TS6BA                          75689
          3. White Green    7. white BrcwTm
          4. Blue           8. Hrcwri

                                                                       2
                                                                        1
                                                                        3
                                                                        5

                                              TIA/EIA T568-B

      STATE OF MAINE I/ OFFICE OF INFORMATION TECHNOLOGY I/ NETWORK SERVICES DIVISION
                 TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                        REV 7.1-01/2024

                                                      I

                                                                                                                    APPENDIX
                  TYPICAL
                  TYPICAL BUILDING
                          BUILDING TELECOMMUNICATIONS
                                   TELECOMMUNICATIONS MDF/IDF
                                                      MDF/IDF ROOM
                                                              ROOM LAYOUT
                                                                   LAYOUT

                                                                       PLAN VIEW (LARGE
                                                                       PLAN VIEW ( LARGE BUILDING)
                                                                                         BUILDING)

l                        7
                                                                                                                        8-1 1/2

                                                                                                                                              /OICE RISER/STATION
                      I
    CENTER TERMINAL@
    �                                     �
                                                                                                                 8'-0"               -�
    o             212
                                                                                                                                     �
     o                                                □
                                                      e
                                                      o
                                                          .                                                                          1

                                                                                                                                     �
     O       �
              .
                                                                                                                                     -
     o       e
             e

                                                                                                                               ---- � ---- ---...I
             e
             3                                                                                                      1° � � �                                   r-------------------..,I
                                                                                                                    I                                          I
                                                                                                                    I                             I            I                      I
                                                                                                                    I                             I            I                      I
                                                                                                                    I                             I            I                      I
                                                                                                                    I                             I            I                      I

             �
                  I                              I    �
                                                                                                    722 �
                                                                                                    : 2� :
                                                                                                    4 -
                                                                                                    i s-: »Z
                                                                                                      ; s- :
                                                                                                             I I                es
                                                                                                                                •
                                                                                                                                          7   x  I    7222
                                                                                                                                                      Z:¢ -
                                                                                                                                                      253-
                                                                                                                                                      z2: ':
                                                                                                                                                      <gs -
                                                                                                                                                      7 5i i 4% VVu          �� �
                                                                                                                                                                                 I z2s:
                                                                                                                                                                                   :2:-
                                                                                                                                                                                          722 2
                                                                                                                                                                                          22::
                                                                                                                                                                                          3� �
                                                                                                                                                                                                  □.
                                                                                                    s
                                                                                                    �a3�
                                                                                                                  /'
                                                                                                                                                      - 5::                               2%2-
                                                                                                                         I                I 2-:- I I                             I
                                                                                                                                                                                          --:-
                                                                                                                                                                                                  65o

                                                                                                    : : :
                                                                                                                                                      ¢�7:                                ¢e7:
         �                                                                                          ,;%                         II                                               I
                                                                                                                    I                             I            I                      I
                                                                                                                    I                             I            I                      I
                                                                                                                    I
                                                                                                                    I
                                                                                                                         PATCH PANELS             I
                                                                                                                                                  I
                                                                                                                                                               I
                                                                                                                                                               I
                                                                                                                                                                   EQUIPMENT          I
                                                                                                                                                                                      I
                                                                                                                    I                             I            I                      I
                                                                                                                    s�   ------------------a                   -�------------------a
             ��� �
                 - - -- � �                                                                                                                       FRONT
                              "��
                                    ���
                                          �� �
                                                 ��
                                                      �
                                                              �\
                                                                   �
                                                                       \
                                                                        \
                                                                            %
                                                                                %
                                                                                    %
                                                                                        Y
                                                                                            �%
                                                                                            %

                                                                                                 %
                                                                                                  \
                                                                                                   I
                                                                                                    %
                                                                                                        %
                                                                                                         I

     MINI-SPLIT (ABOVE DOOR)                                                                                                                          ELEC.
                                                                                                             I
                                                                                                             I

                        STATE OF MAINE /I OFFICE OF INFORMATION TECHNOLOGY I/ NETWORK SERVICES DIVISION
                                   TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                                          REV 7.1--01/2024

                                                                                                                                II

                                              APPENDIX
        TYPICAL TELECOMMUNICATIONS MDF/IDF (SWITCH ROOM) RACK LAYOUT
                              FOR ELECTRICAL

 Double-Sided Wide
Vertical Cabling Section(s)

                                                  Rear view of
                                                  Chatsworth
                                                 Universal Rack

 One (1) NEMA L5-30R 125 VAC grounded receptacle              Four (4) NEMA 5-20R 125 VAC grounded
          on one (1) dedicated 30A circuit                 receptacles on two (2) dedicated 20A circuits

                STATE OF MAINE / OFFICE OF INFORMATION TECHNOLOGY / NETWORK SERVICES DIVISION
                           TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                                 REV 7.1--01/2024

                                                     III

                                           APPENDIX
TYPICAL
TYPICAL TELECOMMUNICATIONS
        TELECOMMUNICATIONS MDF/IDF
                           MDF/IDF (SWITCH
                                   (SWITCH ROOM)
                                           ROOM) RACK
                                                 RACK LAYOUT
                                                      LAYOUT
                 FOR EXTRA LARGE
                 FOR EXTRA LARGE BUILDING
                                  BUILDING

       1U BLANK PAN EL                       6008 FIB E R SHELF                      1U B LAN K PANEL
     NARROW WIRE MGR                                                               NARROW WIRE MGR

 48-PORT 5E PATCH PA N EL 1-48                                                4 8 -PO RT 5E PATCH PA N EL 49-96
                                              WIDE WIRE MGR
        WIDE WI RE MGR                                                                WI DE WIRE MGR
                                           NORTEL 470-48 SWITCH

   48 -PORT 5E PATC H PANEL                   WIDE WIRE MGR                     48-PORT 5E PATC H PA N EL

                                           NORTEL 470-48 SWITCH
        WIDE WI RE MG R                                                               WI DE WIRE MGR
                                              WI DE WIRE MGR
   48 -PO RT 5E PATC H PA N EL                                                  48-PORT 5E PATC H PA N EL

        WIDE WIRE MGR                         WIDE WIRE MGR                           WI DE WIRE MGR

                                           NORTEL 470-48 SWITCH
   48-PORT 5E PATCH PANEL                      •··-    ·. -··                   48-PORT 5E PATC H PANEL
                                              WIDE WIRE MGR
        WIDE WIRE MGR                                                                 WI DE WIRE MGR
                                           NORTEL 470-48 SWITCH

   48-PORT 5E PATCH PA N EL                   WIDE WIRE MGR                     48-PORT 5E PATCH PANEL

                                           NORTEL 470-48 SWITCH
        WIDE WIRE MGR                                                                 WI DE WIRE MGR
                                              WI DE WI RE MGR

                                              WI DE WIRE MGR

                                              WIDE WIRE MGR

                                                                                        X-FORMER
                                            NARROW WIRE MGR

                                                                                        X-FORMER

                                                                                            UPS

                                                                                       2 EBMUNITS

                                 THREE-RACK LAYOUT {TYP.}

            STATE OF MAINE /I OFFICE OF INFORMATION TECHNOLOGY I/ NETWORK SERVICES DIVISION
                       TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                              REV 7.1--01/2024

                                                    III

                                        APPENDIX

    TYPICAL TELECOMMUNICATIONS LOGICAL CONNECTIVITY DIAGRAM

[ = SERVICE PROVIDER-OWNED                                       [■ = cu sTOMER (STATE)-OWNED

                   I-
                   0
                   0

        □
        □
       J AC K           K
                            DATA/VoIP

         -DATAVoIP-

                                   PREMISES (OFFICE BUILDING)

         STATE OF MAINE /I OFFICE OF INFORMATION TECHNOLOGY /I NETWORK SERVICES
                                                                       SERVICES DIVISION
                    TELECOMMUNICATIONS FACILITIES & WIRING SPECIFICATIONS
                                           REV 7.1-01/2024

                                               IV

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). Pages 45 of the PDF have no text layer (figures, blank pages or scanned forms) and add no text here.
