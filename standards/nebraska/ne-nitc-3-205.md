---
schema_version: 1
corpus: states-government-it
jurisdiction: nebraska
id: ne-nitc-3-205
title: 3-205. Street centerlines.
doc_type: standard
citation: NITC Technical Standards and Guidelines 3-205
authority_level: ''
issuing_body: Nebraska Information Technology Commission
source_url: https://nitc.nebraska.gov/docs/3-205.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 5aa2c7d2e3671eebb01e362e55cf313828828b178c34413443caa4a52a3d82f5
effective_date: null
source_version: History through November 10, 2022
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# 3-205. Street centerlines. (NITC Technical Standards and Guidelines 3-205)

## At a glance

NITC Technical Standards and Guidelines section 3-205, adopted by the Commission under Neb. Rev. Stat. 86-516 and applying to state agencies, boards and commissions (1-102).

## Full text

                                                                              Nebraska Information Technology Commission
                                                                                         Technical Standards and Guidelines

3-205. Street centerlines.
    (1) The commission adopts by reference the most recent version of sections 2, 3, and 3.1 of
the NENA Standard for NG9-1-1 GIS Data Model released by the National Emergency Number
Association [https://www.nena.org/page/ng911gisdatamodel] for GIS data that consists of street
centerlines.
     (2) The following are optional additional attributes for street centerlines:

                    From Road Level                  FromLevel O                     P        1

                    To Road Level                    ToLevel           O             P        1

                    FromLevel: Specifies the ‘elevation’ of a segment FROM node (start point). This
                    field does not require actual elevation in terms of real-world measurements. The
                    value is only used to determine whether a turn is allowed from one street to a
                    street that intersects it in a 2-dimensional space, similar to floors in a building.
                    Nodes at the lowest level would be assigned 0, with overlapping nodes
                    representing additional level(s)/overpass(es) will be assigned the next sequential
                    integer value accordingly.
                    ToLevel: Specifies the ‘elevation’ of a segment TO node (end point). This field
                    does not require actual elevation in terms of real-world measurements. The value
                    is only used to determine whether a turn is allowed from one street to a street that
                    intersects it in a 2-dimensional space, similar to floors in a building. Nodes at the
                    lowest level would be assigned 0, with overlapping nodes representing additional
                    level(s)/overpass(es) will be assigned the next sequential integer value
                    accordingly.
--
     History: Adopted on March 27, 2015. Amended on July 25, 2019 and November 10, 2022.
     URL: https://nitc.nebraska.gov/standards/3-205.pdf

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the latest date on the section's History line (adoption, renumbering or amendment); the section prints no separate effective date, so effective_date stays empty.
