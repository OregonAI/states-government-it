---
schema_version: 1
corpus: states-government-it
jurisdiction: idaho
id: id-ita-s6040
title: S6040 – Firewall Change Request
doc_type: standard
citation: ITA Standard S6040
authority_level: ''
issuing_body: Idaho Technology Authority (ITA)
source_url: https://ita.idaho.gov/wp-content/uploads/2026/10/s6040.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: c28d898d863a9bb3661d5ba195990f55ea5336edc007ef122c8dfc0a308487e1
effective_date: '2026-05-05'
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

# S6040 – Firewall Change Request (ITA Standard S6040)

## At a glance

Item of the ITA statewide policies, standards and guidelines library (ita.idaho.gov/policies), category '6000 - Security, Standards', a standard. The library's own summary: "The S6040 Firewall Change Request standard establishes requirements for assessing, submitting, reviewing, approving, and documenting firewall changes to ensure secure network access, consistent risk management, and compliance with Idaho Technology Authority security policies."

## Full text

Idaho Technology Authority (ITA)

ENTERPRISE POLICIES – P4500 SECURITY - COMPUTER AND
OPERATIONS MANAGEMENT

Category:     S6040 - FIREWALL CHANGE REQUEST

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

I. DEFINITION

   See ITA Guideline G105 (Glossary of Terms) for any definitions. G105-ITA Glossary of
   Terms

II. RATIONALE

   Firewalls protect state systems by limiting network access and reducing exposure to
   threats. Because changes to Ports, Protocols, and Services (PPS) directly affect security
   risk, they must be carefully reviewed, documented, and approved. A standardized
   change process ensures consistent application of a deny‑by‑default posture, supports
   enterprise risk management, and maintains alignment with ITA policies and NIST
   guidance.

III. APPROVED STANDARD(S)

   Firewall Change Request Process:

   1. Risk Assessment: Agencies must perform an internal risk assessment for any new
      PPS policy or modification, documenting residual risk and business justification.

   2. Submission: The request must be submitted by the agency’s Cybersecurity
      Coordinator (or equivalent role) to initiate review.

S6040 – Firewall Change Request                                                  Page 1 of 3

   3. Coordination: Coordination will involve relevant stakeholders across the security
      stack (e.g., network, firewall, LAN/WAN, cloud security) as appropriate for the
      request. Not all requests route through the Firewall Management Team initially;
      involvement depends on the devices and scope affected.

   4. Approval Workflow:

       a. Standard changes follow the agency Change Advisory Board (CAB) process.
       b. Emergency changes may bypass formal CAB approval but still require informal
       approvals from ITS and other impacted security stack owners before implementation.
       c. The duration of emergency PPS changes is dependent on the nature of the
       request and subsequent approvals; some changes may extend beyond 10 working
       days if justified and documented.

   5. Documentation: All approvals—formal or informal—must be documented in the
   change record for audit purposes.

IV. APPROVED PRODUCTS(S)

   Refer to approved state contracts for IT Security Products:
   https://purchasing.idaho.gov/statewide-contracts/

V. JUSTIFICATION

   This standard establishes a uniform process for requesting and approving firewall
   changes across Executive Branch agencies. A consistent approach reduces
   configuration errors, promotes coordinated risk management, and ensures firewall
   modifications support statewide security objectives and ITA governance requirements.

VI. TECHNICAL AND IMPLEMENTATION CONSIDERATIONS

   Agencies must confirm that requested PPS changes are accurate, necessary, and
   compatible with existing network and security architecture. Requests should include
   required documentation such as risk analysis, system dependencies, and rollback
   considerations. Implementation timelines may vary based on complexity and required
   coordination. All changes must be tested to verify proper function and prevent
   unintended exposure.

VII. EMERGING TRENDS AND ARCHITECTURAL DIRECTIONS

   Firewall capabilities are shifting toward zero trust principles, cloud-native controls, and
   centralized policy management. Trends such as micro‑segmentation, identity‑aware
   enforcement, software-defined networking, and SASE will increasingly influence
   statewide architecture. Agencies should prepare for continued modernization and
   anticipate adjustments to firewall change processes as enterprise security evolves.

S6040 – Firewall Change Request                                                       Page 2 of 3

VIII. PROCEDURE REFERENCE

   Firewall Change Request: https://idahoits.servicenowservices.com

   NIST SP 800-30 (Most current) (Guide for Conducting Risk Assessments)

   NIST SP 800-41 (Most current) (Firewall Policy)

   Enterprise ITA Policy P4570 (Firewall Security)

   Enterprise ITA Policy P4140 (Cybersecurity Framework)

   Enterprise ITA Guideline G535 (Firewall Configuration Guidelines)

IX. REVIEW CYCLE

   3 years

X. CONTACT INFORMATION

   For more information, contact the ITA Staff at (208) 605-4064.

   To report an incident, send email to: cyber@its.idaho.gov or call (208) 605-4000.

REVISION HISTORY

   05/05/2026 – Was previously G536, updates finalize definitions, clarify standard and
   emergency change workflows, refine technical and documentation requirements, and
   align terminology and formatting.

                     Effective Date: May 5, 2026

S6040 – Firewall Change Request                                                  Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
