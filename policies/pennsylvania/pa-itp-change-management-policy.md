---
schema_version: 1
corpus: states-government-it
jurisdiction: pennsylvania
id: pa-itp-change-management-policy
title: Change Management Policy
doc_type: policy
citation: 'Commonwealth of Pennsylvania IT Policy: Change Management Policy'
authority_level: ''
issuing_body: Office of Administration, Office for Information Technology
source_url: https://www.pa.gov/content/dam/copapwp-pagov/en/oa/documents/policies/it-policies/change%20management%20policy.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 946b0769d65783febb560f09ba3ce384d3dc1542304e8b44ae92170d10bac177
effective_date: '2026-03-05'
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
- oversight
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Change Management Policy (Commonwealth of Pennsylvania IT Policy: Change Management Policy)

## At a glance

Information Technology Policy of the Office of Administration for agencies under the Governor's jurisdiction. Printed purpose: This Information Technology Policy (ITP) establishes and maintains the policy, responsibilities, and procedures for Change Management maintenance, specifically the creation of change Blackout periods and Maintenance Windows, on the Commonwealth’s enterprise information technology platforms.

## Full text

                          Change Management Policy

          Effective Date:                                          Category:
          March 05, 2026                                           Systems Management

          Scheduled Review:
          March 2027

1. Authority
Executive Order 2016-06, Enterprise Information Technology Governance

2. Document Control
This document replaces, in its entirety, the Change Management Policy, dated January 6, 2025.

3. Purpose
This Information Technology Policy (ITP) establishes and maintains the policy, responsibilities,
and procedures for Change Management maintenance, specifically the creation of change Blackout
periods and Maintenance Windows, on the Commonwealth’s enterprise information technology
platforms.

4. Scope
This policy applies to all offices, departments, boards, commissions, and councils under the
Governor’s jurisdiction and any other entity connecting to the Commonwealth Network
(hereinafter referred to as "agencies").

5. Policy
For definitions found within this document, refer to the IT Policy Glossary.

The Office of Administration, Office for Information Technology (OA/IT) established the
following maintenance procedures to ensure that Enterprise Services are available during the
most critical and heavily used time periods:

   •   Maintenance Windows (predetermined dates and times for scheduled maintenance)

   •   Blackout Windows (designated periods during which non-emergency changes are restricted or
       prohibited)

All changes shall be documented and approved in the Enterprise IT Service Management

                                                                                    Page 1 of 4

(ITSM) tool prior to implementation. OA/IT staff shall frequently check the enterprise ITSM
tool to carefully review, ask questions, assess the risk of change, work to minimize system
down time, and if appropriate approve enterprise changes. OA/IT staff should assign a delegate
in the enterprise ITSM tool to review change tickets if they are absent from work or otherwise
unavailable to conduct the reviews.

Approved Enterprise Changes (those Enterprise Change Requests which have been approved in
the Enterprise ITSM tool) shall be implemented on a weekly basis during a scheduled
"Enterprise Maintenance Window". The dates and times for implementation of enterprise
maintenance are detailed in Enterprise Maintenance Windows Standard.

   5.1 Maintenance Outside Approved Windows
   Enterprise Maintenance that cannot be scheduled during one of the routine scheduled
   Maintenance Windows requires approval from the Enterprise Change Advisory Board (CAB)
   or designated Enterprise Management￼.

   Emergency changes or maintenance are exempt from Maintenance Windows or Blackout
   restrictions; however, they require approval from Enterprise Emergency CAB and the
   technical area where the emergency is taking place.

   All high-risk changes shall generate a notification to the Chief Information Security Officer
   (CISO) or delegate.

   All changes involving security Configuration Item (CI) shall require CISO or delegate approval.

   Scanning activities are not considered maintenance and not subject to Maintenance
   Windows or Blackouts.

   5.2 Limited, Shared Infrastructure and Comprehensive Production Blackout Window
       Requests
        5.2.1 Limited

        A limited Blackout only affects a single Delivery Center, and the Blackout is limited to
        the Delivery Center requesting it. To request a limited Blackout, agencies shall
        complete the Change Blackout Request Form and e-mail the form to ra-
        oaetsocab@pa.gov.

        Changes submitted during a limited Blackout will require the Blackout agency
        approval only if a Configuration Item (CI) referenced on the change request is related
        to the agency that has the Blackout maintenance. Agency or Delivery Center Change
        Managers in coordination with the Enterprise Change Manager will determine if the
        change requests can be accommodated.

             Scenario 1: If Pennsylvania State Police (PSP) has a limited Blackout and the
             Department of Corrections (DOC) is creating a change request within the PSP
             blackout window, and the affected CIs do not relate to PSP, no PSP Blackout
             approval is required.

             Scenario 2: If PSP has a limited Blackout and the DOC is creating a change

                                                                                     Page 2 of 4

            request within the PSP Blackout window, and the affected CIs relate to PSP, a PSP
            Blackout approval is required.
        5.2.2 Shared Infrastructure
        OA/IT manages Shared Infrastructure. The Blackout processes for Shared
        Infrastructure work as detailed in the following scenarios:

            Scenario 3: If OA/IT has a limited Blackout (not comprehensive) and PSP is
            creating a change request within the OA/IT Blackout window, and the affected
            CIs do not relate to OA/IT managed CIs, no OA/IT Blackout approval is needed.

            Scenario 4: If OA/IT has a limited Blackout (not comprehensive) and PSP is
            creating a change request within the OA/IT Blackout window, and the affected CIs
            relate to OA/IT managed CI’s, an OA/IT Blackout approval is required.

            Scenario 5: If DOC has a Blackout, and PSP is creating a change request
            within DOC Blackout window, and the affected CIs are on Shared
            Infrastructure at OA/IT on which DOC is operating, a DOC Blackout approval
            is required.

        5.2.3 Comprehensive
        No maintenance can be performed by any agency during a comprehensive Blackout
        period. Usually, these occur during critical events within the Commonwealth
        (elections, official state visits, etc.).

        If a comprehensive Blackout is required, the requesting agency shall provide the
        Enterprise Change Manager with a thirty (30) business-day notice prior to the
        Blackout window.

        The agency shall complete the Change Blackout Request Form and send it to ra-
        oaetsocab@pa.gov. Agency or Delivery Center Change Managers and Enterprise
        Change Manager will determine if a change can be accommodated and respond to the
        agency.

        When it is determined that a comprehensive Blackout for all maintenance is needed,
        approvals must be obtained from the Commonwealth Chief Technology Officer (CTO).
        The Enterprise Change Managers will post this Blackout in the Enterprise ITSM tool
        once approval is received.

        If a comprehensive Blackout is approved, change submitters will be unable to submit
        any non-emergency changes in the Enterprise ITSM tool.

   5.3 Override Authority
   The Commonwealth’s Chief Information Officer (CIO), CTO, or CISO have the authority
   to override a Blackout rejection via the Enterprise CAB process. In addition, the
   Commonwealth’s CIO, CTO, or CISO has the authority to delay and/or block any change
   to mitigate risks associated with changes.

6. Contact
Questions or comments may be directed via email to OA, IT Policy.

                                                                                    Page 3 of 4

7. Exception from Policy
In the event an agency chooses to seek an exception from this policy, a request for a policy
exception shall be submitted via the IT policy exception process. Refer to IT Policy
Governance Policy for guidance.

8. Revision History
This chart contains a history of this publication’s revisions. Redline documents outline the
revisions and are available to Commonwealth users only during the drafting process.

Version     Date          Purpose of Revision
Original    01/06/2025    Base Document
Original    03/05/2026    Minor clarifications and grammatical edits

                                                                                      Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
