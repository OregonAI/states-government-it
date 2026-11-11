---
schema_version: 1
corpus: states-it-governance
jurisdiction: washington
id: wa-ea-02-09-s
title: 'Enterprise Service: Integrations'
doc_type: standard
citation: WaTech Standard EA-02-09-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2026-06/EA-02-09-S_Integrations.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 1d20377bf471221a8f307d1d1ff7c715bc455134debfcf545ffb75d66af3aa0b
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

# Enterprise Service: Integrations (WaTech Standard EA-02-09-S)

## At a glance

Item of the WaTech policy library, chapter '3. Enterprise Architecture' (listed as type Standards). Listed at https://watech.wa.gov/policies/enterprise-service-integrations.

## Full text

EA-02-09-S                                                                                Replaces:
State CIO Adopted: 6/11/2026                                                                   N/A
TSB Approved: 6/11/2026
Sunset Review: 6/11/2028

                             INTEGRATION SERVICES
                          ENTERPRISE SERVICE STANDARD
See Also:
RCW 43.105.006 WaTech Purpose
RCW 43.105.054 WaTech Governance
RCW 43.105.020 Definitions
RCW 43.105.450 State agency information technology security

1. PURPOSE
This standard establishes the statewide service capability, Integration Services, as an enterprise
service under EA-02 – Establishing an Enterprise Service Policy. Integration Services provides a
shared, centrally governed capability for secure, consistent, and scalable system integration and
data exchange across Washington state government. It supports legacy and modern systems
through file transfer, message brokering, and Application Programming Interface (API)-based
connectivity under a shared delivery and governance model.
Integration Services has been designated as an enterprise service to reduce fragmented, agency-
specific integration solutions and point-to-point connections. This enterprise service is intended
to reduce technical debt, increase delivery speeds, reduce manual processing, eliminate
duplicative development, and mitigate risk to enterprise security and operations.
A Washington state agency must not adopt, build, expand, or renew a service with similar
capabilities unless it has an approved waiver (see Section 5).

2. SCOPE

   IN SCOPE
   Integration Services must be used to connect systems and automate data exchanges for
   inter-agency state business operations when:
        •    Data moves between agencies or external partners.
        •    Reusable APIs or shared integration patterns are required.

   OUT OF SCOPE
        •    Ad-hoc, end-user file sharing or manual exchanges that do not establish an
             integration (e.g., email attachments or one-time manual uploads).
        •    One-time data extracts performed solely for reporting or analysis.
        •    Native product integrations when they operate within an approved system or agency
             boundary. This includes embedded reporting/analytics connections (such as Power
             BI).

                                                                                                 1

3. APPLICABILITY
This standard applies to all state agencies (as defined in RCW 43.105.020) and their
organizational users (including employees, contractors, partners, and vendors).
This standard does not apply to the K-20 network, institutions of higher education, the
legislature, the judiciary, or local governments (as defined in RCW 43.105.020).

4. ENTERPRISE SERVICE CAPABILITIES
Integration Services encompasses the following capabilities:
   1. Enterprise-managed secure file transfer and automated file exchange.
   2. Enterprise message routing and brokering (e.g., enterprise service bus) for system-
      to-system integration across agencies and shared services.
   3. Enterprise capabilities for reusable service-based interfaces (e.g., APIs) between
      agencies, shared services, and authorized external organizations
   4. Enterprise-managed connectivity to enable secure integration between systems
      operating across on-premises, cloud, and hybrid environments.

5. WAIVERS AND EXEMPTIONS TO THIS STANDARD
In accordance with POL-01-02-S Technology Policy and Standard Waiver Request Standard,
agencies may qualify for a waiver or exemption from compliance with this standard.
Agencies may request an exemption for situations that meet one of the following criteria.
   1. Systems with validated performance or latency requirements that cannot be met by
      Integration Services, including ultra-low latency operational workloads.
   2. Legal, regulatory, or compliance requirements that cannot be supported by the
      existing capabilities of the enterprise service.
   3. Specialized operational environments, including public safety systems, SCADA, or
      proprietary operational platforms requiring alternative integration approaches.
   4. Existing integration platforms that support critical statewide systems and data
      exchanges.

6. AUTHORITY
This standard is issued under the authority of RCW 43.105.054, which grants Washington
Technology Solutions authority to establish statewide technology standards and enterprise
services. RCW 43.105.006 establishes Washington Technology Solutions as the centralized
provider of broadly used and uniform technology services. RCW 43.105.450 requires state
agencies to comply with statewide information technology security policies and standards.

                                                                                            2

REFERENCES
   1. Service Catalog Page: Integration Services
   2. Definition of Terms Used in WaTech Policies and Reports
   3. EA-02 Establishing an Enterprise Service Policy
   4. MGMT-01-01-S Technology Portfolio Foundation – Application Standard
   5. POL-01-01-PR Technology Policies and Standards Waiver Procedure
   6. RCW 43.105.006 WaTech Purpose
   7. RCW 43.105.020 Definitions
   8. RCW 43.105.054 WaTech Governance
   9. RCW 43.105.450 State agency information technology security
   10. SEC-02-01-S Application Security Standard
   11. SEC-06 Access Control Policy
   12. SEC-06-01-S Identification and Authentication Security Standard
   13. SEC-08-01-S Data Classification Standard
   14. SEC-08-02-S Encryption Standard
   15. SEC-11-01-S Risk Assessment Standard

CONTACT INFORMATION
For questions about this policy, please email the WaTech Policy Mailbox.

                                                                            3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
