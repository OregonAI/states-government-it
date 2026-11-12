---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-secure-configuration-standard
title: Secure Configuration Standard
doc_type: standard
citation: MNIT Secure Configuration Standard, Version 1.9
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Secure%20Configuration%20Standard_tcm38-323788.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 336265b3fc42c9877e33e2ab45dd776f72c6ade721699ba523df12c9365693ec
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

# Secure Configuration Standard (MNIT Secure Configuration Standard, Version 1.9)

## At a glance

Controls so that all state systems are approved, inventoried and securely configured with unnecessary functionality disabled.

## Full text

Secure Configuration Standard
From the Office of the Chief Information Officer, State of Minnesota

Version: 1.9
Effective Date: 1/1/2016
Revised: 12/31/2024
Approved: John Israel, State of MN Chief Information Security Officer          Date: 2/27/2026

Standard Statement
All State systems must be approved, inventoried, and securely configured with all unnecessary functionality
disabled to support the confidentiality, availability, and integrity of State data.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Table 1. Secure Configuration Controls

                                                                                                      Applicable
 Control                                                                                                 Data
                Control Name                                  Control Detail
 Number                                                                                               Protection
                                                                                                    Categorization

              Configuration         A configuration management plan must be in place that:               Low
              Management
              Plan                       •   Addresses roles, responsibilities, and configuration     Moderate
                                             management processes and procedures.
                                         •   Establishes a process for identifying configuration        High
                                             items throughout the system development life cycle
     1                                       (SDLC) and for managing the configuration of the
                                             configuration items.
                                         •   Defines the configuration items for the system and
                                             places the configuration items under configuration
                                             management.
                                         •   Protects the configuration management plan from
                                             unauthorized disclosure and modification.

Secure Configuration Standard                                                                                    1

                                                                                                 Applicable
 Control                                                                                            Data
             Control Name                              Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

            Change Control      Change control processes and procedures must be followed            Low
                                for all changes to systems. The change control process must
                                include:                                                         Moderate

                                    •   Documentation of all changes in change request             High
                                        forms.
                                    •   Review of proposed changes by the change advisory
                                        board who approves or disapproves such changes
                                        with explicit consideration for security impact
                                        analyses.
                                    •   Documentation of impact.
                                    •   Documentation of change decisions associated with
                                        the system including approvals.
                                    •   Functionality testing to verify that the change does
                                        not adversely impact the security of the system.
    2                               •   Back-out procedures.
                                    •   Documentation of security flaws and flaw
                                        resolution.
                                    •   Implementation of approved configuration-
                                        controlled changes to the information system.
                                    •   Communication of significant changes to impacted
                                        individuals and organizations.
                                    •   Implementation of all relevant Enterprise Security
                                        Standards on all new or changed systems and
                                        networks.

                                Change control records must be maintained for the life of
                                the system.

                                Activities associated with changes must be periodically
                                audited and reviewed.

Secure Configuration Standard                                                                               2

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            System Inventory    An inventory of all hardware and software must be                    Low
                                maintained and updated through manual inventory checks
                                or a network monitoring tool that automatically maintains         Moderate
                                the inventory. Inventory information must be updated at
                                                                                                    High
                                least annually and during installations, removals, and system
                                updates. Inventory processes must prevent the duplication
                                of inventory items.

                                When a centralized inventory system is available, all
                                hardware and software must be registered in it.

                                The hardware and device inventory must include:

                                    •   Data protection categorization.
                                    •   Business owner.
                                    •   Business owner contact information.
                                    •   Business justification
                                    •   Physical location.
                                    •   Asset tag.
                                    •   Serial number.
    3                               •   Operating system version.
                                    •   Make and model of the device.
                                    •   Host/machine name
                                    •   IP address if static.
                                    •   MAC address.
                                    •   Service delivery support team owner.
                                    •   Service delivery support team contact information.
                                    •   Compliance obligations.

                                The software and application inventory must include:

                                    •   Application name.
                                    •   Application ID.
                                    •   Data protection categorization.
                                    •   Business owner.
                                    •   Business owner contact information.
                                    •   Service delivery support team owner.
                                    •   Service delivery support team contact information.
                                    •   License Number.
                                    •   Host devices.
                                    •   Compliance obligations.

Secure Configuration Standard                                                                                3

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                               Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Approved            A list of all approved hardware and software along with any          Low
            Software and        usage restrictions must be documented and maintained. All
            Hardware            approved software must be:                                        Moderate

                                    •   Legally licensed.                                           High
                                    •   Used in accordance with contract agreements and
    4                                   copyright laws.
                                    •   Approved by MNIT.
                                    •   Securely configured.

                                Software and associated documentation protected by
                                quantity licenses must be tracked to ensure copying and
                                distribution comply with licensing agreements.

            Unapproved          Users must be prevented from installing or using                     Low
            Hardware and        unapproved or unlicensed hardware or software on State
            Software            systems through automated methods.                                Moderate

                                Systems must be continuously monitored for unapproved or            High
                                unlicensed hardware or software. Any unapproved or
    5                           unlicensed software or hardware must be disabled or
                                removed.

                                The use of peer-to-peer file sharing technology must be
                                restricted to ensure that this capability is not used for the
                                unauthorized distribution, display, performance, or
                                reproduction of copyrighted work.

            Personal Devices    Devices not owned and supported by the State must be                High
                                prohibited from storing, processing, or transmitting data
    6                           with a data protection categorization of High or from
                                supporting systems with a data protection categorization of
                                high.

            Unsupported         Hardware must be replaced or retired prior to the end of             Low
            Systems             vendor support.
    7                                                                                             Moderate
                                Operating systems and all software must be upgraded,
                                replaced, or retired prior to end of unpaid support.                High

Secure Configuration Standard                                                                                4

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Patch               All systems including firmware, operating systems,                   Low
            Management          applications, and other software must be protected from
                                known vulnerabilities by installing applicable vendor-            Moderate
                                supplied security patches. Install security patches according
                                                                                                    High
                                to the schedule specified in the Threat and Vulnerability
                                Management Standard

                                Where possible software and firmware updates must be
    8                           tested in a test environment for effectiveness and potential
                                side effects before installation.

                                Where possible utilize a centrally managed the patch
                                management process.

                                Applications that go through vendor patch regression testing
                                must be patched within 30 days of vendor approval, or 7
                                days for Severity 1 vulnerabilities after vendor approval.

            Secure              Secure configuration standards must be developed and                 Low
            Configuration       maintained for all systems. These standards must address all
            Standards           known security vulnerabilities and be consistent with             Moderate
                                industry-accepted system hardening standards. These
    9                                                                                               High
                                standards must be updated annually and when required due
                                to system upgrades, patches, or other significant changes.
                                Use CIS Level 1 benchmarks as a starting point if a specific
                                secure configuration standard is not yet available.

            Secure              Secure configurations must be implemented on all systems.            Low
            Configurations      Any deviations from the standards must be identified,
                                documented, and approved. System configurations must be           Moderate
    10                          reviewed and updated annually and when required due to
                                                                                                    High
                                system upgrades, patches, or other significant changes.

                                Older versions of baseline configuration of the system must
                                be retained as deemed necessary to support rollback.

Secure Configuration Standard                                                                                5

                                                                                                   Applicable
 Control                                                                                              Data
             Control Name                               Control Detail
 Number                                                                                            Protection
                                                                                                 Categorization

            Security Function   Automated processes must be in place to:                             High
            Verification
                                    •   Verify the correct operation of defined security
                                        functions upon system startup and restart, upon
                                        command by the administrator with appropriate
                                        privilege, and monthly.
    11                              •   Notify system administration of failed security
                                        verification tests.
                                    •   Shut the information system down, restart the
                                        information system, or perform some other defined
                                        alternative action(s) when anomalies are
                                        discovered.

            Least               Enable only necessary services, protocols, daemons, etc., as          Low
            Functionality       required for the function of the system. All unnecessary
    12                          functionality, such as scripts, drivers, features, subsystems,     Moderate
                                file systems, and unnecessary web servers must be
                                                                                                     High
                                removed.

            Process Isolation   The information system maintains a separate execution                 Low
                                domain for each executing process.
    13                                                                                             Moderate

                                                                                                     High

            System Defaults     Vendor-supplied default passwords, encryption keys, SNMP              Low
                                community strings, and other authenticators must be
                                changed, and unnecessary default accounts must be                  Moderate
                                removed or disabled before installing a system on the
    14                                                                                               High
                                network. Public "read" and "write" access to files, objects,
                                and directories that may directly impact system functionality
                                and/or performance, or that contain sensitive information
                                must be disabled.

            Separate            Implement only one primary function per server to prevent            High
            Functions           functions that require different security levels from co-
    15                          existing on the same server. (For example, web servers,
                                database servers, and DNS should be implemented on
                                separate servers.)

Secure Configuration Standard                                                                                 6

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Periodic Review     For systems in scope for ARC-AMPE:                                  High

                                    •   The information system must be reviewed at least
                                        quarterly to identify and eliminate unnecessary
    16                                  functions, ports, protocols, and/or services.
                                    •   Functions, ports, protocols, and services within the
                                        information system deemed to be unnecessary
                                        and/or non-secure must be disabled.

            Boot Settings       System initialization (boot) settings must be password-             High
    17
                                protected

            Memory              Systems must be configured to protect memory from                    Low
            Protection          unauthorized code execution. (For example, utilizing data
    18                          execution prevention or address space layout                      Moderate
                                randomization.)
                                                                                                    High

            Mobile Code         Use of mobile code must be restricted by:                         Moderate

                                    •   Defining acceptable and unacceptable mobile code            High
                                        and mobile code technologies.
                                    •   Establishing usage restrictions and implementation
                                        guidance for acceptable mobile code and mobile
                                        code technologies.
                                    •   Authorizing, monitoring, and controlling the use of
                                        mobile code within the information system.
    19
                                NOTE: Mobile code technologies include, for example, Java,
                                JavaScript, ActiveX, Postscript, PDF, Shockwave movies, Flash
                                animations, and VBScript, which are common installations
                                on most end user workstations. Usage restrictions and
                                implementation guidance apply to both the selection and
                                use of mobile code installed on servers and mobile code
                                downloaded and executed on individual workstations and
                                devices (e.g., tablet computers and smartphones).

Secure Configuration Standard                                                                                7

                                                                                                   Applicable
 Control                                                                                              Data
             Control Name                              Control Detail
 Number                                                                                            Protection
                                                                                                 Categorization

            Limit User Access   User functionality must be separate from system                       Low
                                management/administration functionality. Non-privileged
    20                          users must be prevented from executing privileged                  Moderate
                                functions including disabling, circumventing, or altering
                                                                                                     High
                                implemented security safeguards/countermeasures.

            Information in      The system must prevent unauthorized or unintended                    Low
            Shared Resources    information transfer via shared system resources by
                                ensuring that:                                                     Moderate

                                    •   Users of shared system resources cannot                      High
                                        intentionally or unintentionally access information
    21                                  remnants, including encrypted representations of
                                        information, produced by the actions of a prior user
                                        or system process acting on behalf of a prior user.
                                    •   System resources shared between two (2) or more
                                        users are released back to the information system
                                        and are protected from accidental or purposeful
                                        disclosure.

            Network             Network connections associated with a communications                 High
            Disconnect          session must be terminated at the end of the session or:

                                    •   Forcibly de-allocates communications session
                                        Dynamic Host Configuration Protocol (DHCP) leases
                                        after seven (7) days.
                                    •   Forcibly disconnects inactive Virtual Private Network
    22
                                        (VPN) connections after thirty (30) minutes or less of
                                        inactivity.

                                Note: This control addresses the termination of network
                                connections that are associated with communications
                                sessions (i.e., network disconnect) in contrast to user-
                                initiated logical sessions.

            Remote              All non-console administrative access must be encrypted               Low
            Management          using strong cryptography. Technologies such as SSH, VPN,
    23                          or TLS must be used for web-based management and other             Moderate
                                non-console administrative access.
                                                                                                     High

Secure Configuration Standard                                                                                 8

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Secure              All equipment accessible via a network must be registered in         Low
            Name/Address        an approved Name/Address Resolution Service.
            Resolution                                                                            Moderate
            Service             Name and Address Resolution Service must be configured
                                to:                                                                 High

                                   •   Support both forward and reverse lookup of any
                                       network name, network alias, or IP address in use
                                       on state networks.
                                   •   Provide additional data origin authentication and
                                       integrity verification artifacts along with the
                                       authoritative name resolution data the system
    24                                 returns in response to external name/address
                                       resolution queries.
                                   •   Provide the means to indicate the security status of
                                       child zones and (if the child supports secure
                                       resolution services) to enable verification of a chain
                                       of trust among parent and child domains, when
                                       operating as part of a distributed, hierarchical
                                       namespace.
                                   •   Request and perform data origin authentication and
                                       data integrity verification on the name/address
                                       resolution responses the system receives from
                                       authoritative sources.

            Split Tunneling     Devices must be prevented from simultaneously establishing           Low
                                connections with internal state systems or networks and
    25                          communicating via some other connection to resources in           Moderate
                                external networks.
                                                                                                    High

            Secure Services     Additional security features must be applied for any                 Low
                                required services, protocols or daemons that are insecure to
                                address the weaknesses in that service, protocol, or daemon       Moderate
    26
                                (For example, use secured technologies such as SSH, S-FTP,
                                                                                                    High
                                SSL, or IPSec VPN to protect insecure services such as
                                NetBIOS, file-sharing, Telnet, FTP, etc.).

Secure Configuration Standard                                                                                9

                                                                                             Applicable
 Control                                                                                        Data
              Control Name                              Control Detail
 Number                                                                                      Protection
                                                                                           Categorization

            File Sharing        File sharing must be disabled on all wireless clients.          Low

    27                                                                                       Moderate

                                                                                               High

            Integrity           Electronic mechanisms to corroborate that data with high        Low
                                integrity needs has not been altered or destroyed in an
                                unauthorized manner must be implemented. Possible            Moderate
                                mechanisms could include:
                                                                                               High
    28
                                    •   Error-correcting memory
                                    •   Magnetic disk storage
                                    •   Digital signatures
                                    •   Check sum technology.

Secure Configuration Standard                                                                           10

                                                                                                  Applicable
 Control                                                                                             Data
              Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Virtualization      Virtual environments must be configured to:                         High

                                    •   Secure programs that control the hypervisor and
                                        restrict them to authorized administrators only.
                                    •   Enforce separation between VMs.
                                    •   Disable functions that allow one VM to share data
                                        with the hypervisor or another VM, such as
                                        clipboard sharing or shared disks.
                                    •   Disable special VM functions available to system
                                        administrators in a virtualized environment that can
                                        leverage the shared memory space in a virtual
                                        environment between the hypervisor and VM.
                                    •   Prevent data from being dumped outside of the VM
    29                                  when system errors occur.

                                Backups (virtual machine snapshot) must be properly
                                secured and must be stored in a logical location where the
                                backup is only accessible to those with a need-to-know.

                                Virtual environments containing Criminal Justice Information
                                must:

                                    •   Isolate the host from the virtual machine.
                                    •   Physically separate Internet facing Virtual Machines
                                        (web servers, portal servers, etc.) from internal
                                        Virtual Machines.
                                    •   Locate device drivers that are “critical” within a
                                        separate guest operating system.

            Decommissioning     All disk space utilized by a virtual device must be sanitized     Moderate
    30      Virtual Devices     using a secure erase function once the virtual device is
                                decommissioned.                                                     High

            Remote Access       Remote access connections must:                                      Low

                                    •   Be formally authorized prior to allowing such             Moderate
                                        connections.
                                    •   Restrict the use of privileged command execution to         High
    31
                                        only those necessary and authorized for compelling
                                        operational needs.
                                    •   Prohibit FTI or CJI from being accessed from outside
                                        the United States.

Secure Configuration Standard                                                                                11

                                                                                                  Applicable
 Control                                                                                             Data
              Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Resource            The information system must protect the availability of              Low
            Availability        resources by allocating resources by priority and/or quota.
    32                                                                                            Moderate

                                                                                                    High

            Denial of Service    Implement security safeguards to protect against or limit           Low
            Protection          the effects of the types of denial-of-service attacks defined
                                on the following websites:                                        Moderate

    33                              •   CISA: Understanding and Responding to Distributed           High
                                        Denial-of-Service Attacks (cisa.gov)
                                    •   http://www.sans.org/dosstep OWASP: Denial of
                                        Service - OWASP Cheat Sheet Series

Secure Configuration Standard                                                                                12

                                                                                                 Applicable
 Control                                                                                            Data
             Control Name                             Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

            Controlled          All system maintenance must:                                        Low
            Maintenance
                                   •   Be scheduled, performed, documented, and                  Moderate
                                       reviewed in accordance with manufacturer or
                                       vendor specifications and internal State                    High
                                       requirements.
                                   •   Ensure support and/or spare parts for defined key
                                       system components (defined in the applicable
                                       security plan) are obtained within the applicable
                                       Recovery Time Objective (RTO) specified in the
                                       contingency plan.
                                   •   Be approved by authorized personnel and
                                       monitored.
                                   •   Not remove the system from the facility without
                                       approval from authorized personnel.
                                   •   Only be performed using inspected and approved
    34                                 maintenance tools and media.
                                            o Maintenance tools must be inspected for
                                                 Not Public Data prior to removal from the
                                                 facility and any not public data must be
                                                 securely removed from the device (sanitized
                                                 or destroyed).
                                   •   Validate security controls are still functioning
                                       properly after maintenance is completed.
                                   •   Require that the applicable business owner (or an
                                       official designated in the applicable security plan)
                                       explicitly approve the removal of the information
                                       system or system components from organizational
                                       facilities for off-site maintenance or repairs.
                                   •   Sanitize equipment to remove all not public data
                                       from associated media prior to removal from State
                                       facilities for off-site maintenance or repairs.
                                   •   Be documented in maintenance records.

Secure Configuration Standard                                                                               13

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Personal Firewall   A personal firewall must be installed and actively running on        Low
                                all end user devices that have a full-feature operating
                                system (i.e., laptops, desktops, or tablets with Windows or       Moderate
                                Linux/Unix operating systems). At a minimum, the personal
                                                                                                    High
                                firewall must:

                                    •   Be activated when connected to an untrusted
    35                                  network.
                                    •   Manage program access to the Internet.
                                    •   Block unsolicited requests to connect to the user
                                        device.
                                    •   Filter incoming traffic by IP address or protocol.
                                    •   Filter incoming traffic by destination ports.
                                    •   Maintain an IP traffic log.
                                    •   Not be alterable by the users of the device.

Secure Configuration Standard                                                                                14

                                                                                                 Applicable
 Control                                                                                            Data
             Control Name                             Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

            Mobile Device       Mobile device management must be used to enforce secure             Low
            Management          configurations on all State, employee, or contractor mobile
                                devices with access to State data or networks. All mobile        Moderate
                                device access to State systems or networks must be
                                                                                                   High
                                authorized. Mobile device management must be configured
                                to:

                                   •   Remotely lock the device if necessary.
                                   •   Remotely wipe the device if necessary.
                                   •   Set and lock the device configuration.
                                   •   Detect “rooted” and “jailbroken” devices.
                                   •   Enforce folder or disk level encryption.
                                   •   Apply mandatory policy settings on the device.
                                   •   Detect unauthorized configurations or
    36
                                       software/applications.
                                   •   Disable system functionality that provides for
                                       automatic execution of code on mobile devices
                                       without user direction.
                                   •   For devices containing or accessing FTI
                                           o Disable wireless personal area networks
                                               that allow a mobile device to connect to a
                                               computer via Bluetooth or near field
                                               communication (NFC) for data
                                               synchronization and storage.
                                   •   Access to hardware, such as the digital camera,
                                       global positioning system (GPS), and universal serial
                                       bus (USB) interface, must be disabled to the extent
                                       possible.

            Encrypt End User    All laptops, desktops and mobile devices must be encrypted.         Low
            Devices
    37                                                                                           Moderate

                                                                                                   High

Secure Configuration Standard                                                                               15

                                                                                                    Applicable
 Control                                                                                               Data
             Control Name                              Control Detail
 Number                                                                                             Protection
                                                                                                  Categorization

            Multi-Functional    Multi-functional devices (MFD) or High-Volume Printers                 Low
            Devices and High-   must meet the following requirements:
            Volume Printers                                                                         Moderate
                                   •   Maintain a current security baseline for secure
                                       configuration and operation of the MFD or High-                High
                                       Volume Printer.
                                   •   Implement least functionality controls including
                                       disabling all unneeded network protocols, services,
                                       and assigning a dedicated static IP address to the
                                       MFD or High-Volume Printer.
                                   •   Configure access enforcement controls correctly,
                                       including access controls for file shares,
                                       administrator and non-administrator privileges, and
    38                                 document retention functions.
                                   •   Lock MFD's or High-Volume Printers with a
                                       mechanism to prevent physical access to the hard
                                       disk.
                                       Ensure firmware is up to date with the most current
                                       firmware available and should be currently
                                       supported by the vendor.
                                   •   Enable logging of devices and print spoolers,
                                       including logging of user access and fax logs (if fax is
                                       enabled). Logs must be collected and reviewed by a
                                       security administrator.
                                   •   Disposal of all hardware follows media sanitization
                                       and disposal procedure requirements.

Secure Configuration Standard                                                                                  16

                                                                                                    Applicable
 Control                                                                                               Data
             Control Name                               Control Detail
 Number                                                                                             Protection
                                                                                                  Categorization

            Storage Area        SAN environments must meet the following requirements:                High
            Networks
                                    •   Data with a Data Protection Categorization of High
                                        must be segregated from other agency data within
                                        the SAN environment.
                                    •   Access controls must be implemented and strictly
                                        enforced for all SAN components to limit access to
                                        disks containing to authorized users.
                                    •   Fiber channel devices must be configured to
                                        authenticate other devices with which they
                                        communicate in the SAN and authenticate
    39                                  administrator connections.
                                    •   Data with a Data Protection Categorization of High
                                        must be encrypted while in transit within the SAN
                                        environment. SAN management traffic must also be
                                        encrypted for SAN components.
                                    •   All components of the SAN must be hardened in
                                        accordance with State security baseline
                                        configuration standards.
                                    •   SAN components must maintain logs which must
                                        reviewed at least weekly to track access to Data
                                        Protection Categorization of High in the SAN
                                        environment.

            Virtual Desktop     Secure Virtual Desktop Infrastructure (VDI) that is used as a         High
            Infrastructure      means of remote access to data or systems with a Data
                                Protection Categorization of High by:

                                    •   Segregating VDI components so that boundary
                                        protections can be implemented, and access
                                        controls are granulized.
    40                              •   Utilizing an access control system that is specifically
                                        configured to address the complicated nature of the
                                        environment—ensure only authorized clients who
                                        conform to State security policy are permitted
                                        access to the VDI.
                                    •   Configuring the hypervisor, management consoles,
                                        and other VDI components using the secure
                                        configuration guidelines provided by the vendor.

Secure Configuration Standard                                                                                 17

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                              Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Web Browser         Web browsers must:                                                   Low

                                   •   Have security enhancements, such as pop-up                 Moderate
                                       blocker and content filtering enabled.
                                   •   Be configured in accordance with the principle of            High
    41
                                       least functionality and unnecessary items, such as
                                       third-party add-ons, must be disabled.
                                   •   Only enable Java if there is a valid business need and
                                       it has been approved.

            Non-Repudiation     Individuals (or processes acting on behalf of an individual)        High
                                must be prevented from falsely denying having performed a
    42                          particular action by employing non-repudiation techniques
                                or mechanisms including, for example, digital signatures and
                                digital message receipts.

            Mask Data on        Data with a data protection categorization of High must be          High
    43      Display             masked when displayed except for personnel who need
                                access to the data for job duties.

            Removable           The use of system and removable media (CD, USB stick,                Low
            Media               portable hard drive, etc.) on workstations must only be
    44                          enabled for users with an approved business need. If system       Moderate
                                and removable media boot access is authorized, boot access
                                                                                                    High
                                must be password protected.

            Collaborative       All collaborative computing devices (networked white                 Low
            Computing           boards, cameras, microphones, etc.) must be explicitly
            Devices             authorized and configured to:                                     Moderate
    45
                                   •   Prohibit remote activation.                                  High
                                   •   Provide an explicit indication of use to users
                                       physically present at the devices.

Secure Configuration Standard                                                                                18

                                                                                                  Applicable
 Control                                                                                             Data
             Control Name                               Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

            Encryption in       Strong cryptography and security protocols must be used to        Moderate
            Transit             protect State data during transmission including the
                                following:                                                          High

                                    •   Always encrypt data with a data protection
                                        categorization of High in transmission.
    46                              •   Encrypt data with a data protection categorization
                                        of Moderate in transmission over external networks.
                                    •   Only accept trusted keys and certificates.
                                    •   Only support secure versions or configurations of
                                        the protocol in use.
                                    •   Use an encryption strength that is appropriate for
                                        the encryption methodology in use.

            Certificate         All public key certificates used in State systems must be:           Low
            Management
                                    •   Authorized by a supervisor or a responsible official.     Moderate
                                    •   Implemented using a secure process that verifies
                                        the identity of the certificate holder.                     High
                                    •   Issued only to the intended party.
                                    •   Issued from trusted secure internal certificate
    47                                  authority or obtained from an approved service
                                        provider.
                                    •   Valid for no longer than 3 years.
                                    •   Revoked if any of the following is true:
                                            o Associated private key is compromised.
                                            o Management requests revocation
                                            o Certificate is no longer needed

            Encryption at       All data with a data protection categorization of High,             High
            Rest                including Federal Tax Information (FTI), must be encrypted
                                at rest using FIPS 140-2 validated encryption methods.
    48
                                    •   The encryption process must ensure that all stored
                                        FTI always remains protected, including during
                                        backups and in any replicated environments.

Secure Configuration Standard                                                                                19

                                                                                                   Applicable
 Control                                                                                              Data
              Control Name                              Control Detail
 Number                                                                                            Protection
                                                                                                 Categorization

            FIPS Certification   All mechanisms used to encrypt data must be FIPS 140-2               Low
                                 compliant and operate using the FIPS 140-2 compliant
    49                           module.                                                           Moderate

                                                                                                     High

            Disk Encryption      Independent logical access controls must be used in addition        High
                                 to operating system and database access controls if disk
    50                           encryption is used (rather than file- or column-level
                                 database encryption). Decryption keys must not be
                                 associated with user accounts.

            Encryption Key       Encryption keys must be protected against disclosure and             Low
            Security             misuse by:
                                                                                                   Moderate
                                    •   Restricting access to cryptographic keys to the
                                        fewest number of individuals necessary.                      High
                                    •   Always securely storing secret and private keys used
                                        to encrypt/decrypt State data in one (or more) of
                                        the following forms:
                                            o Encrypted with a key-encrypting key that is
                                                 at least as strong as the data-encrypting key
    51                                           and that is stored separately from the data-
                                                 encrypting key.
                                            o Within a secure cryptographic device (such
                                                 as a host security module (HSM)).
                                            o As at least two full-length key components
                                                 or key shares, in accordance with an
                                                 industry-accepted method.
                                    •   Storing encryption keys in the fewest possible
                                        locations.
                                    •   Securely distributing encryption keys.

Secure Configuration Standard                                                                                 20

                                                                                                  Applicable
 Control                                                                                             Data
               Control Name                            Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

             Encryption Key      Encryption keys must be:                                            Low
             Management
                                    •   Strong                                                    Moderate
                                            o At least 10 characters long.
                                            o Not a dictionary word.                                High
                                            o At least one (1) upper case letter, one (1)
                                                lower case letter, one (1) number and one
                                                (1) special character.
                                    •   Changed at the end of their cryptoperiod, as
    52                                  recommended by the application vendor or key
                                        owner and based on industry best practices and
                                        guidelines.
                                    •   Retired or replaced when the integrity of the key has
                                        been weakened or keys are suspected of being
                                        compromised.
                                    •   Managed using split knowledge and dual control if
                                        manual clear-text encryption key-management
                                        operations are used.

             Key Substitutions   The substitution of keys coming from unauthorized sources           Low
                                 or unexpected processes must be prevented.
    53                                                                                            Moderate

                                                                                                    High

             Key Custodians      Encryption key custodians must formally acknowledge that            Low
                                 they understand and accept their key-custodian
    54                           responsibilities.                                                Moderate

                                                                                                    High

             Production Data     Production data must not be used in non-production                  Low
             in Non-             environments.
    55       production                                                                           Moderate
             Environments
                                                                                                    High

Roles & Responsibilities
   •     Employees, Vendors, and Contractors

Secure Configuration Standard                                                                                21

            o   Be aware of and follow relevant information security policies, standards, and procedures.
            o   Ensure information security is incorporated into processes and procedures.
            o   Ensure contract language with vendors and contractors includes required information security
                controls.
            o Consult with information security staff on the purchase and procurement of information
                technology systems or services.
            o Contact information security staff or email GRC@state.mn.us with questions about the
                information security policies, standards, or procedures.
    •   Supervisors and Managers
            o Ensure employees and contractors are proficient in the information security policies, standards,
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
            o Notify appropriate personnel of applicable threats, vulnerabilities, and risks to State data or
                systems.
    •   Agency Data Practices Personnel
            o Assist agencies and personnel with questions on proper data use, collection, storage,
                destruction, and disclosure.

Applicability
This policy applies to all departments, agencies, offices, councils, boards, commissions, and other entities in the
executive branch of Minnesota State Government.

Related Information
Information Security and Risk Management Program Policy

Secure Systems Development and Acquisition Policy

Technical Security Policy

Threat and Vulnerability Management Standard

Secure Configuration Standard                                                                                    22

State Standards and Authoritative Source Cross Mapping

Glossary of Information Security Terms

DNS Naming Guideline for Servers

History
Table 2. Version History

    Version                                        Description                                      Date

 1.0               Initial Release                                                              7/8/2015

 1.1               Added Compliance Enforcement Date                                            12/29/2015

 1.2               Updated Compliance Enforcement Date and New Template                         12/20/2016

 1.3               Updated Compliance Enforcement Date and New Template                         10/26/2017

 1.4               Scheduled Document Refresh                                                   3/10/2020

 1.5               Scheduled Document Refresh                                                   11/1/2021

 1.6               Clarified language and expanded scope of some controls to include all data   10/1/2022
                   categories

 1.7               Clarified when software is considered unsupported; included use of CIS       10/1/2023
                   benchmarks if no secure config is available; moved control addressing use
                   of prod data in non-prod environment into this standard from the Secure
                   Systems Development and Acquisition Standard

 1.8               Added enforcement language; removed broken URLs; clarified some              12/2/2024
                   requirements related to IRS; clarified requirements for name resolution;
                   updated version and revision date

 1.9               Replaced outdated MARS-E reference with ARC-AMPE; corrected wording          1/12/2026
                   for secure configurations control.

Secure Configuration Standard                                                                                23

Contact
GRC@state.mn.us

Secure Configuration Standard   24

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
