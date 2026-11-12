---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-continuous-deployment
title: Continuous Deployment Standard
doc_type: standard
citation: OMES Continuous Deployment Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/continuous-deployment-standard.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 5eee1f8bdad91907fceff8781d36d795bb65e139bf2b4cd6c45b5551f822ddb6
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

# Continuous Deployment Standard (OMES Continuous Deployment Standard)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: The purpose of this document is to define a standard for automation/releasing software.

## Full text

                             Continuous Deployment Standard

Introduction
This document identifies the process for deploying code from a GitHub/Azure DevOps
repository to the platform where the resources are hosted. Azure DevOps is used as the single
control mechanism for both approval tracking and auditing purposes.

Purpose
The purpose of this document is to define a standard for automation/releasing software.

Definitions
Azure DevOps – This is a SaaS solution offered by Microsoft. It has the ability to host Git
repositories and manage test plans, scrum boards, work items and other things needed for a
better DevOps practice.

Pipeline – A pipeline is automation; Azure DevOps has two primary kinds: build and release.

Build pipeline – This type of pipeline is used for building and unit testing code.

Release pipeline – This type of pipeline is used for the actual deployment of the code to the
hosting platform.

GitHub – This is a SaaS solution offered by Microsoft for hosting Git-based repositories.

Standard
Azure DevOps is to be used for all aspects of a code build and release. This is to make auditing
needs simpler to track. Having a single control mechanism for orchestration of code builds to
testing and ultimately to a release, gives a clearer view across all aspects of a deployment.
Azure DevOps gives flexibility to not only deploy to Azure or OnPrem, but into any cloud
platform. A release should be retained for a minimum of 30 days, and the last three releases
should be retained. With the use of Azure DevOps, this retention policy is already set in place.

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

References
   • Creating a CI/CD pipeline with Azure Pipelines and Compute Engine
   • AWS Toolkit for Azure DevOps
   • Configuring a CD pipeline for your Jenkins CI

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 05/06/2022         Review cycle: Annual
 Last revised: 05/06/2022           Last reviewed: 07/29/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
