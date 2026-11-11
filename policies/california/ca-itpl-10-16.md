---
schema_version: 1
corpus: states-it-governance
jurisdiction: california
id: ca-itpl-10-16
title: Server Virtualization
doc_type: policy
citation: ITPL 10-16
authority_level: ''
issuing_body: Office of the State CIO
source_url: https://www.cdt.ca.gov/wp-content/uploads/2021/03/ITPL_10-16_Server_Virtualization_Final.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 474b14f807662a09eaedeee2c7ac0b0d8e010d6cbe17a86e726bf5130a654e36
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Server Virtualization (ITPL 10-16)

## At a glance

ITPL 10-16 (issued 12/17/2010 per the table), 'Server Virtualization': an Information Technology Policy Letter of the Office of the State CIO, marked Active on the Technology Letters page's Information Technology Policy Letters table.

## Full text

OFFICE OF THE STATE CIO
                                                                                    NUMBER:

IT POLICY LETTER                                                                    ITPL 10-16
SUBJECT:                                                                            DATE ISSUED:
SERVER VIRTUALIZATION
                                                                                    DECEMBER 17, 2010
Emphasis: Consolidation of server workload onto high capacity
servers                                                                             EXPIRES:

                                                                                    Until Rescinded
REFERENCES:                                                                         ISSUING AGENCY:
Government Code Section 11545
                                                                                    OFFICE OF THE STATE CHIEF
Chapter 404, Statutes of 2010                                                       INFORMATION OFFICER
Information Technology Policy Letters 09-06, 10-14, and 10-15
Statewide Information Management Manual Sections 18C, 58D,
and 158

Note: Agency Chief Information Officers (Agency CIO) and Department Chief
Information Officers (CIO) are requested to forward a copy of this Information
Technology Policy Letter (ITPL) to their respective Procurement Managers,
Project Management Office(s) and Information Technology (IT) Project Managers.

DISTRIBUTION                Agency Secretaries
                            Department Directors
                            Agency Chief Information Officers
                            Department Chief Information Officers

PURPOSE                     Within California State Government, the past practice was to dedicate
                            one physical server to a single workload, which resulted in chronic
                            underutilization, an expanding data center footprint, and excessive data
                            center power consumption. Building on efforts to strengthen the
                            Statewide Enterprise Architecture (EA) Program, and in support of
                            energy consumption reduction goals identified in Chapter 404, Statutes
                            of 2010 (AB 2408), the purpose of this ITPL is to:
                                     Formally establish the use of server virtualization software in
                                     California State Government as an acceptable practice.
                                     Remind all state agencies1 of the requirement to utilize the EA
                                     Server Virtualization Software Standard that is published in
                                     Section 58D.1 of the Statewide Information Management Manual
                                     (SIMM) as Technical Reference Model (TRM) 4.17.865.001.
                                     Remind all state agencies of the suggested EA Server
                                     Virtualization Practice that is published in Section 158A of the
                                     SIMM as TRM 4.17.865.002.
                                     Announce updates to the Information Technology Acquisition
                                     Plan (ITAP) Request Excel template and XML Schema included
                                     in Section 18C of the SIMM.

1
  When capitalized, the term “Agency” refers to one of the state’s super Agencies such as the State and Consumer
Services Agency or the Health and Human Services Agency. When used in lower case, the term “agency” refers to
any office department, board, bureau, commission or other organizational entity within state government. Within this
ITPL, “agency” and “department” are used interchangeably.
                                                                                                                       1

BACKGROUND                   Within the authority of Government Code (GC) Section 11545, the Office
                             of the State Chief Information Officer2 (OCIO) has responsibility and
                             authority for the establishment and enforcement of state information
                             technology policy in California State Government. This includes
                             establishing and enforcing state IT strategic plans, policies, standards,
                             practices, and EA.
                             In addition, Chapter 404 specifies statewide efforts to reduce energy
                             consumption by 20 percent below the 2009 baseline by July 1, 2011,
                             and by 30 percent below the 2009 baseline by July 1, 2012.
                             ITPL 10-15, Enterprise Architecture Standards and Procedures, included
                             a requirement to comply with the EA Standards in SIMM Section 58D,
                             which includes server virtualization software. Server virtualization
                             software allows the consolidation of new and existing workloads
                             distributed over multiple servers onto fewer high capacity servers.
                             Consolidating workloads onto high capacity servers reduces the physical
                             server inventory, which in turn decreases the associated footprint and
                             power consumption.

POLICY AND                   Agencies shall utilize virtualized server environments in accordance with
PROCESS                      the EA Server Virtualization Software Standard published in Section
                             58D.1 for new workload, increases to existing workload, and server
                             refreshes.
                             The ITAP process established pursuant to ITPL 09-06 will be used to
                             review and validate compliance with this policy.

EXCEPTIONS                   In the event of an emergency as defined in Public Contract Code
                             Section 1102, agencies may conduct acquisitions for IT goods and
                             services with an aggregate value of $25,000 or less without an approved
                             ITAP3. Such acquisitions may be conducted with concurrent notification
                             to the OCIO Program Management Office (PMO).

APPLICABILITY                All state agencies under the direct executive authority of the Governor’s
                             Office are required to comply with this policy.

SAM AND SIMM                 Updates to the SAM and the SIMM concerning ITAPs, virtualization and
CHANGES                      EA Standards and EA Practices were previously announced in the
                             following ITPLs:
                                      ITPL 09-06, Promoting Efficient and Effective Use of IT
                                      through Acquisition Planning – Included an announcement
                                      that the SIMM Section 18C, IT Acquisition Plan, was established
                                      to add the ITAP Request Excel Template and XML Schema.
                                      Please note: The ITAP Request Excel Template and the XML
                                      Schema have been updated to change Fiscal Year references
                                      from 2009-10 to 2010-11.
                                      ITPL 10-14, Data Center Assignments and Consolidation –

2
  Effective January 1, 2011, the Office of the State Chief Information Officer (OCIO) is renamed the California
Technology Agency (CaTA).
3
  An emergency is defined in the Public Contract Code 1102 as a “sudden, unexpected occurrence that poses a clear
and imminent danger, requiring immediate action to prevent or mitigate the loss or impairment of life, health, property,
or essential public services”. SAM Section 6560, specifies that emergency expenditures cannot exceed $25,000,
unless approved by the Department of Finance.
                                                                                                                      2

                   Included an announcement that the SAM Section 4819.2,
                   Definitions, would be updated to include a definition for
                   Virtualization.
                   ITPL 10-15, Enterprise Architecture Standards and
                   Procedures – Included the following announcements:
                       o   An update to the SAM Section 4906, Enterprise
                           Architecture, to include narrative regarding agency
                           compliance with the EA Standards and EA Practices.
                       o   The addition of SIMM Section 58D, Enterprise
                           Architecture Standards, that agencies must comply with,
                           which included the EA Server Virtualization Software
                           Standard TRM 4.17.865.001 in SIMM Section 58D.1.
                       o   The addition of SIMM Section 158, Enterprise
                           Architecture Practices, that agencies are encouraged to
                           follow, which included the EA Server Virtualization
                           Practices TRM 4.17.865.002 in SIMM Section 158A.
               An informational copy of the SAM updates released in the ITPLs
               previously referenced is included in this ITPL as Attachment A.
               Similarly, the SIMM content is available at:
               http://www.cio.ca.gov/Government/IT_Policy/SIMM.html.

CONTACT     Questions regarding EA should be directed to Lee Mosbrucker, Deputy
            Director for Enterprise Architecture, at (916) 403-9624, or by e-mail at
            Lee.Mosbrucker@state.ca.gov.
            Questions regarding Virtualization should be directed to Carol Kelly,
            Project Director, Consolidation, Office of the State Chief Information
            Officer by e-mail at Carol.Kelly@state.ca.gov.
            Questions regarding ITAPs should be directed to your OCIO PMO
            representative. A listing of PMO Managers and Principals, their
            departmental assignments, and department delegated cost thresholds
            can be found at the OCIO Web site located at:
            https://cdt.ca.gov/project-approvals-and-oversight-contact/

SIGNATURE
            _______/s/__________________________
            Christy Quinlan,
            Acting Chief Information Officer
            State of California

                                                                                       3

                                                                                  Attachment A

4819.2 DEFINITIONS
(Revised xx/10)

Virtualization: A framework or methodology of dividing the resources of a computer into
multiple execution environments, by applying one or more concepts or technologies such as
hardware and software partitioning, time-sharing, partial or complete machine simulation,
emulation, quality of service, and many others.

4906 ENTERPRISE ARCHITECTURE
(Revised XX/10)

The statewide Enterprise Architecture (EA) is developed in a cooperative, managed, and
coordinated effort facilitated by the California Technology Agency. The National Association of
State Chief Information Officers methodology and the Federal Enterprise Architecture
framework included in SIMM Section 58A are adopted as the state’s standards to develop and
maintain the statewide EA.

Accordingly, state agencies shall implement EA in accordance with SIMM Section 58. This
includes complying with the EA Standards in SIMM Section 58D. In addition, state agencies
shall, to the extent practical, utilize the EA Practices included in SIMM Section 158.

                                                                                                  4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
