---
schema_version: 1
corpus: states-government-it
jurisdiction: massachusetts
id: ma-is-024
title: IS.024 Physical and Environmental Security Standard
doc_type: standard
citation: IS.024
authority_level: ''
issuing_body: Executive Office of Technology Services and Security, Enterprise Risk Management Office
source_url: https://www.mass.gov/doc/is024-physical-and-environmental-security-standard/download
source_format: pdf
retrieved: '2026-11-11'
source_sha256: ac30c3ec1c2dbcc3a713f681c269e48db3649847cff79dd59a7fcfae97b23811
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

# IS.024 Physical and Environmental Security Standard (IS.024)

## At a glance

One of the seventeen Enterprise Information Security Standards (IS.011 to IS.027) on EOTSS's Technology Standards and Guidelines page, which says executive branch agencies are required to conform to defined EOTSS policies and standards under Chapter 64 of the Acts of 2017. The page for the Physical and Environmental Security Standard carries a summary and this PDF is the standard.

## Full text

                  Commonwealth of Massachusetts
                  Executive Office of Technology Services and Security (EOTSS)
                  Enterprise Risk Management Office

                      Physical and Environmental Security Standard

 Document Name: Physical and Environmental                                  Effective Date:          October 15th,
 Security Standard                                                          2018
 Document ID: IS.024                                                        Last Revised Date: March 21, 2025

                                                Table of Contents
1.   Purpose................................................................................................................. 2
2.   Authority ............................................................................................................... 2
3.   Scope.................................................................................................................... 2
4.   Responsibility ........................................................................................................ 3
5.   Compliance ........................................................................................................... 3
6.   Standard Statements ............................................................................................. 4
7.   Control Mapping .................................................................................................. 10
8.   Document Change Control ................................................................................... 11

Physical and Environmental Security Page 1 of 11

1. PURPOSE
   1.1.   This standard establishes requirements to prevent damage or physical access to
          the Commonwealth’ s information processing facilities and sensitive data. This
          standard defines the following controls and acceptable practices:

      1.1.1. Definition of physical security perimeters and required controls

      1.1.2. Personnel and visitor access controls

      1.1.3. Requirements for environmental protection equipment

      1.1.4. Protection of equipment stored off-site from the Commonwealth’s facilities

   1.2.   Federal statutes and regulations, and, in some cases, state law, may impose
          security requirements in addition to the security requirements set forth in this
          standard (for example, Publication 1075 of the Internal Revenue Service).
          Nothing in this standard will be construed or interpreted as contradicting any
          such federal or state requirement. This standard is meant to encourage adoption
          of its security measures as a baseline, in addition to, and not in place of, any other
          legally required security measures.

2. AUTHORITY
   2.1.   M.G.L. Pursuant to M.G.L. Ch. 7d, the Executive Office of Technology Services
          and Security, (EOTSS), possess the authority to establish policies, procedures,
          and objectives with respect to activities concerning information technology.
          M.G.L. Ch. 7d provides in pertinent part: “Notwithstanding any general or special
          law, rule, regulation, executive order, policy or procedure to the contrary, all
          executive department agencies shall, and other state agencies may, adhere to
          the policies, procedures and objectives established by the executive office of
          technology services and security with respect to activities concerning
          information technology.”

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

Physical and Environmental Security Page 2 of 11

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

   4.2.   Additional information regarding this standard and its related policies and
          standards may be found at https://www.mass.gov/cybersecurity/policies.

   4.3.   In the event of any conflict between the provisions contained in this standard and
          the provisions set forth in any of the Enterprise Information Security Policies, the
          provisions in the Enterprise Information Security Policies will govern.

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

      5.3.1. Specifically state the reason/cause of the non-compliance

      5.3.2. Identify and explain in detail the risks created due to the non-compliance

      5.3.3. Provide a detailed explanation of the controls the agency, or office will
             implement to mitigate the risks to an acceptable level

Physical and Environmental Security Page 3 of 11

        5.3.4. Specify the time-frame required to implement the controls and mitigate the
               identified risks. All Risk Mitigation Plans (RMP) will be for a limited time.

        5.3.5. The names and contact information for both the risk owner and the control
               owner designated by the agency to accept and manage the risks associated
               with the non-compliance and implement the controls that will effectively
               mitigate the identified risks.

6.     STANDARD STATEMENTS
     6.3.   Facility Control and Secured Areas

        6.3.1. Security perimeters will be defined and established to protect areas that
               contain sensitive data and critical information processing facilities. This will
               include, but may not be limited to, data centers and main or intermediate
               distribution facilities (MDF or IDF) where core infrastructure is located and
               where sensitive data is processed, stored, managed, or transported.

        6.3.2. Physical Security Perimeters

            6.3.2.1.   Commonwealth Agencies and Offices must ensure that physical
                       security for the established security perimeters is clearly defined and
                       outfitted with perimeter protection mechanisms to reduce the risk of
                       unauthorized access.

            6.3.2.2.   The level of perimeter protection will be based on the sensitivity and
                       criticality of the information asset housed and the nature of the
                       supported business functions.

            6.3.2.3.   The following controls, at a minimum, will be considered when
                       implementing and revising perimeter protections, based on business
                       requirements:

               6.3.2.3.1. Access Control: Physical barriers, proximity card readers or
                          manned entry points must be in place to control access to internal
                          secured areas to prevent unauthorized entry.

               6.3.2.3.2. Site Monitoring: Physical perimeters will be monitored by manual
                          controls such as security guards and real-time controls such as
                          remote or live closed-circuit camera consoles.

        6.3.3. General Access Controls

            6.3.3.1.   Commonwealth Agencies and Offices will restrict access to internally
                       secured areas to only authorized personnel. The following are
                       minimum controls for restricting access:

Physical and Environmental Security Page 4 of 11

             6.3.3.1.1. Badge Assignment Process: Processes for issuing badges,
                        including granting, and revoking badges for personnel and visitors
                        (if applicable) must be documented.

             6.3.3.1.2. Badge System Access: Access to the badge administration
                        systems must be restricted to only authorized personnel.

             6.3.3.1.3. Authorized Personnel Identification: All Commonwealth full-time
                        and part-time personnel, including full-time and part-time interns,
                        who perform services for the Commonwealth will be issued a
                        badge or comparable identification. All other contractors,
                        consultants and/or vendors must provide 24 hours’ notice before
                        being on-site.

             6.3.3.1.4. Controlled Reception: Procedures to securely receive deliveries
                        for restricted areas must be documented. Deliveries for restricted
                        areas will be monitored and recorded (e.g., delivery company
                        name, time, parcel) for audit purposes.

             6.3.3.1.5. Audit Trail of Access to Restricted Areas: the date and time of entry
                        and departure of visitors to areas of IT assets processing, storing
                        and/or transmitting confidential information assets will be
                        recorded and securely maintained (e.g., data centers, server
                        rooms, Department of Revenue).

             6.3.3.1.6. Non-Business Hours Restriction: facility access outside of regular
                        office hours defined by the agency must be controlled. Access to
                        public areas must be monitored, and access to secure areas must
                        be strictly enforced using the badge and/or escort.

      6.3.4. Visitor Access Control

          6.3.4.1.   Commonwealth Agencies and Offices must ensure that visitor access
                     requires additional controls beyond the requirements for general
                     access. The following are minimum controls for restricting visitor
                     access:

             6.3.4.1.1. Visitor Sign-In: Visitors must sign a visitor’s log that indicates date
                        and time in/out, organization represented (if applicable), and the
                        identity of the Commonwealth Agency and/or Office they visited.

             6.3.4.1.2. Visitor Identification: All visitors will prominently display their
                        visitor identification (badge or alternate form of identification) at all
                        times while in secured areas (i.e., non-public office areas).

Physical and Environmental Security Page 5 of 11

                 6.3.4.1.2.1.   Visitors without a displayed badge will be escorted back to
                                the reception area for identification and authorization of
                                access.

                 6.3.4.1.2.2.   Visitor identification will be set to expire on the day that the
                                identification is granted.

                 6.3.4.1.2.3.   If a physical badge is issued, visitors will be required to
                                surrender the physical badge before leaving the facility or at
                                the date of expiration.

                 6.3.4.1.2.4.   Personnel are not allowed to utilize visitor badges.
                                Identification badges issued to Commonwealth personnel
                                will differ from badges issued to visitors.

                 6.3.4.1.2.5.   Visitors must be positively identified. All visitors must
                                present a government issued photo identification prior to
                                the issuance of a badge and gaining access to
                                Commonwealth facilities.

             6.3.4.1.3. Visitor Monitoring: When visitors are in areas that host sensitive
                        information assets (e.g., data centers), visitors without CORI on
                        file must be monitored at all times by the Commonwealth host.

             6.3.4.1.4. Visitor Hosting: The Commonwealth host will assume responsibility
                        for their visitor for the duration of the visit. Visitors will be granted
                        access to internal secured areas only with authorization.

      6.3.5. Security for Public, Internal and Personnel Areas

          6.3.5.1.   Commonwealth Agencies and Offices must ensure that all areas that
                     provide access to the Commonwealth network implement controls
                     that protect against unauthorized physical access and damage from
                     environmental factors (e.g., fire, flood, natural or man-made disasters,
                     power and temperature or humidity variations).

          6.3.5.2.   The following are minimum considerations for securing offices, rooms
                     and facilities:

             6.3.5.2.1. Environmental Hazards: Hazardous and combustible materials
                        must be stored according to Material Safety Data Sheets (MSDS) to
                        reduce the risk of exposure.

             6.3.5.2.2. Shared Facilities: Physical and environmental controls will be
                        sufficient for protecting Commonwealth’s information in owned,
                        rented, and leased facilities.

Physical and Environmental Security Page 6 of 11

                6.3.5.2.3. Health and Safety Regulation Standards: Relevant health and
                           safety regulation (e.g., OSHA) standards will be considered to
                           ensure implemented protection controls meet requirements.

                6.3.5.2.4. Physical Access to Publicly Accessible Work Area Outlets: Areas
                           accessible to visitors will not have work area outlets (e.g., Ethernet
                           port) enabled unless network access is explicitly authorized.

                6.3.5.2.5. Physical Access to Telecommunication Equipment: Physical
                           access to wireless access points, gateways, handheld devices,
                           networking/communications hardware, and telecommunication
                           lines will be restricted and/or monitored.

      6.3.6. Security for Internal Secure Areas

            6.3.6.1.      Secured areas are those used by the Commonwealth to conduct
                          specific security or business-related functions that require the use of
                          confidential information.

            6.3.6.2.      The following requirements, at a minimum, will be considered to
                          protect the Commonwealth’s secure areas:

                6.3.6.2.1. Personnel Authorization: access to secured areas such as data
                           centers will be restricted to authorized personnel with a
                           demonstrated business justification. Secured areas, where
                           feasible, will not display any obvious signage indicating the
                           purpose of the area.

                6.3.6.2.2. Access Control Mechanisms: Secured areas will be subject to
                           additional entry controls such as locks, proximity card readers and
                           biometric identification.

                6.3.6.2.3. Audit Trail: An audit trail of access to secure areas will be
                           maintained and privileges will be reviewed regularly to assess
                           validity.

    6.4.     Equipment and Other Media Security

           6.4.1. Commonwealth Agencies and Offices must ensure that the
                  Commonwealth’s information assets, whether on-site or off-site, are
                  protected against unauthorized physical access, damage, or loss due to
                  physical and/or environmental causes.

           6.4.2. Physical and Environmental Protection

               6.4.2.1.     All equipment owned or managed by the Commonwealth will be
                            housed in Commonwealth facilities with a level of protection
                            commensurate with the sensitivity and criticality of the equipment

Physical and Environmental Security Page 7 of 11

                         and the information it handles (see IS.015 Asset Management
                         Standard).

            6.4.2.2.     Environmental Threats

                 6.4.2.2.1. The potential danger from environmental threats including
                            weather, malicious attacks, and accidents will be considered
                            and controls appropriate for risk mitigation will be
                            implemented to reduce the potential for an incident to occur.

                 6.4.2.2.2. Environmental conditions will be monitored in appropriate
                            areas. At a minimum, monitoring will be performed for
                            fire/smoke in the general facility areas. Internal secure areas
                            will be subject to additional monitoring for temperature, water,
                            power continuity, humidity and cleanliness.

             6.4.2.2.3. Environmental controls such as heating, ventilation, air
                        conditioning, drainage, fire suppression, emergency lighting,
                        continuous power and humidity control will be implemented in
                        facilities in accordance with risk assessments. Data centers will
                        contain elements of each environmental control at sufficient
                        levels.

            6.4.2.3.     Backup Power

                 6.4.2.3.1. Continuous power will be provided for mission-critical
                            information assets through battery-operated uninterrupted
                            power supply (UPS) protection. The use of generator backup
                            systems should be implemented if risk assessments warrant
                            higher levels of protection.

            6.4.2.4.     Shutdown Procedures

                 6.4.2.4.1. Clearly defined controls and procedures to enable an orderly
                            shutdown of computing resources in the event of a prolonged
                            power failure will be documented and distributed to the
                            personnel responsible for the shutdown process.

          6.4.2.5.     Emergency Power Shutoff

                 6.4.2.5.1. In the case of an emergency, emergency power off switches will
                            be located near emergency exits in equipment rooms to
                            facilitate rapid power down.

            6.4.2.6.     Alarm Systems

Physical and Environmental Security Page 8 of 11

                 6.4.2.6.1. Configuration of alarm systems will be periodically reviewed
                            and evaluated to detect malfunctions in the supporting utilities
                            and reconfigured as needed.

          6.4.2.7.     Voice Services

                 6.4.2.7.1. Telecommunications equipment will be connected to support
                            redundant connection points to the utility provider to prevent
                            failure in case of emergency. Voice services will be adequate to
                            meet local legal requirements for emergency communications.

      6.4.3. Off-Site Equipment and Security

            6.4.3.1.     Equipment (e.g., network and telecommunication devices, servers,
                         power, and cooling equipment) may only be taken off-site for valid
                         business reasons and with authorization from the Information
                         Owner.

            6.4.3.2.     Personnel who take equipment offsite are responsible for the
                         physical protection of the system and will ensure the equipment is
                         secure at all times.

          6.4.3.3.     Equipment taken off-site will be recorded when removed off-site and
                       recorded when returned as necessary.

      6.4.4. Cabling protection

            6.4.4.1.     Power and telecommunications cabling will be protected
                         adequately against risks such as interference, data capture or
                         physical damage. These cables will be easily identifiable using
                         appropriate markers or labels to ensure handling errors are minimal.

   6.5.   Maintenance of Information Assets

      6.5.1. Equipment maintenance controls, at a minimum, will include the following:

          6.5.1.1.     Equipment will be serviced in accordance with the
                       manufacturer’s/supplier’s recommendations and tested periodically.

          6.5.1.2.     Prior to the disposal or reuse of equipment, all data will be removed
                       or securely overwritten to ensure that any confidential data and
                       licensed software is removed (see Information Disposal in IS.015
                       Asset Management Standard).

      6.5.2. Upon termination of personnel and/or expiration of external business
             relationships, all organizationally owned equipment must be returned within
             ten (10) business days.

Physical and Environmental Security Page 9 of 11

       6.5.3. Food and water will not be stored in or around secure workspaces or other
              areas hosting mission-critical systems (e.g., data centers).

7.   CONTROL MAPPING
            Section           NIST SP800-53 R4 (1)      CIS 20 v6        NIST CSF
 6.1 Facility Control and          CP Family                -                -
 Secure Areas                        PE-1                   -             ID.GV-1
                                     PE-2                   -            PR.AC-2
                                     PE-9                   -             ID.BE-4
                                     PE-10                  -             PR.IP-5
                                     PE-11                  -             ID.BE-4
                                     PE-13                  -             PR.IP-5
                                     PE-15                  -             PR.IP-5
                                      AT-2              CSC 17            PR.AT-1
                                      AT-3               CSC 5            PR.AT-2
                                      PL-4                  -                -
                                     PS-6               CSC 13           PR.DS-5
                                     PE-1                   -             ID.GV-1
                                     PE-2                   -            PR.AC-2
                                     PE-3                   -            PR.AC-2
                                     PE-4                   -            PR.AC-2
                                     PE-6                   -            PR.AC-2
                                     PE-8                   -                -
                                     PE-9                   -             ID.BE-4
                                     PE-11                  -             ID.BE-4
                                     PE-12                  -             PR.IP-5
                                     PE-14                  -             PR.IP-5
                                     PE-16               CSC 1           PR.DS-3
                                     PE-18                  -             PR.IP-5
                                                            -            PR.IP-11
 6.2 Equipment and Other           MA Family                -                -
 Media Security                      MP-5                CSC 8            PR.PT-2
                                     MP-6                CSC 1           PR.DS-3
                                     PE-1                   -             ID.GV-1
                                     PE-3                   -            PR.AC-2
                                     PE-6                   -            PR.AC-2
                                    PE-16                CSC 1           PR.DS-3
                                    PE-19               CSC 13           PR.DS-5
                                    PE-20               CSC 19           DE.CM-2
                                     CM-9                CSC 3            PR.IP-1
                                   PS Family

Physical and Environmental SecurityPage 10 of 11

8.     DOCUMENT CHANGE CONTROL
 Version   Revised by                     Effective     Description of changes
 No.                                         date
 0.90      Jim Cusson                    10/01/2017   Corrections and formatting.
 0.92      John Merto                    01/02/2018     Corrections, Formatting
 0.95      Sean Vinck                      5/7/2018   Corrections and Formatting
 0.96      Andrew Rudder                  5/31/2018   Corrections and Formatting
 0.98      Anthony O’Neill               05/31/2018   Corrections and Formatting
 1.0       Dennis McDermitt              06/01/2018     Pre-Publication Review
 1.0       Andrew Rudder                  10/4/2018   Approved for Publication by:
                                                               John Merto
 1.1       Megan Perkins                  7/15/2020      Annual Review; Minor
                                                       corrections and formatting
 1.2       Sean M. Hughes                11/04/2021          Annual Review
 1.3       Sean M. Hughes                08/29/2022          Annual Review
 1.4       Thomas E. McDermott           11/30/2023     Corrections, Formatting,
                                                      Updating and Annual Review
 1.4       Anthony O’Neill               11/30/2023           Final Review
 1.5       Thomas E. McDermott           12/11/2024   Corrections, Formatting and
                                                             Annual Review
 1.5       Anthony O’Neill               12/11/2024           Final Review
 1.6       Thomas E. McDermott            2/24/2025    Updates, Corrections and
                                                               Formatting
 1.6       Miklos Lavicska                3/10/2025   Corrections and Formatting
 1.6       Anthony O’Neill                3/21/2025           Final Review

Physical and Environmental SecurityPage 11 of 11

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
