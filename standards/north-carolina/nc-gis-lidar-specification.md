---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-gis-lidar-specification
title: North Carolina Technical Specification for LiDAR Base Mapping
doc_type: standard
citation: 'NC GIS standard: North Carolina Technical Specification for LiDAR Base Mapping'
authority_level: ''
issuing_body: Land Records Management Division, North Carolina Secretary of State (published by NCDIT)
source_url: https://it.nc.gov/documents/files/north-carolina-technical-specification-lidar-base-mapping/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: c1df0254706462405965140baa26a1b2ad20b3be443dd7256f39969bdf858c97
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

# North Carolina Technical Specification for LiDAR Base Mapping (NC GIS standard: North Carolina Technical Specification for LiDAR Base Mapping)

## At a glance

The technical specification for LiDAR base mapping (adopted January 30, 2013) by the Land Records Management Division of the Secretary of State.

## Full text

             North Carolina
     Technical Specifications for
         LiDAR Base Mapping

 Land Records Management Division
    North Carolina Department of
       The Secretary of State

  Elaine F. Marshall, Secretary of State

By Thomas W. Morgan, PLS Land Records Manager

      Adopted 1/30/2013

 North Carolina Technical Specifications for LiDAR Base Mapping

                                                                                   Page 2 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

Acknowledgements: The North Carolina Secretary of State’s Land Records
Management Division would like to thank the following people and their
companies or departments for the valuable help and guidance they gave in the
development of this standard.

Gary W. Thompson                    North Carolina Geodetic Survey
Hope S. Morgan                      North Carolina Geospatial & Technology
                                    Management Office (GTM)
Tonda L. Shelton                    North Carolina Geospatial & Technology
                                    Management Office (GTM)
John Dorman                         North Carolina Geospatial & Technology
                                    Management Office (GTM)
Jeff Brown                          North Carolina Center of Geographic Information
                                    and Analysis (CGIA)
Karl Heidemann                      United Sates Geologic Survey (USGS)
Zsolt Nagy                          AECOM
Keith Johnston                      North Carolina Department of Transportation (NCDOT)
Bill Shinar                         Fugro EarthData, Inc
Brandon Banks                       AECOM
Srinivasan Dharmapuri               Michael Baker Corporation
Silvia Terziotti                    USGS, NC Water Science Center

Revision Notes:
1/22/2013 Added Appendix J and K as reference material.
1/22/2013 Corrected spelling of Bandon to Brandon

                                                                                   Page 3 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

                                   Table of Contents:

1        GENERAL
      1.01   Light Detection and Ranging (LiDAR) Systems Defined
      1.02 General Guidelines for Use
      1.03 Definitions
           1.03.1 General Definitions
               1.03.1.1     Client
               1.03.1.2     The Contracting Officer
               1.03.1.3     The Contractor
               1.03.1.4     Mapping Basic Modular Unit
           1.03.2 LiDAR Definitions
               1.03.2.1     LiDAR
               1.03.2.2     Active Sensors
               1.03.2.3     Discrete
               1.03.2.4     Waveform
               1.03.2.5     Multiple-Return LiDAR
               1.03.2.6     Monochromatic
               1.03.2.7     Intensity Data
               1.03.2.8     Bare Earth
               1.03.2.9     Datum
               1.03.2.10    FIRM (Flood Insurance Rate Map)
               1.03.2.11    GIS (Geographic Information System)
               1.03.2.12    GPS (Global Positioning System)
               1.03.2.13    North Carolina Unit of Measurement
               1.03.2.14    Feet/Meter Conversions
               1.03.2.15    H&H (Hydrologic & Hydraulic)
               1.03.2.16    IMU (Inertial Measurement Unit)
               1.03.2.17    Z-Values
               1.03.2.18    Mass Points
               1.03.2.19    Point Cloud
               1.03.2.20    Vegetation Removal
               1.03.2.21    Artifact Removal
               1.03.2.22    Voids
               1.03.2.23    LiDAR Preliminary Processing
               1.03.2.24    LiDAR Post-Processing
               1.03.2.25    LASer File Format Exchange (LAS)
               1.03.2.26    Control Point
               1.03.2.27    Daily Calibration Survey

                                                                                   Page 4 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

             1.03.2.28      Point Family
         1.03.3 Digital Elevation Data
         1.03.4 Metadata
         1.03.5 Geospatial Accuracy Standard Definitions
             1.03.5.1       Geospatial Accuracy Standard
             1.03.5.2       Accuracy
                  1.03.5.2.1 Absolute Accuracy
                  1.03.5.2.2 Accuracyr
                  1.03.5.2.3 Accuracyz
                  1.03.5.2.4 Vertical Accuracy
                  1.03.5.2.5 Local Accuracy
                  1.03.5.2.6 Network Accuracy
                  1.03.5.2.7 Percentile
                  1.03.5.2.8 Precision
                  1.03.5.2.9 Positional Accuracy
                  1.03.5.2.10 Relative Accuracy
                  1.03.5.2.11 Root Mean Square Error (RMSE)
                  1.03.5.2.12 95% Confidence Level
                  1.03.5.2.13 95th Percentile
             1.03.5.3       Resolution
                  1.03.5.3.1 Nominal Pulse Spacing
                  1.03.5.3.2 Nominal Point Spacing
         1.03.6 Derived Products Definitions
             1.03.6.1       Bare Earth DEM (Digital Elevation Model)
             1.03.6.2       DTM (Digital Terrain Model)
             1.03.6.3       DEM Post Spacing
             1.03.6.4       Digital Surface Model (DSM)
             1.03.6.5       Hillshade
             1.03.6.6       Contours
             1.03.6.7       Breakline
                  1.03.6.7.1 Soft breakline
                  1.03.6.7.2 Hard Breakline
             1.03.6.8       TIN (Triangulated Irregular Network)
    1.04 North Carolina Legislative Requirements
         1.04.1 North Carolina Surveying Law N.C. G.S. 89C
         1.04.2 NC Board of Registration Administrative Code
         1.04.3 Procurement of Architectural, Engineering, and Surveying Services
    1.05 North Carolina File Naming Convention
         1.05.1 Name Format
         1.05.2 Basic Modular Unit with Millionth-Place Digits

                                                                                   Page 5 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

2        CONTRACT MANAGEMENT
      2.01 Sample Request for Qualifications (RFQ),
      2.02 Work Statement
      2.03 Product Ownership and Contractor Product Retention Requirements
      2.04 IT Computer Requirements

3        LiDAR ACQUSITION
      3.01 LiDAR Project Parameters
            3.01.1 Project Boundaries
            3.01.2 Principal Contract Deliverables
            3.01.3 Flightline Overlap
            3.01.4 Buffering
            3.01.5 Project Start/Stop Dates

4     PRE-PROJECT ACTIVITIES
      4.01 Sensor Certification
      4.02 North Carolina In Situ Validation Range Requirements
      4.03 Daily Calibration Survey
      4.04 Flight Line Layout
      4.05 Ground Control Map

5     LiDAR ACQUISITION
      5.01 Collection
           5.01.1 Multiple Discrete Return
           5.01.2 Intensity Values
           5.01.3 Nominal Pulse Spacing
           5.01.4 Data Voids
           5.01.5 Spatial Distribution
           5.01.6 Scan Angle
           5.01.7 Cross Scans
           5.01.8 Vertical Accuracy
           5.01.9 Point Cloud Accuracy
           5.01.10 Land Cover Testing
           5.01.11 Relative Accuracy
           5.01.12 Flightline Overlap
           5.01.13 Collection Area
           5.01.14 Collection Conditions
           5.01.15 Vegetation
      5.02 DATA PROCESSING and HANDLING

                                                                                   Page 6 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

           5.02.1 Performed Within the United States of America
           5.02.2 LAS Format
           5.02.3 Delivery of the Waveform Packets
           5.02.4 GPS Times
           5.02.5 Horizontal Datum
           5.02.6 North Carolina State Plane
           5.02.7 Unit of Measure “U.S. Survey”
           5.02.8 Long Swaths
           5.02.9 Each Swath Assigned a Unique File Source ID
           5.02.10 Point Families
           5.02.11 All Collected Swaths Delivered as Part of the “Raw Data Deliverable”
      5.03 American Society of Photogrammetry and Remote Sensing (ASPRS)/LAS
            Standard Classifications
           5.03.1 Overlap points
           5.03.2 Positional Accuracy Validation
           5.03.3 Classification Accuracy
      5.04 Tiles
           5.04.1 North Carolina Grid Panel Scheme
           5.04.2 Tile Names
           5.04.3 Tile Size
           5.04.4 Tile Units
           5.04.5 Tiled Deliverables
           5.04.6 Tiled Edge-match
           5.04.7 Tile Size for all deliverables

6        Horizontal and Vertical Quality Control
      6.01      Independent Quality Control Checkpoints
           6.01.1 Land Cover Categories
           6.01.2 Checkpoint Selection
           6.01.3 Checkpoint Surveys
           6.01.4 Cluster Survey Points
           6.01.5 Cross Section Surveys
           6.01.6 Documentation
           6.01.7 Orthometric Heights
           6.01.8 3-D Coordinate Files
           6.01.9 Security

      6.02      LiDAR Accuracy Assessment
             6.02.1 LiDAR Acquisition Plans
             6.02.2 LiDAR Acquisition Data
             6.02.3 Bare Earth Data
                                                                                   Page 7 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

             6.02.4 Interpolated z-values
             6.02.5 Checkpoint Elevation Discrepancies
             6.02.6 Fundamental Vertical Accuracy Test
             6.02.7 Supplemental Vertical Accuracy Test
             6.02.8 Consolidated Vertical Accuracy Test
             6.02.9 Vertical Accuracy Assessment and Reporting

      6.03        Error Assessment
             6.03.1 Assessments by Land Cover
             6.03.2 Assessments by Error Locations
             6.03.3 Assessments by Dates/Sensors
             6.03.4 Accuracy Assessment Report
             6.03.5 Airborne GPS Verification
             6.03.6 IMU Verification
             6.03.7 Laser Range Verification
             6.03.8 Total System Verification
             6.03.9 Systematic Error Corrections
             6.03.10 Recalculation of Accuracy Statistics
             6.03.11 LiDAR Accuracy Assessment Report

      6.04      Final Resolution of Problems
             6.04.1 Provisional LiDAR Accuracy Assessment Report
             6.04.2 LiDAR Vendor Checkpoints
             6.04.3 Elevation Contractor Control Points
             6.04.4 Potential Resurveys of Quality Control Contractor Checkpoints
             6.04.5 Potential Reacquisition of LiDAR
             6.04.6 Detailed Ground Surveys

      6.05      Additional Quality Assessments
             6.05.1 Intensity Images
             6.05.2 Assessment of Cross Sections
             6.05.3 Assessment of Edge Matching
             6.05.4 Assessment of Superfluous Elevations

      6.06      Additional Duties of Quality Control Contractor
             6.06.1 Review LAS Point Allocation
             6.06.2 Review Flight Logs

7     HYDRO-FLATTENING REQUIREMENTS
      7.01 Inland Ponds and Lakes
      7.02 Inland Streams and Rivers
      7.03 Non-Tidal Boundary Waters
                                                                                    Page 8 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

      7.04   Tidal Waters
      7.05   Single-Line Streams
      7.06   Docks or Piers
      7.07   Island Features

8     TERRAIN MODELING SUPPLEMENTS
      8.01 Road Features
      8.02 Soft Features
      8.03 Low Confidence Areas
      8.04 Overpasses and Bridges
      8.05 Depressions
      8.06 Water Bodies

9     DELIVERABLES
      9.01 Surveyors Certification
      9.02 Collection Report
      9.03 Survey Report
      9.04 Processing Report
      9.05 Quality Assurance /Quality Control (QA/QC) Reports
      9.06 Control and Calibration points
      9.07 Daily Calibration Report
      9.08 Flight Plan Map
      9.09 Geo-referenced Extent of each Delivered Dataset
      9.10 Metadata
      9.11 Raw Point Cloud
      9.12 Classified Point Cloud
      9.13 Bare Earth Surface (Raster DEM)
      9.14 Breaklines

10      COMMON DATA UPGRADES
      10.01 Independent 3rd-Party QA/QC
      10.02 Higher Nominal Pulse Spacing
      10.03 Increased Vertical Accuracy
      10.04 Full Waveform Collection and Delivery
      10.05 Additional Environmental Constraints
      10.06 Top-of Canopy
      10.07 Intensity Images
      10.08 Detailed Classification
      10.09 Hydro-Enforced DEMs
      10.10 Breaklines (hydrographic features)

                                                                                   Page 9 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

     10.11 Breaklines (other features)
     10.12 Extracted Buildings
     10.13 Other Products

11   DERIVED PRODUCTS
   11.01 Digital Terrain Models
   11.02 Triangulated Irregular Network (TIN)
   11.03 Hillshade Model
   11.04 Contours
        11.04.1 Contour domain
            11.04.1.1     Intermediate contours
            11.04.1.2     Supplementary Contours
            11.04.1.3     Depression Contours
            11.04.1.4     Fill Contours
            11.04.1.5     Index Contours
12   PRODUCT LIMITATIONS
   12.01 Points Designated as Bare Earth
   12.02 DEM, DTM, and TIN
   12.03 Contours
   12.04 Water and Asphalt Areas
13   APPENDICES
     Appendix A: Request for Qualifications (RFQ), (Example)
     Appendix B: Hydro-Flattening Reference
     Appendix C: Naming Convention for Geospatial Data
     Appendix D: Issue Papers
     Appendix E: Quality Control of Light Detection and Ranging (LiDAR)
            Elevation Data in North Carolina (Background)
     Appendix F: Example of a LiDAR Metadata Record
     Appendix G: Daily Calibration Survey / Boresight Calibration
     Appendix H: ASPRS Guidelines, Vertical Accuracy Reporting for LiDAR Data,
     Appendix I: Affirmation of Vertical Datum for Surveying and Mapping Activities
     Appendix J: USGS Lidar Base Specifications Version1.0 book 11 collection and
            Delineation of Spatial Data
     Appendix K: USGS National Enhanced Elevation Assessment

                                                                                   Page 10 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

   1. GENERAL
    1.01 Light Detection and Ranging (LiDAR) Systems

                For the purposes of this Standard, LiDAR (Light Detection And Ranging) is
                defined as an airborne laser system, flown aboard rotary or fixed-wing aircraft,
                that is used to acquire x, y, and z coordinates of terrain and terrain features that
                are both manmade and naturally occurring. LiDAR systems consist of an
                airborne Global Positioning System (GPS) with attendant GPS base station(s),
                Inertial Measuring Unit (IMU), and light-emitting scanning laser.

                The system measures ranges from the scanning laser to terrain surfaces within a
                scan width beneath the aircraft. The time it takes for the emitted light (LiDAR
                return) to reach the earth's surface and reflect back to the onboard LiDAR
                detector is measured to determine the range to ground. Scan widths will vary,
                depending on mission purpose, weather conditions, desired point density and
                spacing, and other factors. The airborne GPS component ascertains the in-flight
                three-dimensional position of the sensor, and the IMU component delivers
                precise information about the attitude of the sensor: role, pitch, and yaw. This
                information provides the origin point of the pulse. The sensor collects the
                direction and slope of the pulse. It also collects the range of each return. Post
                processing of this data will generate coordinates for all returns.

                See: http://www.ncfloodmaps.com/pubdocs/LiDAR_final_jan03.pdf

    1.02    General Guidelines for Use

                Important factors to consider in the LiDAR-system mission planning are the
                desired pulse density required to produce the randomly spaced LiDAR points
                and the point spacing of the uniformly spaced digital elevation model (DEM)
                points derived from the randomly spaced LiDAR returns. The correct point
                density necessary to accurately represent terrain and terrain features will
                depend on vegetation, structures, flight conditions, mission purpose, and
                required accuracy. Even with adequate LiDAR points, if the chosen DEM
                spacing is too large the micro-terrain will not be reflected in the DEM.

                                                                                        Page 11 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                 Flight-path planning is another important factor in the LiDAR system mission.
                 The flight path shall cover the study area satisfactorily including both parallel
                 and cross flight lines to eliminate shadowing and allow for proper quality
                 control. Unlike aerial photogrammetry, LiDAR missions can be flown without
                 regard to sun angle. Flights may take place at night, if conditions otherwise
                 allow.

                 Elevation and measurement information related to subsurface channel and
                 hydraulic structure geometry must be obtained through the use of other
                 mapping technologies. In some instances, shallow, clear water and near-shore
                 coastal surveys can be accomplished using LiDAR systems equipped with
                 lasers operating in portions of the light spectrum that allow transmission
                 through water.

                 LiDAR system tolerance for inclement weather conditions (e.g., high winds,
                 wet snow, rain, fog, high humidity, low cloud cover) generally is higher than
                 that of other photogrammetric methods. However, such conditions have been
                 known to degrade the accuracy of laser return data. Therefore, the contractor
                 shall generally avoid missions during inclement weather.

                 In dense foliage, more pulses equate to a greater probability that the return data
                 set will include adequate bare earth coordinates to produce an accurate terrain
                 model. A single pulse may generate multiple returns, depending on how many
                 objects it strikes before it is completely blocked. There is no guarantee that the
                 pulse will reach bare earth. Care must be taken in planning missions with
                 regard to both natural (vegetative) and manmade (structure) ground cover.
                 Pulse width, beam divergence, first and last pulse return discrimination, and
                 choice of the post-processing algorithms may all affect the accuracy of LiDAR-
                 derived data in areas of dense foliage.

    1.03     Definitions:
           1.03.1 General Definitions

               1.03.1.1 Client is the financially responsible entity entering into a mapping
                         contract with a Contractor under the provisions of these specifications.
                         A Client may be a county government, municipal government, any
                         local, state agency or private entity.

               1.03.1.2 The Contracting Officer is the officially designated representative of
                         the financially responsible entity (Client) obtaining the mapping

                                                                                       Page 12 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                        products or other services. This individual's authority and
                        responsibilities shall be as prescribed by the Client.

              1.03.1.3 The Contractor is that firm, company, or organization to which the
                        mapping or service contract has been let. References to the Contractor
                        in these specifications shall also apply in full to any subcontractor
                        working for the named Contractor.

              1.03.1.4 Mapping Basic Modular Unit: The 1" = 400' map is the smallest scale
                        map included in these specifications and is designated the "Basic
                        Modular Unit" in a series of maps which provide for four map scales,
                        as follows:

                             •   1" = 400'. The boundaries of each Basic Modular Unit shall be
                                 the grid ticks of the North Carolina State Plane Coordinate
                                 System evenly divisible by 10,000 ft. in north-south and east-
                                 west directions.
                             •   1" = 200'. Each map will be one-quarter (1/4) of a Basic
                                 Modular Unit. The neat image area shall be bounded by the
                                 North Carolina grid ticks whose eastings and northings are
                                 evenly divisible by 5,000 feet.
                             •   1" = 100'. Each map shall be one-sixteenth (1/16) of a Basic
                                 Modular Unit. The neat image area of this unit shall be
                                 bounded by the North Carolina grid ticks with eastings and
                                 northings evenly divisible by 2,500 feet.
                             •   1" = 50'. Each map shall be one sixty-fourth (1/64) of a Basic
                                 Modular Unit. The neat image area of this unit shall be
                                 bounded by the North Carolina grid ticks with eastings and
                                 northings evenly divisible by 1,250 feet.

         1.03.2 LiDAR Definitions:
              1.03.2.1 LiDAR is an acronym for Light Detection and Ranging. LiDAR is
                        synonymous with airborne laser mapping and laser altimetry. A LiDAR
                        sensor is an instrument that measures distance to a reflecting object by
                        emitting timed pulses of laser light and measuring the time between

                                                                                      Page 13 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                         emission and reception of reflected pulses. The measured time interval
                         is converted to distance.
              1.03.2.2 Active Sensors send a pulse of energy and await the return of that
                         energy. Passive sensors, by contrast, record reflected or emitted energy
                         (e.g. thermal sensors) where the sun is the typical source of the energy.
              1.03.2.3 Discrete: A laser pulse is a beam of light comprising a continuous
                         waveform. When LiDAR systems for mapping were first developed
                         for commercial purposes, the LiDAR sensors were not electronically
                         capable of recording the entire waveform in the return signal. A filter
                         was applied to detect peaks in the reflected waveform and to record the
                         timing of those peaks as discrete “returns”. For example, a peak is
                         generated from a reflection caused by the top of the tree, but a
                         sufficient amount of laser light energy is able to continue on to
                         generate returns from lower ports of the tree, and finally, from the
                         ground. You might think of discrete LiDAR as a digitization of
                         waveform LiDAR. In that sense, when the return waveform is above a
                         certain threshold, the LiDAR system records a discrete pulse - up to
                         five discrete pulses per return.
              1.03.2.4 Waveform: The entire waveform from the laser pulse is recorded (as
                         opposed to discrete returns). This technique currently has lower spatial
                         resolution than discrete LiDAR but captures more detailed information
                         on vertical structure and can more accurately detect the true ground
                         topography under the dense vegetation canopy. Waveform LiDAR is
                         not subject to signal processing errors.
              1.03.2.5 Multiple-Return LiDAR: Still further classifications exist within
                         discrete LiDAR: LiDAR can be collected as single return or multiple-
                         return. Single-return LiDAR is cheaper but can only be used to derive a
                         bare earth and a canopy height model. Multiple-return LiDAR is
                         required to assess 3-D forest structure characteristics.
              1.03.2.6 Monochromatic means it has one wavelength of light - usually in the
                         near-infrared range for terrestrial applications.
              1.03.2.7 Intensity Data: A LiDAR return is made up of the x, y, and z position of
                         the point. The sensor also records the intensity of the reflected signal;
                         that data can be viewed as an image similar to a panchromatic
                         orthophoto. Because the Lidar pulse is in the near infrared (NIR)
                         spectrum the image will have similarities to NIR. The intensity of the
                         reflection can be affected by a combination of factors such as flying
                         height, laser power and wavelength, atmosphere, direction of the laser
                         beam and the number of returns.

                                                                                      Page 14 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              1.03.2.8 Bare Earth is the digital elevation data of the terrain, free from
                        vegetation, buildings, and other man-made structures. Elevations of the
                        ground are derived from post-processing of LiDAR data. Automated
                        and manual post-processing routines are used to eliminate points that
                        impinge on elevation features.
              1.03.2.9 Datum: For digital elevation data produced under the Standard, the
                        horizontal datum (i.e., coordinate system in which control points are
                        located) is the North Carolina State Plane Coordinates system, as
                        defined in the North Carolina Official Survey Base (N.C. G.S. 102)
                        including the latest published adjustment, and the vertical datum (i.e.,
                        set of constants defining a height system) is the North American
                        Vertical Datum of 1988 (NAVD 88) (see Appendix I). The most
                        current Geoid model published by National Geodetic Survey shall be
                        used. All data will be based on US Survey Foot unless the contractor
                        has obtained a written waver from the contracting official; said waver
                        shall be prominently noted in all deliverables. Elevation will be stated
                        as orthometric height.
              1.03.2.10 FIRM (Flood Insurance Rate Map) is an official map of a
                        community on which Federal Emergence Management Agency
                        (FEMA) has delineated the flood hazard areas and the risk premium
                        zones.
              1.03.2.11 GIS (Geographic Information System): A system of spatially
                        referenced information, including computer programs that store,
                        manipulate, analyze, and display spatial data.
              1.03.2.12 GPS (Global Positioning System): Technology that computes the
                        three-dimensional position in space, for example the LiDAR sensor,
                        using satellites.
              1.03.2.13 North Carolina Unit of Measurement: U.S. Survey Foot
              1.03.2.14 Feet/Meter Conversions: The U. S. Survey Foot (l meter =
                        3.2808333333 feet) shall be used in all conversions of North Carolina
                        State Plane Coordinates from meters to feet or feet to meters. All final
                        control data shall be in U.S. Survey feet and the datum used (See
                        Section 1.03.2.9 Datum) will be noted on any sheets bearing
                        coordinates.
              1.03.2.15 H&H (Hydrologic & Hydraulic) is the modeling of rainfall runoff
                        (hydrology), providing peak discharges, and the resulting flow within a
                        channel (hydraulics), which provides a profile of water surface
                        elevations. Digital elevation data are used for H&H analyses.

                                                                                     Page 15 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              1.03.2.16 IMU (Inertial Measurement Unit): Instrumentation that computes the
                        roll, pitch, and heading of a moving object, for example a LiDAR
                        sensor mounted in an aircraft.
              1.03.2.17 Z-Values: The elevations of the 3-D surface above the vertical datum
                        at designated X-Y locations.
              1.03.2.18 Mass Points is a sub set of the point cloud. Irregularly spaced points,
                        each with X-Y location coordinates and Z-value, typically segregated
                        by some criteria for example first return or bare earth. Mass point
                        spacing and pattern may depend upon the characteristics of the
                        technologies used to acquire and post process the data.
              1.03.2.19 Point Cloud: Often referred to as the “raw point cloud”, this is the first
                        data product of a LiDAR instrument. In its crudest form, a LiDAR raw
                        point cloud is a collection of range measurements and sensor
                        orientation parameters. After initial processing, the range and
                        orientation of each laser value is converted to a position in a three
                        dimensional frame of reference and this spatially coherent cloud of
                        points is the base for further processing and analysis. The raw point
                        cloud typically includes first, last, and intermediate returns for each
                        laser pulse. In addition to spatial information, LiDAR intensity returns
                        provide texture or color information. The combination of three
                        dimensional spatial information and spectral information contained in
                        the LiDAR dataset allows great flexibility for data manipulation and
                        extraction. In its refined form all points will have a LAS classification
                        even those deemed noise. (see Section 1.03.2.25)
              1.03.2.20 Vegetation Removal: Correction of surface elevations so as to depict
                        the elevation of the bare earth terrain without interference due to above
                        ground objects.
              1.03.2.21 Artifact Removal: Correction of surface elevations so as to depict the
                        elevation of the bare earth terrain beneath manmade structures.
              1.03.2.22 Voids: Portions of a digital elevation dataset where no elevation data
                        are available.
              1.03.2.23 LiDAR Preliminary Processing: The initial processing and analysis
                        of laser data to fully “calibrated point clouds” in some specified tile
                        format. All LiDAR data should be set to the American Society for
                        Photogrammetry and Remote Sensing (ASPRS) LAS Class 1
                        (unclassified) and it is recommended that testing for Fundamental
                        Vertical Accuracy (FVA) be performed during preliminary processing.
                        The tile format can change later, if necessary.
              1.03.2.24 LiDAR Post-Processing: The final processing and classification of
                        LiDAR data to the recommended ASPRS LAS classes, per project

                                                                                      Page 16 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                        specifications. It is recommended that testing for Consolidated Vertical
                        Accuracy (CVA) and Supplemental Vertical Accuracy (SVA) be
                        performed after LiDAR post-processing is complete. At this point, the
                        datasets are referred to as the “classified point cloud.”
              1.03.2.25 LASer File Format Exchange (LAS): The ASPRS LAS file format is
                        a public file format for the interchange of 3-dimensional point cloud
                        data between data users. Although developed primarily for exchange of
                        LiDAR point cloud data, this format supports the exchange of any 3-
                        dimensional X-Y-Z triplet. This binary file format is an alternative to
                        proprietary systems or a generic American Standard Code for
                        Information Interchange (ASCII) file interchange system used by many
                        companies.
                        Http://www.asprs.org/society/committees/standards/LAS_1_4_r11.pdf
              1.03.2.26 Control Point is any horizontal or vertical ground point established by
                        the contractor for the purpose of validation, project control, and /or
                        quality control.
              1.03.2.27 Daily Calibration Survey is a survey designed to validate the LiDAR
                        data collected daily by each sensor used that day to collected data at the
                        start and end on each mission by flying the pre-established range. The
                        flight pattern is flown over the test area in two opposing directions and
                        a cross-flight at 90 degrees to the former.
              1.03.2.28 Point Family consists of multiple returns resulting in a group of points
                        (children) from a single pulse (parent).

         1.03.3 Digital Elevation Data: Includes all of the following terms: mass points, point
                clouds, breaklines, contours, TINs, DEMs, DTMs or DSMs.
         1.03.4 Metadata: A data file that describes other data. It provides information about a
                certain item's content. For example, an image may include metadata that
                describes how large the picture is, the color depth, the image resolution, when
                the image was created, and other data. A text document's metadata may contain
                information about how long the document is, who the author is, when the
                document was written, and a short summary of the document. Federal
                Geographic Data Committee (FGDC) Compliant Metadata is metadata that
                follows an FGDC approved standard that provides a common set of
                terminology, definitions, and information about values to be provided in a
                formally-structured documentation of digital data products.

                                                                                      Page 17 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

         1.03.5 Geospatial Accuracy Standard Definitions

              1.03.5.1 Geospatial Accuracy Standard – A common accuracy testing and
                        reporting methodology that facilitates sharing and interoperability of
                        geospatial data. Published in 1998, the National Standard for Spatial
                        Data Accuracy (NSSDA) is the Federal Geographic Data Committee
                        (FGDC) standard relevant to digital elevation data when assuming that
                        errors follow a normal error distribution. However, after it was learned
                        that LiDAR datasets do not necessarily follow a normal distribution in
                        vegetated terrain, the National Digital Elevation Program (NDEP)
                        published its “Guidelines for Digital Elevation Data” and the American
                        Society for Photogrammetry and Remote Sensing (ASPRS) published
                        the “ASPRS Guidelines: Vertical Accuracy Reporting for LiDAR
                        Data,” both of which were published in 2004 and use newer terms
                        defined below as Fundamental Vertical Accuracy (FVA), Supplemental
                        Vertical Accuracy (SVA) and Consolidated Vertical Accuracy (CVA).
                        All of these standards, designed for digital elevation data, replace the
                        National Map Accuracy Standard (NMAS) that is applicable only to
                        graphic maps defined by map scale and contour interval. See Appendix
                        H.
              1.03.5.2 Accuracy – The closeness of an estimated value (e.g., measured or
                        computed) to a standard or accepted (true) value of a particular
                        quantity. Note: With the exception of GPS Continuously Operating
                        Reference Stations (CORS), assumed to be known with zero errors
                        relative to established datums, the true locations of 3-D spatial
                        coordinates or other points are not known, but only estimated.
                        Therefore, the accuracy of other coordinate information is unknown
                        and can only be estimated. Other accuracy definitions are as follows.
                   1.03.5.2.1 Absolute Accuracy – A measure that accounts for all systematic
                              and random errors in a data set. Absolute accuracy is stated with
                              respect to a defined datum or reference system.
                   1.03.5.2.2 Accuracyr is the NSSDA reporting standard in the horizontal
                              component that equals the radius of a circle of uncertainty, such
                              that the true or theoretical horizontal location of the point falls
                              within that circle 95-% of the time. Accuracyr = 1.7308 x Root
                              Mean Square Errorr (RMSEr). Horizontal accuracy is defined as
                              the positional accuracy of a dataset with respect to a horizontal
                              datum.
                   1.03.5.2.3 Accuracyz is the NSSDA reporting standard in the vertical
                              component that equals the linear uncertainty value, such that the
                                                                                     Page 18 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                              true or theoretical vertical location of the point falls within that
                              linear uncertainty value 95-% of the time. Accuracyz = 1.9600 x
                              RMSEz. Vertical accuracy is defined as the positional accuracy of
                              a dataset with respect to a vertical datum.
                   1.03.5.2.4 Vertical Accuracy
                              Consolidated Vertical Accuracy (CVA) is the result of a test of
                              the accuracy of vertical checkpoints (z-values) consolidated for
                              two or more of the major land cover categories, representing both
                              open terrain and other land cover categories. Computed by using
                              the 95th percentile, CVA is always accompanied by Fundamental
                              Vertical Accuracy (FVA).
                              Fundamental Vertical Accuracy (FVA) is the value by which
                              vertical accuracy can be equitably assessed and compared among
                              datasets. The FVA is determined with vertical checkpoints
                              located only in open terrain, where there is a very high probability
                              that the sensor will have detected the ground surface. FVA is
                              calculated at the 95% confidence level in open terrain only, using
                              RMSEz x 1.9600,
                              Supplemental Vertical Accuracy (SVA) is the result of a test of
                              the accuracy of z-values over areas with ground cover categories
                              or combination of categories other than open terrain. Computed
                              by using the 95th percentile, SVA is always accompanied by
                              FVA. SVA values are computed individually for different land
                              cover categories. Each land cover type representing 10% or more
                              of the total project area is typically tested and reported as an
                              SVA. SVA specifications are normally target values that may be
                              exceeded so long as overall CVA requirements are satisfied.

                   1.03.5.2.5 Local Accuracy – A value that represents the uncertainty in the
                              coordinates of a control point relative to the coordinates of other
                              directly-connected, adjacent control points at the 95% confidence
                              level. The reported local accuracy is an approximate average of
                              the individual local accuracy values between this control point
                              and other observed control points used to establish the
                              coordinates of the control point.
                   1.03.5.2.6 Network Accuracy – A value that represents the uncertainty in
                              the coordinates of a control point with respect to the geodetic
                              datum at the 95% confidence level. For National Spatial
                              Reference System (NSRS) network accuracy classification in the
                              U.S., the datum is considered to be best expressed by the geodetic

                                                                                      Page 19 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                              values at the CORS supported by the National Geodetic Survey
                              (NGS). By this definition, the local and network accuracy values
                              at CORS sites are considered to be infinitesimal, i.e., to approach
                              zero.
                   1.03.5.2.7 Percentile – Any of the values in a dataset of errors dividing the
                              distribution of the individual errors in the dataset into one
                              hundred groups of equal frequency. Any of those groups can
                              specify a specific percentile, e.g., the 95th percentile as defined
                              below.
                   1.03.5.2.8 Precision – A statistical measure of the tendency of a set of
                              random numbers to cluster about a number determined by the
                              dataset. Precision relates to the quality of the method by which
                              the measurements were made and is distinguished from accuracy
                              which relates to the quality of the result. The term “precision” not
                              only applies to the fidelity with which required operations are
                              performed, but, by custom, has been applied to methods and
                              instruments employed in obtaining results of a high order of
                              precision. Precision is exemplified by the number of decimal
                              places to which a computation is carried and a result stated.
                   1.03.5.2.9 Positional Accuracy – The accuracy of the position of features,
                              including horizontal and/or vertical positions.
                   1.03.5.2.10 Relative Accuracy – A measure that accounts for random errors
                              in a dataset. Relative accuracy may also be referred to as point-to-
                              point accuracy. The general measure of relative accuracy is an
                              evaluation of the random errors (systematic errors and blunders
                              removed) in determining the positional orientation (e.g., distance,
                              azimuth) of one point or feature with respect to another.
                   1.03.5.2.11 Root Mean Square Error (RMSE) – The square root of the
                              average of the sum of squared differences between dataset
                              coordinate values and coordinate values from an independent
                              source of higher accuracy for identical points. The vertical RMSE
                              (RMSEz), for example, is calculated as the square root of S(Zn –
                              Z’n)2/N, where: Zn is the set of N z-values (elevations) being
                              evaluated, normally interpolated (for TINs and DEMs) from
                              dataset elevations of points surrounding the X-Y coordinates of
                              checkpoints; and Z’n is the corresponding set of checkpoint
                              elevations for the points being evaluated; -N is the number of
                              checkpoints; and n is the identification number of each of the
                              checkpoints from 1 through N.

                                                                                      Page 20 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                   1.03.5.2.12 95% Confidence Level – Accuracy reported at the 95%
                              confidence level means that 95% of the positions or elevations in
                              the dataset will have an error with respect to true ground position
                              or true elevation that is equal to or smaller than the reported
                              accuracy value. The reported accuracy value reflects all
                              uncertainties, including those introduced by geodetic control
                              coordinates; GPS-IMU system error, sensor error, processing
                              algorithm error, interpolation error, and final computation of
                              ground coordinate values in the product. Where errors follow a
                              normal error distribution, Accuracyz defines vertical accuracy at
                              the 95% confidence level (computed as RMSEz x 1.9600), and
                              Accuracyr defines horizontal (radial) accuracy at the 95%
                              confidence level (computed as RMSEr x 1.7308).
                   1.03.5.2.13 95th Percentile – Accuracy reported at the 95th percentile
                              indicates that 95% of the errors will be of equal or lesser value
                              and 5% of the errors will be of larger value. This term is used
                              when errors may not follow a normal error distribution, e.g., in
                              forested areas where the classification of bare-earth elevations
                              may have a positive bias. Vertical accuracy at the 95%
                              confidence level and 95th percentile may be compared to evaluate
                              the degree to which actual errors approach a normal error
                              distribution. See “Issue 37: Quality Control of Light Detection
                              and ranging (LiDAR) Elevation Data in North Carolina for Phase
                              II of the NCFMP” .
                              http://www.ncfloodmaps.com/pubdocs/issue_papers/IP37-
                              phaseII_lidar_qc.pdf
              1.03.5.3 Resolution – In the context of elevation data, resolution is synonymous
                        with the horizontal density of elevation data points for which two
                        similar terms are used; Nominal Pulse Spacing and Nominal Point
                        Spacing.
                   1.03.5.3.1 Nominal Pulse Spacing (NPS) is the estimated average spacing
                              of irregularly-spaced LiDAR points in both the along-track and
                              cross-track directions resulting from: the laser pulse repetition
                              frequency (e.g., 100,000 pulses of laser energy emitted in one
                              second from a 100 kHz sensor); scan rate (sometimes viewed as
                              the number of zigzags per second for this common scanning
                              pattern); field-of-view; flight airspeed, and flight altitude above
                              the terrain. LiDAR system developers currently provide “design
                              NPS” as part of the design pulse density, although the American
                              Society for Photogrammetry and Remote Sensing (ASPRS) is

                                                                                     Page 21 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                              currently developing standard procedures to compute the
                              “empirical NPS” which should be approximately the same as the
                              “design NPS” when accepting statistically insignificant loss of
                              returns and disregarding void areas, from water for example. The
                              NPS assessment is made against single swath first return data
                              located within the geometrically usable center portion (typically
                              ~90%) of each swath. Average along-track and cross-track pulse
                              spacing should be comparable. When point density is increased
                              by relying on overlap or double-coverage it should be
                              documented in metadata, and the project’s reported NPS should
                              not change. The NPS should be equal to or less than the desired
                              Digital Elevation Model grid. NPS is not to be substituted for
                              Nominal Point Spacing.
                   1.03.5.3.2 Nominal Point Spacing is not an appropriate term in LiDAR
                              because a single Pulse can produce multiple points. NPS as used
                              in this standard pertains to LiDAR only and is not intended to
                              pertain to photogrammetry or Interferometric Synthetic Aperture
                              Radar (IFSAR).

         1.03.6 Derived Products Definitions
              1.03.6.1 Bare Earth DEM (Digital Elevation Model): A popular acronym used
                        as a generic term for digital topographic and/or bathymetric data in all
                        its various forms, but most often bare earth elevations at regularly
                        spaced intervals in X and Y directions. Regularly spaced elevation data
                        are easily and efficiently processed in a variety of computer uses. A
                        DEM contains elevations at points arranged in a raster data structure, a
                        regularly spaced X, Y grid, where the intervals of ΔX and ΔY are
                        normally in linear units (feet or meters) or geographic units (degrees or
                        fractions of degrees of latitude or longitude). The Z-values in a DEM
                        represent the height of the terrain, relative to a specific vertical datum
                        and void of vegetation or manmade structures such as buildings,
                        bridges, walls, et cetera. The elevation of lakes and rivers in a DEM
                        implies the height of the water surface based on elevation of the
                        exposed shoreline. The observations, or direct measurements, of
                        elevation that comprise the DEM are almost never actually captured on
                        a regular grid; therefore, the elevation for any given point in the grid is
                        normally interpolated from other forms of source data. LiDAR, for
                        example, yields a dense set of irregularly spaced points; interpolation to
                        a grid requires using one of many possible interpolation algorithms,
                        which produce varying results. Linear features, such as streams,

                                                                                       Page 22 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                        drainage ditches, ridges, and roads are often lost in a DEM if the grid
                        spacing is larger than the dimensions of the feature. Furthermore, in a
                        DEM, it is unlikely that the hard edge of the feature will be represented
                        correctly in the terrain model. The DEM, because it is a raster data
                        structure similar to a digital image, is an efficient format for storage,
                        analysis, rendering, and visualization.
                   1.03.6.1.1 DEM post spacing is defined as the constant sampling interval
                              in X- and Y-directions of a DEM lattice or grid. This is also
                              called the horizontal resolution of a gridded DEM or the DEM
                              grid spacing. If a DEM is required as part of project
                              specifications the contract must include the desired grid spacing.
                              It is standard industry practice to have:
                        •            1-meter DEM post spacing for elevation data with 1-foot
                                     equivalent contour accuracy;
                        •            2-meter DEM post spacing for elevation data with 2-foot
                                     equivalent contour accuracy; and
                        •            5-meter DEM post spacing for elevation data with 5-foot
                                     equivalent contour accuracy.

              1.03.6.2 Digital Terrain Model (DTM) data structure is also made up of X and
                        Y points with Z-values representing elevations, but unlike the DEM,
                        these may be irregularly or randomly spaced mass points. Direct
                        observations of elevation at a particular location can be incorporated
                        without interpolation, and the density of points can be adjusted so as
                        best to characterize the actual terrain. Fewer points can describe very
                        flat or evenly sloping ground; more points can be captured to describe
                        very complicated terrain. In addition to mass points, the DTM data
                        structure often incorporates breaklines (further defined below) to retain
                        abrupt linear features in the model. A DTM is often more expensive
                        and time consuming to collect than a DEM, but is considered
                        technically superior for most engineering analyses because it retains
                        natural features of the terrain.
              1.03.6.3 Digital Surface Model (DSM) is an elevation model created for use in
                        computer software that is similar to DEMs or DTMs except that DSMs
                        depict the elevations of the top surfaces of buildings, trees, towers, and
                        other features elevated above the bare earth.
              1.03.6.4 Hillshade is a function used to create an illuminated representation of a
                        surface, using a hypothetical light source that simulates the cast shadow
                        thrown upon a raised relief map. This process is helpful in identifying
                        linear features such as streams and ridgelines.
                                                                                      Page 23 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              1.03.6.5 Contours are lines of equal elevation on a surface. An imaginary line on
                        the ground, all points of which are at the same elevation above or
                        below a specified reference surface (datum).
              1.03.6.6 Breakline is a linear feature demarking a change in the smoothness or
                        continuity of a surface such as abrupt elevation changes or a stream
                        line. The two most common forms of breaklines are as follows:
                   1.03.6.6.1 Soft breakline ensures that known elevations, or Z-values, along
                               a linear feature are maintained (e.g., elevations along a pipeline,
                               road centerline, or drainage ditch), and ensures the boundary of
                               natural and man-made features on the Earth’s surface are
                               appropriately represented in the digital terrain data by use of
                               linear features and polygon edges. They are generally
                               synonymous with 3-D breaklines because they are depicted with
                               series of Z-Y-Z coordinates.
                   1.03.6.6.2 Hard breakline defines interruptions in surface smoothness, e.g.,
                               to define streams, shorelines, dams, ridges, building footprints,
                               and other locations with abrupt surface changes. Although some
                               hard breaklines are 3-D breaklines, they are often depicted as 2-D
                               breaklines because features such as shorelines and building
                               footprints are normally depicted with a series of horizontal
                               coordinates only, that are often digitized from digital
                               orthophotography that include no elevation data.
              1.03.6.7 Triangulated Irregular Network (TIN) is a set of adjacent, non-
                        overlapping triangles computed from the mass points and breaklines in
                        a DTM. TINs also preserve abrupt linear features and are excellent for
                        calculations of slope, aspect, and surface area and for automated
                        generation of topographic contours, which are all important functions
                        to the flood study engineering. Storage formats for TINs are more
                        complex than either DEMs or DTMs, because the relationship of
                        elevation points and triangular surfaces must be preserved within the
                        data structure. A TIN model may be preferable to a DEM when it is
                        critical to preserve the location of narrow or small surface features such
                        as a stream channel or ridge line.

    1.04    North Carolina Legislative Requirements - All Data must be collected and
            processed under the supervision of a Professional Land Surveyor licensed in North
            Carolina and in accordance with:
                 Note: Laws and administrative code affecting this standard may be changed
                without notice. For the current Statute or Code wording consult the official
                legislative or licensing board website.

                                                                                      Page 24 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

           1.04.1 North Carolina Surveying Law N.C. G.S. 89C
           http://www.ncleg.net/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_89
           C.html

           1.04.2 NC Board of Registration Administrative Code
                  http://reports.oah.state.nc.us/ncac.asp?folderName=\Title%2021%20-
                  %20Occupational%20Licensing%20Boards%20and%20Commissions\Ch
                  apter%2056%20-%20Engineers%20and%20Surveyors

               See 21 NCAC 56 .1606 SPECIFICATIONS FOR TOPOGRAPHIC
               AND PLANIMETRIC MAPPING, INCLUDING GROUND, AIRBORNE,
               AND SPACEBORNE SURVEYS

                See 21 NCAC 56 .1607           GLOBAL POSITIONING SYSTEMS
               SURVEYS

           1.04.3     Procurement of Architectural, Engineering and Surveying Services NC
                    GS 143-64.31 (Mini-Brooks Act)
                    http://www.ncleg.net/EnactedLegislation/Statutes/HTML/BySection/Chapt
                    er_143/GS_143-64.31.html

    1.05     North Carolina File Naming Convention - The “Naming Convention for
             Geospatial Data presented in the North Carolina Grid Panel Scheme” is an
             outgrowth of the naming specification found in the North Carolina Technical
             Specifications for Digital Orthophoto base mapping, August 20, 2009. For lack of a
             better term consider the use of this naming scheme as “extra-lite” metadata. This
             convention using the base modular unit from the above standard is consistent with
             county mapping standards for the last 20 years and compatible with the Parcel
             Identifier Number (PIN) used for most county tax mapping in North Carolina. This
             convention is for all types of geospatial data (raster, vector, point, etc.) as long as the
             data is geo-segregated by grid panel.

           1.05.1 Name Format:
                    LG1m0_37_000_ 20765400_20100601R0 :

                                                                                           Page 25 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                 LG -2-digit product code:
                            • OC (O = Orthoimagery, C = color)
                            • OB (O = Orthoimagery, B = Black and White)
                            • O4 (O = Orthoimagery, 4 = 4 Band)
                            • OR (O = Orthoimagery, R = Infrared)
                            • DL (D = Digital Elevation Model, L = LiDAR)
                            • DP (D = Digital Elevation Model, P = Photogrammetric)
                            • LA (L = LiDAR Point Data, A = All Return)
                            • LF (L = LiDAR Point Data, F = First Return)
                            • LG (L = LiDAR Point Data, G = Ground or Bare Earth)
                            • LI (L = LiDAR Point Data, I = Intensity)
                            • LW (L = LiDAR Point Data, W = Waveform)
                            • HL (H = Hill Shade Model, L = LiDAR)

       Note: Codes for other datasets will be added as needed. If the product is a primary
       deliverable of a technology process, use the technology code as the first character. If
       the product is a derived product from a technology process, use the product term as the
       first character and the technology process as the second character.

              1.05.1.1    1m0 – 3-digit pixel size or post spacing: XuD, with X = resolution before a
                         decimal place, u = unit, D = decimal amount of resolution. Use the unit indicator
                         code (i = Inch, f = Foot, m = Meter, c = Centimeter) as the decimal
                         point. 6 Inch = 6i0, 1.5 feet = 1f5, 1.5 meter = 1m5, 15 centimeters =
                         15c. Note the unit indicator code is always lower case.
                              •      6u0 = pixel size, u= unit indicator code
                              •      6i0 = 6 inches.
                              •      1f0= 1foot,
                              •      1m5= 1.5 meter,
                              •      15c = 15 centimeters, etc.

              1.05.1.2   37 – 2-digit NC ANSI (FIPS) Code : The North Carolina ANSI (FIPS)
                         Code will be used for all data using the North Carolina Grid paneling
                         convention to facilitate its incorporation into national mapping systems.

              1.05.1.3   000 – 3-digit alphanumeric custodian code:
                            • For county maintained data this would be county ANSI (FIPS)
                                  code,
                              http://www.lib.ncsu.edu/gis/countfips.html
                              http://www.census.gov/geo/www/fips/fips65/download.html
                              • 000 for statewide,
                                                                                              Page 26 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping
                             •   city code (RAL)
                             •   agency code (DOT)

              1.05.1.4    20765400 – Map Index Number -8-digit SOS LRM Numbering of the
                         Basic Modular Unit with Millionth place digits. As in the NC
                         Floodplain Mapping Program, the final two digits are reserved for the
                         two-digit indication of scale and location within the Basic Modular
                         Unit.(see Section 1.05.2)

              1.05.1.5 20100601R0 – 10-digit tile project date (YYYYMMDD)(RN)
                       (RN=revision number, 0 is no revisions, R1,R2, etc. to be used as
                       needed.)

              1.05.1.6 Additional user generated info can be appended at the END of the
                       file name; an underscore will be used between the date field and the
                       additional information. While there is no limitation to the number of
                       characters a user can append to a file name, users must be cognizant
                       that the maximum length of a file name (which typically includes the
                       entire file path and not just the file name) can be limited by an
                       operating system or software application.

         1.05.2 Basic Modular Unit with Millionth-Place Digits is an eight-digit SOS LRM
                number. As in the NC Floodplain Mapping Program, the final two digits are
                reserved for the two-digit indication of scale and location within the Basic
                Modular Unit.

                             •   10,000 x10,000 Map Panel Graphic Layout of Integer Codes
                                    Ex. 20770400

                File name: OC6i0_37_000_ 20770400_20100601R0.tif

              1.05.2.1 10,000 x10,000 Map Panel Graphic Layout of Integer Codes
                                     Ex. 20770400

                                                                                    Page 27 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North
     h Carolin
             na Techn
                    nical Speccification
                                       ns for LiD
                                                DAR Basse Mappiing

              1.05.2
                   2.2       5,000 x5,000 Map
                                          M Panel Graphic
                                                  G       Layo
                                                             out of Integerr Codes
                                     Ex. 20770404

              1.05.2
                   2.3       2,500 x 2,500 Map
                                           M Panel Graphic
                                                   G       layout of Integerr Codes
                                     Ex. 207
                                           770416

                                                                                     Page 288 of 74
Adopted January 30, 2013 by Noorth Carolinaa Secretary of
                                                       o State Elainne F. Marshall

 North
     h Carolin
             na Techn
                    nical Speccification
                                       ns for LiD
                                                DAR Basse Mappiing

              1.05.2
                   2.4       1,250 x 1,250 Map
                                           M Panel Graphic
                                                   G       layout of Integerr Codes
                                     Ex. 207
                                           770460

                                                                              1,250 X 1,250 Sub Unit

                 Notte: For a fu
                               ull backgrou
                                          und of the naaming conveention (See Appendix
                                                                              A        D
                                                                                       D)

                                                                                     Page 299 of 74
Adopted January 30, 2013 by Noorth Carolinaa Secretary of
                                                       o State Elainne F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

2        CONTRACT MANAGEMENT
      2.01 Sample Request for Qualifications (RFQ), Example: (See Appendix A)

      2.02   Work Statement: The Contractor shall furnish all materials, superintendence, labor,
             equipment, and transportation and shall execute and complete all of the work
             required by the contract in conformance with these specifications and any
             contractual modifications to these specifications. Any deviation from these
             specifications, unless specifically authorized in writing by the Contracting Officer or
             his representative, shall be sufficient cause for rejection of any part or all of the
             work performed. If a contract change is not approved by the Contracting Officer in
             writing, said change will not be considered for payment.

      2.03   Product Ownership and Contractor Product Retention Requirements: The
             digital data files and any interim and final products are the property of the Client.
             The Contractor will be responsible for storage of digital data files under proper file
             maintenance and backup procedures for a period of at least 5 years at no cost to the
             Client. Digital data should be stored on negotiated media, portable hard drives,
             secure FTP, DVD+/-R, DVD-ROM, CD-R, CD-ROM, or DLT. All digital media
             should be readable by both Windows and UNIX systems. All digital media should
             contain finalized closed sessions, no multi-session discs. All digital media should be
             properly labeled. If CD or DVD type media is used standard cases (no slim-line or
             non-standard cases) will be accepted. The Contractor shall not make, sell, or loan
             copies of the digital files or any other products without the expressed written
             approval of the Contracting Officer. The film or data file shall be handled carefully
             before, during, and after authorized use to ensure that the quality is not degraded and
             is safeguarded from defects. It is the Contractors’ obligation to inform the Client if
             he is no longer able to meet the 5-year storage requirement and provide an
             opportunity to transfer the records to the Client or their designee. This includes any
             change in ownership of the Contractor or inability to meet the 5-year storage
             requirement due to the Contractor going out of business.

      2.04   IT Computer Requirements: Prior to contracting for a LiDAR Project the client
             should inventory the Hardware resources available to be used to house and work
             with the project deliverables. It is common that for an all return point cloud to
             require several terabytes of storage. This does not include the derived products that
             might also be contracted for, i.e., elevation terrain model, hill shade model,
             contours, etc. Adequate storage with built in redundancy such as a Raid system, a
             functioning backup system, offsite storage, an archive plan and adequate processing

                                                                                        Page 30 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

               power are the fundamental elements in an IT system. The client should at a
               minimum review :
                                • Hardware Requirements
                                • Software Requirements
                                • Long Term Storage Requirements
                                • Disaster Recovery Backup
                                • Archiving of Data. Including archiving of source and/or raw
                                   data. (Note: A Backup system is not an Archive system.)

3       LiDAR ACQUSITION

      3.01     LiDAR Project Parameters

             3.01.1 Project Boundaries: Project boundaries shall be defined on a project map in
                    North Carolina state plane coordinates (see section 1.03.2.9 Datum). Said map
                    shall have the appropriate State tiling scheme as an overlay. The project map
                    will be in a digital GIS format, i.e. shapefile or other format suitable to the
                    Contracting Officer, a paper or PDF map may be included as well.
             3.01.2 Principal Contract Deliverables:
                  3.01.2.1 Point Data: Fully compliant LAS V1.2 or V1.3 or greater, Point Record
                             format 1,3,4,5, (or equivalent record format). LAS Version shall be
                             stated in the contract, said version will be determined pursuant to the
                             Clients needs. Note, if the Contracting Officer feels that the client will
                             have difficulty extracting the Bare Earth Points from the point data, he
                             may request a Bare Earth Point Dataset as an additional deliverable.
                  3.01.2.2 Waveform Data (if required)
                  3.01.2.3 Intensity Data (image file)
                  3.01.2.4 Low confidence area polygons (shape file)
                  3.01.2.5 Breaklines (shape file)
                  3.01.2.6 DEM (Digital Elevation Model )(Hydro Flattened)
                  3.01.2.7 FGDC compliant metadata
                  3.01.2.8 QA/QC Reports
                  3.01.2.9 Flight logs
                  See Section 9 for a review of required deliverables.
             3.01.3 Flightline Overlap: 50% is required unless contracting officer specifies a
                     different overlap. Note: mountainous area or areas with dense vegetation need
                     50% overlap coverage; other areas may be adequately covered with less
                     overlap. Overlap should not be reduced below 30%.
             3.01.4 Buffering: Project boundary shall be buffered by a minimum of 2,000 feet.
                     Buffer areas may be adjusted by Contracting Officer.
                                                                                           Page 31 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

           3.01.5 Project Start/Stop Dates: Leaf-off Conditions: Start and Stop dates
                  determined by local conditions. Dates set by Contracting Officer.

4        PRE-PROJECT ACTIVITIES
      4.01 Sensor Certification: When a LiDAR sensor is manufactured, the Inertial
            Reference Systems (INS) and sensor system undergoes laboratory calibration at the
            factory to establish a very precise vertical alignment. Unless the LiDAR sensor is
            damaged or modified, this laboratory calibration is done only once. However, each
            time the LiDAR system is installed, re-installed, or moved within the aircraft, small
            changes in the alignment may occur, requiring field testing of the calibration
            parameters. Routine sensor calibration and maintenance are required to ensure
            proper function of the LiDAR system. LiDAR system components are most
            effectively tested and calibrated by the equipment manufacturer. Prior to
            commencing data acquisition, the contractor should provide the factory calibration
            certification and documentation of preventive maintenance completed either in
            accordance with the manufacturer’s maintenance scheduled , or as justified by
            apparent lack of calibration stability, whichever interval is shorter. Documentation
            that recommended firmware/software upgrades have been installed. If the Contractor
            feels that firmware/software upgrades are too new to be reliable the contractor may
            apply for a waiver from the Contracting Officer.
      4.02 North Carolina In Situ Validation Range Requirements: The state of North
            Carolina has developed a In Situ Validation Range for the purpose of validating
            and/or calibrating sensor systems. The purpose of the In Situ range is to validate the
            sensor in its working environment and ensure that the Contractor(s) can correctly
            and consistently acquire and quality control data collection, and produce data
            products that meet specification. Prior to commencing data acquisition, it is
            recommended that the Contractor acquire data over the validation range, preprocess
            the data and deliver to the Client for evaluation. This requirement can be waived
            upon consent of the Contracting Officer.
      4.03 Daily Calibration Survey: A daily calibration test course shall be established by
            the contractor within the project area. Daily calibration survey data will be
            collected by each sensor over this course at the start and end of each flight mission.
            The calibration sites must be established by ground surveying prior to the collection
            of any aerial LiDAR data for the projects. GPS base stations and surrounding High
            Accuracy Reference Network (HARN) points should be used to control redundant
            RTK GPS surveys and conventional surveys to approximately 8 to 10 calibration
            points at each site. The calibration site should be selected in an open flat area where
            elevation ground truth can be unambiguously established. Elevation points should
            be on smooth, unpainted or bare natural surfaces. Static initialization of the airborne
            GPS should be performed prior to take-off and upon landing. At minimum three

                                                                                       Page 32 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

             flight lines shall be flown over the calibration site for the detection of systematic
             errors in the airborne GPS/IMU and LiDAR system data. The flight pattern is flown
             over the test area in two opposing directions and a cross-flight at 90 degrees to the
             former. A report of the daily calibration results and documentation of calibration
             points used will be furnished to the Contracting Officer and the quality control team.
             Any corrective action taken as a result of the daily calibrations shall be included in
             the report. See Chapter 7 (pages 218-219) of Digital Elevation Model Technologies
             and Applications: The DEM Users Manual for additional information and Appendix
             G: Daily Calibration Survey / Boresight Calibration
       4.04 Flight Line Layout: A digital map showing the study area boundaries and planned
             flight path. Documentation specifying altitude, airspeed, scan angle, scan rate, LiDAR
             pulse rates, receiver return mode, and other flight and equipment information deemed
             appropriate.
     4.05 Ground Control Map shall identify which GPS ground control points are used as base
           stations on particular flight paths with coverage areas and all points used by the contractor
           for field verification. Said Map shall be in an approved GIS format.

5        LiDAR ACQUISITION
         Note: It is conceivable that in some cases, based on specific topography, land cover,
         intended application, or other factors, the Contracting Officer may require acquisition
         specifications different than those defined in this document. All changes in specification
         requirements should be fully documented in project metadata and preapproved in writing
         by the Contracting Officer.

       5.01      Collection
              5.01.1 Multiple Discrete Return, capable of at least 3 returns per pulse.
                     Note: Full waveform collection is both acceptable and welcomed; however,
                     waveform data is regarded as supplemental information. The requirement for
                     deriving and delivering multiple discrete returns remains in force in all cases.

              5.01.2 Intensity Values for each return.
              5.01.3 Nominal Pulse Spacing (NPS) is 1meter, unless the Contracting Officer
                     preapproved in writing a change to the NPS requirement. NPS assessment to be
                     made against single swath, first return data located within the geometrically
                     usable center portion (typically ~90%) of each swath. Average along-track and
                     cross-track point spacing should be comparable. Collections designed to
                     achieve the NPS through swath overlap or multiple passes are generally
                     discouraged. There are conditions where such collections may be permitted.
                     This should be with prior approval by the Contracting Officer.

                                                                                            Page 33 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

         5.01.4 Data Voids [areas => (4*NPS)2, measured using 1st-returns only] within a
                single swath are not acceptable, except:
                              • where caused by water bodies;
                              • where caused by areas of low near infra-red (NIR) reflectivity
                                 such as asphalt or composition roofing; or
                              • where appropriately filled-in by another swath.
         5.01.5 Spatial Distribution of geometrically usable points is expected to be uniform
                and free from clustering. In order to ensure uniform densities throughout the
                data set:
                              • A regular grid, with cell size equal to the design NPS*2 will be
                                 laid over the data.
                              • At least 90% of the cells in the grid shall contain at least one
                                 LiDAR point.
                              • Assessment to be made against single swath, first return data
                                 located within the geometrically usable center portion
                                 (typically ~90%) of each swath.
                              • Acceptable data voids identified previously in this specification
                                 are excluded. Note: This requirement may be relaxed in areas
                                 of significant relief where it is impractical to maintain a
                                 consistent NPS.
         5.01.6 Scan Angle: Total (Field Of View) FOV should not exceed 40⁰ (+/-20⁰ from
                nadir). Quality assurance on collections performed using scan angles wider
                than 34⁰ FOV will be particularly rigorous in the edge-of-swath areas.
                Horizontal and vertical accuracy shall remain within the requirements as
                specified below. Note: This requirement is primarily applicable to oscillating
                mirror LiDAR systems. Other instrument technologies may be exempt from this
                requirement.
         5.01.7 Cross Scans: Contracting officer may require periodic flights at approximately
                12 mile intervals. Said flights shall be approximately perpendicular to normal
                flight lines. These swaths will be used to compare continuity of adjacent flight
                lines during the Q/C.
         5.01.8 Vertical Accuracy of the LiDAR data will be assessed and reported in
                accordance with the guidelines developed by the NDEP and subsequently
                adopted by the ASPRS. The complete guidelines may be found in Section 1.5
                of the Guidelines document. See:
             http://www.ndep.gov/NDEP_Elevation_Guidelines_Ver1_10May2004.pdf

                                                                                     Page 34 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              5.01.8.1 Vertical accuracy requirements using the NDEP/ASPRS methodology
                       are:
                            • FVA <= 24.5cm ACCz, 95% (12.5cm RMSEz) (See Section
                               1.03.5.2.4 For RMSEz definition)
                            • CVA <= 36.3cm, 95th Percentile
                            • SVA <= 36.3cm, 95th Percentile

         5.01.9 Point Cloud Accuracy for the LiDAR data is to be reported independently
                 from accuracies of derivative products (i.e., DEMs). Point cloud data accuracy
                 is to be tested against a TIN constructed from bare-earth LiDAR points.
         5.01.10 Land Cover Testing: Each land cover type representing 10% or more of the
                 total project area must be tested and reported as a Standard Vertical Accuracy
                 (SVA).
              5.01.10.1 For SVAs, the value is provided as a target. It is understood that in
                          areas of dense vegetation, swamps, or extremely difficult terrain, this
                          value may be exceeded. Overall CVA requirements must be met in
                          spite of "busts" in individual SVAs.
                 Note: These requirements may be relaxed in cases:
                               • where there exists a demonstrable and substantial increase in
                                   cost to obtain this accuracy;
                               • where an alternate specification is needed to conform to
                                   previously contracted phases of a single larger overall
                                   collection effort, i.e., multi-year statewide collections, etc;, or
                               • where the contracting officer agrees that it is reasonable and
                                   in the best interest of all stakeholders to use an alternate
                                   specification.
                       (Note: any alteration to this standard must be approved in writing by the
                       Contracting Officer.)
         5.01.11 Relative Accuracy <=7cm RMSEZ within individual swaths; <=10cm
                 RMSEz within swath overlap (between adjacent swaths).
         5.01.12 Flightline Overlap of 50% is recommended to ensure there are no data gaps
                 between the usable portions of the swaths unless approved in writing by the
                 Contracting Officer. Collections in high relief terrain are expected to require
                 greater overlap. Any data with gaps between the geometrically usable portions
                 of the swaths will be rejected.
         5.01.13 Collection Area: Defined Project Area, buffered by a minimum of 2,000 feet.
         5.01.14 Collection Conditions:
              5.01.14.1 Atmospheric: Cloud and fog-free between the aircraft and ground.
              5.01.14.2 Ground:

                                                                                          Page 35 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                              •  Snow free. Very light, un-drifted snow may be acceptable in
                                 special cases, un-melted snow within shadow areas may be
                                 acceptable with prior approval of the Contracting Officer.
                              • No unusual flooding or inundation, (outside of the stream or
                                 river banks) except in cases where the goal of the collection is
                                 to map the inundation. If contractor suspects that parts of the
                                 project area may be flooded the contractor should contact the
                                 Contracting Officer for permission to proceed with the project.
                    5.01.14.2.1 Vegetation: Leaf-off, unless project specific requirements
                               dictate otherwise, prior approval by the contracting officer in
                               writing is required. Collections for specific scientific research
                               projects may be exempted from this requirement, with prior
                               approval.

                              •   As numerous factors will affect vegetative condition at the time
                                  of any collection, penetration to the ground must be adequate
                                  to produce an accurate and reliable bare-earth surface suitable
                                  to meet the DEM specifications or density requirements. Any
                                  ground hidden areas (i.e., areas obscured by dense vegetation
                                  or woods, or areas obscured by overhanging bluffs, ledges or
                                  manmade objects) should be delineated by low confidence area
                                  polygons. Low confidence areas indicate areas where the
                                  vertical data may not meet the data accuracy requirements due
                                  to voids within the data set. If the contractor feels that in his
                                  professional judgment that contact accuracies cannot be met
                                  within an area those areas should be bound by a low
                                  confidence area polygon. Said areas should be significant in
                                  size to warrant notification of a potential user but small enough
                                  as to not jeopardize the integrity of the project.. The
                                  Contractor should take reasonable steps to minimize areas
                                  delineated as low confidence areas.

    5.02      Data Processing and Handling
           5.02.1 All processing shall be performed within the United States of America or its
                  territories unless the contractor gets prior approval in writing from the
                  Contracting Officer.
           5.02.2 All processing should be carried out with the understanding that all point
                  deliverables are required to be in fully compliant LAS format, v1.2, v1.3 or
                  current ASPRS LAS format standard. The Contracting Officer has final

                                                                                       Page 36 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                determination of LAS format to be used. Data producers are encouraged to
                review the LAS specification in detail.
         5.02.3 If full waveform data is collected, delivery of the waveform packets is
                required. LAS v1.3 deliverables with waveform data are to use external
                “auxiliary” files with the extension “.wdp” for the storage of waveform packet
                data. See the LAS v1.3 Specification for additional information.
         5.02.4 GPS Times are to be recorded as Adjusted GPS Time, at a precision sufficient
                to allow unique timestamps for each pulse. Adjusted GPS Time is defined to
                be Standard (or satellite) GPS Time minus 1*109. See the LAS Specification
                for more detail.
         5.02.5 Horizontal Datum shall be referenced to the North Carolina official Survey
                Base (see section 1.03.2.9). Vertical datum shall be referenced to the North
                American Vertical Datum of 1988 (NAVD 88). The most recent NGS
                published Geoid model shall be used to perform conversions from ellipsoidal
                heights to orthometric heights. Mandatory Variable-length Record,
                GeoKeyDirectory must be populated. This record contains the key values that
                define the coordinate system.
         5.02.6 All X, Y, and Z coordinates shall be in North Carolina State Plane.
         5.02.7 All references to the Unit of Measure “Feet” or “Foot” must specify “U.S.
                Survey” in North Carolina.
         5.02.8 Long Swaths (those which result in a LAS file larger than 2GB) should be split
                into segments no greater than 2GB each. Each segment will thenceforth be
                regarded as a unique swath and shall be assigned a unique File Source ID.
                Other swath segmentation approaches may be acceptable, with prior approval.
                Renaming schemes for split swaths are at the discretion of the data producer.
                The Processing Report shall include detailed information on swath
                segmentation sufficient to allow reconstruction of the original swaths if needed.
         5.02.9 Each Swath shall be assigned a Unique File Source ID. The Point Source ID
                field for each point within each LAS swath file shall be set equal to the File
                Source ID prior to any processing of the data. See the LAS Specification.
         5.02.10 Point Families (multiple return “children” of a single “parent” pulse) shall be
                maintained intact through all processing prior to tiling. Multiple returns from a
                given pulse shall be stored in sequential (collected) order.
         5.02.11 All collected swaths are to be delivered as part of the “Raw Data Deliverable”
                or arrangements need to be made by the contracting officer for storage,
                retrieval, and archiving of the “Raw Data Deliverable”. This includes
                calibration swaths and cross-ties. All collected points are to be delivered. No
                points are to be deleted from the swath LAS files. This in no way requires or
                implies that calibration swath data are to be included in product generation.
                Excepted from this are extraneous data outside of the buffered project area

                                                                                     Page 37 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                (aircraft turns, transit between the collection area and airport, transit between
                fill-in areas, etc.). These points may be permanently removed.

    5.03    American Society of Photogrammetry and Remote Sensing (ASPRS)/LAS
            Standard Classifications: LiDAR point classes should be used in LiDAR point
            classification unless previously approved by the Contracting Officer. Any
            deviations from ASPRS classifications should be fully documented in project
            metadata. At a minimum Class 1, Class 2, Class 7, Class 9, and Class 11 (if
            applicable) should be populated. Class 8 and Class 10 should be populated when
            applicable if contour deliverables are a derived product.

              LIDAR Point Classes Classification            Meaning
              Value (bits 0:4)
              0                                             Created, never classified
              1                                             Unclassified1
              2                                             Ground
              3                                             Low Vegetation
              4                                             Medium Vegetation
              5                                             High Vegetation
              6                                             Building
              7                                             Low Point (noise)
              8                                             Model Key-point (mass
                                                            point)
              9                                             Water
              10                                            Ignored Ground (Breakline
                                                            Proximity)
              11                                            Withheld (If the “Withheld”
                                                            bit is not implemented the
                                                            processing software or if
                                                            client/end-user software is
                                                            not capable of handling
                                                            “withheld” bits)
              12                                            Overlap Points2
              13-31                                         Reserved for ASPRS
                                                            Definition

              Withheld points are typically those points that were culled during preprocessing
              or post-processing. These points are typically not used in LiDAR processing. If
              Client end-user software is capable of handling withheld flags as defined in the
              ASPRS/LAS specifications, outliers, blunders, noise points, geometrically
              unreliable points near the extreme edge of the swath (the geometrically usable
              center portion is typically ~90% of each swath) , and other points deemed
              unusable can be identified using the “Withheld” flag. It is important to verify this

                                                                                          Page 38 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              capability. Software used for analysis and visualization of final product
              deliverables may be different than software used to pre- and post-process LiDAR
              data. For example, at the present time, ESRI products for LAS to multipoint
              currently do not process withheld flags. If Client end-user software is not capable
              of handling withheld flags as defined in the ASPRS/LAS specifications, withheld
              points may be identified using Class =11. This applies primarily to points which
              are identified during preprocessing or through automated post-processing
              routines. “Noise points” subsequently identified during manual Classification and
              Quality Assurance/Quality Control (QA/QC) may be assigned the standard LAS
              classification value for “Noise” (Class =7), regardless of whether the noise is
              “low” or “high” relative to the ground surface.

         5.03.1 Overlap points are typically those points that were immediately culled during
                 the merging of overlapping flight lines. This does not include geometrically
                 unreliable points near the extreme edge of the swath which are considered
                 withheld points as defined above. If overlap points are required to be
                 differentiated by the Client, Contracting Officer, or Contractor, said points
                 must be identified using a method that does not interfere with their
                 classification, such as:
                              • Overlap points are tagged using Bit:0 of the User Data byte, as
                                   defined in the LAS specification. (SET=Overlap).
                              • Overlap points are classified using the Standard Class values +
                                   16.
                              • Other techniques as agreed upon in advance.
                              • The technique utilized must be clearly described in the project
                                   metadata files.
              If Client end-user software is capable of processing flags as defined in the
              ASPRS/LAS specifications, the ASPRS/LAS “Overlap” classification (Class=12)
              shall not be used. ALL points not identified as “Withheld” are to be classified. If
              Client end-user software is not capable of processing flags as defined in the
              ASPRS/LAS specifications, the “overlap” classification (Class 12) can be used
              with prior approval of the Contracting Officer.
               Note: A standard bit setting for identification of overlap points has been planned
              for a future version of LAS.

         5.03.2 Positional Accuracy Validation: The absolute and relative accuracy of the
                data, both horizontal and vertical, and relative to known control, shall be
                verified prior to classification and subsequent product development. This
                validation is obviously limited to the Fundamental Vertical Accuracy,
                                                                                      Page 39 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

                  measured in clear, open areas. A detailed report of this validation is a required
                  deliverable.
           5.03.3 Classification Accuracy: It is expected that due diligence in the classification
                  process will produce data that meets the following test:
                               • Within any 1km x 1km area, no more than 2% of non-withheld
                                  points will possess a demonstrably erroneous classification
                                  value.
                               • This includes points in Classes 0 and 1 that should correctly be
                                  included in a different Class as required by the contract.
                Note: This requirement may be relaxed to accommodate collections in areas
                where the Contracting Officer agrees classification to be particularly difficult.

                                •    Classification Consistency: Point classification is to be
                                     consistent across the entire project. Noticeable variations in
                                     the character, texture, or quality of the classification between
                                     tiles, swaths, lifts, or other non-natural divisions will be cause
                                     for rejection of the entire deliverable.
      5.04 Tiles: Shall be based on the North Carolina Base Modular unit and its subdivisions
             as dictated by tile size designated within the contract specifications.
          5.04.1 North Carolina Grid Panel Scheme (see appendix D)
          5.04.2 Tile Names shall use the “Naming Convention for Geospatial Data presented
                  in the North Carolina Grid Panel Scheme.”
          5.04.3 Tile Size must be an integer multiple of the cell size of raster deliverables.
          5.04.4 Tile must be sized using the same units as the coordinate system of the data.
          5.04.5 Tiled Deliverables shall conform to the tiling scheme, without added overlap.
          5.04.6 Tiled Edge-Match Deliverables shall be seamlessly and without gaps in both
                  the horizontal and vertical.
          5.04.7 Tile Size for All Deliverables shall be the same. Raster, point, and vector data
                  if said data is to be delivered in a tile format shall be the same as LiDAR data.

6       HORIZONTAL AND VERTICAL QUALITY CONTROL: If at all practical there
        should be an independent Quality Control Contractor employed for project review. North
        Carolina Geodetic Survey (NCGS) and North Carolina Center for Geographic
        Information and Analysis (NCCGIA) may be able to provide some guidance and
        assistance. Quality Control will be conducted by Quality Control Area (QC area). A QC
        area is that project area within a county boundary. If the project includes multiple
        counties or areas within multiple counties there will be a QC area for each county area,
        i.e., if it is a 4 county project then there will be 4 QC areas. If the project area is part of a
        county there is a QC area for that part of the county. A project buffer that includes an
        area within another county does not constitute an additional QC area. (see Appendix E)
                                                                                            Page 40 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

    6.01      Independent Quality Control Checkpoints:
           6.01.1 Land Cover Categories: The Quality Control Contractor will categorize all
                  land into one of five major land cover categories representative of the project
                  area (1) open terrain (e.g., bare-earth, sand, rock, plowed fields, short grass,
                  golf courses); (2) high grass, weeds, and crops (e.g., hay, corn, wheat, tobacco);
                  (3) brush lands and low trees; (4) fully forested; and (5) urban areas (vicinity of
                  manmade structures, preferably high density). USGS National Land Cover
                  Data 2006 (www.mrlc.gov) should be consulted as an initial reference before
                  final determination is made and the latest ortho photography should be
                  reviewed.
           6.01.2 Checkpoint Selection: Quality Control Contractor will direct independent
                  survey contractors to select 20 or more checkpoints, in each of the five land
                  cover categories, except for forested areas where 40 checkpoints will be
                  surveyed for each QC area. Each checkpoint should be on terrain that is flat or
                  uniformly sloping within 5 meters in all directions (i.e., no breaklines within 5
                  meters of the checkpoint). Checkpoints clustered together will be rejected. The
                  Quality Control Contractor will provide maps of land-cover categories, and the
                  survey contractors will be provided with large-area polygons dispersed
                  throughout each county within which the surveyors will select the checkpoints.
                  Where possible, checkpoints should be interspersed throughout a QC area so
                  that checkpoints will cover different flight lines. For example, if LiDAR flight
                  lines are generally north-south, it is ideal for surveyors to survey in the vicinity
                  of east-west roads in order to disperse checkpoints to cover different flight
                  lines. The checkpoints in urban areas should be located, if possible, on clearly
                  defined points expected to be visible on LiDAR intensity images, e.g., where a
                  paint stripe on a road intersects with a curb line; recognizing that some points
                  in urban areas may subsequently prove to be invisible on the LiDAR intensity
                  image, those that are visible will be used to evaluate the LiDAR horizontal
                  accuracy (Accuracyr) in addition to its vertical accuracy (Accuracyz).
           6.01.3 Checkpoint Surveys: Quality Control Contractor will contract for
                  independent surveys of all checkpoints to 5-cm Local Network accuracy
                  according to NOAA Technical Memorandum NOS NGS-58, "Guidelines for
                  Establishing GPS-Derived Ellipsoid Heights (Standards: 2 cm and 5 cm),"
                  Version 4.3, November 1997 (referred to as NGS-58). Static field procedures
                  following the NGS-58 guidelines are preferred for establishing checkpoints.
                  Alternatively, GPS Real Time Kinematic (RTK) field procedures using the
                  North Carolina Real Time Network (RTN) or by establishing a temporary RTK
                  base station may be used providing: (1) the temporary RTK base station is
                  established on an existing NC HARN, NGS 3-D mark (that has published
                  vertical value of 2nd order or higher)or a new NGS-58 mark established by
                  NCGS; and (2) RTK can only be used in open areas, and each RTK point must
                  be occupied twice on different days and at different times of the day. The
                  purpose is to ensure different atmospheric conditions and significantly different
                  satellite geometry. The difference between observations must not exceed 5 cm.
                  Online Processing User Service (OPUS) can be used if the contractor obtains
                  written approval from NC Geodetic Survey. Third-order or higher conventional
                                                                                          Page 41 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                surveys may be used to extend control from open areas (surveyed by GPS) to
                forested areas where GPS signals are blocked. Trigonometric leveling may be
                used in lieu of conventional leveling. To use trigonometric leveling, the field
                procedure used by the contractor must be approved by Quality Control
                Contractor. These checkpoints will be used for the official vertical accuracy
                assessments (Fundamental Vertical Accuracy and the Consolidated Vertical
                Accuracy) of the bare-earth LiDAR data after post processing.
         6.01.4 Cluster Survey Points: Additional survey measurement should be included
                where possible surrounding the control point being established for the vertical
                comparisons in vegetated areas. This will include both conventional methods
                and RTK. For RTK surveys, additional surrounding points within a few meters
                of the new control point should be established to help identify whether the
                LiDAR penetrated the vegetated surface. The same procedure can be utilized
                for conventional surveys. While the total station is set up, the survey
                instrument person could move a few meters in each direction to collect
                additional measurements. These additional cluster points will not be used for
                vertical accuracy assessments, but they will be used to evaluate artifacts and
                cleanliness.
         6.01.5 Cross Section Surveys: This survey will only be used when specified in the
                contract. Cross section surveys are be used when the data is collected along
                streams for flood mapping applications. The number of cross sections will
                depend on the water body, the surrounding terrain, and other local factors. A
                total of _(to be determined by contract)_ cross sections of varying terrain will
                be measured. Ideally stream channels should be measured, but standard
                Airborne LiDAR will not include underwater measurements. If streams cannot
                be measured, undulating terrain or drainage ditches exceeding 3 meter width
                could be measured using RTK. Measurements could be taken at two meter
                intervals for 50 meters over undulating terrain. These cross section surveys
                will not be used for official vertical accuracy assessments, but they will be used
                to assess the bare-earth mass points to ensure that post-processing did not
                overly flatten stream channel geometry (stream banks) used for hydraulic
                modeling.
         6.01.6 Documentation: The survey company will mark each checkpoint with a 60d
                nail or larger. Photographs will be used to document the location, the land
                cover surrounding each stake, and the uniform slope of the terrain surrounding
                each stake. A full report will be required outlining the methodology of the data
                collection, the equipment used, software, full output of duplicate point
                comparisons, least squares adjustment, and any information pertinent to the
                survey. FGDC metadata will also be included with the final coordinates.
         6.01.7 Orthometric Heights: Geoid09 or current Geoid will be used to convert GPS
                ellipsoid heights into orthometric heights for each checkpoint, using NAVD 88,
                the specified vertical datum. Contact North Carolina Geodetic Survey for
                verification of current Geoid.
         6.01.8 3-D Coordinate Files: The PLS will provide Quality Control Contractor with
                Microsoft Excel 3-D point files (X-Y-Z values) by State Plane coordinates
                (U.S. survey feet) to 2 decimal places for the checkpoint surveys, cluster point
                                                                                      Page 42 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

               surveys, and cross section surveys along with a code of the method used to
               derive the coordinate value (i.e., GPS or conventional survey).
        6.01.9 Security: Quality Control Contractor will ensure that these 3-D coordinate
               files are secured and not made available outside of Quality Control Contractor
               and the Contracting Officer or his designee prior to receipt of the post-
               processed LiDAR data.
    6.02 LiDAR Accuracy Assessment
        6.02.1 LiDAR Acquisition Plans: The PLS in responsible charge of the elevation
               data collection will provide Quality Control Contractor with acquisition
               planning information, including, but not limited to, flight line directions, types
               of sensors, pulses per second, flying altitude above mean terrain, swath width,
               average point spacing, maximum positional dilution of precision (PDOP),
               maximum airborne GPS baselines, and sidelap percentage.
        6.02.2 LiDAR Acquisition Data: Upon request, the PLS will provide Quality
               Control Contractor with actual data for each sensor on each day, to include
               daily calibration checks, flying altitude, average point spacing, maximum
               PDOP, maximum GPS baselines, etc., plus maps showing actual flight lines
               and swaths, by dates acquired and sensors (when multiple LiDAR systems are
               used). The daily Acquisition Report will be provided to the Quality Control
               Contractor by the end of the second business day following data acquisition to
               ensure data is actually processed in a timely manner.
        6.02.3 Bare Earth Data: The PLS will post-process the LiDAR data to generate bare
               earth 3-D ASCII files or Triangulated Irregular Network (TIN) files.
        6.02.4 Interpolated Z-values: When notified that the ASCII/TIN data are complete,
               2-D (X-Y coordinates without Z-values) will be provided for all checkpoints
               per land cover category to the PLS. The PLS will immediately (within a few
               minutes) compute the interpolated LiDAR Z-values for the X-Y coordinates of
               the checkpoints and provide 3-D (X-Y-Z) files to Quality Control Contractor.
               Fewer than 20 checkpoints may be allowed in some land cover categories, if
               difficulty is encountered in finding certain vegetation groups.
        6.02.5 Checkpoint Elevation Discrepancies: A spreadsheet with checkpoint
               elevation discrepancies (Z-values interpolated from LiDAR TIN minus Z-
               values from surveyed checkpoints) separated by land cover categories will be
               prepared. Draft values for Fundamental, Consolidated, and Supplemental
               vertical accuracies will be determined.
        6.02.6 Fundamental Vertical Accuracy Test: Using only the checkpoints in open
               terrain, the RMSE will be computed of the bare-earth LiDAR dataset. If the
               RMSEz value is equal to or less than 12.5 cm, then this test passes and the
               Fundamental Vertical Accuracyz = 1.9600 x RMSEz; proceed to step 6.02.7. If
               the RMSEz is larger than the specified RMSE, there may be systematic errors
               or problem with the LiDAR sensor and/or parameters used for post-processing.
               All systematic errors need to be corrected and the dataset resubmitted for re-
               evaluation with additional checkpoints. Since there is no vegetation to be
               removed in post processing, there should be no excuse for the LiDAR dataset
               not performing to specifications in open terrain.

                                                                                     Page 43 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

         6.02.7 Supplemental Vertical Accuracy Test: For each of the other four land cover
                categories, the quality control team will determine the 95th percentile error
                separately by land cover category. The 95th percentile equals the Supplemental
                Vertical Accuracy at the 95% confidence level by individual land cover
                category. Although there is no standard to be met, any individual land cover
                category with a 95th percentile error significantly larger than 1.6 ft (49.0 cm) is
                an indication that there may be a systematic problem in post-processing the
                LiDAR data for that type of land cover. Such information is valuable in trouble
                shooting should the Consolidated Vertical Accuracy test fail. See Section
                1.03.5.2.14 95th Percentile and “Issue 37: Quality Control of Light Detection
                and ranging (LiDAR) Elevation Data in North Carolina for Phase II of the
                NCFMP” for guidance in figuring the 95th Percentile.
                              http://www.ncfloodmaps.com/pubdocs/issue_papers/IP37-
                              phaseII_lidar_qc.pdf

         6.02.8 Consolidated Vertical Accuracy Test: Using all checkpoints in all five land
                cover categories combined, the quality control team will determine the 95th
                percentile error for the consolidated dataset. The 95th percentile equals the
                Consolidated Vertical Accuracy at the 95% confidence level for all land cover
                categories combined. If the Consolidated Vertical Accuracy is less than 1.6 ft
                (49.0 cm), then the dataset passes; if not, the dataset fails. For each dataset, the
                quality control team will also evaluate the error outliers that are larger than the
                95th percentile. Outliers larger than 6.6 ft (2 meters) will be cause for
                investigation by the LiDAR provider to explain the large errors, but such
                outliers will not necessarily cause the dataset to fail. These will be evaluated on
                a case-by-case basis by the quality control team. The quality control team will
                document the magnitude of the errors that are larger than the 95th percentile.
         6.02.9 Vertical Accuracy Assessment and Reporting: The Quality Control Team
                will prepare a LiDAR Accuracy Assessment Report that reports the following:
                 • Map with location of checkpoints, color-coded by land cover category

                  •   Fundamental Vertical Accuracy at 95% confidence level in open terrain
                      using RMSEz x 1.9600, compared with the 1.19 ft specification;

                  •   Consolidated Vertical Accuracy at 95th percentile in all land cover
                      categories combined, compared with the 1.61 ft specification;

                  •   Supplemental Vertical Accuracy at 95th percentile, reported separately for
                      open terrain, weeds and crops, scrub, forest, and built up areas, compared
                      with the target of 1.61 ft.;

                  •   Graphs showing the 95th percentile errors and RMSE errors, graphed
                      separately for each of the five land cover categories;

                  •   Magnitude of outliers larger than the 95th percentile, by land cover
                      category;
                                                                                        Page 44 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                    •   Graph that illustrates the magnitude of the differences between the
                        checkpoints and LiDAR data by specific land cover category, sorted from
                        lowest to highest;

                    •   Overall descriptive statistics to include RMSE, mean, median, skew,
                        standard deviation, minimum and maximum errors, for each land cover
                        category; and

                    •   Histogram showing the frequency of checkpoint elevation differences,
                        normally by 1 cm increments between the largest negative error and the
                        largest positive error; this helps to visualize the outliers and proximity to a
                        normal error distribution.

    6.03        Error Assessment
           6.03.1 Assessments by Land Cover: The causes for the data to not pass the accuracy
                  criteria differ according to land-cover category. Typically, data in category "a"
                  (open terrain) should pass the Fundamental Vertical Accuracy criteria unless
                  there is a systematic problem; however, the daily calibration checks should
                  confirm that the system performed well at the test site (on that same day with
                  the same sensor), and the test site should be on bare terrain or short grass only.
                  If the Consolidated Vertical Accuracy value is higher than the 1.6 ft (49.0 cm)
                  standard, whereas the Fundamental Accuracy test passed the 1.2 ft (36.3 cm)
                  standard, errors in post-processing need to be corrected, and the individual
                  Supplemental Vertical Accuracy assessments should assist in trouble shooting.
                  If Supplemental Vertical Accuracy tests are considerably higher than 1.6 ft
                  (49.0 cm) for land cover categories "c" (scrub) or "d" (forests), the most
                  probable causes are shortcomings in the vegetation-removal procedures. If the
                  Supplemental Vertical Accuracy tests are considerably higher than 1.6 ft (49.0
                  cm) for land cover category "e" (urban areas), the most probable cause is a
                  systematic problem with handling buildings or abnormal responses from
                  asphalt.
           6.03.2 Assessments by Error Locations: The Quality Control Team will evaluate
                  the location of significant errors to see if they are consistent throughout the area
                  and to determine where these errors are located within the flight line (e.g., near
                  the beginning or end of swaths).
           6.03.3 Assessments by Dates/Sensors: The Quality Control Team will evaluate the
                  datasets to see if errors are distinguishable by dates or by individual sensors.
           6.03.4 Accuracy Assessment Report: If the above assessments do not yield the
                  probable source of systematic errors, the Quality Control Team will prepare an
                  Accuracy Assessment Report indicating that the LiDAR data did not pass the
                  accuracy criteria. This report will include the same type of information in task
                  6.02.9 above, but with a printout of z-value errors, sorted by elevations, without
                  x/y coordinates. The report may identify polygons within which major errors
                  are clustered, to assist in trouble-shooting. The report may recommend that
                                                                                           Page 45 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                quality control team spot check the elevations on several of the independent
                checkpoints that yielded the poorest results when compared with the
                interpolated LiDAR elevations, or the report may recommend that the LiDAR
                vendor assess the quality of individual components (airborne GPS, inertial
                measuring unit (IMU), and laser range systems) as well as the integrated
                system.
         6.03.5 Airborne GPS Verification: The PLS will examine GPS flight trajectories;
                verify the Positional Dilution of Precision (PDOP) and/or Vertical Dilution of
                Precision (VDOP); verify GPS satellite residuals; verify the satellite phase
                RMS; compare forward and reverse flight trajectories' combined separation;
                verify weighting adjustments when two or more differential base stations are
                used; verify the base station distance separation; verify position standard
                deviations; check satellite health; check geo-magnetic observations; verify that
                the correct vertical datum was used; and verify the correct application of the
                Geoid09 calculation of orthometric heights.
         6.03.6 IMU Verification: The PLS will review the Kalman filter, the measurement
                residual ratio (MRR), and the consecutive measurement rejections settings;
                confirm that the IMU was in "fine align" mode for the whole of the data set;
                check accelerometer drift and scale factor and gyro drift and scale factor to
                ensure that they are within specifications; compare GPS trajectory with re-
                computed IMU trajectory and investigate large discrepancies; and review IMU
                to lever arm parameter measurements and ensure that they are entered correctly
                in the proper reference system.
         6.03.7 Laser Range Verification: The PLS will review raw laser ranges; identify
                areas of high dropouts (no returns) and correlate them to justifiable features;
                review scanner mirror angles (galvanometers or micro-controller) reports;
                examine intensity images; and review system-generated error log sheets.
         6.03.8 Total System Verification: The PLS will review daily calibration checks and
                compare to system flight parameters; use CAD software to analyze flight lines
                and verify pitch, roll, and heading errors; check overlap for roll and scaling
                errors; check ground features for pitch (e.g., buildings, bridges); if water bodies
                exist, check scaling errors; compare cross flight data for altitude; review
                parameters if data were "corrected" or adjusted for pitch, roll, and heading
                errors; and verify vegetation removal procedure.
         6.03.9 Systematic Error Corrections: If systematic errors are found, the data will be
                reprocessed by the PLS, with clear written explanations provided to the quality
                control team. If no systematic errors are found, the process moves to Phase 4
                discussed below.
         6.03.10 Recalculation of Accuracy Statistics: Using additional QC checkpoints, the
                PLS will interpolate the LiDAR dataset for the new checkpoints' 2-D (X-Y)
                coordinate values and provide 3-D (X-Y-Z) files for re-computation of
                Fundamental Vertical Accuracy and Consolidated Vertical Accuracy. The QC
                Contractor may be tasked to collect additional points from those points held in
                reserve.
         6.03.11 LiDAR Accuracy Assessment Report: If the new calculations from task
                6.03.10 pass the accuracy criteria, the quality control team will prepare a

                                                                                       Page 46 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                 LiDAR Accuracy Assessment Report indicating this fact. If the new
                 calculations do not pass the accuracy criteria, a provisional Accuracy
                 Assessment Report will document the new statistics and recommend
                 alternatives (when pre-approved by Quality Control Contractor) listed in 6.04.
    6.04     Final Resolution of Problems
         6.04.1 Provisional LiDAR Accuracy Assessment Report: As coordinated by client,
                 the provisional Accuracy Assessment Report will document the accuracy
                 assessments and recommend resolution to problems identified.
         6.04.2 LiDAR Vendor Checkpoints: The PLS will provide the Quality Control
                 Team with checkpoints used to validate the LiDAR adjustments, so that the
                 Quality Control Team can determine the proximity of the LiDAR vendor
                 checkpoints to the QC Contractor checkpoints, or perform independent surveys
                 of the vendor's checkpoints.
         6.04.3 Elevation Contractor Control Points: The PLS will provide the quality
                 control team with control points and/or Least Squares Adjustments used to
                 define the control points for the LiDAR processing. This will allow the quality
                 control team to perform an independent analytical assessment of the vendor’s
                 control points to determine if there are any fundamental flaws or discrepancies
                 in the control used for the project area. If the control points are inaccurate, the
                 LiDAR vendor will need to resolve the control point(s) issue and reprocess the
                 LiDAR data to fit the new control values. If the control points used are
                 accurate, then 6.04.4 shall be implemented.
         6.04.4 Potential Resurveys of Quality Control Contractor Checkpoints: The
                 LiDAR vendor will be provided with 3-dimensional coordinates with
                 supporting documentation and will be afforded the opportunity to
                 independently survey and analyze the checkpoints used for the RMSE and 95th
                 percentile calculations at the vendor’s expense. If discrepancies are found with
                 the coordinates, the Quality Control Team will rectify the problem and reassess
                 the LiDAR data. If no discrepancies are found, the vendor shall comply with
                 the results and establish procedures to correct the LiDAR data through
                 reprocessing and/or reacquisition of the data.
         6.04.5 Potential Reacquisition of LiDAR: The quality control team may decide that
                 the LiDAR vendor be allowed to refly the area and acquire a new LiDAR
                 dataset, perhaps with shorter GPS baselines, lower PDOP values, lower flying
                 altitude, narrower swath widths, etc. This would normally be performed at the
                 LiDAR firm’s expense.
         6.04.6 Detailed Ground Surveys: The PLS’s firm may be offered the opportunity to
                 perform extensive ground surveys of cross sections to satisfy the data needs for
                 hydraulic modeling.
    6.05 Additional Quality Assessments: The PLS’s firm may be tasked to provide
            additional deliverables and assessments: LiDAR intensity images, and shaded relief
            images of selected sample bare-earth mass point tiles.
         6.05.1 Intensity Images: In addition to the intensity images being used by the
                 LiDAR vendor to assist in post-processing vegetation removal, the quality
                 control team will request samples of intensity images at the urban area
                 checkpoints so as to evaluate the horizontal accuracy of the LiDAR data, for

                                                                                        Page 47 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

                 comparison with the LiDAR vendor's own assessment of horizontal accuracy
                 based on periodic calibration checks.
          6.05.2 Assessment of Cross Sections: Cross sections of survey breakpoints along a
                 stream channel will be compared to the corresponding cross section derived
                 from the TIN. Using the survey cross sections, the horizontal component of the
                 line derived from the survey points will be draped over the TIN. Interpolated
                 elevation values will be generated from the intersection of the line with the
                 vertices of the TIN and a new TIN cross section will result. Comparisons will
                 be made between the surveyed cross section and the interpolated TIN Cross
                 section. Differences will be measured at the breakpoints of the surveyed cross
                 sections. Values greater than 49.0 cm will be evaluated on a case-by-case
                 basis.
          6.05.3 Assessment of Edge Matching: Edge matching will be tested with a variety of
                 comparative methods. These methods will include a vector and/or a raster
                 approach. If the data were flown with the same sensor, and the post processing
                 procedures are consistent, very little change should be visible along seam
                 edges. One method will be to compare the density of points within a given grid
                 size (i.e. 20 ft.) along the tile boundaries. Significant discrepancies of point
                 densities between adjacent tiles will flag further analysis. A second approach
                 will be to build the TIN of each tile and compare the number of TIN triangles
                 to the adjacent tile, or build a TIN of one tile including a 100 foot buffer of
                 points from the adjacent TIN. Significant differences will again be flagged for
                 review. A third approach would be to use a raster technique and create a TIN
                 GRID. Visually the tile edges should be fairly seamless due to the interpolation
                 of tile edges. Secondary to this, adjacent pixels along seam edges can be
                 compared for elevation differences.
          6.05.4 Assessment of Superfluous Elevations: Elevations will have a minimum and
                 maximum value that should reflect the true range of the surface being
                 measured. LiDAR at times can have errant elevation values that are well above
                 or below the surface. Statistical analysis will be performed on the elevation
                 data which will include: minimum and maximum elevation, standard deviation
                 and the total number of points within a given class range (i.e. two-foot
                 increments). Elevation values out of the norm, more than 20 feet from the next
                 populous class will be flagged for review.
      6.06 Additional Duties of Quality Control Contractor.
          6.06.1 Review LAS Point allocation
          6.06.2 Review Flight Logs

7       HYDRO-FLATTENING REQUIREMENTS:
               Note: Please refer to Appendix B for reference information on hydro-flattening.
                       Hydro-flattening pertains only to the creation of derived DEMs. No manipulation of or
                       changes to originally computed LiDAR point elevations are to be made. Breaklines may
                       be used to help classify the point data.

                                                                                                Page 48 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                     Breaklines: North Carolina does not require any particular process or
                     methodology be used for breakline collection, extraction, or integration.
                     However, the following general guidelines must be adhered to:

                              •   Bare-earth LiDAR points that are in close proximity
                                  breaklines should be excluded from the DEM generation
                                  process. This is analogous to the removal of masspoints for
                                  the same reason in a traditional photogrammetrically
                                  compiled DTM.

                              •   The proximity threshold for reclassification as “Ignored
                                  Ground” is at the discretion of the data producer, but in
                                  general should be approximately equal to the NPS.

                              •   These points are to be retained in the delivered LiDAR point
                                  dataset and shall be reclassified as “Ignored Ground” (class
                                  value = 10) so that they may be subsequently identified.

                              •   Delivered data must be sufficient for the Client to effectively
                                  recreate the delivered DEMs using the LiDAR points and
                                  breaklines without significant further editing.

    7.01   Inland Ponds and Lakes:
        7.01.1 ~2-acre or greater surface area (~350’ diameter for a round pond) at the time of
               collection.
        7.01.2 Flat and level water bodies (single elevation for every bank vertex defining a
               given water body).
        7.01.3 The entire water surface edge must be at or below the immediately surrounding
               terrain.
        7.01.4 Long impoundments such as reservoirs, inlets, and fjords, whose water surface
               elevations drop when moving downstream, should be treated as rivers.
    7.02 Inland Streams and Rivers:
        7.02.1 100’ nominal width: This should not unnecessarily break a stream or river into
               multiple segments. At times it may squeeze slightly below 100’ for short
               segments. Data producers should use their best professional judgment.
        7.02.2 Flat and level bank-to-bank (perpendicular to the apparent flow centerline);
               gradient to follow the immediately surrounding terrain.
        7.02.3 The entire water surface edge must be at or below the immediately
               surrounding terrain.
        7.02.4 Streams channels should break at road crossings (culvert locations). These road
               fills should not be removed from DEM. However, streams and rivers should
               not break at elevated bridges. All elevated portions of Bridges should be
                                                                                       Page 49 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

               removed from DEM. When the identification of a feature as a bridge or culvert
               cannot be made reliably, the feature should be regarded as a culvert.
    7.03 Non-Tidal Boundary Waters:
        7.03.1 Represented only as an edge or edges within the project area; collection does
               not include the opposing shore.
        7.03.2 The entire water surface edge must be at or below the immediately surrounding
               terrain.
        7.03.3 The elevation along the edge or edges should behave consistently throughout
               the project. May be a single elevation (i.e., lake) or gradient (i.e., river), as
               appropriate.
    7.04 Tidal Waters:
        7.04.1 Water bodies such as oceans, seas, gulfs, bays, inlets, salt marshes, very large
               lakes, etc. Includes any water body that is affected by tidal variations.
        7.04.2 Tidal variations over the course of a collection or between different collections
               will result in discontinuities along shorelines. This is considered normal and
               these “anomalies” should be retained. The final DEM should represent as
               much ground as the collected data permits.
        7.04.3 Variations in water surface elevation resulting in tidal variations during a
               collection should NOT be removed or adjusted, as this would require either the
               removal of valid, measured ground points or the introduction of unmeasured
               ground into the DEM. The client’s priority is on the ground surface, and
               accepts there may be occasional, unavoidable irregularities in water surface.

                7.04.3.1        Scientific research projects in coastal areas often have very
                        specific requirements with regard to how tidal land-water boundaries are
                       to be handled. For such projects, the requirements of the research will
                        take precedence.

    7.05     Single-Line Streams:
           7.05.1 Breaklines for single-line streams shall be collected unless waved in writing by
                  the Contracting Officer. If collected the following guidelines are required:
                7.05.1.1       All vertices along single-line stream breaklines are at or below the
                               immediately surrounding terrain.
                7.05.1.2       Single-line stream breaklines are not to be used to introduce cuts
                               into the DEM at road crossings (culverts), dams, or other such
                               features. This is hydro-enforcement and as discussed in Appendix
                               B, creates a non-traditional DEM that is not suitable for integration
                               into the National Elevation Dataset (NED).
                7.05.1.3       All breaklines used to modify the surface are to be delivered to the
                               client with the DEMs.
                                                                                        Page 50 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

    7.06    Docks or Piers: These guidelines apply only to docks or piers that follow the
            coastline or water’s edge, not for docks or piers that extend perpendicular from the
            land into the water. If it can be reasonably determined where the edge of water most
            probably falls, beneath the dock or pier, then the edge of water will be collected at
            the elevation of the water where it can be directly measured. If there is a clearly-
            indicated headwall or bulkhead adjacent to the dock or pier and it is evident that the
            waterline is most probably adjacent to the headwall or bulkhead, then the water line
            will follow the headwall or bulkhead at the elevation of the water where it can be
            directly measured. If there is no clear indication of the location of the water’s edge
            beneath the dock or pier, then the edge of water will follow the outer edge of the
            dock or pier as it is adjacent to the water, at the measured elevation of the water.

    7.07    Island Features: The shoreline of islands within water bodies shall be captured as
            two-dimensional breaklines in coastal and/or tidally influenced areas and as three-
            dimensional breaklines in non-tidally influenced areas. Island features will be
            captured for features one-half acre in size or greater. These breaklines will be
            delivered as closed polygons with constant elevation.

            An island within a Closed Water Body Feature will also have a “donut polygon”
            compiled in addition to an island polygon.

                      Note: Breaklines: North Carolina does not require any particular process
                      or methodology be used for breakline collection, extraction, or
                      integration. However, the following general guidelines must be adhered
                      to:
                                   • Bare-earth LiDAR points that are in close proximity
                                      breaklines should be excluded from the DEM generation
                                      process. This is analogous to the removal of masspoints
                                      for the same reason in a traditional photogrammetrically
                                      compiled DTM.

                                   •   The proximity threshold for reclassification as “Ignored
                                       Ground” is at the discretion of the data producer, but in
                                       general should be approximately equal to the NPS
                               .
                                   •   These points are to be retained in the delivered LiDAR
                                       point dataset and shall be reclassified as “Ignored
                                       Ground” (class value = 10) so that they may be
                                       subsequently identified.
                                                                                      Page 51 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

    North Carolina Technical Specifications for LiDAR Base Mapping

                                   •   Delivered data must be sufficient for the Client to
                                       effectively recreate the delivered DEMs using the LiDAR
                                       points and breaklines without significant further editing.

8        TERRAIN MODELING SUPPLEMENTS:
      8.01   Road Features: Both sides of paved road features, not including bridges and
            overpasses, shall be captured as edge-of-pavement breaklines. These features will
            be captured as three-dimensional breaklines.
      8.02 Soft Features: In areas where the LiDAR mass points are not sufficient to create a
            hydrologically correct DTM, soft features such as ridges, valleys, top of banks, etc.,
            shall be captured as soft breaklines of varying elevations. These features will be
            captured as three-dimensional breaklines. Soft features may also include
            embankments.
      8.03 Low Confidence Areas: Low Confidence Areas are defined as vegetated areas that
            are considered obscured to the extent that adequate vertical data cannot be clearly
            determined to accurately define the DTM. These features shall be captured as two-
            dimensional closed polygon features. These features are for reference information
            indicating areas where the vertical data may not meet the data accuracy requirements
            due to heavy vegetation.
      8.04 Overpasses and Bridges: Overpass and bridge features will be captured as three-
            dimensional breaklines; the breaklines will use the elevation of the edge of the
            driving surface as the z coordinate (rather than elevation of guard rails or other
            bridge surfaces). These breaklines will be segregated in some way from other
            breakline types.
      8.05 Depressions (sinks), natural or man-made, are not to be filled (as in hydro-
            conditioning and hydro-enforcement).
      8.06   Water Bodies (ponds and lakes), wide streams and rivers (“double-line”), and other
            non-tidal water bodies as defined in Section 6 are to be hydro-flattened within the
            DEM. Hydro-flattening shall be applied to all water impoundments, natural or man-
            made, that are larger than ~2 acre in area (equivalent to a round pond ~350’ in
            diameter), to all streams that are nominally wider than 100’, and to all non-tidal
            boundary waters bordering the project area regardless of size. The methodology
            used for hydro-flattening is at the discretion of the data producer.
                       Note: Please refer to Section 6 and Appendix B for detailed discussions of
                       hydro-flattening.
9       DELIVERABLES: The Client shall have unrestricted rights to all delivered data and
        reports, which will be placed in the public domain. This specification places no
        restrictions on the data provider's rights to resell data or derivative products. This
                                                                                       Page 52 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       Standard does not supersede any requirements imposed by State or Federal statute or
       regulation as to distribution such as the NC Public Records Law (NC GS 132).
       Deliverables are to be forwarded to the Q/C team as they are completed.
    9.01 Surveyors Certification: All products prepared under the supervision of a North
            Carolina Professional Land Surveyor shall be accompanied with a report which will
            be certified and sealed by the surveyor in responsible charge in accordance with
            State Law and NC Board of Registration Administrative Code (See section 1.04).
    9.02 Collection Report detailing mission planning and flight logs.
    9.03 Survey Report detailing the collection of control and reference points used for
            calibration and QA/QC.
    9.04 Processing Report detailing calibration, classification, and product generation
            procedures including methodology used for breakline collection and hydro-
            flattening (see Section 6 and Appendix B for more information on hydro-flattening).
    9.05 Quality Assurance /Quality Control (QA/QC) Reports detailing the analysis,
            accuracy assessment and validation of:
         9.05.1 The point data (absolute, within swath, and between swath)
         9.05.2 The bare-earth surface (absolute)
         9.05.3 Other optional deliverables as appropriate
    9.06 Control and Calibration points: All control and reference points used to calibrate,
            control, process, and validate the LiDAR point data or any derivative products are to
            be delivered (See 4.03).
    9.07 Daily Calibration Report (See 4.03)
    9.08 Flight Plan Map (See 4.04)
    9.09 Geo-referenced, digital spatial representation of the precise extents of each
            delivered dataset. This should reflect the extents of the actual LiDAR source or
            derived product data, exclusive of Triangular Irregular Network (TIN) artifacts or
            raster NODATA areas. A union of tile boundaries or minimum bounding rectangle
            is not acceptable. ESRI Polygon shapefile or geodatabase is preferred.
    9.10 Metadata will be attached to all appropriate deliverables; said metadata will be in
            FGDC-compliant metadata files.
         9.10.1 Product metadata (FGDC compliant, XML format metadata). One file for
                  each:
                      • Project
                      • Lift
                      • Tiled deliverable product group (classified point data, bare-earth DEMs,
                          breaklines, etc.). Metadata files for individual tiles are not required.
         9.10.2 FGDC compliant metadata must pass the USGS metadata parser (“mp”) with
                  no errors or warnings.
    9.11 Raw Point Cloud

                                                                                      Page 53 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                     Note: delivery of the Raw Point Cloud should be discussed by the
                     contracting officer, arrangements should be made for storage, retrieval,
                     and archiving of the “Raw Data Deliverable” if said data is to be held by
                     a party other than the Client. This is a very large data set that is not
                     readily usable by an end user.
        9.11.1 All returns, all collected points, fully calibrated and adjusted to ground, by
                swath shall be in fully compliant LAS v1.2 or v1.3, or current ASPRS LAS
                format standard. Point Record Format 1, 3, 4, or 5, (a newer LAS equivalent
                Point Record format may be substituted) .and shall include the following
                requirements if applicable. The Contracting Officer has final determination of
                LAS format to be used.
        9.11.2 LAS v1.3 or current ASPRS LAS format standard deliverables with waveform
                data are to use external “auxiliary” files with the extension “.wdp” for the
                storage of waveform packet data. See the LAS v1.3 or current ASPRS LAS
                specification for additional information.
        9.11.3 Georeference information is to be included in all LAS file headers.
        9.11.4 GPS times are to be recorded as Adjusted GPS Time, at a precision sufficient to
                allow unique timestamps for each pulse.
        9.11.5 Intensity values (native radiometric resolution) are to be included.
        9.11.6 Requirements are one file per swath, one swath per file, and file size not to
                exceed 2GB, as described in 6.14.6.
    9.12 Classified Point Cloud
                     Note: Delivery of a classified point cloud is a standard requirement for
                     North Carolina LiDAR projects. Specific scientific research projects may
                     be exempted from this requirement.
        9.12.1 Fully compliant LAS v1.2 or v1.3, Point Record Format 1, 3, 4, or 5, (a newer
                LAS equivalent Point Record format may be substituted)and shall include the
                following requirements if applicable.
             9.12.1.1 LAS v1.3 deliverables with waveform data are to use external
                        “auxiliary” files with the extension “.wdp” for the storage of waveform
                        packet data. See the LAS v1.3 Specification for additional information.
             9.12.1.2 Georeference information is to be included in LAS header.
             9.12.1.3 GPS times are to be recorded as Adjusted GPS Time, at a precision
                        sufficient to allow unique timestamps for each pulse.
             9.12.1.4 Intensity values (native radiometric resolution) are to be included.
             9.12.1.5 Tiled delivery, without overlap (tiling scheme TBD), is to be included.
             9.12.1.6 Classification Scheme (minimum) as follows:

                             Code           Description

                                                                                   Page 54 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                               1                Processed, but unclassified
                               2                Bare-earth ground
                               7                Noise (low or high, manually identified, if
                                                needed)
                               8                Model Key Point (masspoint)
                               9                Water
                               10               Ignored Ground (Breakline Proximity)
                               11               Withheld (if the “Withheld” bit is not
                                                implemented in processing software)

                        Note: Class 7, Noise, is included as an adjunct to the “Withheld” bit. All
                        “noise points” are to be identified using one of these two methods.

                        Note: Class 10, Ignored Ground, is for points previously classified as
                        bare-earth but whose proximity to a subsequently added breakline
                        requires that it be excluded during Digital Elevation Model (DEM)
                        generation.

    9.13       Bare Earth Surface (Raster DEM), and shall include the following requirements
              if applicable.
                         Note: Delivery of a bare-earth DEM is a standard requirement for LiDAR
                         projects. Specific scientific research projects may be exempted from this
                         requirement.
           9.13.1 Cell Size will be no greater than 3 meters or 10 feet, and no less than the design
                    Nominal Pulse Spacing (NPS).
           9.13.2 Delivery will be in an industry-standard, GIS-compatible, 32-bit floating point
                    raster format (ERDAS .IMG preferred).
           9.13.3 Georeference Information shall be included in each raster file.
           9.13.4 Tiled Delivery, without overlap, is required.
                 9.13.4.1 Each tile will include industry standard header information.
           9.13.5 DEM Tiles will show no edge artifacts or mismatch. A quilted appearance in
                    the overall project DEM surface, whether caused by differences in processing
                    quality or character between tiles, swaths, lifts, or other non-natural divisions,
                    will be cause for rejection of the entire DEM deliverable.
           9.13.6 Void Areas (i.e., areas outside the project boundary but within the tiling
                    scheme) shall be coded using a unique “NODATA” value. This value shall be
                    identified in the appropriate location within the file header.
           9.13.7 Vertical Accuracy of the bare earth surface will be assessed and reported in
                                                                                          Page 55 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

                 accordance with the guidelines developed by the NDEP and subsequently
                 adopted by the ASPRS. The complete guidelines may be found in Section 1.5
                 of the Guidelines document. See:
                 http://www.ndep.gov/NDEP_Elevation_Guidelines_Ver1_10May2004.pdf

               9.13.7.1 Vertical accuracy requirements using the NDEP/ASPRS methodology
                         are:
                    9.13.7.1.1 FVA <= 24.5cm ACCz, 95% (12.5cm RMSEz) (see section
                               1.03.5.2.4 for RMSEz definition)
                    9.13.7.1.2 CVA <= 36.3cm, 95th Percentile
                    9.13.7.1.3 SVA <= 36.3cm, 95th Percentile

              9.13.7.2 All QA/QC analysis materials and results are to be delivered to the
                          Client.
     9.14 Breaklines
                      Note: Delivery of the breaklines used in hydro-flattening is a standard
                      requirement. Specific scientific research projects may be exempted from
                      this requirement. If hydro-flattening is achieved through other means, this
                      section may not apply.
         9.14.1 All breaklines developed for use in hydro-flattening shall be delivered as an
                 ESRI feature class (PolylineZ or PolygonZ format, as appropriate to the type of
                 feature represented and the methodology used by the data producer). Shapefile
                 or geodatabase file formats are preferred.
         9.14.2 Each feature class or shapefile will include properly formatted and accurate
                 georeference information in the standard location. All shapefiles must include
                 the companion .prj file (projection).
         9.14.3 Breaklines must use the same coordinate reference system (horizontal and
                 vertical) and units as the LiDAR point delivery.
         9.14.4 Breakline delivery may be as a continuous layer or in tiles, at the discretion of
                 the data producer. Tiled deliveries must edge-match seamlessly, both
                 horizontally and vertically.

10     COMMON DATA UPGRADES
     10.01 Independent 3rd-Party QA/QC by another AE Contractor (encouraged)
     10.02 Higher Nominal Pulse Spacing (point density)
     10.03 Increased Vertical Accuracy
     10.04 Full Waveform collection and delivery
     10.05 Additional Environmental Constraints
             10.05.1.1 Tidal coordination, flood stages, crop/plant growth cycles, etc.

                                                                                     Page 56 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              10.05.1.2 Shorelines corrected for tidal variations within a collection
     10.06 Top-of Canopy (First-Return) Raster Surface (tiled). Raster representing the highest
           return within each cell is preferred.
     10.07 Intensity Images (8-bit gray scale, tiled)
     10.08 Detailed Classification (additional classes):

                               Code           Description

                               3              Low vegetation

                               4              Medium vegetation (use for single vegetation class)

                               5              High vegetation

                               6              Buildings, bridges, other man-made structures

                               n              additional Class(es) as agreed upon in advance

     10.09 Hydro-Enforced and/or Hydro-Conditioned DEMs
     10.10 Breaklines (PolylineZ and PolygonZ) for single-line hydrographic features (narrow
           streams not collected as double-line, culverts, etc.), including appropriate integration
           into delivered DEMs.
     10.11 Breaklines (PolylineZ and PolygonZ) for other features (TBD), including
           appropriate integration into delivered DEMs.
     10.12 Extracted Buildings (PolygonZ): Footprints with maximum elevation and/or height
           above ground as an attribute.
     10.13 Other products as defined by requirements and agreed upon in advance of funding
           commitment.

11     DERIVED PRODUCTS
     11.01 Digital Terrain Models
     11.02 Triangulated Irregular Network (TIN). A TIN is usable for small areas but
           quickly becomes unmanageable for larger areas. A Terrain Feature Class may be a
           better choice if the site is larger than ±150 acres.
     11.03 Hillshade Model
     11.04 Contours shall be certified to meet or exceed National Map Accuracy Standards.
           Contours within low confidence areas shall be attributed as such and are not
           required to meet National Map Accuracy Standards. Contours must be delivered in
           the ArcGIS geodatabase or shapefiles format with separate feature classes for 1- and
           2-foot contours. The feature classes will contain an elevation field and a contour

                                                                                       Page 57 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

            type field with the specified domain. While contours should be moderately
            aesthetically pleasing to the layperson, this deliverable is not intended to develop
            high-quality cartographic contours. However, an acceptable level of smoothing
            should be established and approved and be consistent across all deliverables.

            Note: Relationship between National Standard for Spatial Data Accuracy (NSSDA)
            and National Map Accuracy Standard (NMAS) (vertical) NMAS (U.S. Bureau of the
            Budget, 1947) specifies the maximum allowable vertical tolerance to be one half the
            contour interval, at all contour intervals. If vertical error is normally distributed,
            the factor 1.6449 is applied to compute vertical accuracy at the 90% confidence
            level (Greenwalt and Schultz, 1968). Therefore, the Vertical Map Accuracy
            Standard (VMAS) based on NMAS is estimated by the following formula:

            VMAS = 1.6449 * RMSEz

            The VMAS can be converted to Accuracyz, accuracy reported according to the
            NSSDA using equations from Appendix 3-A, Section 2:

            Accuracyz = 1.9600/1.6449 * VMAS = 1.1916 * VMAS.

           Therefore, vertical accuracy reported according to the NSSDA is (1.1916)/2 * CI =
           0.5958 * CI, where CI is the contour interval.
         11.04.1    The contour domain contains the following eight values:

              1. Intermediate
              2. Supplementary
              3. Depression
              4. Index
              5. Intermediate Obscured
              6. Supplementary Obscured
              7. Depression Obscured
              8. Index Obscured

         Index contours are defined below and will take precedence over the depression
         classification. Supplementary contours are only required for the Contour_2FT feature
         class and are not required for the Contour_1FT feature class. The contour type
         definitions listed below reference the USGS Digital Line Graph Standards (Part 7:
         Hypsography). http://rockyweb.cr.usgs.gov/nmpstds/dlgstds.html

                                                                                        Page 58 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

               11.04.1.1 Intermediate contours (the three or four lines between adjacent index
                         contours) are about half the line weight of index contours. They are
                         normally continuous throughout a map, but may be dropped or joined
                         with an index contour where the slope is steep and where there is
                         insufficient space to show all of the intermediate lines.

               11.04.1.2 Supplementary contours are used to portray important relief features
                         that would otherwise not be shown by the index and intermediate
                         contours (basic contours). They are normally added only in areas of
                         low relief, but they may also be used in rugged terrain to emphasize
                         features. Supplementary contours are shown as screened lines so that
                         they are distinguishable from the basic contours, yet not unduly
                         prominent on the published map.

               11.04.1.3 Depression contours are closed contours that surround a basin or sink.
                         They are shown by right-angle ticks placed on the contour lines,
                         pointed inward (down slope).

               11.04.1.4 Fill contours are a special type of depression contours, used to indicate
                         an area that has been filled to support a road or railway grade.

                                                                th
               11.04.1.5 Index contours are defined as every 5 contour line. For example,
                         with the Contour_2FT feature class, the first positive index contour
                         would be 0 with the following index contours at 10, 20, and 30 feet,
                         etc.

12     PRODUCT LIMITATIONS

     12.01 Points Designated as Bare Earth should be reviewed with some skepticism in area
           of dense vegetation. These points could be more appropriately called last return
           because they are bare earth only if the pulse actually reaches the bare earth. In thick
           grass, brush, or dense leaf clutter the elevation will probably be above the actual
           ground elevation. Look for and pay attention to low confidence area designations.
     12.02 DEM, DTM, and TIN: While LiDAR produces a very dense data set, the
           placement of points is random and not done intelligently. The terrain model will
           have some inconsistencies that would not typically be found in a terrain model
           generated from human, interactive techniques. This is due to points being chosen
           along terrain breaks rather than randomly near a terrain break. If precise data is
           required, dense post spacing is required or some supplemental ground or
           photogrammetric surveying can be included. DEM’s tend to mask micro topography
                                                                                      Page 59 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

           within the cell boundaries. Depending on the use of the DEM this could produce
           some problems. For example, in orthophotography production, too large a cell in
           steep terrain can produce some wavering in linear features such as rail road tracks.
     12.03 Contours at any interval can be generated from a digital terrain model but the
           reliability of the contours rapidly breaks down as the contour interval exceeds
           accuracy for the data set or for contours within low confidence areas. United States
           National Map Accuracy Standards, Vertical Accuracy, as applied to contour maps
           on all publication scales, shall be such that not more than 10 percent of the
           elevations tested shall be in error by more than one-half the contour interval. In
           checking elevations taken from the map, the apparent vertical error may be
           decreased by assuming a horizontal displacement within the permissible horizontal
           error for a map of that scale.
     12.04 Water and Asphalt Areas tend to absorb some of the LiDAR signal giving an
           elevation below the surface.

13     APPENDICES

       Appendix A - Request for Qualifications (RFQ), Example:

       REQUEST FOR QUALIFICATIONS

       1. General: _________________, herein after known as the Organization in this
       document, hereby request your written proposal for a contractual commitment to a digital
       LiDAR all return elevation mapping project. The project is to be divided into five phases
       (as shown in Section 2), and the response to the Request for Qualifications (RFQ). The
       primary deliverable for LIDAR Points , Waveform data and intensity horizontal data
       shall be North Carolina State Plane Coordinates, North American Datum (NAD) 1983
       (NSRS 2007). Vertical data will be in NAVD 88. All data will be based on US Survey
       Foot unless otherwise approved and noted.

       2. Scope of Project: This project will be divided into separate phases for the purposes of
       planning and funding; however, work may be done in several phases simultaneously.

              A. All Return LiDAR (collection phase): LiDAR collection phase including pre-
              paneling for Project areas is required. Data Collection shall include all return
              point cloud data, intensity data, and waveform data. All LiDAR is to be flown
              according to the Technical Specifications for LiDAR Data, ________________,
              North Carolina Department of the Secretary of State, Land Records Management
              Division, here after known as State Standard). The contractor must identify the
              LiDAR sensor by make, model and serial number to be used along with the
              specifications and certifications for the sensor per the State Standard. Data
              collection shall include reduction of the raw LiDAR information into LiDAR

                                                                                      Page 60 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              point data records including the combined information from GPS, IMU and laser
              pulse range data to produce X, Y, and Z point data.

              B. Ground Control: The Contractor is to review the attached contract map to
              determine what horizontal / vertical control is required. North Carolina Geodetic
              Survey can provide information on existing government control monuments. If
              additional control is required, the Contractor is to indicate the location of the
              necessary additional control and describe how that control is to be established.
              The Contractor is to indicate on a proposed flight line map all of the control
              points planned for establishment or used to control this project. Previously flown
              LiDAR may be used in the preliminary check process by the contractor, but it is
              an unacceptable form of control.

              C. All Return LiDAR point cloud (processing phase): The American Society of
              Photogrammetry and Remote Sensing (ASPRS) LAS Specification v 1.2, v 1.3 or
              later shall be used to process and store the point cloud into its respective
              designations.

              D. All Return Waveform data (processing phase)(optional): The American
              Society of Photogrammetry and Remote Sensing (ASPRS) LAS Specification
              version 1.3 or later shall be used to process and store the wave form data into its
              respective format.

              E. All Return Intensity data (processing phase): The American Society of
              Photogrammetry and Remote Sensing (ASPRS) LAS Specification v1.2 , v 1.3 or
              later shall be used to process and store the intensity data into its respective format.

              F. Production of LiDAR Base Maps: Point cloud data and Intensity data shall be
              geo-segregated into the North Carolina paneling scheme. The LiDAR data is to be
              based on North Carolina NAD83 (NSRS 2007) US survey foot. A Map Inventory
              by Panel is attached as Appendix A. Map panels shall be named using the “North
              Carolina Land Records Management Program Naming convention for Geospatial
              data presented in the North Carolina Grid Panel Scheme”

              G. Deliverable Product Specifications
              Two sets of digital LiDAR Data will be delivered on DVD’s, on a portable hard-
              drive, or other portable media to the county for their contract area. All point data
              will be in ASPRS LAS v1.2, v 1.3 or later. Additional information will be
              included in accordance with State Standards and in a format approved by the
              contracting officer. DVD’s and DVD containers will be labeled in accordance
              with State Standards.

              In addition to the LiDAR data, any Derived Products that are specified in this
              proposal shall be included in the appropriate file format labeled with the same file
              name/number as the corresponding LiDAR.

                                                                                         Page 61 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

              Metadata records, Metadata detailing the characteristics and quality of submitted
              point cloud data must be provided, including the version of this standard which the
              dataset uses. Metadata should make every effort to meet the more rigorous standards
              set forth in the Federal Metadata Content Standard, where feasible. Metadata must
              provide sufficient information to allow the user to determine if that data will meet the
              intended purpose, as well as telling the user how to access the data. Metadata must
              provide a process description summarizing collection parameters (flying height above
              ground, IMU type, ground GPS procedures, target spot spacing, kilohertz setting, and
              percent overlap) as well as process description highlighting steps toward delivered
              point cloud. Examples of metadata records may be found at
              http://floodmaps.nc.gov/fmis/Download.aspx (LiDAR Metadata).

              The organization also requires a copy of the flight report, a list of existing
              monuments used for control, descriptions and data sheets for new control points
              established (it is recommended that these points be published in OPUS Data Base
              (http://beta.ngs.noaa.gov/OPUS/), and a signed and sealed surveyors report from
              the North Carolina Professional Land Surveyor (PLS) in responsible charge.

              H. Ownership of Materials
              All materials produced as a result of this project including but not limited to LAS
              point data, bare earth data set, intensity data, control points, terrain and elevation
              models shall become property of the Organization. The Organization may request
              that the Contractor store these materials at the Contractor’s facility at no charge;
              however, any and all materials shall be returned to the Organization upon written
              request.

       3. Organization Contract Map: A copy of the Organization Contract Maps are attached
       as Appendix A and will become a part of the final contract. These contract maps depict
       the boundaries of the maps to be delivered and the panel layout and panel size to be used.

       4. Desired Timetable:
       A. LiDAR Data collection covering the County will be flown and completed prior to dd,
       mm, yyyy. New and existing horizontal and vertical ground control shall be established
       prior to or during LiDAR collection. Exporting of the raw data from the airplane
       collection system is considered part of collection.

       B. Processing the raw data into the ASPRS LAS format is to begin as soon as the
       additional horizontal ground control (if required) has been established and approved by
       the Contracting Officers.

       C. All LiDAR base maps are to be completed and delivered to the Organization by dd,
       mm, yyyy. The project is not considered complete until all reports and deliverables have
       been review and accepted the contracting officer.

       5. Conformance to Specifications: All work performed by the Contractor under any
       agreement resulting from selection for this project shall be in strict conformance with the
                                                                                         Page 62 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       State Standards attached to this RFQ unless otherwise noted. Any modifications to the
       LiDAR specifications or other terms of the Agreement shall be permitted only upon
       written request by the Contractor, stating justifications thereof, and with written approval
       by the Organization. There will be visual quality control checks and ground- truthing
       done in accordance with State Standard.

       6. Technical Proposals: Outline of Proposal – The Contractor’s technical proposal
       should be organized so that the outline of the proposal generally follows the format of the
       State Standards. The proposal should cover the approach and the methods the Contractor
       intends to use in carrying out the project. The Contractor must indicate on a copy of the
       Organization’s Contract Map the control points that will be paneled and all flight lines to
       be flown, and include this map as part of the proposal.

       Responsibility for Proposal Costs - The vendor shall be responsible for all costs incurred
       in proposal preparation and submission.

       Bonding – A letter from a reputable bonding company verifying that the firm can be
       bonded for this project must be submitted with the proposal. A Performance Bond, a
       surety bond of 100 percent (100%) of the amount of the proposal, shall be required for
       the faithful performance of the contract and to indemnify the Organization against loss.
       The Contractor is to also furnish a payment bond to insure payment for all materials and
       subcontracting. The premiums are to be paid by the Contractor. The surety must be a
       substantial surety company satisfactory to the Organization, authorized by law to do
       business in the State of North Carolina and endorsed by a local representative of such
       surety company. All performance and payment bonds shall name ______________ as
       obligee. Certified proof that the bond has been issued by an approved bonding firm must
       be presented.

       Equipment – A list of all equipment that will be used in this project is to be included in
       the technical proposal.

       Binding – The Contractor shall be bound by its proposal for a term of ninety (90)
       calendar days from the due date of the proposals. A Contractor may withdraw a proposal
       by written request prior to the date and time of the proposal opening.

       Present Workload – The Contractor shall include in the technical proposal a complete
       tabulation of its currently held projects. Each such project shall be identified by name
       and be defined as to size, required period of performance, equipment and personnel
       assigned to that project as well as the completion deadline.

       7. Subcontracting: The Organization desire to contract with a firm that can perform all
       primary functions of the Digital LiDAR project. Subcontracting any portion of project is
       acceptable but must be indicated in the proposal. Personnel and work location of said
       personnel shall be disclosed.

                                                                                        Page 63 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       8. Qualifications: The Organization desires to contract with a firm that has experience
       performing LiDAR Collection, airborne GPS control and LiDAR Base mapping
       production with its own staff and equipment. The Contractor shall include in this
       proposal a description of at least two regional LiDAR projects that have been
       successfully completed with aircraft and equipment owned by the contractor and staff
       directly employed by the contractor. If the proposing firm is planning to use
       subcontractors in fulfilling any phase of this project, the subcontractor shall be identified
       by name, credentials must be clearly defined and any equipment utilized by said
       subcontractor must be indicated. All work location shall be disclosed for the contractor
       and subcontractors. Any production work that is proposed to be performed outside of the
       United States or its Territories shall require a waiver by the Contracting Official.

       A list of key staff members who are assigned to this project must be provided. The
       information shall include resume, professional credentials, certificates, licenses and level
       of qualifications that are necessary to perform this project. This includes the North
       Carolina Professional Surveyor that is designated to be in responsible charge of the
       project.

       9. Disqualifications: The Organization reserves the right to disqualify any company upon
       discovery by the Organization of any convincing evidence of collusion with intent to
       defraud or to commit any other illegal practices on the part of the company. Failure to
       comply with applicable state laws concerning insurance or bonding may also be grounds
       for disqualification. The Organization reserves the right to reject any and all proposals.

       10. Award of Contract: The award will be made to the Contractor who submits the
       proposal which is in the best interest of the organization. Such evaluations will include
       the relevant experience of the contractor, the capability of the contractor, the cost of the
       project and other factors deemed by the organization to be in the best interest of the
       organization. The organization reserves the right to reject any or all proposals at its sole
       discretion or to waive any specific irregularities or formalities in order to accept a
       proposal deemed to be in the best interest of the organization.

       11. Inquiries: Questions concerning this RFQ should be directed to:

       [Contact name and title, address, phone, fax, email

       All correspondence and questions should be in writing and all responses should be in
       writing. Any questions that the Organization feel are pertinent to all proposers will be
       mailed along with their corresponding answers as an addendum to the RFQ. Fax and
       email messages will be treated as written questions.

       12. Submission of Proposals: Final written proposals must be submitted to
       __________________________________. Proposals must be received no later than 4:00
       p.m. (local time) on ______________________. Two hard copies with original
       signatures and one PDF digital copy of the original must be submitted. Late proposals
       will not be considered.

                                                                                        Page 64 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       13. Save Harmless: The successful Contractor shall indemnify and save harmless the
       parties of the Organization from suits, actions, damages, and cost of every name and
       description resulting from work under this contract during its prosecution and suits
       brought against any parties of the Organization for or on account of the use of patented
       appliances, products, or processes, or the infringement of any patent, trademark,
       copyright, or alleged negligence on the part of the Contractor. At the time of contracting,
       the successful vendor must supply evidence of insurance to cover liability for mishaps of
       the vendor.

       14. Taxes:

       A. Federal Taxes –_________________ County, is exempt from Federal Excise Taxes
       and Transportation Taxes. The County will issue exemption certificates only upon
       request of the Contractor. The County will not guarantee any Federal Tax refunds to the
       Contractor.

       B. State Taxes –______________________ County is liable for North Carolina Sales and
       Use Taxes; however, this item shall not be shown on the proposal but shall be added to
       invoices as a separate item.

       15. Payment: Payment of the final invoice and retainage shall be made within 30 days
       after, in the judgment of the Organization’s representatives, the Contractor has
       completely delivered all materials or performed all services in accordance with the
       specifications and the terms of the contract. Payment will be allowed for work in
       progress. The Contractor must show that the portion of work included in the invoice is
       completed. A retainage of ten percent (10%) will be withheld from each invoice until all
       of the deliverable products are delivered to and formally accepted by the Organization as
       complete, satisfactory, and meeting all applicable specifications and standards. The
       contractor shall warrant the project from defects not meeting best management practices
       for one year.

       16. Liquidated Damages: The Organization and the Contractor shall mutually agree on
       incremental delivery dates for the deliverables prior to signing the final contract. This
       delivery schedule shall be included in the contract. Should the contractor fail to meet the
       delivery schedule of the contract, a liquidation damage of one hundred dollars per
       calendar day ($100.00/calendar day) will be imposed until delivery is made unless
       written authorization of extension is granted by all parties of the Organization. Request
       for extensions must be submitted in writing by the Contractor with full explanation as to
       reasoning for request of extension.

       17. Submission of Proposal: Proposals must be on the standard forms furnished by the
       Organization. The Technical Proposal is required. Proposals must be placed in a sealed
       envelope plainly marked to indicate its contents without being opened. All packages
       shall be clearly labeled on the outside with the following notice:

                                                                                       Page 65 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       “PROPOSAL FOR ____________________COUNTY DIGITAL LiDAR MAPPING”

       18. Signing Proposals: The Organization will prepare contracts for the successful
       Contractor using the name exactly as it appears in the proposal. Therefore, it is
       absolutely necessary that proposers sign the proposal using their correct and complete
       legal names.

       19. Other instructions:

       A. North Carolina law does not permit the award of contracts when proposals contain
       escalation clauses unless (1) the escalation clause incorporates a maximum figure for
       escalation, or (2) the escalation is computed at a fixed rate per period of time and the
       periods of time have a cut-off date so that there is a computable maximum escalation
       figure.

       B. The Organization shall have a period of thirty (30) days after the opening of the
       proposals in which to award the contract.

       C. The Organization expressly reserves the right to reject any or all proposals, to waive
       any informality or irregularities in the proposals received, and to accept the proposal
       which best serves the interests of the Organization (according to the judgment of the
       Organization).

       D. The award will be made to the Contractor who submits the proposal which is in the
       best interest of the Organization. Such evaluations will include the directly related
       experience of the Contractor, the capability of the Contractor, the cost of the project, time
       frame to complete the project and completeness of the proposed program as well as other
       factors deemed by the Organization to be in the best interest of the Organization.

       E. Proposals will be opened at 4:00 p.m. on ______________ by the
       __________________. Proposals received which are not in compliance with the above
       instructions will be considered to be non-responsive and will not be evaluated for
       possible award.

       20. Project Schedule

       A. RFQ sent to Contractors (__________________)

       B. Written Questions due by (_________________)

       C. Proposals due (____________________________)

       D. Contractor Interviews (if necessary) ( _______________________)

       E. Contractor Selection (_______________________________)

                                                                                        Page 66 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       F. Project Completion (_______________________________)

       Optional Items:

       Option # 1 -._______________________________________________________. See
       previous option maps for area size for entire project area and for individual county sizes.

       It is distinctly understood that the County Board of Commissioners reserves the right to
       reject any or all proposals.

       Alternate Proposal

       The Organization desires to obtain LiDAR data at the same scales, pixel resolutions and
       accuracies as described in the primary RFQ, but welcomes the opportunity to discuss
       methodology which may include different or innovative procedures and equipment. This
       proposal should include a step-by-step narrative of the methodologies and equipment to
       be utilized as well as the Contractor’s experience providing similar deliverables.

       Appendix B: HYDRO-FLATTENING REFERENCE
       The subject of modifications to LiDAR-based Digital Elevation Models (DEM) is
       somewhat new, and although authoritative references are available, there remains
       significant variation in the understanding of the topic across the industry. The following
       material was developed to provide a definitive reference on the subject only as it relates
       to the creation of DEMs intended to be integrated into the USGS National Elevation
       Dataset (NED). The information presented here is not meant to supplant other reference
       materials and it should not be considered authoritative beyond its intended scope.
       The term “hydro-flattening” is also new, coined for this document and to convey our
       specific needs. It is not, at this time, a known or accepted term across the industry. It is
       our hope that its use and acceptance will expand beyond the USGS with the assistance of
       other industry leaders.
       Hydro-flattening of DEMs is predominantly accomplished through the use of breaklines,
       and this method is considered standard. Although other techniques may exist to achieve
       similar results, this section assumes the use of breaklines. The USGS does not require
       the use of any specific technique.
       The Digital Elevation Model Technologies and Applications: The DEM Users Manual,
       2nd Edition (Maune et al., 2007) provides the following definitions related to the
       adjustment of DEM surfaces for hydrologic analyses:
       1. Hydrologically-Conditioned (Hydro-Conditioned) – Processing of a DEM or TIN
       so that the flow of water is continuous across the entire terrain surface, including the
       removal of all spurious sinks or pits. The only sinks that are retained are the real ones on
       the landscape. Whereas “hydrologically-enforced” is relevant to drainage features that are
                                                                                       Page 67 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       generally mapped, “hydrologically-conditioned” is relevant to the entire land surface and
       is done so that water flow is continuous across the surface, whether that flow is in a
       stream channel or not. The purpose for continuous flow is so that relationships/links
       among basins/catchments can be known for large areas. This term is specifically used
       when describing EDNA (see Chapter 4), the dataset of NED derivatives made
       specifically for hydrologic modeling purposes.

       2. Hydrologically-Enforced (Hydro-Enforced) – Processing of mapped water bodies
       so that lakes and reservoirs are level and so that streams flow downhill. For example, this
       process could create a DEM, TIN or topographic contour dataset with elevations removed
       from the tops of selected drainage structures (bridges and culverts) so as to depict the
       terrain under those structures. Hydro-enforcement enables hydrologic and hydraulic
       models to depict water flowing under these structures, rather than appearing in the
       computer model to be dammed by them because of road deck elevations higher than the
       water levels. Hydro-enforced TINs also utilize breaklines along shorelines and stream
       centerlines, for example, where these breaklines form the edges of TIN triangles along
       the alignment of drainage features. Shore breaklines for streams would be 3-D breaklines
       with elevations that decrease as the stream flows downstream; however, shore breaklines
       for lakes or reservoirs would have the same elevation for the entire shoreline if the water
       surface is known or assumed to be level throughout. See also the definition for
       “hydrologically-conditioned” which has a slightly different meaning.

        While these are important and useful modifications, they both result in surfaces that
       differ significantly from a traditional DEM. A “hydro-conditioned” surface has had its
       sinks filled and may have had its water bodies flattened. This is necessary for correct
       flow modeling within and across large drainage basins. “Hydro-enforcement” extends
       this conditioning by requiring water bodies be leveled and streams flattened with the
       appropriate downhill gradient, and also by cutting through road crossings over streams
       (culvert locations) to allow a continuous flow path for water within the drainage. Both
       treatments result in a surface on which water behaves as it physically does in the real
       world, and both are invaluable for specific types of hydraulic and hydrologic (H&H)
       modeling activities. Neither of these treatments is typical of a traditional DEM surface.
       A traditional DEM such as the National Elevation Dataset (NED), on the other hand,
       attempts to represent the ground surface more the way a bird, or person in an airplane,
       sees it. On this surface, natural depressions exist, and road fills create apparent sinks
       because the road fill and surface is depicted without regard to the culvert beneath.
       Bridges, it should be noted, are removed in most all types of DEMs because they are
       man-made, above-ground structures that have been added to the landscape.
       Note: DEMs developed solely for orthophoto production may include bridges, as their
       presence can prevent the “smearing” of structures and reduce the amount of post-
       production correction of the final orthophoto. These are “special use DEMs” and are
       not relevant to this discussion.
       For years, raster DEMs, have been created from a Digital Surface Model (DSM) of
       masspoints and breaklines, which in turn were created through photogrammetric

                                                                                        Page 68 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       compilation from stereo imagery. Photogrammetric DSMs inherently contain breaklines
       defining the edges of water bodies, coastlines, single-line streams, and double-line
       streams and rivers, as well as numerous other surface features.
       LiDAR technology, however, does not inherently collect the breaklines necessary to
       produce traditional DEMs. Breaklines have to be developed separately through a variety
       of techniques, and either used with the LiDAR points in the generation of the DEM, or
       applied as a correction to DEMs generated without breaklines.
       In order to maintain the consistent character of the NED as a traditional DEM, the USGS
       National Geospatial Program (NGP) requires that all DEMs delivered have their inland
       water bodies flattened. This does not imply that a complete network of topologically
       correct hydrologic breaklines be developed for every dataset; only those breaklines
       necessary to ensure that the conditions defined in Section 7 exist in the final DEM.
       USGS NGP LiDAR Guidelines and Base Specification Version 13 – ILMF 2010
       http://lidar.cr.usgs.gov/USGS-
       NGP%20Lidar%20Guidelines%20and%20Base%20Specification%20v13(ILMF).pdf

       Appendix C: Naming Convention for Geospatial Data Presented in the
       North Carolina Grid Panel Scheme see
       http://www.secretary.state.nc.us/land/ThePage.aspx and down load
       NC Base Mapping file naming convention.pdf

       Appendix D: Issue Papers http://www.ncfloodmaps.com/issue_papers.htm

       Appendix E : Quality Control of Light Detection and Ranging (LiDAR)
                Elevation Data in North Carolina (Background)

       Reference Appendix A, Guidance for Aerial Mapping and Surveying, of FEMA's
       Guidelines and Specifications for Flood Hazard Mapping Partners at
       www.fema.gov/mit/tsd/dl_cgs.htm, and the National Standard for Spatial Data Accuracy
       (NSSDA) which specifies that accuracy of geospatial data be reported in ground
       distances at the 95% confidence level. The requirements for digital elevation data for
       flood insurance studies should be determined early in the process. Typically, for
       hydraulic modeling, FEMA specifies that elevation data equivalent to 4' contours
       (RMSEz = 1.2 ft (37 cm); Accuracyz = 2.4 ft (72.5 cm) at 95% confidence level) are
       appropriate for rolling to hilly terrain, and elevation data equivalent to 2' contours
       (RMSEz = 0.6 ft (18.5 cm); Accuracyz = 1.2 ft (36.3 cm) at 95% confidence level) are
       appropriate for flat terrain. FEMA encourages its own Project Officers, as well as

                                                                                   Page 69 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       Cooperating Technical Partners and States, to establish practical accuracy requirements
       for digital elevation datasets consistent with technical requirements and funds available.

       For Phase I of the North Carolina Floodplain Mapping Program (NCFMP) initiated in
       2000, the state specified a vertical RMSE (RMSEz) of 20 cm for coastal counties and
       RMSEz of 25 cm for inland counties, computed after deletion of the worst 5% of the
       checkpoints. This is equivalent to vertical accuracies (Accuracyz) of 1.3 ft (39.2 cm) and
       1.6 ft (49.0 cm), respectively, at the 95% confidence level, except that all accuracy
       assessments for Phase I were based on the best 95% of the checkpoints rather than the
       entire population of checkpoints. In 2000, the state had no better way to accommodate
       the fact that up to 5% of the checkpoints might not follow a normal error distribution
       required for the RMSE process to be applicable. There were no published alternatives at
       the time, other than accepting the fact that, by utilizing 100% of the checkpoints, even a
       single outlier could totally skew the RMSE calculations and accuracy assessments
       derived there from. Since the majority of Phase I LiDAR datasets had error distributions
       that did not follow a normal distribution, this demonstrated the validity of not using
       RMSE calculations for all 100% of the checkpoints because this would have unduly
       skewed the accuracy statistics.

       In 2002, the National Digital Elevation Program (NDEP) established draft guidelines that
       specifically address LiDAR and the fact that the RMSE process is inappropriate for many
       land cover categories except for open terrain where there are no valid reasons why errors
       should not follow a normal error distribution. Version 1.0 of the final NDEP guidelines
       were published on May 10, 2004 (see
       http://www.ndep.gov/NDEP_Elevation_Guidelines_Ver1_10May2004.pdf) entitled:
       "Guidelines for Digital Elevation Data." The NDEP guidelines specify Fundamental
       Vertical Accuracy at the 95% confidence level, computed by multiplying the RMSEz by
       1.9600, for open terrain only; this establishes the fundamental accuracy of the LiDAR
       sensor in open terrain. Additionally, the NDEP establishes both Supplemental Vertical
       Accuracy for other individual land cover categories, and Consolidated Vertical Accuracy
       in all land cover categories combined, using the 95th percentile errors to determine
       vertical accuracy at the 95% confidence level. This allows 5% of the checkpoint errors to
       exceed the established standard for Accuracyz. The Supplemental Vertical Accuracy
       establishes the vertical accuracy in land cover categories, other than open terrain, where
       there may be legitimate reasons why errors do not follow a normal distribution; this
       determines how well the sensor performed, as well as the effectiveness of the post-
       processing used to establish "bare earth" elevations. The Consolidated Vertical Accuracy
       does the same for all combined land cover categories representative of the area being
       mapped.

       For Phase II of the NCFMP, the state has specified Fundamental Vertical Accuracy of 1.2
       ft (36.3 cm) in open terrain, and Consolidated Vertical Accuracy of 1.6 ft (49.0 cm) in all
       land cover categories combined, including open terrain, weeds and crops, scrub, forests,
       and urban terrain (built-up areas). The state has also specified horizontal (radial)
       accuracy (Accuracyr) of 5.68 ft (1.73 m) at the 95% confidence level, which is equivalent

                                                                                       Page 70 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       to a horizontal (radial) RMSE (RMSEr) of 3.28 ft (1 meter). These same specifications
       pertain to Phase III.

       Appendix F: Example of a LiDAR Metadata record

       See: http://www.oregongeology.org/sub/lidar/metadata/metadata-lidar.htm

       Appendix G: Daily Calibration Survey / Boresight Calibration

       What’s a boresight?
       • GPS antenna, IMU center of mass, and the LiDAR detector are all at physically
         different locations

       •   We do not really care what the position of the antenna or attitude of the IMU is –
           rather, we use these to calculate a precise offset to determine the exact location and
           orientation of the LiDAR detector

       •   Shock of landing and other environmental changes can shift the position of the
           instruments enough to upset data.

       •   This test is performed for each flight mission

       •   Removes systematic errors

              –   Flight-to-flight variations on instrument mounting

              –   Environmentally induced changes

       •   Performing a kinematic GPS survey on a roadway within the collection area is a
           reliable check

              –   Validate the vertical for a feature with first returns on an unobstructed surface

              –   Apply any vertical correction as necessary (a “z-bump”)

                                                                                        Page 71 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

 North
     h Carolin
             na Techn
                    nical Speccification
                                       ns for LiD
                                                DAR Basse Mappiing

       The Importan
       T           nce of daily Calibration
                                 C
   •   C
       Control pointts on a buildiing and otheer regularly shaped
                                                           s      surfaaces are acquuired

   •   R
       Results of callibration fligghts compareed to controll points to coorrect for:

           –   edge curl
                    c

           –   pitch

           –        g issues (GP
               timing          PS, IMU)

           –   other system biasees

   •   Iff the instrum
                     ment is not “ddialed-in” foor each missiion, data from
                                                                          m successivee lifts will not
       m
       match!!

                                                                                             Page 722 of 74
Adopted January 30, 2013 by Noorth Carolinaa Secretary of
                                                       o State Elainne F. Marshall

 North
     h Carolin
             na Techn
                    nical Speccification
                                       ns for LiD
                                                DAR Basse Mappiing

       Appendix H:
       A        H ASPRS Guideline
                                es, Vertica
                                          al Accuracy
                                                    y Reportin
                                                             ng for LiDA
                                                                       AR
       D
       Data,

       http://www.a
       h          asprs.org/a//society/com
                                         mmittees/lidaar/Downloaads/Verticall_Accuracy__Rep
       orting_for_L
                  Lidar_Data..pdf

       Appendix I:
       A          I Affirmattion of Verrtical Datu
                                                 um for Surrveying an
                                                                    nd Mappin
                                                                            ng
       A
       Activities

       F
       Federal                  5 No. 120 / Thursday. June 24, 19993 / Notices 34245
               Regiister / Vol. 58,

        Docket No. 930650-31550]
       [D

       A
       Affirmation of Vertical Datum for Surveying and
                                                   a Mappin
                                                          ng Activitiess

       SUBAGENC   CY: Nationall Ocean Servvice, Coast & Geodetic Survey.
                                                                 S       Natiional Oceanic
       annd Atmosph
                  heric Adminiistration, DO
                                          OC.

       A
       ACTION: Notice.

       SUMMARY      Y: This Noticce announcess a decision by the Federral Geodeticc Control
       Subcommitteee (FGCS) too affirm the North N      Ameriican Verticaal Datum of 1988
                                                                                        1      (NAVD   D
       88) as the offficial civiliann vertical dattum for survveying and mapping
                                                                         m          activvities in the
       U
       United   Statess performed or o financed byb the Federral Governm ment. and to the
                                                                                        t extent
       prracticable, leegally allow
                                  wable, and feaasible, require that all Feederal agenccies using or
       prroducing verrtical height informationn undertake an   a orderly trransition to NAVD
                                                                                        N         88.

                                                                                               Page 733 of 74
Adopted January 30, 2013 by Noorth Carolinaa Secretary of
                                                       o State Elainne F. Marshall

 North Carolina Technical Specifications for LiDAR Base Mapping

       FOR FURTHER INFORMATION CONTACT. Mr. James & Stem, N/CG1x4,
       SSMC3, Station 9357, National Geodetic Survey. NOAA, Silver Spring, Maryland
       20910; telephone: 301-713-3230.

       SUPPLEMENTARY INFORMATION The Coast and Geodetic Survey (C&GS),
       National Geodetic Survey (NGS), has completed the general adjustment portion of the
       NAVD 88 project, which includes approximately 80 percent of the previously published
       bench marks in the NGS data base. The remaining "posted" bench marks which comprise
       approximately 20 percent of the total will be published by October 1993. Regions of
       significant crustal motion will be analyzed and published as resources allow. NAVD 88
       supersedes the National Geodetic Vertical Datum of 1929 (NGVD 29) which was the
       former official height reference (vertical datum) for the United States. NAVD 88
       provides a modem, improved vertical datum for the United States, Canada, and Mexico.
       The NAVD 88 heights are the result of a mathematical least squares general adjustment
       of the vertical control portion of the National Geodetic Reference System and include
       80,000 km of now U.S. Leveling observations undertaken specifically for this project.
       NAVD 88 height information in paper or digital form is available from the National
       Geodetic Information Branch, N/CG174, SSMC3, Station 9202, National Geodetic
       Survey. NOAA, Silver Spring, Maryland, 20910; telephone: 301-713-3242.

       Dated: June 21, 1993.
       W. Stanley Wilson,
       Assistant Administrator for 0cean Services and Coastal Zone Management, NOAA.
       [FR Doc. 93-14922 Filed 6-23--93; 8:45 am)
       BILLING CODE 351

       Appendix J: USGS Lidar Base Specifications Version1.0 book 11
       collection and Delineation of Spatial Data
       The USGS NGP LiDAR specification has been published as a final report
       (http://pubs.er.usgs.gov/publication/tm11B3 )

       Heidemann, Hans Karl, 2012, Lidar base specification version 1.0: U.S.Geological
       Survey Techniques and Methods,
       book 11, chap. B4, 63 p.

       Appendix K: USGS National Enhanced Elevation Assessment
       Revised March 29, 2012
       Submitted By: Dewberry,
        8401 Arlington Boulevard
       Fairfax Virginia 22031-4666
       http://www.dewberry.com/files/pdf/NEEA_Final%20Report_Revised%203.29.12.pdf

                                                                                   Page 74 of 74
Adopted January 30, 2013 by North Carolina Secretary of State Elaine F. Marshall

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
