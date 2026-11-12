---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-gis-gnss-standards
title: Statewide Global Navigation Satellite System Data Collection and Documentation Standards
doc_type: standard
citation: 'NC GIS standard: Statewide Global Navigation Satellite System Data Collection and Documentation
  Standards'
authority_level: ''
issuing_body: Geographic Information Coordinating Council (published by NCDIT)
source_url: https://it.nc.gov/documents/files/statewide-global-navigation-satellite-system-gnss-data-collection-and-documentation/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 634182e28eea7e2d6e41d58dbba59b4e92db9d475f52bee8b6188ff50b8be008
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

# Statewide Global Navigation Satellite System Data Collection and Documentation Standards (NC GIS standard: Statewide Global Navigation Satellite System Data Collection and Documentation Standards)

## At a glance

The statewide standards for GNSS data collection and documentation (version 4, March 2014), by the Statewide Mapping Advisory Committee.

## Full text

             Geographic Information Coordinating Council
               Statewide Mapping Advisory Committee

                               Statewide
              Global Navigation Satellite System (GNSS)
             Data Collection and Documentation Standards

                              Version 4
                             March 2014

*
Formerly known as the “Statewide Global Positioning System (GPS) Data
Collection and Documentation Standards”

Table of Contents
1.       Executive summary.......................................................................................................... 4
2.       Position statement ............................................................................................................ 7
3.       Global Navigation Satellite System ............................................................................... 11
4.       Mapping-grade receiver levels ....................................................................................... 16
5.       Best practices for GNSS use .......................................................................................... 16
5.1.     Purchasing ...................................................................................................................... 16
5.2.     Using the most appropriate grade of receiver ................................................................ 16
5.3.     Capturing data ................................................................................................................ 18
5.3.1. Static mode..................................................................................................................... 18
5.3.2. Kinematic mode ............................................................................................................. 18
5.3.3. Elevation mask ............................................................................................................... 18
5.3.4. Datum ............................................................................................................................. 18
5.3.5. Ellipsoid ......................................................................................................................... 18
5.3.6. Satellites ......................................................................................................................... 18
5.3.7. Signal to Noise Ratio (SNR) .......................................................................................... 19
5.3.8. Positional Dilution of Precision (PDOP) ....................................................................... 19
5.4.     Mission planning............................................................................................................ 20
5.5.     Processing data............................................................................................................... 22
5.5.1. Processing data settings ................................................................................................. 22
5.5.1.1. Units ............................................................................................................................... 22
5.5.1.2. Coordinate system .......................................................................................................... 22
5.5.1.3. Vertical datum ................................................................................................................ 22
5.5.2. Timely post-processing of GNSS data ........................................................................... 22
5.5.3. Processing of GNSS data in real time ............................................................................ 29
5.5.3.1. North Carolina GNSS Real Time Network (RTN) ........................................................ 29
5.5.3.2. Nationwide Differential Global Positioning System (NDGPS)..................................... 30
5.5.3.3. Wide Area Augmentation System (WAAS) .................................................................. 33
5.6.     GNSS records retention and accessibility ...................................................................... 37
5.7.     Equipment and procedure testing................................................................................... 37
5.8.     Training and certification ............................................................................................... 38
5.9.     GNSS data documentation (metadata) ........................................................................... 38
5.9.1. Metadata: Receiver ........................................................................................................ 39
5.9.2. Metadata: Feature........................................................................................................... 42
6.       Alternatives to mapping with a mapping-grade GNSS receiver .................................... 45
7.       Summary ........................................................................................................................ 49
8.       References ...................................................................................................................... 51

                                                                                                                                               2

9.        Glossary ......................................................................................................................... 53
9.1.      Abbreviation and acronyms ........................................................................................... 53
9.2.      Definitions...................................................................................................................... 56
10.       GNSS resources ............................................................................................................. 59
10.1.     GNSS standards from governments and organizations ................................................. 59
10.1.1.   International ................................................................................................................... 59
10.1.2.   Federal............................................................................................................................ 60
10.1.3.   State................................................................................................................................ 61
10.1.4.   Organizations ................................................................................................................. 61
10.2.     GNSS information ......................................................................................................... 62
10.2.1.   Federal............................................................................................................................ 62
10.2.2.   State................................................................................................................................ 63
10.2.3.   Private ............................................................................................................................ 63
10.3.     Online GNSS-related magazines ................................................................................... 63
10.4.     Free mission planning software ..................................................................................... 64
10.5.     Commercial GNSS software .......................................................................................... 64
10.5.1.   Field computer software ................................................................................................ 64
10.5.2.   Desktop software ........................................................................................................... 65
10.6.     Government software ..................................................................................................... 65
10.7.     GPS/GNSS receivers ..................................................................................................... 66
10.7.1.   Sub-foot accuracy mapping-grade ................................................................................. 66
10.7.2.   Sub-meter (1 - 3 feet) accuracy mapping-grade ............................................................ 67
10.7.3.   Sub-5 meter (3 - 15 feet) accuracy mapping-grade ....................................................... 68

                                                                                                                                                3

1. Executive summary
Due to the increasing use of 1Global Navigation Satellite System (GNSS) receivers (which are
now available in a multitude of models having varying levels of accuracy, error correcting
ability, and data quality documenting potential) by North Carolina state government agencies to
produce maps or Geographic Information System (GIS) data sets, the Geographic Information
Coordinating Council (GICC) Statewide Mapping Advisory Committee (SMAC) has updated the
“Statewide Global Positioning System (GPS) Data Collection and Documentation Standards”
document to the more inclusive, more technically up to date “Global Navigation Satellite System
Data Collection and Documentation Standards” document.

GNSS is a generic name for satellite navigation systems that provide autonomous positioning
worldwide. GNSS includes:
   Global systems

    System                                        Country      URL
    Navigation Signal Timing and Ranging
                                                  U.S.A.       http://www.gps.gov/systems/gps/
    Global Positioning System (NAVSTAR GPS)
    GLObal NAvigation Satellite System                         http://www.glonass-
                                                  Russia
    (GLONASS)                                                  center.ru/en/GPS/
                                                               http://www.esa.int/Our_Activities/
                                                  European
    Galileo                                                    Navigation/The_future_-
                                                  Union
                                                               _Galileo/What_is_Galileo
    Bediou or Compass                             China        http://en.beidou.gov.cn/

   Regional systems

    System                                        Country      URL
    Indian Regional Navigation Satellite System                http://www.isro.org/satellites/irnss.a
                                                  India
    (IRNSS)                                                    spx
    Quasi-Zenith Satellite System(QZSS) or
                                                  Japan        http://www.qzs.jp/en/
    Michibiki

At the present time (March 2014), GPS and GLONASS are the only satellite-based positioning
and navigation systems that are fully operational.

1 A GNSS receiver is a receiver that has been manufactured to receive signals from at least GPS

 and GLONASS satellites and may or may not have been manufactured to receive signals from
 WAAS, Galileo, Bediou or Compass, IRNSS, and/or QZSS satellites. Thus, these standards
 will refer to satellite-based positioning, navigation, and timing receivers as GNSS receivers.

                                                                                                    4

Each state agency that collects locational data must understand that there may be other users of
the data (in the present and/or in the future) with even more stringent accuracy requirements than
their requirements. Therefore, each state government agency that collects locational data shall:
   Ensure that their locational data collecting personnel have a strong foundation in GNSS
   theory and have been trained in the proper use of GNSS equipment.
   Use either mapping-grade or survey-grade receivers in GNSS data collection efforts where
   horizontal accuracy ranging from five (5) meters to sub-centimeter is required or the data are
   being collected for authoritative purposes.
   For inventory (non-authoritative) type applications, a procedure described in Section 6 can be
   used to collect non-authoritative information with a non-professional grade receiver in lieu of
   using a mapping or survey-grade receiver. Such receivers can only be used when the
   procedure in Section 6 is strictly followed to ensure that the state standard for horizontal
   accuracy has been met. Non-professional grade receivers are not adequate for any state
   locational data collection for authoritative purposes. A non-professional grade receiver
   should not be used to collect vertical information that is used for any state authoritative
   application.
   Test their GNSS receivers for accuracy daily if geodetic horizontal control monuments are
   located at the place of work or near the project site. Testing should occur at a minimum
   immediately prior to and immediately following the conclusion of a project, and at a
   minimum monthly.
   Differentially correct GNSS data (Figure 1) using post-processing software or via a real time
   correction service.
   Archive the digital products representing all stages of the GNSS data collection and
   processing chain (e.g., uncorrected field files, base station files used for differential
   corrections, electronic data entry forms, corrected GNSS files, and final GIS datasets).
   Document all GNSS-derived GIS data products with appropriate forms of metadata.

These minimum GNSS data collection and data documentation standards will have five (5)
important effects:
   Agencies that collect GNSS data will know exactly what is required
   Each agency’s GNSS data will contain metadata
   Agencies that use state GNSS data will have confidence in the data’s quality
   The state will save money by eliminating the need to re-collect locational data
   The use of GNSS will become more prevalent in state government

                                                                                                 5

Figure 1. A graphical explanation of the importance of collecting and processing GNSS data according to these data
          collection and documentation standards.

                                                                                                                     6

2. Position statement
This document is an update to the minimum standards that were adopted in 1994, and revised in
1999 and 2006, to be used by all state agencies and their contractors using GNSS technology to
generate locational data. The demand for more accurate and precise locational data within North
Carolina state government will only increase with the continued automation of locational data
sets. GNSS will be the principal tool for collecting locational data used in systems, such as a
computer models or a GIS, for which horizontal geographic accuracy is critical. GNSS is an
important and cost-effective method for locating features too numerous or too dynamic to be
mapped by traditional methods. Therefore, GNSS mapping is being recommended by many
state and federal agencies as the locational data collection method of choice.

There are three segments to GNSS:
   Space segment:       The constellation of navigation satellites
   Control segment:     The worldwide network of satellite tracking stations
   User segment:        The people who use a GNSS receiver to collect locational data, navigate,
                        and/or collect time information (note: satellite navigation systems are based on
                        very accurate atomic clocks).

GNSS receivers or units fall into two categories: Non-professional and Professional. For the
purpose of these standards, the professional receivers discussed are used to produce mapping and
survey products. This document does not address standards for survey-grade, but is focused on
the use of professional mapping-grade receivers and non-professional grade receivers for non-
authoritative applications. The choice of a GNSS receiver depends upon the intended use and
the accuracy requirement of the GNSS locational data.
   Non-professional (previously referred to as “recreational-grade”) GNSS receivers are sold
   primarily for outdoor sports or recreational activities and have horizontal accuracy
   requirements that do not meet the state standard for GIS data. Non-professional receivers
   operate in autonomous point positioning mode without the GNSS-derived positions being
   differentially corrected in either real-time or post-processing. These GNSS receivers are the
   least accurate of all the grades.
   “Enhanced” recreational-grade GNSS receivers that have been equipped to operate in a
   differential GNSS (DGPS) mode could meet state standards if their output files documented
   which points were differentially corrected and the age of the real-time data on each
   differentially corrected point.
   Mapping-grade GNSS receivers have the capacity for higher accuracy (sub–foot to five-
   meter horizontal accuracy) and are designed to facilitate data collection for a GIS program.
   Mapping-grade GNSS units use differential correction for high accuracy.
   Survey-grade GNSS receivers also use differential correction for the highest accuracy and are
   used for surveying tasks that require very high accuracy (within 1 cm).

                                                                                                       7

This document does not address standards for survey-grade GNSS activities. Agencies involved
in locational data collection must decide whether or not their projects require survey-grade
accuracy (+/- 1-2 cm). Surveying activities are governed by strict standards beyond the scope of
this document. This document defines standards for on-ground field collection using GNSS. It
does not address aerial GNSS data collection or control. These standards apply to current GNSS
technology. Thus, these standards will require periodic review and possible revision as GNSS
technologies evolve.

There are five (5) main uses for GNSS today:
   Navigation:    Getting from one location to another
   Position:      Determining a basic position using precise locational data
   Tracking:      Monitoring the movement of people and things
   Mapping:       Attaching coordinates to features, attributes, and metadata
   Timing:        Providing precise timing

GNSS techniques are one of the primary tools for locating features on or above the earth's
surface. In North Carolina, government agencies, academic institutions, and private companies
are using GNSS to determine the location of a multitude of features, including:
   Points: Features such as pollutant discharges and water supply wells
   Lines:    Features such as roads and streams
   Areas: Features such as waste lagoons

Before GNSS, such features had to be located with surveying equipment, aerial photographs, or
satellite imagery. Now with GNSS, these features can be located by a single operator using
hand-held equipment. However, the accuracy of data collected using GNSS technology is highly
variable depending on field methods, type of equipment, and post-processing of the data.

                                                                                                8

When collecting location information for producing maps or GIS data sets, all state
government agencies must:
   Use professional-grade GNSS receivers
   Differentially correct the GNSS derived locational data
   Use the procedure outlined in Section 6 if a non-professional grade GNSS unit is used
   for data collection

Professional and non-professional GNSS units are designed and built for different purposes.
Professional units have been engineered and built to provide accurate location coordinates and
efficient collection of attribute information and metadata.

GIS users typically require horizontal accuracies within 5 meters or better for mapping features
so that data layers can be overlaid and spatial relationships determined. It is imperative that all
state agencies collect locational data with the knowledge that there may be other users of the data
in the future. Potential users, unknown to the original data collectors, may have accuracy
requirements exceeding those of the collecting agency.

Typically, GNSS does not capture vertical positions as accurately as horizontal positions. The
vertical accuracy from a GNSS observation is 2-3 times worse than the horizontal accuracy.
Mapping units should not be used to obtain elevation values for applications that require accurate
elevations of less than three (3) meters.

These minimum GNSS data collection and data documentation standards will have four
important effects:
1. Agencies collecting GNSS data will know exactly what is expected from their time and effort
   spent to collect and document the data with Federal Geographic Data Committee (FGDC)
   compliant metadata.
2. Local, state, and federal agencies using state-collected GNSS data can do so with confidence
   in its quality, because the data will be collected, corrected, and documented according to
   standardized procedures.
3. The state will save money by maximizing original locational data collection accuracy and
   documentation, which will eliminate the need for additional trips to previously located sites.
4. The use of GNSS for collecting locational data will become more prevalent in state
   government because GNSS technology, training, and data documentation will be more
   consistent and more readily accessible.

                                                                                                    9

The GICC supports the development and adoption of standards for the successful collection,
exchange, and use of locational data. GNSS data collection standards are necessary so that state
agencies and their contractors have minimum specifications for collecting GNSS data.
Contractors should be in compliance with North Carolina General Statute Chapter 89C
(Engineering and Land Surveying)
(http://www.ncleg.net/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_89C.html), when
applicable, with respect to the collection of GNSS data.

GNSS data documentation in the form of metadata is required in order to provide spatial data
users with specific information about the lineage of a spatial data set (e.g. source, quality, and
content). Adequate metadata is required for the appropriate, responsible, and defensible use of
any spatial data set. Consequently, the GICC has adopted the FGDC “Content Standards for
Digital Geospatial Metadata” (CSDGM) (http://www.fgdc.gov/metadata/csdgm).

                                                                                                 10

3. Global Navigation Satellite System
Global Navigation Satellite System (GNSS) is a generic name for satellite navigation systems
that provide autonomous positioning worldwide. GNSS includes:
   Global systems

    System                                        Country     URL
    Navigation Signal Timing and Ranging
                                                  U.S.A.      http://www.gps.gov/systems/gps/
    Global Positioning System (NAVSTAR GPS)
    GLObal NAvigation Satellite System                        http://www.glonass-
                                                  Russia
    (GLONASS)                                                 center.ru/en/GPS/
                                                              http://www.esa.int/Our_Activities/
                                                  European
    Galileo                                                   Navigation/The_future_-
                                                  Union
                                                              _Galileo/What_is_Galileo
    Bediou or Compass                             China       http://en.beidou.gov.cn/

   Regional systems

    System                                        Country     URL
    Indian Regional Navigation Satellite System               http://www.isro.org/satellites/irnss.a
                                                  India
    (IRNSS)                                                   spx
    Quasi-Zenith Satellite System(QZSS) or
                                                  Japan       http://www.qzs.jp/en/
    Michibiki

At the present time (March 2014), GPS and GLONASS are the only satellite-based positioning
and navigation systems that are fully operational.

Background on GPS
GPS, which is a satellite-based positioning, navigation, and timing system, is a $12 billion
project that was initiated by the U.S. Department of Defense (DoD) in the 1970s for military
purposes. Although DoD still manages the system, the use of GPS has spread to a wide range of
civilian and commercial applications. For more information, please peruse the following
resources on the Internet:
    GPS information resources: www.gps.gov
   GPS Information: http://www.gps.gov/systems/gps/
   How GPS Works: http://www.gps.gov/multimedia/poster/
   GPS Accuracy: http://www.gps.gov/systems/gps/performance/accuracy/

                                                                                                 11

The GPS system consists of the following three segments:
   Space: The constellation of 32 (as of December 19, 2013) NAVSTAR satellites that orbit
          the earth twice a day at an altitude of approximately 20,200 km (12,500 miles).
             Note:    Although the original design had 24 satellites, there may be more than 24
                      satellites in orbit at a given time due to the longer than expected lifespan
                      of some of the earlier satellites. At the time of this writing, 32 satellites
                      were in orbit.
   Control: The DoD operated ground stations, data links, and command and control facilities.
   Users:    GNSS users throughout the world on land, sea, and in the air.

The GPS satellites broadcast high-frequency radio signals, which contain satellite position and
precise time data, twenty-four hours a day to enable anyone with a GNSS receiver to determine
his/her 3-D position, velocity, and time. Each GPS satellite broadcasts two signals:
    L1 signal (1575.42 MHz) for Standard Positioning Service (SPS) users (i.e. civilians)
   L2 signal (1227.60 MHz) for Precise Positioning Service (PPS) users (i.e. the military)

The DoD has continually modernized the system with more advanced satellites as older satellites
become non-functional. Newer generation satellites are providing a third frequency (L5), a
civilian code on L2 (L2C), and a military code on all signals. Additional information on GPS
modernization can be found at the following URL:
    http://www.gps.gov/systems/gps/modernization/

The basis of GPS technology is precise information about time and position. To determine a
horizontal or vertical location on earth, signals from at least four (4) satellites are required.
Accurate and precise time is obtained through the use of atomic clocks, which are accurate to
within one (1) second every 70,000 years. GNSS receivers calculate the distance to each satellite
by measuring the time interval between the transmission and the reception of a satellite signal.
Once the distance measurements of at least four (4) satellites are known, the GNSS receiver uses
the process of trilateration to determine its position.

                                                                                                 12

GPS can be used worldwide, 24 hours a day, and in all types of weather. While positional
accuracy is very high, it does vary depending on the receiver, field techniques used, post-
processing of data, and the following inherent errors:

 Error               Description
                     Interference with the GPS radio signals as they pass through the charged particles in
 Atmospheric
                     the ionosphere and the water vapor in the troposphere.
 Ephemeris or
 satellite           Inconsistencies or uncertainties about a satellite’s exact position in orbit.
 position
                     Minute discrepancies in a satellite's atomic clock that translate into travel time
 Timing
                     measurement errors.
                     The GPS signal’s non-straight line path as it reflects off objects in the local
 Multipath           environment (e.g., trees, fences, and/or buildings) before it reaches a GNSS receiver,
                     which results in derived distant errors.
                     The satellite position geometry index for precision (Figure 2):
 Positional              Low PDOP (favorable configuration) where the GPS satellites are spread out
 Dilution of             across the sky (left image)
 Precision
 (PDOP) value             High PDOP (less favorable configuration) where the GPS satellites are bunched
                          together in the sky (right image)

                 Low PDOP (favorable)                                         High PDOP (less favorable)

                        GPS receiver                                                     GPS receiver

 Figure 2. A diagram showing the satellite position geometry index for precision, Positional Dilution of
           Precision (PDOP):
                 Low PDOP (favorable configuration) where the GPS satellites are spread out across the sky (left
                 image)
                 High PDOP (less favorable configuration) where the GPS satellites are bunched together in the
                 sky (right image)

             Note:   Previously, a PDOP value greater than or equal to 6 was considered as a “bad” or “poor”
                     configuration. In the past few years, technological and software improvements have made it
                     possible for certain GNSS receivers to extract useful positional information from a set of
                     GPS satellites with a considerably higher PDOP value, which may or may not involve an
                     extended observation period and/or using carrier signals. Nevertheless, a GNSS user must
                     not exceed the recommended settings for his/her receiver and software.

                                                                                                                   13

Each of the preceding inherent errors, except for multipath and high PDOP, can be eliminated or
significantly reduced through the use of Differential GPS (DGPS) techniques (Figure 1). DGPS
involves the use of a stationary receiver, referred to as a base station or a Continuously Operating
Reference Station (CORS) that continuously records satellite measurements at a fixed and known
location. Since the base station’s position is known, the errors in the signal to each satellite can
be determined by measuring the ranges to each satellite and comparing the measured ranges to
the calculated ranges from the known position of the base station. The difference between the
measured range and the calculated range is the differential correction for each satellite that is in
view from the base station’s GNSS antenna. This error correction factor information can be
either:
    Broadcasted by a radio transmitter or transmitted via the internet for real-time differential
    correcting by GNSS receivers equipped with a radio link or cell phone data link, respectively.
   Stored on an Internet server for post-processing (i.e. a GNSS user downloads the
   corresponding base station data after completing the GNSS data collection and does the
   differential correcting procedure on a computer)

In contrast, the roving receiver collects measurements (ranges) in the field at unknown locations:
   Real-time differential correcting: The roving GNSS receiver applies the broadcast or
   transmitted differential corrections to its GNSS range observations as they are collected in
   order to remove errors in the ranges and improve the accuracy.
   Post-processing differential correcting: The GNSS user transfers the stored GNSS range
   observations from the GNSS receiver to a computer, downloads the corresponding base
   station data via the Internet, and uses post-processing software to remove errors in the ranges
   and improve the accuracy
Note: In order for differential correction to work, whether in real-time or post-processing, the
      roving receiver needs to record its measured positions and the exact time that each
      measurement was made. This timing information is then used in the differential
      correction procedure to remove the positional error at each instant.

The North Carolina Geodetic Survey (NCGS) maintains the NC GNSS CORS Network. Due to
the fact that NCGS is continually adding new CORS, users are advised to view the current status
map on the “CORS and GNSS” web page at the following URL:
    http://geodeticsurvey.nc.gov/Pages/CORS-and-GNSS.aspx

                                                                                                   14

The quality of the GNSS receiver also has a significant impact on positional accuracy. Survey-
grade receivers are the most expensive and produce data of the highest precision and accuracy.
Mapping-grade receivers are mid-range in price and provide sufficient accuracy for most
locational and GIS applications.

Data obtained using non-professional-grade receivers, the least expensive type of receiver, is the
least accurate. Some non-professional-grade receivers have add-on modules that can be used for
real-time differential correction. Companion data-logging and post-processing software are now
available for a very limited number of the most high-end non-professional-grade GNSS
receivers. The horizontal accuracy of such “enhanced” non-professional-grade GNSS receivers
can in most instances meet the “within 5 meters 95% of the time” state standard.

Note: The specific type of enhanced non-professional unit shall have been tested and
      approved by NCGS before it can be used for state GIS data collection. The cost of
      the extra data-logging hardware and post-processing software required to bring the
      accuracy of data collected with a non-professional-grade GNSS unit up to mapping-grade
      standards begins to approach that of lower-end mapping-grade GNSS units. It is
      questionable whether this approach to acquiring GNSS equipment is a sound investment.

Without differential correction, the accuracy of any GNSS receiver, regardless of grade, will not
meet the accuracy requirements to support the development of locational information for
geographic information systems in North Carolina.

Using DGPS can result in much greater accuracy, as shown in Table 1. Vertical error is typically
two to three times higher than horizontal error.

Table 1: GNSS receiver types and horizontal accuracies with differential GPS

 Type of             Differential GPS       Real-time differential Differential GPS with
 receiver            capabilities           GPS                    post-processing
 Survey              Yes                     + 1 cm                   + 1 cm
 Mapping             Yes                     + 1-5 m                  + 1-5 m
 Enhanced non-
                     Note1                   Note2                    Some open source options.
 professional

Note1: Requires external hardware device or built in data collection capacity.
Note2: Requires external radio beacon or built-in capability to receive range corrections.

                                                                                               15

4. Mapping-grade receiver levels
Mapping-grade receiver levels:
   Sub-foot mapping-grade
   Sub-meter (1-3 feet) mapping-grade
   Sub-5 meter (3-15 feet) mapping-grade

Note:     Regardless of the mapping-grade receiver’s stated level of accuracy, the locational
          data must be differentially corrected either in real time [e.g. NC Real-Time Network
          (RTN), Nationwide DGPS (NDGPS), or another real time correction service] or after
          the data is collected by post-processing.

5. Best practices for GNSS use
The best practices for using GNSS technology include:
    Coordination of purchases with NCGS
    Using the most appropriate grade receiver
    Data collection
    Data processing
    Training
    Operator certification

5.1. Purchasing
State government agencies are encouraged to coordinate their purchases of GNSS technology
with NCGS. The NCGS staff are aware of the latest developments in the technology and the
relative specifications between product offerings of the various GNSS vendors.

5.2. Using the most appropriate grade of receiver
To select the most appropriate GNSS receiver grade, answer the questions in the GNSS receiver
selection decision tree (Figure 3).

Note: For those applications that require 5-10 m (15-30 ft) accuracy, an agency could use an
      enhanced recreational-grade receiver with either real-time differential correction or post
      processing. However, the positional data derived from such a GNSS receiver would not
      be suitable for any NC State government database or GIS.

                                                                                               16

Figure 3. A decision tree diagram on how to select the most appropriate GPS receiver grade for conducting a particular locational
          project/task.
                                                                                                                                17

5.3. Capturing data
5.3.1. Static mode
Receiver procedures vary between models. Thus, a GNSS user should follow the manufacturer’s
guidelines. In general, a guideline to follow for static point positioning is to collect data at one
(1) second intervals. The amount of data to be collected will vary with the type of receiver from
a minimum number of ten (10) readings to a maximum of about one hundred and eighty (180)
readings for very old GNSS units (e.g. GeoExplorer II series). These readings need to be
automatically stored in the receiver for later downloading onto a computer for post-processing or
the readings need to be differentially corrected in real time and then downloaded onto a
computer.

5.3.2. Kinematic mode
The recommended measurement interval for collecting data in a kinematic mode (i.e. while
moving) is dependent on the operator’s velocity, shape of the feature, and the receiver model.
Therefore, the user should follow the manufacturer’s guidelines. If data is being collected from a
fast moving platform such as an automobile, airplane, or train, the measurement interval shall not
exceed one (1) second. In contrast, if the user is collecting data while walking, the measurement
interval will vary depending on shape of the feature, the receiver model, and any blockages.
These readings need to be automatically stored in the receiver for later downloading onto a
computer for post-processing or the readings need to be differentially corrected in real time and
then downloaded onto a computer.

5.3.3. Elevation mask
Greater than fifteen (15) degrees (recommended for older units). Note: An elevation mask is the
setting to exclude signals from satellites below a certain angle from the horizon. Please refer to
your GNSS receiver’s manual for the mapping-grade or higher setting, because modern receivers
and processing software are designed to utilize satellite signals from satellites below fifteen (15)
degrees by filtering out poor signals.

5.3.4. Datum
NAD 83, the state legislated datum

5.3.5. Ellipsoid
Geodetic Reference System 1980 (GRS 80) ellipsoid

5.3.6. Satellites
Minimum of four (4) satellites

                                                                                                  18

5.3.7. Signal to Noise Ratio (SNR)
39 dBHz (recommended).
Please refer to your GNSS receiver’s manual for the mapping-grade or higher setting.

5.3.8. Positional Dilution of Precision (PDOP)
Less than six (6) (recommended for older units)
Please refer to your GNSS receiver’s manual for the mapping-grade or higher setting, because
modern receivers and their software are designed to utilize less favorable PDOP conditions.

The Positional Dilution of Precision (PDOP) is the satellite position geometry index for precision
referring to how close or far apart the satellites are from each other in the sky (Figure 2).

                                                                                               19

5.4. Mission planning
GNSS mission planning is an effective method for GNSS users to determine the optimal time to
perform field data collection. Two of the most important factors in obtaining the highest
accuracy in your GNSS data are having at least four (4) satellites in view at a sufficiently high
elevation above the horizon and having the lowest possible PDOP values. A low PDOP value
indicates an evenly spaced arrangement of satellites in the constellation above the survey site at
the time the data is to be collected. There are certain periods of the day in which the satellite
constellation is in a poor configuration for collecting data (i.e. high PDOP) and should be
avoided. Therefore, it is important to assess satellite availability before heading into the field to
collect GNSS data. Furthermore, these high PDOP conditions are exacerbated in mountainous
terrain, heavy forest cover, or urban canyon situations, because satellite signals would be
blocked. Therefore, a user planning to collect data under such conditions should conduct the
mission planning with a higher elevation mask (i.e. 20 or 25 degrees instead of the standard 15
degrees).

Trimble offers mission planning as a free online service with its Trimble GNSS Planning Online
(http://www.trimble.com/GNSSPlanningOnline/#/Settings). The company used to include
mission planning in its processing software, GPS Pathfinder Office
(http://www.trimble.com/mappingGIS/PathfinderOffice.aspx), as the QuickPlan module, but has
since removed that module. Although the company still provides a free stand-alone mission
planning program, Trimble Planning Software v2.9
(http://ww2.trimble.com/planningsoftware_ts.asp), the program is no longer listed on their GPS
Data Resources webpage (http://www.trimble.com/Support/GPD_Data_Resources.aspx) and the
company has not updated the program since August 2010.

Whether a user utilizes a stand-alone program, an integrated module, or an online service, the
mission planning software requires current (less than 2 weeks old) satellite orbit information,
which is broadcasted from each GPS satellite in a file called an almanac. The advantage of using
an online service is that the provider is responsible for using the most up-to-date almanac
available. Unfortunately, the Trimble GNSS Planning Online service does not post the date and
time of its current almanac file. However, this information can be obtained by visiting their GPS
Data Resources webpage (http://www.trimble.com/Support/GPD_Data_Resources.aspx) and
examining the file’s information on their ftp site:
    Latest Almanac Data
    Latest Almanac files for use with Trimble planning utilities
    GPS/GLONASS almanac in Trimble Planning file format
    (ftp://ftp.trimble.com/pub/eph/almanac.alm)

                                                                                                    20

The disadvantage of using a stand-alone program or an integrated module is that the user is
responsible for obtaining and using the most up-to-date almanac available. Fortunately, a current
almanac file can be easily obtained from the following resources:
   The U.S. Coast Guard Navigation Center (NAVCEN) GPS NANUS, ALMANACS, & OPS
   ADVISORIES webpage (http://www.navcen.uscg.gov/?pageName=gpsAlmanacs) offers
   almanacs in the following formats:
   o YUMA Almanac - .alm, .txt
   o SEM Almanac - .al3, .txt
   Note: Certain GNSS mission planning software may require almanac information in a specific
         format. Check your GNSS equipment manufacturer’s documentation for specific
         details.
   A mapping-grade or survey-grade GNSS receiver
   Note: A GNSS user should have his/her GNSS receiver track GPS satellites until the receiver
         has reported that an almanac file has been downloaded, which may take 15+ minutes,
         before transferring the receiver’s downloaded almanac file to a computer. In addition,
         the user should also verify the almanac file’s date in order to ensure that the file is
         current.
   A GNSS manufacturer’s GNSS data resources webpage, such as Trimble’s GPS Data
   Resources webpage (http://www.trimble.com/Support/GPD_Data_Resources.aspx)

The advantage of using the stand-alone program or the module was that the PDOP values
throughout a user’s data collection period could be exported in either a graph or a table format.
A graph was useful for quickly determining what parts of the day would have PDOP peaks.
Whereas, a table was useful for knowing exactly when these PDOP peaks would occur. In
contrast, the online version exports data only as graphs.

In contrast, the advantages of using the online version are as follows:
   It is convenient in not having to download and load an almanac.
   The site location can be determined by entering a street address into an Internet-based
   mapping service as well as the coordinates from a geodetic monument’s datasheet.
   It provides time-lapse maps (global maps down to the user’s site) of ionospheric total
   electron content (TEC) and scintillation (disruption).

                                                                                                    21

5.5. Processing data
5.5.1. Processing data settings
5.5.1.1. Units
Meters. North Carolina § 102-1.1.
(http://www.ncleg.net/EnactedLegislation/Statutes/PDF/ByChapter/Chapter_102.pdf) stipulates,
“All coordinates of the system are expressed in metres.” and then stipulates that, “The U.S.
Survey Foot, 1 meter = 39.37 inches or 3.2808333333 feet, shall be used as a conversion
factor.” for converting between feet and meters.

5.5.1.2. Coordinate system
North Carolina State Plane, the state legislated coordinate system
(http://www.ncleg.net/EnactedLegislation/Statutes/PDF/ByChapter/Chapter_102.pdf).

5.5.1.3. Vertical datum
North American Vertical Datum of 1988

5.5.2. Timely post-processing of GNSS data
GNSS data may be corrected by two methods:
   Real time corrections from either:
   o NC GNSS Real Time Network (RTN) (http://rtnweb.nc.gov/)
   o A satellite correction service provider, such as Omnistar (http://www.omnistar.com/) or
     StarFire
     (http://www.navcomtech.com/wps/dcom/navcom_en_US/technology/augmentation/starfi
     re/starfire.page?).
   o Nationwide Differential GPS (NDGPS)
     (http://www.navcen.uscg.gov/?pageName=ndgpsMain)
   Post-processing by downloading the GNSS field file(s) from your GNSS receiver to a
   computer, downloading GNSS base station files, and then using desktop software to perform
   the differential correction.

In order to post-process a GNSS field file, the processing software needs base station correction
files, which can be downloaded from the NC GNSS RTN Reference Data Shop using the
following directions
(http://geodeticsurvey.nc.gov/Documents/How_to_download_GNSS_base_station_data_from_th
e_NCRTN.pdf).
Note:    The NC GNSS RTN Reference Data Shop posts GNSS (GPS + GLONASS) base station files
         for only the previous three (3) months in order to conserve space on the server. Therefore, a
         spatial data user should post-process his/her field files on a daily or weekly basis.

                                                                                                   22

Base station files can also be obtained from the National Geodetic Survey (NGS) User Friendly
CORS site (UFCORS) (http://www.ngs.noaa.gov/UFCORS/) as a “GPS only” file (i.e., no
GLONASS data) or as a GNSS file. A spatial data user may access UFCORS directly
(http://www.ngs.noaa.gov/UFCORS/) or from within a frame of a desired CORS webpage [e.g.
ASHEBORO 2 (NCZO) (http://www.ngs.noaa.gov/cgi-cors/corsage.prl?site=NCZO]. Although
the UFCORS interface is identical whether it is accessed directly or within a frame of a CORS
webpage, this document will cover how to access it from within a frame of a desired CORS
webpage to emphasize the fact that UFCORS does not automatically select a spatial data user’s
desired station even if the user accessed UFCORS as a frame from within his/her desired
station’s CORS webpage.

Note: The UFCORS webpage posted the following dated notices:

   Updated: 2014-APR-08, Tuesday, 1414hEDT
   Augmented GPS (L2C and L5) and GLONASS is now available from 2007:208 [2007 JUL
   29] -present. No earlier data is available.

                                                                                          23

The UFCORS download webpage (http://www.ngs.noaa.gov/UFCORS/) can be accessed as frame within a desired station’s CORS webpage by
the following steps:
1. Visit the NCGS “CORS and GNSS” webpage (http://geodeticsurvey.nc.gov/Pages/CORS-and-GNSS.aspx):
    a. Observer that the network (Figure 4) has achieved not only statewide coverage at a dense 30-60 km spacing arrangement, but provides
         seamless coverage along the Tennessee and South Carolina borders due to a data sharing agreement with those two neighboring states.
    b. Click on the closest base station to your collection site [e.g. ASHEBORO 2 (NCZO)], which will direct you to the NGS CORS webpage
         for that station (e.g. http://www.ngs.noaa.gov/cgi-cors/corsage.prl?site=NCZO).

  Figure 4.   The status map of the NC Continuously Operating Reference Station (CORS) Network and the NC Real-Time Network (RTN),
              which is also known as the Real-Time Kinematic (RTK) Network, showing the location and capability of each CORS:
                 NC GNSS CORS site (i.e. can receive signals from both the U.S. and the Russian navigation satellites) in the RTN (i.e. can be
                 accessed in real-time via a data cell phone and accessed for post-processing via the Internet)
                 NC CORS site (i.e. can receive signals from only the U.S. navigation satellites) in the RTN
                 NC CORS site not in the RTN (i.e. cannot be accessed in real-time, but can be accessed for post-processing via the Internet)
                 NC GNSS CORS site that is being installed and will be incorporated into the RTN
                 South Carolina GNSS CORS site that is accessible via the NC RTN
                 Tennessee GNSS CORS site that is accessible via the NC RTN                                                                    24

2. From the NGS CORS webpage for your
   selected station [e.g. ASHEBORO 2 (NCZO)
   (http://www.ngs.noaa.gov/cgi-
   cors/corsage.prl?site=NCZO] (Figure 5),
   which shows vicinity photographs of that
                                                            Click
   station in a frame of that station’s webpage,
   a. Click on the “Custom Files (UFCORS)”
       link on the left side of the page, which
       will replace the photographs in the frame
       (identified with the orange dashed line      Figure 5. The NGS CORS webpage for
       rectangle) with the UFCORS webpage.                    ASHEBORO 2 (NCZO).
   b. Please observe that UFCORS opens with no station selected (Figure 6). In addition, the
       UFCORS download site is a context sensitive form in that it will only offer the option of
       downloading GNSS data if you select a station that has a GNSS receiver. Every CORS
       in the NCGS CORS Network utilizes a GNSS receiver. However, the following CORS
       in North Carolina utilize a “GPS only” receiver:
           PARI_OBS_NC-2008 (P779), which is operated by UNAVCO
           (http://www.unavco.org/aboutus/aboutus.html)
           GREENSBORO 5 (NCG5) and NEW BERN 6 (NBR6), which are operated by the
           U.S. Coast Guard (http://www.navcen.uscg.gov/)

                                                                         Observe that UFCORS does
                                                                         not know what station you
     Figure 6. The opening UFCORS                                        want even when accessed as
               dialog box as a frame within                              a frame within your selected
               the NGS CORS webpage for                                  station’s CORS webpage.
               ASHEBORO 2 (NCZO).

                                                                                                 25     25

c. Decide on which time zone you will utilize for referencing your data collection time
   period as either Coordinated Universal Time (UTC), which is basically Greenwich
   Mean Time (GMT), or the local time zone:
       Eastern Standard Time (EST), which is UTC - 5 or GMT – 5
       ~or~
       Eastern Daylight Time (EDT), which is UTC – 4 or GMT - 4
   Hint: The sooner that you can think in UTC in the 24-hour format, the better.
d. Answer the following questions
   about your GNSS data collection
   period (Figure 7) and then press
   the [Get CORS data file] button:
       Start Date:
       1). Place the cursor in the
           “Start Date” field to
           activate the pop-up
           calendar.
       2). Select your starting date
           and then press the [Done]
           button, which will fill-in
           the following fields:
           “Year” and “Day of
           Year” (i.e. Julian Day).
       Start Time:
       1). Place your cursor in the

          “Start Time” field to          Figure 7. The UFCORS dialog box completed to download
          activate the pop-up menu,                base station files from ASHEBORO 2 (NCZO).
          which offers the starting time hour in the 24-hour format from 0:00 hrs to 23:00
          hrs.
       2). Select the start time hour in the same time zone as what you will select for the
           “Time Zone” option.
                                                                  Continued on the next page.

                                                                                              26

d. Answer the following questions about your GNSS data collection period and then press
   the [Get CORS data file] button (continued from the previous page):
       Time Zone:
       1). Place your cursor in the “Time Zone” field to activate the pop-up menu, which
           offers time zones listed as UTC (GMT), GMT-1…GMT-12, GMT + 1…GMT +
           14.
       2). Select the time zone that you utilized for referencing your data collection time
           period.
       Duration in Hours:
       1). Place your cursor in the “Duration in Hours” field to activate the pop-up menu,
           which offers 1 to 24-hour long files in whole hour increments.
       2). Select the minimum number of hours to cover your time collection period.
       Site ID:
       If you do not remember the CORS ID of your selected station, press the “CORS
       Map” link and then zoom down to your collection area to find the closest CORS.
       1). Place your cursor in the “Site ID” field to activate the pop-up menu.
       2). Scroll down to your closest station and then select it, which will invoke the
           “Available Satellite Systems” option to list the satellite systems available for that
           particular station.
       Sampling Rate:
       1). Place your cursor in the “Sampling Rate” field to activate the pop-up menu,
           which offers the following options: “As is”, 1 second, 5 seconds, 15 seconds, and
           30 seconds.
       2). Select the “As is” option.

          Note: All the stations in the NCGS CORS Network record GNSS data at the 1-
                sec rate, which means that the “As is” is equivalent to the “1-sec rate”
                option. However, the three North Carolina CORS stations that are not in
                the NCGS network record at the following rates: NBR6 at 5 seconds,
                NCG5 at 5 seconds, and P779 at 15 seconds
          Note: Please remember that NGS decimates data files older than 30 days from
                the sampling rate that it was recorded at (e.g. 1-sec intervals) to a 30-sec
                sampling rate in order to save space on their server. Therefore, process
                your GNSS field data in a timely manner.
                                                                   Continued on the next page.

                                                                                               27

   d. Answer the following questions about your GNSS data collection period and then press
      the [Get CORS data file] button (continued from the previous page):
           Available Satellite Systems:
           1). If you collected the data with an old (legacy) “GPS only” receiver and your
               processing software cannot handle GLONASS data or the new GPS signals, then
               select only the “GPS (L1+L2 only)” option.
           2). If you collected the data with a relatively new “GPS only” receiver and your
               processing software can handle the new GPS signals, but not GLONASS signals,
               then select only the “GPS (L1+L2+L2C+L5)” option.
               Note: If your processing software can handle the new GPS signals, it will very
                     likely be able to handle GLONASS signals.
           3). Conversely, if you collected the data with a GNSS receiver or collected it with a
               “GPS only” receiver and use a processing program that can handle GLONASS
               data, then select the “GLONASS” option in addition to either the “GPS
               (L1+L2+L2C+L5)” or “GPS (L1+L2 only)” GPS options.
           Optional files?
           o Coordinate File: Yes or No (not needed for mapping-grade, but encourage the
             user to download for verification)
           o NGS data sheet: Yes or No (not needed for mapping-grade, but encourage the
             user to download for verification)
           o IGS Orbits in SP3 format: Yes or No (not needed for mapping-grade)
   3). Download the requested zip file, which will be named CORS ID Julian day.zip (e.g.
       nczo061.zip).

Base station files can also be downloaded automatically from UFCORS by using download
scripts with a GNSS processing software program, such as Trimble’s GPS Pathfinder Office
(http://www.trimble.com/mappingGIS/PathfinderOffice.aspx) or Leica’s Leica Zeno Office
(http://www.leica-geosystems.us/en/Leica-Zeno-Field-Office_79643.htm).

Whether a GNSS user downloads base station files from UFCORS automatically with a
download script or by visiting the UFCORS, this section is titled “Timely post-processing of
GNSS data” for a reason. It is important for each GNSS user to not delay differentially
correcting his/her uncorrected field files (i.e. stockpiling them for en masse processing), but
rather to download the necessary base station files and perform the differential correction process
on a daily or a weekly basis, because NGS decimates the sampling rate of each base station
GPS/GNSS file that is over 30-days-old from its original sampling rate (i.e. 1-sec for NCGS
stations) to a 30-sec rate in order to conserve space on their server.

                                                                                                   28

5.5.3. Processing of GNSS data in real time
5.5.3.1. North Carolina GNSS Real Time Network (RTN)
The NC GNSS RTN is a recommended source of real-time GNSS differential corrections for
GIS mapping by state agencies. In fact, the system is designed to support centimeter (cm) level
survey applications. Thus, it is more than robust enough for GIS mapping applications.

A user with a GNSS receiver can connect to the RTN using a wireless Internet connection [i.e. a
data enabled cell phone or a MiFi (i.e. a wireless router that can act as a mobile Wi-Fi hotspot)].
Once the RTN has determined that the user’s GNSS receiver is operating within the network’s
coverage area (Figure 4), it will then send GNSS correctors back to the user’s GNSS receiver for
real-time differential correction.

NCGS developed the RTN with software that can stream real-time correction signals to
individual users from a location-specific set of the six (6) closest stations within the statewide
NC CORS Network while simultaneously doing the same operation for other users. However,
instead of providing these correction signals as a set of correction signals from these closest
stations, the RTN assembles a “virtual” amalgamated station with the correction signals from the
closer base stations weighted more than those from the more distant stations.

                                                                                                 29

5.5.3.2. Nationwide Differential Global Positioning System (NDGPS)
The Nationwide Differential Global Positioning System (NDGPS) began as a United States
Coast Guard (USCG) maritime navigation system that has since expanded inland and become the
world’s largest ground-based GPS augmentation service covering the continental US, Alaska
(southern coast), Hawaii, and Puerto Rico (Figure 8).

 Figure 8.   The coverage area map of the Nationwide Differential GPS (NDGPS) network showing
             the location of DGPS sites in the network and the coverage areas with coverage from:
                 A single NGPS station shown in blue shading
                 Multiple NDGPS stations shown with pink shading
             Map source: USCG

Currently, the tower sites are positioned at a density of at least single coverage (i.e. being able to
receive signals from at least one tower) throughout nearly the entire coverage area of the system.
However, the USCG is working to increase that density to double coverage (i.e. being able to
receive signals from at least two towers) throughout the entire coverage area.

                                                                                                    30

The purpose of the NDGPS is to provide accurate positioning and location information in real-
time to meet surface transportation navigation needs (e.g. harbor navigation, emergency response
units, positive train control, etc.). Since the major uses of the system are for critical navigation
needs, each NDGPS site monitors the integrity of the GPS signal and will broadcast a warning if
an anomaly is detected. In addition to using the system for navigation, the correction signals can
also be used for a multitude of positioning needs, such as precision farming, land surveying,
mapping, and scientific applications.

In North Carolina (Figure 9), NDGPS provides statewide coverage from a station in Greensboro
and New Bern as well as from a station in Dandridge, Tennessee; Driver, Virginia; and
Kensington, South Carolina. In fact, most of the state has double coverage.

                                      DGPS coverage from the Nationwide DGPS for
                                       North Carolina and the surrounding states

 Figure 9. The coverage area map of the Nationwide
           Differential GPS (NDGPS) network in North
           Carolina and the surrounding states showing
           the location of DGPS sites in the network and
           the coverage areas with coverage from:
                A single NGPS station shown in blue
                shading
                Multiple NDGPS stations shown with
                pink shading
           Map source: USCG

These differential correction signals can be obtained in real-time from an NDGPS broadcast
tower site by tuning a navigation radio beacon, which can be purchased from most GNSS
vendors, to either the site’s transmitting frequency or its ID
(http://www.navcen.uscg.gov/?pageName=dgpsSiteInfo&All):
   New Bern, NC (294 kHz / ID 771)                         Driver, VA (289 kHz / ID 806)
   Greensboro, NC (303 kHz / ID 824)                       Kensington, SC (292 kHz / ID 778)
   Dandridge, TN (305 kHz / ID 782)

                                                                                                  31

The Nationwide Differential Global Positioning System (NDGPS) provides GPS differential
corrections that can yield a horizontal accuracy of 1-3 meters at the 95% confidence level. Thus,
it is an acceptable source of differential corrections for GIS mapping by state agencies.
However, since this differential correction procedure is dependent on receiving a radio signal
corresponding to each collected GPS position, the user must set the GNSS receiver’s real-time
settings with the following cascading search protocol:
1. Search for an NDGPS signal
2. If an NDGPS signal is not received, then use uncorrected GPS.

Since it is impractical to check to see if each collected GNSS position was differentially
corrected in real-time via an NDGPS signal, the user will still need to post-process the
collected GNSS field data to ensure that each collected GNSS position has been
differentially corrected. Basically, when NDGPS is used for:
   Mapping, the real-time corrections can create a good map of the mapped positions for the
   user to view while collecting data, but this map may contain uncorrected positions. Hence
   the need to post-process afterwards.
   Navigation, the real-time correction signals can be used to guide the user to the target site. If
   the receiver loses the signal during the navigation process, then the receiver should report a
   message like “Old navigation.”

Although the system is led by the USCG, it is an interagency collaborative with the following
partners (http://www.navcen.uscg.gov/?pageName=dgpsMain):
    US Department of Transportation (DOT): http://www.navcen.uscg.gov/?pageName=ndgpsMain
    US Army Corps of Engineers (USACE):
    http://www.navcen.uscg.gov/?pageName=ArmyCorpsEngineers

                                                                                                  32

5.5.3.3. Wide Area Augmentation System (WAAS)
The Wide Area Augmentation System (WAAS) is not an acceptable sole source of differential
corrections for GIS mapping by state agencies due to:
   Signal interruption problems from trees, buildings, and mountains
   Lower quality mapping accuracy (7 m)

When using WAAS as a source of differential corrections in the field, the data must still be post-
processed to verifty that all data has been corrected [please the procedure outlined in section
5.5.2. Timely post-processing of GNSS data].

Yet, the two high quality WAAS-based mapping receivers that are on the market now [SX Blue
(http://sxbluegps.com/) by GENEQ inc. and ikeGPS (http://www.ikegps.com/)] and their
accompanying software packages [PC-Mapper (http://sxbluegps.com/product/pc-mapper/) and
ikeDesktop 2.0 (http://www.ikegps.com/ikegps/ikedesktop/)] are designed for users to not post-
process. However, GENEQ inc. stated on its “Technology” webpage
(http://sxbluegps.com/technology/) that they will provide High Accuracy Solutions
(http://www.sxbluegps.com/survey-accessories-pp.html) for those who need information on how
to collect data that can be post-processed and information about “…specific L1 carrier phase
software for the post-processing,” but the link was diverted to their “Product Quote” request for
information form webpage (http://sxbluegps.com/product-quote/). [Please see the note in the
middle of p. 15 discussing the added costs of working with enhanced non-professional grade
receivers.]

If a WAAS-based receiver and its accompanying software package exist that can be post-
processed, the user would need to set the GNSS receiver’s real-time settings with the following
cascading search protocol:
1. Search for a WAAS signal
2. If a WAAS signal is not received, then use uncorrected GPS.

Basically, when WAAS is used for:
   Mapping, the real-time corrections can create a good map of the mapped positions for the
   user to view while collecting data, but this map may be contain uncorrected positions. Hence
   the need to post-process afterwards.
   Navigation, the real-time correction signals can be used to guide the user to the target site. If
   the receiver loses the signal during the navigation process, then the receiver should report a
   message like “Old navigation.”

                                                                                                  33

WAAS was developed by the Federal Aviation Administration (FAA) and the Department of
Transportation (DOT) for en route and precision approach aircraft navigation, because
unaugmented GPS alone cannot provide the positional accuracy to meet FAA's navigation
requirements for accuracy, availability, and integrity. WAAS tackles each of these requirements
accordingly:
    Positional accuaracy is achieved by providing differential correction to remove GPS signal errors
    caused by ionospheric disturbances, timing, and satellite orbit errors.
    Availability is achieved by broadcasting the differential correction signals from two (2)
    geostationary satellites positioned over the U.S.
    Integrity is achieved by monitoring the GPS signals to ensure that the corrections being transmitted
    are correct.

On 10 July 2003, FAA declared WAAS operational for aviation safety-of-life use in the U.S.
National Airspace System (NAS) by providing
    En route navigation across the entire NAS
    Vertical guidance performance [localizer performance with vertical guidance (LPV)] to
    most of the continental U.S.

                                                                                                        34

The system (Figure 10) utilizes a network of precisely-located ground Wide-area Reference
Stations (WRS) positioned across the continental U.S., Alaska, Hawaii, Puerto Rico as well as
additonal stations in Canada and Mexico. These stations collect and process GPS satellite data
and send this data to either of the three Wide-area Master Station (WMS), which calculates GPS
correction messages and then sends these messages to the Ground Uplink Stations, which in turn
transmit these correction signals to the three WAAS satellites, which in turn broadcast these
correction signals using the same frequency as the GPS satellites back to the earth for en route
and precision approach aircraft navigation.

 Figure 10. The basic design of the Wide Area Augmentation System (WAAS) (http://www.nstb.tc.faa.gov/):
               GPS satellites (shown at the top of the image) broadcasting GPS signals towards the earth.
                Wide-area Reference Stations (WRS) (shown as yellow circles in the U.S. and dark blue circles in
                Canada and Mexico) receiving GPS signals, which are then sent to the closest Wide-area Master Station
                (WMS) (shown as a rectangular server icon)
                WMS calculates correction signals and transmits them to the Ground Uplink Stations (shown as a
                parabolic antenna icon)
                The Ground Uplink Stations transmits the signals to the three WAAS satellites (shown at the bottom of
                the image as the two GEO Satellites)
                The WAAS satellites transmits the correction signals for en route and precision approach aircraft
                navigation

                                                                                                           35

As for mapping and navigating on the ground, the GNSS receiver must have a clean line-of-sight to one of the geostationary WAAS satellites to
receive the signals and be a WAAS enabled GNSS receiver to utilize the signals for differential correcting. Unfortunately, the necessity of
obtaining a line-of-sight with one the WAAS satellites to receive the signals renders this differential correction source as too unreliable for some
mapping projects. Although North Carolina is one of the states located closest to the WAAS satellite for the eastern U.S., (PRN 138, which is
labeled as ANIK in Figure 11), the satellite always resides relatively low in the southwestern sky at ~40 elevation due to being positioned in a
geostationary orbit at the equater at 107.3 W.

  Figure 11. Left image: An angle of elevation chart showing the elevation angle that would be observed in Raleigh, NC for the two geostationary WAAS
             satellites (PRN 138, which is labeled as ANIK, and PRN 135, which is labeled as PanAM) as well as for the constellation of GPS satellites
             (G01-G32).
             Right image: The location of the two geostationary WAAS satellites (PRN 138, which is labeled as ANIK, at 107.3 W and PRN 135, which
             is labeled as PanAM, at 133 W).

Therefore, any trees, mountains, and/or buildings on the horizon could easily obstruct the WAAS signal. Conversely, WAAS signal reception is
ideal for recreational GNSS uses in either open land or marine locations.

                                                                                                                                                     36

5.6. GNSS records retention and accessibility
It is strongly recommended that GNSS data collectors archive (i.e., safely backed up on a server,
CD, or DVD in an organized manner) all phases of the data used to create either a GIS data layer
or GNSS coordinates stored in a relational database. The GNSS data files should be easily
retrievable if questions about the processing methodology ever arise. Retaining the raw GNSS
data and correction files allows for re-processing if errors in the original process are discovered
later. More specifically, the data that should be archived in an easily recoverable and organized
manner include the following file types:
   Uncorrected (raw) GNSS filed data files
   GNSS base station correction files that were used to perform the original differential
   corrections
   Electronic data entry form (e.g. data dictionary) used to collect each mapped feature’s
   attributes
   Final differentially corrected GNSS datasets

5.7. Equipment and procedure testing
In order to ensure that faulty GNSS receivers can be identified for repair or disposal, all GNSS
receivers used in state work (including new equipment, old equipment, and equipment owned by
contractors) should be tested for accuracy every six (6) months by the following procedure:
1. Collect five (5) readings of ten (10) epics (1 or 5 second intervals) of any geodetic survey
    monument.
2. Perform the necessary differential correction.
3. Compare the differentially corrected state plane results (i.e. the northing and easting values)
    to the station's published horizontal position.
4. Retest each GNSS receiver that yielded accuracy results greater than the manufacturer's
    specified accuracy level.
5. Repair or dispose each receiver that failed the accuracy test twice.

The location and published horizontal position of geodetic survey monuments throughout the
state can be found on the NCGS website at the following URLs:
    http://geodeticsurvey.nc.gov Click on the [Geodetic Control] button at the top of the page.
    http://ncgs.nc.gov/geodeticmonuments/

Each agency that uses GNSS receivers should keep these biannual accuracy results of each
receiver (identified by model number and serial number) in their archives.

                                                                                                  37

5.8. Training and certification
An “Introduction to GNSS” course is available from NCGS for the benefit of the GNSS user.
This course covers the basics of GNSS theory, field receiver operation, differential correction,
and data documentation. It is recommended as a first step in the training process for new users
of GNSS technology.

GNSS operator certification is one result of the training course described above. Certification is
issued to the operator through NCGS. Continued certification requires completion of a refresher
training course on an annual basis.

5.9. GNSS data documentation (metadata)
Data collected using GNSS equipment should contain data documentation or metadata that
describe various aspects of the data set collected. Some of the pertinent information include:
   Model and accuracy of GNSS receiver
   Base station(s) used for differential corrections
   Software used for performing differential corrections
   Estimated horizontal and vertical accuracy of the data collected
   Datum
   Collection units (feet or meters)
   Coordinate system

All of these elements of the data set should be recorded in the data set’s accompanying metadata
file, which should be prepared in accordance with the FGDC “Content Standards for Digital
Geospatial Metadata” (CSDGM) as adopted by the GICC. The pertinent information listed
above is covered under the CSDGM’s Section 2 (Data Quality Information):
     http://www.fgdc.gov/metadata/csdgm/02.html

It is important that GNSS-collected GIS datasets contain two distinct forms of GNSS metadata
information:
    Documentation in the FGDC metadata of metadata specific to the GNSS receiver,
    differential correction process, and export settings used to create the final GIS layer (Note:
    Please read the 5.9.1. Metadata: Receiver section for a detailed explanation).
    Documentation in each feature’s attributes of a GIS layer of the quality of GNSS positional
    information used to create that feature (Note: Please read the 5.9.2. Metadata: Feature
    section for a detailed explanation).

                                                                                                     38

5.9.1. Metadata: Receiver
Documentation in the FGDC metadata of metadata specific to the GPS receiver,
differential correction process, and export settings used to create the final GIS layer.

The first type of documentation should reside in the FGDC metadata record for the final GIS
dataset. This documentation should include the following information:
    The type of receiver(s) used to collect the GNSS data
    Number of receiver channels
    The manufacturer’s published horizontal and vertical accuracy of receiver(s)
    The minimum number of satellites allowed during data collection
    The minimum elevation mask setting during data collection
    The maximum PDOP allowed during data collection
    The maximum SNR allowed during data collection
    The minimum number of positions collected for each feature, if applicable
    The dates of GNSS data collection
    The differential correction methods applied to the raw data, including type of correction,
    software name, and version used
    The GNSS base station(s) used for differential correction of GNSS data
    The approximate distance of the base station from the target GNSS data
    The projection or coordinate system used
    The datum used
    The units of measure used
    The altitude reference system [e.g. Height Above Ellipsoid (HAE) or Mean Sea Level
    (MSL)]. If MSL was used, then indicate which geoid model was used.
    The estimated percentage of vegetative cover (i.e., canopy) over feature locations
    The part of the feature where coordinates were recorded (e.g. general perimeter, center line,
    center point, shoulder of road/river, centroid of parcel, driveway entrance, or front door,
    etc.), if applicable
    The offsets used (if applicable)
    Collection speed [(i.e., stationary or moving) and mode of transportation (i.e., walking,
    bicycling, or driving in a motorized vehicle]. Note: This standard does not cover aerial
    GNSS data collection.

                                                                                                 39

Occasionally, project restrictions or unavoidable circumstances may necessitate GNSS receiver
settings or collection methods outside of those recommended by the State of North Carolina’s
GNSS standard. When this occurs, the actual GNSS collection conditions should be precisely
documented in the metadata so that secondary users of the dataset will be able to determine if the
data adequately supports their intended use. When GIS datasets covering the entire state or
regional areas have employed more than one GNSS methodology for data collection in
identifiable sub-areas, such as individual counties, each method should be separately
documented in the FGDC metadata. Using a standard checklist (Table 2) to document this
information for each data collection session is an efficient method of ensuring that this
information is captured.

Table 2: A standard metadata checklist.
Requirement                                          Example
                                                     Manufacturer & model:
                                                        Leica Zeno 10 or 15
Receiver type (s) used
                                                        Trimble Geo7 series
                                                        Trimble GeoExplorer 5 series
Number of receiver channels                          12
Horizontal accuracy of receiver (manufacturer’s
specifications for predicted error, including        1-5 meters+ 2ppm (root mean square)
reporting statistic)
Vertical accuracy as stated by manufacturer          3-5 meters+ 2ppm (root mean square)
Minimum number of satellites required                4
Minimum elevation mask setting                       15
Maximum PDOP allowed                                 6
Minimum SNR ratio allowed                            4
                                                     10 - 180 depending on the manufacturer’s
Minimum positions collected for each point feature
                                                     guidelines
Dates of GNSS Collection                             Between 1/15/2005 and 3/15/2005
                                                     Code Phase Post-Processed Differential using
                                                     Trimble’s Pathfinder Office 5.6 software,
                                                     including appropriate levels of detail in the
                                                     metadata process steps.
                                                     Other options might include:
GNSS correction methodology utilized                    Code Phase Real Time Differential (list
                                                        correction source, e.g. NDGPS beacon,
                                                        OmniStar, WAAS)
                                                        Carrier Phase / Real Time Kinematic
                                                        Carrier Phase / Static
                                                        Carrier Phase / Fast Static

Table continued on the next page.

                                                                                                     40

Table 2: A standard metadata checklist. Table continued from the previous page.

Requirement                                                   Example
                                                              RALEIGH DOT CORS ARP (NCRD)

                                                              The reference position used by the National
                                                              Geodetic Survey (NGS) is NAD 83(2011).
Base station used for differential correction.
                                                              NAD 83 (2011) position of Antenna Reference
If it is a statewide dataset and multiple base stations are   Point (ARP) of the geodetic antenna:
used, specify the base station used for each county and
list each base station’s pertinent information, which is          Latitude: 35 45 49.50795 N
readily available from the NCGS website:                          Longitude: 78 34 44.39448 W
http://geodeticsurvey.nc.gov/Pages/CORS-and-                      Ellipsoid Height (2011): 51.789 meters
GNSS.aspx                                                         NAVD 88 Orthometric Height: 85.04
                                                                  meters
                                                                  Receiver: Trimble NetR5 GNSS
                                                                  Antenna: Trimble Zephyr GNSS
                                                                  Geodetic II
Approximate distance from the base station used
                                                              20-30 miles
for differential correction
                                                              Geographic (Latitude/Longitude):
                                                                 Degrees Minutes Seconds (DMS)
                                                                 Decimal Degrees (DD)
Coordinate system used by GNSS Receiver(s)
                                                              NC State Plane (Zone 3200):
                                                                  Feet
                                                                  Meters
Unit of Measure                                               Feet or Meters
Datum used by GNSS Receiver(s)                                WGS84
                                                              Height Above Ellipsoid (HAE) or Mean Sea
Altitude reference system                                     Level (MSL) – if MSL was used, then indicate
                                                              which geoid model was used
Average percent of vegetative cover                           20%
                                                              Front door of main building
General location where the coordinates were                   Intersection of driveway and main road
recorded (if applicable)                                      Approximate center of parcel
                                                              As close to the smokestack as possible
Type of offset used (if applicable)                           15’ right offset from road centerline
                                                              Stationary
                                                              Walking
Collection speed/mode
                                                              Moving bicycle
                                                              Moving motorized vehicle

                                                                                                            41

5.9.2. Metadata: Feature

 Documentation in each feature’s attributes of a GIS layer of the quality of GPS positional
 information used to create that feature.

The second type of GNSS metadata is dependent upon the software and hardware product(s)
used to collect and process the GNSS data. Therefore, it is not feasible to specify a complete set
of GNSS quality attributes that are
universally supported. However, since
the vast majority of North Carolina state
and local government agencies use
Trimble brand GNSS hardware and
software for their mapping-grade GNSS
data collection, this GNSS standard
advises that all GNSS-collected GIS
datasets should include as many of the
GNSS quality attributes that are readily
available from Trimble GPS systems.
The Trimble Pathfinder Office software
supports retention and export of the
GNSS quality attributes to the final GIS Figure 12. The “General Attributes” export settings to
file format for each feature as listed in              select as listed in the Trimble Pathfinder
Figure 12 and Table 3. The majority of                 Office software package.
mapping and survey-grade GNSS
receivers and software packages should support collection and export of many, if not all, of the
GNSS quality attributes available for “All Feature Types” (Figure 12 and Table 3).

                                                                                               42

Table 3:   The GNSS quality attributes that Trimble Pathfinder Office can export from a GNSS
           file for all feature types as well as additional attributes that can be exported for point,
           line, and area features.

 Feature type         Exportable attribute
                          PDOP                                                Feature Name
                          Horizontal Dilution of Precision (HDOP)             Data File Name
                          Correction Status                                   Total Positions
 All feature types:       Receiver Type                                       Filtered Positions
                          Date Recorded                                       Data Dictionary Name
                          Time Recorded                                       GPS Week
                          Update Status                                       GPS Second
                          Height                                              Standard Deviation
 Point features:          Vertical Precision                                  Position
                          Horizontal Precision                                Point ID
                          Length (2d)                                         Worst Vertical Precision
                          Length (3d)                                         Worst Horizontal Position
 Line features
                          Average Vertical Position                           Line ID
                          Average Horizontal Position
                          Area (2d)                                           Average Horizontal Position
                          Perimeter (2d)                                      Worst Vertical Precision
 Area features
                          Perimeter (3d)                                      Worst Horizontal Position
                          Average Vertical Position                           Area ID

In addition, filtering of GNSS positions
during the final export (Figure 13) to a GIS
format should ensure that GNSS positions
that do not meet the following minimum data
quality standards will be filtered out of the
final GIS dataset:
   Uncorrected positions,
   Positions not using signals from at least
   four (4) satellites
   Positions where the PDOP and HDOP are
                                                      Figure 13. The “Position Filter Criteria” export
   greater than six (6).                                         settings to select as listed in the Trimble
   [Please refer to section 5.3.8. Positional                    Pathfinder Office software package.
   Dilution of Precision]

                                                                                                        43

The purpose of requiring both project level GNSS documentation in the FGDC metadata and the
GNSS quality information at the feature level as dataset attributes is to provide enough
information about GNSS-collected GIS data layers so that both analysis and decisions based on
the primary layer and any potential secondary uses of the dataset are conducted based upon the
knowledge of the dataset’s true accuracy.

                                                                                            44

6. Alternatives to mapping with a mapping-grade GNSS receiver
This section describes two methods for refining data collected with a non-professional GNSS
receiver utilizing orthoimagery that has documented horizontal accuracy that meets or exceeds
the GNSS data collection horizontal accuracy standard.

Method A: Imagery reference
The first method—what may be called “imagery reference”—is used to determine the final
coordinates for geospatial features based on their locations visible and identifiable in
orthoimagery. This method involves locating the area containing a feature that has been mapped
using one of the following techniques:
    Collecting feature data with a non-professional-grade GNSS receiver
    Applying GNSS data that has not been differentially corrected

For geospatial features from either type of source, the following steps will produce confirmed or
corrected features that meet horizontal accuracy standards. First, create a temporary “working”
dataset of uncorrected GNSS data. Next, use GIS software to display the “working” dataset over
orthoimagery that serves as a base map with known horizontal accuracy. For example, North
Carolina statewide orthoimagery has 6-inch ground resolution and an accuracy of +/- 2.0 feet or
better.

The next step is to use an editing tool in GIS to adjust the
location of each feature based on the corresponding feature
visible in the orthoimagery. For example, in Figure 14, a
point feature collected in the field using a non-professional-               after
grade receiver is located to the south of the intended
location (representing the front entrance to a public school
building). This “working” point can better represent the
school location with an adjustment. An analyst would move
the “before” point about 100 meters, adjacent to the                    before

apparent front entrance in the image (the “after” point or
whatever placement is               Figure 14. Imagery reference method of using aerial imagery that
specified in the business rules                has a documented horizontal accuracy that meets or
for the dataset) and document                  exceeds the GNSS data collection horizontal accuracy
the edit. This action refines                  standard to determine the coordinates of a feature
the positional accuracy of the                 collected with a non-professional GNSS receiver
estimated data to match the                    (shown as the “before” point) by creating a point at the
precision of the imagery,                      feature’s actual location (shown as the “after” point).
which would bring the spatial
                                    plotting the coordinates derived from A public school point location
                                                 displayed over orthoimagery of D.F. Walker Elementary
                                                 School in Edenton, NC.
                                                                                                          45

data into compliance with accepted state mapping accuracy standards. This method typically
works best for features that are represented as points, but can be used for lines and polygons as
long as the features (points or areas) are visible in the imagery.

                                                                                                    46

Method B: Digitizing without GNSS
The second method is to use GIS software to interactively create points over an orthoimagery
base map. This method does not involve a GNSS receiver to collect field data. Instead, an
analyst would display orthoimagery and any other base geographic datasets with known accuracy
to use as a visual reference. Next, the analyst would then use an editing tool to “digitizes”
recognizable point (e.g. wells), line (e.g. stream centerlines), and area (forest stand boundaries)
features in the imagery. For example, a playground behind a school, in leaf-off conditions, has
boundaries that are visible and may be represented as a new geographic feature. The horizontal
accuracy of the output dataset is largely based on the horizontal accuracy of the orthoimagery
along with the pixel resolution (e.g., 1 pixel = 6 inches by 6 inches), the digitizing scale (how
zoomed in on the image), and the digitizing skill of the individual. For example, the 2010 North
Carolina Statewide Digital Orthoimagery dataset has a horizontal accuracy of no worse than 4
feet error in any direction. If the digitizer zooms into reasonable scale (1:1000 to 1:500), that
person can expect
horizontal accuracies as
good as or better than
using differentially
corrected mapping-grade
GNSS which typically
generates horizontal
errors of no more than 15
feet.

Figure 15 displays an
example of North
Carolina statewide
imagery that contains
clearly visible features
suitable for interactive
data creation: a farm
field with distinct
vegetation (on the left), a
pond (on the right), and a
greenway (bottom
center).                      Figure 15. Digitizing without GNSS to create point, line, and/or area
                                         features. The example shows a digitized farm field area
                                         feature in the top left corner, a digitized pond area feature
                                         in the top right corner, and a digitized centerline of
                                         greenway line feature in the bottom.
                                                                                                         47

The digitizing without GNSS method has several possible advantages over using GNSS:
1) If the area to be mapped is large (i.e. a county or more), this method is useful given that
   much more area can be covered in one digitizing session than could ever be collected by an
   individual using GNSS on the ground over the same time interval.
2) Many geographic feature boundaries (stream edges, tree lines, etc.) are readily apparent to
   the eye when viewed from above. This can make collecting these boundaries digitally very
   easy compared to locating and mapping them on the ground.
3) Many locations are simply too difficult to map on the ground with GNSS due to terrain,
   weather, vegetation, wildlife, hostile property owners, etc. This method can be used to map
   any location covered by the imagery.
4) Many commercial and open source GIS software packages are available with capability to
   utilize Methods A and B.

There are also several possible drawbacks for Methods A and B:
1) Any imagery dataset is literally a snapshot in time. If a GIS analyst tries to map a feature as
   it exists today, then a snapshot from 2010 may be of little use depending on how much the
   feature has changed over time. For example, the latest available imagery for a site may have
   been acquired just 1 year ago, but would not show the development that has occurred in the
   intervening period.
2) The feature you wish to map may not be easily discernible in the imagery due to the scale of
   the imagery, shadows from nearby tall objects, or being obscured by vegetation. For
   example, mapping narrow streams in evergreen forests can be very difficult.
3) Training is usually required to develop the skill necessary to properly identify some
   geographic features visible in orthoimagery.

                                                                                                 48

7. Summary
The demand for more accurate and precise locational data within North Carolina state
government agencies will only increase with the continued automation of locational data sets.
GNSS is already the principal tool for collecting locational data used in systems, such as a
computer models or a GIS, for which geographic accuracy is critical. GNSS is an important and
cost-effective method for locating features too numerous or too dynamic to be mapped by
traditional methods. Therefore, GNSS mapping is being recommended by many state and
federal agencies as the locational data collection method of choice.

Each state agency that collects locational data must understand that there may be other
users of the data (in the present and/or in the future) with even more stringent accuracy
requirements than their requirements. Therefore, each state government agency that
collects locational data shall:
    Ensure that their locational data collecting personnel have a strong foundation in GNSS
    theory and have been trained in the proper use of GNSS equipment.
   Use either mapping-grade or survey-grade receivers in their GNSS data collection efforts.
   Non-professional receivers are not adequate for any state authoritative locational data
   collecting purpose. Non-professional grade receivers can be used for navigation and non-
   authoritative data collection activities, if the data collected is verified that it meets or exceeds
   the horizontal accuracy requirements by adhering to the procedure outlined in section 6
   Alternatives to mapping with a mapping-grade GNSS receiver.
   Test their GNSS receivers for accuracy daily if geodetic horizontal control monuments are
   located at the place of work or near the project site. At a minimum immediately prior to and
   immediately following the conclusion of a project, and at a minimum monthly.
   Differentially correct GNSS data or utilize the procedure outlined in section 6 Alternatives
   to mapping with a mapping-grade GNSS receiver.
   Archive the digital products representing all stages of the GNSS data collection and
   processing chain (e.g. uncorrected field files, base station files used for differential
   corrections, electronic data entry forms, corrected GNSS files, and final GIS datasets).
   Document all GNSS-derived GIS data products with appropriate forms of metadata.

                                                                                                     49

These minimum GNSS data collection and data documentation standards will have four (4)
important effects:
   Each state agency that collects GNSS data will know exactly what is expected from their
   time and effort spent to collect the locational data.
   Local, state, and federal agencies using state GNSS data can do so with confidence in its
   quality, because the data will have been collected, differentially corrected or verified that it
   meets the state horizontal accuracy standard by comparing the collected data to independent
   data source that meets or exceeds the state horizontal accuracy requirement, and documented
   according to standardized procedures.
   The state will save money by maximizing original locational data collection accuracy and
   documentation, which eliminates the need to recollect data.
   The use of GNSS for collecting locational data will become more prevalent in state
   government, because GNSS technology, training, and data documentation will be more
   consistent and readily accessible.

                                                                                                 50

8. References
Arkansas State Land Information Board. (2001). Standards for Collecting Mapping-grade
      Global Positioning System Positions. Retrieved from:
      http://www.gis.state.ar.us/Docs/LAW/GPS_Standard.pdf

August, P., Michaud, J., Labash, C., and Smith, C. (1994). GPS for Environmental Applications:
      Accuracy and Precision of Locational Data. Photogrammetric Engineering and Remote
      Sensing, v. 60, no. 1, pp. 41-45.

General Statutes of North Carolina. Chapter 89C: Engineering and Land Surveying. "The
      North Carolina Engineering and Land Surveying Act." (1951, c. 1084, s. 1; 1975, c. 681,
      s.1.). Retrieved from:
      http://www.ncga.state.nc.us/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_89C
      .html

Gilbert, C. (1994, April). Accuracy Specifications of GPS Data Collection Systems - Code-
        Based vs. Carrier-Based Systems. Earth Observation Magazine, pp. 57-59.

Hurn, J. (1989). GPS - A Guide to the Next Utility. Trimble Navigation.

Hurn, J. (1993). Differential GPS Explained. Trimble Navigation.

New Jersey Department of Environmental Protection. (2002). NJDEP GPS Data Collection
      Standards for GIS Data Development. Retrieved from:
      http://www.nj.gov/dep/gis/gpsoutstand.html

United States Department of Agriculture Forest Service, Technology Development Program.
       (2004). Comparing Four Methods of Correcting GPS Data: DGPS, WAAS, L-Band, and
       Postprocessing. 0471–2307–MTDC. Retrieved from:
       http://www.fs.fed.us/database/gps/pubs/htmlpubs/htm04712307/

United States Environmental Protections Agency. (2003). Global Positioning Systems -
       Technical Implementation Guidance. Retrieved from:
       http://www.epa.gov/esd/gqc/pdf/GPS-TIG_rev_2.pdf

                                                                                            51

United States National Park Service, 2004. Field Data Collection with Global Positioning
       Systems Standard Operating Procedures and Guidelines. Retrieved from:
       http://www.nps.gov/gis/gps/documents/FieldDataCollectionwithGPS_070204.doc

Vermont Center for Geographic Information, Inc. (2005). Vermont GPS Guidelines. In, VGIS
     Handbook. Retrieved:
     http://vcgi.vermont.gov/sites/vcgi/files/guidelines/partiii_section_l.pdf

Victoria (Australia) Department of Sustainability and Environment and Department of Primary
       Industries. (2006). Global Positioning System Handbook: GPS Data Collection for
       Integration with Geographic Information Systems - Standards, Specifications and Best
       Practice Field Guide, Version 7.2. (56 p.). Retrieved from:
       http://www.dse.vic.gov.au/__data/assets/pdf_file/0018/104661/GPSHandbookreduced.pd
       f

                                                                                           52

9. Glossary
9.1. Abbreviation and acronyms

 Abbreviation/Acronym Definition

 C/A code                Course/Acquisition GPS code

 CORS                    Continuously Operating Reference Station

 CSDGM                   Content Standards for Digital Geospatial Metadata

 dBHz                    decibel hertz

 DD                      Decimal degrees

 DGPS                    Differential Global Positioning System

 DMS                     Degrees minutes seconds

 DoD                     Department of Defense

 DOP                     Dilution of Precision

 DOT                     Department of Transportation

 EDT                     Eastern Daylight Time

 EST                     Eastern Standard Time

 FAA                     Federal Aviation Administration

 FGDC                    Federal Geographic Data Committee

 GICC                    Geographic Information Coordinating Council

 GIS                     Geographic Information System

                         Global Navigation Satellite System (English translation of
 GLONASS
                         Глобальная навигационная спутниковая система)

 GMT                     Greenwich Mean Time

 GNSS                    Global Navigation Satellite System

 GPS                     Global Positioning System

 GRS 80                  Geodetic Reference System 1980

 HAE                     Height Above Ellipsoid

Table continued on the next page

                                                                                      53

Continued from the previous page.

 Abbreviation/Acronym Definition

 HDOP                    Horizontal Dilution of Precision

 LPV                     Localizer Performance with Vertical guidance

 MiFi                    Mobile Wi-Fi, WiFi, or Wifi

 MSL                     Mean sea level

 NAD 83                  North American Datum of 1983

 NAS                     National Airspace System

 NAVSTAR                 Navigation and Vehicular Satellite Timing and Ranging

 NCGS                    North Carolina Geodetic Survey

 NDGPS                   Nationwide Differential Global Positioning System

 NGS                     National Geodetic Survey

 OPUS                    Online Positioning User Service

 P-code                  Precise code.

 PDOP                    Positional Dilution of Precision

 PPS                     Precise Positioning Service

 PPS                     Precise Positioning Service

 PRN                     Pseudo-Random Noise

 RTK                     Real Time Kinematic

 RTN                     Real-Time Network

 SA                      Selective Availability

 SMAC                    Statewide Mapping Advisory Committee

 SNR                     Signal to Noise Ratio

 SPS                     Standard Positioning Service

Table continued on the next page

                                                                                 54

Table continued from the previous page.

 Abbreviation/Acronym Definition

 UERE                    User Equivalent Range Error

 UFCORS                  User Friendly Continuously Operating Reference Station

 URE                     User Range Error

 USCG                    United States Coast Guard

 UTC                     Coordinated Universal Time

 WAAS                    Wide Area Augmentation System

 WGS 84                  World Geodetic System of 1984

 WMS                     Wide-area Master Station

 WRS                     Wide-area Reference Station

                                                                                  55

9.2. Definitions

Term                    Definition

                        The accumulated phase of either the L1 or L2 carrier of a GPS signal,
Carrier phase GPS       measured by a GPS receiver since locking onto the signal. Also called
                        integrated Doppler.

                        GPS measurements based on the pseudo random code (C/A or P) as
Code phase GPS
                        opposed to the carrier of that code.

                        That portion of the Global Positioning System that consists of a master
                        control station, monitoring stations, and ground antennas, which
Control segment
                        monitor and update satellite signals and upload correction data to the
                        satellites.

                        Also known as the civilian code. A family of PRN codes transmitted by
Course/Acquisition      GPS satellites. Each satellite is assigned one of 32 unique codes in the
(C/A) code              family. Each code consists of 1,023 chips and is sent at a rate of 1.023
                        megabits per second. The code sequence repeats every millisecond.

                        A discontinuity in GPS carrier-phase observations, usually of an integer
                        number of cycles, caused by temporary signal loss. If a GPS receiver
                        loses a signal temporarily, due to obstructions for example, when the
Cycle slip
                        signal is reacquired there may be a jump in the integer part of the
                        carrier-phase measurement due to the receiver incorrectly predicting the
                        elapsed number of cycles between signal loss and reacquisition.

                        A technique for reducing the error in GPS-derived positions by using
Differential
                        additional data from a reference GPS receiver (i.e. a base station) at a
positioning
                        known position.

                        A dimensionless number that accounts for the contribution of relative
                        satellite geometry to errors in position determination. DOP has a
Dilution of Precision   multiplicative effect on the User Equivalent Range Error (UERE).
                        Generally, the wider the spacing between the satellites being tracked by
                        a GPS receiver, the smaller the position error.

Table continued on the next page.

                                                                                                   56

Table continued from the previous page.

 Term                    Definition

                         A description of the path of a celestial body indexed by time (from the
                         Latin word, ephemeris, meaning diary). The navigation message from
                         each GPS satellite includes a predicted ephemeris for the orbit of that
 Ephemeris               satellite valid for the current hour. The ephemeris is repeated every 30
                         seconds and is in the form of a set of 16 Keplerian-like parameters
                         with corrections that account for the perturbations to the orbit caused
                         by the earth’s gravitational field and other forces.

                         That layer of the atmosphere approximately 30-300 miles above the
                         earth’s surface that contains electrically charged particles (ions).
 Ionosphere
                         These charged particles interfere with or distort transmissions of
                         electromagnetic signals through the layer.

                         Errors caused by the interference of a signal that has reached the
 Multipath error         receiver antenna by two or more different paths. Usually caused by
                         one path being bounced or reflected.

                         The Precise code. A PRN code transmitted by GPS satellites. The
                         code consists of about 2.35 3 1014 chips and is sent at a rate of 10.23
                         megabits per second. At this rate, it would take 266 days to transmit
 P-code
                         the complete code. Each satellite is assigned a unique one-week
                         segment of the code that is reset at Saturday/Sunday midnight. The P-
                         code is currently transmitted on both the L1 and L2 frequencies.

                         The full-accuracy, single-receiver GPS positioning service provided to
 Precise Positioning
                         the United States military, its allied military organizations, and other
 Service
                         selected agencies. It includes access to the unencrypted P-code.

                         The range between the antenna phase centers of a GPS satellite and a
                         receiver, measured by the receiver’s delay-lock loop using either the
 Pseudorange             C/A- or P-code. The range is biased by the offset of the clock in the
                         receiver from that in the satellite and by atmospheric propagation
                         delays.

Table continued on the next page.

                                                                                                 57

Table continued from the previous page.

 Term                    Definition

                        A Department of Defense policy and procedure, which was
                        discontinued as of May 1, 2000, that introduced intentional clock noise
 Selective Availability
                        into the GPS satellite signals to degrade accuracy in the Standard
                        Positioning Service (SPS) (i.e. civilian service).

 Space segment           The part of the whole GPS system that is in space (i.e. the satellites).

                         Also known as the civilian system. The GPS single receiver (stand-
 Standard                alone) positioning service available to any user on a continuous,
 Positioning Service     worldwide basis. It is intended to provide access only to the C/A-code
                         and the L1 carrier.

                         Location determination when the receiver’s antenna is presumed to be
 Static positioning      stationary on the earth. This allows the use of various averaging
                         techniques to greatly improve accuracy.

                     Any error contributing to the error budget of stand-alone GPS receiver
 User Equivalent     positioning, expressed as an equivalent error in the range between a
 Range Error or User user’s receiver and a satellite. UEREs originate from different sources,
 Range Error         and thus are independent of each other. The total UERE is the square
                     root of the sum of the squares of the individual errors.

                                                                                                    58

10. GNSS resources
10.1. GNSS standards from governments and organizations
10.1.1. International
   British Columbia, Canada/Ministry of Forests, Lands and Natural Resources Operations
   o Standards, Specifications and Guidelines for Resource Surveys Using Global Positioning
     System (GPS) Technology [April 2008]
          http://www.ilmb.gov.bc.ca/risc/pubs/other/gps/gps_standard_2008.pdf

   Natural Resources Canada/Geomatics Canada/Geodetic Survey Division
   o GPS Positioning Guide      [July 1995]
          http://webapp.csrs.nrcan.gc.ca/GPS_Guide_e/GPS_Guide_e.pdf
   o Guidelines for RTK/RTN GNSS Surveying in Canada         [July 2013]
          http://webapp.geod.nrcan.gc.ca/geod/publications/pdf/Canada%20RTK_UserGuide_v
          1%201_EN.pdf

   Province of Victoria, Australia/Department of Sustainability and Environment & Department
   of Primary Industries
   o Handbook for GPS Data Collection for Integration with GIS Standards, Specifications
     and Best Practice Field Guide [Feb 2006]
          http://www.dse.vic.gov.au/__data/assets/pdf_file/0018/104661/GPSHandbookreduce
          d.pdf
          Note: There are 2 underscores (“_” and “_”) between “.au/” and “data” in the URL.

                                                                                              59

10.1.2. Federal
   NOAA/National Geodetic Survey (NGS)
   o User Guidelines for Single Base Real Time GNSS Positioning        [August 2011]
          http://www.ngs.noaa.gov/PUBS_LIB/NGSRealTimeUserGuidelines.v2.1.pdf
   o Real Time Positioning - Best Methods for the Field (webinar)      [11-09-2011]
          http://www.ngs.noaa.gov/corbin/class_description/RT_field_2011.shtml

   U.S. Army Corps of Engineers
   o Engineering and Design: Navstar Global Positioning System Surveying (EM 1110-1-
     1003) [02-28-2011]
          http://140.194.76.129/publications/eng-manuals/EM_1110-1-1003_pfl/

   U.S. Environmental Protection Agency (EPA)/Office of Environmental Information
   o GPS Technical Implementation Guidance       [July 2006]
          http://www.epa.gov/esd/gqc/pdf/GPS-TIG_rev_2.pdf

   U.S. Department of the Interior (DOI)/National Park Service (NPS)
   o Field Data Collection with GPS Standard Operating Procedures and Guidelines
     [07-02-2004]
          http://www.nps.gov/gis/gps/documents/FieldDataCollectionwithGPS_070204.doc
   o Global Positioning System Data Acquisition and Processing      [01-28-2009]
          http://science.nature.nps.gov/im/units/nccn/assets/docs/dm_docs/NCCN_GPS_Guidel
          ines.pdf

                                                                                       60

10.1.3. State
   Arkansas State Land Information Board
   o Standards for Collecting Mapping Grade Global Positioning System Positions and GPS
     Metadata [8-29-2001]
           http://www.gis.state.ar.us/Docs/LAW/GPS_Standard.pdf

   Georgia Department of Transportation (GDOT)
   o GPS Data Collection Policy        [5-2-2013 cited NC’s GPS stds]
           http://mydocs.dot.ga.gov/info/gdotpubs/Publications/8085-2.pdf

   Idaho Transportation Dept (ITD)
   o Global Positioning System Data Collection and Documentation Standards             [8-15-2003]
           http://itd.idaho.gov/planning/gis/maps/Standards/GPSStandards.doc

   New Jersey Department of Environmental Protection (NJDEP)
   o NJDEP GPS Data Collection Standards For GIS Data Development                [6-8-2011]
           http://www.nj.gov/dep/gis/GPSStandards_2011.pdf

   Texas Commission on Environmental Quality
   o GPS: Guidelines and Information         [11-4-2002]
           http://www.tceq.state.tx.us/permitting/water_supply/pdw/SWAP/gps/opp_8.12.html

   Texas Department of Transportation (TXDOT)
   o Survey Manual – GPS Surveying          [April 2011]
           http://onlinemanuals.txdot.gov/txdotmanuals/ess/gps_surveying.htm

   Vermont Center for Geographic Information (VCGI)
   o Vermont GPS Guidelines         [September 2005]
           http://vcgi.vermont.gov/sites/vcgi/files/guidelines/partiii_section_l.pdf
10.1.4. Organizations
   Royal Institution of Chartered Surveyors (RICS)
   o Guidelines for the use of GNSS in land surveying and mapping          [11-2010]
           http://www.rics.org/us/shop/Guidelines-for-the-use-of-GNSS-in-Surveying-and-
           Mapping-18524.aspx
           http://www.cnavgnss.com/uploads/Guidelines_for_the_use_of_GNSS_in_surveying_
           and_mapping.pdf

                                                                                                61

10.2. GNSS information
10.2.1. Federal
    Federal Aviation Administration (FAA)
   o Real-Time WAAS DOP Accuracy Display          [updated every three minutes]
          http://www.nstb.tc.faa.gov/RT_NPACoverage.htm

   National Geospatial-Intelligence Agency
   o Office of Geomatics    [4-30-2013]
          http://earth-info.nga.mil/GandG/

   NOAA/National Geodetic Survey
   o Continuously Operating Reference Station (CORS) Network
          http://www.ngs.noaa.gov/CORS/      [12-17-2013]
   o GPS and Geodesy for Dummies: Do You Know Where You Are?             [08-19-2007]
          http://learningcenter.nsta.org/products/symposia_seminars/stlouis07/GPS/webseminar
          .aspx

   U.S. Coast Guard NAVCEN
   o General information on GPS      [12-11-2013]
          http://www.navcen.uscg.gov/?pageName=GPSmain

   U.S. Dept of Agriculture/Natural Resources Conservation Service (NRCS)
   o National Geospatial Center of Excellence (NGCE)        [no date info on the content, but
     the social media links imply that it is current]
          http://www.ncgc.nrcs.usda.gov/products/gps/index.html

   US Department of the Interior (DOI)/National Park Service (NPS)
   o Global Positioning Systems     [no date info on the content]
          http://www.nps.gov/gis/gps/

   U.S. Naval Operations Center
   o GPS Timing and Data       [updated each second]
          http://www.usno.navy.mil/USNO/time/gps

                                                                                                62

10.2.2. State
   New Jersey Department of Environmental Protection (NJDEP)
   o A Guide to the Basic Concepts of the NAVSTAR Global Positioning System   [5-8-2003]
           http://www.nj.gov/dep/gis/gpsweb/train00_files/frame.htm

10.2.3. Private
   Rocco V. D'Andrea, Inc.
   o Interactive GPS Day/Week Calendar            [3-15-2010]
           http://www.rvdi.com/freebies/gpscalendar.html

   Samuel J. Wormley
   o GPS Errors & Estimating Your Receiver's Accuracy           [7-15-2010]
           http://edu-observatory.org/gps/gps_accuracy.html
   o DGPS Resources         [12-18-2009]
           http://www.edu-observatory.org/gps/dgps.html

10.3. Online GNSS-related magazines
   GeoInformatics       [updated daily]
       http://www.geoinformatics.com/

   GIM International       [updated daily]
       http://www.gim-international.com/

   GPS World
       http://gpsworld.com/     [updated daily]

   Inside GNSS
       http://www.insidegnss.com/         [updated daily]

   Point of Beginning      [updated daily]
       http://www.pobonline.com/

   Professional Surveyor      [updated ~daily]
       http://www.profsurv.com/

   Spatial Source    [updated daily]
       http://www.gisuser.com.au/

                                                                                      63

10.4. Free mission planning software
   Trimble GNSS Planning Online      [almanac updated daily]
      http://www.trimble.com/GNSSPlanningOnline/#/Settings

   Trimble Planning Software v2.9      [Aug 2010]
      http://ww2.trimble.com/planningsoftware_ts.asp
      Note: This software requires the current almanac, which can be downloaded from either:
      o NAVCEN (http://www.navcen.uscg.gov/?pageName=gpsAlmanacs)
      o Trimble (ftp://ftp.trimble.com/pub/eph/almanac.alm)

10.5. Commercial GNSS software
10.5.1. Field computer software
   ESRI ArcPad
      http://www.esri.com/software/arcgis/arcpad
      Note: Mobile field mapping and data collection software
      o Extensions for ESRI ArcPad or ArcGIS mobile
          - Trimble Positions Software Suite
             http://www.trimble.com/mappingGIS/trimblepositions.aspx
             Note: Integrates Trimble's field solutions/data verification into the ArcGIS
                   environment
          - Trimble GPSCorrect Extension for ESRI ArcPad
             http://www.trimble.com/mappingGIS/gpscorrect.aspx
             Note: Provides the ability to log GNSS data for post-processing

   Leica Zeno Field & Office
      http://www.leica-geosystems.us/en/Leica-Zeno-Field-Office_79643.htm
      Note: Original equipment manufacturer (OEM) version of ArcPad that provides GNSS
            raw data logging for post-processing

   Trimble TerraSync
      http://www.trimble.com/mappingGIS/TerraSync.aspx
      Note: Field GIS data collection and maintenance with seamless GNSS control in the field

                                                                                            64

10.5.2. Desktop software
    Leica Zeno Field & Office
       http://www.leica-geosystems.us/en/Leica-Zeno-Field-Office_79643.htm
       Note: Provides the ability to post-process GNSS data within ArcGIS Desktop

   Trimble GPS Pathfinder Office
       http://www.trimble.com/mappingGIS/PathfinderOffice.aspx
       Note: Provides the ability to post-process, manage, and export GNSS data

   Trimble GPS Analyst Extension for ESRI ArcGIS
       http://www.trimble.com/mappingGIS/gpsanalyst.aspx
       Note: Provides the ability to post-process GNSS data within ArcGIS Desktop

10.6. Government software
   NOAA/National Geodetic Survey
   o Geodetic Toolkit
          http://www.ngs.noaa.gov/TOOLS/
   o Geodetic software
          http://www.ngs.noaa.gov/PC_PROD/pc_prod.shtml

                                                                                    65

10.7. GPS/GNSS receivers
      Note: Several of the following GPS/GNSS receivers could be placed in more than one
             accuracy category depending on the data collection method utilized)
10.7.1. Sub-foot accuracy mapping-grade
    ikeGPS
   o ikePro (http://www.ikegps.com/ikegps/ikepro/), but only in combination with a
     Septentrio APS-3X Pak (http://www.ikegps.com/ikegps/high-accuracy-tools/)

   Leica
   o Leica CS25 GNSS
           http://www.leica-geosystems.us/en/Leica-CS25-GNSS_101857.htm

   Spectra Precision
   o MobileMapper 100
           http://www.spectraprecision.com/products/gis-mobile-mapping/mobilemapper-100/

   SX Blue (only the RTN or OmniStar enabled series)
   o SXBlue III GNSS
           http://sxbluegps.com/product/sxblue-iii-gnss/
   o SXBlue III-L GNSS
           http://sxbluegps.com/product/sxblue-iii-l-gnss/
   o SXBlue III GPS
           http://sxbluegps.com/product/sxblue-iii-gps/

   Trimble
   o Trimble Pro 6H
           http://www.trimble.com/mappingGIS/pro6.aspx
   o Trimble Pro 6T
           http://www.trimble.com/mappingGIS/pro6.aspx
   o Trimble Geo 6 Series (Geo XH)
           http://www.trimble.com/mappingGIS/geo6.aspx

                                                                                           66

10.7.2. Sub-meter (1 - 3 feet) accuracy mapping-grade
   Trimble
   o GPS Pathfinder ProXRT
           http://www.trimble.com/mappingGIS/pathfinderproxrt.aspx
   o Geo 7 Series
           http://www.trimble.com/mappingGIS/geo-7-series.aspx
   o Geo 6 Series (Geo XT)
           http://www.trimble.com/mappingGIS/geo6.aspx
   o GeoExplorer 5 Series
           http://www.trimble.com/mappingGIS/geo5.aspx

   Leica
   o Leica Zeno 10 & Zeno 15
           http://www.leica-geosystems.us/en/Leica-Zeno-10-Zeno-15_79645.htm

   Spectra Precision

      MobileMapper 120
           http://www.spectraprecision.com/products/gis-mobile-mapping/mobilemapper-120/

      MobileMapper 10
           http://www.spectraprecision.com/products/gis-mobile-mapping/mobilemapper-10/

                                                                                           67

10.7.3. Sub-5 meter (3 - 15 feet) accuracy mapping-grade
   Trimble
   o Juno 5 Series Handheld
           http://www.trimble.com/mappingGIS/juno5.aspx
   o Juno 3 Series
           http://www.trimble.com/mappingGIS/juno3.aspx
   o Juno SD
           http://www.trimble.com/mappingGIS/junoS.aspx
   o Juno SA
           http://www.trimble.com/mappingGIS/junosa.aspx
   o Nomad G Series
           http://www.trimble.com/mappingGIS/nomadg.aspx
   o Yuma 2 Rugged Tablet
           http://www.trimble.com/mappingGIS/yuma2_rugged_tablet.aspx

   Leica
   o Leica Zeno 5
           http://www.leica-geosystems.us/en/Leica-Zeno-5_99189.htm

                                                                        68

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
