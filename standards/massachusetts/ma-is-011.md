---
schema_version: 1
corpus: states-government-it
jurisdiction: massachusetts
id: ma-is-011
title: IS.011 Information Security Standard
doc_type: standard
citation: IS.011
authority_level: ''
issuing_body: Executive Office of Technology Services and Security, Enterprise Risk Management Office
source_url: https://www.mass.gov/doc/is011-information-security-standard-1/download
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 73ba0e851b58325c5e15c035a2b81106b95a3e0a9791b4d3224272ed7a2c6353
effective_date: '2018-10-15'
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
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# IS.011 Information Security Standard (IS.011)

## At a glance

One of the seventeen Enterprise Information Security Standards (IS.011 to IS.027) on EOTSS's Technology Standards and Guidelines page, which says executive branch agencies are required to conform to defined EOTSS policies and standards under Chapter 64 of the Acts of 2017. The page for the Information Security Standard carries a summary and this PDF is the standard.

## Full text

                   Commonwealth of Massachusetts
                   Executive Office of Technology Services and Security (EOTSS)
                   Enterprise Risk Management Office

                                    Information Security Standard
 Document Name: Information Security Standard                               Effective Date: October 15th, 2018
 Document ID: IS.011                                                        Last Revised Date: March 4, 2025

                                                Table of Contents
  1. Purpose ................................................................................................................ 2
  2. Authority ............................................................................................................... 2
  3. Scope ................................................................................................................... 2
  4. Responsibility ........................................................................................................ 2
  5. Compliance ........................................................................................................... 3
  6. Information Security objectives ............................................................................... 4
  7. Communications ................................................................................................... 4
  8. Reporting requirements .......................................................................................... 4
  9. Requirements ........................................................................................................ 5
  10. Standard Framework Coverage ............................................................................. 8
  11. Document Change Control ................................................................................. 10

Enterprise Information Security                  Page 1 of 11

1. PURPOSE
   1.1.   The purpose of this standard is to document the framework, principles and
          controls of an effective information security program, and outline the
          information security requirements to safeguard information assets. The
          Commonwealth is committed to continually improving the information
          security program to meet its strategic objectives and ensure that it is able to
          adapt to changes in the cyber threat landscape, as well as evolving
          organizational, legal, and regulatory requirements.

2. AUTHORITY
   2.1.   Pursuant to M.G.L. Ch. 7d, the Executive Office of Technology Services and
          Security, (EOTSS), possess the authority to establish policies, procedures,
          and objectives with respect to activities concerning information technology.
          M.G.L. Ch. 7d provides in pertinent part: “Notwithstanding any general or
          special law, rule, regulation, executive order, policy or procedure to the
          contrary, all executive department agencies shall, and other state agencies
          may, adhere to the policies, procedures and objectives established by the
          executive office of technology services and security with respect to activities
          concerning information technology.”

3. SCOPE
   3.1.   This document applies to the use of information, information systems,
          assets, applications, and network resources used to conduct business on
          behalf of the Commonwealth. The document applies to the Executive Branch
          including all executive offices, boards, commissions, agencies, departments,
          divisions, councils, and bureaus, hereinafter referred to as Commonwealth
          Agencies and Offices. Other Commonwealth entities that use or participate in
          services provided by the Executive Office of Technology Services and Security,
          (EOTSS), by any form of contractual arrangement, are required to comply with
          this document, as a condition of use. Commonwealth Agencies and Offices are
          required to implement procedures that ensure their personnel comply with
          the requirements herein to safeguard information.

4. RESPONSIBILITY
   4.1.   The Enterprise Risk Management Office is responsible for the development and
          ongoing maintenance of this standard. The Enterprise Risk Management Office
          is responsible for this standard and may enlist other departments to assist in
          maintaining and monitoring compliance with this standard. The owner of this
          document is the Commonwealth CISO, or his or her designee. The document
          owner will review and update this standard on an annual basis, or when

Enterprise Information Security Page 2 of 11

          significant policy or procedural changes necessitate an amendment.
          Questions regarding this document must be submitted to the document owner
          by sending an email to ERM@mass.gov.

   4.2.   Additional information regarding this standard and its related policies and
          standards may be found at https://www.mass.gov/cybersecurity/policies.

   4.3.   In the event of any conflict between the provisions contained in this standard
          and the provisions set forth in any of the Enterprise Information Security
          Policies, the provisions in the Enterprise Information Security Policies will
          govern.

   4.4.   Definitions of terms in bold may be found in the IS.Glossary of Terms at
          https://www.mass.gov/cybersecurity/policies.

5. COMPLIANCE
   5.1.   Compliance with this document is mandatory for the Executive Branch and all
          Commonwealth Agencies and Offices. Violations are subject to disciplinary
          action in accordance with applicable employment and collective bargaining
          agreements, up to and including the termination of their employment and/or
          assignment with the Commonwealth.

   5.2.   In the event any Commonwealth Agency or Office is unable to comply with any
          of the requirements of this document, the agency or office must submit an
          Information Security Policy Non-Compliance Report to the Enterprise Risk
          Management          Office       online        through         ServiceNow,
          https://www.mass.gov.service-now.com).

   5.3.   The Non-Compliance Report will:

   5.4.   Specifically state the reason/cause of the non-compliance

   5.5.   Identify and explain in detail the risks created due to the non-compliance

   5.6.   Provide a detailed explanation of the controls the agency, or office will
          implement to mitigate the risks to an acceptable level

   5.7.   Specify the time-frame required to implement the controls and mitigate the
          identified risks. All Risk Mitigation Plans (RMP) will be for a limited time.

   5.8.   The names and contact information for both the risk owner and the control
          owner designated by the agency to accept and manage the risks associated
          with the non-compliance and implement the controls that will effectively
          mitigate the identified risks.

Enterprise Information Security Page 3 of 11

6. INFORMATION SECURITY OBJECTIVES
   6.1.   The goal of the information security program is to manage risk within the
          Commonwealth’s information technology environment and achieve its
          information security objectives through the establishment of supporting
          policies, standards, processes, and controls. The information security
          objectives of the Commonwealth are:

   6.2.   Enable organizational strategy through the protection of data and non-public
          information.

      6.2.1. Comply with applicable laws, regulations, and contractual obligations with
             relevant stakeholders.
      6.2.2. Establish a governance structure to effectively and efficiently manage
             information security risk.

   6.3.   Manage identified security risks to an acceptable (i.e., risk tolerance) level
          through design, implementation, and maintenance risk remediation plans.

   6.4.   Establish a culture of accountability and increasing the level of awareness of all
          personnel in order to meet information security requirements.

   6.5.   Establish responsibility and accountability for information security policies,
          standards and governance across the Commonwealth.

7. COMMUNICATIONS
   7.1.   The Commonwealth’s Information Security policies and standards are publicly
          available on the mass.gov website. EOTSS will inform Commonwealth agencies
          when policies or standards are created, or when major revisions are published.

8. REPORTING REQUIREMENTS
   8.1.   Violations

      8.1.1. Compliance with this document is mandatory for all Commonwealth
             Agencies and Offices. Violation of the requirements of this standard may
             cause irreparable injury to the Commonwealth of Massachusetts. Violations
             are subject to disciplinary action in accordance with applicable employment
             and collective bargaining agreements, up to and including the termination of
             their employment and/or assignment with the Commonwealth.

   8.2.   Reporting Violations

      8.2.1. Any violation of the security requirements of this standard should be
             reported to agency management and/or the Information Security Team.

Enterprise Information Security Page 4 of 11

                Information security incidents (e.g., security breaches) will follow the
                reporting requirements outlined in IS.020 Information Security Incident
                Management Standard.

     8.3.    Information Security Policy Non-Compliance Reports

         8.3.1. In the event that any Commonwealth Agency, Office, or other party is unable
                to comply with the requirements of this standard, an Information Security
                Policy Non-Compliance Report must be submitted as detailed above.

9.     REQUIREMENTS
  9.1.      Organization of Information Security

         9.1.1. Commonwealth Agencies and Offices will develop, maintain, and implement
                policies, standards, guidelines, and procedures (PSGPs) to support the
                Commonwealth’s information security program to safeguard the
                confidentiality, integrity, and availability of its information assets, as directed
                by the Commonwealth’s technology leadership.

  9.2.      Acceptable Use

         9.2.1. Personnel are the first line of defense and have a shared responsibility to
                safeguard information owned or entrusted to the Commonwealth.

  9.3.      Access Management

         9.3.1. Access will be managed throughout the account lifecycle from the initial
                identification of a user to the granting, modifying, and revoking of user access
                privileges to confirm that information assets are protected from
                unauthorized access.

         9.3.2. Accounts will be provisioned using the principle of least privilege.

         9.3.3. Access privileges will be monitored and reviewed periodically commensurate
                with their risk classification.

         9.3.4. Passwords must meet the Commonwealth’s complexity requirements and
                should be changed on a regular basis.

  9.4.      Asset Management

         9.4.1. Agencies will establish and maintain an asset inventory and implement a
                program to manage the asset life cycle (i.e., procurement through end-of-
                support/end-of-life).

         9.4.2. Agencies will implement security controls to protect endpoints and mobile
                devices from malware and information leakage.
Enterprise Information Security Page 5 of 11

  9.5.     Business Continuity and Disaster Recovery

         9.5.1. Commonwealth Agencies and Offices must protect mission-critical
                information assets, processes, and facilities from the effects of major
                failures or disasters by developing and implementing a business continuity
                strategy that is consistent with organizational objectives and priorities.

         9.5.2. Commonwealth Agencies and Offices are required to back up critical data,
                such as confidential information, and strive to prevent disasters and
                implement timely recovery from disasters as well as continue critical
                organizational functions during a disaster or major disruption while
                maintaining confidentiality.

  9.6.     Communication and Network Security Management

         9.6.1. Commonwealth Agencies and Offices will implement network security
                controls such as firewalls, intrusion prevention/detection systems (IPS/IDS),
                virtual private networks (VPNs) and segmentation techniques so that the
                Commonwealth protects its information assets from compromise both from
                external and internal actors.

  9.7.     Compliance

         9.7.1. Commonwealth Agencies and Offices will establish a compliance
                framework that will enable the Commonwealth to comply with all relevant
                legislative, regulatory, statutory, and contractual requirements related to
                information security.

  9.8.     Cryptographic Management

         9.8.1. Define requirements for encrypting data at rest, data in transit and data in
                use, commensurate with the information classification of the information
                requiring protection. Maintain cryptographic keys to preserve the integrity of
                cryptographic controls. Use of encryption controls will be determined after
                a risk assessment is performed.

  9.9.     Information Security Incident Management

         9.9.1. Commonwealth Agencies and Offices will develop, maintain, and implement
                policies, standards, guidelines, and procedures (PSGPs) to effectively
                detect, respond and resolve incidents that affect the security of the
                Commonwealth’s information assets, including establishing a Security
                Incident Response Team (SIRT) to manage the incident response process.

         9.9.2. PSGPs will identify relevant stakeholders (both internal and external).

      9.9.3. Commonwealth Agencies and Offices will test incident response plans not
              less than annually.
Enterprise Information Security Page 6 of 11

  9.10. Information Security Risk Management

      9.10.1.Commonwealth Agencies and Offices will identify and analyze information
             security risks that could compromise the confidentiality, integrity, or
             availability of the Commonwealth’s information assets, and mitigate them to
             an acceptable level to meet organizational objectives and compliance
             requirements.

      9.10.2.All relevant statutory, regulatory, and contractual requirements that include
             security and privacy controls, and the Commonwealth’s approach to meet
             these requirements must be explicitly defined, documented, and kept up to
             date.

  9.11. Logging and Event Monitoring

      9.11.1.Commonwealth Agencies and Offices will develop and implement a process
             to monitor and review activity on information systems, so that information
             system problems are identified and corrected, and operator logs, and fault
             logging are enabled, collected, and reviewed.

      9.11.2.The Commonwealth must comply with all relevant legal, regulatory, and
             contractual requirements applicable to logging and event monitoring.

  9.12. Operations Management

      9.12.1.Agencies and Offices will develop and document standard operating
             procedures, change management, configuration management, capacity
             management and release management processes for technology
             environments.

      9.12.2.Agencies and Offices will back up information in a secure manner to enable
             the organization to restore its operational activities after a planned or
             unplanned interruption of service.

      9.12.3.Agencies and Offices will establish standards to support the secure
             implementation of applications and services in public and private cloud
             environments, including Software as a Service (SaaS), Platform as a Service
             (PaaS) and Infrastructure as a Service (IaaS).

  9.13. Physical and Environment Security

      9.13.1.Commonwealth Agencies and Offices will enforce physical security controls
             to manage access to information assets.

      9.13.2.Organizations must physically protect facilities with safeguards to protect
             information assets against environmental hazards.

Enterprise Information Security Page 7 of 11

  9.14. Secure System and Software Life Cycle Management

      9.14.1.Commonwealth Agencies and Offices will perform information security
             reviews throughout all phases of the system and software management
             lifecycle to ensure risks are properly identified, addressed, and mitigated in
             a timely and cost-efficient manner.

      9.14.2.Agencies and Offices must configure systems using security hardening
             standards and review configurations periodically.

  9.15. Third-party Information Security

      9.15.1.Commonwealth Agencies and Offices will establish a process to perform
             initial risk assessments and perform ongoing due diligence of third parties
             that enter formal business arrangements with the Commonwealth.

      9.15.2.Contractual agreements between third parties and Commonwealth
             agencies must address baseline information security clauses, including,
             but not limited to, the right to audit and adhere to data protection
             requirements.

  9.16. Vulnerability Management

      9.16.1. Commonwealth Agencies and Offices must implement security controls to
             manage and monitor risks to the Commonwealth’s information technology
             environment.

      9.16.2.Vulnerability management personnel must be able to identify and respond
             to vulnerabilities within established and predictable timeframes.

      9.16.3.Vulnerability management activities must be reported to management on a
             regular basis.

10. STANDARD FRAMEWORK COVERAGE

  Standard
           Standard name                       Topics covered
  ref.
                                                • Information Security Organization Structure
             Organization of Information        • Roles and Responsibilities
  IS.012
             Security Standard                  • Standard Framework
                                                • Standard Life Cycle Management

             Acceptable Use of Information
  IS.013
             Technology Standard

Enterprise Information Security Page 8 of 11

  Standard
           Standard name                       Topics covered
  ref.
                                               • User and System Access Management
  IS.014     Access Management Standard        • Account Management
                                               • Password Management

                                               • Information Asset Management
                                               • Information Protection Requirements
                                               • Information Classification
                                               • Information System Classification
  IS.015     Asset Management Standard
                                               • Information Labeling and Handling
                                               • Endpoint Security
                                               • Information Disposal
                                               • Mobile Device Management

             Business Continuity and           • Business Continuity
  IS.016
             Disaster Recovery Standard        • Disaster Recovery

                                               • Network Security Management
             Communication and Network         • Remote Access Security Management
  IS.017
             Security Standard                 • Secure File Transfer
                                               • Management of Third-party Network Access

                                               • Compliance with Policies, Standards,
                                                 Guidelines, and Procedures
  IS.018     Compliance Standard               • Reporting Security Incidents and Violations
                                               • Security Compliance Reviews
                                               • External Attestation of Compliance

             Cryptographic Management          • Key Management
  IS.019
             Standard                          • Approved Cryptography Techniques

             Information Security Incident
  IS.020                                       • Information Security Incident Management
             Management Standard
             Information Security Risk         • Information Security Risk Management
  IS.021
             Management Standard               • Security Awareness and Training

             Logging and Event Monitoring
  IS.022                                       • Logging and Event Monitoring
             Standard
                                               • Standard Operating Procedures
                                               • Change Management
                                               • Configuration Management
             Operations Management
  IS.023                                       • Capacity Management
             Standard
                                               • Release Management
                                               • Data Backup and Restoration
                                               • Cloud Computing

Enterprise Information Security Page 9 of 11

  Standard
           Standard name                        Topics covered
  ref.
              Physical and Environmental        • Facility Controls and Secure Areas
  IS.024
              Security Standard                 • Equipment and Other Media Security

              Secure System and Software        • Security in System and Software Life Cycle
  IS.025      Lifecycle Management              • Security in SDLC Support Processes
              Standard                          • System Hardening

                                                • Contractual Security Risk Identification
              Third Party Information           • Third-party Selection
  IS.026
              Security Standard                 • Contractual Security Provisions
                                                • Third-party Life Cycle Management

              Vulnerability Management
  IS.027                                        • Vulnerability and Patch Management
              Standard

                              Table 1 — Standard Structure

11. DOCUMENT CHANGE CONTROL
Version    Revised by             Effective      Description of changes
No.                               date
  0.80     Jim Cusson              10/01/2017                Corrections and formatting
  0.90     John Merto              12/18/2017                Minor corrections, wording
  0.95     Sean Vinck               5/7/2018             Minor corrections and formatting
  0.96     Andrew Rudder           5/31/2018                 Corrections and formatting
  0.97     Anthony O’Neill         05/31/2018                Corrections and formatting
  1.0      Dennis McDermitt        06/01/2018              Final pre-publication Review
  1.0      Andrew Rudder           10/4/2018         Approved for Publication by: John Merto
  1.1      Megan Perkins           7/15/2020     Annual Review; Minor corrections and formatting
  1.2      Sean M. Hughes          11/04/2021                     Annual Review
  1.3      Sean M. Hughes          08/29/2022                     Annual Review
  1.4      Thomas McDermott        9/27/2023        Annual Review, Corrections and Updating
  1.4      Anthony O’Neill         9/27/2023                        Final Review
  1.5      Thomas McDermott        11/4/2024       Annual Review, Corrections and Formatting
  1.5      Anthony O’Neill         11/4/2024                        Final Review
  1.6      Thomas McDermott         2/4/2025          Updates, Corrections and Formatting

Enterprise Information Security Page 10 of 11

  1.6     Miklos Lavicska         2/27/2025     Corrections and Formatting
  1.6     Anthony O’Neill         3/4/2025             Final Review

Enterprise Information Security Page 11 of 11

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
