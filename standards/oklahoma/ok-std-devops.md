---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-devops
title: DevOps Standard
doc_type: standard
citation: OMES DevOps Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/DevOpsStandard.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 576f3b051babbe332fbaac861e17a7ea281bdb067e66881546c56294c5d32107
effective_date: '2022-05-24'
source_version: Last revised 01/23/2025
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

# DevOps Standard (OMES DevOps Standard)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: The purpose of this standard is to provide guidance to vendors who are selected to create or modify custom solutions for the state.

## Full text

                                       DevOps Standard

Introduction
The State of Oklahoma has made a commitment to develop software using a DevOps
philosophy.
With DevOps, quality assurance and security teams become more tightly integrated with
development and operations throughout the application lifecycle.
Teams that follow DevOps practices automate processes that historically have been manual
and slow. They use a technology stack and tooling which helps them operate and evolve
applications quickly and reliably.

Purpose
The purpose of this standard is to provide guidance to vendors who are selected to create or
modify custom solutions for the state.

Standard
   • Code repository.
         o GitHub is the code repository used by the state. Vendors must request access to
             the state’s repository and store all project code there.
         o Azure DevOps Repos was a former acceptable alternative to GitHub. However,
             owners of any existing repositories in Azure DevOps should create a plan for
             migrating to GitHub Enterprise.
                  A future mandate will require all DevOps repos to move to GitHub
                     Enterprise.
   • Testing and building source code.
         o Azure DevOps or Github Actions are used to build, test and deploy application
             source code.
   • Each project has at a minimum, a develop branch and a production branch.
   • The default branch for a repository should be called develop and not master.
   • Each project should have a basic continuous integration/continuous deployment
      workflow that tests the basic build function of the project.

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
 Effective date: 05/24/2022         Review cycle: Annual
 Last revised: 01/23/2025           Last reviewed: 03/10/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
