---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-defects-tracking
title: Defects Tracking Standard
doc_type: standard
citation: OMES Defects Tracking Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/defects-tracking-standard.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 87f0d984ba37b1f18635806fe29ff156a88e0e00048b7081d47510721c892888
effective_date: '2022-05-06'
source_version: Last revised 05/06/2022
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

# Defects Tracking Standard (OMES Defects Tracking Standard)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: The purpose of this document is to define the standard method of tracking defects in software applications.

## Full text

                                  Defects Tracking Standard

Introduction
This document identifies the standard methods of tracking for bugs/defects in application
software. The tracking follows the life of the bugs/defects from identification to resolution.

Purpose
The purpose of this document is to define the standard method of tracking defects in software
applications.

Definitions
Defect tracking – the tracking of bugs and defects in software from identification all the way
through to resolution.

Standard
ServiceNow.
   • ServiceNow is the standard for customer identification of defects and bugs in software
       applications. Once a bug is identified, it should be assigned to the application support
       team for analysis. Cross team collaboration may be required as applications frequently
       break for many other reasons, including security changes, firewall changes, workstation
       changes and user error. Journal notes should be updated and modified as the issue is
       worked. The customer should be able to follow each step of the process. The request
       can be closed when a resolution is found and the customer is notified. Additionally, if a
       bug is found that requires a software change, an Azure DevOps bug should be entered
       into the backlog and tracked through the software development cycle as noted in the
       next section.

Azure DevOps.
   • Azure DevOps is the standard for tracking of application software and bugs if an
       application code issue is identified and needs to be worked by an application support or
       development team. The bug should be identified in a product backlog and worked as
       prioritized by the product owner and management team. User stories should be entered
       on the bug if the issue needs to be worked across teams, and individual tasks created
       and worked as needed. The status of each of these items should be updated and each
       step of the work is completed. Upon resolution, all of the tasks should be closed out, and
       any service requests that initiated the application changes should also be updated and
       the customer notified. If a new version of software is required, a change request should
       be completed and approved before the software is pushed to production.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§
34.11.1 and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended
standards policies and standards at any time. Compliance is expected with all published policies
and standards, and any published amendments thereof. Employees found in violation of this
standard may be subject to disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases
and projects to enable the chief information officer to assess the needs and capabilities of state
agencies as well as streamline and consolidate systems to ensure that the state delivers
essential public services to its citizens in the most efficient manner at the lowest possible cost to
taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 05/06/2022         Review cycle: Annual
 Last revised: 05/06/2022           Last reviewed: 07/28/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
