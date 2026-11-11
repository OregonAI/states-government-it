---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-data-02-03-s
title: Web Mapping Services Publication Standard
doc_type: standard
citation: WaTech Standard DATA-02-03-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2023-09/161.06_WebMapping_Std_ADOPTED_2014.docx
source_format: docx
retrieved: '2026-11-11'
source_sha256: ad4e0e19b655d66f561d4fa7eb8f16699277f2bcfd8c67987426f0745cbde28c
effective_date: '2014-09-05'
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Web Mapping Services Publication Standard (WaTech Standard DATA-02-03-S)

## At a glance

Item of the WaTech policy library, chapter '6. Data Management' (listed as type Standards). Listed at https://watech.wa.gov/policies/web-mapping-services-publication-standard.

## Full text

Standard Number 161.06

Web Mapping Services Publication Standard

Effective Date: September 5, 2014

Related Documents:

• Geospatial Policy & Standards Procedure 162.00
• Waiver Process 101.00

Statutory Authority

The provisions of RCW 43.105.041 detail the powers and duties of the Technology Services Board (TSB), including the authority to develop statewide or interagency information services and technical policies, standards, and procedures.

These standards apply to state of Washington executive branch agencies, agencies headed by separately elected officials, and institutions of higher education referred to as “agencies” throughout this document. Academic and research applications at institutions of higher education are exempt.

Purpose

This standard is designed to ensure Washington State geospatial data are correctly located and aligned with industry standard online mapping tools and web-based geospatial data systems.

They are designed to improve data quality, accuracy, rendering speed and improve the sharing of spatial data on the Web. It enables consistent online web mapping of geospatial data, based on an industry standard map tiling scheme and projection, with other commercial map services.

Standard

This standard applies when building web accessible geospatial services including:

• Cached, web-based map services that will be integrated with similarly tiled services
• Dynamic map services that will be integrated with similarly projected cached and dynamic services

Cached Map Services

Agencies should use the following guidelines for a Map Tiling Scheme when developing map caches in support of online mapping applications and services which will be integrated with industry standard map services and made available on the Web.

Tiling Scheme Parameter | Guideline | Authority
World Coordinate System | Web Mercator Auxiliary Sphere coordinate system (EPSG 3857, ESRI WKID 102100) | ESRI
Horizontal Datum | World Geodetic System of 84, with revisions | NGA
Map Units | Meters | ESRI
Tile Origin | x=-20037508.342787 y=20037508.342787 | ESRI
Tile Size | 256 x 256 | ESRI
DPI | 96 | ESRI
Scale Level and Scale denominator | Level 0, 591657527.591555 Level 1, 295828763.795777 Level 2, 147914381.897889 Level 3, 73957190.948944 Level 4, 36978595.474472 Level 5, 18489297.737236 Level 6, 9244648.868618 Level 7, 4622324.434309 Level 8, 2311162.217155 Level 9, 1155581.108577 Level 10, 577790.554289 Level 11, 288895.277144 Level 12, 144447.638572 Level 13, 72223.819286 Level 14, 36111.909643 Level 15, 18055.954822 Level 16, 9027.977411 Level 17, 4513.988705 Level 18, 2256.994353 Level 19, 1128.497176 |

Map Projection for Dynamic Map Services

Agencies should use the following guideline when producing map services utilizing dynamic spatial data that will be integrated with industry standard map services and made available on the Web.

Parameter | Guideline | Authority
Coordinate System | Web Mercator Auxiliary Sphere coordinate system (EPSG 3857, ESRI WKID 102100) | ESRI
Datum | World Geodetic System of 84, with revisions | NGA
Map Units | Meters | ESRI

References

• Web Mercator, The Standard for Sharing Data on the Web, ESRI
• World Geodetic System 1984 (WGS 84) https://www1.nga.mil/ProductsServices/GeodesyGeophysics/WorldGeodeticSystem/Pages/default.aspx
• Surveying and Positioning, OGP Surveying and Positioning Committee. http://www.epsg.org

Definitions

Cached Map Service– A map service which uses a map tiling scheme designed to support high performance and scalability. Cached map services need to use the same coordinate system in order to overlay in a web client applications.

Dynamic Map Service – A map service which renders a map image on demand directly from a live data source.

Horizontal Datum – A reference surface against which locations on the earth are described, most commonly using latitude and longitude coordinates.

Map Cache – A collection of pre-rendered map images defined by a map tiling scheme.

Map Projection – A mathematical model used to transform spherical geographic coordinates on the earth’s curved surface to a planimetric Cartesian coordinate system.

Map Service – A service available across the Web which uses standardized protocols including XML and SOAP to transmit map images.

Map Tiling Scheme – A specification which defines the coordinate system, scales, geographic extent, dpi, tile size, and tile system origin of a set of hierarchically organized static map images that compose a map cache.

Web Mercator Auxiliary Sphere Coordinate System- A world coordinate system used by popular web mapping tools such as Google Maps, Bing Maps, ArcGIS Online, and others

WGS 84 Coordinate System – Acronym for “World Geodetic System 1984”. WGS84 is a commonly used geocentric horizontal datum.

World Coordinate System – A Cartesian coordinate system which represents locations on the earth using a single worldwide coordinate grid.

Contact Information

For questions about this standard, please contact the Office of the CIO.

Revision History

Date | Action taken
September 5, 2014 | Adopted by the state CIO
June 5, 2014 | Adopted by the Geographic Information Technology (GIT) Committee

Approving Authority

Chief Information Officer Date

Chair, Technology Services Board

## Curator notes

Text extracted from the Word file (.docx) with pandoc's docx reader, tracked changes accepted and the result rendered one line per paragraph, heading, list item and table row (a table row's cells are joined by ' | '; list markers are written out as the file numbers them, bullets as a bullet character; footnotes follow the text as [n]). Running headers and footers, pictures and the text inside text boxes (such as a cover-page title) are not read. Headings carry no markup.
