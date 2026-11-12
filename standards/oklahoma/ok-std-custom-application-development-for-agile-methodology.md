---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-custom-application-development-for-agile-methodology
title: Custom Application Development for Agile Methodology
doc_type: standard
citation: OMES Custom Application Development for Agile Methodology
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/cad-agile-methodology.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 47ca683611992fa108fd2c1aeb7074873aff7a6bdbf49cb3215c328471b23842
effective_date: '2022-01-18'
source_version: Last revised 04/15/2025
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

# Custom Application Development for Agile Methodology (OMES Custom Application Development for Agile Methodology)

## At a glance

A CIO standard in the 'Applications and Data' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document establishes requirements for planning, design, development, enhancements and the maintenance of custom developed applications and integrations for agile methodology within the State of Oklahoma.

## Full text

         Custom Application Development for Agile Methodology Standard

Introduction
Custom software development projects must be managed according to agile methodologies
when building a new customer application or adding features to an existing application at the
State of Oklahoma. Agile projects are broken up into short cycles where demands and solutions
evolve through the collaborative effort with cross-functional team and customers for rapid
production and constant revision, and each sprint is evaluated after completion.

Purpose
This document establishes requirements for planning, design, development, enhancements and
the maintenance of custom developed applications and integrations for agile methodology within
the State of Oklahoma.

Standard
All custom software development must follow agile methodologies unless an exception is
approved. When an exception is approved, custom software development would follow waterfall
methodologies (Custom Application Development for Waterfall Methodology).
    • Kickoff meeting.
           o All stakeholders are invited.
           o The meeting agenda includes introductions, problem overview, the customer
               identifying the problem(s), deadlines, duration of sprints, role definitions (i.e.,
               product owner or scrum master) and general or housekeeping information
               relevant to the project.
    • Planning.
           o Decisions on where an application is hosted (on-premises, in the cloud, or a hybrid)
               is identified in the planning phase.
           o The team defines requirements, writes user stories, prioritizes stories, estimates
               length of time to complete stories and adds to the product backlog.
    • Develop/code.
           o Developer(s) write code and complete tasks defined in a user story, and the
               specifications for acceptance criteria are defined in user stories.
           o Convert decisions made in design into interfaces to be interacted and tested.
           o All custom code must be added and maintained in Git for version control and
               hosted according to the Version Control and Hosting Standard, which is currently
               Github Enterprise.
    • Testing.
           o Large projects require a quality assessment and may include automated testing
               throughout subsequent sprints.
           o Small projects require user acceptance testing.
           o All data used for testing must be carefully selected, protected and controlled to
               ensure only test or dummy data is used in cases that use sensitive data in the
               application(s).
    • Deployment.
           o The deployment environment is a staging environment for developments made
               during a sprint.
           o Deployments must follow deployment policies.

   •   Tiered environments.
           o Custom applications must have a separation between production and non-
              production environments.
           o At a minimum, there must be development, test and a production environment for
              custom developed applications. In some cases, for small integrations or
              applications, the development environment can be the developer’s workstation.
           o Role-based control must be created for access to each environment. A
              production environment will only be granted on an as-need basis.
   •   Code-related artifacts: All code artifacts produced during custom application
       development must be version controlled using Git and hosted according to the Version
       Control and Hosting Standard, which is currently Github Enterprise.
   •   Maintenance.
           o After deployment, a product must be monitored and managed to ensure a smooth
              operation, resolve software bugs or issues and monitor continuous integration
              builds as a pre-alert to dependency issues. This requires adjustments from system
              environmental changes or business process changes.
           o Downstream dependency changes may prompt a need for changes.
           o Refactoring may occur after better techniques are discovered and improving
              efficiency as the volume of data the application processes increases.
   •   Change management: Once a product is released into a production environment, all
       change management policies must be adhered to when updates require changing the
       code in that environment arise.

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
   • Custom Application Development for Waterfall Methodology.
   • Version Control and Hosting Standard.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 01/18/2022         Review cycle: Annual
 Last revised: 04/15/2025           Last reviewed: 04/15/2025
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
