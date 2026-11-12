---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-waiver
title: Waiver Policy
doc_type: policy
citation: MaineIT Waiver Policy
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/Waiver.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 480c977bbe4d2bb099cc0a8617a29f4d79111bed92883ad5f9737b7ba2a6e8b2
effective_date: null
source_version: 'Latest Revision Date: May 15, 2026'
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Waiver Policy (MaineIT Waiver Policy)

## At a glance

The process by which an exception to a policy, standard or procedure is requested, granted and tracked.

## Full text

                               Maine State Government
                  Department of Administrative & Financial Services
                       Office of Information Technology (OIT)

                                      Waiver Policy

1.0    Statement
       Adherence to policy, standards, and procedures is a necessary part of conducting
       State business. It is equally important to document the process for exceptions.

2.0    Purpose
       The purpose of this policy is to document the waiver workflow and compliance-
       tracking.

3.0    Applicability & Definitions
       This policy is applicable to all Office of Information Technology (OIT) issued
       policies, standards, and procedures. The following definitions are applicable to this
       policy:

3.1    Approved: A waiver has been approved by the Chief Information Officer (CIO) or
       authorized designee.
3.2.   Approved with Conditions: Depending on the context of the approval, there may
       be conditions formally connected to the approval.
3.2    Expired: A waiver has exceeded the time that was approved by the CIO. Should a
       waiver still be required, please follow the Waiver Extension provision in this policy
       below.
3.3    Modified: A waiver that has been changed to reflect current state of conditions
       which can be either Minor or Significant
3.4    Not Approved: A waiver request was denied by the CIO or authorized designee.
3.5    Replaced: A waiver extension has been filed and accepted by the CIO. This waiver is
       no longer active and is marked “Replaced.” The extension waiver will become the
       current waiver for the defined asset.
3.6    Satisfied: The CIO has approved the closure of the waiver based on evidence that
       explicitly shows that the waiver condition has been resolved. A waiver is a candidate
       for closeout if it meets the criteria specified in section 5.4 below.
3.7    Withdrawn: A waiver has been officially requested to be withdrawn, and the waiver
       is voided.
3.8    Waiver Close Out: A waiver which has been satisfied, or the asset has been formally
       decommissioned, and the associated artifacts to record detailed actions (Request for
       Change (RFC) and Enterprise Tickets) have been referenced to confirm the status.

4.0    Responsibilities
4.1.   The Chief Information Officer (CIO) is responsible for the enforcement of this policy.

                                         Page 1 of 5

                                           Waiver Policy

4.2.   The Enterprise Architect facilitates the waiver workflow.

4.3.   The Enterprise Architect must ensure that all updates are accurately reflected in the
       Enterprise Waiver Application Inventory to maintain accurate tracking of waivers
       and their associated assets.

4.4.   Those seeking a waiver are not permitted to proceed with their desired outcome
       until they receive an email from the Enterprise Architect on behalf of the CIO
       indicating the waiver has been approved. There is no transfer or accepting liability
       by the State of Maine involving a vendor product through a waiver being submitted,
       reviewed and approved by the CIO.

4.5.   Those seeking a waiver must ensure that the business owner identified in section
       5.1.1 supports the waiver request, understands and accepts the risk, and supports
       the remediation strategy to achieve standard/policy compliance within the
       timeframe specified.

5.0    Directives
5.1.   The waiver application is initiated by including any relevant documentation within
       an Enterprise Ticketing System ticket and detailing the answers to the following
       items (5.1.1 through 5.1.8) within the body of an email to
       OITEnterpriseArchitect@Maine.Gov (see Appendix A). Scans must be attached to an
       Enterprise Ticketing System ticket and noted in sections 5.1.7. or 5.1.8.

       5.1.1. State the department and agency requesting the waiver and the full name(s)
              of the individual(s) requesting the waiver, the IT Manager approving the
              request to move forward, and the business owner accepting the risk
              identified in the waiver request.
              5.1.1.1. The identified business owner must have the authority within their
                       organization to form a binding agreement with the OIT CIO.
              5.1.1.2. The identified IT Manager must be an IT Director, or a designee
                       authorized on their behalf.
              5.1.1.3. The three individuals identified as the requestor, IT Manager, and
                       business owner must be different.
              5.1.1.4. Please explicitly copy the individuals listed above in the waiver
                       application.

       5.1.2. Identify the policy or standard 1 for which the waiver is being requested.

       5.1.3. Describe what risk is being waived by this request, and why the waiver is
              needed.
              5.1.3.1. Provide the compelling technical or business justification for the
                       policy exception.

1 https://www.maine.gov/oit/policies-standards

                                             Page 2 of 5

                                              Waiver Policy

                5.1.3.2. Describe the impact if the waiver is not approved.

        5.1.4. What are the business and technical risks to the State if the waiver is
               approved?

        5.1.5. State the duration of the waiver.

        5.1.6. All Waivers: Describe the exit strategy to satisfy the waiver and to bring the
               product into our standard offering and policy posture, which includes the
               exit strategy. Waivers must include the support model to be used until
               compliance is achieved.

        5.1.7. Security Waivers: When requesting a security waiver, provide the following:
               5.1.7.1. Application Inventory ID number of the application.
               5.1.7.2. The Enterprise Ticketing System ticket number that contains a
                        security scan no older than six months.
               5.1.7.3. An approximate number of both internal and external users, and
               5.1.7.4. The classification of the data transacted by the application (see the
                        Data Classification Policy). 2
               5.1.7.5. If the most recent security scan is older than six months, a new scan
                        must be requested, completed and evaluated by the Security
                        Operations Center (SOC) team prior to submitting a waiver request.
               5.1.7.6. Security scans completed by external parties must be submitted to
                        the SOC team through the Enterprise Ticketing System for further
                        evaluation.

        5.1.8. Digital Accessibility Waivers: When requesting an accessibility waiver,
               provide the following:
               5.1.8.1. The Application Inventory ID number of the application,
               5.1.8.2. The Enterprise Ticketing System ticket number that contains the
                        most recent accessibility scan, and
               5.1.8.3. An approximate number of both internal and external users.

5.2.    Approval or denial of the request will be made within three weeks of the submittal
        via email to the requestor and will include the individuals outlined in 5.1.1.
        Emergency requests will be handled in the same manner, only on an expedited scale.

5.3.    Before the expiration date of the waiver period, it is expected that corrective actions
        would have been undertaken to convert to an accepted policy standard. All requests
        for waiver extensions, with justifications, must meet the minimum requirements
        outlined in 5.1, above.

        5.3.1. If requesting a waiver extension, the request must cite the waiver number,
               title of the most-current waiver, and describe all progress toward

2 https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/DataClassificationPolicy.pdf

                                               Page 3 of 5

                                             Waiver Policy

                remediation that was made during the previous authorized waiver period. If
                remediation was not achieved, explain why.

5.4     A Waiver is a candidate for closeout if either:
        5.4.1 The underlying waived condition has been remediated, and the purpose of
              the waiver has been satisfied (see Applicability & Definitions, 3.0, above).
        5.4.2 The underlying information asset has been decommissioned.

        To request the closeout of a waiver, the requester must formally notify the
        Enterprise Architect that the waiver is no longer necessary, and the asset owner
        must confirm the current status of the asset. The requester is responsible for
        providing the following items to the Enterprise Architect through the formal email
        box OITEnterpriseArchitect@Maine.Gov:
        5.4.3 The Waiver number.
        5.4.4 The asset name.
        5.4.5 The documentary evidence behind the closeout request.
               5.4.4.1. The most common documentary evidence is the reference to a
                        Request for Change (RFC) number or a ticket in the Enterprise
                        Ticketing System.

6.0     Document Information
6.1.    Initial Issue Date: February 22, 2010
6.2.    Latest Revision Date: May 15, 2026
6.3.    Point of Contact: PolicyTeam.OIT@Maine.Gov
6.4.    Approved By: Chief Information Officer, OIT
6.5.    Legal Citation: Title 5, Chapter 163: Office of Information Technology 3.
6.6.    Waiver Process: N/A

3 http://legislature.maine.gov/statutes/5/title5ch163sec0.html

                                               Page 4 of 5

                                          Waiver Policy

Appendix A: Sample of Required Information Table for Waiver Requests. (This can be
copied and pasted into the body of an email to: OITEnterpriseArchitect@Maine.Gov)

Bold: Required Information | Plain text: Example (for reference)

5.1.1 Department, Agency, Requestor, IT Manager, and Business Owner:

Department: Department of X

Agency: Bureau of Administrative Systems

Requestor: Jane Doe, IT Analyst, Dept. of X

IT Manager: John Smith, IT Director

Business Owner: Sarah Johnson, Deputy Commissioner, Dept. of X

5.1.2 Policy or Standard Provision Impacted:

Identi�ication Authentication Policy – Section 8.1.4. (Multifactor Authentication Requirement)

5.1.3 Justi�ication:

Legacy payroll system cannot support MFA; denial would delay payroll processing.

5.1.4 Risks:

Increased risk of unauthorized access; mitigated by enhanced monitoring and restricted access.

5.1.5 Duration:

6 months (Jan 1 – Jun 30, 2026)

5.1.6 Exit Strategy:

Vendor upgrade scheduled for Q2 2026; support team will provide temporary monitoring until
replacement.

5.1.7 Security Waivers:

App ID: 789; Assyst #654321;

120 internal / 40 external users;

Data: TLP Amber

5.1.8 Accessibility Waivers:

Assyst #987654; 75 internal / 300 public users

                                              Page 5 of 5

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
