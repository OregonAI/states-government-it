---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-enterprise-patch-management-cc
title: Enterprise Patch Management
doc_type: standard
citation: 'Security Domain Compliance Component: Enterprise Patch Management'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Enterprise-Patch-Management.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 24a8ef257bd7f1e2a68fb10e9ff811e346a70ea30f39981029828f2493494cad
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

# Enterprise Patch Management (Security Domain Compliance Component: Enterprise Patch Management)

## At a glance

Row 'Enterprise Patch Management' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/enterprise-patch-management-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Under Review, not Approved, with Date Approved / Rejected 02/19/2025. OWNER DECISION, see left_out. The index lists it under Approved Standards; it is kept as a document on the index label as the status of record, and the owner may treat it as an under-review revision instead.

## Full text

                                      COMPLIANCE COMPONENT

                                                        DEFINITION
Name                   Enterprise Patch Management
                       Enterprise patch management is the process of identifying, prioritizing, acquiring,
                       installing, and verifying the installation of patches, updates, and upgrades throughout
Description
                       an organization. Patches, updates and upgrades are pieces of code developed to
                       address security flaws within an application or operating system.

Rationale              Enterprise patch management reduces or eliminates the potential for exploitation.

                       Potentially eliminates the exploitation of vulnerabilities.
Benefits

                                        ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name         Security
Specify the Discipline Name     Management Controls
Specify the Technology Area
                                System Life Cycle Security
Name
Specify the Product
Component Name

                                            COMPLIANCE COMPONENT TYPE
Document the Compliance
                                Guideline
Component Type
Component Sub-type

                                                  COMPLIANCE DETAIL
                                This document outlines possible risk response approaches for software
                                vulnerabilities, provides an overview of the software vulnerability management life
                                cycle, and takes a closer look at parts of that life cycle with respect to patching.

                                1. Risk Responses - Patching is one of several ways to respond to risks from
                                     software vulnerabilities.

                                     a. Accept the risk from vulnerable software as is.
State the Guideline, Standard
or Legislation                       b. Mitigate: Reduce the risk by eliminating the vulnerabilities and/or
                                           deploying additional security controls to reduce vulnerability exploitation.

                                     c. Transfer: Reduce the risk by sharing some of the consequences with
                                           another party.

                                     d. Avoid: Ensure that the risk does not occur by eliminating vulnerable
                                           assets.

                              2. Software Vulnerability Management Life Cycle - The following describes a
                                 basic software vulnerability management life cycle. This life cycle applies to all
                                 risk response approaches.
                                 a. Know when new software vulnerabilities affect your organization’s assets,
                                      including applications, operating systems, and firmware. Know what
                                      assets your organization uses and which software and software versions
                                      those assets run, down to the level of packages and libraries, as well as
                                      keeping track of new vulnerabilities in that software.
                                 b. Plan the risk response. Assess the risk the vulnerability poses to your
                                      organization, choose which form of risk response (or combination of forms)
                                      to use, and decide how to implement the risk response.
                                 c. Execute the risk response. Common phases include the following:
                                           i. Prepare the risk response.
                                           ii. Implement the risk response.
                                           iii. Verify the risk response. Ensure that the implementation has been
                                                  completed successfully.
                                           iv. Continuously monitor the risk response. Ensure that the risk
                                                  response continues to be in place.
                              3. Risk Response Execution – Below are the common phases of executing a
                                 risk response, specifically within the context of patching.
                                      a. Prepare to Deploy the Patch:
                                                   i. Prioritize the patch. Some patches will have a higher priority
                                                      than others based on their risk of vulnerability.
                                                  ii. Schedule patch deployment.
                                                 iii. Acquire and validate the patch. After acquiring the patch its
                                                      authenticity and integrity should be confirmed, preferably by
                                                      automated means, before the patch is tested or installed.
                                                 iv. Test the patch. Reduce operational risk by identifying
                                                      problems with a patch before placing it into production.
                                      b. Deploy the Patch - Common steps for deploying a patch include the
                                           following:
                                                i.    Distribute the patch. Distribution may be automatic, manual or
                                                      scheduled.
                                               ii.    Validate the patch. A patch’s authenticity and integrity should
                                                      be confirmed before installation, preferably through automated
                                                      means.
                                             iii.     Install the patch. Installation may be automatic, manual or
                                                      scheduled.
                                             iv.      Change software configuration as needed in order to properly
                                                      implement the patch.
                                               v.     Resolve any issues related to the implantation of the patch.
                              4. Verify Deployment - A patch’s deployment can be verified to ensure that it
                                 has been installed successfully and taken effect. The robustness of verification
                                 can vary a great deal and is largely dependent on an organization’s needs, but
                                 automated means are generally needed to achieve verification at scale.
                              5. Monitor the Deployed Patches In the last phase of the life cycle, the patch’s
                                 deployment can be monitored using automation to confirm that the patch is still
                                 installed.

                              This document shall be reviewed annually or as needed.
                              NIST SP 800-40, Version 4, Guide to Enterprise Patch Management Planning:
Document Source Reference #
                              Preventive Maintenance for Technology (Apr. 2022)

                                                 Compliance Sources
                                National Institute of
                                Standards and Technology                           http://csrc.nist.gov/
Name                                                                Website
                                (NIST), Computer Security
                                Resource Center (CSRC)
Contact Information             inquiries@nist.gov
Name                                                                Website
Contact Information

                                                  KEYWORDS
                                System Life Cycle, exploitation, bugs, vulnerabilities, malicious,
List Keywords                   remediation, maintenance, monitor, threats, holes, defects, bad code,
                                Patch and Vulnerability Group, PVG.
                                             COMPONENT CLASSIFICATION
Provide the Classification          Emerging                  Current                    Twilight          Sunset
     Sunset Date

                                           COMPONENT SUB-CLASSIFICATION
 Sub-Classification          Date                          Additional Sub-Classification Information
    Technology Watch
    Variance
    Conditional Use

                                      Rationale for Component Classification
Document the Rationale for
Component Classification
                                                     Migration Strategy
Document the Migration
Strategy
                                               Impact Position Statement
Document the Position
Statement on Impact

                                                     CURRENT STATUS
Provide the Current Status          In Development            Under Review               Approved          Rejected

                                                       AUDIT TRAIL
Creation Date                   07-06-06                      Date Approved / Rejected     02/19/2025
     Reason for Rejection
Last Date Reviewed              02/19/2025                    Last Date Updated            02/19/2025
     Reason for Update          Vitality

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
