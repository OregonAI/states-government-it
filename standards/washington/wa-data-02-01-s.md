---
schema_version: 1
corpus: states-government-it
jurisdiction: washington
id: wa-data-02-01-s
title: Geodetic Control Data Standard
doc_type: standard
citation: WaTech Standard DATA-02-01-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2025-10/DATA-02-01-S_GCDS.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 43505cba3b43efdfdf3ecb8e533e9421c4b0e33ffcd41eca0f65b0f8fa903860
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

# Geodetic Control Data Standard (WaTech Standard DATA-02-01-S)

## At a glance

Item of the WaTech policy library, chapter '6. Data Management' (listed as type Standards). Listed at https://watech.wa.gov/policies/geodetic-control-data-standard.

## Full text

DATA-02-01-S                                                                                   Replaces:
State CIO Adopted: September 2025                                                   IT Standard 161.01
TSB Approved: September 2025                                             Geodetic Control Data Standard
Sunset Review: September 2028                                                              July 26, 2019

                   GEODETIC CONTROL DATA STANDARD
See Also:
RCW 43.105.054 WaTech Governance
RCW 43.105.020 (22) “State agency”

1. Agencies will use the following Geodetic Control Data Standards for significant new or
   redesigned agency geospatial datasets, geographic information systems, and data
   exchanges.

                                                                              Owner/
     Geodetic Control                State Standard                           Primary Steward

     Horizontal Datum                NAD 83/92 – North American Datum of      NGS
                                     1983, with 91 adjustments

     State Plane Coordinate          Washington Coordinate System of 1983     DNR
     System

     Vertical Datum                  NAVD 88 – North American Vertical        NGS
                                     Datum of 1988

2. The North American Datum 1983 (NAD 83) with 1991 (NAD 83/91) adjustments will be
   the state standard for Horizontal Datum.

       a. Reference datum and adjustments in metadata.

3. The Washington Plane Coordinate System will be the coordinate system in Washington,
   per RCW 58.20.

       a. The standard unit of measure is the U.S. Survey Foot.

       b. For conversion of coordinates between the meter and the United States survey
          foot, one foot equals 0.3048 meters, per RCW 58.20.185, Standard Value – one
          foot.

c. Use Washington Plane Coordinate System South Zone for Statewide Layers and for
   layers that are both in the South and North Zones. See FIPS: 4602; WKID: 2927.

d. Use South Zone for layers that are not in the North Zone. The area now included in
   the following counties will constitute the south zone:
      i.      Adams
      ii.     Asotin
      iii.    Benton
      iv.     Clark
      v.      Columbia
      vi.     Cowlitz
      vii.    Franklin
      viii.   Garfield
      ix.     That part of Grant lying south of parallel 47 30’ north latitude
      x.      Grays Harbor
      xi.     Kittitas
      xii.    Klickitat
      xiii.   Lewis
      xiv.    Mason
      xv.     Pacific
      xvi.    Pierce
      xvii. Skamania
      xviii. Thurston
      xix.    Wahkiakum
      xx.     Walla Walla
      xxi.    Whitman
      xxii. Yakima

e. Use Washington Plane Coordinate System North Zone for layers that are not in the
   South Zone (FIPS: 4601; WKID: 2926). The area now included in the following
   counties will be considered the North Zone:
      i.      Chelan
      ii.     Clallam
      iii.    Douglas

              iv.     Ferry
              v.      Island
              vi.     Jefferson
              vii.    King
              viii.   Kitsap
              ix.     Lincoln
              x.      Okanogan
              xi.     Pend Oreille
              xii.    San Juan
              xiii.   Skagit
              xiv.    Snohomish
              xv.     Spokane
              xvi.    Stevens
              xvii. Whatcom
              xviii. That part of Grant lying north of the parallel 47 30’ north latitude

4. The North American Vertical Datum of 1988 (NAVD 88) will be the state standard for
   vertical datum.

        a. National Geodetic Survey (NGS) Geodetic Tool Kit provides various free online
           interactive and downloadable software programs and tools for computing,
           converting, and adjusting geospatial data. See National Oceanic and Atmospheric
           Administration NGS http://www.ngs.noaa.gov/.

        b. VDatum is a free software tool designed to vertically transform geospatial data
           among a variety of tidal, orthometric, and ellipsoidal vertical datums. See National
           Oceanic and Atmospheric Administration VDatum http://vdatum.noaa.gov.

REFERENCES

   1.   Link to reference.
   2.   Definition of Terms Used in WaTech Policies and Reports.

CONTACT INFORMATION

   •    For questions about this policy, please email the WaTech Policy Mailbox.
   •    For technical assistance, please email confirmemail@watech.wa.gov.

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
