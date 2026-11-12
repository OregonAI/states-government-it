---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-gis-water-sewer-data-standard
title: Geographic Data Content Standard for Water Distribution and Sanitary Sewer Systems
doc_type: standard
citation: 'NC GIS standard: Geographic Data Content Standard for Water Distribution and Sanitary Sewer
  Systems'
authority_level: ''
issuing_body: Geographic Information Coordinating Council (published by NCDIT)
source_url: https://it.nc.gov/geographic-data-content-standard-water-distribution-and-sanitary-sewer-systems/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 200e321c9cc3fdf803c59ae6ee62fb9492450fd04893d949caea408d04e59d11
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

# Geographic Data Content Standard for Water Distribution and Sanitary Sewer Systems (NC GIS standard: Geographic Data Content Standard for Water Distribution and Sanitary Sewer Systems)

## At a glance

The data content standard adopted by the Geographic Information Coordinating Council on December 4, 1997 (version 3.1). Linked on the standards page as /geographic-data-content-standard-water-distribution-and-sanitary-sewer-systems.

## Full text

                 Adopted by the North Carolina
           Geographic Information Coordinating Council
                        December 4, 1997

                 Geographic Data Content Standard for
                    Water Distribution Systems and
                       Sanitary Sewer Systems
                                         VERSION 3.1

                             State of North Carolina
                    Center for Geographic Information & Analysis
                       301 North Wilmington Street, Suite 700
                               Raleigh, NC 27601-2825

                                          April 1997

                                 Updated September 2011

                                     PREFACE (1997)

The use of geographic information systems (GIS) and related technology to manage vital
information about our communities and regions of the state has clearly become more
commonplace. Perhaps no other recent effort than the development of this document and the
related project to inventory and characterize the water distribution and sanitary sewer systems
in rural North Carolina is testament to the growing use of GIS. Through this project, numerous
elected officials, town managers, and others from non-urban regions of the state have been
exposed to the value of using GIS for managing and understanding large and complex amounts
of detailed information. Many are now beginning to use GIS data to help maintain future safe
drinking water supplies and to develop environmentally responsible waste treatment plans in
hopes to spur or ensure continued economic growth in their communities.

This standard is primarily intended to serve as a specification for the statewide water and sewer
inventory project conducted by the North Carolina Rural Economic Development Center and the
Western Piedmont Council of Governments. It is anticipated that the standard will be used to

                                                1

provide a basis for continued maintenance of the inventory and by others that develop and
manage data about water and sewer infrastructures.

The development of this standard evolved over many months and its content reflects "in the field"
experiences of staff from the Rural Center, McGill & Associates, and the Western Piedmont
Council of Governments. The experiences shared from the field were important and significantly
improved the document from its first draft.

We expect that many will consider and use the standard as developed and we certainly anticipate
that they also will provide their insights and requirements back to us so that subsequent versions
of the document are valuable to the community at large.

Zsolt Nagy,
North Carolina Center for Geographic Information and Analysis

John Soles,
North Carolina Rural Development Council
Rural Economic Development Center, Inc.

Francine Stephenson
North Carolina Office of State Planning

                              ACKNOWLEDGMENTS (1997)

Many served to launch this initiative and provided feedback on specific aspects of this document.
The following is a list of key project participants the authors wish to recognize.

DeWitt Blackwell, Western Piedmont Council of Governments
Billy Ray Hall, NC Rural Economic Development Center
Kenneth Flowers, NC Rural Development Council
Karen Siderelis, Center for Geographic Information and Analysis

Dana Bolden, McGill & Associates
Faith Hege, Western Piedmont Council of Governments
Mike Williams, Western Piedmont Council of Governments
Neil Thomas, Resource Data, Inc.
David Giordano, Center for Geographic Information and Analysis
Cathy Bock, Rural Economic Development Center, Inc.
Eddie Staley, Hobbs, Upchurch and Associates

Funding and support provided by the
Western Piedmont Council of Governments and the
North Carolina Rural Economic Development Center, Inc.
Research and Demonstration Grants Program.

                                                2

Preface to Update (2011)
The Lumber River Council of Governments led a review of the standard in 2010 and identified
additional or updated attributes for water and sewer systems to reflect current practices in local
facility management, regional planning, and data management. The review team specified
additional data layers that are common in facility management and practical to represent as
geospatial data at larger mapping scales than applied in the 1997 efforts. The review included a
set of recommendations for applying GIS software to add value to datasets. Those
recommendations are contained in a separate document intended to serve as a guide to best
practices in developing geospatial data for water and sewer systems.

North Carolina Center for Geographic Information and Analysis
Tim Johnson, Director
Jeff Brown, Coordination Program Manager
David Giordano, Database Administrator and staff to the Statewide Mapping Advisory
Committee

Acknowledgements (2011)
This update relied on the following key participants and their respective organizations:

Jim Perry, Executive Director, Lumber River Council of Governments
James Armstrong, GIS Director, Richmond County and member of the Statewide Mapping
Advisory Committee
Julie Haigler Cubeta, Senior Director, Physical Infrastructure, NC Rural Economic Development
Center
Anne Payne, Chair, Statewide Mapping Advisory Committee

                                                 3

                            TABLE OF CONTENTS
Section 1: Introduction
       Background                                                          5
       Objective                                                           5
       Geographic Information Coordinating Council                         6
       NC OneMap                                                           6
Section 2: Content Standards - General
       Methodology                                                         7
       Document                                                            7
       Participants                                                        7
Section 3: Content Standards - Water Distribution Systems
       Definition                                                    9
       Geometric Representation                                     10
       Geographic Coordinate System, Datum, and Unit of Measurement 10
       Annotation                                                   10
       Metadata                                                     10
       Symbology                                                    11
       Attributes                                                   11
       Summary of Attributes                                        11
       Definition of Attribute Fields                               15
Section 4: Content Standards - Sanitary Sewer Systems
       Definition                                                   34
       Geometric Representation                                     35
       Geographic Coordinate System, Datum, and Unit of Measurement 35
       Annotation                                                   35
       Metadata                                                     35
       Symbology                                                    35
       Attributes                                                   36
       Summary of Attributes                                        36
       Definition of Attribute Fields                               40
Section 5: Content Standards - Supplementary Owner Information             60

Lists
List 1 - Summary of Water Distribution Systems Attribute Fields            11
List 2 - Summary of Sanitary Sewer Systems Attribute Fields                36
List 3 - Summary of Supplementary System Owner Information                 60

Tables
Table 1 - Definitions of Attribute Fields for Water Distribution Systems   15
Table 2 - Definitions of Attribute Fields for Sanitary Sewer Systems       40
Table 3 - Definitions of Attribute Fields for Owners                       61

Glossary of Terms                                                          64

                                                4

SECTION 1: INTRODUCTION
Background

The availability of safe drinking water supplies and the ability to economically treat, process,
sanitize, and return treated sewerage into the state's rivers and lakes are critical issues for citizens
of North Carolina as we approach the next millennium. Thorough knowledge about the location,
condition, and capacity of water distribution and sanitary sewer systems and information about
the projected need for these systems throughout the state is vital. Federal, state and local
officials, planners, and engineers are in need of reliable and comprehensive information that can
be used to manage the current infrastructure and plan for the future.

In response to this need, the Rural Economic Development Center conducted a detailed
inventory of all water and sewer systems in North Carolina and an assessment of needs for
expansion and development of new systems (late 1990s). Information collected in that project
has been stored and maintained in the North Carolina OneMap Database, a collection of strategic
geographic information.

Two agencies, the Western Piedmont Council of Government, and the North Carolina Rural
Economic Development Center, agreed to cooperate with the North Carolina Center for
Geographic Information and Analysis (CGIA) on the development of this water distribution and
sanitary sewer systems geographic data content standard. This document was used in the project
as the data content specifications for the statewide geographic data layer on water and sewer
systems.

The information is accessible through the use of geographic information systems technology.
Geographic information systems (GIS) are now widely used by public and private organizations
to manage information, analyze, predict, and assist with human and natural activities on the
earth. GIS is now being used by all 100 counties in North Carolina, as well as lead regional
organizations, state departments, federal organizations, and private businesses and utilities.

Since the 1990s, mapping of water and sewer projects is much more common by municipalities
and counties and their service providers. In addition, a second statewide project by the Rural
Economic Development Center, Water 2030, completed in 2007, developed a statewide
representation of service areas (not facilities) that was consistent with this set of standards.
Additional data items collected for water and sewer systems for Water 2030, beyond items in this
set of standards, are included in a best practices document.

Objective

The objective of this effort is to develop a geographic data content standard for use in the
development of a statewide geographic dataset for water distribution and sanitary sewer systems
in rural North Carolina. With the guidance and oversight of the Geographic Information
Coordinating Council, North Carolina has implemented a strategic plan to guide the growth of

                                                   5

geographic information systems, geographic information, and related technologies. An
important aspect of the strategic plan is the development of data and technology standards.
The original geographic data content standard was intended to be the basis for the development
of a statewide data layer, as a component of the NC OneMap Database, for water distribution and
sanitary sewer systems. The updated standard adds facility detail intended to enhance water and
sewer asset management. The standard is intended to represent the minimum requirements of
data content for all organizations planning, building, and/or maintaining geographic data about
water distribution and sanitary sewer systems. The fields specified in this standard enable visual
display and analysis of patterns within local systems and across systems. Additional fields
related to costs, contractors, facility conditions, and system maintenance, though not specified in
the standard, would add value to a database linked to mapped facilities. Modern database
software enables multiple related tables that may be linked to map features by a unique identifier.

Geographic Information Coordinating Council
Established by Executive Order Number 16 in May 1993 and mandated by the General
Assembly in 2001 (North Carolina General Statutes Article 76, Sections 143-735 through 143-
727), the North Carolina Geographic Information Coordinating Council (GICC) is responsible
for the oversight and cost-effective development, management, and utilization of geographic
information, geographic information systems and other related technologies in the state. The
GICC is specifically responsible for (a) strategic planning, (b) resolution of policy and
technology issues, (c) coordination, direction and oversight, and (d) advising the Governor and
the Legislature as to the needed directions, responsibilities, and funding regarding geographic
information.

Statewide initiatives to coordinate the growth and use of geographic information systems and the
sharing of geospatial data involves the cooperation of state, federal, and local government
agencies; academic institutions; and the private sector. Initiatives are intended to improve the
quality, access, and utility of North Carolina's geographic information and to promote
geographic information as a strategic resource in the state.

NC OneMap Database
The NC OneMap Database is a statewide strategic resource containing an abundant supply of
information about North Carolina. For example, the content of the NC OneMap Database
includes information about North Carolina's cultural resources, surface waters, topography,
jurisdictional boundaries, environmental regulations, land cover, streets and highways,
demographics, and natural resources. Each category of data is geo-referenced, described, and
managed in data layers and online services. The data layers and services are produced,
maintained, accessed, distributed, hosted, and otherwise used by government and private
organizations for a number of purposes. Water and sewer datasets are among the priorities for
the GICC and NC OneMap. See www.nconemap.com for more information.

                                                6

SECTION 2: Content Standards
Methodology (1997)
Development of the data content standard has occurred in several phases.
Phase one activity consisted of an assessment of information needs through an informal survey
and through two facilitated workshops. Information needs were identified by a variety of
potential data users, including public officials, resource managers, and professional engineers.
Phase two activity consisted of the collection and assessment of other water and sewer systems
standards and an assessment of existing geographic data files containing features pertaining to
water and sewer systems. Phase three activity was an implementation of the standard by two
organizations in the state. The working content standard was used in the development of
geographic data files by the Rural Economic Development Center and the Western Piedmont
Council of Government. Reaction to the standard in the field by both organizations was an
important aspect of the development and refinement of the document.

An update phase occurred in 2010, led by the Lumber River Council of Governments, the NC
Rural Economic Development Center, Richmond County, the Statewide Mapping Advisory
Committee, the Local Government Committee, and a utilities working group. The purpose of
this effort was to update the standard to be consistent with current mapping needs and to
supplement the standard with recommended practices that take advantage of current technology.

Document (1997)
This document was prepared under a research and demonstration grant provided to the Western
Piedmont Council of Governments by the Rural Economic Development Center, Inc. in support
of the collaborative efforts with the NC Rural Development Council, the US Department of
Agriculture, and the Office of the Governor's "NC Water and Sewer Inventory and Needs
Assessment Project."
The document has been prepared for immediate use by all organizations that plan to implement
digital geographic water and sewer inventory projects in the state. This document was revised in
2011 with the intention of making the standard consistent with current geospatial data
development needs.

Participants (1997)
An advisory committee consisting of state, regional, and local representatives familiar with the
delivery and management of water and sanitary sewer systems were assembled for two
information requirement sessions. The advisory committee also included several members who
were very familiar with the operations and management of data using geographic information
systems and related technologies.

Advisory Committee Members (1997)
E.H. Alexander, REDC Board of Directors, Infrastructure Committee
E. Lee Armour, Centralina Council of Governments
DeWitt Blackwell, Western Piedmont Council of Governments
Bobby Blowe, NC Division of Environmental Management
Steven Dear, NC Rural Assistance Project, Inc.
Bill Gibson, Southwestern NC Planning and Economic Development Commission

                                                7

Ronald Goswick, Kerr-Tar Regional Council
Wayne Jenkins, Northampton County Public Works
Buck Kennedy, The Wooten Company
Al Leonard, Town of Tabor City
Herman Little, Anson County Commissioner
Rose Ann Mack, Cape Fear Council of Governments
Gary McGill, McGill Associates, P.A.
David Muse, City of New Bern
Lynn Norton, Alexander Water Corporation
Jerry Perkins, NC Division of Environmental Health
Ed Regan, NC Association of County Commissioners
Bob Schley, NC Rural Water Association
Edgar R. Shuller, NC Department of Transportation
Karen Siderelis, NC Center for Geographic Information and Analysis
Paula Thomas, NC League of Municipalities
Bobby White, Burke County
Zettie Williams, Duplin County Commissioner

Participants in the 2011 Update to the Standard

Lumber River Council of Governments

The NC Rural Economic Development Center

Local Government Committee (LGC)

Statewide Mapping Advisory Committee (SMAC)
       Anne Payne, Chair, Wake County
       Utilities Working Group:
               Chris Butts, Moore County
               Jeff Cooke, City of Goldsboro
               Ray Kurtiak, City of Gastonia
               Rob Bailey, City of Charlotte
               Mike Mull, Town of Cary
               Sarah Sheldon, Town of Wake Forest
               Kathryn Brewer, MSD of Buncombe County
               Trey Cleaton, City of Salisbury
               James Armstrong, Richmond County

NC Center for Geographic Information and Analysis (CGIA)
      CGIA received helpful comments on draft revisions from SMAC members as well as
      Julie Haigler Cubeta of the NC Rural Economic Development Center, Bliss Kite of the
      NC Public Utilities Commission, Jessica Godreau of the NC Public Water Supply
      Section, and Wayne Francisco, GHD.

                                             8

SECTION 3: Content Standard - Water Distribution
Systems
Definition
The Water Distribution Systems (WDS) dataset includes information about the primary facilities,
mechanical components, and distribution lines that serve as a delivery system for drinking water.
The WDS dataset includes a delineation of the service area boundary of each water distribution
system. It also contains features of the locations of important mechanical components for the
delivery of drinking water from a drinking water supply source to the curbside valve for
customers in the system. The database contains attributes that describe all or portions of each
component of the system.

Three types of water distribution systems exist for the digital water distribution system
inventory: Type A, Type B, and Type P. Type A systems are generally considered large systems
and are represented in the dataset as a service area with a variety of components. The
components included in Type A systems are: water distribution pipes, groundwater wells, surface
water intakes, water tanks, pumping stations, treatment plants, and master meters.

Type B systems are generally smaller and are represented in the dataset as a service area. Type
B systems will be delineated by boundaries and stored as polygonal features. Pipes and
components are not required for the Type B systems.

Type P systems represent "proposed" expansion areas or "proposed" new systems. Type P
systems will be delineated by boundaries and stored as polygonal features. Pipes and mechanical
components are not included in the mapping for Type P systems.

Type A, B, and P systems are defined as follows:

       Type A Water System
       Water Systems defined as public "Community Water Systems" by the NC Department of
       Environment, Health, and Natural Resources are classified as Type A Water Systems.
       Type A Water Systems are existing systems for provision to the public of piped water for
       human consumption which serve fifteen (15) or more connections or which regularly
       serve at least 25 year-round residents.

       Type B Water System
       Type B Water Systems are existing systems defined as public "Community Water
       Systems", which generally represent small private, mobile home, multi-family housing or
       single subdivision systems and have very limited potential future economic development
       impact.

       Type P Water System
       Type P Water Systems are planned or proposed public community water system service
       areas where public systems do not currently exist and are outside of current service area
       boundaries. Type P system are areas which have been identified as having sufficient

                                                9

       need and population density to support viable public systems and which have an existing
       minimum potential user density of 20 existing potential connections per mile of
       waterline.

The dataset for the water distribution system contains a large amount of descriptive information
about each component and the service area. The descriptive information is contained in attribute
tables that are linked to each geographic feature in the database. The attribute contents of the
water distribution systems geographic dataset are listed in the Attribute Listing for Water
Distribution Systems beginning on page 9. Attribute data field names and domain values are
itemized for the Water Distribution Systems dataset in Table 1 beginning on page 12. Additional
system owner information is stored in a table described in Section 5 on page 38.

Geometric Representation
Water Distribution System (Type A, Type B and P) service areas are to be delineated by
boundaries and in the geometric form of one or more contiguous or non-contiguous polygons.
Type A, B, and P systems will be stored in separate geographic data files. In circumstances
where systems are small and can only be delineated by a point, a polygon is to be generated
using a radius of 50 feet.

Mechanical components of the Water Distribution System - Type A are to be delineated as either
lines or points. Pipelines will be collected and stored as lines in one geographic data file.
Facilities/devices will be collected and stored as points in a separate geographic data file for each
facility/device type.

All geographic data files are to be topological.

Geographic Coordinate System, Datum, and Unit of Measure
The water distribution systems datasets will be geo-referenced using the NC State Plane
Coordinate System (NAD83).

The unit of measurement will be metric or English.

Annotation
Specifications for annotation of facilities and pipes for this dataset are not included in the
standard. All relevant information for each feature is assumed to be recorded as an attribute in
the database. Annotation, if desired, should be considered as an optional specification for
consideration at the time of data collection or maintenance.

Metadata
Metadata, or data about data, are required for each geographic dataset. Beginning January 1995,
all federal organizations involved in the development of geographic data must comply with the
Federal Geographic Data Committee's (FGDC) Content Standards for Digital Geospatial
Metadata. The FGDC Standard has been adopted by the North Carolina Geographic Information
Coordinating Council and is required for all data submitted to the NC OneMap Database. The
Center for Geographic Information and Analysis has implemented the Federal Content Standard
for Digital Geospatial Metadata for all datasets currently in the NC OneMap Database and will

                                                   10

assist in the development of complete metadata for data layers.

Symbology
Graphic symbols of facilities and pipes for this data layer are not included in the standard.
Symbology is considered a product generation standard and not a content issue. However, all
relevant information pertaining to symbology is presumed to be recorded as an attribute in the
database. Symbology should be considered as an optional specification for consideration at the
time of product generation.

Attributes
Physical characteristics and descriptive information about each system and component are
contained within the attribute table of each data file. Geometric features such as polygons, lines,
nodes, and points identify the location or boundary of a feature in the dataset. An attribute or a
set of attributes describe each feature in the dataset. Attribute field names, data type, field
domain, and additional comments are described in Table 1 - Attribute Names, Field Definitions,
and Supplementary Data Definitions for Water Distribution System Features. A list of all
descriptive information for the Water Distribution Systems Dataset follows:

List 1 - Summary of Water Distribution Systems Attribute Fields

Water Distribution Systems - Type A
System Identification Number                         Inter Basin Transfer
Name of System                                       Problems and Needs
Owner Identification Number                          Recommendations
Part Indicator                                       Improvement Cost
Total Parts                                          Expansion Indicator
Water Pressure Zones                                 Maximum Daily Usage - Current Year
Original Construction Year                           Maximum Daily Usage - Plus 10 Years
Description of Service Area                          Maximum Daily Usage - Plus 20 Years
Supply Sources                                       Average Daily Usage - Current Year
Customer Connections - Residential                   Average Daily Usage - Plus 10 Years
Customer Connections - Non-Residential               Average Daily Usage - Plus 20 Years
Customer Connections - Bulk Purchasers               Contact Person
Maximum Daily Usage                                  Contact Telephone
Average Daily Usage                                  Contact Person Email
User Charges - Residential
User Charges - Non-Residential                       Water Distribution System - Type B
User Charges - Bulk Purchasers                       Service Areas
Average Monthly Usage Per Customer -                 System Identification Number
Residential                                          Name of System
Average Monthly Usage Per Customer -                 Population Served
Non-Residential                                      Contact Person
Average Monthly Usage Per Customer -                 Contact Telephone
Bulk Purchasers                                      Contact Person Email

                                                11

Water Distribution System - Type P            Intakes, Surface Water
Service Areas                                 Surface Water Intake - ID
System Identification Number                  Surface Water Intake - Year of Original
Parent ID                                     Installation
New Cost                                      Surface Water Intake - Year of Most Recent
                                              Renovation
Water Distribution System Pipes               Surface Water Intake Flow Capacity
System Identification Number                  Service Status
Original Construction Year                    Date Created in GIS
Renovation Year - Most Recent                 Created By (Person)
Material                                      Date of Last Update
Diameter                                      Edited By (Person)
Elevations                                    Expected Life of Asset
Casing                                        Source of Data
Service Status                                Data Collector
Date Created in GIS                           X Coordinate
Created By (Person)                           Y Coordinate
Date of Last Update                           Z Coordinate
Edited By (Person)                            Picture of Asset
Expected Life of Asset                        Equipment/Device Manufacturer
Source of Data                                Year of Installation
Data Collector
Equipment/Device Manufacturer
Year of Installation

Wells, Groundwater Intakes
Groundwater Intake Well Identification
Number
Original Construction Year
Renovation - Most Recent
Safe Yield
Service Status
Date Created in GIS
Created By (Person)
Date of Last Update
Edited By (Person)
Expected Life of Asset
Source of Data
Data Collector
X Coordinate
Y Coordinate
Z Coordinate
Picture of Asset
Equipment/Device Manufacturer
Year of Installation

                                         12

Water Storage Tanks                              Z Coordinate
Water Storage Tank - ID                          Picture of Asset
Water Storage Tank Location Descriptor           Equipment/Device Manufacturer
Water Storage Tank Year of Original              Year of Installation
Construction
Water Storage Tank Year of Most Recent           Water Treatment Plants
Renovation                                       Water Treatment Plant ID
Water Storage Tank Type                          Water Treatment Plant Year of Original
Water Storage Tank Utilization                   Construction
Water Storage Tank Material                      Water Treatment Plant Year of Most Recent
Water Storage Tank Bottom Elevation              Renovation
Water Storage Tank Overflow Elevation            Water Treatment Plant Permitted Plant
Water Storage Tank Storage Capacity              Capacity
Service Status                                   Water Treatment Plant Maximum Daily
Date Created in GIS                              Production
Created By (Person)                              Water Treatment Plant Average Daily
Date of Last Update                              Production
Edited By (Person)                               Water Treatment Plant Type of Water
Expected Life of Asset                           Treatment Technology
Source of Data                                   Water Treatment Plant Estimated Area
Data Collector                                   Service Status
X Coordinate                                     Date Created in GIS
Y Coordinate                                     Created By (Person)
Z Coordinate                                     Date of Last Update
Picture of Asset                                 Edited By (Person)
Equipment/Device Manufacturer                    Expected Life of Asset
Year of Installation                             Source of Data
                                                 Data Collector
Water Pumping Stations                           X Coordinate
Water Pumping Station ID                         Y Coordinate
Water Pumping Station Location Descriptor        Z Coordinate
Water Pumping Station Year of Original           Picture of Asset
Construction                                     Equipment/Device Manufacturer
Water Pumping Station Year of Most Recent        Year of Installation
Renovation
Water Pumping Station Pumping Capacity
Service Status
Date Created in GIS
Created By (Person)
Date of Last Update
Edited By (Person)
Expected Life of Asset
Source of Data
Data Collector
X Coordinate
Y Coordinate

                                            13

Water Master Meters                               Expected Life of Asset
Master Meter ID                                   Source of Data
Master Meter Year of Original Construction        Data Collector
Master Meter Year of Most Recent                  X Coordinate
Renovation                                        Y Coordinate
Master Meter Size                                 Z Coordinate
Master Meter Maximum Available for                Picture of Asset
Purchase Daily                                    Equipment/Device Manufacturer
InterSystem Connection                            Year of Installation
Service Status                                    Model Name
Date Created in GIS                               Nozzle Size
Created By (Person)                               Nozzle Type
Date of Last Update
Edited By (Person)                                Water Service Meters
Expected Life of Asset                            ID, Service Meter
Source of Data                                    Original Construction Year
Data Collector                                    Renovation – Most Recent
X Coordinate                                      Size of Meter
Y Coordinate                                      Service Account
Z Coordinate                                      Type
Picture of Asset                                  Service Status
Equipment/Device Manufacturer                     Date Created in GIS
Year of Installation                              Created By (Person)
                                                  Date of Last Update
Water Hydrants                                    Edited By (Person)
ID, Hydrant                                       Expected Life of Asset
Original Construction Year                        Source of Data
Renovation – Most Recent                          Data Collector
Static Pressure                                   X Coordinate
Residual Flow                                     Y Coordinate
Service Status                                    Z Coordinate
Date Created in GIS                               Picture of Asset
Created By (Person)                               Equipment/Device Manufacturer
Date of Last Update                               Year of Installation
Edited By (Person)

                                             14

In the following tables, new data fields added in 2011 are indicated by bold font.

Table 1- Definitions of Attribute Fields for Water
Distribution Systems
Water System - Type A -                Boundary of legally defined service area, including additional
                                       areas being served. Exclude outside areas for which service is
(POLYGON                               planned; these are P systems. Exclude area surrounding intake
ATTRIBUTES)                            mains where no customers exist.
Data Field                                            Domain and
                 Attribute (Alias)     Data Type                           Comments
Name                                                  Units
                                                                           Water System Number (retain
WASYID           System ID             Text           7 characters
                                                                           leading zero(s))
WASYNAME         Name of System        Text           50 characters
                                                                           Assign unique number for each
                                                                           within state. Owner ID may be
                                                                           same for both a water and sewer
WSSYOW1          Owner ID (One)        Text           00000 - 99999
                                                                           system. Use supplementary table
                                                                           'TOWNER' for additional
                                                                           information about system owners.
                 Owner ID (Second,                                         Additional Owner ID, if multiple
WSSYOW2                                Text           00000 - 99999
                 if applicable)                                            owners
                 Owner ID (Third,                                          Additional Owner ID, if multiple
WSSYOW3                                Text           00000 - 99999
                 if applicable)                                            owners
                 Owner ID (Fourth,                                         Additional Owner ID, if multiple
WSSYOW4                                Text           00000 - 99999
                 if applicable)                                            owners
                 Owner ID (Fifth, if                                       Additional Owner ID, if multiple
WSSYOW5                                Text           00000 - 99999
                 applicable)                                               owners
                                                                           If the information for any field in
                                                                           polygon attributes has possible
                                                                           multiple values (for different parts
                                                                           of the whole), then the system
WASYPART         Part Indicator        Integer        1,2,3,4,5,6,7,8,or 9
                                                                           must be characterized as separate
                                                                           systems that form parts of the
                                                                           whole and each part makes
                                                                           separate record(s).
                                                                           Total parts in entire system. See
WASYTOPT         Total Parts           Integer        1,2,3,4,5,6,7,8,or 9
                                                                           Part Indicator.
                 Water Pressure
WAPRESZN                               Text                                Names of water pressure zones.
                 Zones
                                                                           Exclusive of pipes. Use closest
                                                                           decade if exact year is unknown
                                                                           (e.g., if the original construction
                 Original                                                  year was sometime between 1965
WASYCSTR                               Integer        4 digits
                 Construction Year                                         and 1970, specify "1970"; likewise
                                                                           if you believe it to be sometime
                                                                           between 1960 and 1964, specify
                                                                           "1960").

                                                 15

Data Field                                       Domain and
             Attribute (Alias)    Data Type                            Comments
Name                                             Units
                                                                       Brief description of extent of
             Description of
WASYDESC                          Text           50 characters         service area. Must cover area for
             Service Area
                                                                       which permit is issued.
                                                                       Brief list of all supply sources by
WASYSUPP     Supply Sources       Text           50 characters
                                                                       name, separated by commas.
                                                                       Number of residential customer
             Customer
                                                                       connections for finished water,
WASYCCR      Connections -        Integer        000000 - 999999
                                                                       most recent June 30th. "0" if none,
             Residential
                                                                       "999999" if unknown.
                                                                       Number of non-residential
             Customer
                                                                       customer connections for finished
WASYCCNR     Connections - Non- Integer          000000 - 999999
                                                                       water, most recent June 30th. "0" if
             Residential
                                                                       none, "999999" if unknown.
                                                                       Number of bulk purchaser
             Customer
                                                                       connections for finished water,
WASYCCBP     Connections - Bulk   Integer        000000 - 999999
                                                                       most recent June 30th. "0" if none,
             Purchasers
                                                                       "999999" if unknown.
                                                                       Maximum daily usage during
                                                 000.000 - 999.999
             Maximum Daily                                             fiscal year ending most recent June
WASYMAXD                          Numeric        millions of gallons
             Usage                                                     30. "0" if none, "999.999" if
                                                 per day
                                                                       unknown.
                                                 000.000 - 999.999     Average daily usage during fiscal
             Average Daily
WASYAVGD                          Numeric        millions of gallons   year ending most recent June 30.
             Usage
                                                 per day               "0" if none, "999.999" if unknown
                                                                       Average monthly charge per
                                                                       customer for fiscal year ending last
                                                                       June 30. Average of 12 months,
             User Charges -                      000.00 - 999.99       each calculated as total monthly
WASYCGR                           Numeric
             Residential                         dollars               charges divided by monthly
                                                                       number of customers. Omit dollar
                                                                       sign. "0" if none, "999.99" if
                                                                       unknown.
                                                                       Average monthly charge per
                                                                       customer for fiscal year ending last
                                                                       June 30. Average of 12 months,
             User Charges -                      9999999.99
WASYCGNR                          Numeric                              each calculated as total monthly
             Non-Residential                     dollars
                                                                       charges divided by monthly
                                                                       number of customers. "0" if none,
                                                                       "9999999.99" if unknown.
                                                                       Average monthly charge per bulk
                                                                       purchaser connection for fiscal
                                                                       year ending last June 30. Average
             User Charges -                      9999999.99            of 12 months, each calculated as
WASYCGBP                          Numeric
             Bulk Purchaser                      dollars               total monthly charges divided by
                                                                       monthly number of bulk purchaser
                                                                       connections. "0" if none,
                                                                       "9999999.99" if unknown.

                                            16

Data Field                                      Domain and
             Attribute (Alias)   Data Type                          Comments
Name                                            Units
                                                                    Average monthly usage per
                                                                    customer for fiscal year ending last
             Average Monthly
                                                                    June 30. Average of 12 months,
             Usage Per                          999999 gallons
WASYAMR                          Integer                            each calculated as total monthly
             Customer -                         per month
                                                                    usage divided by monthly number
             Residential
                                                                    of customers. "0" if none,
                                                                    "999999" if unknown
                                                                    Average monthly usage per
                                                                    customer for fiscal year ending last
             Average Monthly
                                                000000000-          June 30. Average of 12 months,
             Usage Per
WASYAMNR                         Integer        999999999           each calculated as total monthly
             Customer - Non-
                                                gallons per month   usage divided by monthly number
             Residential
                                                                    of customers. "0" if none,
                                                                    "999999999" if unknown
                                                                    Average monthly usage per bulk
                                                                    purchaser connection for fiscal
             Average Monthly                                        year ending last June 30. Average
                                                000000000-
             Usage Per                                              of 12 months, each calculated as
WASYAMBP                         Integer        999999999
             Customer - Bulk                                        total monthly usage divided by
                                                gallons per month
             Purchaser                                              monthly number of bulk purchaser
                                                                    connections. "0" if none,
                                                                    "999999999" if unknown
                                                                    Yes (Y) if there is transfer of water
             Inter-Basin                                            from one water basin to another by
WASYIBTR                         text           Y or N
             Transfer                                               this water distribution system.
                                                                    Otherwise, no (N).
                                                                    Brief narrative documenting
             Problems and                                           current conditions, problems, and
WPRJNEED                         text           254 characters
             Needs                                                  needs, citing compliance with
                                                                    federal standards.
                                                                    Brief narrative listing
WPRJREC      Recommendations     text           254 characters      recommendations for improving
                                                                    the system.
                                                                    Estimated cost in current dollars to
                                                                    implement recommendations for 1)
                                                0000000 -           adding capacity, (2) rehabilitating
                                                9999999             assets, and/or (3) replacing assets
WPRJCOST     Improvement Cost    Integer
                                                thousands of        within current service area
                                                dollars             boundary (excluding any plans for
                                                                    expanding service area
                                                                    boundaries).
                                                                    Yes, if recommend expanding
             Expansion
WPRJEXP                          text           Y or N              current service area boundaries of
             Indicator
                                                                    this system. Otherwise, no.
                                                000.000 - 999.999   Projected maximum daily usage
             Maximum Daily
WPRJMU00                         Numeric        millions of         during fiscal year ending June
             Usage - Current
                                                gallons per day     30, . "999.999" if unknown

                                           17

Data Field                                      Domain and
             Attribute (Alias)   Data Type                          Comments
Name                                            Units
                                                                    Projected maximum daily usage
                                                000.000 - 999.999
             Maximum Daily                                          during fiscal year ending June
WPRJMU10                         Numeric        millions of
             Usage - Plus 10                                        30 plus 10 years. "999.999" if
                                                gallons per day
                                                                    unknown
                                                                    Projected maximum daily usage
                                                000.000 - 999.999
             Maximum Daily                                          during fiscal year ending June
WPRJMU20                         Numeric        millions of
             Usage - Plus 20                                        30 plus 20 years. "999.999" if
                                                gallons per day
                                                                    unknown
                                                000.000 - 999.999   Projected maximum daily usage
             Average Daily
WPRJAU00                         Numeric        millions of         during fiscal year ending June
             Usage - Current
                                                gallons per day     30, "999.999" if unknown
                                                                    Projected maximum daily usage
                                                000.000 - 999.999
             Average Daily                                          during fiscal year ending June
WPRJAU10                         Numeric        millions of
             Usage - Plus 10                                        30 plus 10 years. "999.999" if
                                                gallons per day
                                                                    unknown
                                                                    Projected maximum daily usage
                                                000.000 - 999.999
             Average Daily                                          during fiscal year ending June
WPRJAU20                         Numeric        millions of
             Usage - Plus 20                                        30 plus 20 years. "999.999" if
                                                gallons per day
                                                                    unknown
                                                                    First name and last name, no
WSYCONT      Contact Person      Text           25 characters
                                                                    titles or middle names.
             Contact
WSYPHON                          Text           xxx-xxx-xxxx
             Telephone
             Contact Person
WSEMAIL                          hyperlink                          email address
             Email

Water System - Type B -          All Type B systems will be recorded as polygons, regardless of size.
(POLYGON                         Systems too small to outline should be represented as a circle with a
ATTRIBUTES)                      50 foot radius.
Data Field                                      Domain and
             Attribute (Alias)   Data Type                          Comments
Name                                            Units
WBSYID       System ID           Text           7 characters        Water System Number
WBSYNAME     Name of System      Text           50 characters
                                                000000 - 999999
WBSYPOP      Population Served   Integer                            Estimate if unknown
                                                persons
                                                                    First name and last name, no titles
WBSYCONT     Contact Person      Text           25 characters
                                                                    or middle names.
WBSYPHON     Contact Telephone   Text           xxx-xxx-xxxx
             Contact Person
WSEMAIL                          hyperlink                          email address
             Email

                                           18

                                      Boundary determined by current need and viability. Includes
Water System - Type P -               contiguous areas (outside any current water system service area)
(POLYGON ATTRIBUTES)                  that average at least 20 existing potential connections per linear
                                      highway/street mile. May or may not abut existing system(s).
                                      Data        Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type        Units
                                                                         First digit is a “9”, the next three
                                                                         are county FIPS code (primary
                                                                         county if crosses counties), and
WPSYID            System ID           Text        7 characters           the final three set as desired, to
                                                                         avoid duplicating an existing
                                                                         system ID. Initial “9” indicates
                                                                         "new" or "P" system.
                                                                         ID of parent system, if this is a
                                                                         proposed expansion outside
WPSYPAR           Parent ID           Text        7 characters
                                                                         service area of a current system.
                                                                         Otherwise blank.
                                                                         Cost in current dollars to put
                                                  000000.0 -             proposed system in place.
                                                  999999.9 in            Customer pool for driving cost
WPSYCOST          New Cost            Numeric
                                                  thousands of           estimates is to be derived from
                                                  dollars                projections of population growth
                                                                         rates since 1970.

                                      A new pipe segment is designated each time any pipe attribute
Water Pipes (Line Attributes)         changes. A segment of pipe may include many vertices.

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type           Units
                                                                         Water System Number (retain
WASYID            System ID           Text           7 characters
                                                                         leading zero(s))
                                                                         Use closest decade if exact year is
                                                                         unknown (e.g., if the original
                                                                         construction year was sometime
                  Original                                               between 1965 and 1970, specify
WAPICSTR                              Integer        4 digits
                  Construction Year                                      "1970"; likewise if you believe it
                                                                         to be sometime between 1960 and
                                                                         1964, specify "1960"). "9999" if
                                                                         unknown.
                                                                         Estimate of the year (or decade) of
                                                                         the most recent renovation or
                                                                         renewal, defined as replacement or
                  Renovation or
                                                                         substantial repair / rehabilitation
WAPIRENV          Renewal - Most      Integer        4 digits
                                                                         of at least 400 linear ft. Data
                  Recent
                                                                         management may require
                                                                         additional line segments. "0" if
                                                                         none, "9999" if unknown.

                                                19

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                         Comments
                                      Type           Units
                                                     asbestos cement,
                                                     cast iron, concrete,
                                                     copper, ductile
                                                     iron, galvanized       Material currently in place.
WAPIMATR          Material            Text           steel, polystyrene,    Declare one material type, exactly
                                                     polyvinyl              as shown
                                                     chloride, steel,
                                                     unknown, other.
                                                     25 characters
                                                                            All pipes two (2) inches in
                                                                            diameter and larger must be
WAPIDIAM          Diameter            Integer        00 - 99 inches
                                                                            reported. Smaller diameter pipes
                                                                            may be reported. "99" if unknown.
                                                     Above Ground,
WAPIPELEV         Elevations          Text
                                                     Below Ground
                                                                            Indicator if pipe is within a
WACASE            Casing              Text           Yes, No
                                                                            protective casing
                                                     In Services, Out
                                                                             Note: planned service is ready
                                                     of Service,
                                                                            to be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                            future service is anticipated or
                                                     In Construction,
                                                                            projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                            A domain of person allowed to
                  Created By
CREATBY                               Text                                  edit should be created for this
                  (Person)
                                                                            attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                            A domain of person allowed to
UPDTBY            Edited By (Person) Text                                   edit should be created for this
                                                                            attribute.
                                                                            Number of years that asset is
                  Expected Life of
LIFECYC                               Text                                  expected to be in use before
                  Asset
                                                                            being renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                            Name of person or firm
DATACOLL          Data Collector      Text
                                                                            collecting the field data
                  Equipment/Device
MANUFACT                              Text                                  Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                               Current asset
                  Installation

                                                20

Ground Water Intakes, Wells
(Point Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type           Units
                                                                         First three digits are FIPS county
                                                                         code; next 7 digits are water
                  ID, Groundwater
WAWEID                                Text           13 characters       system ID, last 3 digits are
                  Well
                                                                         assigned to be unique within
                                                                         county.
                                                                         Use closest decade if exact year is
                                                                         unknown (e.g., if the original
                                                                         construction year was sometime
                  Original                                               between 1965 and 1970, specify
WAWECSTR                              Integer        4 digits
                  Construction Year                                      "1970"; likewise if you believe it
                                                                         to be sometime between 1960 and
                                                                         1964, specify "1960"). "9999" if
                                                                         unknown
                                                                         Estimate of the year (or decade) of
                  Renovation - Most
WAWERENV                              Integer        4 digits            the most recent renovation. "0" if
                  Recent
                                                                         none, "9999" if unknown
                                                                         If water is purchased, there may be
                                                     000.000 - 999.999
WAWEYELD          Safe Yield          Numeric                            no well data and no safe yield. "0"
                                                     mgd
                                                                         if none, "999.999" if unknown
                                                     In Services, Out
                                                                         Note: planned service is ready to
                                                     of Service,
                                                                         be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                         future service is anticipated or
                                                     In Construction,
                                                                         projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                         A domain of person allowed to
                  Created By
CREATBY                               Text                               edit should be created for this
                  (Person)
                                                                         attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                         A domain of person allowed to
UPDTBY            Edited By (Person) Text                                edit should be created for this
                                                                         attribute.
                                                                         Number of years that asset is
                  Expected Life of
LIFECYC                               Text                               expected to be in use before
                  Asset
                                                                         being renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                         Name of person or firm
DATACOLL          Data Collector      Text
                                                                         collecting the field data
XCOORD            X coordinate        Double                             GPS collected X Coordinate
YCOORD            Y coordinate        Double                             GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                             GPS collected Z Coordinate

                                                21

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type           Units
ASSETPIC          Picture of Asset    URL                                A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                               Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                            Current asset
                  Installation

Surface Water Intakes (Point
Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type           Units
                                                                         First three digits are FIPS county
                                                                         code; next 7 digits are water
                  ID, Surface Water
WAINID                                Text           13 characters       system ID, last 3 digits are
                  Intakes
                                                                         assigned to be unique within
                                                                         county.
                                                                         Use closest decade if exact year is
                                                                         unknown (e.g., if the original
                                                                         construction year was sometime
                  Original                                               between 1965 and 1970, specify
WAINCSTR                              Integer        4 digits
                  Construction Year                                      "1970"; likewise if you believe it
                                                                         to be sometime between 1960 and
                                                                         1964, specify "1960"). "9999" if
                                                                         unknown
                                                                         Estimate of the year (or decade) of
                  Renovation - Most
WAINRENV                              Integer        4 digits            the most recent renovation. "0" if
                  Recent
                                                                         none, "9999" if unknown
                                                     000.000 - 999.999   7 day/10 year low flow in million
WAINFLOW          Flow Capacity       Numeric
                                                     mgd                 gallons per day
                                                     In Services, Out
                                                                          Note: planned service is ready
                                                     of Service,
                                                                         to be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                         future service is anticipated or
                                                     In Construction,
                                                                         projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                         A domain of person allowed to
                  Created By
CREATBY                               Text                               edit should be created for this
                  (Person)
                                                                         attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                         A domain of person allowed to
UPDTBY            Edited By (Person) Text                                edit should be created for this
                                                                         attribute.
                                                                         Number of years that asset is
                  Expected Life of
LIFECYC                               Text                               expected to be in use before
                  Asset
                                                                         being renewed.

                                                22

                                        Data           Domain and
Data Field Name   Attribute (Alias)                                         Comments
                                        Type           Units
                                                       GPS, Paper
DATASOURCE        Source of Data        Text           Maps, Digital
                                                       Maps
                                                                            Name of person or firm
DATACOLL          Data Collector        Text
                                                                            collecting the field data
XCOORD            X coordinate          Double                              GPS collected X Coordinate
YCOORD            Y coordinate          Double                              GPS collected Y Coordinate
ZCOORD            Z coordinate          Double                              GPS collected Z Coordinate
ASSETPIC          Picture of Asset      URL                                 A link to an image of the asset.
                  Equipment/Device
MANUFACT                                Text                                Current asset
                  Manufacturer
                  Year of
INSTALL_YR                              Integer                             Current asset
                  Installation

Water Storage Tanks (Point
Attributes)
                                        Data           Domain and
Data Field Name   Attribute (Alias)                                         Comments
                                        Type           Units
                                                                            First three digits are FIPS county
                                                                            code; next 7 digits are water
WATKID            ID, Water Tanks       Text           13 characters        system ID, last 3 digits are
                                                                            assigned to be unique within
                                                                            county.
WATKLOC           Location Descriptor   Text           20 characters        Name of area of location.
                                                                            Use closest decade if exact year is
                                                                            unknown (e.g., if the original
                                                                            construction year was sometime
                  Original                                                  between 1965 and 1970, specify
WATKCSTR                                Integer        4 digits
                  Construction Year                                         "1970"; likewise if you believe it
                                                                            to be sometime between 1960 and
                                                                            1964, specify "1960"). "9999" if
                                                                            unknown
                                                                            Estimate of the year (or decade) of
                  Renovation - Most
WATKRENV                                Integer        4 digits             the most recent renovation. "0" if
                  Recent
                                                                            none, "9999" if unknown
                                                       elevated, hydro-
                                                       pneumatic, ground
                                                                            Use one option for type, exactly as
WATKTYPE          Type                  Text           storage, other,
                                                                            shown
                                                       unknown. 25
                                                       characters
                                                       raw water,
                                                                            Use one option for type, exactly as
WATKUTIL          Utilization           Text           finished water. 25
                                                                            shown
                                                       characters

                                                  23

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                        Comments
                                      Type           Units
                                                     metal, concrete,
                                                     pond, lake,
                  Construction                                             Use one option for type, exactly as
WATKMATR                              Text           reservoir, other,
                  Material                                                 shown
                                                     unknown. 15
                                                     characters
                                                     00000.0 - 99999.9
                                                                           "99999.9" if unknown. Use 0.0 if
WATKEBOT          Elevation, Bottom   Numeric        feet above mean
                                                                           WATKTYPE is hydropneumatic.
                                                     sea level
                                                     00000.0 - 99999.9
                  Elevation,                                               “99999.9” if unknown. Use 0.0 if
WATKEOFL                              Numeric        feet above mean
                  Overflow                                                 WATKTYPE is hydropneumatic.
                                                     sea level
                                                     000.000 - 999.999
WATKCPTY          Storage Capacity    Numeric                              “999.999” if unknown
                                                     millions of gallons
                                                     In Services, Out
                                                                            Note: planned service is ready
                                                     of Service,
                                                                           to be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                           future service is anticipated or
                                                     In Construction,
                                                                           projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                           A domain of person allowed to
                  Created By
CREATBY                               Text                                 edit should be created for this
                  (Person)
                                                                           attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                           A domain of person allowed to
UPDTBY            Edited By (Person) Text                                  edit should be created for this
                                                                           attribute.
                                                                           Number of years that asset is
                  Expected Life of
LIFECYC                               Text                                 expected to be in use before
                  Asset
                                                                           being renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                           Name of person or firm
DATACOLL          Data Collector      Text
                                                                           collecting the field data
XCOORD            X coordinate        Double                               GPS collected X Coordinate
YCOORD            Y coordinate        Double                               GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                               GPS collected Z Coordinate
ASSETPIC          Picture of Asset    URL                                  A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                                 Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                              Current asset
                  Installation

                                                24

Water Pumping Stations
(Point Attributes)
                                        Data           Domain and
Data Field Name   Attribute (Alias)                                       Comments
                                        Type           Units
                                                                          First three digits are FIPS county
                                                                          code; next 7 digits are water
                  ID, Pumping
WAPSID                                  Text           13 characters      system ID, last 3 digits are
                  Stations
                                                                          assigned to be unique within
                                                                          county.
WAPSLOC           Location Descriptor   Text           50 characters      Name of area of location.
                                                                          Use closest decade if exact year is
                                                                          unknown (e.g., if the original
                                                                          construction year was sometime
                  Original                                                between 1965 and 1970, specify
WAPSCSTR                                Integer        4 digits
                  Construction Year                                       "1970"; likewise if you believe it
                                                                          to be sometime between 1960 and
                                                                          1964, specify "1960"). "9999" if
                                                                          unknown
                                                                          Estimate of the year (or decade) of
                  Renovation - Most
WAPSRENV                                Integer        4 digits           the most recent renovation. "0" if
                  Recent
                                                                          none, "9999" if unknown
                                                       000000.0 -
WAPSCPTY          Pumping Capacity      Numeric        999999.9 gallons   "999999.9" if unknown
                                                       per minute
                                                       In Services, Out
                                                                           Note: planned service is ready
                                                       of Service,
                                                                          to be funded and put in place;
SERVSTAT          Service Status        Text           Planned, Future,
                                                                          future service is anticipated or
                                                       In Construction,
                                                                          projected without specific plans.
                                                       Abandoned
                  Date Created in
CREATDAT                                Date
                  GIS
                                                                          A domain of person allowed to
                  Created By
CREATBY                                 Text                              edit should be created for this
                  (Person)
                                                                          attribute.
                  Date of Last
UPDTON                                  Date
                  Update
                                                                          A domain of person allowed to
UPDTBY            Edited By (Person) Text                                 edit should be created for this
                                                                          attribute.
                                                                          Number of years that asset is
                  Expected Life of
LIFECYC                                 Text                              expected to be in use before
                  Asset
                                                                          being renewed.
                                                       GPS, Paper
DATASOURCE        Source of Data        Text           Maps, Digital
                                                       Maps
                                                                          Name of person or firm
DATACOLL          Data Collector        Text
                                                                          collecting the field data
XCOORD            X coordinate          Double                            GPS collected X Coordinate
YCOORD            Y coordinate          Double                            GPS collected Y Coordinate

                                                  25

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                        Comments
                                      Type           Units
ZCOORD            Z coordinate        Double                               GPS collected Z Coordinate
ASSETPIC          Picture of Asset    URL                                  A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                                 Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                              Current asset
                  Installation

Water Treatment Plant
(Point Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                        Comments
                                      Type           Units
                                                                           First three digits are FIPS county
                                                                           code; next 7 digits are water
                  ID, Treatment
WATPID                                Text           13 characters         system ID, last 3 digits are
                  Plants
                                                                           assigned to be unique within
                                                                           county.
                                                                           Use closest decade if exact year is
                                                                           unknown (e.g., if the original
                                                                           construction year was sometime
                  Original                                                 between 1965 and 1970, specify
WATPCSTR                              Integer        4 digits
                  Construction Year                                        "1970"; likewise if you believe it
                                                                           to be sometime between 1960 and
                                                                           1964, specify "1960"). "9999" if
                                                                           unknown
                                                                           Estimate of the year (or decade) of
                  Renovation - Most
WATPRENV                              Integer        4 digits              the most recent renovation. "0" if
                  Recent
                                                                           none, "9999" if unknown.
                                                     000.000 - 999.999
                  Permitted Plant
WATPCPTY                              Numeric        millions of gallons   "999.999” if unknown
                  Capacity
                                                     per day
                                                     000.000 - 999.999
                  Maximum Daily
WATPMDP                               Numeric        millions of gallons   “999.999” if unknown
                  Production
                                                     per day
                                                     000.000 - 999.999
                  Average Daily
WATPADP                               Numeric        millions of gallons   “999.999” if unknown
                  Production
                                                     per day

                                                26

                                      Data          Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type          Units
                                                    Ground water w.
                                                    disinfection,
                                                    ground water w.
                                                    reverse osmosis,
                                                    ground water w.
                                                    softener, ground
                                                    water w. iron       Description of treatment type up to
                  Type of Water
                                                    remover, ground     100 characters. Use one or more
WATPTRMT          Treatment           Text
                                                    water w. softener   options, exactly as shown. Also,
                  Technology
                                                    and iron removal,   use "unknown" if unknown.
                                                    surface water w.
                                                    direct filter,
                                                    surface water w.
                                                    coagulation,
                                                    sedimentation and
                                                    filter, other
                                                                        Estimate of area of water
                                                    00000.00 -
WATPAREA          Estimated Area      Numeric                           treatment plant. "99999.99" if
                                                    99999.99 acres
                                                                        unknown.
                                                    In Services, Out
                                                                         Note: planned service is ready
                                                    of Service,
                                                                        to be funded and put in place;
SERVSTAT          Service Status      Text          Planned, Future,
                                                                        future service is anticipated or
                                                    In Construction,
                                                                        projected without specific plans.
                                                    Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
UPDTBY            Edited By (Person) Text                               edit should be created for this
                                                                        attribute.
                                                                        Number of years that asset is
                  Expected Life of
LIFECYC                               Text                              expected to be in use before
                  Asset
                                                                        being renewed.
                                                    GPS, Paper
DATASOURCE        Source of Data      Text          Maps, Digital
                                                    Maps
                                                                        Name of person or firm
DATACOLL          Data Collector      Text
                                                                        collecting the field data
XCOORD            X coordinate        Double                            GPS collected X Coordinate
YCOORD            Y coordinate        Double                            GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                            GPS collected Z Coordinate
ASSETPIC          Picture of Asset    URL                               A link to an image of the asset.

                                               27

                                       Data           Domain and
Data Field Name   Attribute (Alias)                                         Comments
                                       Type           Units
                  Equipment/Device
MANUFACT                               Text                                 Current asset
                  Manufacturer
                  Year of
INSTALL_YR                             Integer                              Current asset
                  Installation

Water Master Meters
(System) (Point Attributes)
                                       Data           Domain and
Data Field Name   Attribute (Alias)                                         Comments
                                       Type           Units
                                                                            First three digits are FIPS county
                                                                            code; next 7 digits are water
WAMMID            ID, Master Meters    Text           13 characters         system ID, last 3 digits are
                                                                            assigned to be unique within
                                                                            county.
                                                                            Use closest decade if exact year is
                                                                            unknown (e.g., if the original
                                                                            construction year was sometime
                  Original                                                  between 1965 and 1970, specify
WAMMCSTR                               Integer        4 digits
                  Construction Year                                         "1970"; likewise if you believe it
                                                                            to be sometime between 1960 and
                                                                            1964, specify "1960"). "9999" if
                                                                            unknown.
                                                                            Estimate of the year (or decade) of
                  Renovation - Most
WAMMRENV                               Integer        4 digits              the most recent renovation. "0" if
                  Recent
                                                                            none, "9999" if unknown.
WAMMSIZE          Size                 Integer        00-99 inches
                                                      000.000 - 999.999     Maximum daily amount of water
                  Max. Available for
WAMMMAAV                               Numeric        million gallons per   available for purchase at this meter
                  Purchase, Daily
                                                      day                   site. "999.999” if unknown.
                                                                            System to which connection is
                                                                            being made. First three digits
                  InterSystem                                               are FIPS county code; next 7
WAMMCON                                Text           13 characters
                  Connection                                                digits are water system ID, last 3
                                                                            digits are assigned to be unique
                                                                            within county.
                                                      In Services, Out
                                                                             Note: planned service is ready
                                                      of Service,
                                                                            to be funded and put in place;
SERVSTAT          Service Status       Text           Planned, Future,
                                                                            future service is anticipated or
                                                      In Construction,
                                                                            projected without specific plans.
                                                      Abandoned
                  Date Created in
CREATDAT                               Date
                  GIS
                                                                            A domain of person allowed to
                  Created By
CREATBY                                Text                                 edit should be created for this
                  (Person)
                                                                            attribute.

                                                 28

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units
                  Date of Last
UPDTON                                Date
                  Update
                                                                     A domain of person allowed to
UPDTBY            Edited By (Person) Text                            edit should be created for this
                                                                     attribute.
                                                                     Number of years that asset is
                  Expected Life of
LIFECYC                               Text                           expected to be in use before
                  Asset
                                                                     being renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                     Name of person or firm
DATACOLL          Data Collector      Text
                                                                     collecting the field data
XCOORD            X coordinate        Double                         GPS collected X Coordinate
YCOORD            Y coordinate        Double                         GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                         GPS collected Z Coordinate
ASSETPIC          Picture of Asset    URL                            A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                           Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                        Current asset
                  Installation

Water Hydrants (Point
Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units
                                                                     First three digits are FIPS
                                                                     county code; next 7 digits are
WAHYID            ID, Hydrant         Text           15 characters   water system ID, last 5 digits are
                                                                     assigned to be unique within
                                                                     county.
                                                                     Use closest decade if exact year
                                                                     is unknown (e.g., if the original
                                                                     construction year was sometime
                  Original                                           between 1965 and 1970, specify
WAHYCSTR                              Date           4 digits
                  Construction Year                                  "1970"; likewise if you believe it
                                                                     to be sometime between 1960
                                                                     and 1964, specify "1960").
                                                                     "9999" if unknown.
                                                                     Estimate of the year (or decade)
                  Renovation - Most
WAHYRENV                              Date           4 digits        of the most recent renovation.
                  Recent
                                                                     "0" if none, "9999" if unknown.
                                                                     Static Pressure as measured at
WAHYSTATIC        Static Pressure     Integer
                                                                     Hydrant
                                                                     Residual Flow as measured at
WAHYRESID         Residual Flow
                                                                     Hydrant

                                                29

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type           Units
                                                     In Services, Out
                                                                         Note: planned service is ready
                                                     of Service,
                                                                        to be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        future service is anticipated or
                                                     In Construction,
                                                                        projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
UPDTBY            Edited By (Person) Text                               edit should be created for this
                                                                        attribute.
                                                                        Number of years that asset is
                  Expected Life of
LIFECYC                               Text                              expected to be in use before
                  Asset
                                                                        being renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                        Name of person or firm
DATACOLL          Data Collector      Text
                                                                        collecting the field data
XCOORD            X coordinate        Double                            GPS collected X Coordinate
YCOORD            Y coordinate        Double                            GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                            GPS collected Z Coordinate
ASSETPIC          Picture of Asset    URL                               A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                              Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                           Current asset
                  Installation

                                                30

Water Service Meters (Point
Attributes)
                                                                    First three digits are FIPS
                                                                    county code; next 7 digits are
WASMID        ID, Service Meter   Text           25 characters      water system ID, last 15 digits
                                                                    are assigned to be unique within
                                                                    county.
                                                                    Use closest decade if exact year
                                                                    is unknown (e.g., if the original
                                                                    construction year was sometime
              Original                                              between 1965 and 1970, specify
WASMCSTR                          Date           4 digits
              Construction Year                                     "1970"; likewise if you believe it
                                                                    to be sometime between 1960
                                                                    and 1964, specify "1960").
                                                                    "9999" if unknown.
                                                                    Estimate of the year (or decade)
              Renovation - Most
WASMRENV                          Date           4 digits           of the most recent renovation.
              Recent
                                                                    "0" if none, "9999" if unknown.
WASMSIZE      Size of Meter       Integer                           Size of meter service.
                                                                    Service Account from billing
                                  Text /
WASMACCT      Service Account                                       data base associated with
                                  Integer
                                                                    Service meter
                                                 Residential,
                                                 Commercial,        Type of service meter is
WASMTYPE      Type                Text
                                                 Industrial,        providing.
                                                 Irrigation
                                                 In Services, Out
                                                                     Note: planned service is ready
                                                 of Service,
                                                                    to be funded and put in place;
SERVSTAT      Service Status      Text           Planned, Future,
                                                                    future service is anticipated or
                                                 In Construction,
                                                                    projected without specific plans.
                                                 Abandoned
              Date Created in
CREATDAT                          Date
              GIS
                                                                    A domain of person allowed to
              Created By
CREATBY                           Text                              edit should be created for this
              (Person)
                                                                    attribute.
              Date of Last
UPDTON                            Date
              Update
                                                                    A domain of person allowed to
UPDTBY        Edited By (Person) Text                               edit should be created for this
                                                                    attribute.
                                                                    Number of years that asset is
              Expected Life of
LIFECYC                           Text                              expected to be in use before
              Asset
                                                                    being renewed.
                                                 GPS, Paper
DATASOURCE    Source of Data      Text           Maps, Digital
                                                 Maps
                                                                    Name of person or firm
DATACOLL      Data Collector      Text
                                                                    collecting the field data

                                            31

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type           Units
XCOORD            X coordinate        Double                            GPS collected X Coordinate
YCOORD            Y coordinate        Double                            GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                            GPS collected Z Coordinate
ASSETPIC          Picture of Asset    URL                               A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                              Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                           Current asset
                  Installation

Water Valves (Point
Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type           Units
                                                                        First three digits are FIPS
                                                                        county code; next 7 digits are
WAWVALID          ID, Water Valve     Text           25 characters      water system ID, last 15 digits
                                                                        are assigned to be unique within
                                                                        county.
                                                                        Use closest decade if exact year
                                                                        is unknown (e.g., if the original
                                                                        construction year was sometime
                  Original                                              between 1965 and 1970, specify
WAWVACSTR                             Date           4 digits
                  Construction Year                                     "1970"; likewise if you believe it
                                                                        to be sometime between 1960
                                                                        and 1964, specify "1960").
                                                                        "9999" if unknown.

                                                                        Estimate of the year (or decade)
                  Renovation - Most
WAWVARENV                             Date           4 digits           of the most recent renovation.
                  Recent
                                                                        "0" if none, "9999" if unknown.

                                                     In Services, Out
                                                                         Note: planned service is ready
                                                     of Service,
                                                                        to be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        future service is anticipated or
                                                     In Construction,
                                                                        projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.

                                                32

                                      Data           Domain and
Data Field Name Attribute (Alias)                                    Comments
                                      Type           Units
                  Date of Last
UPDATON                               Date
                  Update
                                                                     A domain of person allowed to
                  Edited By
UPDATBY                               Text                           edit should be created for this
                  (Person)
                                                                     attribute.
                                                                     Number of years that asset is
                  Expected Life of
LIFECYC                               Text                           expected to be in use before
                  Asset
                                                                     being renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                     Name of person or firm
DATACOLL          Data Collector      Text
                                                                     collecting the field data.

XCOORD            X coordinate        Double                         GPS collected X Coordinate

YCOORD            Y coordinate        Double                         GPS collected Y Coordinate

ZCOORD            Z coordinate        Double                         GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                            A link to an image of the asset.
                  Equipment/Device
MANUFACT                              Text                           Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                        Current asset
                  Installation
ASSETNAME         Name of the Asset   Text

VALVETYPE         Type of Valve       Text

                                                33

SECTION 4: Content Standard - Sanitary Sewer Systems
Definition
The Sanitary Sewer Systems (SSS) dataset includes information about the primary facilities,
mechanical components, and collection lines that function as a discharge and treatment system
for sewerage. The SSS dataset includes a delineation of the service area boundary of each
sanitary sewer system. It also contains features of the locations of important mechanical
components for the delivery and treatment of sewerage from the curbside connection point to the
site where treated sewerage is released back into the natural environment. The database contains
attributes that describe all or portions of each component of the system.

Three types of sanitary sewer systems exist for the digital sanitary sewer system inventory: Type
A, Type B, and Type P. Type A systems are generally considered large systems and are
represented in the dataset by a service area with a variety of system components. The
components included in Type A systems are: sewer pipes, pumping stations, treatment plants,
discharges, and land application areas.

Type B systems are generally smaller and are represented in the dataset as a service area. Type
B systems will be delineated by boundaries and stored as polygonal features. Pipes and
components are not required for the Type B systems.

Type P systems represent "proposed" expansion areas or "proposed" new systems. Type P
systems will be delineated by boundaries and stored as polygonal features. Pipes and mechanical
components are not included in the mapping for Type P systems.

Type A, B, and P systems are defined as follows:

       Type A Sewerage Systems
       Existing community sanitary sewer systems including collection lines, transport lines or
       pumping and treatment facilities which serve the general public and accept domestic
       wastewater are classified as Type A Sewerage Systems.

       Type B Sewerage Systems
       Type B Sewerage Systems are existing community sanitary sewer systems which serve
       the general public and accept domestic wastewater, but generally represent small, private,
       business, industrial, mobile home, multi-family housing or single subdivision systems
       which have very limited potential future economic development impact.

       Type P Sewerage Systems
       Type P Sewerage Systems are planned or proposed public community sanitary sewer
       system service areas, outside of current service area boundaries, where public systems do
       not currently exist. Type P systems are areas which have been identified as having
       sufficient need and population density to support viable public systems and which have
       an existing minimum potential user density of 40 existing potential connections per mile
       of wastewater collection line.

                                               34

The dataset for the sanitary sewer system contains a large amount of descriptive information
about each component and the service area. The descriptive information is contained in attribute
tables that are linked to each geographic feature in the database. The attribute contents of the
sanitary sewer systems geographic dataset are listed in the Attribute Listing for Sanitary Sewer
System beginning on page 26. Attribute data field names and domain values are itemized for the
Sanitary Sewer System dataset in Table 2 beginning on page 28. Additional system owner
information is stored in a table described in Section 5 on page 38.

Geometric Representation
Sanitary Sewer Systems (Type A, Type B and Type P) service areas are to be delineated by
boundaries and in the geometric form of one or more contiguous or non-contiguous polygons.
Type A, B, and P systems will be stored in separate geographic data files. In circumstances
where systems are small and can only be delineated by a point, a polygon is to be generated
using a radius of 50 feet.

Mechanical components of the Sanitary Sewer System - Type A are to be delineated as either
lines or points. Pipelines will be collected and stored as lines in one geographic data file.
Facilities/devices will be collected and stored as points in a separate geographic data file for each
facility/device type.

All geographic data files will be topological.

Geographic Coordinate System, Datum, and Unit of Measurement
The sanitary sewer systems data sets will be geo-referenced using the NC State Plane Coordinate
System (NAD83).
The unit of measurement will be metric or English.

Annotation
Specifications for annotation of facilities and pipes for this dataset are not included in the
standard. All relevant information for each feature is assumed to be recorded as an attribute in
the database. Annotation, if desired, should be considered as an optional specification for
consideration at the time of data collection or modification.

Metadata
Metadata, or data about data, are required for each geographic dataset. Beginning January 1995,
all federal organizations involved in the development of geographic data must comply with the
Federal Geographic Data Committee's (FGDC) Content Standards for Digital Geospatial
Metadata. The FGDC Standard has been adopted by the North Carolina Geographic Information
Coordinating Council and is now required for all data submitted to the NC OneMap Database.
The Center for Geographic Information & Analysis has implemented the Federal Content
Standard for Digital Geospatial Metadata for all datasets currently in the NC OneMap Database
and will assist in the development of complete metadata for corporate data layers.

Symbology
Graphic symbols of facilities and pipes for this data layer are not included in the standard.
Symbology is considered as a product generation standard and not a content issue. However, all
relevant information pertaining to symbology is presumed to be recorded as an attribute in the
                                                 35

database. Symbology should be treated as an optional specification for consideration at the time
of product generation.

Attributes
Physical characteristics and descriptive information about components are contained within the
attribute table of each data set. Polygons, lines, areas, nodes, and points identify the location or
boundary of a feature in the dataset. An attribute or a set of attributes describe each feature in
the dataset. Attribute field names, data type, field domain, and additional comments are
described in Table 2 - Attribute Names, Field Definitions, and Supplementary Data Definitions
for Sanitary Sewer System Features. A list of all descriptive information for the Sanitary Sewer
Systems Dataset follows:

List 2 - Summary of Sanitary Sewer Systems Attribute Fields
Sanitary Sewer System - Type A                        Average Daily Flow Plus 10 Years
System Identification Number                          Average Daily Flow Plus 20 Years
Name of System                                        Contact Person
Owner Identification Number                           Contact Telephone
Part Indicator                                        Contact Person Email
Total Parts
Original Construction Year                            Sanitary Sewer System - Type B Service
Description of Service Area                           Areas
Customer Connections - Residential                    System Identification Number
Customer Connections - Non-Residential                Name of System
Customer Connections - Bulk Purchaser                 Population Served
Maximum Daily Flow                                    Contact Person
Average Daily Flow                                    Contact Telephone
User Charges - Residential                            Contact Person Email
User Charges - Non-Residential
User Charges - Bulk Purchasers                        Sanitary Sewer System - Type P Service
Average Monthly Flow Per Customer -                   Areas
Residential                                           System Identification Number
Average Monthly Flow Per Customer - Non-              Parent System ID
Residential                                           New Cost
Average Monthly Flow Per Customer - Bulk
Purchaser                                             Land Application Areas
Inter Basin Transfer Amount                           Land Application Area - ID
Problems and Needs                                    Land Application Area Year of Original
Recommendations                                       Construction
Improvement Cost                                      Land Application Area Year of Most Recent
Expansion Indicator                                   Renovation
Maximum Daily Flow Current Year                       Land Application Area - Permit Expiration
Maximum Daily Flow Plus 10 Years                      Date
Maximum Daily Flow Plus 20 Years                      Land Application Area - Estimated Area
Average Daily Flow Current Year

                                                 36

Sanitary Sewer System Pipes                     Treatment Plants
System Identification Number                    Treatment Plant - ID
Original Construction Year                      Treatment Plant Location Descriptor
Renovation Year - Most Recent                   Treatment Plant Year of Original
Material                                        Installation
Diameter                                        Treatment Plant Year of Most Recent
Type - Pressure, Gravity, Vacuum                Renovation
Utilization Type - Interceptor, Outfall,        Treatment Plant Permitted Flow Capacity
Collection                                      Treatment Plant Maximum Daily Flow
Elevations                                      Treatment Plant Average Daily Flow
Slope                                           Treatment Plant Type of Treatment
Casing                                          Technology
Service Status                                  Treatment Plant Sludge Disposal
Date Created in GIS                             Technology
Created By (Person)                             Treatment Plant Infiltration/Inflow
Date of Last Update                             Treatment Plant Estimated Area
Edited By (Person)                              Service Status
Expected Life of Asset                          Date Created in GIS
Source of Data                                  Created By (Person)
Data Collector                                  Date of Last Update
Equipment/Device Manufacturer                   Edited By (Person)
Year of Installation                            Expected Life of Asset
                                                Source of Data
Pumping Stations                                Data Collector
Pumping Station - ID                            X Coordinate
Pumping Station Location Descriptor             Y Coordinate
Pumping Station Year of Original                Z Coordinate
Construction                                    Picture of Asset
Pumping Station Year of Most Recent             Equipment/Device Manufacturer
Renovation                                      Year of Installation
Pumping Station Capacity
Service Status
Date Created in GIS
Created By (Person)
Date of Last Update
Edited By (Person)
Expected Life of Asset
Source of Data
Data Collector
X Coordinate
Y Coordinate
Z Coordinate
Picture of Asset
Equipment/Device Manufacturer
Year of Installation

                                           37

Discharge Points
Discharge -ID                                   Sewer Valves
Discharge Location Descriptor                   ID, Valve
Discharge Year of Original Construction         Location Descriptor
Discharge Year of Most Recent Renovation        Original Construction Year
Service Status                                  Renovation – Most Recent
Date Created in GIS                             Pipe Connection
Created By (Person)                             Service Status
Date of Last Update                             Date Created in GIS
Edited By (Person)                              Created By (Person)
Expected Life of Asset                          Date of Last Update
Source of Data                                  Edited By (Person)
Data Collector                                  Expected Life of Asset
X Coordinate                                    Source of Data
Y Coordinate                                    Data Collector
Z Coordinate                                    X Coordinate
Picture of Asset                                Y Coordinate
Equipment/Device Manufacturer                   Z Coordinate
Year of Installation                            Picture of Asset
                                                Equipment/Device Manufacturer
Sewer Manholes                                  Year of Installation
ID, Manhole
Location Descriptor                             Sewer Cleanouts
Original Construction Year                      ID, Cleanout
Renovation – Most Recent                        Location Descriptor
Top Elevation                                   Original Construction Year
Invert Out                                      Renovation – Most Recent
Invert 1                                        Pipe Connection
Invert 2                                        Service Status
Invert 3                                        Date Created in GIS
Service Status                                  Created By (Person)
Date Created in GIS                             Date of Last Update
Created By (Person)                             Edited By (Person)
Date of Last Update                             Expected Life of Asset
Edited By (Person)                              Source of Data
Expected Life of Asset                          Data Collector
Source of Data                                  X Coordinate
Data Collector                                  Y Coordinate
X Coordinate                                    Z Coordinate
Y Coordinate                                    Picture of Asset
Z Coordinate                                    Equipment/Device Manufacturer
Picture of Asset                                Year of Installation
Equipment/Device Manufacturer
Year of Installation

                                           38

Sewer Stream Crossings
ID, Crossing
Location Descriptor
Original Construction Year
Renovation – Most Recent
Name of Stream
Service Status
Date Created in GIS
Created By (Person)
Date of Last Update
Edited By (Person)
Expected Life of Asset
Source of Data
Data Collector
X Coordinate
Y Coordinate
Z Coordinate
Picture of Asset
Equipment/Device Manufacturer
Year of Installation

                                39

In the following tables, data fields added in 2011 are indicated by bold font.

Table 2 - Definitions of Attribute Fields for Sanitary Sewer
Systems
                                         Boundary of legally defined service area, including additional
Sanitary Sewer System - Type areas being served. Exclude outside areas for which service is
A (Polygon Attribute)        planned; these are P systems. Exclude area surrounding intake
                                         mains where no customers exist.

                                         Data           Domain and
Data Field Name    Attribute (Alias)                                          Comments
                                         Type           Units
                                                                              First three digits are FIPS county
                                                                              code (primary co. of location), next
                                                                              4 digits are unique identifier. Note:
                                                                              cannot use permit number for
                                                                              discharge due to multiple
SSSYID             System ID             Text           7 characters          discharges.
SSSYNAME           Name of System        Text           50 characters
                                                                              Assign unique number for each
                                                                              within state. Owner ID may be
                                                                              same for both a water and sewer
                                                                              system. Use supplementary table
                                                                              'TOWNER' for additional
SSSYOW1            Owner ID (One)        Text           00000 - 99999         information about system owners.
                   Owner ID (Second,                                          Additional Owner ID, if multiple
SSSYOW2            if applicable)        Text           00000 - 99999         owners.
                   Owner ID (Third, if                                        Additional Owner ID, if multiple
SSSYOW3            applicable)           Text           00000 - 99999         owners.
                   Owner ID (Fourth,                                          Additional Owner ID, if multiple
SSSYOW4            if applicable)        Text           00000 - 99999         owners.
                   Owner ID (Fifth, if                                        Additional Owner ID, if multiple
SSSYOW5            applicable)           Text           00000 - 99999         owners.
                                                                              If the information for any field in
                                                                              polygon attributes table has possible
                                                                              multiple values (for different parts
                                                                              of the whole), then the system must
                                                                              be characterized as separate systems
                                                        1,2,3,4,5,6,7,8, or   that form parts of the whole and
SSSYPART           Part Indicator        Integer        9                     each part makes separate record(s).
                                                        1,2,3,4,5,6,7,8, or   Total parts in entire system. See
SSSYTOPT           Total Parts           Integer        9                     Part Indicator.

                                                   40

                                       Data           Domain and
Data Field Name   Attribute (Alias)                                         Comments
                                       Type           Units
                                                                            Exclusive of pipes. Use closest
                                                                            decade if exact year is unknown
                                                                            (e.g., if the original construction
                                                                            year was sometime between 1965
                  Original                                                  and 1970, specify "1970"). "9999"
SSSYCSTR          Construction Year    Integer        4 digits              if unknown.
                                                                            Brief description of service area.
                  Description of                                            Must cover area for which permit is
SSSYDESC          Service Area         Text           50 characters         issued.
                                                                            Number of residential customer
                  Customer                                                  connections for sanitary sewer,
                  Connections -                                             most recent June 30th. "0" if none,
SSSYCCR           Residential          Integer        000000 - 999999       "999999" if unknown.
                                                                            Number of non-residential customer
                  Customer                                                  connections for sanitary sewer,
                  Connections - Non-                                        most recent June 30th. "0" if none,
SSSYCCNR          Residential          Integer        000000 - 999999       "999999" if unknown.
                                                                            Number of bulk purchaser
                  Customer                                                  connections for sanitary sewer,
                  Connections - Bulk                                        most recent June 30th. "0" if none,
SSSYCCBP          Purchasers           Integer        00000 - 99999         "99999" if unknown.
                                                      000.000 - 999.999     Maximum daily flow during fiscal
                  Maximum Daily                       millions of gallons   year ending most recent June 30.
SSSYMAXF          Flow                 Numeric        per day               "999.999" if unknown.
                                                      000.000 - 999.999     Average daily flow during fiscal
                  Average Daily                       millions of gallons   year ending most recent June 30.
SSSYADGD          Flow                 Numeric        per day               "999.999" if unknown.
                                                                            Average monthly charge per
                                                                            customer for fiscal year ending last
                                                                            June 30. Average of 12 months,
                                                                            each calculated as total monthly
                                                                            charges divided by monthly number
                  User Charges -                      000.00 - 999.99       of customers. "0" if none, "999.99"
SSSYCGR           Residential          Numeric        dollars               if unknown.
                                                                            Average monthly charge per
                                                                            customer for fiscal year ending last
                                                                            June 30. Average of 12 months,
                                                                            each calculated as total monthly
                                                                            charges divided by monthly number
                  User Charges -                      0.00 - 9999999.99     of customers. "0" if none,
SSSYCGNR          Non-Residential      Numeric        dollars               "9999999.99" if unknown.

                                                 41

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type           Units
                                                                         Average monthly charge per bulk
                                                                         purchaser connection for fiscal year
                                                                         ending last June 30. Average of 12
                                                                         months, each calculated as total
                                                                         monthly charges divided by
                                                                         monthly number of bulk purchaser
                  User Charges -                     0.00 - 9999999.99   connections. "0" if none,
SSSYCGBP          Bulk Purchasers     Numeric        dollars             "9999999.99 if unknown.
                                                                         Average monthly usage per
                                                                         customer for fiscal year ending last
                                                                         June 30. Average of 12 months,
                                                                         each calculated as total monthly
                  Average Monthly                                        Flow divided by monthly number of
                  Flow Per Customer                  999999 gallons      customers. "0" if none, "999999" if
SSSYAMR           - Residential       Integer        per month           unknown.
                                                                         Average monthly flow per customer
                                                                         for fiscal year ending last June 30.
                                                                         Average of 12 months, each
                                                                         calculated as total monthly Flow
                  Average Monthly                                        divided by monthly number of
                  Flow Per Customer                  999999999           customers. "0" if none,
SSSYAMNR          - Non-Residential   Integer        gallons per month   "999999999" if unknown.
                                                                         Average monthly flow per bulk
                                                                         purchaser connection for fiscal year
                                                                         ending last June 30. Average of 12
                                                                         months, each calculated as total
                                                                         monthly Flow divided by monthly
                  Average Monthly                                        number of bulk purchaser
                  Flow Per Customer                  999999999           connections. "0" if none,
SSSYAMBP          - Bulk Purchasers   Integer        gallons per month   "999999999" if unknown.
                                                                         Yes(Y) if there is transfer of
                                                                         wastewater or processed wastewater
                                                                         from one water basin to another by
                  Inter-Basin                                            this sanitary sewer system.
SSSYIBTR          Transfer            Text           Y or N              Otherwise, no (N).
                                                                         Brief narrative documenting current
                                                                         conditions, problems, and needs,
                  Problems and                                           citing compliance with federal
SPRJNEED          Needs               Text           254 characters      standards.
                                                                         Brief narrative listing
                                                                         recommendations for improving the
SPRJREC           Recommendations     Text           254 characters      system.

                                                42

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                      Comments
                                      Type           Units
                                                                         Estimated cost in current dollars to
                                                                         implement recommendations for
                                                                         improving the system including
                                                     0000000 -           expansion within current service
                                                     9999999             area boundary (excluding any plans
                                                     thousands of        for expanding service area
SPRJCOST          Improvement Cost    Integer        dollars             boundaries).
                                                                         Yes, if recommend expanding
                                                                         current service area boundaries of
SPRJEXP           Expansion Indicator Text           Y or N              this system. Otherwise, no.
                                                     000.000 - 999.999   Projected maximum daily usage
                  Maximum Daily
                                                     millions of         during fiscal year ending June 30,
                  Flow - Current
SPRJMF00                              Numeric        gallons per day     "999.999" if unknown.
                                                                         Projected maximum daily usage
                  Maximum Daily
                                                     000.000 - 999.999   during fiscal year ending June 30
                  Flow - Plus 10
                                                     millions of         plus 10 years. "999.999" if
                  Years
SPRJMF10                              Numeric        gallons per day     unknown.
                                                                         Projected maximum daily usage
                  Maximum Daily
                                                     000.000 - 999.999   during fiscal year ending June 30
                  Flow - Plus 20
                                                     millions of         plus 20 years. "999.999" if
                  Years
SPRJMF20                              Numeric        gallons per day     unknown.
                                                     000.000 - 999.999   Projected maximum daily usage
                  Average Daily
                                                     millions of         during fiscal year ending June 30,
                  Flow - Current
SPRJAF00                              Numeric        gallons per day     "999.999" if unknown.
                                                                         Projected maximum daily usage
                  Average Daily
                                                     000.000 - 999.999   during fiscal year ending June 30
                  Flow - Plus 10
                                                     millions of         plus 10 years. "999.999" if
                  Years
SPRJAF10                              Numeric        gallons per day     unknown.
                                                                         Projected maximum daily usage
                  Average Daily
                                                     000.000 - 999.999   during fiscal year ending June 30
                  Flow - Plus 20
                                                     millions of         plus 20 years. "999.999" if
                  Years
SPRJAF20                              Numeric        gallons per day     unknown.
                                                                         First name and last name, no
SSYCONT           Contact Person      Text           25 characters
                                                                         titles or middle names.
SSYPHON           Contact Telephone Text             xxx-xxx-xxxx
                  Contact Person    hyperlin
SSEMAIL                                                                  email address
                  Email             k

                                                43

Sanitary Sewer System - Type All type B systems will be recorded as polygons, regardless of
                             size. Systems too small to outline should be represented as a
B (Polygon Attribute)        circle with a 50 foot radius.
                                                      Domain and
Data Field Name   Attribute (Alias)   Data Type                         Comments
                                                      Units
                                                                        First three digits are FIPS county
                                                                        code (primary co. of location), next
SBSYID            System ID           Text            7 characters      4 digits are unique identifier.
SBSYNAME          Name of System      Text            50 characters
                                                      000000 - 999999   If unknown, provide best estimate
SBSYPOP           Population Served   Integer         persons           of population.
                                                                        First name and last name, no titles
SBSYCONT          Contact Person      Text            25 characters     or middle names.
SBSYPHON          Contact Telephone   Text            xxx-xxx-xxxx
                  Contact Person
SBSEMAIL          Email               hyperlink                         email address

                             Boundary determined by current need and viability. Includes
Sanitary Sewer System - Type contiguous  areas (outside any current sewer system service
                             area) that average at least 40 existing potential connections per
P (Polygon Attribute)        linear highway/street mile. May or may not abut existing
                             system(s).
                                      Data
Data Field Name   Attribute (Alias)                  Domain and Units Comments
                                      Type
                                                                        First digit is a “9”, the next three
                                                                        are county FIPS code, and the final
                                                                        three set as desired, to avoid
                                                                        duplicating an existing system ID.
                                                                        Initial “9” indicates "new" or "P"
SPSYID            System ID           Text           7 characters       system.
                                                                        ID of parent system, if this is a
                                                                        proposed expansion outside service
                                                                        area of a current system. Otherwise
SPSYPAR           Parent ID           Text           7 characters       blank.
                                                                        Cost in current dollars to put
                                                     000000.0 -         proposed system in place. Customer
                                                     999999.9 in        pool for driving cost estimates is to
                                                     thousands of       be derived from projections of
SPSYCOST          New Cost            Numeric        dollars            population growth rates since 1970.

                                                44

Land Application Areas
(Polygon Attribute)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                    Comments
                                      Type           Units

                                                                       Nine digits: seven digit Land
                  ID, Land
SSTPLAID                              Text           11 characters     Application Number (exclude 'WQ')
                  Application Areas
                                                                       and two digits for unique identifier.
                                                                       Use closest decade if exact year is
                                                                       unknown (e.g., if the original
                                                                       construction year was sometime
                  Original                                             between 1965 and 1970, specify
SSLACSTR                              Integer        4 digits
                  Construction Year                                    "1970"; likewise if you believe it to
                                                                       be sometime between 1960 and
                                                                       1964, specify "1960"). "9999" if
                                                                       unknown.
                                                                       Estimate of the year (or decade) of
                  Renovation - Most
SSLARENV                              Integer        4 digits          the most recent renovation. "0" if
                  Recent
                                                                       none, "9999" if unknown.
                  Permit Expiration
SSLADATE                              Date           YYMMDD
                  Date
                                                     000000.00 -       Estimate of area. "999999.99" if
SSLAAREA          Estimated Area      Numeric
                                                     999999.99 acres   unknown.

                                                45

                                       A new pipe segment is designated each time any pipe attribute
Sewer Pipes (Line Attribute)
                                       changes. A segment of pipe may include many vertices.

                                       Data           Domain and
Data Field Name    Attribute (Alias)                                        Comments
                                       Type           Units
                                                                            First three digits are FIPS county
                                                                            code (primary co. of location), next
                                                                            4 digits are unique identifier. Note:
SSSYID             System ID           Text           7 characters
                                                                            cannot use permit number for
                                                                            discharge due to multiple
                                                                            discharges.

                                                                            Use closest decade if exact year is
                                                                            unknown (e.g., if the original
                                                                            construction year was sometime
                   Original                                                 between 1965 and 1970, specify
SSPICSTR                               Integer        4 digits
                   Construction Year                                        "1970"; likewise if you believe it to
                                                                            be sometime between 1960 and
                                                                            1964, specify "1960"). "9999" if
                                                                            unknown.

                                                                            Estimate of the year (or decade) of
                   Renovation - Most
SSPIRENV                               Integer        4 digits              the most recent renovation. "0" if
                   Recent
                                                                            none, "9999" if unknown.
                                                      ABS, asbestos
                                                      cement, brick, cast
                                                      iron, concrete,
                                                      corrugated metal,
                                                      ductile iron,
                                                      fiberglass,
                                                                            Material currently in place. Declare
SSPIMATR           Material            Text           galvanized steel,
                                                                            one type, exactly as shown.
                                                      polystyrene,
                                                      polyvinyl
                                                      chloride, steel,
                                                      vitrified clay,
                                                      unknown,
                                                      other.25.
                                                                            For gravity systems, all interceptors
                                                                            and forced mains must be reported,
                                                                            as well as all collection lines 8 in.
                                                                            and larger. For low pressure and
SSPIDIAM           Diameter            Integer        00 - 99 inches
                                                                            other systems, all lines 2 in. and
                                                                            greater must be reported. Smaller
                                                                            pipes may be reported. "99" if
                                                                            unknown.
                                                      pressure, gravity,
                   Type - Pressure,                   vacuum, other,        Negative pressure implies a
SSPITYPGV                              Text
                   Gravity, Vacuum                    unknown. 15           vacuum.
                                                      characters.

                                                 46

                                          Data           Domain and
Data Field Name   Attribute (Alias)                                             Comments
                                          Type           Units
                                                         interceptor,
                  Utilization Type -
                                                         outfall, collection,
SSTYIOC           Interceptor, Outfall,   Text                                  State one option, exactly as shown.
                                                         other, unknown.
                  Collection
                                                         15 characters.
                                                         Above Ground,
SSPIPELEV         Elevations              Text
                                                         Below Ground
SSSLOPE           Slope                   Integer                               Slope of Sewer Line
                                                                                Indicator if pipe is within a
SSCASE            Casing                  Text           Yes, No
                                                                                protective casing
                                                         In Services, Out
                                                                                 Note: planned service is ready to
                                                         of Service,
                                                                                be funded and put in place; future
SERVSTAT          Service Status          Text           Planned, Future,
                                                                                service is anticipated or projected
                                                         In Construction,
                                                                                without specific plans.
                                                         Abandoned
                  Date Created in
CREATDAT                                  Date
                  GIS
                                                                                A domain of person allowed to
                  Created By
CREATBY                                   Text                                  edit should be created for this
                  (Person)
                                                                                attribute.
                  Date of Last
UPDTON                                    Date
                  Update
                                                                                A domain of person allowed to
                  Edited By
UPDTBY                                    Text                                  edit should be created for this
                  (Person)
                                                                                attribute.
                                                                                Number of years that asset is
                  Expected Life of
LIFECYC                                   Text                                  expected to be in use without
                  Asset
                                                                                repair.
                                                         GPS, Paper
DATASOURCE        Source of Data          Text           Maps, Digital
                                                         Maps
                                                                                Name of person or firm collecting
DATACOLL          Data Collector          Text
                                                                                the field data
                  Equipment/Device
MANUFACT                                  Text                                  Current asset
                  Manufacturer
                  Year of
INSTALL_YR                                Integer                               Current asset
                  Installation

                                                    47

Sewer Pumping Stations
(Point Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                       Comments
                                      Type           Units

                                                                          First 7 digits are same as those of
                                                                          sewer system ID, last 4 digits are
                  ID, Pumping
SSPSID                                Text           11 characters        unique identifying code within
                  Station
                                                                          system. Note fewer digits in last
                                                                          segment may be practical.

                  Location
SSPSLOC                               Text           30 characters        Name of area of location.
                  Descriptor

                                                                          Use closest decade if exact year is
                                                                          unknown (e.g., if the original
                                                                          construction year was sometime
                  Original                                                between 1965 and 1970, specify
SSPSCSTR                              Integer        4 digits
                  Construction Year                                       "1970"; likewise if you believe it to
                                                                          be sometime between 1960 and
                                                                          1964, specify "1960"). "9999" if
                                                                          unknown.

                                                                          Estimate of the year (or decade) of
                  Renovation - Most
SSPSRENV                              Integer        4 digits             the most recent renovation. "0" if
                  Recent
                                                                          none, "9999" if unknown.

                                                     000000 - 999999
SSPSCPTY          Capacity            Integer                             "999999" if unknown.
                                                     gallons per minute
                                                     In Services, Out
                                                                           Note: planned service is ready to
                                                     of Service,
                                                                          be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                          future service is anticipated or
                                                     In Construction,
                                                                          projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                          A domain of person allowed to
                  Created By
CREATBY                               Text                                edit should be created for this
                  (Person)
                                                                          attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                          A domain of person allowed to
                  Edited By
UPDTBY                                Text                                edit should be created for this
                  (Person)
                                                                          attribute.

                                                48

                                        Data           Domain and
Data Field Name   Attribute (Alias)                                    Comments
                                        Type           Units

                                                                       Number of years that asset is
                  Expected Life of
LIFECYC                                 Text                           expected to be in use before being
                  Asset
                                                                       renewed.
                                                       GPS, Paper
DATASOURCE        Source of Data        Text           Maps, Digital
                                                       Maps
                                                                       Name of person or firm collecting
DATACOLL          Data Collector        Text
                                                                       the field data.
XCOORD            X coordinate          Double                         GPS collected X Coordinate
YCOORD            Y coordinate          Double                         GPS collected Y Coordinate
ZCOORD            Z coordinate          Double                         GPS collected Z Coordinate

ASSETPIC          Picture of Asset      URL                            A link to an image of the asset.

                  Equipment/Device
MANUFACT                                Text                           Current asset
                  Manufacturer
                  Year of
INSTALL_YR                              Integer                        Current asset
                  Installation

Sewer Treatment Plant
(Point Attributes)
                                        Data           Domain and
Data Field Name   Attribute (Alias)                                    Comments
                                        Type           Units

                                                                       National Pollutant Discharge
                                                                       Elimination System Identification
SSTPID            ID, Treatment Plant   Text           7 characters    Number assigned by NC Div. of
                                                                       Environmental Management
                                                                       (Exclude "NC").
                  Location
SSTPLOC                                 Text           20 characters   Name of area of location.
                  Descriptor

                                                                       Use closest decade if exact year is
                                                                       unknown (e.g., if the original
                                                                       construction year was sometime
                  Original                                             between 1965 and 1970, specify
SSTPCSTR                                Integer        4 digits
                  Construction Year                                    "1970"; likewise if you believe it to
                                                                       be sometime between 1960 and
                                                                       1964, specify "1960"). "9999" if
                                                                       unknown.

                                                  49

                                        Data           Domain and
Data Field Name   Attribute (Alias)                                          Comments
                                        Type           Units

                                                                             Estimate of the year (or decade) of
                  Renovation - Most
SSTPRENV                                Integer        4 digits              the most recent renovation. "0" if
                  Recent
                                                                             none. "9999" if unknown.

                  Permitted Flow                       00000.0 - 999.999     7 day, 10 year low flow. "999.999"
SSTPCPTY                                Numeric
                  Capacity                             mgd                   if unknown.
                  Maximum Daily                        000.000 - 999.999
SSTPMDPR                                Numeric                              “999.999” if unknown.
                  Flow                                 mgd
                  Average Daily                        000.000 - 999.999
SSTPADPR                                Numeric                              “999.999” if unknown.
                  Flow                                 mgd
                                                       Stabilization
                                                       lagoon, secondary
                                                       treatment,
                                                       advanced
                                                       secondary
                                                       treatment, tertiary
                                                       treatment,
                                                       secondary             State one or more options, exactly
                  Type of Treatment
SSTPTRMT                                Text           treatment plus        as shown. Also use "unknown" if
                  Technology
                                                       nutrient removal,     unknown.
                                                       tertiary treatment
                                                       plus nutrient
                                                       removal, land
                                                       application,
                                                       created wetlands,
                                                       rapid infiltration,
                                                       other. 100 chars.

                  Sludge Disposal                                            Brief, free text to describe sludge
SSTPSLUD                                Text           50 characters
                  Technology                                                 disposal treatment and handling.

                                                       000.000 - 999.999     Estimate of system-wide maximum
SSTPINFT          Infiltration/Inflow   Numeric        millions of gallons   daily infiltration/inflow measured at
                                                       per day               the plant. "999.999” if unknown.

                                                                             Estimate of total area (excluding
                                                       000000.00 -
SSTPAREA          Estimated Area        Numeric                              land application area extent).
                                                       999999.99 acres
                                                                             "999999.99" if unknown.

                                                       In Services, Out
                                                                              Note: planned service is ready to
                                                       of Service,
                                                                             be funded and put in place; future
SERVSTAT          Service Status        Text           Planned, Future,
                                                                             service is anticipated or projected
                                                       In Construction,
                                                                             without specific plans.
                                                       Abandoned

                                                  50

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                     A domain of person allowed to
                  Created By
CREATBY                               Text                           edit should be created for this
                  (Person)
                                                                     attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                     A domain of person allowed to
                  Edited By
UPDTBY                                Text                           edit should be created for this
                  (Person)
                                                                     attribute.
                                                                     Number of years that asset is
                  Expected Life of
LIFECYC                               Text                           expected to be in use before being
                  Asset
                                                                     renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                     Name of person or firm collecting
DATACOLL          Data Collector      Text
                                                                     the field data.
XCOORD            X coordinate        Double                         GPS collected X Coordinate
YCOORD            Y coordinate        Double                         GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                         GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                            A link to an image of the asset.

                  Equipment/Device
MANUFACT                              Text                           Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                        Current asset
                  Installation

                                                51

Sewer Discharge Outlets
(Point Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type           Units

                                                                        7 digits from the Treatment Plant ID
                                                                        (National Pollutant Discharge
SSTPDCID          ID, Discharges      Text           10 characters      Elimination System Identification
                                                                        Number) and the 3 digit outfall
                                                                        code.

                                                                        Name of area of location. Include
                  Location
SSDCLOC                               Text           30 characters      name of stream in location
                  Descriptor
                                                                        descriptor.

                                                                        Use closest decade if exact year is
                                                                        unknown (e.g., if the original
                                                                        construction year was sometime
                  Original                                              between 1965 and 1970, specify
SSDCCSTR                              Integer        4 digits
                  Construction Year                                     "1970"; likewise if you believe it to
                                                                        be sometime between 1960 and
                                                                        1964, specify "1960"). "9999" if
                                                                        unknown.

                                                                        Estimate of the year (or decade) of
                  Renovation - Most
SSDCRENV                              Integer        4 digits           the most recent renovation. "0" if
                  Recent
                                                                        none, "9999" if unknown.

                                                     In Services, Out
                                                                         Note: planned service is ready to
                                                     of Service,
                                                                        be funded and put in place; future
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        service is anticipated or projected
                                                     In Construction,
                                                                        without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
                  Edited By
UPDTBY                                Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                                                                        Number of years that asset is
                  Expected Life of
LIFECYC                               Text                              expected to be in use before being
                  Asset
                                                                        renewed.

                                                52

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                     Name of person or firm collecting
DATACOLL          Data Collector      Text
                                                                     the field data.
XCOORD            X coordinate        Double                         GPS collected X Coordinate
YCOORD            Y coordinate        Double                         GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                         GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                            A link to an image of the asset.

                  Equipment/Device
MANUFACT                              Text                           Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                        Current asset
                  Installation

Sewer Manholes (Point
Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units

                                                                     First 7 digits are same as those of
                                                                     sewer system ID, last 4 digits are
SSMHID            ID, Manhole         Text           11 characters   unique identifying code within
                                                                     system. Note fewer digits in last
                                                                     segment may be practical.

                                                                     Name of area of location. Include
                  Location
SSMHLOC                               Text           30 characters   name of stream in location
                  Descriptor
                                                                     descriptor.

                                                                     Use closest decade if exact year is
                                                                     unknown (e.g., if the original
                                                                     construction year was sometime
                  Original                                           between 1965 and 1970, specify
SSMHCSTR                              Integer        4 digits
                  Construction Year                                  "1970"; likewise if you believe it
                                                                     to be sometime between 1960 and
                                                                     1964, specify "1960"). "9999" if
                                                                     unknown.

                                                53

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type           Units

                                                                        Estimate of the year (or decade)
                  Renovation - Most
SSMHRENV                              Integer        4 digits           of the most recent renovation. "0"
                  Recent
                                                                        if none, "9999" if unknown.

SSMHTOP           Top Elevation       Double                            Top of Rim Elevation.
SSMHOUT           Invert Out          Double                            Elevation of Invert Out
                                                                        Elevation of Invert 1 going
SSMHINVERT1       Invert 1            Double
                                                                        Clockwise from North.
                                                                        Elevation of Invert 2 going
SSMHINVERT2       Invert 2            Double
                                                                        Clockwise from North.
                                                                        Elevation of Invert 3 going
SSMHINVERT3       Invert 3            Double
                                                                        Clockwise from North.
                                                     In Services, Out
                                                                         Note: planned service is ready to
                                                     of Service,
                                                                        be funded and put in place; future
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        service is anticipated or projected
                                                     In Construction,
                                                                        without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
                  Edited By
UPDTBY                                Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                                                                        Number of years that asset is
                  Expected Life of
LIFECYC                               Text                              expected to be in use before being
                  Asset
                                                                        renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                        Name of person or firm collecting
DATACOLL          Data Collector      Text
                                                                        the field data.
XCOORD            X coordinate        Double                            GPS collected X Coordinate
YCOORD            Y coordinate        Double                            GPS collected Y Coordinate

                                                54

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units
ZCOORD            Z coordinate        Double                         GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                            A link to an image of the asset.

                  Equipment/Device
MANUFACT                              Text                           Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                        Current asset
                  Installation

Sewer Valves (Point
Attributes)
                                      Data           Domain and
Data Field Name   Attribute (Alias)                                  Comments
                                      Type           Units

                                                                     First 7 digits are same as those of
                                                                     sewer system ID, last 4 digits are
                  ID, Valve (or
SSVID                                 Text           11 characters   unique identifying code within
                  fitting)
                                                                     system. Note fewer digits in last
                                                                     segment may be practical.

                                                                     Name of area of location. Include
                  Location
SSVLOC                                Text           30 characters   name of stream in location
                  Descriptor
                                                                     descriptor.

                                                                     Use closest decade if exact year is
                                                                     unknown (e.g., if the original
                                                                     construction year was sometime
                  Original                                           between 1965 and 1970, specify
SSVCSTR                               Integer        4 digits
                  Construction Year                                  "1970"; likewise if you believe it
                                                                     to be sometime between 1960 and
                                                                     1964, specify "1960"). "9999" if
                                                                     unknown.

                                                                     Estimate of the year (or decade)
                  Renovation - Most
SSVRENV                               Integer        4 digits        of the most recent renovation. "0"
                  Recent
                                                                     if none, "9999" if unknown.

                                                                     Sewer Pipe (force) to which valve
SSVPIPE           Pipe Connection     Text
                                                                     is connected.

                                                55

                                      Data           Domain and
Data Field Name   Attribute (Alias)                                     Comments
                                      Type           Units
                                                     In Services, Out
                                                                         Note: planned service is ready to
                                                     of Service,
                                                                        be funded and put in place;
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        future service is anticipated or
                                                     In Construction,
                                                                        projected without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
                  Edited By
UPDTBY                                Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                                                                        Number of years that asset is
                  Expected Life of
LIFECYC                               Text                              expected to be in use before being
                  Asset
                                                                        renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                        Name of person or firm collecting
DATACOLL          Data Collector      Text
                                                                        the field data
XCOORD            X coordinate        Double                            GPS collected X Coordinate
YCOORD            Y coordinate        Double                            GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                            GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                               A link to an image of the asset.

                  Equipment/Device
MANUFACT                              Text                              Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                           Current asset
                  Installation

                                                56

Sewer Cleanouts (Point
Attributes)
                                      Data
Data Field Name   Attribute (Alias)                  Domain and Units Comments
                                      Type

                                                                        First 7 digits are same as those of
                                                                        sewer system ID, last 4 digits are
SSCOID            ID, Cleanout        Text           11 characters      unique identifying code within
                                                                        system. Note fewer digits in last
                                                                        segment may be practical.

                                                                        Name of area of location. Include
                  Location
SSCOLOC                               Text           30 characters      name of stream in location
                  Descriptor
                                                                        descriptor.

                                                                        Use closest decade if exact year is
                                                                        unknown (e.g., if the original
                                                                        construction year was sometime
                  Original                                              between 1965 and 1970, specify
SSCOCSTR                              Integer        4 digits
                  Construction Year                                     "1970"; likewise if you believe it
                                                                        to be sometime between 1960 and
                                                                        1964, specify "1960"). "9999" if
                                                                        unknown.

                                                                        Estimate of the year (or decade)
                  Renovation - Most
SSCORENV                              Integer        4 digits           of the most recent renovation. "0"
                  Recent
                                                                        if none, "9999" if unknown.

                                                                        Sewer Pipe (force) to which valve
SSCOPIPE          Pipe Connection     Text
                                                                        is connected.
                                                     In Services, Out
                                                                         Note: planned service is ready to
                                                     of Service,
                                                                        be funded and put in place; future
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        service is anticipated or projected
                                                     In Construction,
                                                                        without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
                  Edited By
UPDTBY                                Text                              edit should be created for this
                  (Person)
                                                                        attribute.

                                                57

                                      Data
Data Field Name   Attribute (Alias)                  Domain and Units Comments
                                      Type

                                                                     Number of years that asset is
                  Expected Life of
LIFECYC                               Text                           expected to be in use before being
                  Asset
                                                                     renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                     Name of person or firm collecting
DATACOLL          Data Collector      Text
                                                                     the field data
XCOORD            X coordinate        Double                         GPS collected X Coordinate
YCOORD            Y coordinate        Double                         GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                         GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                            A link to an image of the asset.

                  Equipment/Device
MANUFACT                              Text                            Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                         Current asset
                  Installation

Sewer Stream Crossings
(Point Attributes)
                                      Data
Data Field Name   Attribute (Alias)                  Domain and Units Comments
                                      Type
                                                                     First 7 digits are same as those of
                                                                     sewer system ID, last 4 digits are
SSSTRID           ID, Crossing        Text           11 characters   unique identifying code within
                                                                     system. Note fewer digits in last
                                                                     segment may be practical.
                                                                     Name of area of location. Include
                  Location
SSSTRLOC                              Text           30 characters   name of stream in location
                  Descriptor
                                                                     descriptor.

                                                                     Use closest decade if exact year is
                                                                     unknown (e.g., if the original
                                                                     construction year was sometime
                  Original                                           between 1965 and 1970, specify
SSSTRCSTR                             Integer        4 digits
                  Construction Year                                  "1970"; likewise if you believe it
                                                                     to be sometime between 1960 and
                                                                     1964, specify "1960"). "9999" if
                                                                     unknown.

                                                58

                                      Data
Data Field Name   Attribute (Alias)                  Domain and Units Comments
                                      Type
                                                                        Estimate of the year (or decade)
                  Renovation - Most
SSSTRRENV                             Integer        4 digits           of the most recent renovation. "0"
                  Recent
                                                                        if none, "9999" if unknown
                                                                        Names of Stream that sewer
SSSTRNAME         Name of Stream      Text
                                                                        crosses.
                                                     In Services, Out
                                                                         Note: planned service is ready to
                                                     of Service,
                                                                        be funded and put in place; future
SERVSTAT          Service Status      Text           Planned, Future,
                                                                        service is anticipated or projected
                                                     In Construction,
                                                                        without specific plans.
                                                     Abandoned
                  Date Created in
CREATDAT                              Date
                  GIS
                                                                        A domain of person allowed to
                  Created By
CREATBY                               Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                  Date of Last
UPDTON                                Date
                  Update
                                                                        A domain of person allowed to
                  Edited By
UPDTBY                                Text                              edit should be created for this
                  (Person)
                                                                        attribute.
                                                                        Number of years that asset is
                  Expected Life of
LIFECYC                               Text                              expected to be in use before being
                  Asset
                                                                        renewed.
                                                     GPS, Paper
DATASOURCE        Source of Data      Text           Maps, Digital
                                                     Maps
                                                                        Name of person or firm collecting
DATACOLL          Data Collector      Text
                                                                        the field data.
XCOORD            X coordinate        Double                            GPS collected X Coordinate
YCOORD            Y coordinate        Double                            GPS collected Y Coordinate
ZCOORD            Z coordinate        Double                            GPS collected Z Coordinate

ASSETPIC          Picture of Asset    URL                               A link to an image of the asset.

                  Equipment/Device
MANUFACT                              Text                              Current asset
                  Manufacturer
                  Year of
INSTALL_YR                            Integer                           Current asset
                  Installation

                                                59

SECTION 5: Content Standard - Supplementary Owner Information
Additional Information about Water Distribution and Sewer System Owners are stored as a data
table in the dataset. The data is linked to the systems data files through the owner identification
number.

List 3 - Supplementary System Owner Information

Owner ID
Owner Name
Owner Type
County of Owner
Bond Rating, NC Municipal Council
Capital Improvement Plan Availability
Cash Reserves
Outstanding Indebtedness - Water
Outstanding Indebtedness - Sewer

                                                 60

Table 3- Definitions of Attribute Fields for Owners
Supplemental Table:
TOWNER
                                      Data
Data Field Name   Attribute (Alias)               Domain and Units Comments
                                      Type

                                                                      Assign unique numbers
WSSYOWID          Owner ID            Text        00000 - 99999
                                                                      statewide.
                                                                      Assign unique numbers
WSSYOWNM          Owner Name          Text        50 characters       statewide. May have same owner
                                                                      ID for a water and sewer system.
                                                  town, city,
                                                  county, water
                                                  dst, sewer dst,
                                                  wat & sew dst,
                                                  metro wat dst,
                                                  metro sew dst,
                                                  metro wat&sew
                                                  dst, wat auth,
                                                  sew auth,
WSSYOWTP          Owner Type          Text                            Also use "unknown" if unknown.
                                                  wat&sew auth,
                                                  sanitary dst,
                                                  state, fed, non-
                                                  profit, profit
                                                  corp, private,
                                                  special purpose
                                                  dst, home owner
                                                  assoc., other. 50
                                                  chars.
                                                                      FIPS Code. County of Business
WSCOFIPS          County of Owner     Text        001 - 199
                                                                      Address of System Owner.
                                                  000 - 100, or
                                                  "NR" for No         Use North Carolina Municipal
                  Bond Rating, NC
                                                  Rating, or          Council, Inc. Ratings of
WSSYOWRA          Municipal           Text
                                                  "NSR" for Not       Counties, Cities, and Towns.
                  Council
                                                  Subject to          Latest Available Publication.
                                                  Rating.
                  Capital
WSSYOWCI          Improvement         Text        Y or N
                  Plan Availability

                                             61

                                      Data
Data Field Name   Attribute (Alias)               Domain and Units Comments
                                      Type
                                                  0000000.0 -
                                                  9999999.9       Based on latest audit. Omit
WSSYOWCR          Cash Reserves       Numeric
                                                  thousands of    dollar sign.
                                                  dollars
                                                  0000000.0 -
                  Outstanding
                                                  9999999.9       Based on latest audit. Omit
WSSYOWIW          Indebtedness -      Numeric
                                                  thousands of    dollar sign.
                  Water
                                                  dollars
                                                  0000000.0 -
                  Outstanding
                                                  9999999.9       Based on latest audit. Omit
WSSYOWIS          Indebtedness -      Numeric
                                                  thousands of    dollar sign.
                  Sewer
                                                  dollars

                                             62

Glossary
Component
Any natural or man-made entity that is a categorical part of a water distribution or a sanitary
sewer system. Examples of components may include water tanks, sewer pipes, and fire hydrants.

Discharge Point
The location where treated wastewater is released into a receiving stream or body of water.

Feature
The unique segment or part of a system that is spatially represented by a geometric figure, such
as a polygon, line, point, or node.

Wells, Ground Water Intake
The location at which raw water is drawn into the water system from an underground source.

Hydrant
An upright pipe with a nozzle or spout for drawing water from a water main.

Intake, Surface Water
The location at which raw water is drawn into the water system from a surface water source.

Land Application Area
An area on which treated wastewater or sludge is applied to be absorbed into the soil.

Manhole
A chamber built upon a sewer line to facilitate inspection and cleaning.

Master Meter
A device generally used to measure the volume of water flow to bulk purchasers whereby the
water is intended for resale to users within the purchaser's system.

Sanitary Sewer Pumping Station
Any device or facility used to force wastewater from one elevation or location to another within
a wastewater system.

Sanitary Sewer System
All facilities used to collect, treat, pump, and dispose of sewerage. The boundaries comprising
the sanitary sewer system may or may not be coincident with the water distribution system.

Sanitary Sewer System - Type A
Existing community sanitary sewer systems including collection lines, transport lines or pumping
and treatment facilities which serve the general public and accept domestic wastewater are
classified as Type A Sewerage Systems.

                                                63

Sanitary Sewer System - Type B
Type B Sewerage Systems are existing community sanitary sewer systems which serve the
general public and accept domestic wastewater, but generally represent small, private, business,
industrial, mobile home, multi-family housing or single subdivision systems which have very
limited potential future economic development impact.

Sanitary Sewer System - Type P
Type P Sewerage Systems are planned or proposed public community sanitary sewer system
service areas, outside of current service area boundaries, where public systems do not currently
exist. Type P systems are areas which have been identified as having sufficient need and
population density to support viable public systems and which have an existing minimum
potential user density of 40 existing potential connections per mile of wastewater collection line.

Sanitary Sewer Treatment Plant
A facility used to treat wastewater and the related appurtenant works.

Sewer Cleanout
A small chamber, not intended for a person, usually located on a system line (such as a lateral)
for cleaning purposes.

Sewer Pipe
A pipe that is used to carry wastewater from one location in the system to another.

Sewer Stream Crossing
The location where a sewer pipe crosses a stream.

Sewer Valve
A movable device by which the flow of wastewater is started, stopped, or regulated.

Water Pipe
A pipe that is used to carry water from one location to another in a water supply or distribution
system.

Water Distribution System
All facilities used to supply, treat, store, and distribute water. The boundaries comprising the
water system may or may not be coincident with the Sanitary Sewer System.

Water Distribution System - Type A
Water Systems defined as public "Community Water Systems" by the NC Department of
Environment, Health, and Natural Resources are classified as Type A Water Systems. Type A
Water Systems are existing systems for provision to the public of piped water for human
consumption which serve fifteen (15) or more connections or which regularly serve at least 25
year- round residents.

Water Distribution System - Type B
Type B Water Systems are existing systems defined as public "Community Water Systems",

                                                64

which generally represent small private, mobile home, multi-family housing or single
subdivision systems and have very limited potential future economic development impact.

Water Distribution System - Type P
Type P Water Systems are planned or proposed public community water system service areas
where public systems do not currently exist and are outside of current service area boundaries.
Type P system are areas which have been identified as having sufficient need and population
density to support viable public systems and which have an existing minimum potential user
density of 20 existing potential connections per mile of waterline.

Water Pumping Station
A device or facility used to force water from one elevation or location to another within the
water supply or distribution system.

Water Service Meter
A device that measures the flow of water to a customer for billing purposes.

Water Storage Tank
A natural or manmade facility where water is stored for the water system.

Water Treatment Plant
A facility where raw water is treated and purified for human consumption.

                                                65

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
