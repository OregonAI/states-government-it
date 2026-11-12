---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-application-data-integration-standard
title: Application/Data Integration Standard
doc_type: standard
citation: 'NCDIT: Application/Data Integration Standard'
authority_level: ''
issuing_body: North Carolina Department of Information Technology
source_url: https://it.nc.gov/documents/applicationdata-integration-standard/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 58992a833a782e6ae3bcc7f4ed355715e3e2c0c7db36bd6d3aa0544b29905dcc
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
- cloud-resilience
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Application/Data Integration Standard (NCDIT: Application/Data Integration Standard)

## At a glance

The statewide standard for application and data integration (middleware).

## Full text

State of North Carolina
Application/Data Integration Standard
Statewide IT Standard

Version 1.0
March 25, 2025

                                                                             State of North Carolina

Document Information
Revision History

 Date               Version         New or Revised      Description           Author
                                    Requirement

 8/1/2024           1.0             New                 Standard Approved     Chris Brittingham

 3/25/2025          1.0             Revised             Boomi link updated    Chris Brittingham

Document Details

 Department Name              Middleware Team

 Title                        Application/Data Integration Standard

 Publication Date             March 25, 2025

 Next Release                 March 24, 2026

 Document Type                PDF

 Document Number              1

 Version                      1.0

Version 1.0                                                2                        March 25, 2025

                                                                                                             State of North Carolina

Table of Contents
Document Information .................................................................................................. 2
  Revision History ........................................................................................................... 2
  Document Details ......................................................................................................... 2
Purpose .......................................................................................................................... 4
Owner ............................................................................................................................. 4
Scope ............................................................................................................................. 4
Standards....................................................................................................................... 4
  New Agency Application Implementations .................................................................... 4
  Existing Agency Application Implementations .............................................................. 5
Roles and Responsibilities ........................................................................................... 5
  NCDIT Application Integration Platform Service Owner ............................................... 5
  Application Owner ........................................................................................................ 5
Regulations and Applicable Laws ............................................................................... 5
Standard Review Cycle ................................................................................................. 6
Definitions ...................................................................................................................... 6
  Application Programming Interface (API) ..................................................................... 6
  Enterprise API .............................................................................................................. 6
  File-Based Batch Integrations ...................................................................................... 6
  NCDIT Boomi API Catalog ........................................................................................... 6
References ..................................................................................................................... 7

Version 1.0                                                      3                                                   March 25, 2025

                                                                          State of North Carolina

Purpose
The purpose of this document is to establish the application/data integration standards
for enterprise data and application integration services for all agencies when data needs
to be shared between two applications and the agency has not previously identified an
application integration solution and is not currently using an application integration
solution.

Owner
N.C. Department of Information Technology – Middleware Team

Scope
This standard is applicable to all state agencies and vendors and supports the approach
to establish a unified data integration strategy.

The standard is also applicable to any technical requirements providing application data
integration, message brokers, or any other means of interaction with applications.

Standards
New Agency Application Implementations

New agency application implementations are subject to the requirements of this standard:

         1. Agency applications requiring application interfacing are recommended to use
            the Boomi application programming interface (API) gateway* for data
            integration services when a data integration solution has not been identified
            and is not currently in use.
         2. All agencies must use the Boomi API gateway and its management capabilities
            to manage APIs when an existing data integration solution does not exist.
         3. The Boomi API gateway affords the opportunity to establish a library of shared
            APIs between applications for the enterprise.
                   a. It is recommended that all API developers (vendors, contractors,
                       employees) seeking an interface between applications look to
                       existing shared APIs within the NCDIT Boomi API catalog to find a
                       solution.
                   b. To improve API sharing between applications while developing new
                       APIs, the API design must be reviewed by NCDIT Enterprise
                       Architecture and shared with the Enterprise Security and Risk
                       Management Office, the Office of Privacy and Data Protection, and
                       the Data Division prior to being published to the NCDIT Boomi API
                       catalog.

Version 1.0                                  4                                   March 25, 2025

                                                                         State of North Carolina

                  c. It is recommended that the API owner adds the API to the NCDIT
                     Boomi API Catalog. Once added, the API owner controls who the
                     API is shared with within the NCDIT Boomi API catalog.

* Features and benefits of the Boomi Platform can be found in the References

Existing Agency Application Implementations
Existing agency technology solutions that utilize data integration services/capabilities
other than Boomi do not need to rewrite their data integration to incorporate Boomi.

Existing agency technology solutions that utilize data integration services/capabilities
other than Boomi and are undergoing modernization are recommended to:

         1. Use the NCDIT Boomi API gateway for integration and full API lifecycle
            management when a data integration solution has not been identified and is
            not currently in use.
         2. Use API based integration instead of file-based batch integration, when
            feasible.

Roles and Responsibilities
NCDIT Application Integration Platform Service Owner
The NCDIT Application Integration Platform Service Owner is responsible for managing
one or more services for agency consumption throughout the entire lifecycle, including
applications supporting delivery of the service(s).

Application Owner
The application owner is responsible for managing the application throughout the entire
lifecycle.

Regulations and Applicable Laws
The following reference sections in the N.C. General Statutes provide additional
information with respect to compliance of state law:

    •    N.C.G.S. § 143B-1320

    •    N.C.G.S. § 143B-1321

    •    N.C.G.S. § 143B-1325

    •    N.C.G.S. § 143B-1350 (a)

Version 1.0                                5                                    March 25, 2025

                                                                         State of North Carolina

    •    N.C.G.S. § 143B-1370 (a)

    •    N.C.G.S. § 143B-1376

    •    N.C.G.S. § 143B-1377

    •    09 NCAC 06b.0701

Standard Review Cycle
The Application/Data Integration Standard will undergo a periodic review at annual
intervals, or as changes are required.

Any identified changes, or outdated information within the standard will be addressed
promptly. This may involve revisions, additions, or removals as needed to ensure that
policies remain current and relevant.

Definitions
Application Programming Interface (API)

API stands for application programming interface, which is a set of definitions and
protocols for building and integrating application software.

Enterprise API

API that is leveraged across agency divisions/sections or across agencies.

File-Based Batch Integrations
File-based batch integration allows data to be moved offline at scheduled periods of time
between different data sources without necessarily connecting directly to them.

NCDIT Boomi API Catalog

NCDIT Boomi API catalog is a library of enterprise APIs, that allows users to
strategically manage, promote, and share APIs with relevant applications, developers,
and end-users.

Version 1.0                                 6                                   March 25, 2025

                                      State of North Carolina

References
Boomi Platform Information Page

Version 1.0                       7          March 25, 2025

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
