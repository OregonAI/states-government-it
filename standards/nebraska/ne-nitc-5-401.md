---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-5-401
title: 5-401. Active Directory; user photographs.
doc_type: standard
citation: NITC Technical Standards and Guidelines 5-401
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/5-401.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 3d844e6fb728429e3a872a92dde4d81afe93fd9fd031fce2b5e0e902fb138fb8
effective_date: null
source_version: History through July 12, 2018
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). source_version is the latest date on the section's History line (adoption, renumbering or
  amendment); the section prints no separate effective date, so effective_date stays empty.
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# 5-401. Active Directory; user photographs. (NITC Technical Standards and Guidelines 5-401)

## At a glance

NITC Technical Standards and Guidelines section 5-401, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102).

## Full text

                                                                        Nebraska Information Technology Commission
                                                                                   Technical Standards and Guidelines

5-401. Active Directory; user photographs.
    (1) Purpose. Microsoft Active Directory has an attribute ("thumbnailPhoto") to store a
thumbnail photograph of each user. Other applications, including Microsoft Outlook and the
Exchange Global Address List, will display these photographs automatically in the context of
providing information about the user. This policy provides guidance on the use of this feature in
the state's shared Active Directory forest.
   (2) Optional Use. Each agency has the option to use, or not use, the thumbnail photograph
functionality in the state's shared Active Directory forest.
    (3) Requirements. If an agency chooses to use the thumbnail photograph functionality, the
following requirements will apply:
     (a) Image file type: JPEG;
     (b) Image file size: 10 KB or smaller;
   (c) Image file name: Same as the user login ID plus the .jpg extension (for example,
john.doe.jpg);
     (d) Image size: 96x96 pixels is recommended;
   (e) Image content: A recent head-and-shoulders photograph of the user (not an avatar, icon,
drawing, etc.);
     (f) The agency is responsible for obtaining photographs of their users;
   (g) The agency must use the mechanism provided by the Office of the CIO for uploading
agency image files; and
     (h) The agency must not modify the Active Directory “thumbnailPhoto” attribute directly.
--
     History: Adopted on December 10, 2013. Amended on July 12, 2018.
     URL: https://nitc.nebraska.gov/standards/5-401.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
