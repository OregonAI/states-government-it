---
schema_version: 1
corpus: states-government-it
jurisdiction: massachusetts
id: ma-is-020
title: IS.020 Information Security Incident Management Standard
doc_type: standard
citation: IS.020
authority_level: ''
issuing_body: Executive Office of Technology Services and Security, Enterprise Risk Management Office
source_url: https://www.mass.gov/doc/is020-information-security-incident-management-standard/download
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 8a1905236c225f3ef63ea8dca92cf92e76ebc8653ee03a986a7c203624f6982d
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# IS.020 Information Security Incident Management Standard (IS.020)

## At a glance

One of the seventeen Enterprise Information Security Standards (IS.011 to IS.027) on EOTSS's Technology Standards and Guidelines page, which says executive branch agencies are required to conform to defined EOTSS policies and standards under Chapter 64 of the Acts of 2017. The page for the Information Security Incident Management Standard carries a summary and this PDF is the standard.

## Full text

                   Commonwealth of Massachusetts
                   Executive Office of Technology Services and Security (EOTSS)
                   Enterprise Risk Management Office

                 Information Security Incident Management Standard

 Document Name: Information Security Incident                                Effective Date: October 15th, 2018
 Management Standard                                                         Last Revised Date: March 18, 2025
 Document ID: IS.020

                                                 Table of Contents
1.   Purpose ................................................................................................................. 2
2.   Authority ................................................................................................................ 2
3.   Scope .................................................................................................................... 2
4.   Responsibility......................................................................................................... 2
5.   Compliance ........................................................................................................... 3
6.   Standard Statements .............................................................................................. 4
7.   Control Mapping ................................................................................................... 13
8.   Document Change Control ..................................................................................... 14

Incident Management                              Page 1 of 14

1. PURPOSE
   1.1.   This standard documents the requirements for managing an information
          security incident; describes the actions to be taken should an incident occur;
          and details each phase of the incident management life cycle, including
          identification, investigation, response, and remediation.

2. AUTHORITY
   2.1.   Pursuant to M.G.L. Ch. 7d, the Executive Office of Technology Services and
          Security, (EOTSS), possess the authority to establish policies, procedures, and
          objectives with respect to activities concerning information technology. M.G.L.
          Ch. 7d provides in pertinent part: “Notwithstanding any general or special law,
          rule, regulation, executive order, policy or procedure to the contrary, all executive
          department agencies shall, and other state agencies may, adhere to the policies,
          procedures and objectives established by the executive office of technology
          services and security with respect to activities concerning information
          technology.”

3. SCOPE
   3.1.   This document applies to the use of information, information systems, assets,
          applications, and network resources used to conduct business on behalf of the
          Commonwealth. The document applies to the Executive Branch including all
          executive offices, boards, commissions, agencies, departments, divisions,
          councils, and bureaus, hereinafter referred to as Commonwealth Agencies and
          Offices. Other Commonwealth entities that use or participate in services
          provided by the Executive Office of Technology Services and Security, (EOTSS), by
          any form of contractual arrangement, are required to comply with this document,
          as a condition of use. Commonwealth Agencies and Offices are required to
          implement procedures that ensure their personnel comply with the
          requirements herein to safeguard information.

4. RESPONSIBILITY
   4.1.   The Enterprise Risk Management Office is responsible for the development and
          ongoing maintenance of this standard. The Enterprise Risk Management Office is
          responsible for this standard and may enlist other departments to assist in
          maintaining and monitoring compliance with this standard. The owner of this
          document is the Commonwealth CISO, or his or her designee. The document
          owner will review and update this standard on an annual basis, or when
          significant policy or procedural changes necessitate an amendment. Questions
          regarding this document must be submitted to the document owner by sending
          an email to ERM@mass.gov.

Incident Management                 Page 2 of 14

   4.2.   The Enterprise Risk Management Office is responsible for this standard and may
          enlist other departments to assist in the monitoring and maintenance of
          compliance with this standard.

   4.3.   Additional information regarding this standard and its related policies and
          standards may be found at https://www.mass.gov/cybersecurity/policies.

   4.4.   In the event of any conflict between the provisions contained in this standard and
          the provisions set forth in any of the Enterprise Information Security Policies, the
          provisions in the Enterprise Information Security Policies will govern.

   4.5.   Definitions of terms in bold may be found in the IS.Glossary of Terms at
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

      5.3.1. Specifically state the reason/cause of the non-compliance

      5.3.2. Identify and explain in detail the risks created due to the non-compliance

      5.3.3. Provide a detailed explanation of the controls the agency, or office will
             implement to mitigate the risks to an acceptable level

      5.3.4. Specify the time-frame required to implement the controls and mitigate the
             identified risks. All Risk Mitigation Plans (RMP) will be for a limited time.

      5.3.5. The names and contact information for both the risk owner and the control
             owner designated by the agency to accept and manage the risks associated
             with the non-compliance and implement the controls that will effectively
             mitigate the identified risks.

Incident Management                Page 3 of 14

6. STANDARD STATEMENTS
   6.1.   Incident Response Program

      6.1.1. The Enterprise Security Office will be responsible for developing a program to
             effectively detect, respond to and resolve incidents that affect the security of
             the Commonwealth’s information assets.

      6.1.2. The incident response program will include:

          6.1.2.1. Documented process that defines the incident response life cycle.

          6.1.2.2. Definition of roles and responsibilities for internal and external
                   stakeholders, including the formal establishment of a Security Incident
                   Response Team.

          6.1.2.3. Formal event reporting and escalation procedures.

          6.1.2.4. Tools and enablers to facilitate incident management.

   6.2.   Incident Response Lifecycle

      6.2.1. The incident lifecycle follows the National Institute of Standards and
             Technology (“NIST”) incident response guidance outlined in NIST Special
             Publication 800-61 Revision 2.

      6.2.1 The response lifecycle addresses the preparation, detection, containment,
            eradication, and recovery phases of the incident response process:

          6.2.1.1.    Preparation: This phase consists of the development of policies and
                      procedures, as well as preparation for incidents and handling of
                      incidents through incident handling processes and systems.

          6.2.1.2.    Detection and Analysis: This phase consists of the identification of
                      events through probable attack vectors, signs of incidents, detection
                      sources such as SIEMs, anti-virus, and logs, detailed incident
                      analysis, incident documentation, incident prioritization, and
                      incident notification.

          6.2.1.3.    Containment, Eradication and Recovery: This phase consists of
                      mitigating and limiting the scope of impact to systems and data
                      through containment strategies, evidence gathering, identification of
                      attackers, threat neutralization, and restoration of normal operations.

          6.2.1.4.    Post Incident Activity: This phase consists of identifying and analyzing
                      historical information, development of lessons learned reports,

Incident Management                 Page 4 of 14

                      analysis of incident information, and retention of evidence for
                      investigations and legal requirements and identifying lessons learned.

   6.3.   Security Incident Response Team (SIRT)

      6.3.1 The roles and responsibilities for the members of the core and extended SIRT
            team must be clearly defined.

          6.3.1.1.    The Incident Response Coordinator (i.e., Commonwealth CISO or his
                      or her designee) will:

             6.3.1.1.1. Oversee and provide guidance and direction to the incident
                        response team.

             6.3.1.1.2. Serve as a communication liaison to internal and external entities,
                        including Enterprise Security Office leadership, the agency
                        leadership, and other relevant stakeholders.

             6.3.1.1.3. Validate the results of response actions.

             6.3.1.1.4. Coordinate the development of training plans for the incident
                        response plan. The SIRT will receive training on the incident
                        response plan on an annual basis.

             6.3.1.1.5. Sponsor periodic (i.e., annually recommended) tabletop exercises
                        to test incident response readiness.

             6.3.1.1.6. Sustain, maintain, and improve the information security incident
                        response process.

             6.3.1.1.7. Maintain compliance with record retention requirements.

          6.3.1.2.    The Incident Response Lead will:

             6.3.1.2.1. Oversee response efforts for a specific information security
                        incident. (Note: Every incident may have a different IR Lead).

             6.3.1.2.2. Serve as the escalation/communication liaison between the SIRT
                        team and information security leadership as well as other
                        relevant stakeholders.

             6.3.1.2.3. Act as or engage the appropriate subject matter resources when
                        key decisions need to be made during the information security
                        incident response process.

          6.3.1.3.    The Incident Response Analyst (i.e., subject-matter resources) will:

Incident Management                 Page 5 of 14

             6.3.1.3.1. Ensure investigations are conducted in accordance with
                        documented procedures and that evidence is handled
                        appropriately.

             6.3.1.3.2. Collect, process, and maintain information security incident
                        information.

             6.3.1.3.3. Manage information security incident status documentation.

             6.3.1.3.4. Communicate and escalate incidents, as required.

             6.3.1.3.5. Manage security incidents through post-incident review.

      6.3.2. The extended incident response team includes cross-functional resources
             that will provide support as appropriate.

          6.3.2.1.    Digital Forensics Service Provider: Maintains a forensics service
                      provider on retainer to assist with the recovery and investigation of
                      information in digital formats as needed.

          6.3.2.2.    Legal: Provides advice regarding liability issues if an incident affects
                      customers or third parties or may lead to litigation.

          6.3.2.3.    Human Resources: Provides advice on managing incidents that
                      involve personnel.

          6.3.2.4.    Public Relations/Communications: Communicates the details of
                      security incidents to external stakeholders, including state and
                      federal law enforcement and regulators. Manages crisis
                      communication.

   6.4. Incident Identification, Investigation and Analysis

      6.4.1. Defining potential information security incidents

          6.4.1.1.    A security incident is defined as any event which has the potential, or
                      already has, resulted in the unauthorized acquisition,
                      misappropriation, use or manipulation of information that
                      compromises the confidentiality, integrity, or availability of the
                      Commonwealth’s information assets. Examples include, but are not
                      limited to:

             6.4.1.1.1 Unauthorized and illegal disclosure, destruction and/or alteration
                       of files, Commonwealth IT systems and information, including
                       confidential information.

             6.4.1.1.2. Unauthorized use of a Commonwealth IT system for the
                        transmission, processing, or storage of information.

Incident Management                 Page 6 of 14

              6.4.1.1.3. Changes to system hardware, firmware or software characteristics
                         intentionally concealed from the IT Information Owner and made
                         without their knowledge or consent.

              6.4.1.1.4. Detection of malware or malicious code (viruses, worms, etc.).

              6.4.1.1.5. Unauthorized probes, scans, or sniffers on the Commonwealth’s
                         internal network.

              6.4.1.1.6. Denial of Service (DOS) or Distributed Denial of Service (DDOS)
                         attacks.

              6.4.1.1.7. Harassment and threats conducted via Commonwealth email
                         resources.

              6.4.1.1.8. Web page defacement, unauthorized use of system privileges and
                         attempts (either failed or successful) to gain unauthorized access
                         to a system or its information.

              6.4.1.1.9. Legal or regulatory       violations   involving   Commonwealth
                         information assets.

              6.4.1.1.10 Violation of the Commonwealth’s information security policies.

              6.4.1.1.11 Cyber-stalking, identity theft or child pornography.

              6.4.1.1.12 Unauthorized physical access to a secure area (e.g., data centers).

      6.4.2      Per IS.022 Logging and Event Monitoring Standard, security alerts from
                 security monitoring systems, including but not limited to intrusion
                 detection and prevention, firewalls, email, and file-integrity monitoring
                 systems will be collected and monitored.

         6.4.2.1      The Security Operations Center (SOC) will analyze log information
                      from security monitoring systems to establish a baseline of events
                      expected for the normal system and network operations.
                      Commonwealth Agencies and Offices must ensure that any
                      exceptions from these baseline events will be reported to the
                      responsible Information Owner.

         6.4.2.2      External feed sources, including resources from the Fusion Center, will
                      be leveraged to assist with the incident response process.

      6.4.3      Security Alerts may be received from the following external sources:

         6.4.3.1      The Cybersecurity and Infrastructure Security Agency (CISA).

         6.4.3.2      Others

Incident Management                 Page 7 of 14

       6.5.          Incident Reporting and Escalation

            6.5.1.         Commonwealth Agencies and Offices must establish, document, and
                           distribute security incident response and escalation procedures to
                           ensure timely and effective handling of incidents.

            6.5.2.         Information security incident impact rating

                                                                 Response                Notification   Post-incident
Impact                 Characteristics
                                                                   time1                    Level        report req.

            Threat to human safety.
            Adverse impact on a “Critical”
            or “High” risk rated
            information asset, including
            infrastructure, applications,
            and services (see IS.015 Asset                                            Risk Governance
            Management Standard).                                                       Committee,
 High .     Financial or legal liability equal                  Immediate             Commonwealth          Yes
            to $1m and above to the                                                    CIO, CISO and
            Commonwealth.                                                              agency heads
       A. Potential compromise of
          information classified as
          restricted, or confidential
          information, including PII and
          other regulated information.

       Adverse impact on a “Medium”
       risk rated information asset,
       including infrastructure,
       applications, and services
       (see IS.015 Asset Management                                                   Commonwealth
Medium Standard).                                                  4 hours             CISO, agency         Yes
       Financial or legal liability                                                       heads
       between $100,000 and $1m.
            Potential compromise of
            information not intended for
            public disclosure.

  1 Note: This is not resolution time but the start time of the incident response process.

  Incident Management                                  Page 8 of 14

      Adverse impact on a “Low” risk
      rated information asset,
      including infrastructure,                                Technical       No, unless
      applications, and services                              support for       decided
                                     Next business
Low   (see IS.015 Asset Management                             impacted       otherwise by
                                          day
      Standard).                                             information         the IR
                                                                 asset        Coordinator
      Financial or legal liability of
      less than $100,000.

      6.5.3.     Information Security Incident Reporting and Escalation

          6.5.3.1     Define regular metrics and reporting cadence to the appropriate
                      audience.

          6.5.3.1.    Security incidents, whether potential or actual, will be reported
                      immediately to the agency helpdesk, or the EOTSS Security Operations
                      Center (SOC). More information on Security Incident reporting
                      procedures may be found in the EOTSS or Secretariat Security
                      Incident Response Plans.

          6.5.3.2.    All Commonwealth personnel are required to fully cooperate with the
                      SIRT team and will provide accurate and timely information. All
                      Commonwealth Agencies and Offices must ensure that all personnel
                      are available to the SIRT team when needed.

          6.5.3.3.    As the first line of defense, Commonwealth Agencies and Offices must
                      ensure that personnel are responsible for reporting suspicious
                      activities.

      6.5.4. Management Reporting and Escalation

          6.5.4.1.    The SIRT team will notify the Risk Governance Committee about
                      security incidents that have an impact rating of “high.” The report will
                      include, but is not limited to the following (as applicable):

               6.5.4.1.1. Date and time incident detected.

               6.5.4.1.2. Dated and time of notification.

               6.5.4.1.3. Type of incident detected

               6.5.4.1.4. Description of the incident

               6.5.4.1.5. Incident response status

               6.5.1.4.6 Location

Incident Management                     Page 9 of 14

             6.5.1.4.7. Affected systems

             6.5.1.4.8. User groups affected

             6.5.1.4.9. Recover time expectations

             6.5.1.4.10 Internal and external stakeholder contacts that need to be notified

             6.5.1.4.11 Identification, containment, and eradication measures

             6.5.1.4.12 Evidence collected

             6.5.1.4.13 Pending actions (if any)

             6.5.1.4.14 Name(s) and contact information of the person(s) who discovered
                        the incident.

             6.5.1.4.15 Date and time incident reported to supervisor(s) and/or upper
                        management.

      6.5.5. Communication Protocols

          6.5.5.1.    All information pertaining to an incident investigation will be handled
                      with discretion and disclosed only on a need-to-know basis. Incident
                      reports will be categorized as confidential at the discretion of the
                      Commonwealth CISO or his or her designee and the Enterprise
                      Security Office. The Commonwealth CISO or his or her designee, will
                      be designated the owner for all incident investigation related
                      documentation.

   6.6.   Security Incident Response and Investigation

      6.6.1. The Enterprise Security Office, with the relevant stakeholders, must take
             appropriate steps to ensure proper documentation, investigation, risk
             analysis, impact analysis and containment measures are taken in order to
             minimize the risk to the Commonwealth once a security event is identified.

      6.6.2. Incident response procedures

          6.6.2.1.    Commonwealth Agencies and Offices must document procedures for
                      responding to security incidents to limit further damage to the
                      Commonwealth's information assets. Procedures will include:

             6.6.2.1.1. Identification of the cause of the incident

             6.6.2.1.2. Execution of corrective actions

             6.6.2.1.3. Post-incident analysis

Incident Management                Page 10 of 14

            6.6.2.1.4. Communication strategy

      6.6.3. Incident Response Plan

         6.6.3.1.     EOTSS and all other Commonwealth Agencies and Offices will
                      establish an incident response plan. The incident response plan will
                      include, at a minimum:

            6.6.3.1.1. Roles, responsibilities, and communication and contact strategies
                       in the event of a compromise, including notification of required
                       internal and external parties.

            6.6.3.1.2. Specific incident response procedures.

            6.6.3.1.3. Reportable incident criteria

            6.6.3.1.4. Incident response metrics

            6.6.3.1.5. Execution of corrective actions and post-incident analysis.

            6.6.3.1.6. Establish criteria to activate business recovery and continuity
                       processes (See IS.016 Business Continuity and Disaster Recovery
                       Standard).

            6.6.3.1.7. Data backup processes (See Data Backup and Restoration in
                       IS.015 Asset Management Standard).

            6.6.3.1.8. Analysis of legal requirements for reporting compromises.

            6.6.3.1.9. Reference or inclusion of incident response procedures from
                       required external parties.

         6.6.3.2.     Commonwealth Agencies and Offices will establish a process to
                      modify and evolve the incident response plan and procedures
                      according to lessons learned. The incident response plan and
                      procedures will be tested at least annually.

      6.6.4. Incident Containment

         6.6.4.1.     The SIRT team will confirm the validity of the reported incident,
                      containing and minimizing the impact of the incident in collaboration
                      with the relevant stakeholders.

         6.6.4.2.     The information asset will be removed or quarantined from all
                      Commonwealth networks as soon as possible, where technically
                      feasible.

Incident Management                Page 11 of 14

      6.6.5. Incident Investigation

         6.6.5.1.     The SIRT team will perform the following as part of the incident
                      investigation process:

               6.6.5.1.2. Gather information regarding the situation and elements involved
                          (e.g., log correlation analysis).

               6.6.5.1.3. Determine the scope, severity, impact, and nature of the incident.

               6.6.5.1.4. Determine root cause.

               6.6.5.1.5. Determine response and recovery timelines.

               6.6.5.1.6. Contextualize the evidence collected and document facts of the
                          incident.

               6.6.5.1.7. Gather system events and/or audit records.

      6.6.6.     Collection of Evidence

         6.6.6.1.     Evidence, in whichever form it exists (digital, physical, original, or
                      copied) will be collected. Evidence will be collected and preserved in a
                      manner that is consistent with legal and record retention
                      requirements.

         6.6.6.2.     A file comparison utility will be run to identify all changes to
                      information systems (where applicable).

         6.6.6.3.     Log(s) will be copied to separate media and stored appropriately.

         6.6.6.4.     The information asset will be restored from trusted backup copies.

         6.6.6.5.     If there is an expectation that there may be legal implications,
                      appropriate chain of custody requirements must be met. The SIRT
                      team will consult with Legal on whether a certified forensics
                      professional is engaged.

         6.6.6.6.     Information describing all reported information security incidents
                      will be retained for a minimum of three (3) years or as determined by
                      Legal.

      6.6.7.     Post-Incident Analysis

         6.6.7.1.     The post-incident analysis will be conducted in a timely manner to
                      determine the organizational impact and confirm the causes, motives
                      of the attack, and any potential mitigating actions. The analysis will
                      include:

Incident Management                 Page 12 of 14

                6.6.7.1.1. Post-incident inventory to account for all the information systems
                           owned or managed by the Commonwealth that may have been
                           impacted.

                6.6.7.1.2. Assessment of the involved systems to ensure that once they are
                           returned to service only those with access needs are granted
                           access to the system.

                6.6.7.1.3. Risk-analysis of critical systems based on knowledge acquired and
                           lessons learned.

       6.6.8.     Based on lessons learned, policies, processes or controls should be
                  reviewed to determine whether there are opportunities for improvement.

7.        CONTROL MAPPING
                Section                   NIST SP800-53 R5       CIS 18 v8       NIST CSF
 6.1. Security Incident Response                IR-1              CSC 17          ID.GV-1
 Team (SIRT)                                    IR-2                 -               -
                                                IR-8                              PR.IP-7
                                                IR-7                              PR.AT-4

 6.2. Incident Identification,                   SI-4              CSC 1          ID.RA-1
 Investigation and Analysis                                                       PR.IP-9
                                                                                  RS.AN -
                                                                                   Family
                                                 SI-5                 -           ID.RA-1

 6.3. Incident Reporting and                     AU-6              CSC 8         PR.PT-1
 Escalation                                                                      ID.GV-1
                                                 IR-6                            RS.CO-2
                                                 IR-5                           RC.CO-1
                                                                                RC.CO-2
                                                                                RC.CO-3
 6.4. Security Incident Response                 IR-3             CSC 17         PR.IP-10
 and Investigation                                                             RS.MI Family
                                                 IR-4                          DE.AE-family
                                                 IR-6                            RS.CO-2
                                                                                  RS.CO
                                                                                  Family
                                                                                 RC.RP-1
 6.5. Collection of Evidence                     IR-6             CSC 17         RS.CO-2
                                                 IR-7                                -
                                                                                 PR.PT-1

Incident Management                 Page 13 of 14

                                                                        PR.PT-1
                                                                        PR.PT-1
 6.6. Post-Incident Analysis              IR-4           CSC 17       DE.AE-family
                                                                       RS.IM - 1,2
                                                                        DE.AE-3

8.       DOCUMENT CHANGE CONTROL
 Version          Revised by      Effective date       Description of changes
    No.
 0.9        Jim Cusson              10/01/2017        Corrections and formatting.
 0.92       John Merto              01/02/2018        Corrections and Formatting
 0.95       Sean Vinck               5/7/2018         Corrections and formatting
 0.97       Andrew Rudder           5/31/2018         Corrections and formatting
 0.98       Anthony O’Neill         05/31/2018        Corrections and Formatting
 1.0        Dennis McDermitt        06/01/2018          Pre-publication Review
 1.0        Andrew Rudder           10/4/2018      Approved for Publication by: John
                                                                 Merto
 1.1        Megan Perkins           7/15/2020      Annual Review; Corrections and
                                                              formatting
 1.2        Sean M. Hughes          11/04/2021              Annual Review
 1.3        Sean M. Hughes          08/29/2022     NIST 800-53r5 and Annual Review
 1.4        Thomas E. McDermott     08/29/2023     Corrections, formatting, updating
                                                          and Annual Review
 1.4        Anthony O’Neill         08/29/2023               Final Review
 1.5        Thomas E. McDermott     12/6/2024        Corrections, Formatting and
                                                            Annual Review
 1.5        Anthony O’Neill         12/6/2024                Final Review
 1.6        Thomas E. McDermott     2/14/2025          Updates, Corrections and
                                                              Formatting
 1.6        Miklos Lavicska         2/20/2025         Corrections and Formatting
 1.6        Anthony O’Neill         3/18/2025               Final Approval

Incident Management            Page 14 of 14

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
