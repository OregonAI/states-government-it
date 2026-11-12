---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-network-security-standard
title: Network Security Standard
doc_type: standard
citation: MNIT Network Security Standard, Version 1.9
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Network%20Security%20Standard_tcm38-323785.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 459e027d29718140d04d51d12090c9e479a81420edede3aa9a9d537ec318a6fa
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

# Network Security Standard (MNIT Network Security Standard, Version 1.9)

## At a glance

Network security controls (firewalls, segmentation, remote access) that limit access to only the systems and services necessary.

## Full text

Network Security Standard
From the Office of the Chief Information Officer, State of Minnesota

Version: 1.9
Effective Date: 1/1/2016
Revised: 12/31/2024
Approved: John Israel, State of MN Chief Information Security Office         Date: 2/27/2026

Standard Statement
Network security controls must be in place to limit access to only the systems and services necessary.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Table 1. Network Security Controls

                                                                                                    Applicable
 Control                                                                                               Data
              Control Name                                  Control Detail
 Number                                                                                             Protection
                                                                                                  Categorization

             Firewalls           Firewalls must be in place at each Internet connection,                 Low
                                 between wireless networks and networks containing data with
     1                           a data protection categorization of High and between any           Moderate
                                 demilitarized zone (DMZ) and internal network zones.
                                                                                                         High

             Firewall            Firewalls from at least two different vendors must be utilized          High
             Vendors             at the various levels within networks containing systems in
     2
                                 scope for ARC-AMPE to reduce the possibility of compromising
                                 the entire network.

Network Security Standard                                                                                       1

                                                                                                 Applicable
 Control                                                                                            Data
            Control Name                              Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

           Network           All network connections and changes to the firewall and router         Low
           Connection        configurations must be tested, justified, communicated, and
    3      Approval          approved by authorized personnel.                                   Moderate

                                                                                                   High

           Firewall and      Firewall and router rule sets must:                                    Low
           Router Rule
           Sets                  •   Restrict connections between lower trusted networks         Moderate
                                     and systems in higher trusted networks.
                                 •   Restrict inbound and outbound traffic to only that            High
    4                                which is necessary and specifically deny all other
                                     traffic. Configure these firewalls or routers to permit
                                     only traffic necessary for business purposes between
                                     the wireless environment and any systems with a data
                                     protection categorization of High.

           Rule Set Review   Firewall and router rule sets must be reviewed at least               High
    5                        annually. Firewall rules for systems in scope for PCI must be
                             reviewed every six months.

           Unnecessary       Any rules that are no longer needed or justified must be               Low
           Rules             removed.
    6                                                                                            Moderate

                                                                                                   High

           Rule              All services, protocols, and ports used must be documented.         Moderate
           Documentation     Documentation must include:
                                                                                                   High
                                 •   Business justification.
    7                            •   Duration needed.
                                 •   Security features implemented for those protocols
                                     considered to be insecure.
                                 •   Business owner contact information.
                                 •   Technical owner contact information.

Network Security Standard                                                                                   2

                                                                                                  Applicable
 Control                                                                                             Data
            Control Name                             Control Detail
 Number                                                                                           Protection
                                                                                                Categorization

           Router           Router configuration files must be secured and backed up.                Low
           Configuration
    8      Backup                                                                                 Moderate

                                                                                                    High

           DMZ              Inbound Internet traffic must be restricted to a security zone of        Low
                            control that is physically or logically separated from internal
    9                       networks. The zone must only contain systems that are                 Moderate
                            intended and authorized to be publicly accessible.
                                                                                                    High

           Anti-Spoofing    Anti-spoofing measures to detect and block forged source IP              Low
                            addresses from entering the network must be in place
   10                       between the internal network and the Internet.                        Moderate

                                                                                                    High

           Outbound         All outbound Internet traffic must be through a security proxy.         High
   11      Traffic          Outbound traffic must be limited to only that which is
                            authorized and needed for business purposes.

           Stateful         Stateful inspection, also known as dynamic packet filtering,             Low
           Inspection       must be in place between the internal network and the
   12                       Internet.                                                             Moderate

                                                                                                    High

           Network          All systems that store process or transmit State data must be in      Moderate
           Placement        network zones appropriate for their function and their
                            protection requirements. System components that store data              High
                            (such as a database) must be in an internal network zone,
                            segregated from the DMZ and other untrusted networks.
   13                       Key information security tools, mechanisms, and support
                            components associated with system and security
                            administration such as Active Directory Servers, LDAP Servers,
                            DNS Servers, Logging Servers, Patching Servers, etc., must be
                            isolated from other internal information system components
                            via physically or logically separate subnets.

Network Security Standard                                                                                    3

                                                                                                 Applicable
 Control                                                                                            Data
            Control Name                             Control Detail
 Number                                                                                          Protection
                                                                                               Categorization

           Internal IP      Network address translation (NAT) or similar methods of                 Low
           Address          masking internal IP addresses must be implemented between
   14      Disclosure       the internal network and the Internet.                               Moderate

                                                                                                   High

           Wireless         Internal wireless access must be restricted to authorized users         Low
           Security         with a business need. Only devices that are managed by the
                            State shall be allowed to connect to Internal wireless networks.     Moderate

                            Internal wireless networks must:                                       High

                                •   Use the Institute of Electrical and Electronic Engineers
   15                               802.11i wireless security standard.
                                •   Perform mutual authentication via 802.1X and
                                    extensible authentication protocol.
                                •   Have service set identifier broadcasting disabled.
                                •   Shut down access points when not in use (i.e., nights,
                                    weekends).
                                •   Utilize MAC address authentication.
                                •   Utilize static IP addresses not DHCP.

           VoIP Security    For VoIP systems in scope for IRS regulatory requirements:             High

                                •   VoIP traffic must be physically or logically segmented
                                    from other network traffic.
                                •   All VoIP communications involving FTI must be
                                    encrypted in transit using FIPS 140-2 validated
                                    encryption methods.
                                •   VoIP traffic must be filtered using VoIP-ready firewalls
   16                               and inspected for unauthorized access or misuse.
                                    Firewalls must be configured to only allow authorized
                                    traffic between VoIP devices.
                                •   Auditing of VoIP traffic must be enabled to ensure all
                                    access to FTI is logged and reviewed regularly for
                                    unauthorized activity.
                                •   VoIP systems handling FTI must implement access
                                    control mechanisms and ensure proper identification
                                    and authentication of users.

Network Security Standard                                                                                   4

                                                                                                     Applicable
 Control                                                                                                Data
             Control Name                               Control Detail
 Number                                                                                              Protection
                                                                                                   Categorization

             Publicly          Network jacks that are in unsecured areas (accessible to the             Low
             Accessible        public) must be disabled and only turned on when needed,
             Network Jacks     configured to only allow access directly to the Internet, or          Moderate
    17                         configured to only allow approved devices access to the
                                                                                                       High
                               internal network.

                               Any physical ports (e.g., wiring closets and patch panels) not in
                               use must be disabled.

             External File     Access to file sharing services outside of the State of                  Low
             Sharing           Minnesota network will be blocked unless such access is
    18                         approved by management                                                Moderate

                                                                                                       High

Reason for the Standard
Implementing strong network security controls limits the remotely accessible targets for an attacker. Strong
network security also restricts access to sensitive information to only those systems and individuals that have a
business need.

Roles & Responsibilities
    •    Employees, Vendors, and Contractors
             o Be aware of and follow relevant information security policies, standards, and procedures.
             o Ensure information security is incorporated into processes and procedures.
             o Ensure vendors and contractors are following required information security controls.
             o Contact information security staff or email GRC@state.mn.us with questions about the
                 information security policies, standards, or procedures.
    •    Supervisors and Managers
             o Ensure employees and contractors are proficient in the information security policies, standards,
                 and procedures that are relevant to their role.
             o Hold employees accountable for following the information security policies, standards, and
                 procedures.
    •    Information Technology Personnel
             o Apply appropriate controls to the design, operation and maintenance of systems, processes, and
                 procedures in conformance with the information security policies, standards, and procedures.
    •    Information Security Personnel

Network Security Standard                                                                                           5

              oDevelop, maintain, and assess compliance with the information security policies, standards, and
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
Enterprise Technical Security Policy

State Standards and Authoritative Source Cross Mapping

Glossary of Information Security Terms

History
Table 2. Version History

    Version                                        Description                                         Date

 1.0               Initial Release                                                                7/8/2015

 1.1               Added Compliance Enforcement Date                                              12/29/2015

 1.2               Updated Compliance Enforcement Date and Template                               12/20/2016

 1.3               Updated Compliance Enforcement Date and Template                               10/26/2017

 1.4               Changed title of document. Edited for clarity and to include additional        3/10/2020
                   MARS-E requirements

Network Security Standard                                                                                           6

   Version                                    Description                                      Date

 1.5            Scheduled Document Refresh                                                 11/1/2021

 1.6            Scheduled document refresh                                                 10/1/2022

 1.7            Updated version number and revision date                                   10/1/2023

 1.8            Added enforcement language; clarified VoIP requirements; updated version   12/2/2024
                and revision date

 1.9            Replaced outdated MARS-E reference with ARC-AMPE                           1/12/2026

Contact
GRC@state.mn.us

Network Security Standard                                                                              7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
