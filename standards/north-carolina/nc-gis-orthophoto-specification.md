---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-gis-orthophoto-specification
title: North Carolina Technical Specifications for Digital Orthophoto Base Mapping
doc_type: standard
citation: 'NC GIS standard: North Carolina Technical Specifications for Digital Orthophoto Base Mapping'
authority_level: ''
issuing_body: Land Records Management Division, North Carolina Secretary of State (published by NCDIT)
source_url: https://it.nc.gov/documents/files/north-carolina-technical-specifications-digital-orthophoto-base-mapping/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 77add726e14f75193402401702161f11d622e06a7317878d97f35de6c23f792d
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

# North Carolina Technical Specifications for Digital Orthophoto Base Mapping (NC GIS standard: North Carolina Technical Specifications for Digital Orthophoto Base Mapping)

## At a glance

The technical specifications for digital orthophoto base mapping (December 11, 2014) by the Land Records Management Division of the Secretary of State.

## Full text

         North Carolina
   Technical Specifications for
Digital Orthophoto Base Mapping

Land Records Management Division
   North Carolina Department of
      The Secretary of State
      Edited by Thomas W. Morgan

       December 11, 2014

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               2

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               3

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               4

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               5

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               6

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               7

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               8

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                               1

   NC Technical Specifications for Digital Orthophoto Base Mapping
                                 2014

                                      PREFACE

       The "Land Records Management Program" (LRMP) was established in 1977 by
the North Carolina Legislature in order to provide technical and financial assistance to
local governments for the modernization of their land records systems. The Technical
Specification(s) for Base, Cadastral, and Digital Mapping (Orthophotos)” are thus
prepared as an essential element of the LRMP and is applicable to all county or
municipal mapping projects. To the maximum extent practicable, these specifications
should also be utilized by state agencies involved in mapping operations. Section 6,
“Digital Orthophotos”, was adopted on August 18, 2004, by the North Carolina
Geographic Information Coordinating Council (GICC).
       Invaluable guidance and assistance have been provided by the Standards
Committee of the North Carolina Property Mappers Association and by representatives
of local governments. Assistance was also provided by the North Carolina Geodetic
Survey (NCGS), the Center for Geographic Information and Analysis (CGIA), the
North Carolina Department of Transportation, and the North Carolina Department of
Revenue. I also want to thank Atlas Geodata, Spatial Data, Surdex and Photo Science
for providing industry prospective.

Edits and Additions:
As you use this standard if there are edits or suggestions that you wish were included,
please forward them to Landrecords@sosnc.com , Subject: Orthophoto technical
Standards (Proposed Revisions). Depending on the nature of the update and the update
cycle of the standard there may be a delay in evaluating the suggestion and including it
in the standard. Be assured that we are appreciative of your help in making the
standard better.

                                           2

              NC Technical Specifications for Digital Orthophoto Base Mapping
                                            2014

     TECHNICAL SPECIFICATIONS FOR ORTHOPHOTO DIGITAL
                         MAPPING

Table of Contents
GENERAL ....................................................................................................................................................... 6
   Definitions ................................................................................................................................................. 6
       Aerial Frame Camera ............................................................................................................................ 6
       Aerial Pushbroom Camera .................................................................................................................... 6
       Band ...................................................................................................................................................... 6
       Brightness Value ................................................................................................................................... 6
       Burning .................................................................................................................................................. 7
       Chip ....................................................................................................................................................... 7
       Client ..................................................................................................................................................... 7
       Clipping ................................................................................................................................................. 7
       Contracting Officer:............................................................................................................................... 7
       Contractor ............................................................................................................................................. 7
       Digital Number (DN).............................................................................................................................. 7
       Dodging ................................................................................................................................................. 8
       Exploitation Images............................................................................................................................... 8
       Field ....................................................................................................................................................... 8
       Global Navigation Satellite System (GNSS) ........................................................................................... 8
       Ground Sampling Distance (GSD).......................................................................................................... 8
       Image File Directory (IFD) ..................................................................................................................... 8
       Inertial Measuring Unit (IMU) ............................................................................................................... 9
       Metadata............................................................................................................................................... 9
       Nadir Ground Sample Distance (NGSD) ................................................................................................ 8
       Orthophotography/Orthoimagery ........................................................................................................ 9
       Photography.......................................................................................................................................... 9
       Raw Images ........................................................................................................................................... 9
       Re-sampling......................................................................................................................................... 10

                                                                                 1

             NC Technical Specifications for Digital Orthophoto Base Mapping
                                           2014

      Tag ....................................................................................................................................................... 10
      Transportation Feature Ground Sample Distance (TGSD) .................................................................... 8
   Work Statement:..................................................................................................................................... 10
   General Mapping Specifications: ............................................................................................................ 10
   Visits to Contractor’s Site:....................................................................................................................... 11
   Surveying Activities: ................................................................................................................................ 11
AERIAL PHOTOGRAPHY ............................................................................................................................... 13
   Project Area and Client Contract Map: ................................................................................................... 13
   Conditions During Photography:............................................................................................................. 13
   Ground Sampling Distance (GSD) for Final Orthoimagery Deliverable: ................................................. 14
   Actual Image Acquisition Geometry ....................................................................................................... 15
      Nadir Ground Sample Distance (GSD) for acquisition......................................................................... 15
      Transportation Feature Ground Sample Distance (GSD) .................................................................... 15
   Flight Plan:............................................................................................................................................... 16
   Re-flights: ................................................................................................................................................ 16
   Spacing of Photographs: ......................................................................................................................... 17
      Forward Overlap (not applicable to pushbroom cameras): ............................................................... 17
      Side Overlap: ....................................................................................................................................... 18
      Angular Exterior Orientation Parameters for Actual Image Acquisition ............................................ 19
   Aircraft: ................................................................................................................................................... 20
   Digital Sensor System:............................................................................................................................. 21
   Digital Image Data Files:.......................................................................................................................... 21
   Digital Sensor Exposure History: ............................................................................................................. 22
   Flight Log: ................................................................................................................................................ 22
   Exploitation images:................................................................................................................................ 22
HORIZONTAL AND VERTICAL CONTROL ...................................................................................................... 24
   General:................................................................................................................................................... 24
   Horizontal Control Surveys: .................................................................................................................... 25
   Vertical Control Surveys:......................................................................................................................... 25
   Photo Control Points: .............................................................................................................................. 26
   Permanent Monuments:......................................................................................................................... 26

                                                                                2

             NC Technical Specifications for Digital Orthophoto Base Mapping
                                           2014

   Survey Records:....................................................................................................................................... 27
      Field Notes and Observation Logs. ..................................................................................................... 27
      Observation Logs shall contain: .......................................................................................................... 27
      Computations...................................................................................................................................... 28
      Control Diagram. ................................................................................................................................. 28
      Control Data. ....................................................................................................................................... 28
      GNSS Observation Summary. .............................................................................................................. 29
   Feet/Meter Conversions: ........................................................................................................................ 29
   Global Navigation Satellite System (GNSS): ............................................................................................ 29
   Global Navigation Satellite System & Inertial Measurement Units (GNSS-IMU).................................... 30
      General. ............................................................................................................................................... 30
      Accuracy. ............................................................................................................................................. 30
      Ground Stations. ................................................................................................................................. 30
      Satellite Geometry. ............................................................................................................................. 30
      Post-processing Software. .................................................................................................................. 30
      Reporting............................................................................................................................................. 31
   Targeting: ................................................................................................................................................ 31
   Property Entry: ........................................................................................................................................ 31
   Target Removal: ...................................................................................................................................... 32
ANALYTICAL TRIANGULATION: ................................................................................................................... 33
   Aerotriangulation (general): ................................................................................................................... 33
   Nominal Scales for Triangulation: ........................................................................................................... 34
   Ground Coordinate Systems: .................................................................................................................. 34
   Aerotriangulation: ................................................................................................................................... 34
   GNSS-IMU Post Processing & Aerial Triangulation Report: .................................................................... 35
      Control and Flight Line Indexes........................................................................................................... 35
   Drop Points: ............................................................................................................................................ 37
   Blind Checkpoints: .................................................................................................................................. 37
DIGITAL ORTHOPHOTOS ............................................................................................................................. 38
   General:................................................................................................................................................... 38
   Traditional Digital Orthophotography In Built Up Areas: ....................................................................... 38

                                                                               3

               NC Technical Specifications for Digital Orthophoto Base Mapping
                                             2014

     Orthophoto Horizontal Accuracy Standards: .......................................................................................... 39
     Reporting of Horizontal Accuracy: .......................................................................................................... 40
     Processed Digital Imagery: ...................................................................................................................... 40
     Digital Terrain Model/Digital Elevation Model: ...................................................................................... 41
     Image Completeness:.............................................................................................................................. 42
     Ground Resolution: ................................................................................................................................. 42
     Image Rectification Algorithm: ............................................................................................................... 42
     Tile Coverage Area: ................................................................................................................................. 42
     Image Mosaicking: .................................................................................................................................. 42
     A North Carolina Panel Naming Convention:.......................................................................................... 44
     Mapping Basic Modular Unit: (8 digit SOS LRM BMU )........................................................................... 45
     Numbering of the Basic Modular Units: ................................................................................................. 45
     Border Data: ............................................................................................................................................ 46
     Reference Product: ................................................................................................................................. 46
     Orthophoto Image Quality:..................................................................................................................... 47
     Radiometric Resolution:.......................................................................................................................... 48
        Color Imagery. ..................................................................................................................................... 48
        Color Infrared Imagery. ....................................................................................................................... 48
        4-Band Imagery. .................................................................................................................................. 49
     File Compression: .................................................................................................................................... 49
     Deliverable Product Format: ................................................................................................................... 49
     Deliverable Items by Contractor: ............................................................................................................ 50
     Project Report: ........................................................................................................................................ 50
a)      Date of photography by scale. ............................................................................................................ 50
b)      Altitude of digital sensor and lens focal length. ................................................................................. 50
Attachment 1 .............................................................................................................................................. 52
     Numbering sequence for Tileing of areas smaller than 10,000 x 10,000 ............................................... 52
Addendum 1................................................................................................................................................ 53
     Deliverable Items by Contractor: ............................................................................................................ 53
Addendum 2................................................................................................................................................ 56
     NC Orthoimagery Quality Assurance (QA) Procedures........................................................................... 56

                                                                                4

             NC Technical Specifications for Digital Orthophoto Base Mapping
                                           2014

References .................................................................................................................................................. 59

                                                                               5

   NC Technical Specifications for Digital Orthophoto Base Mapping
                                 2014

                             SECTION 1

                              GENERAL
GENERAL
   Definitions:
         Aerial Frame Camera:
           Aerial Frame Camera is an aerial digital imaging sensor, which may be
           comprised of multiple digital cameras, whose shutters open and close while
           collecting imagery one frame at a time as the aircraft moves along a flight line.

         Aerial Pushbroom Camera:
           Aerial Pushbroom Camera is an aerial digital imaging sensor, which collects a
           strip of imagery with digital arrays as the aircraft moves along a flight line.
           Pushbroom cameras have nadir, forward, and aft sets of arrays that
           simultaneously and continuously record. The forward array is pitched forward
           along the flight line and the aft arrays are pitched backward along the flight
           lines. Stereoscopic imagery is obtained by viewing forward and aft array
           imagery over common areas.

         Band:
           A band is image data gathered within a range of wavelengths of
           electromagnetic radiation. Typically the bands are Red, Blue, Green, and Near
           Infrared.

         Brightness Value:
           Brightness value is a number (normally 0-255 for 8-bit imagery) representing a
           discrete intensity color level of a pixel in an image. Also referred to as a
           “digital number” (DN).

                                          6

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     Burning:
       Burning is the manipulating of the intensity of part of a photograph to make
       something darker.

     Chip:
       A Chip is each separate piece of an image mosaic that contributes to the final
       image.

     Client:
       Client shall be construed to include not only county governments, but also
       municipal governments, state governmental agencies or any other agency or
       party wishing to enter into a mapping contract with a Contractor under the
       provisions of these specifications.

     Clipping:
       Clipping is a result of capturing or processing an image where the intensity in a
       certain area falls outside the minimum and/or maximum intensity which can be
       represented by that image. This is evidenced by the presence of pixels exhibiting
       the minimum or maximum digital count in an image’s dynamic range.

     Contracting Officer:
       Contracting Officer is the officially designated representative of the state or
       local government obtaining the mapping products or services. This individual’s
       authority and responsibilities shall be prescribed by the appropriate state,
       county, or municipal governing board or authority.

     Contractor:
       Contractor is that firm, company, or organization to which the mapping or
       service contract has been let. References to the Contractor in these
       specifications shall also apply in full to any subcontractor working for the
       named Contractor.

     Digital Number (DN):
       Digital Number (DN) is the color value assigned to a pixel within a band
       (R,G,B,NIR) or luminosity. This number shall be 0-255 for 8-bit images.

                                       7

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     Dodging:
       Dodging is the manipulation of the intensity of part of a photograph to make
       something lighter.

     Exploitation Images:
       Exploitation images are the result from post-processing the “raw” images by
       sensor-specific software. The sensor-specific software applies geometric and
       radiometric processing to the images which enables common professional and
       consumer software to view and manage the resulting “post-processed” images.
       “Exploitation” images exhibit a natural color balance, contrast, and intensity and
       are ready for introduction into the production process.

     Field:
       Field refers only to the entire field, including the value, of the geokey (as
       defined in the TIFF Specification).

     Global Navigation Satellite System (GNSS):
       GNSS includes all satellite navigation systems. Formerly the Global
       Positioning System (GPS) term was used and only referenced the US Satellite
       navigation system.

     Ground Sampling Distance (GSD):
       GSD is the physical measure of the level of detail expressed in linear units of
       data collection for remote digital imaging of the surfaces of the Earth.

         Nadir Ground Sample Distance (NGSD):
              NGSD is the physical measure of the level of detail expressed in linear
              units of data collection of the surfaces of the Earth vertically under the
              center of the remote digital imaging sensor.

         Transportation Feature Ground Sample Distance (TGSD):
              TGSD is the physical measure of the level of detail expressed in linear
              units of data collection of the surfaces of the Earth at any given
              transportation feature.

     Image File Directory (IFD):
       IFD contains information about the image. There must be at least 1 IFD in a
       TIFF file and each IFD must have at least one entry.

                                         8

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     Inertial Measuring Unit (IMU):
       IMU is an electronic device hard mounted to or integrated with a sensor that
       measures and reports the sensor’s velocity and orientation using a combination
       of accelerometers and gyroscopes. With post processing of the recorded
       orientation data, the exterior orientation angular values (Omega, Phi, Kappa) of
       a frame camera exposure can be determined. IMU data is required to produce a
       virtual frame with a line scanner sensor system.

     Metadata:
       Metadata is a description of the content, quality, condition, and other
       characteristics of the geospatial data that is compliant with the North Carolina
       Geographic Information Coordinating Council’s endorsed metadata standard.
       The Council adopted the Federal Geographic Data Committee (FGDC) Content
       Standard for Digital Geospatial Metadata (CSDGM) in 1994 and is in the
       process of adopting a North Carolina State and Government Profile based on
       the ISO-19115-1 metadata standard (2014). A valid metadata record may be
       compliant with either FGDC or ISO standards as adopted by the Council.

     Orthophotography/Orthoimagery:
       Orthophotography/Orthoimagery is an aerial photograph geometrically
       corrected ("ortho-rectified") such that the scale is uniform and can be used to
       measure true distances, because it is an accurate representation of the Earth's
       surface, having been adjusted for topographic relief, lens distortion, and camera
       tilt.

     Photography:

     Photography and/or aerial photography shall be used inclusive of a film image or
     a digital sensor image.

     Raw Images:
       Raw images are defined as the original captured image and metadata, devoid of
       the application of geometric and radiometric processing and generally unfit for
       introduction into a production process. This data is typically in a proprietary
       format and its form and format readable only by sensor-specific processing
       software. This data must be post-processed by sensor-specific software.

                                      9

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     Re-sampling:
       Re-sampling is a software method that is used to increase or decrease the size
       and/or resolution of a digital image by interpolation of pixel values based upon
       neighboring pixel values.

     Tag:
       Tag refers only to the identifying number portion of the geokey (as defined in
       the TIFF Specification).

Work Statement:
   The Contractor shall furnish all materials, superintendence, labor, equipment, and
   transportation and shall execute and complete all of the work required by the
   contract in conformance with these specifications and any contractual modifications
   to these specifications. Any deviation from these specifications, unless specifically
   authorized in writing by the Contracting Officer or his representative, shall be
   sufficient cause for rejection of any part or all of the work performed.

General Mapping Specifications:
             a) Orthophotography/orthoimagery is to be collected with an aerial
                digital sensor unless specifically authorized by the Client in writing.
             b) Unless otherwise specified the deliverable will be a seamless mosaic
                product with no boarders or overlay masks.
             c) All orthoimagery shall be adjusted to the North Carolina Official
                Survey Base as defined in NC GS Chapter 102 -
                http://www.ncleg.net/gascripts/Statutes/StatutesTOC.pl?Chapter=0102
                and adjusted to the latest realization released by National Geodetic
                Survey. All deliverable hardcopy maps/overlays and/or softcopy
                maps/overlays shall contain a statement identifying the above
                information: i.e. “This map/overlay is correlated to the North
                Carolina State Plane Coordinate System, NAD83(2011) epoch
                2010.0.” The contracting officer may require additional deliverables
                that are converted to another datum. If so, the above statement will be
                modified to reflect that the product was so converted.

                                      10

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

              d) All lettering on all deliverable hardcopy maps or overlays and softcopy
                 maps or overlays shall be produced solely by mechanical or electronic
                 means. Hand lettering will not be permitted.

Visits to Contractor’s Site:
   The Contract Officer or officially designated representatives or agents may visit the
   Vendor’s site to inspect work in progress and verify that the procedures and
   equipment being used are in compliance with these Specifications and contract
   requirements. The Contractor agrees to allow access to its production facilities for
   periodic visits by the Client representatives or agents. These visits may be
   unannounced and/or may be upon short notice.

Surveying Activities:
    All surveying activities, as defined in North Carolina General Statute § 89C,
    http://www.ncleg.net/gascripts/Statutes/StatutesTOC.pl?Chapter=0089C undertaken
    by the Contractor shall be conducted by surveyors licensed by the North Carolina
    Board Examiners for Engineers and Surveyors. Photogrammetry services shall only
    be provided by North Carolina licensed surveyors who are competent by virtue of
    education and experience in the discipline of photogrammetry. At the beginning of
    a project involving photogrammetric services, the Contractor shall identify the
    licensed surveyor who will sign and seal the completed project, and who will have
    direct supervisory control of the project. If in the course of the project the surveyor
    designated as being “In Responsible Charge” is replaced, the Contractor shall notify
    the contracting officer immediately in writing. The Surveyor that is in responsible
    charge is required to abide by Board Rules North Carolina Administrative code
    (NCAC title 21, Chapter 56)
    http://reports.oah.state.nc.us/ncac.asp?folderName=\Title%2021%20-
    %20Occupational%20Licensing%20Boards%20and%20Commissions\Chapter%205
    6%20-%20Engineers%20and%20Surveyors

    21 NCAC 56 .0701       RULES OF PROFESSIONAL CONDUCT
    (3)    Shall not affix the signature or seal to any engineering or land surveying plan
           or document dealing with subject matter for which the licensee lacks
           competence by virtue of education or experience, nor to any such plan or
           document not prepared under the licensee's direct supervisory control.
           Direct supervisory control (responsible charge) requires a licensee or

                                        11

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

          employee to carry out all client contacts, provide internal and external
          financial control, oversee employee training, and exercise control and
          supervision over all job requirements to include research, planning, design,
          field supervision and work product review. Direct supervisory control may
          be accomplished face to face or by other means of communication. A
          licensee shall not contract with a non-licensed individual to provide these
          professional services. Research, such as title searches and soil testing, may
          be contracted to a non-licensed individual, provided that individual is
          qualified or licensed to provide such service and provided the licensee
          reviews the work. The licensee may affix the seal and signature to drawings
          and documents depicting the work of two or more professionals provided it
          is designated by a note under the seal the specific subject matter for which
          each is responsible; and
   (4)    In circumstances where a licensee in responsible charge of the work is
          unavailable to complete the work, or the work is a design plan signed and
          sealed by an out-of-jurisdiction licensee (not a site adaptation of a standard
          design plan under Rule 21 NCAC 56 .1106) a successor licensee may take
          responsible charge by performing and documenting all professional services
          to include developing a design file including work or design criteria,
          calculations, code research, and any necessary and appropriate changes to the
          work. The non-professional services, such as drafting, need not be redone by
          the successor licensee but must distinguish in a clean and obvious manner
          and accurately reflect the successor licensee's work. The burden is on the
          successor licensee to show such compliance. The successor licensee shall
          have control of and responsibility for the work product and the signed and
          sealed originals of all documents.
   21 NCAC 56 .1101      GENERAL
            It is misconduct for a Professional Engineer or Professional Land
            Surveyor to seal work done by another individual unless the work is
            performed under the "responsible charge" of the Professional Engineer or
            Professional Land Surveyor.

                                     12

   NC Technical Specifications for Digital Orthophoto Base Mapping
                                 2014

                             SECTION 2
            AERIAL PHOTOGRAPHY

AERIAL PHOTOGRAPHY
  Project Area and Client Contract Map:
      The location, size, and boundaries of the areas to be mapped will be outlined on a
      Client Map and further subdivided and designated in a way to show the number and
      scales of the final base maps to be prepared; the map shall be at a scale adequate for
      its purpose and shall be in an electronic format. When the mapping project includes
      the entire county or portions along county boundary lines, the area to be mapped
      shall extend 2,000 feet beyond the county boundary or to the extent defined by the
      Contracting Officer. This marked Client Map shall be entitled "Client Contract
      Map" and shall be attached to and become a part of any contractual agreement. The
      flight plan proposed by the Contractor shall be generated and referenced to a copy of
      this map and submitted to the Contracting Officer for approval prior to flying aerial
      photography (see Flight Plan). The Client Contract Map may be prepared by the
      Client or by the Contractor at the request of the Client.

  Conditions During Photography:
      Photography shall be undertaken only when conditions meet capture specifications
      as described below.

      Vertical photography shall be flown during the period when deciduous trees are
      barren and when the sun angle or elevation is not less than 33 degrees above the
      horizon (Mountain area: e.g. west of the Blue Ridge Escarpment shall be limited to a
      sun angle or sun elevation of not less than 38 degrees above the Horizon). The
      precise line of demarcation between 33 degrees and 38 degrees shall be defined by
      the contracting officer. It shall be the contractor’s responsibility to monitor
      atmospheric conditions such as haze, dust, fog, water vapor, etc., and adjust the

                                         13

 NC Technical Specifications for Digital Orthophoto Base Mapping
                               2014

     flight time window to maintain visual image quality. If possible the flight window
     should be centered on solar noon. The United States Naval Observatory has an
     online Sun Angle Calculator and the present web address is:
     http://aa.usno.navy.mil/data/docs/AltAz.php .
     The Contracting Officer may require a higher sun angle to reduce the risk of long or
     objectionable shadows caused by relief, vegetation or manmade objects. Images
     will not be undertaken when atmospheric conditions such as moisture, haze, fog, or
     dust will hinder the capture of clear imagery of the ground. Images will not be used
     in orthophotography production that show streams not within their normal banks.
     When an area is obscured by snow, clouds, cloud shadows and/or smoke, the
     obscured area will be evaluated for the nature of ground cover and improvements.
     The Contracting Officer has the authority to accept or reject the inclusion of
     obscured areas. If rejected a refight may be required. Images shall only be used in
     the production of Orthophotography project when capture specifications are met.
     Manufactured snow areas (Ski Slopes), snow piles from roads and parking lots, or
     other clearing activity and remnant snow areas (small patches of snow remaining in
     shadows) are exempt from the requirement. If the contractor has a question about
     flooding or snow extent the contracting officer is to be consulted. Re-flights of
     areas obscured by smoke from forest fires or control burns shall be required once
     smoke conditions have ceased. Single point sources fires where the smoke is
     minimal and does not appear to obscure manmade structures may be acceptable with
     contracting officer approval. Obscured ground features due to permanent smoke
     sources such as cooling towers or industrial smoke stacks cannot be avoided but the
     contractor should make efforts to minimize the obscurity. The contracting officer
     may set additional project restrictions if it is felt that these restrictions would insure
     additional usefulness of the product. Lunar tide levels or wave conditions on large
     open bodies of water are examples that could have additional requirements

Ground Sampling Distance (GSD) for Final Orthoimagery Deliverable:
Map Class or Map Scale shall have the pixel size of the final deliverable product:
Description    Map Scale       Ground Sampling Distance   Recommended Land Cover
Class D        1’= 400’                1.00 ft pixel           Rural
Class C        1”= 200’                0.50 ft pixel           Suburban / General overall
Class B        1”= 100’                0.25 ft pixel           Urban

                                          14

 NC Technical Specifications for Digital Orthophoto Base Mapping
                               2014

Class A         1”= 50’                0.125 ft pixel         Ultra-Urban

Actual Image Acquisition Geometry
     The flight plan shall be designed such that the actual image acquisition geometry
     meets the following GSD and overlap specifications.

          Nadir Ground Sample Distance (GSD) for acquisition
          1.     Nadir GSD shall be between 70% less than ortho specification (0.15 feet
                 for .50 feet GSD) to GSD ortho specification (0.50 feet GSD) for 75.0%
                 of planned exposures or pseudo exposures for the pushbroom cameras
          2.     Nadir GSD shall not be less than 76% less than ortho specification (0.12
                 feet for .50 feet GSD) or greater than 6% greater than ortho specifications
                 (0.53 feet for .50 feet GSD) of planned exposures or pseudo exposures for
                 the pushbroom cameras
          3.     For pushbroom cameras, GSD nadir values will be computed at pseudo
                 exposure station spacing along the flight line at 400 times GSD (200 feet
                 for .50 feet GSD) intervals
          4.     If either Nadir GSD actual image acquisition specification is not met,
                 then re-flights may be directed at the sole discretion of the Contracting
                 Officer after consultation with the vendor

          Transportation Feature Ground Sample Distance (GSD)
          1.     Transportation feature GSD shall be between 70% less than ortho
                 specifications (0.15 feet for .50 feet GSD) to 10% greater than ortho
                 specifications (0.55 feet for .50 feet GSD) feet for 98.0% of tested points
          2.     Transportation feature GSD shall not be less than 80% less than ortho
                 specifications (0.10 feet for .50 feet GSD) or greater than 20% greater
                 than ortho specifications (0.60 feet for .50 feet GSD)
          3.    For pushbroom cameras, transportation feature GSD values will be
                 computed at a distance not to exceed 200 times GSD (100 feet for a .50
                 GSD) foot spacing along the flight line
          4.    If either Transportation feature GSD actual image acquisition
                 specification is not met, then re-flights may be directed at the sole
                 discretion of the Contracting Officer after consultation with the vendor

                                          15

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Flight Plan:
     The Contractor's flight plan shall be overlaid on the Client Contract Map. The map
    may be digital or hard copy at the Client’s discretion. Every effort shall be made to
    avoid breaks within individual flight lines. When breaks within a flight line are
    necessary, the entire flight line composed of the resulting segments shall meet all of
    the requirements set forth in these specifications. Where breaks occur, there shall be
    forward overlap between flight lines to ensure at least 10,000 times the final
    orthoimagery Ground Sample Distance (GSD) of stereo coverage. (See Ground
    Sampling Distance (GSD) For Final Orthoimagery Deliverable.) For pushbroom
    sensors, the replacement imagery shall include full forward and aft stereoscopic
    coverage. All photos within a single flight line shall be acquired with the same
    aerial sensor and with the sensor oriented in the same direction. The principal points
    of the first two and the last two exposures of each flight strip shall fall outside the
    boundaries of the area to be mapped. For pushbroom sensors, the flight design shall
    ensure that the forward and aft imaging arrays coverage fall outside the ends of each
    strip to accommodate stereo viewing of the entire project area. All side boundaries
    shall include an overlap at least equal to the sidelap specifications for the project.
    The flight plan will be designed using the primary side and forward overlap
    percentages specified in Forward Overlap and Side Overlap. The flight plan
    submitted to the Contracting Officer is to be executed by the contractor. The
    rejection limits incorporated within Forward Overlap and Side Overlap are to help
    with unforeseen flying conditions and will not be used as the minimum criteria for
    the basic flight plan. In addition the Contracting Officer may include special flight
    lines for areas of interest; tall bridges, tall buildings, deep gorges, etc. These areas
    will be flown as close to nadir as possible (by increased forward and/or side overlap
    or direct feature overhead exposure) and be included in the orthoimagery.

Re-flights:
     Within one week of the flight mission, the Contractor shall submit a detailed quality
    control report to the Contracting Officer confirming compliance to the aerial
    photography specifications. If the Contractor cannot meet the one week reporting
    time frame the Contractor shall inform the Contracting Officer in advance of the
    delay. Unacceptable aerial photography shall be corrected by the Contractor at no
    additional cost to the Client, with re-flight coverage overlapping the accepted
    photography by at least 10,000 times the final orthoimagery Ground Sample

                                        16

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   Distance (GSD) of stereo coverage. For pushbroom sensors, the replacement
   imagery shall include full forward and aft stereoscopic coverage. Replacement
   exposures shall be acquired with the same sensor make and model used to acquire
   the original exposures and shall be exposed as nearly as possible to the same time
   and lighting conditions as the original exposures. Re-flights shall be flown
   immediately (ideally within one week of the original flight), provided ground
   conditions have not yet terminated the photographic “season.” A Digital Sensor
   System or its components may be substituted if approved in writing by the Client.

   The contractor will apply a file naming convention for all exploitation images that
   shall adhere to the following guidelines:
     1. StudyAreaNumber_FlightLine_FrameNumber (Use all underbars, not dashes).
          EXAMPLE: SA3_100_01
     2. Initial planned flight line numbers will be represented as three digits (e.g.
          100/101/102 or 001, 002, 003). The flight line number for re-flights will be
          represented as four digits by adding increments of 1000 up to 9000 to the
          initial flight line designation (e.g. 1100/1101/1102 or 2001, 2002, 2003).
     3. For the frame, there will be leading zeros only on frames 1-9 (01, 02, 03).

Spacing of Photographs:
      Overlapping photographs in each flight line shall provide full stereoscopic
     coverage of the area to be mapped. Flight line planning shall use the 60% forward
     overlap and 30 % side overlap as constraints over a digital terrain model. Varying
     flight line spacing and varying photo center spacing along the flight line are
     recommended in achieving the overlap requirements to comply to
     minimum/maximum GSDs from terrain variations within raw imagery At all times
     pixel size (GSD) requirements shall be maintained. The Client may specify a
     digital elevation model to be used for the flight planning.

             Forward Overlap (not applicable to pushbroom cameras):
                    Planned forward overlap between successive exposures shall
                    average no less than sixty percent (60%) plus or minus two percent
                    (±2 percent). Greater forward overlap may help reduce building
                    lean. Clients shall have the option when dealing with large
                    changes in elevation due to natural ground elevation or man-made

                                      17

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                differences such as a tall building to increase forward overlap
                requirements. Dependent upon the local terrain variation and
                direction of the Contracting Officer, the contractor should either
                use 2-D flight planning with the flying height set to average mean
                elevation over the planned flight lines or use full 3-D flight
                planning software in conjunction with a terrain model of the
                project area. As a rule of thumb any project area with elevation
                variations of 2,000 times or more the final orthoimagery Ground
                Sample Distance (GSD) requirements or greater is a good
                candidate for 3-D flight planning with a terrain model. With 3-D
                flight planning, flight line spacing and exposure spacing may vary.
                Adhering to project GSD specifications shall be required regardless of
                2-D or 3-D flight planning used to prepare the project flight plan.
                Deviation from the planned image acquisition to the actual image
                acquisition resulting in a forward overlap of less than fifty-five
                percent (55%) may be cause for rejection of a flight line or any
                portion thereof, and shall be subject to re-flights as determined by
                the Contracting Officer.

          Side Overlap:
                Planned side overlap between adjacent parallel flight lines shall
                average no less than thirty percent (30%) plus or minus two
                percent (±2 percent). Greater side overlap may help reduce
                building lean. Clients shall have the option when dealing with
                large changes in elevation due to natural ground elevation or man-
                made differences such as a tall building of increased side overlap
                requirements. Dependent upon the local terrain variation and
                direction of the Contracting Officer, the contractor should either
                use 2-D flight planning with the flying height set to average mean
                elevation over the planned flight lines or use full 3-D flight
                planning in conjunction with a terrain model of the project area. As
                a rule of thumb any project area with elevation variations of 2,000
                times or more times the final orthoimagery Ground Sample
                Distance (GSD) or greater is a good candidate for 3-D flight

                                  18

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                   planning with a terrain model. With 3-D flight planning, flight line
                   spacing and exposure spacing may vary. Adhering to project GSD
                   specifications shall be required regardless of 2-D or 3-D flight
                   planning used to prepare the project flight plan. Deviation from the
                   planned image acquisition to the actual image acquisition resulting
                   in a side overlap of less than twenty-five percent (25%) may be
                   cause for rejection of a flight line or any portion thereof, and shall
                   be subject to re-flights as determined by the Contracting Officer .

     Angular Exterior Orientation Parameters for Actual Image Acquisition

       1. Omega (Roll):
           Omega of the sensor from verticality at the instant of exposure shall not
           exceed three (3) degrees, nor shall it exceed five (5) degrees between
           successive exposure stations. Absolute average omega over the entire
           project shall not exceed one (1) degree.

       2. Phi (Pitch):
           Phi of the sensor from verticality at the instant of exposure shall not
           exceed three (3) degrees, nor shall it exceed five (5) degrees between
           successive exposure stations. Absolute average phi over the entire project
           shall not exceed one (1) degree.

       3. Kappa (Yaw)
          Kappa shall not exceed three degrees (3º) from the planned flight line
          orientation nor deviate more than three degrees (3°) measured with respect to
          any two successive exposures.

            Deviation from the angular exterior orientation parameter specifications
            stated above may be cause for rejection of a flight line or any portion
            thereof, and shall be subject to re-flights as determined by the Contracting
            Officer.

                                     19

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Aircraft:
     The aircraft to be used shall be equipped with all essential geodetic GNSS-IMU
     navigational and photographic instruments and accessories including, sensor
     position and sensor orientation necessary to satisfactorily produce the required
     imagery. The aircraft and sensor system shall be operated by a well-trained and
     experienced crew. The GNSS-IMU system shall be integrated into an aerial survey
     Flight Management System to provide navigation along the proposed flight lines and
     real time precise sensor positioning and sensor orientation. The geodetic GNSS-
     IMU navigation system must also have the capability to capture and store spatial
     positioning information for determining exterior orientation of the sensor and
     geographic location of the photo center at the instant of exposure.

     The design of the aircraft shall be such that, when the sensor is mounted with all
     of its parts above the outer structure, an unobstructed view is obtained, shielded
     from exhaust gases, oil, effluence, and air turbulence. There is neither a
     requirement nor a prohibition to place the camera lenses behind a port glass in the
     aircraft. The sensor shall be mounted vertically in the aircraft in a gyro stabilized
     mount designed to isolate the sensor from angular motion and vibration of the
     aircraft. Angular vibration of the sensor shall be reduced to such a level so as to
     have no significant detrimental effect on resolution.

     The aircraft shall have a proven service ceiling with an operating ceiling of not
     less than five percent (5%) above the highest altitude requirements to secure the
     specified imagery. It shall be the responsibility of the Contractor to secure all
     licenses and authorizations for overflight of contract areas and to secure necessary
     permits or clearances for controlled or restricted airspace areas. If the flight area
     includes a military installation, the Contractor must comply with security
     regulations. The Contractor shall notify the Contracting Officer as soon as
     possible if difficulties in obtaining the appropriate authorizations are encountered.
     The Contractor shall be responsible for operating and maintaining the aircraft in
     accordance with all applicable regulations of the Federal Aviation Administration.

                                       20

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Digital Sensor System:
     The digital sensor system shall have the following general, large-format digital
     camera characteristics:
        1. The cross track width shall be approximately 12,000 pixels or greater.
        2. Simultaneous capture of red, green, blue, and infrared for each exposure.
            A captured radiometric resolution of at least 12 bits/pixel (bpp) for each
            band/channel.
        3. If utilized, a pan-sharpening ratio of 5:1 or better.
        4. Include a gyro stabilized mount, survey grade GNSS components, and an
            Inertial Measurement Unit (IMU).
        5. The Contractor shall present the most recent manufacturer’s calibration
            certificate or the manufacturer’s most recent Geometric Calibration
            Verification Report for each digital sensor system. The Contractor shall
            also present proof that the digital sensor system has been approved by the
            State of North Carolina for orthoimagery projects within the past 4 years.

            The State of North Carolina, through the North Carolina Geodetic Survey,
            maintains a digital camera validation range in Surry County for the
            purpose of testing, evaluating and certifying digital imagery sensor
            systems for use on orthoimagery projects in North Carolina. In order to
            receive approval from the State of North Carolina, potential contractors
            are required to acquire GNSS-IMU controlled digital imagery at least
            every 4 years at the validation range and submit aerotriangulation data and
            orthophotos for evaluation by the state. Upon satisfactory evaluation of
            the Contractor submittals, the NCDOT Photogrammetry Unit will issue an
            Advisory Report indicating the digital sensor system is approved for
            orthoimagery projects in North Carolina

Digital Image Data Files:
     Digital image data files and any interim or final products are the property of the
     Client. The Contractor will be responsible for storage of digital image data files
     under proper file maintenance and backup procedures for a period of at least 5
     years at the contractor’s cost. Digital data should be stored on negotiated media;
     internal servers and/ or redundant external hard drives. All digital media should be
     readable by both Windows and UNIX systems. All digital media should contain
     finalized closed sessions, no multi-session discs. All digital media should be
     properly labeled. The Contractor shall not make, sell, or loan copies of the digital

                                      21

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     image files or any other products without the expressed written approval of the
     Contracting Officer. The data file shall be handled carefully before, during, and
     after authorized use to ensure that the quality is not degraded and is safeguarded
     from defects. It is the Contractors’ obligation to inform the Client if he is no
     longer able to meet the 5 year storage requirement due to going out of business
     and provide an opportunity to transfer the records to the Client or their designee.

Digital Sensor Exposure History:
     The contractor shall be responsible for the following deliverables as a minimum
     requirement: GNSS-IMU Post Processed or Aerotriangulated Exterior
     Orientation Parameters (NC State plane coordinates). For the pushbroom camera,
     exterior orientation parameters and GNSS time shall be provided at spacing equal
     to nominally times the final orthoimagery Ground Sample Distance (GSD).
         1. Date and time of exposure (GNSS time)
         2. Aircraft tail number
         3. Sensor manufacture, model, serial number
         4. Planned and actual altitude (MSL)
         5. Sensor-specific settings.
         6. Exposure ID
         7. Flight line ID
          (The file format shall be specified by the contracting officer)

Flight Log:
   For each flight day, the pilot or sensor technician shall prepare a signed flight log
   containing the date, project name, aircraft used, and names of crew members. In
   addition, the following shall be prepared for each flight line: altitude, digital sensor
   make and serial number, beginning and ending exposure numbers and times, and
   any other comments relative to the flight conditions. Pertinent data about the sensor
   settings shall be included. These flight logs, or copies, shall be delivered to the
   Contracting Officer at the end of the project flights.

Exploitation Images:
   Exploitation images result from post-processing by sensor-specific software and are
   ready for introduction into the production process. All radiometric and geometric

                                       22

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   calibrations have been applied, but the images shall be in full (original) bit depth
   (e.g.: 12 or more bits per pixel) and include all contracted bands. This imagery shall
   be supplied in GeoTIFF format with overviews and accompanying TFW (TIFF
   World) files establishing approximate position and orientation in the project
   reference frame. These images, combined with aerotriangulation (or
   geopositioning) data shall be directly viewable in a stereoscopic imagery
   workstation. A shape file shall also be delivered that represents the image exposure
   stations in the project reference frame. The shape file attributes shall include, at a
   minimum, the textual name of the sensor system, the serial number of the sensor
   system, the name of the image file, exposure date, exposure time, position (x,y,z),
   orientation (omega, phi, kappa), and focal length. The contracting officer may
   approve the substitution of an excel file for the shape file for all or part of the
   information.

                                       23

   NC Technical Specifications for Digital Orthophoto Base Mapping
                                 2014

                             SECTION 3
      HORIZONTAL AND VERTICAL
             CONTROL

HORIZONTAL AND VERTICAL CONTROL
   General:
      Sufficient horizontal and, if applicable, vertical control surveys shall be established
      by the Contractor for all photogrammetric mapping purposes. Prior to the
      establishment of the necessary basic horizontal and vertical control, the Contractor
      shall make a thorough search of the project area for existing control that has
      published (by the National Geodetic Survey or NC Geodetic Survey) NAD 83
      horizontal positional information of the latest realization of NAD 83(at the time of
      the adoption of the standards the realization was NAD83 (2011) epoch 2010.0,as
      established by the National Geodetic Survey (NGS, formerly the United States Coast
      and Geodetic Survey [CGS]), North Carolina Geodetic Survey (NCGS), or the
      North Carolina Department of Transportation (NC DOT). North Carolina Geodetic
      Survey (NCGS) Station Recovery Forms are to be filled out using online forms and
      electronically submitted to NCGS on monuments that a recovery effort was made.
      This includes both monuments found and monuments not recovered or destroyed.
      Additional control points established by the Contractor may require permanent
      monuments as described in subsection Horizontal and Vertical Control –
      Permanent Monuments. All such control recovered or established shall be utilized
      to the fullest extent. All control used in the project will be paneled prior to flying
      the aerial imagery acquisition unless such control is clearly a photo-identifiable
      point. The Contractor will indicate on a copy of the Client Contract Map the
      horizontal control stations (existing and to be established). Control previously
      established in an adjacent county will be utilized by the Contractor to the fullest
      extent possible to assure compatibility of maps from county to county. The
      Contractor will provide the Contracting Officer a brief description of the equipment

                                          24

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   and methods to be used for new ground surveys prior to conducting any control
   surveys. All horizontal and vertical control surveys shall be performed using
   procedures and/or accuracy standards consistent with professional surveying and
   photogrammetric practices. The use of Airborne Global Navigation Satellite System
   (ABGNSS) in combination with ground survey is required; the amount of ground
   control may be reduced but not eliminated by the use of ABGNSS technology. All
   ground control surveying activities will be directed, approved, and certified by a
   North Carolina Professional Land Surveyor whose area of expertise is surveying.

Horizontal Control Surveys:
   All basic horizontal control shall be established by Global Navigation Satellite
   System (GNSS). At a minimum, all horizontal ground control placed as a result of
   this project shall be established at an accuracy level of Class AA (Local Control
   Network Surveys, 21 NCAC 56.1603) or better. OPUS-S. RS and the using of the
   NC Real Time Network are acceptable as long as the results meet or exceed Class
   AA (Local Control Network Survey) standards. NCGS and FGDC standards as
   applicable to the order and class of survey shall be followed. All horizontal control
   shall be correlated to the North Carolina Official Survey Base as defined in NC GS
   Chapter 102 and adjusted to the latest realization released by the National Geodetic
   Survey. At the time of the adoption of this standard that was NAD83(2011) epoch
   2010.0. Said survey shall be certified in accordance with the North Carolina Board
   of Examiners for Engineers and Surveyors (21 NCAC 56.1607).

Vertical Control Surveys:
   All basic vertical control shall be established by Global Navigation Satellite System
   (GNSS) using NGS-58 guidelines and/or traditional leveling techniques (21 NCAC
   56.1605). At a minimum, all vertical ground control placed as a result of this project
   shall be established at an accuracy level of Third Order Class I or better. NCGS,
   NGS, and FGDC standards as applicable to the order and class of survey shall be
   followed. All vertical control shall be correlated to the North Carolina State Plane
   Coordinate System, National Geodetic Vertical Datum (NAVD), 1988.

                                      25

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Photo Control Points:
   The Contractor is required to establish a sufficient number of control points to meet
   the accuracy requirements of the project. Control points may be photo-identifiable
   points or targeted control points. Control points may be marked and targeted for
   aerial imagery and then surveyed after the imagery has been flown. Control points
   that are not painted or paneled targets may also be used. Permanent features such as
   parking lot corners, sidewalk or driveway intersections, street corners, cattle guard
   corners, fence intersections, and other such clearly defined features selected by the project
   surveyor can also be used. These points may then later be used for subsequent
   acquisition of city, state, or national programs such as NAIP since they do not need
   to be repainted or paneled. Control points shall be situated on well defined, distinct,
   and photo-identifiable features or points that have been targeted by the Contractor
   (see Horizontal and Vertical Control - Targeting).
      Control points shall be:
          1. Situated at or very near ground level, not on an elevated surface.
          2. Have a clear view of the sky
          3. Located in relatively level terrain, away from steep embankments.
          4. Located in areas where the target has a high probability of remaining
              undisturbed during the project.
          5. Located outside of areas that may be covered by shadows at time of
              minimum sun angle.
          6. Semi permanent markers, such as nails, should be set when possible to
              define the exact location of survey point observed. Example: PK nail set at
              the corner intersection of a private driveway and public roadway or PK
              nail set at the end of a paint stripe.

   Note: if photo-identifiable points are use, the accompanying location description
   shall be sufficient to positively identify the designated point.

Permanent Monuments:
   If requested in writing by the Contracting Officer, some or all control points
   established by the Contractor will be monumented with permanent monuments
   which meet the requirements for permanent monuments established by the NCGS.
   Said monument information is to be submitted by the Contractor to NGS Opus

                                         26

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   database for publication if Opus is used, if a static observation is used the monument
   report shall be submitted as is required in Control Data section of this standard.

Survey Records:
   The following information shall be delivered to the Contracting Officer as hard copy
   and a digital (ASCII) file:

     Field Notes and Observation Logs.
        Field Notes and Observation Logs shall be carefully and neatly prepared,
        identified, indexed and preserved. All data regarding the establishment and
        extension of horizontal and vertical control, including descriptions of all
        established and recovered monuments, shall be recorded. Where existing
        control points are recovered by the Contractor in extending the basic control,
        the field notes shall contain:
        (1)    Information as to the general condition of the recovered mark,
        (2)    The original description,
        (3)    Exact letter and numbers stamped on (not cast in) the mark,
        (4)    Amended description, if applicable,
        (5)    Additional tie data, if any,
        (6)    A sketch of the location as appropriate to facilitate future recovery.

     Observation Logs shall contain:
        (1)    Monument name and location
        (2)    Name and title of the observer
        (3)    Time of arrival at monument
        (4)    Height of instrument at beginning of observation (in feet and meters)
        (5)    Type and serial number of the GNSS receiver(s)
        (6)    Type and serial number of the Tribrach(s) or type of fixed height pole
        (7)    Observation period (indicate if programmed)
        (8)    Epoch rate
        (9)    Satellites observed
        (10)   Height of instrument at end of observation (in feet and meters)
        (11)   Additional notes describing problems encountered during the
               observation period

                                       27

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     An additional sheet containing an obstruction diagram shall be provided for each
     existing and/or new monument observed. North Carolina Geodetic Survey
     (NCGS) Station Recovery Forms are to be filled out and submitted to NCGS on
     searched for monuments. Each baseline shall be identified by a number and brief
     description in the field notes. If the field notes are electronically recorded,
     printouts of the electronically recorded field notes shall be provided.

     Computations.
       The Contractor shall do all computations necessary to comply with 21 NCAC
       56 .1607 GLOBAL POSITIONING SYSTEMS SURVEYS at a minimum.
       Said Computations will be provided to the contract Officer upon request.

   Control Diagram.
     The Contractor shall furnish a control diagram report indicating all horizontal and
     vertical control pertinent to this project on a copy of the Client Contract Map.
     This report shall document all existing and established control points utilized in
     the project with sufficient metadata to identify the location of the control points. .
     The report shall be delivered to the client in the format requested by the client.

   Control Data.
     The Contractor shall provide the Contracting Officer with the complete
     information as listed below for all monumented control points established and/or
     recovered by the Contractor:
        1.   Information on control points established by the Contractor shall include
             the following information.
             (a) Designation of station (County name and sequential number).
             (b) Establishing agency (name of Contractor or subcontractor who
                    established the control point).
             (c) Date of establishment.
             (d) Horizontal and/or vertical control data.
             (e) A complete description of the nature and location of the point to
                    include the coordinate of the point and identified by field survey

                                       28

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

                    ties (bearing and distance) to three or more definable photo image
                    points in the immediate vicinity.
              (f)   The location of all horizontal control points, shall be provided in a
                    Shape file oriented in the project coordinate system, and shall
                    include each station designation. (See section (a) of this section)
        2.    Information on existing points recovered by the Contractor. The
              information will be submitted on a completed NCGS Station Recovery
              Form (see the web based form at NCGS’s web site).

     GNSS Observation Summary.
             The observation summary shall contain a discussion of the results of the
             ground GNSS survey, including accuracies achieved, problems
             encountered, and a statement of the overall quality of the survey. The
             summary must contain the signature and seal of the Professional Land
             Surveyor certifying that the survey meets accuracy requirements and is
             tied to the proper datums.

Feet/Meter Conversions:
   The U. S. Survey Foot (l meter = 3.2808333333 feet) shall be used in all
   conversions of North Carolina State Plane Coordinates from meters to feet or feet to
   meters. All final control data shall be in feet, and the datum used (e.g.
   NAD83(2011) epoch 2010.0) , and Geoid will be noted on any sheets bearing
   coordinates.

Global Navigation Satellite System (GNSS):
   All basic horizontal and vertical control shall be established by GNSS. All GNSS
   network design, observation techniques, and data adjustments must be according to
   the specifications in the most current FGCC “Geometric Geodetic Accuracy
   Standards and Specifications for using GNSS Relative Positioning Techniques and
   the most resent specifications and standards adopted by North Carolina Geodetic
   Survey, including NAD and Geoid.

                                      29

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Global Navigation Satellite System & Inertial Measurement Units
(GNSS-IMU):
    The use of post processed airborne GNSS-IMU exterior orientation in combination
    with ground survey is required; the amount of ground control may be reduced but
    not eliminated by the use of GNSS-IMU technology. The following specifications
    shall be met for airborne GNSS-IMU exterior orientation:

     General.
            Airborne GNSS-IMU solutions shall be required to utilize dual-frequency
            GPS systems during the aerial imagery missions. The Contractor shall
            post-process the airborne GNSS-IMU data relative to simultaneous
            observations collected at fixed land-based reference stations. Geodetic
            positions corresponding to the photo centers at the instant of exposure
            shall be calculated and (later) combined with ground control point values
            in an analytical aerotriangulation solution.

     Accuracy.
            Sensor perspective centers must have accurately located position offsets
            with respect to the GNSS antenna phase center positions.

     Ground Stations.
            Simultaneous with the aerial imagery acquisition and use of airborne
            GNSS-IMU data, a minimum of two static GPS reference receivers must
            be used to record satellite data over known geodetic control points on the
            ground. CORS maintained by North Carolina Geodetic Survey may be
            used to meet this requirement. These additional receivers must be active
            during the entire flight mission. The base stations must be in the most
            appropriate locations within the project area.

     Satellite Geometry.
            It is the duty of the contractor to verify that space weather and satellite
            geometry is suitable of accurately positioning the aircraft to meet the
            requirements of this project.

     Post-processing Software.
            The GNSS-IMU post-processing software must be capable of backward
            and forward processing.

                                      30

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     Reporting.
             At the conclusion of Airborne GNSS collection, the Contractor shall be
             required to submit a report of GNSS observations and results data,
             observation logs, and data analysis and adjustments as part of a combined
             GNSS-IMU Post Processing and Aerotriangulation Report. This report
             shall be kept for reference. The Client reserves the right to obtain any and
             all data, readings, records, or any other information relating to the conduct
             of the survey for this project from the Contractor. This information is part
             of the official report and will be required to meet the requirements of the
             North Carolina Board of Examiners for Engineers and Surveyors rules.

Targeting:
     It is the responsibility of the Contractor to place the ground control targets (panels),
    to monitor and repair the targets to ensure that targets have not been damaged or
    removed before the aerial imagery acquisition has been completed, and to remove
    the targets in a timely fashion once the aerial imagery acquisition has been
    completed. A notice shall be attached to each target identifying the contractor
    responsible for the targets with contact information and anticipated time of target
    removal. Targets shall be of an appropriate size, color, and shape to adequately
    appear on the selected scale of aerial imagery.

Property Entry:
   Targets and ground control points should be placed on public property whenever
   possible; however, it is recognized that it may be desirable or necessary to locate
   some targets and control points on private property. It is the Contractor’s
   responsibility to obtain owner’s permission when it is necessary to pass through or
   locate targets or control points on private property. At the written request of the
   Contractor, the Contracting Officer will assist in any reasonable effort to attain
   permission for entry to private property.

                                        31

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Target Removal:
   Paneling material shall be removed by the Contractor, at the Contractor’s expense
   within 30 days after final flight approval. If the targets are painted, the paint should
   be such a type that is biodegradable and will wash away over a relatively short time.

                                       32

   NC Technical Specifications for Digital Orthophoto Base Mapping
                                 2014

                             SECTION 4
    ANALYTICAL TRIANGULATION

ANALYTICAL TRIANGULATION:
   Aerotriangulation (general):
        Aerotriangulation is essentially an interpolation tool, capable of extending control
        points to areas between ground survey control points using several contiguous
        uncontrolled stereomodels. The Contractor shall use fully analytical
        aerotriangulation to extend the horizontal control from relatively few ground
        survey control points to additional supplemental control points – pass points.
        Each stereomodel is to be scaled and leveled using the adjusted coordinate values
        of the pass points located in the stereomodel. Ground control should be located
        along the perimeter of the project area and within the project area; should be
        added as necessary to limit error propagation in the adjusted pass point
        coordinates. The use of post preprocessed airborne GNSS-IMU data in
        combination with ground control surveyed points is required. The amount of
        ground control may be reduced but not eliminated by the use of airborne GNSS-
        IMU technology. An aerotriangulation solution should be limited to the areal
        extent of ground control wherever feasible, but may be extended beyond ground
        control boundaries by airborne GPS-IMU data where ground control is not
        feasible such as across large water bodies, into restricted military ground space,
        into large rural forested inaccessible areas, etc. (beyond the ground control of the
        project area). In conducting the aerotriangulation, the Contractor shall perform a
        fully analytical simultaneous bundle adjustment using a weighted least squares
        adjustment to meet project accuracy requirements.

                                         33

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Nominal Scales for Triangulation:
     Aerial triangulation may be used for horizontal scaling to produce maps of 1" =
     400', 1" = 200', and 1" = 100'.

Ground Coordinate Systems:
     All ground positions determined by aerial triangulation will be in the North
     Carolina State Plane Coordinate System (see 3.02 and 3.03), Based on the NAD +
     Realization and NAVD + Geoid as adopted by NC Geodetic Survey. The
     contracting officer may require additional deliverables that are converted to
     another datum.

Aerotriangulation:
     Aerotriangulation shall be accomplished by procedures that involve fully
     analytical aerotriangulation software. The Contractor must follow accepted
     aerotriangulation procedures and utilize equipment that will achieve the
     aerotriangulation accuracy required to meet or exceed required orthophoto
     accuracy standards. Software and hardware used by the Contractor must be
     capable of model orientation in both the stereo and monoscopic modes, capable of
     interior, relative, and absolute orientation, as well as single image resection.
     Manual or auto correlated pass and tie point image measurement is acceptable.
     The contractor will have image measurements for frame sensors at the 9
     traditional Von Gruber locations per image. Those measurements will be made
     available to the contracting officer upon request. In regions of frame imagery
     where auto-correlated image measurements are not produced at the 9 traditional
     Von Gruber locations per image as a minimum, the Contractor shall make every
     effort to manually measure pass or tie points. For pushbroom sensors, pass points
     shall be located along each strip at intervals corresponding to, at a minimum, half
     of the nadir imaging array format width. Additionally, tie points in overlapping
     strips shall be measured at the same interval. If the Contractor elects to use
     photogrammetrically derived coordinates as “tie control points” between adjacent
     aerotriangulation blocks, then these points shall be manually measured on the
     ground surface, preferably at a photo-identifiable feature. The Contractor is

                                     34

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     ultimately responsible for designing the aerotriangulation scheme that will meet
     the accuracy requirements of the project.

GNSS-IMU Post Processing & Aerial Triangulation Report:
     Immediately upon completion of all aerial triangulation, the Contractor will
     prepare a formal aerial triangulation report for submission to the Contracting
     Officer. Two copies of the report are required and shall include, but not be
     limited to, the following:

     Control and Flight Line Indexes.
        1.    Flight lines
             • Exposure stations or model layout identifying digital camera and date of
                 acquisition
             • All control points and check points appropriately labeled with
                 identification designation.
             • All indexes will be generated strictly from digital data sources and are
                 printable on suitable materials at a scale suitable for presentation. The
                 indexes will contain grid lines labeled with their corresponding northing
                 and easting coordinate grid values. The indexes will also be labeled
                 with the County name, map scale, title, and date. Digital index files
                 such as shapefiles and/or pdf drawings are a required deliverable.

        2.    Aerial Triangulation Results.
             • Sigma naught.
             • GNSS accuracy of sensor. For pushbroom systems, the accuracy of the
                trajectory solution shall be presented.
             • Standard errors of adjusted tie-point terrain coordinates (RMS errors in
                x, y for horizontal coordinates) referenced to photo scale in micron and
                ground units.
             • Standard error of adjusted tie-point terrain coordinates (RMS errors of z
                vertical coordinates) referenced to photo scale in micron and ground
                units.
             • RMS errors (absolute accuracy) of x, y and z at independent
                checkpoints in microns at photoscale and in ground units.

                                       35

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

            •  Space resection parameters for each frame of aerial imagery included in
               the aerial triangulation adjustment. This requirement does not apply to
               pushbroom systems.
            • All misclosures at ground control points with and without use of
               checkpoints.
            • Computer printout of the final adjusted aerial triangulation solution to
               horizontal and vertical ground control. The printout should contain the
               final State Plane Coordinates for all ground control points, pass points,
               and checkpoints.
            • Identification of all points which were included in the initial solution
               and were subsequently discarded, with an explanation of the reasons for
               being discarded.
            • Identification of the weighting factors applied to all points used in the
               final solution.
            • An ASCII file on approved electronic media containing the coordinate
               data and the results of the FAAT adjustments.
            • An RMSE report of ground control held back and used as checkpoints
               (not to include photogrammetric determined pass or tie points)
               independent of a subsequent final RMSE report that incorporates all
               included ground control.

       3.       Narrative.
                The report shall include a brief narrative tying together items from GNSS-
                IMU Post Processing & Aerial Triangulation Report and Aerial
                Triangulation Results as well as descriptions of equipment, procedures,
                and computer programs used. Root-mean square (RMS) error summaries
                shall be provided for bundle adjustment photographic measurement
                residuals or strip tie point residuals and misclosures at control/check
                points. In addition, significant misfits encountered at control points, and
                steps taken to analyze such misfits and to rectify the discrepancies, will be
                described. All control shall be listed in the report with an explanation of
                how the control was used in the FAAT. Also, the report shall contain a
                statement signed and sealed by the North Carolina Professional Surveyor
                (photogrammetrist) in charge of the project that the aerial triangulation

                                          36

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

             solution will provide sufficient control to produce orthophotos that meet
             the accuracy requirements of the project.

Drop Points:
   Drop points may be used to control lower altitude flights for direct compilation from
   imagery of larger scale. These points shall be marked, measured, and carried as
   extra pass points in the aerial triangulation of the higher altitude imagery. Any drop
   point procedures must be specifically described within the Triangulation report
   narrative.

Blind Checkpoints:
   Blind Checkpoints are horizontal control points that have been established through
   ground control procedures by the Contracting Officer for accuracy checking
   purposes and will not be used in the analytical adjustment. These points are for
   quality control and not to be shared with the Contractor.

                                      37

   NC Technical Specifications for Digital Orthophoto Base Mapping
                                 2014

                              SECTION 5
           DIGITAL ORTHOPHOTOS
DIGITAL ORTHOPHOTOS:
   General:
      A digital orthophoto is a digital image that has the properties of an orthographic
      projection. It is a digital representation from a perspective aerial image by
      differential rectification so that image displacements caused by sensor orientation
      and terrain relief are removed. A simplified work flow is that a digital orthophoto is
      created by using a raw aerial image that is processed into an exploitation image
      which in turn is then rectified to an orthographic projection by processing each
      image pixel through photogrammetric space resection equations. This process
      requires, as input, aero triangulated exterior orientation parameters and a digital
      terrain/elevation model.

   Traditional Digital Orthophotography In Built Up Areas:
      Any aerial imagery will exhibit a characteristic known as relief displacement. Relief
      displacement is the geometric distortion that occurs due to elevation differences in
      the terrain being imaged. Objects of higher elevation, like buildings, hills, and trees,
      will be displaced radially outward from the center of the image. The greater the
      elevation of the object, and the further it is from the center-of-view, the greater the
      radial distortion. The process of ortho-rectification corrects these distortions by
      performing, on the image, a mathematical transformation that takes into account the
      shape of the terrain depicted in the form of a digital terrain model (DTM). In
      traditional digital orthophotography, objects like buildings and bridges are not
      modeled in the DTM. Therefore, the elevated portions of these features are displaced
      from their true location in the final orthophotography. This displacement shows up
      in the form of leaning buildings, towers and warped bridges. In severe cases, this
      displacement can be aesthetically displeasing and may impact the usefulness of the
      orthophotography. For example, a tall building may “lean” over a street, hiding

                                          38

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   information like manholes, fire hydrants, and utility poles. Complex, multi-level
   freeway interchanges appear badly deformed. When a vector GIS layer is overlaid
   with the imagery, building outlines do not match up with the imagery representing
   the tops of the buildings, and vector road edges may appear as passing through
   buildings.

   In the production of orthophotography the Contractor shall use Best Management
   Practices to minimize relief displacement. For tall buildings, the image nearest to
   nadir should be used, building lean should be held to a maximum coverage of 50% of
   the adjacent road where possible. Horizontal displacement along seam lines in
   images shall be held to no more than ±3 pixels along transportation features, unless
   project specifications specifically state otherwise. Clipping of features (e.g. radio
   towers, water tanks, buildings) at seam line boundaries shall be held to a minimum.
   Smearing shall be held to a minimum. Structure warping (bridges) shall be adjusted
   for viewing. While elevated structures normally are not corrected, elevated
   transportation features shall be corrected using Best Management Practices for
   viewing. It is not required that transportation features be adjusted for accurate 3D
   modeling.

Orthophoto Horizontal Accuracy Standards:
   Orthophotos shall meet or exceed the horizontal accuracy standards as follows:
     1.0' GSD - 1"=400' scale - limiting RMSE X or RMSE Y of 3.0 feet

      0.5' GSD - 1"=200' scale - limiting RMSE X or RMSE Y of 1.5 feet

      0.25' GSD - 1"=100' scale - limiting RMSE X or RMSE Y of 1.0 feet

      0.125' GSD - 1"=50' scale - limiting RMSE X or RMSE Y of 0.5 feet

   All orthophotos may be subject to quality control testing by the Contracting Officer,
   by independent third parties, and/or by the Contractor working under the direct
   review of the Contracting Officer to ensure that orthophotos comply with the
   accuracy requirements. See Addendum 2, NC Orthoimagery Quality Assurance

                                      39

 NC Technical Specifications for Digital Orthophoto Base Mapping
                               2014

     (QA) Procedures. If during the quality control testing position anomalies are
     detected, the contractor may be required to investigate said anomalies and explain or
     fix said anomalies even if the total project would pass the Quality Assurance
     Procedures with the anomalies included.

Reporting of Horizontal Accuracy:
     Reporting of Horizontal Accuracy shall be as follows:

       1. "This county orthophoto project was checked and found to have a RMSE X
       value of ________Feet and a RMSE Y value of ______feet which conforms to the
       horizontal accuracy standard as defined in the Orthophoto Horizontal Accuracy
       Standards section of North Carolina Technical Specifications for Digital
       Orthophoto Base Mapping by The Land Records Management Division of The
       North Carolina Department of the Secretary of State and

       2. "This North Carolina orthophoto project was tested using the Case 1 formula
       and procedures set forth in FGDC-STD-007-1998. The result of that test was
       ____________feet horizontal accuracy."

       Horizontal accuracy quality control shall be implemented under the following
       guide lines located at:

http://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part1/chapter1

http://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part3/chapter3

Processed Digital Imagery:
     The finished digital orthophoto shall have an image visually consistent within reason
     relative to the source exploitation image. The following provides a holistic
     approach model whereas a single contractor or multiple contractors are considered
     to ultimately deliver a consistent radiometric product. This product should be one
     defined by minimal adjustment and considers scene dependent factors such as
     acquisition date, time of day, environmental conditions, and landcover:

                                         40

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

  Contractors shall perform exploitation image post processing such that exploitation
  images are visually consistent (within reason) across the following:
     1. across AT blocks within the boundaries of a study area and internally across
         the jurisdictions of sub-contractors
     2. between study areas and specifically in overlap areas
     3. internal to study areas and between multiple sub-contractors
     4. with existing imagery if applicable and/or practical
     5. with existing land cover representative of differing regions
  Exploitation image post processing shall be such that resulting exploitation images
  have the following characteristics when viewing at full (1:1) resolution.
     1. Pavement markings and concrete with pavement interfaces shall have clear,
         well-defined edges with minimum noise, minimum visual artifacts, and the
         absence of “black outlines”.
     2. Imagery should not demonstrate a “haze” effect or kept to the absolute
         minimum.
     3. Achieve good contrast without losing detail in shadow and highlight areas

Digital Terrain Model/Digital Elevation Model:
  1.    A Digital Terrain Model (DTM)/Digital Elevation Model (DEM) shall be
        developed at a density level necessary to support the orthophoto production.
        Terrain/elevation data used in the development of the DTM/DEM may be
        captured by photogrammetric editing/updating techniques from using the most
        recent LIDAR dataset that is approved by the Contracting Officer. The
        Statewide DTM generated by North Carolina Floodplain Mapping Program is
        one example of an acceptable LIDAR product. If an existing LIDAR data set
        is used, the project area must be reviewed to determine if significant terrain
        altering activity has occurred since the LIDAR data was acquired. If such an
        area is identified the contractor shall update the DTM. The DTM/DEM will
        consist of points spaced at regular intervals along a grid, points of significant
        high or low elevations, and ortho specific breaklines at all significant terrain
        breaks. It is not necessary to capture breaklines at all curbs, ditches, stream
        banks, or other similar minor terrain breaks. Elevation/terrain data shall be
        captured at a density level sufficient to accurately represent the shape of the
        ground and to meet the required orthophoto accuracy standards defined in the
        contract.
  2.    The DTM/DEM data is not to be stored as a record (Z component) for each
        pixel of the orthophoto image.

                                      41

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

  3.    The Contractor shall provide to the Client the DTM/DEM in a format that can
        be used on the Client's GIS system or in an acceptable standard data exchange
        format. Note: The DTM/DEM data will be used for the orthorectification of
        images and data sets, and it is acknowledged that the DTM/DEM is not
        suitable for detailed engineering activities.
  4.    DTM/DEM data generated from aerial photography of a prior project shall not
        be used for a new project without a quality control review and then only if
        approved by the Contracting Officer.

Image Completeness:
   There shall be no areas of an orthophoto tile where ortho production process was
   incomplete due to incomplete data (i.e., lack of DTM/DEM data, image gaps, etc.).

Ground Resolution:
   The horizontal ground resolution (pixel - x and y components) of the finished digital
   orthophoto image (both hardcopy and softcopy) shall be at a contracted Ground
   Sampling Distance (GSD).

Image Rectification Algorithm:
   Image rectification shall be carried out using either cubic convolution or better
   algorithm.

Tile Coverage Area:
   The geographic extent of each softcopy digital orthophoto shall be based on the
   North Carolina Land Records Management Program’s "Basic Modular Unit" and
   shall cover the same geographic area. The softcopy digital orthophoto shall only
   contain the neat image of the corresponding map unit, and there shall be no image
   overlap between adjacent softcopy digital orthophotos.

Image Mosaicking:
   Mosaicking shall be accomplished using both automated and interactive (manual)
   methods; the sole use of fully automated methods is not acceptable. Mosaic join

                                       42

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   lines (seam lines) shall not cross through building, bridges, or other structures or
   items which could be considered as a visual entity and shall try to follow features
   such as roads, tree lines, water bodies, etc when possible. Acceptable mosaicking
   must produce quality orthophoto imagery of consistent tone and contrast and must
   do so without obvious join lines.
   1.        Interior mosaicking.
             Interior mosaicking occurs when an orthophoto cannot or is not made
             from a single digital aerial photograph, and the orthophoto is made from
             two or more digital aerial photographs. The join line between photograph
             images shall be chosen so as to minimize the obtrusiveness of the join
             itself and to reduce the difference in brightness, tone and contrast between
             the different photograph images. Interior mosaicking shall not affect the
             positional accuracy of the orthophoto.
   2.        Edge mosaicking and feathering.
             Mosaicking and feathering at/near the edge lines of adjacent orthophotos
             is permitted in order to create a nearly seamless image of the entire project
             area and to minimize any visual edge lines of adjacent orthophotos due to
             tonal variations. The mosaicked edge line between adjacent orthophotos
             shall be chosen so as to minimize the obtrusiveness of the edge line itself.
             If feathering (a process used on the join between two adjacent orthophotos
             to help reduce the difference in tone and contrast between the adjacent
             orthophotos) is used along the edge line, it shall not result in any
             noticeable image degradation such as image blurring or double imagery.
             Edge mosaicking and feathering shall not affect the positional accuracy of
             the orthophoto. The Contractor shall provide the Contracting Officer with
             samples of edge mosaicking and feathering to evaluate. The Contracting
             Officer will select one image set (four adjacent orthophotos) which will
             become the reference to which all sequent softcopy orthophotos will be
             compared for edge mosaicking and feathering acceptance/rejection.

   3.        Radiometry Balance.
             When a mosaic of two or more chips is made, the brightness and color
             values of the other chips will be adjusted to match that of the principal
             chip. The join lines between the overlapping chips will be chosen to
             minimize tonal variations. Localized adjustment of the brightness and

                                       43

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

            color values will be done to reduce radiometric differences between join
            areas.

   4.       Edge-Matching.
            All chips shall not have more than ±3 pixels offset between the principal
            chip.

   5.       Seam Lines.
            The contractor will provide the final seam line data set that was used to
            construct the Othophotos presented for quality control at the same time as
            image delivery. The seam line file shall be in a polygon feature class
            shape file format. The seamline polygon shall contain attribute fields at
            minimum:
                    a. Flight line ID
                    b. Exposure ID
                    c. Image acquisition date

A North Carolina Panel Naming Convention:
    OC6I_37_000_ 20765400_20100601 (name format)

  OC -2 digit product code: O= orthoimagery, C = color. Other product codes OB
     (B&W) OI (Infrared) DE (DEM)
  6I – 2 digit pixel size: 6 = measurement, I= unit of measure 6I = 6 inches. 1F=
     1foot, 1M= 1 meter, etc
  37 – 2 digit NC ANSI (FIPS) Code
  000 – 3 digit alphanumeric custodian code. For county maintained data this would
     be county ANSI (FIPS) code, 000 for statewide, or city code (RAL) agency code
     (DOT)
  20765400 – 8 digit SOS LRM Numbering of the Basic Modular Unit with Millionth
     place digit. (See section 6.17)
  20100601 – 8 digit tile processed date (YYYYMMDD)
  Additional user generated info can be appended at the END of the file name

                                     44

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

Mapping Basic Modular Unit: (8 digit SOS LRM BMU):
             a. The 1" = 400' map is the smallest scale map included in these
                specifications and is designated the "Basic Modular Unit" in a series of
                maps which provide for four map scales, as follows:
             b. 1" = 400'. The boundaries of each Basic Modular Unit shall be the
                grid ticks of the North Carolina State Plane Coordinate System evenly
                divisible by 10,000 ft. in north-south and east-west directions.
             c. 1" = 200'. Each map will be one-quarter (1/4) of a Basic Modular Unit
                (see Attachment 1). The neat image area shall be bounded by the
                North Carolina grid ticks whose eastings and northings are evenly
                divisible by 5,000 feet.
             d. 1" = 100'. Each map shall be one-sixteenth (1/16) of a Basic Modular
                Unit (see subsection Attachment 1). The neat image area of this unit
                shall be bounded by the North Carolina grid ticks with eastings and
                northings evenly divisible by 2,500 feet.
             e. 1" = 50'. Each map shall be one sixty-fourth (1/64) of a Basic
                Modular Unit (see subsection 6.16 a. and Attachment 1). The neat
                image area of this unit shall be bounded by the North Carolina grid
                ticks with eastings and northings evenly divisible by 1,250 feet.

        Final map tiles will conform to the Basic Modular Units as defined in this
        section.

Numbering of the Basic Modular Units:
   Each Basic Modular Unit map shall be identified by a map number derived from
   selected paired digits of the east and north coordinates of the southwest corner of the
   module. For example, a map with the lower left corner coordinates of E = 640,000
   and N = 530,000 will be named as Map Number 6543. The digit "6" in the
   100,000th place of the east coordinate is paired with the digit "5" in the 100,000th
   place of the north coordinate; the digit "4" in the 10,000th place of the east
   coordinate is paired with the digit "3" in the corresponding position in the north
   coordinate. These four digits uniquely define the modular map unit in any one
   county. This map numbering system also forms an integral part of the parcel
   identifier number (PIN) system. In counties where the coordinate values equal or

                                       45

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

   exceed 1,000,000 feet, the digit in the millionth place is redundant and will be
   dropped. However, the map must be clearly identified with its proper county name.
   Thus, the map in Gates County having coordinates for its southwest corner of E =
   2,660,000 and N = 1,010,000 can be identified as Gates County Map Number 6061.
   The map numbers at the 1" = 400' scale will contain only four digits. The map
   numbers at the 1" = 200' scale and the 1" = 100' scale will contain only six digits.
   For these larger scales, the first four digits of the map numbers shall be those of the
   Basic Modular Unit with the addition of a two-digit suffix determined according to
   the chart in Attachment 1. There will be a decimal point between the four digits of
   the Basic Modular Unit and the suffix, for example Gates County Map Number
   6061.15. (See Attachment 1)

Border Data:
   Traditional hardcopy map border data such as map number, north arrow, grid ticks,
   grid coordinate values, etc shall not be a part of the digital orthophoto image. A
   digital border may be included as a user applied overlay if requested by the
   Contracting Officer. If said overlay is included pertinent data will be inserted in the
   boarder overlay from the panel header. If said overlay is available for use at
   different zoom levels the scale ratio should be included in the information within the
   digital border.

Reference Product:
   There shall be sample digital images chosen to represent the overall image quality
   here after known as the reference product. It shall be specified in the contract as to
   who is responsible for the production of the Reference Product. These images shall
   consist of defined different land cover areas: swamp/marsh, woods, rural, urban, and
   industrial/commercial. Contracting Officer will select sample digital image sets to
   evaluate and accept as examples of overall image quality. This Reference Product
   will be the project visual quality control reference standard. If quality control issues
   arise during final review, this Reference Product will be used as the project standard.
   The Contracting Officer will select one or more image sets that will become the
   reference to which all subsequent digital orthophotos will be compared for image
   quality acceptance/rejection. The sets will consist of four or more adjacent, like

                                       46

 NC Technical Specifications for Digital Orthophoto Base Mapping
                               2014

     scale orthophotos and also three or more adjacent, unlike scale (e.g. 100’ against
     200’) orthophotos. Care should be taken to include a variety of visual conditions
     (large white areas – concrete, large dark areas – conifer woods, and large shadows)
     when choosing the reference product. The Contractor and Contractor Officer shall
     agree on the Reference Product area. This procedure may vary from contract to
     contract.

Orthophoto Image Quality:
     The digital orthophoto image shall be compared to representative samples of
     exploitation images, the approved Reference Product and the guide lines listed
     below to determine if image degradation has occurred during the orthophoto
     process. Spot Blurring or haze that does not appear in the original imagery will be
     considered processing error. Depending on the severity, the contractor may be
     required to correct any problems. It is recognized that processing of imagery will
     inevitably cause some image change. North Carolina is interested in the final
     orthophoto products being visually consistent within reason, rather than specifying
     processes and procedures which vary from vendor to vendor based on their available
     tool sets and practices.

1.   Clipping. The images shall exhibit minimal clipping by exhibiting information and
     detail within both shadow and highlight areas. Contrast adjustments that produce
     artifacts or excessive clipping shall be considered detrimental to the product and
     may be rejected

2.   The Reference Product will be consulted.

3.   Color Balance. All images should have a neutral color balance without the
     dominance of any individual color. Pixel color should closely represent the natural
     color of the ground represented by that pixel at the time of image capture if possible.
     In particular, pavement areas must correctly represent the gray scale of the actual
     pavement in development of overall color balance. There should be no attempt to
     mask the existing color of the ground. The contractor will make every attempt to
     minimize the temporal displacement between flight lines. The Reference Product
     will be consulted.

                                         47

 NC Technical Specifications for Digital Orthophoto Base Mapping
                               2014

4.   Band to Band Registration Accuracy:
     Registration between any color bands shall not exceed 1 pixel.

5.   Image blemishes and artifacts. Imagery shall be free of blemishes, and artifacts that
     obscure ground feature detail. Artifact and blemishes that are introduced during the
     processing of the orthophotography will be reviewed on an individual basis with a
     bias toward rejection. Blemishes and artifacts that are a result of the capture process,
     such as light flashes, ghosting of moving objects, etc will be reviewed by category
     for acceptability.

Radiometric Resolution:
     The native 12-16 bit format will be maintained though the production cycle and it
     may be reduced only at the production of the deliverable product. The deliverable
     product shall include the near infrared spectral band and can be delivered as either
     separate color infrared orthoimagery tiles or as 4 band orthoimagery tiles as directed
     by the Contracting Officer. The Contracting Officer may also elect to not include
     the near infrared spectral band as a deliverable in which case only 3 band color
     orthoimagery would be delivered.

       Color Imagery.
          All color imagery shall be an 8-bit RGB image in accordance with Section 6,
          RGB Full Color Images, of TIFF Revision 6.0 - Adobe Partners
          (https://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf).

       Color Infrared Imagery.
          All color infrared imagery shall be an 8-bit image with bands ordered near
          infrared (NIR), R, G image in accordance with Section 6, RGB Full Color
          Images, of the TIFF Revision 6.0 - Adobe Partners
          (https://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf). Modification
          of the near infrared band in the radiometric adjustment process shall be
          performed at the direction of the Contracting Officer.

                                         48

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     4-Band Imagery.
       All imagery that contains both natural color and the additional near infrared
       band shall meet the same requirements as color imagery specified in the
       paragraph above and shall have the bands ordered as Red, Green, Blue, and
       Near Infrared (RGBN, bands 1,2,3,4). Modification and/or inclusion of the
       near infrared band in the radiometric adjustment process shall be performed at
       the direction of the Contracting Officer.

File Compression:
     The Contractor shall deliver to the Client a complete set of uncompressed digital
     orthophoto images in a format (GeoTIFF or TIFF with world file) on portable
     hard drives supplied by the contractor. In addition to the uncompressed images,
     the Contractor shall also deliver to the Client one sets of compressed orthophoto
     images using an industry accepted compression too , compression ratio, and
     format agreed upon by the Contracting Officer.

Deliverable Product Format:
     The Contractor will only provide digital data to the Client in a format that can be
     used on the Client's GIS system or in an acceptable standard data exchange
     format. If the Contractor's GIS system either uses or can produce digital files in
     the same format that is used by the Client, the information shall be transferred in
     that format. If there is a specific intermediate format that will facilitate the
     transfer of the data between the two computer mapping systems, then the
     intermediate format may be used with the written approval of the Contracting
     Officer. Care will be taken by the Contractor in the construction of the data files
     to assure that data is compatible with and will work on the Client's GIS system.
     Data will not be considered as delivered until the data has been successfully
     loaded and utilized on the Client's system. (This assumes that the Client has an
     operating GIS system at the time of delivery and that problems are wholly data
     related and not hardware or software related.) The Contractor shall transfer the
     digital data to the Client on a media agreed upon between the Contracting Officer
     and the Contractor. Each media item will be accompanied by a label on the box

                                      49

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     and the media, a summary report including the name of the Contractor, study area,
     date, etc. a fact sheet or spreadsheet that specifies the name of each file, the size
     of each file, the map number of each map on the media, and an index shape file
     that confirms the geographic extent.

Deliverable Items by Contractor:
   At the completion of the mapping project as specified in the project contract or at
   times which facilitate the flow of work (delivery dates may be specified in the
   project contract), the Contractor shall deliver to the Contracting Officer for
   acceptance the items in Addendum 1.

Project Report:
   At the completion of the project, the Contractor shall deliver to the Contracting
   Officer two copies of a project report. One copy of the project report shall be
   hardcopy (paper); the second copy of the project report shall be softcopy (as a PDF
   file) and shall accompany and be a part of the digital orthophoto delivery. The project
   report shall contain the following information:
      a) Date of photography by scale.
      b) Altitude of digital sensor and lens focal length.
     c) Date of data set compilation by scale.
        Coordinate system for horizontal and vertical control (including GEOID
        Model) denoting metric or English units (i.e., NAD83(2011) epoch 2010.0
        and GEOID 2012A), assumed, or other coordinate system).
     d) A list of the ground control points used for the project. The minimum data
        shown for each point shall include: physical attributes (i.e. iron rod, railroad
        spike, etc), X and Y Grid coordinates, and elevation, as applicable.
     e) A statement of accuracy of the orthophotos.
     f) A county map of suitable scale and detail depicting the individual orthophotos
        prepared by scale and map number and a count of the total number of
        orthophotos prepared by scale.
     g) Company name, address and phone number.
     h) The name of the Client agency for whom the project was conducted.

                                       50

NC Technical Specifications for Digital Orthophoto Base Mapping
                              2014

     i)   A statement that the orthophotos meet the Land Record Management Program
          Mapping Specifications with Specifications date and, if applicable, a listing of
          exceptions to the Mapping Specifications.
               1. A certificate, substantially in the following form or a form required
                  by the North Carolina Board of Engineers and Land Surveyors,
                  signed, sealed, and dated by the surveyor in control of the project:

                 “I, ______________________, certify that this project was completed
                under my direct and responsible charge from an actual
                photogrammetric survey made under my supervision; that this survey
                was performed to meet Land Records Management Program Standards
                as applicable; that the imagery and/or original data was obtained on
                _______________; that the survey was completed on __________.”.

              2. Identify sensor used and bands collected.

   A project is not considered completed until a Project Report has been submitted to
   and accepted by the Contracting Officer.

                                       51

     NC Technical Specifications for Digital Orthophoto Base Mapping
                                   2014

Attachment 1

    Numbering sequence for Tileing of areas smaller than 10,000 x 10,000

                                   52

        NC Technical Specifications for Digital Orthophoto Base Mapping
                                      2014

Addendum 1

Deliverable Items by Contractor:

 At the completion of the mapping project as specified in the project contract or at a time which
facilitates the flow of work (delivery dates may be specified in the project contract), the
Contractor shall deliver to the Contracting Officer for acceptance the following items:

   Data:
   1. One copy of each digital orthophoto image in GeoTiff format and its associated
      georeferencing world file.
   2. One copy of each softcopy mask on the selected media (Optional)
   3. One copy of the DTM/DEM used in the development of the digital orthophotos in
      uncompressed ASCII format on the selected media.
   4. One optional compressed set of orthophoto files at the specified compression ratios for
      each orthophoto on the specified media
   5. Original raw sensor data (at the Client’s request)
   6. Post Processed Exploitation Images for all contracted bands at pixel depth (bits/band) (at
      the Client’s request)
   7. Seamlines in shapefile format.
   8. Map index in digital form showing the layout/location of the orthophotos.

   Survey and Control:
   1. Contractor will indicate on a copy of the County Contract Map the horizontal control
      stations (existing and to be established) that will be paneled.
   2. The Contractor will provide the Contracting Officer hard copy and digital (ASCII) files
      of survey records:
             a. Field notes and observation
             b. North Carolina Geodetic Survey (NCGS) Station Recovery Forms are to be
                 filled out using online forms and electronically submitted to NCGS
             c. Computations
             d. Control Diagram
             e. Control Data

                                                53

    NC Technical Specifications for Digital Orthophoto Base Mapping
                                  2014

         f. GNSS Observation Summary
3. At the conclusion of Airborne GNSS collection, the Contractor shall be required to
   submit a report of GNSS observations and results data, observation logs, and data
   analysis and adjustments
4. The Contractor will provide the Contracting Officer a brief description of the equipment
   and methods to be used for new ground surveys prior to conducting any control surveys.

Acquisition and Data Reporting:

1. The sensor calibration report shall be submitted to the Contracting Officer for approval
   before proceeding with work.

2. The flight logs, or copies, shall be delivered to the Contracting Officer at the end of the
   project flights.
3. Within one week of each flight mission, the Contractor shall submit a detailed quality
   control report to the Contracting Officer confirming compliance to the aerial photography
   specifications. If the Contractor cannot meet the one-week reporting time frame the
   Contractor shall inform the Contracting Officer in advance of the delay.

4. The Contractor will provide the Contracting Officer the GNSS-IMU Posting Processing
   & Aerial Triangulation Report.

Reporting
1. A summary fact sheet shall contain the following items.
    a) Image Naming Convention Standard Definition
    b) Delivery date
    c) Nominal map scale
    d) Location map of tiled study area with base map
    e) Name of Contractor
    f) Name and license number of professional registered land surveyor/photogrammetrist
         in charge of project
    g) Number of tiles delivered
    h) Coordinate system of map - (NC State Plane)
    i) Horizontal datum
    j) Map unit - (feet)
    k) Feet /meter conversion – (US Survey Foot)

                                            54

    NC Technical Specifications for Digital Orthophoto Base Mapping
                                  2014

    l) Image pixel resolution of final orthoimagery product (GSD)
    m) Bounding coordinates
    n) Digital sensor type
    o) Sensor serial number
    p) Acquisition scale of Imagery
    q) Range of acquisition dates
    r) Map horizontal accuracy
    s) DEM development
    t) Mapping standards used – (NC Land Records Management Mapping Specifications,
        2014)
2. FGDC compliant metadata. See North Carolina endorsed standards and resources on NC
   OneMap http://www.nconemap.com/DiscoverGetData/Metadata.aspx .
3. Flight and Control Plan
4. Imagery Acquisition Compliance Report
5. Two copies of the Project Report
6. Aerotriangulation (AT) Report, including ASCII file
7. Ground Control survey report to include datasheets.
8. Airborne GNSS and IMU post processing data and report.
9. Horizontal Accuracy Assessment
10. Reference Product

                                        55

         NC Technical Specifications for Digital Orthophoto Base Mapping
                                       2014

Addendum 2

NC Orthoimagery Quality Assurance (QA) Procedures

A data delivery inventory is required at the beginning of the QA process. Deliverables are
checked against the Statement of Work (SOW)/State Standard and task order to verify that all
delivery specifications were met. Specific items inventoried include:

1. Formatting and Delivery
  •      Verify shipping manifest against materials received.
  •      Media drive is not corrupted and all orthoimagery files expected in delivery have been
         received.
  •      Media drive does not contain residual or stale data and manufacturer software has been
         removed.
  •      All media can be read by appropriate software, such as ESRI, Microstation,
         GeoExpress, and Intergraph products.
  •      All orthoimages have been correctly named as stated in the contract or partnership
         agreement.
  •      All data is organized by agreed upon folder structure to include orthoimagery files,
         metadata, seamline polygons, DEM adjustment areas, index grid or any other project
         related data.
  •      Verify any use or distribution restrictions with the data and document in the project file.
         •     Notify Contractor of any discrepancies/problems immediately, before the rest of
               the QA process is begun.
2. Image Quality
Every image tile within a project is visually inspected for the following. The Reference Product
will be the project visual quality control reference standard. If quality control issues arise during
final review, this Reference Product will be used as the project standard. Examples of common
visual and geometric discrepancies and guidelines for in and out of scope issues can be found at
http://nconemap.com/Portals/7/documents/EP13_Voice_IssuesHelp.pdf.
  2.1.   Radiometric visual consistency demonstrated at a macro level.
  2.2.   Tonal quality demonstrating visual consistency within reason across the project area
         and between regions.
  2.3.   Tone, contrast, over/under exposure, and over/under saturation.
  2.4.   Leaf off conditions.
  2.5.   Cloud cover, shadows, smoke, haze, snow, and flooding that obstruct ground features.
  2.6.   Seamlines do not visibly impact structures or other manmade items (road, bridges, etc.)
         or are not noticeably visible in non-rural landcover.

                                                 56

         NC Technical Specifications for Digital Orthophoto Base Mapping
                                       2014

  2.7.  Horizontal displacement is less than ±3 pixels along transportation features unless
        project specifications specifically state otherwise.
  2.8. Artifacts, blurs, seamline displacement, pixel stretching.
  2.9. Distortions, misrepresentations, smears, warped or wavy features or structures.
        Smearing that affects cultural features will be corrected by the Contractor.
  2.10. Excessive tilt in bridges, buildings, and other raised features as to not obstruct more
        than 50% of any adjacent roads.
  2.11. Clipped features and non-conforming edgematching at tile boundaries and edges.
  2.12. Elevation issues that cause building or road distortion or warping.

Note: All edges are checked. During this inspection, individual images are checked for
problems. The maximum allowable misalignment between transportation features is ±3 pixels.

3. Reference Data
  •      All orthoimagery files are GeoTIFF 6.0 compliant to not include custom tags.
  •      TIFF world file is delivered that aligns with the TIFF file name and is expressed to
         minimum of two decimal places.
  •      Imagery files are referenced to and use a defined projection for the North Carolina State
         Plane Coordinate System, NAD83 (2011) US Survey Feet, or other agreed upon
         coordinate system.

4. Horizontal Accuracy Assessment.
When test point control is available and “suitable”, a horizontal accuracy check is performed to
verify the veracity of the data producer’s accuracy statement. In the interest of clarity, “suitable”
test point control is defined to be:

  4.1.   Completely independent of data used in the production of the base dataset.
  4.2.   Independent accuracy of test point control should ideally be at least three times more
         accurate than the dataset being tested whenever possible. At an absolute minimum, test
         points must have a horizontal accuracy better than the ground sample distance (or pixel
         size), of the imagery being tested.
  4.3.   Situated on well defined, distinct, and photo-identifiable features.
  4.4.   Situated at or very near ground level, not on an elevated surface.
  4.5.   Preferably obtained by an entity other than the producer of the base data.
  4.6.   Located in relatively level terrain, away from steep embankments.
  4.7.   Not within shadows that might interfere with imagery measurement.

                                                 57

        NC Technical Specifications for Digital Orthophoto Base Mapping
                                      2014

Test points should be dispersed throughout the project area as much as possible. If the dataset to
be tested covers a rectangular area, at least 20% of the points should fall in each quadrant (NW,
NE, SW, SE). The spacing between points should be at least 10% of the diagonal distance across
the rectangular area. The minimum spacing guideline can be waived if more than the minimum
number of independent test points are established. However, the logic behind the spacing
requirement is to ensure that the points are not clustered in a few regions of the project dataset,
and that requirement remains.

Reporting of Horizontal Accuracy shall be as follows:
       1. "This ___________ orthophoto project was checked and found to have a RMSE X
       value of ________Feet and a RMSE Y value of ______feet which conforms to the RMSE
       standard as defined in the North Carolina Technical Specifications for Digital Orthophoto
       Base Mapping

       And

       2. "This __________ orthophoto project was tested using the Case 1 formula and
       procedures set forth in FGDC-STD-007-1998. The result of that test was
       ____________feet horizontal accuracy."

       Horizontal accuracy quality control shall be implemented under the following guide lines.

http://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part1/chapter1

http://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part3/chapter3

5. Metadata Inspection
   •     Verify the existence and content of project-level metadata in an .XML and .TXT format
         metadata file that is FGDC compliant.
   •     Check for proper FGDC metadata structure and mandatory elements:
       o     Check for correct project/urban area name usage.
       o     Check for proper citations, abstract, and purpose.
       o     Check for appropriate dates for time period, production and metadata.
       o     Check for minimum bounding rectangle entry.
       o     Check for Data Credits.
       o     Check for pertinent placekey entries.
       o     Check for production platform/software.

                                                58

         NC Technical Specifications for Digital Orthophoto Base Mapping
                                       2014

        o      Check for a production process description narrative.
        o      Check for an accuracy report narrative and RMS entry.
        o      Check for image, elevation, and control entries in the lineage.
        o      Check for data quality entries (logic and completeness).
        o      Check for accurate geospatial entries (coordinate system, units, horizontal datum).

References
“
 Positional Accuracy Handbook; Using the National Standard for Spatial Data Accuracy to
measure and report geographic data quality;” Minnesota Planning Land Management
Information Center; October 1999. http://www.mnplan.state.mn.us/pdf/1999/lmic/nssda_o.pdf

Checkpoint location cited in ASPRS Accuracy Standards for Large Scale Maps, July 1990

“Guidelines and Specifications for Flood Hazard Mapping Partners; Appendix A: Guidelines for
Aerial Mapping and Surveying; FEMA; April 2003.
http://www.fema.gov/library/viewRecord.do?id=2206

“Geospatial Positioning Accuracy Standards; Part 3: National Standard for Spatial Data
Accuracy”; Federal Geographic Data Committee; 1998
http://www.fgdc.gov/standards/projects/FGDC-standards-projects/accuracy/part3/chapter3

                                                     59

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
