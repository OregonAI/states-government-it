---
schema_version: 1
corpus: states-government-it
jurisdiction: west-virginia
id: wv-wvot-pr1013
title: WVOT Patch Management
doc_type: policy
citation: WVOT-PR1013
authority_level: ''
issuing_body: West Virginia Office of Technology (Chief Information Officer)
source_url: https://docs.google.com/document/d/1923XC1sdhyRyS5j00FyKSplvU5E6SXXs/export?format=docx
source_format: docx
retrieved: '2026-11-12'
source_sha256: c3ca5b3cebd2e33ca93b7885bffc9dae940a6151429df46c87fbe540d11d4c58
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: Text extracted from the Word file (.docx) with pandoc's docx reader, tracked changes
  accepted and the result rendered one line per paragraph, heading, list item and table row (a table row's
  cells are joined by ' | '; list markers are written out as the file numbers them, bullets as a bullet
  character; footnotes follow the text as [n]). Running headers and footers, pictures and the text inside
  text boxes (such as a cover-page title) are not read. Headings carry no markup.
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# WVOT Patch Management (WVOT-PR1013)

## At a glance

The Office of Technology's patch management procedure for Windows-based systems (security patches, software updates, drivers). The index marks it 'Under Review'; it is still the published procedure, so it is held. The title block (number, title, dates) is in the document's page header, which the Word reader does not read, so identity is checked by a phrase the body prints.

## Full text

PURPOSE

The purpose of this procedure is to ensure that the West Virginia Office of Technology (WVOT) meets the organizational objective of a secure, stable, and standardized computing environment for customer agencies. The WVOT is committed to the routine maintenance of its computing assets, as well as ensuring all Windows based systems are systematically kept up to date with the latest security patches, software updates, and/or relevant drivers. This ongoing maintenance is an integral part of maintaining both the security and availability of the State network.

SCOPE

This procedure applies to all systems that are maintained by WVOT, or connected to an agency network maintained by the WVOT Exceptions to this procedure must be specifically defined and approved by the WVOT.

PROCEDURE

Enterprise Patching

Patching to enterprise-wide applications (See Appendix A for a complete list) will occur on workstations/end-point devices at a minimum of every 30 days in order to remediate exposure to applicable security issues.

Microsoft Updates are released on the second Tuesday of each month, and will be tested prior to deployment.

Out-of-Band and Emergency Patching

Out of Band or emergency patches will be evaluated when issued by the vendor with an associated risk rating.

High - CVE rating of 10 and/or remotely exploitable

Medium - CVE rating between 5-9

Low - CVE rating less than 5

Patching will be applied based on the Common Vulnerabilities and Exposures (CVE) rating maintained in the National Vulnerability Database by NIST:

Ratings with High severity within seven (7) calendar days;

Medium severity within fifteen (15) calendar days; and

all others within thirty (30) calendar days.

Portable computers such as laptops and tablets must be connected to the agency network at least once every 10 work days.

The WVOT reserves the right to disable access for any device that has not connected to the agency network within the designated interval.

WVOT will review identified vulnerabilities and reserves the right to elevate any vulnerability rating and associated patches based on widespread exploitation or imminent threat to the environment.

All patches, when practical, and assets are available, are to be tested in a non-production environment prior to deployment to production

Maintenance that requires down time with state-wide impacts will be communicated in advance through the OT Communications email.

Any issues or problems related to a patch release should be documented and reported immediately to the WVOT Service Desk.

Due to the risk of sustaining operations there is the possibility that some patches or updates may be approved to be installed on a different schedule than this policy allows.

These will be evaluated on a case by case basis to be approved by WVOT with input from the appropriate support staff and agency contact.

Exceptions to the patch management policy will require documented approval from WVOT.

A WVOT Help Desk Ticket must be submitted by the Agency’s Designated Approval Authority (DAA) for all exceptions.

The specific machine ID/name must be provided in the ticket, and

The purpose for the exemption must be documented as well.

ENFORCEMENT

Not applicable to this document

DEFINITIONS

Chief Technology Officer (CTO) – The person responsible for the State’s information resources.

Employee – Individuals retained and authorized on a temporary or permanent basis by the State of West Virginia to perform a service. For the purposes of Information Technology and Security policy, the term “employee” shall include the following: contractors, subcontractors, contractors’ employees, volunteers, county health department staff, business associates, and any other persons who are determined and notified by the WVOT to be subject to this policy. This definition does not create any additional rights or duties.

West Virginia Office of Technology (WVOT)- The division of the Department of Administration established by WV Code § 5A-6-4a, et. seq., which is led by the State’s CTO and designated to acquire, operate, and maintain the State’s technology infrastructure. The WVOT is responsible for evaluating equipment and services, and reviewing information technology contracts.

Please find below a list of Enterprise-Wide software to be updated monthly:

• AD Self Service
• Adobe Air
• Adobe Flash
• Adobe Reader (DC)
• Anti-Virus/End-Point Protection
• Cisco AnyConnect VPN Client
• Firefox
• Java
• LAPS
• Microsoft BitLocker
• Microsoft Office
• Nomad - Wake-up, Night Watchmen
• Shockwave
• System Center

## Curator notes

Text extracted from the Word file (.docx) with pandoc's docx reader, tracked changes accepted and the result rendered one line per paragraph, heading, list item and table row (a table row's cells are joined by ' | '; list markers are written out as the file numbers them, bullets as a bullet character; footnotes follow the text as [n]). Running headers and footers, pictures and the text inside text boxes (such as a cover-page title) are not read. Headings carry no markup.
