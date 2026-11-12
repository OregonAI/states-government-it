---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-development-continuous-integration-and-continuous-delivery
title: Development – Continuous Integration and Continuous Delivery Standard
doc_type: standard
citation: OMES Development – Continuous Integration and Continuous Delivery Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/ContinuousIntegrationDelivStn.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 4169e8ee9b59e7fb633d5b4055c02717c9ebabd33054a596c58c3beb13efc4a7
effective_date: '2022-04-07'
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

# Development – Continuous Integration and Continuous Delivery Standard (OMES Development – Continuous Integration and Continuous Delivery Standard)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: The purpose of this document is to establish a standard for OMES development around the testing and deployment of applications and to establish the tools and products used for this part of the development workflow.

## Full text

       Development – Continuous Integration and Continuous Delivery Standard

Introduction
Continuous integration and either continuous delivery or continuous deployment are important
pieces of the modern development workflow.

Purpose
The purpose of this document is to establish a standard for OMES development around the
testing and deployment of applications and to establish the tools and products used for this part
of the development workflow.

Definitions
Continuous delivery – Continuous delivery automatically deploys all code changes that have
passed continuous integration into a testing and/or production environment after the build stage.
Typically, these changes are grouped together and then released as a standard release every
two weeks.
Continuous deployment – A more advanced concept where all changes in the code repository
are automatically moved to production without going to a testing environment first. Instead of
code being released during release days, every code change results in a corresponding
release.
Continuous integration – The step during the development process where tests are run (typically
automatically) as code is checked into a code repository.

Standard
Any tool that has been approved for CI/CD on the OMES reference architecture is allowed. If
there is no specific tool listed on the reference architecture, it is expected that the development
group should use either GitHub Enterprise or Azure DevOps tools for CI/CD in their
development.
All new applications created after the establishment of this standard must implement at least the
most basic form of CI/CD in that they must:
   •     Keep their code in a Git repository in GitHub Enterprise.
              o Owners of repositories for any code in Azure DevOps should begin to create a
                 plan for migration to GitHub Enterprise. A future mandate will require migration of
                 all Azure DevOps Repos to GitHub Enterprise.
   •     Add at least a basic build test for CI purposes to make sure that the app can build before
         it can be deployed.
   •     Connect the Git repository to the deployment space with a code pipeline using the
         available CD tools so that code that has passed approval and testing can be deployed.
It is acceptable for code that has been tested and passed automated approval to be “gated” or
held for deployment approval until a pipeline approver has approved it to be deployed. It is also
acceptable for code to be deployed from development to test to production or any other
branching standard set by the repository admin.

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
 Effective date: 04/07/2022         Review cycle: Annual
 Last revised: 01/23/2025           Last reviewed: 03/10/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
