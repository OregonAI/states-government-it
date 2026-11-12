---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-identity-management
title: Identity Management Standard
doc_type: standard
citation: OMES Identity Management Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/identity-management-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 94de7de8bc7c218fcdeb5f3e6744cee0b32fae3388a58d9bb112695c54ede346
effective_date: '2023-08-08'
source_version: Last revised 08/13/2026
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

# Identity Management Standard (OMES Identity Management Standard)

## At a glance

A CIO standard in the 'Security' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document defines the types of user accounts managed by OMES IS.

## Full text

                               Identity Management Standard

Introduction
User accounts are the only legitimate method by which OMES information systems may be
accessed. OMES Information Services actively manages user accounts to prevent illegitimate use
of state information systems. The use of authorization, identification and authentication controls
ensure that only known users make use of state systems. Without these controls, the potential
exists for information systems to be accessed illicitly, and the security of those information
systems could be compromised.

Purpose
This document defines the types of user accounts managed by OMES IS.

Definitions
   • Affiliate – worker who is not a state employee but serves in a supporting role to a state
        agency’s mission, typically at the county, local or municipality level.
   • Contractor – worker with economic independence who is in business for themselves but
        has been hired by the state to perform a particular function or produce a desired product.
   • Decentralized security representative (DSR) – individual, designated by the head of the
        agency, who is authorized to approve requests for their agency and state resources
        including creation of new user IDs, modification of user access and termination of user
        access.
   • Disabled account – inactive account requiring approval from an agency’s DSR to enable.
   • Employee – worker who is economically dependent on the business of the employer.
   • Expired account – elapsed account for a contractor that has exceeded the configured
        expiration date.
   • Interactive logon – an authentication process where a human user provides credentials
        directly to a computer to access its resources.
   • Locked-out account – account that is blocked from user access and requires the OMES
        Service Desk to unlock (e.g. password expiration or a user incorrectly entering a password
        too many times).
   • Terminated account – User ID for an inactive affiliate, contractor or employee that has been
        disabled and had all permissions removed.
   • User ID – unique login ID assigned to each user of state systems.

Standard
   • OMES IS ensures all users (affiliates, contractors and employees) are issued a user ID
      whose activity is uniquely identifiable on IT systems and is established through an
      authentication mechanism.
   • User accounts must be onboarded by and to the agency in which the contractor/employee
      has been hired.
   • Prior to user access modification, DSR approval shall be obtained and approved access
      shall be granted with least privilege.

   •   Enterprise systems are provisioned access by roles approved by the agency and system
       owner when applicable. Examples include PeopleSoft Financials and Workday@OK.
   •   Generic accounts are not permitted without CIO approval obtained through an exception
       request. Generic accounts have additional controls in place for accountability and a
       periodic review for their applicability.
   •   Access for new user ID access (onboarding) is requested via the OMES IS ticketing system
       and must be approved by the DSR.
   •   Access termination requests for departed employees (offboarding) are submitted
       automatically based on the termination date within Workday@OK. Access termination
       requests for interagency transfers, agencies not fully utilizing Workday@OK and
       contractors not in Workday@OK must be submitted by the user’s agency at the time of
       separation of employment and is requested via the OMES IS ticketing system.
   •   Contractor accounts shall be reviewed by the owning agency semi-annually to verify
       continued access is required.
   •   User IDs not utilizing interactive logon for logical or physical access to the system for 60
       days are verified against agency leave of absence reports prior to being disabled. Following
       a 30-day period of being disabled, the account is offboarded. Reactivation of the account
       requires an onboarding ticket to be submitted.
   •   Offboarded accounts are archived after a period of 30 days.
   •   To ensure proper access and continuity of business, individual user accounts shall not be
       used for shared resources, such as email or calendars. A dedicated resource for team or
       group activities must be requested.
   •   OMES employees are entitled to a single email account within the OMES mail domain
       regardless of their number of accounts within state systems.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§ 34.11.1
and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended standards
policies and standards at any time. Compliance is expected with all published policies and
standards, and any published amendments thereof. Employees found in violation of this standard
may be subject to disciplinary action, up to and including termination.

Rationale
To ensure efficient, secure, and cost-effective delivery of essential public services, all state agency
IT purchases and projects must receive central approval. This allows the Chief Information Officer
to evaluate agency needs and capabilities, strengthen data protection and security, and streamline
and consolidate systems to reduce costs for taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.

 Effective date: 08/08/2023           Review cycle: Annual
 Last revised: 08/13/2026             Last reviewed: 08/13/2026
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
