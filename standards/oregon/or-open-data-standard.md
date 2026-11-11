---
schema_version: 1
corpus: states-government-it
jurisdiction: oregon
id: or-open-data-standard
title: Oregon's Open Data Standard
doc_type: standard
citation: Oregon's Open Data Standard (2021)
authority_level: ''
issuing_body: Enterprise Information Services
source_url: https://data.oregon.gov/api/views/ewk6-d856/files/f1e5e94c-324f-4508-9e71-4e5bb278a3b3?download=true&filename=Final%20Open%20Data%20Standard%2020210128.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 23bf7d53f0387c340f0b85e173ca1ef56b1b015253b8e68fd13bfa29bda3ac9b
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

# Oregon's Open Data Standard (Oregon's Open Data Standard (2021))

## At a glance

Requirements for agencies publishing open data under ORS 276A.350-276A.374. Listed under Statewide Standards on the EIS policy page; the page there links the data.oregon.gov asset, whose PDF is the file at this URL (asset ewk6-d856, file named 'Final Open Data Standard 20210128.pdf').

## Full text

                        2021

Oregon’s Open Data
Standard
GUIDANCE FOR AGENCIES

CONTENTS

Background .................................................................................................................................................................2
        Version notes .....................................................................................................................................................2
        Why open data?.................................................................................................................................................3
    Requirements of the Open Data Standard.............................................................................................................4
        Open Data timeline ............................................................................................................................................4
    Open Data Governance ..........................................................................................................................................5
        Appointing a Data Coordinator..........................................................................................................................5
    Inventorying Data...................................................................................................................................................7
        Methods .............................................................................................................................................................7
        Identifying publishable data ..............................................................................................................................8
        Inventory, then prioritize ...................................................................................................................................8
    Prioritizing Data for Release...................................................................................................................................8
    Planning for Open Data Release ............................................................................................................................9
        Identify commitments from prioritized datasets ..............................................................................................9
        Identify open data phase ................................................................................................................................ 10
        Write agency open data plan.......................................................................................................................... 10
    Publishing Data ................................................................................................................................................... 10
    Guidance for Geospatial Data Publishers ........................................................................................................... 11
        Publishing Spatial Data ................................................................................................................................... 11
        Publishing Geospatial Data as Open Data ...................................................................................................... 12
    Glossary ............................................................................................................................................................... 13
    Resources and Credits ......................................................................................................................................... 16

BACKGROUND

In 2017, the Oregon Legislature passed House Bill 3361, now codified as ORS 276A.350-374, establishing the
Chief Data Officer position and creating several mandates around state agencies’ management, use, and sharing
of data. This statute requires that state agencies identify data used within agency information systems,
contribute this information to an enterprise data inventory maintained by the Chief Data Officer, and that
agencies publish data defined as “publishable” under the Statute to a centralized open data portal. These
requirements comprise the State of Oregon’s first Open Data Program.

The Open Data Standard provides requirements of ORS 276A.350-374 for State Agencies to maintain an
inventory of agency datasets, identify publishable data, and publish data to a central web portal. This standard
outlines the expectations of state agencies and Data Coordinators in identifying, prioritizing, and publishing
open data to the State’s Open Data Portal. Direct guidance for Data Coordinators in how to build open data
programs that meet the requirements of the Open Data Standard are available in the Data Coordinator’s
Handbook.

VERSION NOTES

 DATE                    VERSION           DESCRIPTION OF CHANGES
 November 2, 2020        1.0               Soft launch of the Open Data Standard for public review
 February 1, 2021        1.0               Final version of State Open Data Standard released
                                           Updates include: adding exemption process for
                                           medium/small agencies for inventory timeline, clarifying
                                           language

WHY OPEN DATA?
Open data, defined as “data that can be freely used, modified
and shared by anyone for any purpose,” 1 has increased in
                                                                     Open Data Requires:
popularity and use throughout the last decade. Open Data is
available at no direct cost and is made publicly accessible to a     ∗ Availability and access: data must be
variety of users including other state agencies and employees,         available in a machine readable,
Oregonians, non-profit organizations, and any individual with          convenient form
an interest in accessing, downloading, and using data. Open          ∗ Re-use and Redistribution: data must
data provides transparency and accountability for state                be provided under licenses and terms
agencies, and creates an opportunity for communication and             that permit re-use and redistribution
relationship building with our constituents and engaged public.      ∗ Universal Participation: everyone
The State of Oregon publishes open data through two specific           must be able to use and share open
portals, data.oregon.gov, the State’s Open Data Portal, and            data
ArcGIS Online, the State’s data portal for geospatial data assets
such as map layers. The release of open data provides many
benefits to state agencies, including:

     •    Improving data sharing amongst agencies. Publishing open data allows our government partners as well
          as other state agencies to download and re-use datasets without requiring the agency to provide data
          through a separate process. Agencies can leverage the publication of open data to provide continual
          access to publishable data and decrease the number of sharing requests received from other agencies.
     •    Improving data quality and governance. The process of inventorying and releasing open data
          empowers agencies to review their current data assets, assess their quality, and ensure that governance
          mechanisms are in place for agency data. By inventorying high-value and enterprise data assets,
          agencies have completed an important first step in establishing data governance.
     •    Decreasing volume of public records requests and increasing transparency. Publishing open data can
          decrease the volume of public records requests an agency receives by pro-actively releasing data that is
          of high interest to constituents or is frequently requested through the public records process. The State
          of Texas has estimated a cost savings of $5.7million through self-service access to open data in lieu of
          public records requests. 2
     •    Enabling growth and innovation. Open data is built upon community and civic engagement and
          innovative development. The release of open data can help promote the development of new
          applications and technologies or stimulate new sectors within Oregon. California has used water quality
          data to host a Water Challenge to design applications and perform evaluations around water quality,
          accessibility, safety, and rate setting for water.

1 https://opendefinition.org/
2 Email from Ed Kelly, Chief Data Officer of Texas

      •      Fostering active constituent engagement. Open data provides greater constituent access to data assets
             created within state agencies, allowing the state to be proactively transparent while simultaneously
             empowering constituents to use data to learn more about government functions and services.

REQUIREMENTS OF THE OPEN DATA STANDARD

The open data process for the State of Oregon is comprised of the five phases identified below. Agencies shall
appoint an Agency Data Coordinator who will be responsible for the agency’s completion of each deliverable
associated with the five phases of the open data process.

          Agencies
                                                                                                                           Agencies
          appoint an Data                                             Agencies
                                                                                                                           publish data
          Coordinator for                                             prioritize               Agencies write
                                                                                                                           based upon
          their Open Data              Agencies                       datasets for             and share their
                                                                                                                           committments
Appoint

                                                         Prioritize
                            Identify

          Program                                                     publication              Open Data Plan

                                                                                                                 Publish
                                       inventory their                                                                     in their Open
          Deliverable:                 high-value and                 Deliverable:             Deliverable:

                                                                                        Plan
                                                                                                                           Data Plan
          Data                         enterprise                     Agency data              Submit Open
                                       datasets                                                                            Deliverable:
          Coordinator                                                 inventory                Data Plan to
                                                                                                                           Agencies
          Appointment                                                 submitted to             CDO
                                                                                                                           publish open
          notice to Chief                                             CDO
                                                                                                                           data
          Data Office

OPEN DATA TIMELINE
Agencies will submit deliverables to the Chief Data Office based upon the deadlines listed below. The dates
listed below are the date that an agency should have completed and submitted the associated deliverable to the
Chief Data Officer, but agencies are encouraged to complete deliverables early.

  July 1, 2021                          October 1, 2021                    March 1, 2022                June 1, 2022
  •Agencies appoint                     •Agencies initiate                 •Agencies submit             •Agencies submit
   Data Coordinator                      data inventory                     inventory to Chief           Open Data Plans to
                                                                            Data Officer                 Chief Data Officer
                                                                                                        •Agencies begin
                                                                                                         publishing data

OPEN DATA GOVERNANCE

Agencies should establish internal governance and procedures around the prioritization and publication of open
data, including a process for suggesting an open dataset and an approval workflow for publication. Strong open
data governance ensures that published data high quality and meets the agency's strategy for publishing and
releasing open data. Below is a sample organizational structure that agencies may adopt in building their Open
Data Programs.

                                              •Strategic leadership in agency's open data efforts
  Executive Data Governance Body              •Provides leadership support and engagement to help Open Data
                                               Coordinator complete duties

                                              •Single point-of-contact for open data within the agency
                                              •Coordinates inventory efforts and leads open data prioritization
      Agency Data Coordinator
                                              •Reviews and vets all suggested datasets or prepared datasets
                                               before publication

                                              •Subject-matter experts for data
                                              •Support inventory efforts as needed
            Data Stewards                     •May suggest possible datasets for publication
                                              •Assist with data extraction and curation for publication

APPOINTING A DATA COORDINATOR
Central to the State’s open data efforts are the agency Data Coordinators. Agencies shall appoint a Data
Coordinator to act as the single point of contact between the agency and the Chief Data Officer. The Data
Coordinator will be the primary driving authority behind the agency’s open data program, including conducting
the dataset inventory, guiding the prioritization of datasets, working with stakeholders and subject matter
experts to architect open data processes, and in meeting any data quality requirements, formatting, structure,
and other technical requirements for publishing open data. The Data Coordinator should possess extensive
understanding of the agency’s data landscape, including strong relationships with subject matter experts and
the authority and expertise to guide the agency’s open data program and report up to agency leadership on the
efficacy of the program, including monitoring and ensuring compliance with the requirements of the Open Data
Standard.

Data Coordinators should be an individual who already has responsibility for the management and governance
of data, or a person with the necessary skillset to coordinate with all levels of agency staff, including directors,
managers, and end users of systems. Data Coordinators will also need the authority to request time and
resources from other staff members, or have high-level permission to engage stakeholders as needed to assist
with the inventory, open data plan, and data publication processes. Data Coordinators will not need to focus
full-time on open data, but should anticipate spending 4-6 hours a week conducting the inventory and

prioritization, with fewer hours required as the program becomes more sustainable. Agencies should work
closely with the Chief Data Officer in determining a candidate with the appropriate level of authority and subject
matter expertise to serve as Data Coordinator. Once an agency has appointed their Data Coordinator, they are
required to notify the Chief Data Officer. The deadline for agencies to appoint a Data Coordinator and notify the
Chief Data Officer of their appointment is July 1, 2021.

FOR LARGE AGENCIES
Large agencies (500+ FTE), or agencies with lots of data collections and program areas, may also wish to appoint
data stewards to assist and coordinate with the Data Coordinator in the completion of their duties. Data
stewards shall have business-level knowledge of their domains’ data assets and be accountable to the Data
Coordinator for assisting with the inventory, prioritization, and/or publication processes as needed.

The table below identifies the roles and responsibilities for executive branch agencies, agency-appointed Data
Coordinators, and the Chief Data Officer within the Enterprise Information Services (EIS) Office of Data
Governance and Transparency. 3

 Roles                                      Responsibilities
 State Agencies                             •   Appoint a Data Coordinator responsible for the agency’s participation
                                                and publication of data to the data portal.
                                                    o Agencies may also appoint data stewards, who will assist in the
                                                         process of inventorying, classifying, and prioritizing data for
                                                         release.
                                            •   Create an inventory of agency information assets using guidelines
                                                provided by the Chief Data Officer
                                            •   Identify publishable data within the inventory
                                            •   Create an Agency Open Data Plan identifying the Data Coordinator for
                                                the agency, and including a listing of information resources that will be
                                                made publicly available through the Open Data Portal

 Agency Data Coordinators                   •   Act as the single point of contact for the Chief Data Officer in
                                                coordinating and supporting agency open data activities
                                            •   Be responsible for the agency data inventory, communicate and obtain
                                                information from stakeholders, and be responsible for completion and
                                                submission of the inventory spreadsheet
                                            •   Work with agency stakeholders to create the Agency Open Data Plan
                                            •   Submit the Agency Open Data Plan to the Chief Data Officer
                                            •   Coordinate with the Chief Data Officer as needed to assist the agency
                                                in completing all required deliverables

3 The EIS Office of Data Governance and Transparency is the home office of the Chief Data Officer.

    Chief Data Officer                 •    Maintain the State’s Open Data Portal (data.oregon.gov) for
                                            publication of agencies’ open data
                                       •    Provide support and guidance to agencies throughout the open data
                                            process
                                       •    Receive agency data inventories and aggregate them into a statewide
                                            enterprise data inventory
                                       •    Receive Agency Open Data Plans submitted by agencies
                                       •    Provide support, training, and feedback to agency-appointed Data
                                            Coordinators
                                       •    Report biennially to the State Legislature on the status of open data
                                            and data publication.

INVENTORYING DATA

DELIVERABLE: AGENCY DATA INVENTORY

The agency data inventory is a requirement of ORS 276A.365 (c) (B) and must be submitted to the State of
Oregon’s Chief Data Officer for inclusion in an enterprise inventory. Per the statutory requirements, agencies
must “create and maintain an inventory of agency information resources,” and include an indication as to
whether or not the information or dataset included in the inventory is considered “publishable.”

Each biennium on October 1, the Chief Data Officer will provide Data Coordinators with an inventory
spreadsheet as well as instructions for completing the inventory and a submission deadline. Agencies are
expected to complete and/or update their existing inventory and provide it to the Chief Data Officer by the
identified deadline. The first inventory template will be made available on or before June 1, 2021. The due date
for the first agency data inventory is March 1, 2022 and March 1 of every even numbered year thereafter.*

*Large agencies (agencies over 500 FTEs) may request an exception to the inventory timeline by providing a
memo to the Chief Data Officer indicating their anticipated timeline for completing the inventory. Medium
(150-499 FTE) and small agencies (fewer than 150 FTEs) may also request an exemption provided they have
identified over 150 program areas within their agency 4. The memo must include a phased process for submitting
data to the inventory on a quarterly basis and is subject to review and approval by the Chief Data Officer.

METHODS
Agencies are encouraged to develop their own internal processes and procedures for inventorying data assets.
Several methodologies and examples are provided in the Data Coordinator’s Handbook.

4
 Program areas are defined as business lines or functions with specific identified outcomes and responsibilities. A program
area will contain multiple datasets that are unique to the program area.

Agencies can add fields to their own internal inventories, but the data inventory provided to the Chief Data
Office must follow the template provided exactly. Added, reorganized or removed fields will result in the
submission being returned to the agency to revise.

IDENTIFYING PUBLISHABLE DATA
The inventory process requires that agencies identify “publishable” datasets within their inventory. Publishable
data is defined as any data and datasets collected by a state agency that the agency cannot withhold access to
due to its sensitivity, competitive advantage, or other limitations. 5 Typically, datasets that would have privacy
concerns or limitations on their ability to be published would be either Level 3 or Level 4 data, though agencies
may use privacy protections and anonymization techniques to create a publishable dataset from sensitive data.
For the purposes of the inventory, the agency should indicate where the data falls under the following
definitions of publishable data:

     •    As-is: the data can be published with no redactions or removal of fields [all Level 1 data, some Level 2
          data]
     •    Redaction required: the data may be published but would require redactions, de-identification,
          statistical noise, or aggregation to make it public [some Level 2 and Level 3 data]
     •    Not publishable: the data cannot be published in any format. [some Level 3 and Level 4 data]

Please note that the existence of a few sensitive fields does not mean the dataset can be withheld in its entirety
from publication. If the data is not publishable in its raw format, the agency must identify what processing can
occur to make the data publishable. As an example, if the raw data contains personally identifiable information
(PII), could the agency redact the PII elements and publish the dataset without breaching privacy or breaking
protocols?

For guidance and resources in identifying mechanisms for publishing data while accounting for privacy concerns,
please see the Open Data Privacy Guide provided by the Chief Data Officer

INVENTORY, THEN PRIORITIZE
There are several fields in the inventory template surrounding the prioritization of datasets for publication to
the open data portal. Agencies will first need to complete the inventory of datasets and then prioritize according
to the agency's own internal assessment and valuation of the datasets within the inventory. The inventory shall
be submitted to the Chief Data Officer after the prioritization process has taken place.

PRIORITIZING DATA FOR RELEASE

After completing the Agency Data Inventory, agencies will review datasets under their custodianship and
prioritize them for publication by evaluating the data’s readiness for publication, perceived value as an open

5 For a full list of exceptions to “publishable data”, see Appendix A: Definitions

dataset, and overall priority for publication. Agencies can prioritize data based upon multiple business goals or
identified needs, such as:

    •   Improving an existing published dataset
    •   Publishing a new dataset based on internal or external feedback or prioritization
    •   Cataloging an external dataset on data.oregon.gov
    •   Creating a new dashboard/visualization/Socrata Story to accompany a dataset or externally published
        data

Agencies should consider the interests of other state agencies, external partners, and the public when
prioritizing datasets for release. Agencies may undertake their own internal prioritization processes or utilize
other means to prioritize their open data release as they see fit. Detailed guidance and information on
prioritization is available in the Data Coordinator’s Handbook.

PLANNING FOR OPEN DATA RELEASE

DELIVERABLE: AGENCY OPEN DATA PLAN

After identifying high priority datasets for release, agencies should evaluate their current capacity for publishing
open data in the coming biennium and start drafting open data commitments. The deliverable for this step is
creation of the Agency Open Data Plan, which should answer the question “What will my agency commit to
regarding open data through the next biennium, and what will we plan for in future biennia?” Agencies may
commit to publishing new data assets, maturing current data offerings, or enter into a planning phase to
prepare data assets for publication.

IDENTIFY COMMITMENTS FROM PRIORITIZED DATASETS
Agencies should enter into a strategic conversation based upon their high priority datasets and the time and
resourcing commitments required to publish these datasets as open data. If the agency is able to release
datasets during this biennium as part of a publishing phase, how many datasets can the agency realistically
publish during this timeframe? Are there current projects or initiatives underway within the agency that could
further support or enable the publication of open datasets? If the agency is not yet ready to publish open
datasets due to outside constraints, what planning activities will the agency undertake this biennium to be ready
to publish in the future?

Open data commitments should include one of the following:

    •   Improving an existing open dataset, which includes one or more of the following actions:
           o Changing the data schema (e.g., adding and/or removing columns)
           o Increasing granularity or making a dataset more specific (i.e., aggregated less or not at all)
           o Converting a manual dataset to an automated process
           o Increase scope of data in a dataset (e.g., a dataset covering a single permit type may be
               expanded to cover multiple permit types.)

    •   Publishing a new dataset, which includes one or more of the following actions:
            o Planning for data publication, and/or researching the feasibility of extracting data from agency
                information systems
            o Architecting a process for extracting data and publishing to data.oregon.gov
            o Drafting metadata and a data dictionary
            o Publishing the dataset on data.oregon.gov
            o Automating dataset updates/publication
    •   Cataloging an external dataset on data.oregon.gov
    •   Creating a new dashboard/visualization/Socrata Story to accompany an open dataset or externally
        published data

IDENTIFY OPEN DATA PHASE
Agencies will also identify the appropriate phase they are in concerning open data from the following options:

    •   Planning: if the agency does not anticipate publishing any datasets due to the preparation and
        resourcing required to publish data during the current biennium, the agency should still be engaging in
        planning and preparation efforts to publish datasets in the future. Agencies cannot be in the planning
        phase for more than one consecutive biennium. The agency open data plan should reflect which
        datasets the agency is planning to publish in the future.
    •   Publishing: If the agency intends to publish open data this biennium, the open data plan should reflect
        which datasets the agency intends to publish and any additional detail on data categories or types of
        data the agency may intend to publish.
    •   Maintenance: If all of the publishable data identified in the agency’s inventory has been published and
        cataloged appropriately according to the agency’s data inventory and prioritization outcomes, the
        agency is in a maintenance phase.

WRITE AGENCY OPEN DATA PLAN
The Agency Open Data plan should be 2-3 paragraphs, including a brief description of the agency’s core mission
and functions, identification of which phase the agency is in as listed above, and a description of the datasets
the agency plans to release during the biennium. If the agency is in a “planning” phase for open data, there
should be a description of the planning and preparation work the agency will undertake in the current biennia
and which datasets the agency is planning to publish in the next biennium. Agency open data plans are
submitted to the Chief Data Officer on a biennial basis. The first deadline for the Agency Open Data Plan is June
1, 2022, though agencies can submit their plans as soon as they are ready.

PUBLISHING DATA

Once an agency has identified their open data commitments, they should begin planning and preparing for the
publication of their chosen datasets. The process of publishing open data involves time spent obtaining any
approvals needed from data stewards or data subject matter experts, curating the appropriate fields to appear

in the dataset, designing a publication process or method, and adding appropriate context to the data. Detailed
guidance and expectations for data formatting, quality, and context requirements are documented in the Open
Data Technical Standards Manual.

Agencies are expected to build internal processes and procedures to support and resource the publication of
open data in accordance with the agency’s biennial Open Data Plan. Agencies may work directly with the Chief
Data Officer to assist in developing these processes and procedures and to receive guidance in the technical
implementation of any data publication workflows or technical processes.

DATA.OREGON.GOV
The State Open Data Portal, data.oregon.gov, is a vendor-provided solution called Socrata Data Management
Platform. Socrata automatically makes each published dataset available to download in multiple formats,
accessible through an Application Programming Interface (API), and contains some charting/visualization
capabilities within the application itself, allowing users to filter, sort, roll-up, download, and visualize data within
the platform. The Socrata Data Management Platform allows for multiple options in developing a workflow for
open data, automating data publication to the portal, and provides mechanisms for both data consumers and
publishers to interact with datasets made available on the portal through APIs

PUBLISHING DATASETS OUTSIDE OF DATA.OREGON.GOV
Agencies are expected to utilize data.oregon.gov wherever possible in publishing open data, although there may
be use cases where a different platform, such as ArcGIS Online, is a better option for a specific dataset. Agencies
may publish datasets outside of data.oregon.gov, as long as the mechanism for publishing allows for the same
level of data interaction (data must be accessible in a machine readable, open format, downloadable through an
API endpoint or similar) and these datasets must be federated/cataloged in data.oregon.gov to maintain
accessibility. Agencies should work directly with the Chief Data Officer if they have external portals they plan to
use in lieu of data.oregon.gov.

The state also leverages ESRI’s ArcGIS Online tool for the publication of geospatial data, and agencies may
continue using ArcGIS Online in the publication of geospatial datasets. Datasets that have a location component
such as addresses, zip codes, city blocks, but are primarily structured non-spatial datasets may be better served
by utilizing data.oregon.gov. Assets published in ArcGIS online are federated (linked) between the ArcGIS
platform and Socrata, so agencies do not need to put additional effort into cataloging these items. For
additional information on utilizing ArcGIS Online or other geospatial data platforms to meet the requirements of
the Open Data Standard, refer to “Guidance for Geospatial Data Publishers” at the end of this section.

GUIDANCE FOR GEOSPATIAL DATA PUBLISHERS

PUBLISHING SPATIAL DATA
Oregon’s geospatial community has put extensive effort into establishing standards and avenues for publishing
and sharing spatial data through portals such as the Oregon Spatial Data Library, and Oregon’s ArcGIS Online
Portal. Agencies may continue to publish geospatial data through these platforms, and utilize these portals in

order to publish open geospatial data. Geospatial data assets that are published through the Oregon Spatial
Data Library and ArcGIS Online must conform to the same quality and structure standards as assets being
published on data.oregon.gov, with some additional requirements to accommodate the nature of spatial data.

PUBLISHING GEOSPATIAL DATA AS OPEN DATA

FRAMEWORK DATA
Framework should continue to be published to the Oregon Spatial Data Library and will be automatically
federated to the data.oregon.gov catalog. Given the nature of assets provided to the Oregon Spatial Data
Library and the quality and conformity standards required as part of the framework publication process, no
additional requirements or standards need to be met by data published through the Oregon Spatial Data Library.

ARCGIS ONLINE
Agencies may publish datasets or data assets to ArcGIS Online to meet the requirement for publishing agency
open data. In order to publish open spatial data in ArcGIS Online, agencies will need to ensure that the dataset is
authoritative data6 and flag it accordingly within ArcGIS Online.
Assets within ArcGIS Online that are considered “authoritative” and meet the technical standards established
within the Open Data Technical Standards Manual are automatically linked in the data.oregon.gov catalog with
no action required on part of the agencies.

6
    See GPL Authoritative data guidance: https://www.oregon.gov/geo/GPL%20Documents/AuthoritativeData_GPL_120815_rev3.pdf

GLOSSARY

Aggregation: Process in which information is gathered and expressed in a summary form, for purposes such as
statistical analysis or anonymization. Information summed over a large population is typically free of privacy
implications, so aggregation can be used to mitigate privacy concerns.

Application Programming Interface (API): Provides other products and services universal access to our data on
Oregon’s Open Data Portal. It allows developers to use our data for the creation of applications or other
products.

Comma Separated Value (CSV) File: Used for the digital storage of data structured in a tabular form. Each line of
the CSV file corresponds to a row in the table. Within a line, fields are separated by commas and each field
belongs to one table column. A CSV file is used to move tabular data between different computer programs.

Data: Data means final versions of statistical or factual information, including statistical or factual data about
image files that:

    A) Is in alphanumeric form reflected in a list, table, graph, chart or other nonnarrative form that can be
       digitally transmitted or processed
    B) Is controlled by and regularly created or maintained by, or on behalf of, a state agency
    C) And records a measurement, transaction, or determination related to the mission of the agency

Dataset: a named collection of related records, maintained on a storage device, that contains data organized,
formatted or structured in a specific or prescribed way. The most basic representation of a dataset is data
elements presented in tabular form. A dataset may also present information in a variety of non-tabular formats,
such as an extended mark-up language (XML) file, a geospatial data file, or an image file.

High-Value Data: Data qualifies as high-value if it can be used to increase agency accountability and
responsiveness; improve public knowledge of the agency and its operations; further the core mission of the
agency; create economic opportunity; or respond to need and demand as identified through public consultation.

Machine-Readable: Refers to data that can be easily processed by a computer without losing any semantic
meaning.

Metadata: Describes characteristics about the data such as the title, description, and keywords (data about
data). Metadata facilitates a common language when discussing a dataset’s attributes.

Open Data: Open data can be freely used, modified, and shared by anyone for any purpose.

Personally Identifiable Information (PII): Information that can be used by itself or in conjunction with other
information to identify an individual.

Priority: Prioritize datasets based on their organizational and/or public value, the quality of the data, the
limitations of the tools and processes, alignment with the State of Oregon’s Data Strategy and Agency Strategic
Plans, and demand for this data from other agencies, government entities, or the public.

Publishable Data: any and all data and datasets collected by a state agency, excluding:

    (A) Data to which a state agency may deny access pursuant to any provision of a federal, state or local law,
rule or regulation, or another applicable policy or restriction.

    (B) Data that contain a significant amount of information to which a state agency may deny access pursuant
to any provision of a federal, state or local law, rule or regulation.

   (C) Data that reflect the internal deliberative process of a state agency, including but not limited to
negotiating positions, future procurements or pending or reasonably anticipated legal or administrative
proceedings.

    (D) Data stored on a personal computing device owned by a state agency, or data stored on a portion of a
network that has been exclusively assigned to a single agency employee or to a single computing device owned
or controlled by a state agency.

   (E) Materials subject to copyright, patent, trademark, confidentiality agreements or trade secret protection.

   (F) Materials that have commercial value or the disclosure of which could reduce a state agency’s
competitive advantage.

   (G) Proprietary applications, computer code, software, operating systems and similar materials.

   (H) Employment records, internal employee directories or lists, facilities data, information technology and
other data related to internal state agency administration.

   (I) Any other data the publication of which is prohibited by law.

Quality: Determine the quality of datasets by noting their adherence to data standards, detail of the metadata,
the completeness and accuracy of the file, and whether they are in an open format. The standard often used to
measure open format is the Five Stars of Open Data rating system.

Readiness: Data readiness is defined by the level of effort required to publish data as an open dataset.
Readiness factors include the ability of the system to export source data, the technical debt associated with
publishing a dataset, and other factors that impact the level of work required to produce an open dataset.

Socrata: A company that provides data discovery services for open government data and targets non-technical
users who want to view and share government data. The State portal uses Socrata software to publish and
visualize open data.

Tabular Data: Structured data that exists in a table format, with rows and columns. Datasets on
data.oregon.gov are displayed in a tabular format

RESOURCES AND CREDITS

The Oregon Open Data Standard utilizes input from several city and state open data resources.

State of California Open Data Handbook

San Francisco Data Coordinator Guidebook

New York State Open Data Handbook

Texas Open Data Playbook

Philadelphia Open Data Guidebook

NYC Open Data Resources

Connecticut Open Data resources

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
