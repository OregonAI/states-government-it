---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-data-01-02-s
title: Metadata Standard
doc_type: standard
citation: WaTech Standard DATA-01-02-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2023-09/187_10_MetadataStandard_Approved%252003102020.docx
source_format: docx
retrieved: '2026-11-11'
source_sha256: 0cc48a4946911e5a816a8b503a4fcafe0f6e446ba8274c73d60ae223bc66c7e9
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text extracted from the Word file (.docx) with pandoc's docx reader, tracked changes
  accepted and the result rendered one line per paragraph, heading, list item and table row (a table row's
  cells are joined by ' | '; list markers are written out as the file numbers them, bullets as a bullet
  character; footnotes follow the text as [n]). Running headers and footers, pictures and the text inside
  text boxes (such as a cover-page title) are not read. Headings carry no markup.
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
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Metadata Standard (WaTech Standard DATA-01-02-S)

## At a glance

Item of the WaTech policy library, chapter '6. Data Management' (listed as type Standards). Listed at https://watech.wa.gov/policies/metadata-standard.

## Full text

Standard 187.10 - Metadata Standard

Purpose

Establishes the requirement for documenting agency applications, data and data services through the creation and use of metadata. Metadata plays a fundamental role in the successful management of information and services. The objective of this standard is to protect the states investment in significant information assets through standardized documentation.

Statutory Authority

The provisions of RCW 43.105.041 detail the powers and duties of the Technology Services Board (TSB), including the authority to develop statewide or interagency information services and technical policies, standards, and procedures.

Scope and Exemptions

This standard applies to state of Washington executive branch agencies, agencies headed by separately elected officials, and institutions of higher education referred to as “agencies” throughout this document. Institutions of higher education are exempt but are invited to conform where feasible. This standard applies to those data shared via state open data portals.

Standard

The Metadata Elements described below (based on Dublin Core and ISO) constitute the minimum metadata elements and are required for all open data state applications, data and data services.

For geospatial data, application and data services, the minimum metadata elements are extended to include additional fields as outlined in the “Washington Guideline for Geospatial Metadata” as approved by the Geospatial Information Technology Committee. Geospatial data, applications and data services include explicit coordinates or spatial geometry.

Non-geospatial data may include location elements that communicate the general location (e.g. fields for county, legislative district, address) and are not required to follow the “Washington Guidelines for Geospatial Metadata”.

Unstructured data, narrative documents, or materials in records retention or archival storage are not required to comply with this standard.

Metadata Basic Standard

All Washington State Agency information systems shared to open data portals are expected to include the following data elements in each of the following categories. Agencies are strongly encouraged to include documentation in plain language about the attributes in a dataset when possible.

Identification Information

Element | Description | Format/Example
Title | A name given to the resource. | Format: Character Example: Water Rights Applications
Description / Abstract | An account, description or overview of the service or resource. | Format: Character Example: Pending Water Right Applications in Washington State. Includes both applications for new water rights and to change existing water rights.
Service URL | Standard web address to access or link to the service or resource. | Format: Character Example: https://data.wa.gov/Natural-Resources- Environment/Water-Right-Applications/9ubz-5r4b [1]
Format | The nature or genre of the resource. To describe the file format, physical medium or dimension of the resource. | Format: Character Example: OGC KML XML, REST |
Originator | The entity responsible for publishing the service or resource. | Format: Character Example: Water Quality Program Manager, Washington Department of Ecology, PO box 42222 Olympia, WA 98504-9999 |
Publication Date | The date the service or resource was first made available. | Format: Date Example: Oct 11, 2012 |
Metadata language | The language in which the service or resource is published. | Format: Character Example: English |

Data Theme

Element | Description | Format/Example
Theme Topic | Identifies the most applicable 19 ISO Data Categories. | Format: Character Example: Economic, Environmental, Public Safety

Data Time Period

Element | Description | Format/Example
PeriodofTime (optional) | The timeframe of the data content available in the dataset. | Format: Character Example: July 1, 2015-June 30 2016
Posting Frequency | Planned refresh or update cycle. This is a goal, not a guarantee. Corresponds to Dublin Core value “Coverage (Temporal)”. | Format:Character Example:Annually Example: Hourly

Revision History

Date | Action taken
March 10, 2020 | Approved by Technology Services Board
July 26, 2019 | Standard supersedes existing standard 187.10 and rescinds geospatial standards 161.02 & 161.05
July 26, 2019 | Adopted by state CIO
February 25, 2019 | Updates from Geospatial Metadata Workgroup
December 9, 2015 | Approved by Technology Services Board
October 14, 2015 | Adopted by state CIO

CONTACT INFORMATION

Contact the OCIO Policy & Waiver Mailbox for questions on policy and standards.

SUNSET REVIEW DATE: July 26, 2022

ADOPTION DATE: July 26, 2019

APPROVAL DATE: March 10, 2020 TSB Meeting

APPROVING AUTHORITY: Jim Weaver, State CIO & Chair TSB

## Curator notes

Text extracted from the Word file (.docx) with pandoc's docx reader, tracked changes accepted and the result rendered one line per paragraph, heading, list item and table row (a table row's cells are joined by ' | '; list markers are written out as the file numbers them, bullets as a bullet character; footnotes follow the text as [n]). Running headers and footers, pictures and the text inside text boxes (such as a cover-page title) are not read. Headings carry no markup.
