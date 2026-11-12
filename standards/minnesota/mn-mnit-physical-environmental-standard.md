---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-physical-environmental-standard
title: Physical and Environmental Security Standard
doc_type: standard
citation: MNIT Physical and Environmental Security Standard, Version 1.8
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/admin/assets/Physical%20and%20Environmental%20Security%20Standard_tcm38-323787_tcm36-762150.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 8e71f2d4596d8cbad58ced4a860f4ee44f01782cd424ea0aed4ee78bd711c6d5
effective_date: '2016-01-01'
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

# Physical and Environmental Security Standard (MNIT Physical and Environmental Security Standard, Version 1.8)

## At a glance

Controls for physical access to state systems, media and data (the Department of Administration's asset host serves the MNIT standard). Version 1.8 replaces the version 1.1 file on the same host, which is left out.

## Full text

Physical and Environmental Security Standard
From the Office of the Chief Information Officer, State of Minnesota

Version:           1.8
Effective Date:    1/1/2016
Revised:           12/31/2024
Approved:          John Israel, State Chief Information Security Officer   Date: 3/20/2025

Standard Statement
Physical access to State systems, media, and data must be controlled to ensure the confidentiality, availability,
and integrity of State data.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Table 1. Physical and Environmental Security Controls

Physical and Environmental Security Standard                                                                        1

                                                                                               Applicable Data
 Control
            Control Name                              Control Detail                             Protection
 Number
                                                                                               Categorization

            Labeling          Media must be labeled to indicate the handling and access             High
    1
                              requirements.

            Secure Storage    Paper and electronic media containing State data must be              High
            of Paper and      kept under the immediate protection and control of
    2
            Electronic        authorized personnel or securely locked up.
            Media

            Media             Electronic media containing State data must be inventoried            High
            Inventory         at least annually. Inventories must be documented and any
    3
                              discrepancies with previous inventories must be investigated
                              and communicated to the security incident response team.

            Offsite Storage   All media sent to an off-site storage location must be:               High
                                  •   Labeled
                                  •   Encrypted.
                                  •   Secured in a locked container with the key retained
    4
                                      in State control.
                                  •   Protected from unauthorized access.
                              Off-site storage locations must be secure, and the security of
                              the storage location must be assessed annually.

Physical and Environmental Security Standard                                                                     2

                                                                                                Applicable Data
 Control
            Control Name                             Control Detail                               Protection
 Number
                                                                                                Categorization

            Media            The transport of any kind of paper or electronic media                  High
            Transport        containing State data must be strictly controlled, including
                             the following:

                                 •   Categorize the media based on the data it contains.
                                 •   Send the media by secured courier or other secure
                                     delivery method that can be accurately tracked.
                                 •   Monitor the transport to ensure that each shipment
                                     is properly and timely received and acknowledged.
                                 •   Document the transport of all media. Documentation
                                     must contain:
                                          o a. The name of media recipient.
                                          o b. Signature of media recipient.
                                          o c. Date/time media received.
                                          o d. Media control number and contents.
                                          o e. Movement or routing information.
                                          o f. If disposed of, the date, time, and method
                                              of destruction.
                                 •   Ensure only authorized personnel approve all media
    5                                that is moved from a secured area including when
                                     media is distributed to individuals.
                                 •   Restrict the activities associated with the transport of
                                     media to authorized personnel.
                                 •   Maintain accountability for media during transport
                                     outside of secured areas.
                                 •   Encrypt all electronic media containing data with
                                     data protection categorization of High.
                                 •   Ensure a current, retrievable copy of data is available
                                     for systems containing data with a Data Protection
                                     Categorization of High before movement of servers.
                                 •   Paper or electronic media containing Federal Tax
                                     Information (FTI) must be double sealed using one of
                                     the following:
                                          o One envelope within another envelope with
                                              the inner envelope marked “confidential”
                                              with some indication that only the
                                              designated official or delegate is authorized
                                              to open it.
                                 •   Boxes sealed with tamper evident seals.

Physical and Environmental Security Standard                                                                      3

                                                                                             Applicable Data
 Control
            Control Name                            Control Detail                             Protection
 Number
                                                                                             Categorization

            Secure           Paper containing State data must be securely disposed of          Moderate
            Disposal of      when no longer needed for business or legal reasons and in
            Paper            accordance with record retention requirements by:                    High

                                 •   Ensuring all employees have access to and use secure
                                     shred bins or crosscut shredding devices.
                                         o These devices must be crosscut shredders
                                              which produce particles that are 1 mm x 5
                                              mm (0.04 in. x 0.2 in.) in size or smaller.
                                 •   Physically securing shred bins.
    6                            •   Emptying secure shred bins on a periodic basis to
                                     ensure they do not fill up.
                                 •   Shredding, incinerating, or pulping hard-copy
                                     materials so that State data cannot be reconstructed.
                                 •   Ensuring the disposal or destruction is witnessed or
                                     carried out by authorized personnel.
                                 •   Third parties performing disposal must be National
                                     Association for Information Destruction (NAID)
                                     certified and the state must maintain a copy of, and
                                     periodically validate the NAID certification.

Physical and Environmental Security Standard                                                                   4

            Secure           Media must be securely disposed of when it is no longer            Moderate
            Disposal of      needed for business or legal reasons and in accordance with
            Electronic       record retention requirements as follows:                            High
            Media
                                 •   Review and approve media to be sanitized to ensure
                                     compliance with business, legal, and records
                                     retention requirements.
                                 •   Sanitize or destroy all media prior to disposal, release
                                     out of State control or reuse following the NIST
                                     Special Publication 800-88 Revision 1 Sanitization
                                     Methods
                                         o Media that will be reused in the same
                                              environment with the same or higher data
                                              protection categorization can follow the
                                              “Clear” method.
                                         o Media that will be surplused, returned to the
                                              vendor or otherwise sent outside of state
                                              control, or reused in an environment with a
                                              lower Data protection categorization must
                                              follow the “Purge” or “Destroy” methods.
                                         o Nonfunctional media, media that cannot be
                                              “Purged”, and media not being reused must
                                              follow the “Destroy” method.
    7
                                 •   Ensure the sanitization or destruction is witnessed or
                                     carried out by authorized personnel.
                                 •   Verify the media sanitization or destruction was
                                     successful by testing a representative sample at least
                                     once per year (every 365 days).
                                 •   Document sanitization and destruction actions
                                     including:
                                         o Personnel who reviewed and approved
                                              sanitization or disposal actions.
                                         o Types of media sanitized.
                                         o Sanitization methods used.
                                         o Date and time of the sanitization actions.
                                         o Personnel who performed the sanitization.
                                         o Verification actions taken.
                                         o Personnel who performed the verification.
                                         o Disposal action taken.
                                 •   Provide the business a certificate of destruction
                                     confirming disposition of the media.

                             Third parties performing data disposal must be National
                             Association for Information Destruction (NAID) certified and
                             the state must maintain a copy of, and periodically validate
                             the NAID certification.

Physical and Environmental Security Standard                                                               5

                                                                                                Applicable Data
 Control
            Control Name                             Control Detail                               Protection
 Number
                                                                                                Categorization

            Physical         Areas of the facility containing State systems and data must            Low
            Barriers         be physically separated from other areas of the facility by:
                                                                                                  Moderate
                                 •   Separating nonpublic areas from public areas with
                                     physical barriers (e.g., walls, doors, turnstiles, etc.)        High
                                     and identifying areas as nonpublic with prominent
                                     postings.
                                 •   Separating sensitive areas such as data centers,
                                     network closets, and areas storing or processing data
                                     with data protection categorization of High from
                                     other areas of the facility using at least two physical
                                     barriers. Protected information must be
    8
                                     containerized in areas where other than authorized
                                     employees may have access afterhours.
                                 •   Minimizing the number of entrances to nonpublic
                                     and sensitive areas.
                                 •   Controlling entry and exit points to nonpublic and
                                     sensitive areas of the facility using physical access
                                     control systems/devices and/or guards.

                             Restricting physical access to wireless access points,
                             gateways, VoIP network hardware, handheld devices,
                             networking/communications hardware, and
                             telecommunication lines.

Physical and Environmental Security Standard                                                                      6

                                                                                                Applicable Data
 Control
            Control Name                             Control Detail                               Protection
 Number
                                                                                                Categorization

            Physical Access Physical access to nonpublic and sensitive areas (data                   Low
            Control         centers, wiring closets, rooms where data with a Data
                            Protection Categorization of High is stored or processed, etc.)       Moderate
                            must be controlled by:
                                                                                                     High
                                 •   Developing, approving, and maintaining a list of
                                     individuals with authorized access to nonpublic and
                                     sensitive areas of the facility. This list must include:
                                         o Name of individual.
                                         o Agency or department name.
                                         o Name and contact information of agency
                                             point of contact.
                                         o Purpose for access.
                                 •   Reviewing and updating the access list detailing
                                     authorized access by individuals at least every six
                                     months for data centers and at least annually for all
                                     other areas.
                                 •   Authorizing access to nonpublic and sensitive areas
                                     based on the individual’s job function.
    9                            •   Prohibiting “piggybacking” or “tailgating” into
                                     nonpublic or sensitive locations.
                                 •   Verifying individual access authorizations before
                                     granting access.
                                 •   Enforcing physical access authorizations at defined
                                     entry/exit points
                                 •   Issuing badge access, keys and/or combinations only
                                     to authorized individuals.
                                 •   Revoking access when no longer needed and
                                     ensuring all physical access mechanisms, such as
                                     keys, access cards, etc., are returned, changed
                                     and/or disabled.
                                 •   Requiring the use of two factor authentication for
                                     physical access to data centers.
                                 •   Requiring the inspection of all bags and items
                                     entering data centers and limiting access to only
                                     those items that are needed to perform work.
                                 •   Requiring the completion of required background
                                     checks and training prior to granting access to data
                                     centers.

Physical and Environmental Security Standard                                                                      7

                                                                                              Applicable Data
 Control
            Control Name                            Control Detail                              Protection
 Number
                                                                                              Categorization

            Physical Access Video cameras and/or access control systems (e.g., badge            Moderate
            Monitoring      readers, smart cards, biometrics, etc.) must be used to
                            monitor and track all physical access attempts to nonpublic            High
                            and sensitive areas. Video and/or access control logs must:

                                 •   Capture the following information:
                                         o The owner of the access control device
                                              requesting access and/or the identity of the
                                              individual requesting access.
                                         o The success or failure of the request.
                                         o The date and time of the request.
                                 •   Be reviewed at least weekly and upon occurrence of
    10                               security incidents involving physical security and
                                     correlated with other entries.
                                 •   Unauthorized access must be reported to the
                                     security incident response team for investigation.
                                 •   Stored for at least 90 days for data centers and areas
                                     containing data with a data protection categorization
                                     of High.
                                 •   Be monitored 24 hours per day, 7 days per week by
                                     trained personnel who respond to potential
                                     incidents.
                                 •   Be analyzed by automated mechanisms to recognize
                                     potential intrusions and initiate designated response
                                     actions.

Physical and Environmental Security Standard                                                                    8

                                                                                            Applicable Data
 Control
            Control Name                            Control Detail                            Protection
 Number
                                                                                            Categorization

            Tamper           Systems processing credit cards or located in public spaces         Low
            Prevention       and all video cameras and physical access control devices
                             regardless of physical location, must be:                        Moderate

                                 •   Protected from unauthorized modification or                 High
                                     substitution.
                                 •   Periodically inspected to detect tampering or
                                     unauthorized substitution.

                             Users of these systems must be trained to detect tampering.
                             Training should instruct users to:

    11                           •   Verify the identity of any third-party persons
                                     claiming to be repair or maintenance personnel,
                                     prior to granting them access to modify or
                                     troubleshoot devices.
                                 •   Not install, replace, or return devices without
                                     verification.
                                 •   Be aware of suspicious behavior around devices (for
                                     example, attempts by unknown persons to unplug or
                                     open devices).
                                 •   Report suspicious behavior and indications of device
                                     tampering or substitution to appropriate personnel
                                     (for example, to a manager or security officer).

            Output Device    Prevent the unauthorized viewing of State data by:                  High
            Locations
                                 •   Locating printers and fax machines in secure areas.
    12                           •   Using privacy screens and/or positioning monitors
                                     and laptop screens so that unauthorized users
                                     cannot view the screen.

            System           Systems must be positioned within the facility to minimize          Low
            Locations        potential damage from physical and environmental hazards
    13                       and to minimize the opportunity for unauthorized access.         Moderate

                                                                                                 High

            Physical Device Workstations and laptop computers containing Federal Tax             High
            Lock            Information (FTI) must be physically secured to large objects
    14                      such as desks or tables when not in use. Smaller equipment
                            such as smartphones and tablets must be locked in a filing
                            cabinet or desk drawer when not in use.

Physical and Environmental Security Standard                                                                  9

                                                                                               Applicable Data
 Control
            Control Name                             Control Detail                              Protection
 Number
                                                                                               Categorization

            Alternate        Personnel working from locations not controlled by the State           High
            Work             must ensure the protection of State data. Appropriate
            Locations        security controls must be implemented at alternate work
                             sites that include, but are not limited to, laptop cable locks,
                             recording serial numbers and other identification
                             information about laptops, and disconnecting modems at
                             alternate work sites.
    15
                             Personnel must be provided a means to communicate with
                             information security personnel in case of security incidents
                             or problems.

                             Telework locations for personnel accessing Federal Tax
                             Information must be inspected to ensure that this data is
                             adequately protected. The results of each inspection must be
                             fully documented.

            Physical Access Keys, combinations, and other physical access devices must           Moderate
            Device          be protected by:
            Management                                                                              High
                                • Storing keys, combinations, and other physical access
                                    devices in a secure location.
                                • Inventorying and reconciling all keys and other
                                    physical access devices at least annually.
                                • Changing combinations at least annually and when
                                    an employee who knows or has access to them no
                                    longer has a need to access the area, room, or
    16                              container.
                                • Only giving keys, combinations, and other physical
                                    access devices to those who have a frequent need to
                                    have access to the area, room or container.
                                • Prohibiting the writing of combinations or PINs on a
                                    sticky-note, calendar pad, or any other item (even
                                    though it is carried on one’s person or hidden from
                                    view). If needed a written copy of the combination
                                    may be kept in an envelope that is secured in a
                                    container with appropriate security controls.

            Delivery and     All systems being brought into or removed from State data              Low
            Removal          centers must be authorized, monitored, controlled, and
    17                       documented.                                                         Moderate

                                                                                                    High

Physical and Environmental Security Standard                                                                 10

                                                                                                   Applicable Data
 Control
            Control Name                              Control Detail                                 Protection
 Number
                                                                                                   Categorization

            Personnel        State personnel with access to nonpublic areas of State                    Low
            Badges           facilities must be assigned a photo ID badge that
    18                       distinguishes State personnel from visitors. Badges must be             Moderate
                             always worn above the waist and visible while inside
                                                                                                        High
                             nonpublic areas.

            Visitor Access   Visitors to nonpublic or sensitive areas must be:                          Low

                                 •   Authorized before entering.                                     Moderate
                                 •   Escorted and always monitored within nonpublic or
                                     sensitive areas.                                                   High
                                 •   Identified by examining government issued photo
                                     identification (e.g., state driver’s license or passport)
    19                               for data centers and areas containing Federal Tax
                                     Information.
                                 •   Given a badge or other identification that:
                                         o Expires no later than the end of the visit.
                                         o Visibly distinguishes the visitors from
                                              authorized personnel.
                                         o Is returned before leaving the facility or at
                                              the date of expiration.

            Visitor Log      A visitor log must be used to maintain a physical audit trail of           Low
                             all visitor activity to nonpublic and sensitive areas. This visitor
                             log must:                                                               Moderate

                                 •   Be retained for a minimum of 5 years.                              High
                                 •   Be closed out at the end of each month and
                                     reviewed by management.
                                 •   Contain the following information:
    20                                   o Name of the visitor.
                                         o Organization of the visitor.
                                         o Signature of the visitor (electronic or
                                             physical).
                                         o Form of identification reviewed (if required).
                                         o Date of access.
                                         o Time of entry and departure.
                                         o Purpose of visit.
                                         o Name and organization of authorized escort.

Physical and Environmental Security Standard                                                                     11

                                                                                             Applicable Data
 Control
            Control Name                            Control Detail                             Protection
 Number
                                                                                             Categorization

            Maintenance      Physical access for cleaning, security and maintenance               Low
            Personnel        personnel must controlled by:
            Access                                                                             Moderate
                                 •   Maintaining a list of authorized maintenance
                                     organizations or personnel. This list must be updated        High
                                     at least monthly and include:
                                          o Name of vendor/contractor.
                                          o Name and phone number of State point of
                                              contact authorizing access.
                                          o Name and contact information of vendor
    21                                        point of contact.
                                          o Address of vendor/contractor.
                                          o Purpose and level of access.
                                 •   Ensuring that non-escorted maintenance and
                                     cleaning personnel have completed the same
                                     training, screening, and approval as authorized
                                     employees.
                                 •   Designating State personnel with required access
                                     authorizations and technical competence to
                                     supervise the maintenance activities of personnel
                                     who do not have the required access authorizations.

            Facilities       Permit only authorized maintenance personnel to access            Moderate
            Maintenance      infrastructure assets, including power generators, HVAC
                             systems, cabling, and wiring closets.                                High
    22                       Repairs and modifications to the physical components of a
                             facility which are related to security (for example, door
                             hinges and handles, walls, doors, and locks) must be
                             approved and documented.

            Power            Data center power equipment and power cabling for systems            Low
            Equipment        in the data center must be protected from damage and
    23      and Cabling      destruction.                                                      Moderate

                                                                                                  High

Physical and Environmental Security Standard                                                               12

                                                                                              Applicable Data
 Control
            Control Name                             Control Detail                             Protection
 Number
                                                                                              Categorization

            Emergency         Data centers must have the capability of shutting off power          Low
            Shutoff           to the data center or individual systems in emergency
                              situations. Emergency shutoff switches or devices must be:        Moderate

    24                            •   Located where they can safely and easily be                  High
                                      accessed.
                                  •   Protected from unauthorized or unintended
                                      activation.

            Emergency         Data centers must have:                                              Low
            Power
                                  •   A short-term uninterruptible power supply in place        Moderate
                                      to facilitate the transition of systems to long-term
                                      alternate power in the event of a primary power              High
    25                                source loss.
                                  •   A long-term alternate power supply that can
                                      maintain minimally required operational capability in
                                      the event of an extended loss of the primary power
                                      source.

            Emergency         Automatic emergency lighting that activates in the event of a        Low
            Lighting          power outage or disruption must be maintained and in place
                              to cover:                                                         Moderate

    26                            •   All emergency exits and evacuation routes within the         High
                                      facility.
                                  •   All areas within the facility supporting essential
                                      missions and business functions.

            Fire Protection   Fire suppression and detection devices/systems must be in            Low
                              place that:
                                                                                                Moderate
                                  •   Are supported by an independent energy source.
    27                            •   Activate automatically.                                      High
                                  •   Notify facilities personnel and the local fire
                                      department in the event of a fire detection or
                                      suppression activation.

Physical and Environmental Security Standard                                                                13

                                                                                                     Applicable Data
 Control
              Control Name                               Control Detail                                Protection
 Number
                                                                                                     Categorization

             Temperature        Data centers must have controls in place to:                               Low
             and Humidity
             Controls               •   Maintain temperature and humidity levels within the             Moderate
                                        facility where the information system resides within
                                        acceptable vendor-recommended levels.                              High
                                    •   Monitor temperature and humidity levels. Alert
                                        appropriate personnel in the event the temperature
    28                                  or humidity fall outside of acceptable levels
                                             o Evaluate the level of alert and follow
                                                  prescribed guidelines for that alert level.
                                             o Alert component management of possible
                                                  loss of service and/or media.
                                             o Report damage and provide remedial action.
                                                  Implement contingency plan, if necessary.

             Water Damage       Data centers must have controls in place to prevent damage                 Low
             Protection         from water leakage by:
                                                                                                        Moderate
                                    •   Providing master shutoff or isolation valves that are
                                        accessible, working properly and known to data                     High
    29
                                        center facilities personnel.
                                    •   Using automated mechanisms to detect the presence
                                        of water in the data center and alert data center
                                        facilities personnel.

Reason for the Standard
Physical security is essential to ensure the confidentiality availability and integrity of State data. Physical controls
prevent the unauthorized or unintended disclosure or destruction of State data.

Roles & Responsibilities
    •    Employees, Vendors, and Contractors
            o Be aware of and follow relevant information security policies, standards, and procedures.
            o Ensure information security is incorporated into processes and procedures.
            o Ensure contract language with vendors and contractors includes required information security
               controls.
            o Consult with information security staff on the purchase and procurement of information
               technology systems or services.

Physical and Environmental Security Standard                                                                         14

            o   Contact information security staff or email GRC@state.mn.us with questions about the
                information security policies, standards, or procedures.
    •   Supervisors and Managers
            o Ensure employees and contractors are proficient in the information security policies, standards
                and procedures that are relevant to their role.
            o Hold employees accountable for following the information security policies, standards, and
                procedures.
    •   Information Technology Personnel
            o Apply appropriate controls to the design, operation and maintenance of systems, processes, and
                procedures in conformance with the information security policies, standards, and procedures.
    •   Information Security Personnel
            o Develop, maintain, and assess compliance with the information security policies, standards, and
                procedures.
            o Develop, maintain, and implement a comprehensive information security program.
            o Provide training on information security policies, standards, and procedures.
            o Assist agencies and personnel with understanding and implementing information security
                policies, standards, and procedures.
            o Notify appropriate personnel of applicable threats, vulnerabilities and risks to State data or
                systems.
    •   Agency Data Practices Personnel
            o Assist agencies and personnel with questions on proper data use, collection, storage,
                destruction, and disclosure.

Applicability
This standard applies to all departments, agencies, offices, councils, boards, commissions, and other entities in
the executive branch of Minnesota State Government.

Related Information
Physical and Environmental Security Policy

State Standards and Authoritative Source Cross Mapping

Glossary of Information Security Terms

Physical and Environmental Security Standard                                                                    15

History
Table 2. Version History

    Version                                      Description                           Date

 1.0               Initial Release                                                 7/8/2015

 1.1               Added Compliance Enforcement Date                               12/29/2015

 1.2               Updated Compliance Enforcement Date and Template                12/20/2016

 1.3               Updated Compliance Enforcement Date and Template                10/26/2017

 1.4               Scheduled Document Refresh                                      3/10/2020

 1.5               Scheduled Document Refresh                                      11/1/2021

 1.6               Scheduled document refresh                                      10/1/2022

 1.7               Table formatting; updated version number and revision date      10/1/2023

 1.8               Added enforcement language; updated version and revision date   12/2/2024

Contact
GRC@state.mn.us

Physical and Environmental Security Standard                                                    16

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
