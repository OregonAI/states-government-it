---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-cloud-tagging-labeling
title: Cloud Tagging Labeling Standard
doc_type: standard
citation: OMES Cloud Tagging Labeling Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/cloud-tagging-labeling-std-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 124043ffd616f16fd28fd8cb746295606600316d3d70d7379f16d8e74ff9dc0b
effective_date: '2026-07-28'
source_version: Last revised 07/16/2026
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
- governance
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Cloud Tagging Labeling Standard (OMES Cloud Tagging Labeling Standard)

## At a glance

A CIO standard in the 'IT Enterprise Governance' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: The purpose of this standard is to define the required tagging structure for all cloud resources so financial operations tooling can accurately interpret usage data. Correct tags facilitate cost- allocation, agency visibility, chargeback/showback reporting, financial compliance, and support transparent cloud expenditure management across OMES-managed environments.

## Full text

                       Cloud Resource Tagging and Labeling Standard

Introduction
This standard establishes mandatory, statewide tagging and labeling requirements for cloud
resources across Azure, AWS and Google Cloud Platform. Proper tagging ensures clear resource
ownership strengthens statewide governance practices and supports essential financial
transparency for Oklahoma cloud environments.

Purpose
The purpose of this standard is to define the required tagging structure for all cloud resources so
financial operations tooling can accurately interpret usage data. Correct tags facilitate cost-
allocation, agency visibility, chargeback/showback reporting, financial compliance, and support
transparent cloud expenditure management across OMES-managed environments.

Definitions
Tag/Label – metadata applied to a cloud resource in key-value format.

Agency number – the 3-digit state agency identifier associated with the resource (found in Agency
Overview on Oklahoma.gov).

Owner – the department/program responsible for the resource.

Application – the system or workload supported by the resource.

Life cycle – resource stage (development, testing, staging, production).

Cloudability – FinOps platform that uses tags to generate spend analytics, cost allocation,
chargeback/showback, and agency visibility.

Standard
Required tags/labels.
   • Agency.
           o Must contain only the official 3-digit agency number (e.g., 340, 265, 131).
           o The Agency tag is mandatory for every resource.
                  ▪ Placeholder values – 000 or 090 – are strictly prohibited when information is
                      unavailable.
                         • If unknown, do not deploy the resource until the correct agency
                             number is obtained.
                  ▪ 000 is designated only for shared servers, shared enterprise applications,
                      shared resource groups and projects involving more than one customer
                      agency. It is not intended for statewide infrastructure.
                  ▪ 090 is designated for shared statewide infrastructure, OMES‑ISD resources,
                      monitoring, security and infrastructure guardrails for cloud providers.
   • Owner.
           o Must identify the department or program area responsible for the resource.

           o   If complete information is unavailable at deployment, the Owner tag must still be
               provided.
                    ▪ It may represent the customer submitting the request or the team managing
                      the resource.
                    ▪ Owner is required for proper operational accountability.
   •   Application.
           o Specifies the application or workload associated with the resource.
           o If the application name is initially unknown, the resource may be deployed only if
               Agency and Owner are present and Application is added within 7 business days.
   •   Life Cycle.
           o Must specify development, testing, staging or production.
           o This tag must be updated as the resource transitions between environments.

Optional tags/labels.
   • Service team.
           o Identifies the service delivery team supporting the resource.
           o Helpful for operations and routing but not a mandatory tag.
   • Department.
           o Identifies the department within an agency responsible for the cost.

Additional tagging guidance.
   • Additional tags may be used to provide more detail, such as:
            o Environment (beyond life cycle).
            o Versioning.
            o Network configurations.
            o Dependencies.
            o Etc.
            o Optional tags may enhance automation, governance clarity and Cloudability
                reporting.

Updating tags later.
   • Tags may be updated, edited or modified at any time.
   • Updating is recommended when:
           o Ownership changes.
           o Applications evolve.
           o Resources move between life cycle stages
   • Maintaining accurate tags ensures Cloudability’s financial data remains correct and useful
       for agencies.

Tagging compliance.
   • Resources missing required tags may be clocked from deployment or flagged remediation.
   • Tag accuracy is critical for statewide financial governance and must be continuously
       maintained.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§ 34.11.1
and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended standards
policies and standards at any time. Compliance is expected with all published policies and
standards, and any published amendments thereof. Employees found in violation of this standard
may be subject to disciplinary action, up to and including termination .

Rationale
To ensure efficient, secure, and cost-effective delivery of essential public services, all state agency
IT purchases and projects must receive central approval. This allows the Chief Information Officer
to evaluate agency needs and capabilities, strengthen data protection and security, and streamline
and consolidate systems to reduce costs for taxpayers.

References
   • Agency Overview [Oklahoma.gov].

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 07/28/2026           Review cycle: Annual
 Last revised: 07/16/2026             Last reviewed: 07/16/2026
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
