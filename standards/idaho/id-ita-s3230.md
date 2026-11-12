---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s3230
title: S3230 – Security – Server Security Requirements
doc_type: standard
citation: ITA Standard S3230
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2025/07/s3230.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: b9fd033d37ec7e8a3242b61b7c82302a4296822a2ccc769cf36f6bdd2945229a
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# S3230 – Security – Server Security Requirements (ITA Standard S3230)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '3000 - Network and Telecommunications, Standards', a standard. The library's own summary: "ITA Standard S3230 mandates comprehensive security measures for servers to ensure data protection and system integrity."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE STANDARDS – S3000 – NETWORK AND
TELECOMMUNICATIONS

Category: S3230 – SECURITY – SERVER SECURITY REQUIREMENTS
_________________________________________________________________________
CONTENTS:
I.    Definition
II. Rationale
III. Approved Standard(s)
IV. Approved Product(s)
V. Justification
VI. Technical and Implementation Considerations
VII. Emerging Trends and Architectural Directions
VIII. Procedure Reference
IX. Review Cycle
X. Contact Information
      Revision History

I.   DEFINITION

Server security as used in this standard: a base configuration of server equipment that is
owned and/or operated by any state agency. This standard covers public-facing web servers
because of their exposure to internet attacks, but it also covers internal web servers as well as
other application servers, file servers, and database servers.

Public-facing server: any server which hosts a website or application which is accessible from
the internet.

II. RATIONALE

Idaho State government is responsible for protecting sensitive and business-critical information
on the government network. Each agency and the state government as a whole must ensure
safe practices are in place to reduce the risk that information will be lost, stolen or changed.
This standard provides direction on where to learn minimum configuration requirements for
securing servers to reduce their risk to the many different attacks and misuses that target
servers and the information they hold or process.

III. APPROVED STANDARD

Internet-accessible servers will be configured to meet minimum security requirements as
referenced in the series of Guidelines G950. This series will be under continuous development
in order to cover basic security configurations of common server operating systems and
function. The series will also be updated over time to better address changing security best
practices and industry standards.

S3230 – SECURITY – SERVER SECURITY REQUIREMENTS                                     Page 1 of 4

IV. APPROVED PRODUCTS

N/A.

V. JUSTIFICATION

The associated Guidelines, series G950, will provide minimum security configuration standards
for server administrators to use while managing their servers. Using these guidelines will help
provide better protection for sensitive state information as well as for citizen and employee
personal data that the state holds. Some agencies may choose to use or are required to use
stricter security standards; however, no agency may use less restrictive server configurations.

VI. TECHNICAL AND SECURITY IMPLEMENTATION CONSIDERATION

A. The G950 Series Guidelines will be developed in phases. The initial planned phases include
at least the following:
    1. Initial Operating System (OS) hardening
    2. MS SQL Server security
    3. Web services security basics
    4. More in-depth OS hardening

S3230 – SECURITY – SERVER SECURITY REQUIREMENTS                                  Page 2 of 4

B. Agencies are encouraged to implement these security measures in Tiers. The Tiers reflect
the servers which should be protected first based on their exposure to internet threats and their
proximity to potentially sensitive information. The graphic below shows these phases and tiers.
The Tiers include
   1. Public Facing servers on the internal state network
   2. Servers supporting those Internal Public Facing servers
   3. Public Facing Servers on the Enterprise Demilitarized Zone
   4. All other servers.

C. In general, this standard covers the first evolution of four planned evolutions which are
expected to take as much as five years to complete.
   1. Server security,
   2. Application security,
   3. IT training track options which will enhance security skills,
   4. Move all public-facing servers to the enterprise DMZ (unless a better option is developed)

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

In order to maintain secure server configurations, administrators should open only those ports
and enable only those services which are specifically required for applications on any given
server. Some Operating Systems are defaulted open; unnecessary ports and service must be
disabled; however, other OS’s, to include newer Microsoft Operating Systems, are defaulted to
a secure mode and the required ports and services must be enabled.

VIII. PROCEDURE REFERENCE

Guideline G590 Series.

S3230 – SECURITY – SERVER SECURITY REQUIREMENTS                                    Page 3 of 4

IX. REVIEW CYCLE

Six (6) Months

X. CONTACT INFORMATION

IT Services (ITS) Security Team, (208) 605-4000.

REVISION HISTORY

07/01/18 – Changed “OCIO” to “ITS”.

07/01/13 – Changed “ITRMC” to “ITA”.

      Approved by ITRMC June 23, 2010

S3230 – SECURITY – SERVER SECURITY REQUIREMENTS    Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
