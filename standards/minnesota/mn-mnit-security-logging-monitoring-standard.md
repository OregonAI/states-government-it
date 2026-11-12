---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-security-logging-monitoring-standard
title: Security Logging and Monitoring Standard
doc_type: standard
citation: MNIT Security Logging and Monitoring Standard, Version 1.9
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Security%20Logging%20and%20Monitoring%20Standard_tcm38-323794.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 1a41c6634b88e9cb6baf533ac47714bbfe3a27a9dac7dff0e861e360f6a1e7e2
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

# Security Logging and Monitoring Standard (MNIT Security Logging and Monitoring Standard, Version 1.9)

## At a glance

Detective and preventive monitoring controls: what systems must log, log protection and retention.

## Full text

Security Logging and Monitoring Standard
From the Office of the Chief Information Officer, State of Minnesota

Version: 1.9
Effective Date: 1/1/2016
Revised: 12/31/2024
Approved: John Israel, State of MN Chief Information Security Officer         Date: 2/27/2025

Standard Statement
Detective and preventive information security monitoring controls must be in place to support the
confidentiality, availability, and integrity of State data and systems.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Table 1. Security Logging and Monitoring Controls

                                                                                                    Applicable
 Control                                                                                               Data
              Control Name                                   Control Detail
 Number                                                                                             Protection
                                                                                                  Categorization

             Logging              Implement automated logging on all systems to reconstruct            Low
                                  the following events:
                                                                                                    Moderate
                                      •    All actions taken by accounts with root or
                                           administrative privileges. (All system administrator       High
                                           commands while logged on as system administrator)
                                      •    Access to all log data.
     1                                •    All log-in attempts (successful and unsuccessful).
                                      •    All system log offs.
                                      •    Use of and changes to identification and
                                           authentication mechanisms—including but not limited
                                           to creation, modification, enabling, disabling, and
                                           removal of accounts and modifications of privileges—
                                           and all changes, additions, or deletions to accounts
                                           with root or administrative privileges.

Security Logging and Monitoring Standard                                                                       1

                                                                                                 Applicable
 Control                                                                                            Data
            Control Name                             Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

                                 •   Initialization, stopping or pausing of the logs.
                                 •   Creation and deletion of system-level objects.
                                 •   Setting/modifying logs and logging behavior.
                                 •   Setting/modifying firewall rules.
                                 •   Setting/modifying system configurations and
                                     parameters.
                                 •   All password changes.
                                 •   Switching accounts or running privileged actions from
                                     another account, (e.g., Linux/Unix SU or Windows
                                     RUNAS).
                                 •   Creation or modification of super-user groups.
                                 •   Subset of security administrator commands while
                                     logged on in the security administrator role.
                                 •   Subset of system administrator commands while
                                     logged on in the user role.
                                 •   Clearing of the audit log file
                                 •   Use of identification and authentication mechanisms
                                     (e.g., user ID and password)
                                 •   Change of file or user permissions or privileges (e.g.,
                                     use of suid/guid, chown, su)
                                 •   Remote access outside of the corporate network
                                     communication channels (e.g., modems, dedicated
                                     VPN) and all dial-in access to the system
                                 •   Changes made to an application or database by a
                                     batch file
                                 •   Application-critical record changes
                                 •   Changes to database or application records, where the
                                     application has been bypassed to produce the change
                                     (via a file or other database utility)
                                 •   All system and data interactions concerning FTI
                                 •   System and application alerts and error messages.
                                 •   System and application shutdown and restart.
                                 •   Security policy modifications.
                                 •   Printing sensitive information.
                                 •   Packet-screening denials originating from untrusted
                                     networks.
                                 •   Packet-screening denials originating from trusted
                                     networks.
                                 •   Modification of proxy services.
                                 •   Wireless activity.

Security Logging and Monitoring Standard                                                                    2

                                                                                                  Applicable
 Control                                                                                             Data
            Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

           Logging           Log all individual user access to data with a data protection          High
    2      Individual User   categorization of High.
           Access

           Content of Log    Logged events must contain the following information:                   Low
           Records
                                 •   User identification.                                         Moderate
                                 •   Type of event.
                                 •   Timestamp using internal system clocks that can be             High
                                     mapped to Coordinated Universal Time (UTC) or
    3                                Greenwich Mean Time (GMT).
                                 •   Success or failure indication.
                                 •   Identity or name of affected data, file, system
                                     component or resource.
                                 •   Program or command used to initiate the event.
                                 •   Source and destination addresses.

           Performance       Systems must be monitored for system resource utilization               Low
           Monitoring        and overall system availability to ensure the system meets
    4                        business availability and performance requirements.                  Moderate

                                                                                                    High

           Security System   Immediately report failures of critical security control systems        Low
           Failure           to security and system support personnel, including failures
                             of:                                                                  Moderate

                                 •   Firewalls                                                      High
                                 •   IDS/IPS
    5                            •   FIM
                                 •   Anti-virus
                                 •   Physical access controls
                                 •   Logical access controls
                                 •   Logging mechanisms
                                 •   Segmentation controls (if used)

Security Logging and Monitoring Standard                                                                     3

                                                                                                   Applicable
 Control                                                                                              Data
            Control Name                              Control Detail
 Number                                                                                            Protection
                                                                                                 Categorization

           Security System   Respond to failures of any critical security controls in a timely        Low
           Failure           manner. Processes for responding to failures in security
           Response          controls must include:                                                Moderate

                                 •   Restoring security functions                                    High
                                 •   Identifying and documenting the duration (date and
                                     time start to end) of the security failure
                                 •   Identifying and documenting cause(s) of failure,
                                     including root cause, and documenting remediation
    6                                required to address root cause
                                 •   Identifying and addressing any security issues that
                                     arose during the failure
                                 •   Performing a risk assessment to determine whether
                                     further actions are required because of the security
                                     failure
                                 •   Implementing controls to prevent cause of failure
                                     from reoccurring
                                 •   Resuming monitoring of security controls

           Log Review        Review the following using automated methods, where                     High
                             technically possible, at least daily:

                                 •   All security events.
                                 •   Logs of all systems that store, process, or transmit
                                     data with a data protection categorization of High.
                                 •   Logs of all critical system components
                                 •   Logs of all systems that perform security functions
                                     including but not limited to firewalls, intrusion
                                     detection systems/intrusion prevention systems, and
                                     authentication servers.
    7
                             Review logs of all other system components periodically based
                             on risk.

                             Correlate logs across different repositories to gain enterprise-
                             wide situational awareness.

                             Perform manual reviews of system logs randomly on demand
                             but at least once every thirty (30) days.

                             Exceptions and anomalies identified during the review process
                             must be investigated and security events addressed following
                             the information security incident management process.

Security Logging and Monitoring Standard                                                                      4

                                                                                                 Applicable
 Control                                                                                            Data
            Control Name                             Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

           Clock             Synchronize all system clocks at least hourly to a designated          Low
           Synchronization   internal time source that is accurate to the approved industry-
                             accepted authoritative time source. Time data must be               Moderate
                             protected from unauthorized modification.
                                                                                                   High
    8                        External primary and secondary time servers used must be
                             selected from the National Institute of Standards and
                             Technology (NIST) Internet time service. The secondary server
                             is selected from a different geographic region than the
                             primary server.

           Protection of     Logs must be secured by:                                               Low
           Logs
                                 •   Limiting access to those with a job-related need.           Moderate
                                 •   Protecting log files from unauthorized modification or
                                     deletion.                                                     High
    9                            •   Requiring log configuration changes to be approved by
                                     authorized security personnel.
                                 •   Only allowing defined personnel or roles to set or
                                     change which events are to be logged by specific
                                     systems.

Security Logging and Monitoring Standard                                                                    5

                                                                                                  Applicable
 Control                                                                                             Data
            Control Name                             Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

           Centralized Log   An authorized central log server must be in place that:                High
           Management
           Service               •   Collects/receives log data from systems that store,
                                     process, or transmit data with a data protection
                                     categorization of High.
                                 •   Collects/receives log data from systems/software that
                                     perform security functions including but not limited to
                                     firewalls, intrusion detection systems/intrusion
                                     prevention systems, authentication servers, and anti-
                                     malware software.
                                 •   Collects/receives log data in as near real time as is
                                     appropriate for the log source.
    10                           •   Provides log reduction and normalization.
                                 •   Does not alter the original content or time ordering of
                                     the log data.
                                 •   Ensures the confidentiality, integrity, and availability
                                     of stored logs.
                                 •   Monitors the availability of log sources.
                                 •   Alerts authorized security personnel of inappropriate
                                     or unusual activities.
                                 •   Compiles audit records into a system-wide, time-
                                     correlated audit trail.
                                 •   Alerts authorized security personnel when allocated
                                     log storage volume is nearing maximum storage
                                     capacity.

           Retention of      Retain log data for at least one year, with a minimum of three         High
           Logs              months immediately available for analysis.

                             Log data for Federal Tax Information (FTI) must be retained for
                             seven years.
    11
                             Sufficient storage capacity must be allocated to ensure log
                             data is maintained for the duration of the retention period.
                             The system must alert incident response personnel within 24
                             hours of log storage volume reaching 80 percent of the
                             repository’s maximum audit record storage capacity.

Security Logging and Monitoring Standard                                                                     6

                                                                                                Applicable
 Control                                                                                           Data
            Control Name                               Control Detail
 Number                                                                                         Protection
                                                                                              Categorization

           Change            Centrally managed change detection mechanisms (for                   High
           Detection         example, file integrity monitoring) must be in place to detect
                             and alert on unauthorized changes to:

                                 •   Critical system files.
                                 •   Configuration files.
    12
                                 •   Critical application files.
                                 •   Security log files.

                             Change detection mechanisms must be configured to perform
                             critical file comparisons at least daily events must be
                             immediately forwarded to an authorized central log server.

           Configuration     Centrally managed configuration checking must be in place to         High
    13     Checking          detect and report on system compliance to security
                             configuration baselines.

           Network           Centrally managed network intrusion detection and/or                  Low
           Intrusion         prevention must be in place to:
           Detection and                                                                        Moderate
           Prevention            •   Monitor network traffic between different zones of
                                     control and between the internet and internal                High
                                     network. Intrusion detection agents must be deployed
    14                               on the wireless side of the firewall.
                                 •   Monitor inbound and outbound connections for
                                     unusual or unauthorized activity or conditions.
                                 •   Perform daily system integrity checks of firewalls and
                                     other network access control systems.
                                 •   Network intrusion events must be continuously
                                     forwarded to an authorized central log server.

Security Logging and Monitoring Standard                                                                   7

                                                                                                Applicable
 Control                                                                                           Data
            Control Name                             Control Detail
 Number                                                                                         Protection
                                                                                              Categorization

           Host Intrusion    Host intrusion detection/prevention software must be in place        High
           Detection and     on systems that store, process, or transmit Federal Tax
           Prevention        Information (FTI), where technically possible, to monitor for
                             attack attempts and potential compromises. This software
                             must:

                                 •   Be actively running.
                                 •   Prevent users from disabling or altering the software.
    15                           •   Generate event logs and continuously forward to an
                                     authorized central log management service.
                                 •   Alert authorized personnel when indications of
                                     compromise or potential compromise occur including:
                                 •   Unauthorized export of information.
                                 •   Signaling to an external information system.
                                 •   Potential intrusions.
                                 •   Be centrally managed.

           Wireless          Centrally managed wireless intrusion detection must be in             Low
           Intrusion         place to identify unauthorized wireless devices and to detect
           Detection         attack attempts and potential compromises to the wireless          Moderate
                             network.
                                                                                                  High
                             Wireless network intrusion events must be continuously
    16                       forwarded to an authorized central log server.

                             Where wireless intrusion detection coverage is not in place
                             other processes must be implemented to detect unauthorized
                             wireless access points on a quarterly basis.

                             Incident response procedures must be implemented in the
                             event unauthorized wireless access points are detected.

Security Logging and Monitoring Standard                                                                   8

                                                                                                  Applicable
 Control                                                                                             Data
            Control Name                             Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

           Anti-Malware      Anti-malware software capable of detecting, removing, and               Low
           Software          protecting against all known types of malicious software and
                             malicious functions within other suspicious files on all systems     Moderate
                             commonly affected by malicious software and at critical points
                                                                                                    High
                             throughout the network. This software must:

                                 •   Be actively running.
                                 •   Prevent users from disabling or altering the software.
                                 •   Generate event logs and continuously forward to an
    17                               authorized central log server.
                                 •   Automatically check for and install updates at least
                                     daily.
                                 •   Perform desktop and critical system file scans as the
                                     files are downloaded, opened, or executed. Either
                                     block or quarantine malicious code and send an alert
                                     to the administrator in response to malicious code
                                     detection.
                                 •   Be capable of addressing the receipt of false positives.
                                 •   Be centrally managed.

           Anti-Malware      For systems not commonly affected by malicious software,                Low
           Review            perform evaluations at least annually to identify and evaluate
    18                       evolving malware threats to confirm whether such systems do          Moderate
                             not require anti-malware software.
                                                                                                    High

           Inspect Media     Inspect all media containing diagnostic and test programs for           Low
                             malicious code before the media are used in the information
    19                       system.                                                              Moderate

                                                                                                    High

           Spam Protection   Centrally managed spam protection mechanisms must be in                 Low
                             place at system entry and exit points to detect and act on
                             unsolicited messages.                                                Moderate
    20
                             Update spam protection mechanisms when new releases are                High
                             available following normal change processes.

Security Logging and Monitoring Standard                                                                     9

Reason for the Standard
Security monitoring and log management reduces the likelihood that malicious activity would go unnoticed and
affect the confidentiality, availability, or integrity of State data and systems.

Roles & Responsibilities
    •   Employees, Vendors, and Contractors
            o Be aware of and follow relevant information security policies, standards, and procedures.
            o Ensure information security is incorporated into processes and procedures.
            o Ensure vendors and contractors are following required information security controls.
            o Contact information security staff or email GRC@state.mn.us with questions about the
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
    •   Agency Data Practices Personnel
            o Assist agencies and personnel with questions on proper data use, collection, storage,
                destruction, and disclosure.

Applicability
This standard applies to all departments, agencies, offices, councils, boards, commissions, and other entities in
the executive branch of Minnesota State Government.

Related Information
Security Monitoring and Response Policy

State Standards and Authoritative Source Cross Mapping

Security Logging and Monitoring Standard                                                                        10

Glossary of Information Security Terms

History
Table 2. Version History

    Version                                       Description                                   Date

 1.0               Initial Release                                                          7/8/15

 1.1               Added Compliance Enforcement Date                                        12/29/2015

 1.2               Updated Compliance Enforcement Date and Template                         12/20/2016

 1.3               Updated Compliance Enforcement Date and Template                         10/26/2016

 1.4               New document title and updates for clarification and to include MARS-E   3/10/2020
                   requirements

 1.5               Fixed formatting errors and updated required antimalware scanning        11/1/2021

 1.6               Scheduled document refresh                                               10/1/2022

 1.7               Updated version number and revision date                                 10/1/2023

 1.8               Added enforcement language; updated version and revision date            12/2/2024

 1.9               Removed outdated MARS-E reference                                        1/12/2026

Contact
GRC@state.mn.us

Security Logging and Monitoring Standard                                                                 11

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
