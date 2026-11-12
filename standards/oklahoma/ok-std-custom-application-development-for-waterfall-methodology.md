---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-custom-application-development-for-waterfall-methodology
title: Custom Application Development for Waterfall Methodology
doc_type: standard
citation: OMES Custom Application Development for Waterfall Methodology
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/cad-waterfall-methodology.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 0910c9db6521d8bebe36cfd6208f20d2b392bfc200258573acf19df2a5a36037
effective_date: '2022-01-18'
source_version: Last revised 05/24/2022
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

# Custom Application Development for Waterfall Methodology (OMES Custom Application Development for Waterfall Methodology)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: To describe the requirements for developing, enhancing and maintaining custom developed applications and integrations using waterfall methodology.

## Full text

             Custom Application Development for Waterfall Methodology

Introduction
Whenever an exception is given to not using an agile methodology, custom development may
follow a waterfall methodology. This is an alternate to agile and scrum methodology for building
custom applications. The key difference in software projects using waterfall methodology is
each step is completed in sequence. The waterfall methodology is a linear process where agile
is an iterative process. In waterfall methodology, there is an assumption that once a project has
started, very few, if any, changes should take place to the requirements.

Purpose
To describe the requirements for developing, enhancing and maintaining custom developed
applications and integrations using waterfall methodology.

Standard
   • Requirements gathering
          o All stakeholders are invited to the requirements gathering meeting.
          o Roles and responsibilities on the project are identified.
          o A step-by-step guide is created and used by developers to build applications.
   • Design
          o The team works together to design and create the systems and components
             include brainstorming, architecture and decisions needed to determine how to
             complete the project.
          o Teams identified and roles and responsibilities defined.
          o Design is defined in on-premises, cloud or hybrid.
   • Implementation: The team builds components of the system, a working product, using
      documentation gathered in the requirements and design phases.
   • Testing
          o Every component designed in the build phase is tested and verified, including
             how components work together in the application or system to delivery.
          o The functionality of an application is verified, and any bugs are fixed as issues
             arise.
          o All processes are documented step-by-step and followed for user acceptance.
          o Deployment occurs once the application or system has been accepted.
   • Maintenance: After the software has been successfully deployed, changes to the
      application will occur over time to accommodate business process changes and to keep
      the system up to date.
   • Tiered environments.
          o Custom applications must have a separation between production and non-
             production environments.
          o At a minimum, there must be development, test, and a production environment
             for custom developed applications. In some cases, for small integrations or
             applications, the development environment can be the developer’s workstation.
          o Role-based control must be created for access to each environment. A
             production environment will only be granted on an as-need basis.
   • Code-related artifacts: All code artifacts produced during custom application
      development must be version controlled using Git and hosted on GitHub.

   •   Change management: Once a product is released into the production environment, all
       change management policies must be adhered to when any updates which require
       changing the code in that environment arise.

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
 Effective date: 01/18/2022         Review cycle: Annual
 Last revised: 05/24/2022           Last reviewed: 06/04/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
