---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s3131
title: S3131 – Network Services – Video Conference Dialing Plan
doc_type: standard
citation: ITA Standard S3131
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s3131.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 45fbb0df57bb7b42b8631aa81d06fe5ab3af3506ac3d06ac576b41a2dd3953d9
effective_date: '2009-10-02'
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# S3131 – Network Services – Video Conference Dialing Plan (ITA Standard S3131)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '3000 - Network and Telecommunications, Standards', a standard. The library's own summary: "ITA Standard S3130 mandates security and operational protocols for video conferencing services to ensure secure and reliable communication."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S3000 NETWORK AND
TELECOMMUNICATIONS STANDARDS

Category:     S3131 – NETWORK SERVICES- VIDEO CONFERENCE DIALINGPLAN

CONTENTS:
I.    Definition
II. Rationale
III. Approved Standard(s)
IV. Approved Product(s)
V. Justification
VI. Technical and Implementation Considerations
VII. Emerging Trends and Architectural Directions
VIII. Procedure Reference
IX. Review Cycle
X. Contact Information
XI. Additional Information (if any)
      Revision History

I. DEFINITION
   Telecommunications numbering plan where a telephone number is used to uniquely
   identify a public network termination point, in this case for a State video conferencing
   endpoint. Typically consisting of three fields, CC (country code), NDC (national
   destination code also known as the area code), and SN (subscriber number).

II. RATIONALE

   A well-designed dial plan is a key component of a successful video network and video
   call routing. Without a well-constructed dial plan, it is impossible to scale the network or
   to properly route video calls to the appropriate host agency or endpoint.

III. APPROVED STANDARD(S)

   The recommended video dialing plan is to follow and conform to the current North
   American Numbering Plan (NANP). The NANP is an integrated telephone numbering
   plan serving 19 North American countries that share its resources. It was developed by
   AT&T in 1947 to simplify and facilitate the direct dialing of long distance telephone calls.
   The International Telecommunications Union (ITU) assigned country code "1" to the
   NANP area. The NANP conforms to the ITU E.164 Recommendation, the international
   standard for telephone numbering plans.

S3131 Video Conference Dialing Plan                                                   Page 1 of 3

   All NANP numbers consist of the country code (1 in North America) plus a three-digit
   Numbering Plan Area (NPA) code, commonly called an area code, followed by a seven-
   digit local number usually represented as +1NXX-NXX-XXXX where N is any digit from 2
   through 9 and X is any digit from 0 through 9.

   The State shall use the same numbering plan as its standard for Video Conferencing
   endpoints. Furthermore State video endpoints E.164 number assignments should be
   valid numbers assigned to respective agencies by their local PSTN (public switched
   telephone network) carrier.

IV. APPROVED PRODUCTS(S)

   N/A

V. JUSTIFICATION

   Having a State video dialing plan ensures; network scalability as video endpoints grow
   and the proper routing of video calls to respective endpoints. Also allows for a simple
   directory of dialable video endpoints throughout the State network.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

   We recognize there is currently some legacy video equipment still in use throughout the
   State. Many of these devices are NOT E.164 compliant and will be not be able conform
   to the State standard dialing plan and may encounter interoperability issues. But, all
   new installations should support the standard as well as older non-compliant devices
   upgraded to support the standard where possible.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

   This dialing standard is also intended to position the State to support ENUM (electronic
   numbering) which is the process of creating a domain name from a telephone number
   and resolving it to an Internet address (a URI uniform resource identifier) using DNS
   technology. For example, done correctly an E164 telephone number assigned to a
   video endpoint such as1+ (208) 577-2001 using ENUM technology could be accessed
   using 12085772001@connect.conferencing.idaho.gov from a video endpoint on the
   Internet.

VIII. PROCEDURE REFERENCE

   N/A

IX. REVIEW CYCLE

   Six (6) Months

S3131 Video Conference Dialing Plan                                               Page 2 of 3

X. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

XI. ADDITIONAL INFORMATION (IF ANY)

   N/A

REVISION HISTORY

   07/01/13 – Changed “ITRMC” to “ITA”.

   Effective Date: October 2, 2009

S3131 Video Conference Dialing Plan                                 Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
