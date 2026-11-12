---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-scio-sec-305
title: Configuration Management Policy (CM)
doc_type: policy
citation: SCIO-SEC-305
authority_level: ''
issuing_body: North Carolina Department of Information Technology
source_url: https://it.nc.gov/documents/statewide-policies/scio-configuration-management/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: efd1572836e40f6d41d4c91c38314f7c0cefca1825644fb70646d4ef5026bd2c
effective_date: '2018-01-29'
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

# Configuration Management Policy (CM) (SCIO-SEC-305)

## At a glance

One of the 18 Statewide Information Security Policies (SCIO-SEC-305), each aligned to a NIST SP 800-53 Rev. 5 control family and binding executive branch agencies under G.S. 143B-1376.

## Full text

                                                                                              Document No.
                                   Configuration                                              SCIO-SEC-305

                                 Management Policy

Effective Date                      Review Date                                Version        Page No.
01/29/2018                          03/26/2025                                 4              1 of 15

Scope
  The Statewide Information Security Policies are the foundation for information technology security in
  North Carolina. The policies set out the statewide information security standards required by N.C.G.S.
  §143B-1376, which directs the State Chief Information Officer (State CIO) to establish a statewide set
  of standards for information technology security to maximize the functionality, security, and
  interoperability of the State’s distributed information technology assets, including, but not limited to,
  data classification and management, communications, and encryption technologies. This policy covers
  all State information and information systems to include those used, managed, or operated by a
  contractor, an agency, or other organization on behalf of the State. This policy applies to all State
  employees, contractors, and all other users of State information and information systems that support
  the operation and assets of the State. Use by local governments, local education agencies (LEAs),
  community colleges, constituent institutions of the University of North Carolina (UNC) and other
  executive branch agencies is encouraged to the extent allowed by law. This security policy is consistent
  with applicable laws, executive orders, directives, regulations, and other policies, standards, and
  guidelines.

Material Superseded
  This current policy supersedes all previous versions of the policy. All State agencies and vendors of the
  State are expected to comply with the current implemented version of this policy.

Responsibilities
  All covered personnel who utilize State of NC IT resources are responsible for adhering to this policy
  and any local Configuration Management requirements.
   Role               Definition
   Agency             The Agency Head, the Chief Information Officer (CIO), the Chief Information Security Officer
   Management         (CISO), or other designated organizational officials at the senior leadership level are
                      assigned the responsibility for the continued development, dissemination, implementation,
                      operation and monitoring of the Configuration Management program. Ensures that
                      personnel with significant responsibilities for configuration management are trained.
   Agency             The Agency Security Liaison is responsible for ensuring that security risks are managed in
   Security Liaison   compliance with the State’s requirements by collaborating with organizational entities.
                      Liaisons are responsible for ensuring the appropriate configuration management controls
                      are in effect for agency information systems.

                                                                                       Document No.
                              Configuration                                            SCIO-SEC-305

                            Management Policy
Effective Date                    Review Date                              Version     Page No.
01/29/2018                        03/26/2025                               4           2 of 15

   Information      The information system owner is the individual responsible for the overall procurement,
   System Owner     development, integration, modification, or operation and maintenance of
                    the information system. Develops and maintains configuration management for the
                    information system in coordination with information owners, the system administrator, the
                    information system security officer, and functional “end users.”
   Information      The information owner is the individual with operational responsibility and authority for
   Owner            specified information and responsibility for establishing the controls for its generation,
                    collection, processing, dissemination, and disposal. Provides input to information system
                    owners regarding security requirements and security controls for the information system(s)
                    where the information resides. Decides who has access to the information system and with
                    what types of privileges or access rights.
   Covered          Covered personnel must provide Configuration Management capabilities that meet agency
   Personnel        requirements. Configuration Management practices are subject to periodic review by the
                    agencies.

CM-1 – Policy and Procedures
  All information assets that process, store, receive, transmit or otherwise could impact the
  confidentiality, integrity, and accessibility of State data must meet the required security controls
  defined in this policy document that are based on the National Institute of Standards and Technology
  (NIST) SP 800-53, Security and Privacy Controls. This document addresses the requirements set forth
  by the State to implement the family of Configuration Management security controls at the
  organization, process and/or system level for all information assets / State data. This document
  provides requirements for the configuration management process which is required to assure that
  information systems are designed and configured using controls sufficient to safeguard the State’s
  information systems.

  The State has adopted the Configuration Management security principles established in NIST SP 800-
  53, “Configuration Management” control guidelines as the official policy for this security domain. The
  “CM” designator identified in each control represents the NIST-specified identifier for the
  Configuration Management control family. The following subsections in this document outline the
  Configuration Management requirements that each agency must implement and maintain in order to
  be compliant with this policy. This policy and associated procedures shall be reviewed and updated
  annually, at a minimum. They shall also be updated following agency-defined events that necessitate
  such change.

  This policy and the associated procedures shall be developed, documented, and disseminated by the
  Agency Head, the Chief Information Officer (CIO), the Chief Information Security Officer (CISO), or
  other designated organizational officials at the senior leadership level.

                                                                                           Document No.
                                   Configuration                                           SCIO-SEC-305

                                 Management Policy
Effective Date                         Review Date                             Version     Page No.
01/29/2018                             03/26/2025                              4           3 of 15

CM-2 – Baseline Configuration
      Common security configurations shall be made available that provide a baseline level of security,
      reduce risk from security threats and vulnerabilities, and save time and resources. This requirement
      allows agencies to improve information system performance, decrease operating costs, and ensure
      public confidence in the confidentiality, integrity, and availability of State data. The following shall be
      done:
      a. A current baseline configuration must be developed, reviewed, approved, documented, and
         maintained under configuration control for each information system. The Department of
         Information Technology (DIT) shall be responsible for baseline configurations for enterprise
         solutions.
      b. A baseline configuration must document and provide information about the components of
         an information system including the following:
          i.   Standard operating system/installed applications with current version numbers
          ii. Standard software load for workstations, servers, network components, and mobile devices
              and laptops
          iii. Up-to-date patch level information
          iv. Network topology
          v. Logical placement of the component within the system and enterprise architecture
          vi. Technology platform
      c. New baselines must be created as the information system changes over time to maintain
         the baseline configuration.
      d. Ensure product versions of technologies are kept up to date and the latest security patches
         are applied.
         Agencies will ensure “best effort” to maintain all information technologies within N-1, where
         “N” is a major version. At minimum all operating systems and primary applications shall be
         maintained at baseline security configurations of no less than N-2. All current security patches
         for information technologies shall be applied prior to deployment and shall be maintained as
         meets or exceeds the SI-2 Flaw Remediation control. Whereas, “best effort” means taking, in
         good faith, all reasonable steps to achieve the objective, carrying the process to its logical
         conclusion and leaving no stone unturned.
      e. Utilize best practice system hardening baselines for the operating systems. Refer to CM-6
         Configuration Settings for a list of approved baselines.
 i.       In cases where a baseline security configuration does not exist for an operating system, the State
          Chief Information Security Officer (SCISO) or designee shall ensure a baseline security
          configuration is developed, documented, and approved.

                                                                                    Document No.
                               Configuration                                        SCIO-SEC-305

                             Management Policy
Effective Date                     Review Date                          Version     Page No.
01/29/2018                         03/26/2025                           4           4 of 15

  f.   Document any exceptions to baseline security configurations and obtain approval by the SCRO or
       designee.
  g. Maintain records confirming the implementation of baseline security configurations for each IT
     system they manage.
  h. Review and update the baseline configuration for information systems:
       i.   Annually, at a minimum
       ii. When required due to system upgrades, patches, or other significant changes have
           occurred in the baseline configuration
       iii. As an integral part of information system component installations and upgrades
       iv. When an increase in interconnection with other systems outside the authorization
            boundary or significant changes in the security requirements for the system

CM-2 (2) Baseline Configuration |Automation Support for Accuracy and
Currency
  The currency, completeness, accuracy, and availability of the baseline configuration of the system shall
  be maintained using automated mechanisms such as the following:
  a. Backup of individual configuration files, or similar method that allows for only the restore of the
     configuration
  b. Snapshot systems or applications that may also allow for reviewing differences or compliance
  c. Version control applications that are operated on a system separate from those being versioned

CM-2 (3) – Baseline Configuration |Retention of Previous Configurations
  Retain previous versions of baseline configurations of the information system to support rollback, for
  example, hardware, software, firmware, configuration files, and configuration records.

CM-2 (7) Baseline Configuration | Configure Systems and Components for
High-Risk Areas
  All devices taken to high-risk areas external to the organization should be considered compromised
  upon return from those areas. They could contain malicious software that you do not want to
  introduce to the State’s network or to your home network. Systems and components used for high-risk
  areas shall be configured as follows:

                                                                                    Document No.
                              Configuration                                         SCIO-SEC-305

                            Management Policy
Effective Date                    Review Date                            Version    Page No.
01/29/2018                        03/26/2025                             4          5 of 15

  a. Issue organizational defined selected systems with defined configurations to individuals traveling
     to locations that the organization deems to be of significant risk. Refer to the International Travel
     Policy.
  b. Have laptops, cellphones, and portable devices sanitized prior to travel.
  c. Have devices that will be in high-risk areas securely erased and rebuilt, either from an existing
     backup or through a new installation of the operating system.

CM-3 – Configuration Change Control
  Changes to systems and application programs shall be managed to protect the systems and programs
  from failure as well as security breaches. Adequate management of system change control processes
  shall require the following:
  a. Safeguard production systems during modification, including emergency changes.
  b. Enforcement of formal change control procedures.
  c. Proper authorization and approvals at all levels.
  d. Successful testing of updates and new programs prior to their being moved into a production
     environment.
  e. Determine and document the types of changes to the information system that are configuration
     controlled.
  f.   Review proposed configuration-controlled changes to the information system and approve or
       disapprove such changes with explicit consideration for security and privacy impact analyses.
  g. Document configuration change decisions associated with the information system.
  h. Implement approved configuration-controlled changes to the information system.
  i.   Retain records of configuration-controlled changes to the information system for the life of the
       system.
  j.   Monitor and review activities associated with configuration-controlled changes to the
       information system.
  k. Coordinate and provide oversight for configuration change control activities through a
     Configuration Control Board that convenes when configuration changes occur.
  l.   Test, validate, and document changes to the information system before implementing the
       changes on the system.
  m. Ensure updates addressing significant security vulnerabilities are prioritized, evaluated, tested,
     documented, approved, and applied promptly to minimize the exposure of unpatched resources.

                                                                                     Document No.
                                Configuration                                        SCIO-SEC-305

                              Management Policy
Effective Date                     Review Date                            Version    Page No.
01/29/2018                         03/26/2025                             4          6 of 15

       Vulnerability Management requirements are addressed in the System and Information Integrity
       Policy SCIO-SEC-317, Section SI-2.
  n. Integrate application change control and operational change control procedures. This effort
     should include the following processes, controls, and best practices:
       i    Controls and approval levels for updating libraries
       ii   Requiring formal agreement and approval for any changes
       iii Restricting library content
       iv Restricting programmers’ access to only those parts of the system necessary for their work
       v    Version control for each application.
       vi Tying program documentation updates to source code updates
       vii Audit logs that track all accesses to libraries, copying and use of source code, and updates
           posted to libraries
  o. Define job responsibilities/restrictions and establishing authority levels for the following:
       i.   Program librarian(s)
       ii. Developers (i.e., should neither test their own code nor promote it into production)
       iii. Other IT staff
  p. Identify personnel authorized to make or submit changes to the source library (i.e., a program
     librarian) for each major application to control check-in/check-out.
  q. Provide role-based training for business and technical users covering new features and security
     controls introduced by the upgrade.
  r.   Use rollback procedures designed to recover to previous stable version of programs.

CM-3 (4) – Configuration Change Control | Security and Privacy
Representatives
  Organizational defined security and privacy representatives shall be members of the Configuration
  Control Board.

CM-4 –Impact Analyses
  When significant changes are planned for, or made to, a system, the system owners, agency security
  liaison or business owners for systems shall conduct impact analyses to determine which security and
  privacy controls shall be assessed for proper implementation and operation. An impact analysis may

                                                                                     Document No.
                              Configuration                                          SCIO-SEC-305

                            Management Policy
Effective Date                    Review Date                             Version    Page No.
01/29/2018                        03/26/2025                              4          7 of 15

  include, for example, reviewing plans to understand security and privacy control requirements and
  reviewing system design documentation to understand control implementation and how specific
  changes might affect the controls. The following risk impact analyses activities shall be incorporated
  into the documented configuration change control process:
  a. Identification of the Federal, State, and Local regulatory or legal requirements that address the
     security, confidentiality, and privacy requirements for agency functions or services.
  b. Identification of Restricted or Highly Restricted information, which are stored in the agency’s files,
     and the potential for fraud, misuse, or other illegal activity. Data classifications are defined within
     the Statewide Data Classification and Handling policy.
  c. Identification of essential access control mechanisms used for requests, authorization, and access
     approval in support of critical agency functions and services.
  d. Identification of the processes used to monitor and report to management on whatever
     applications, tools, and technologies the agency has implemented to adequately manage the risk
     as defined by the agency (i.e., baseline security reviews, review of logs, use of IDs, logging events
     for forensics, etc.).
  e. Identification of the agency’s IT Change Management and Vulnerability Assessment
     processes.
  f.   Identification of the security and privacy mechanisms that are in place to conceal agency
       data, for example the use of encryption, data masking, etc.
  g. Changes shall be analyzed and evaluated for the impact on security and privacy preferably before
     they are approved and implemented.
  h. Security and Privacy risk analysis requirements and definitions are addressed in the Risk
     Assessment Policy SCIO-SEC-314, Section RA-3.

CM-4 (2) Impact Analyses | Verification of Controls
  Organizations shall verify (after system changes) that the impacted controls are implemented
  correctly, operating as intended, and producing the desired outcome with regard to meeting the
  security and privacy requirements for the system.

CM-5 – Access Restrictions for Change
  Physical and logical access restrictions associated with changes to the information system shall be
  defined, documented, approved, and enforced. The following shall be done:
  a. Only qualified and authorized individuals are allowed to obtain access to information system
     components for purposes of initiating changes, including upgrades and modifications.

                                                                                    Document No.
                              Configuration                                         SCIO-SEC-305

                            Management Policy
Effective Date                    Review Date                           Version     Page No.
01/29/2018                        03/26/2025                            4           8 of 15

  b. All requests for local administrative rights must be documented and approved by agency
     management.
  c. Access records must be maintained to ensure that configuration change control is being
     implemented as intended and for supporting after-the-fact actions should the State become aware
     of an unauthorized change to an information system.
  d. Privileges to change information system components and system-related information within a
     production or operational environment shall be limited to avoid unintended changes to other
     systems and business processed.
  e. Use two-person integrity to ensure that changes to defined critical systems cannot occur unless
     both individuals implement such changes.
  f.   Restrict access to operating system and operational or production application software/program
       libraries to designated staff only.

CM-6 – Configuration Settings
  Configuration settings are the set of parameters that can be changed in hardware, software, or
  firmware components of the information system that affect the security posture and/or
  functionality of the system. Security-related configuration settings can be defined include, for
  example, mainframe computers, servers (e.g., database, electronic mail, authentication, web,
  proxy, file, domain name), workstations, input/output devices (e.g., scanners, copiers, and printers),
  network components (e.g., firewalls, routers, gateways, voice and data switches, wireless access
  points, network appliances, sensors), operating systems, middleware, and applications. The
  following requirements shall be implemented:
  a. A standard set of mandatory configuration settings must be established and documented for
     information technology components employed within the information system. Standard
     Configuration Documents (SCDs) must detail the configuration settings.
  b. The selected configuration settings, whether State standards or designed specifically for the
     information system, must reflect the most restrictive mode consistent with operational
     requirements and must be derived from the following sources, listed in order of precedence:
       i.   NIST recommended configurations and common secure configurations:
            https://ncp.nist.gov/repository
       ii. Defense Information Systems Agency (DISA) common secure configurations and Standard
           Technical Implementation Guides (STIGs): https://public.cyber.mil/stigs/downloads/
       iii. National Security Agency (NSA) configuration guides:
            https://apps.nsa.gov/iaarchive/library/ia-guidance/security-configuration/index.cfm

                                                                                    Document No.
                                Configuration                                       SCIO-SEC-305

                              Management Policy
Effective Date                     Review Date                          Version     Page No.
01/29/2018                         03/26/2025                           4           9 of 15

      iv. Center for Internet Security (CIS) benchmarks: https://www.cisecurity.org/cis-
          benchmarks/
      v. Safeguard Computer Security Evaluation Matrix (SCSEM):
         https://www.irs.gov/privacy-disclosure/computer-security-compliance-references-
         and-related-topics, for systems that store, process, or transmit federal tax
         information (FTI).
  c. Identify, document, and approve any deviations from established configuration settings for
     information systems.
  d. Monitor and control changes to the configuration settings in accordance with organizational
     policies and procedures.

CM-7 – Least Functionality
  The following requirements shall be implemented to provide least functionality:
  a. Configure information systems to provide only essential capabilities and specifically prohibit or
     restrict the use of functions, ports, protocols, and/or services that are not required for the
     business function of the information system.
  b. Where technically configurable, component functionality shall be limited to a single function per
     device (e.g., email server, web server, etc.).
  c. Disable any functions, ports, protocols, and services within an information system that are deemed
     to be unnecessary and/or non-secure. Organizations can either decide the relative security of a
     function, port, protocol, and/or service or base a security decision on the assessment of other
     entities. The use of the following functions, ports, protocols, software and/or services, at a
     minimum, must be specifically prohibited or restricted:
      i.         ARINC-GATEWAY Port 55210 / TCP
      ii.        Background File Transfer Protocol (BFTP) Port 152 / TCP
      iii.       Border Gateway Protocol (BGP) Port 179 / Transmission Control Protocol (TCP)
      iv.        Courier Port 530 / TCP, User Datagram Protocol (UDP)
      v.         Domain Name System be (DNS) Port 53 / TCP, UDP
      vi.        File Transfer Protocol (FTP) Ports 20, 21 / TCP
      vii.       Finger Port 79 / TCP
      viii.      Hypertext Transfer Protocol (HTTP) Port 80 / TCP; 443 / TCP
      ix.        HTTP-MGMT Port 280 / TCP
      x.         Identification Protocol (IDENT) Port 113 / TCP, UDP
      xi.        Internet Control Messaging Protocol (ICMP) - block incoming echo request (ping and
                 Windows traceroute) block outgoing echo replies, time exceeded, and destination

                                                                                 Document No.
                             Configuration                                       SCIO-SEC-305

                           Management Policy
Effective Date                  Review Date                           Version    Page No.
01/29/2018                      03/26/2025                            4          10 of 15

               unreachable messages except “packet too big” messages (type 3, code 4). Note: Blocking
               ICMP will restrict legitimate use of PING to restrict malicious activity.
      xii.     Internet Message Access Protocol (IMAP) Port 143 / TCP, UDP
      xiii.    Internet Relay Chat (IRC) Port 194 / UDP
      xiv.     Lightweight Directory Access Protocol (LDAP) Port 389 / TCP, UDP
      xv.      Line Printer Daemon (LPD) Port 515 / TCP
      xvi.     LOCKD Port 4045 / TCP, UDP
      xvii.    Network Basic Input Output System (NetBIOS) Ports 135, 445 / TCP, UDP; 137-138 / UDP;
               139 / TCP
      xviii. Network File System (NFS) Port 2049 / TCP, UDP
      xix.     Network News Transfer Protocol (NNTP) Port 119 / TCP
      xx.      Network Time Protocol (NTP) Port 123 / TCP
      xxi.     Oracle Names (ORACLENAMES) Port 1575 / TCP, UDP
      xxii.    Port Mapper (PORTMAP/RPCBIND) Port 111 / TCP, UDP
      xxiii. Post Office Protocol 3 (POP3) Ports 109-110 / TCP
      xxiv. r Services Ports 512-514 / TCP
      xxv.     Secure Shell (SSH) Port 22 / TCP
      xxvi. Session Initiation Protocol (SIP) Port 5060 / TCP, UDP
      xxvii. Shell Port 514 / TCP
      xxviii. SIDEWINDER-COBRA, (S) Port 2809 & 9002 / TCP
      xxix. Simple File Transfer Protocol (SFTP) Port 115 TCP, UDP
      xxx.     Simple Mail Transfer Protocol (SMTP) Port 25 / TCP
      xxxi. Simple Network Management Protocol (SNMP) Ports 161-162 / TCP, UDP
      xxxii. Snare Port 509 / TCP, UDP
      xxxiii. Socket Secure (SOCKS) Port 1080 / TCP
      xxxiv. SOFTWAREAGWEBMETHODS Port 6849 / TCP
      xxxv. Structured Query Language (SQL) Port 118 / TCP, UDP; Port 156 / TCP, UDP
      xxxvi. Super Duper Telnet Port 95 / TCP
      xxxvii. SYMANTEC-ITA Port 3833-3836 / TCP
      xxxviii. Syslog Port 514 / UDP
      xxxix. Telnet Port 23 / TCP
      xl.      TIME Port 37 / TCP, UDP
      xli.     TIMBUKTU Port 407 / TCP, UDP
      xlii.    Trivial File Transfer Protocol (TFTP) Port 69 / UDP

                                                                                  Document No.
                               Configuration                                      SCIO-SEC-305

                             Management Policy
Effective Date                    Review Date                         Version     Page No.
01/29/2018                        03/26/2025                          4           11 of 15

      xliii.     VNC-SERVER Port 5900 / TCP
      xliv.      X Windows Ports 6000-6255 / TCP
      xlv.       YAK-CHAT Port 258 / UDP

CM-7 (1) – Least Functionality | Periodic Review
  The following shall be done:
  a. Review the system on a defined frequency to identify unnecessary and/or non-secure functions,
     ports, protocols, services, and applications; and,
  b. Disable or remove unnecessary and/or non-secure functions, ports, protocols, services, and
     software.

CM-7 (2) - Least Functionality | Prevent Program Execution
  An information system shall prevent program execution in accordance with organizational-defined
  policies regarding software program usage and restrictions, and/or rules authorizing the terms and
  conditions of software program usage.
  This control is optional for LOW risk systems.

CM-7 (5) – Least Functionality | Authorized Software
  The following shall be done:
  a. Identify organizational-defined software programs authorized to execute on the system.
  b. Review and update the list of authorized software programs per an agency-defined frequency.
  c. Where technically configurable, employ a deny-all, permit-by-exception policy for software
     executables on systems with Restricted or Highly Restricted data.
  d. This control is optional for LOW risk systems.

CM-8 – System Component Inventory
  The following shall be done:
  a. Develop, document, and maintain an inventory of information system components that accurately
     reflects the current information system environment.

                                                                                     Document No.
                              Configuration                                          SCIO-SEC-305

                            Management Policy
Effective Date                    Review Date                            Version     Page No.
01/29/2018                        03/26/2025                             4           12 of 15

  b. Verify that all components within the system are not duplicated in other information system
     component inventories.
      Inventory all components within the authorization boundary of the information system (this may
      inter-connected systems). The inventory includes information deemed necessary to achieve
      effective property accountability and is at the level of granularity for tracking and reporting, for
      example, the following:
      i.   hardware inventory specifications (manufacturer, type, model, serial number, physical
           location),
      ii. software license information,
      iii. information system / component owner(s),
      iv. associated component configuration standard,
      v. software/firmware version information, and
      vi. for a networked component/device, the machine name and network address,
  c. Review and audit information system component inventory,
  d. Include assessed component configurations and any approved deviations to current deployed
     configurations in the information system component inventory,
  e. Review and update the information system component inventory annually, at a minimum.

CM-8 (1) – System Component Inventory | Updates during Installation
and Removal
  The inventory of information system components shall be updated as an integral part of component
  installations, removals, and information system updates.

CM-8 (3) –System Component Inventory | Automated Unauthorized
Component Detection
  Automated mechanisms shall be defined and employed to detect the presence of unauthorized
  hardware, software, and firmware components within the information system. One or more of the
  following actions may be taken when unauthorized components are detected:
      i. Disable network access to such components
      ii. Isolate the components
      iii. Notify agency-defined personnel

                                                                                   Document No.
                              Configuration                                        SCIO-SEC-305

                            Management Policy
Effective Date                    Review Date                           Version    Page No.
01/29/2018                        03/26/2025                            4          13 of 15

  This control enhancement is applied in addition to the monitoring for unauthorized remote
  connections and mobile devices. Monitoring for unauthorized system components may be
  accomplished on an ongoing basis or by the periodic scanning of systems for that purpose. Automated
  mechanisms can be implemented within information systems or in other separate devices.

CM-9 – Configuration Management Plan
  A configuration management plan shall be developed, documented, and implemented for information
  systems that does the following:
  a. Addresses roles, responsibilities, and configuration management processes and procedures,
  b. Defines the configuration items for the information system and when in the system development
     life cycle (SDLC) the configuration items are placed under configuration management,
  c. Establishes the means for identifying configuration items throughout the SDLC and a process for
     managing the configuration of the configuration items,
  d. Assigns responsibility for developing the configuration management process to organizational
     personnel that are not directly involved in system development. In the absence of a dedicated
     configuration management team, the system integrator may be tasked with developing the
     configuration management process,
  e. Defines detailed processes and procedures for how configuration management is used to support
     SDLC activities at the information system level,
  f.   Describes how to move a change through the change management process, how configuration
       settings and configuration baselines are updated, how the information system component
       inventory is maintained, how development, test, and operational environments are controlled, and
       finally, how documents are developed, released, and updated,
  g. Creates a step-by-step implementation plan for every configuration change,
  h. Requires that software implementation plans follow change control procedures,
  i.   Protects the configuration management plan from unauthorized disclosure and modification,
  j.   The configuration management plan approval process must include the following:
       i.   Designation of key management stakeholders who are responsible for reviewing and
            approving proposed changes to the information system
       ii. Designation of security personnel that would conduct an impact analysis prior to the
           implementation of any changes to the system

                                                                                     Document No.
                               Configuration                                         SCIO-SEC-305

                             Management Policy
Effective Date                     Review Date                             Version   Page No.
01/29/2018                         03/26/2025                              4         14 of 15

CM-10 – Software Usage Restrictions
   The following shall be done:
  a. Provide employees, contractors and other third parties with guidelines for obeying software
     licensing agreements, to include open source software, and shall not permit the installation of
     unauthorized copies of software on technology devices that connect to the State Network.
      i.   Persons involved in the illegal reproduction of software can be subject to civil damages and
           criminal penalties.
      ii. Employees, contractors and other third parties shall use software and associated
          documentation in accordance with contract agreements and copyright laws.
      iii. Employees, contractors and other third parties who make, acquire, or use unauthorized
           copies of software shall be disciplined as appropriate. Such discipline may include
           termination.
      iv. Open source software must adhere to a secure configuration baseline checklist from the U.S.
          Government or industry.
  b. Inform their users of any proprietary rights in databases or similar compilations and the appropriate
     use of such data.
  c. Control and document the use of peer-to-peer file sharing technology to ensure that this capability is
     not used for the unauthorized distribution, display, performance, or reproduction of copyrighted work.
  d. Establish procedures for software use, distribution, and removal within an organization to ensure
     organizational use of software meets all copyright and licensing requirements. Procedures shall include
     the development of internal controls to monitor the number of licenses available and the number of
     copies in use.

CM-11 – User Installed Software
  Only standard approved software shall be installed on State owned assets with any deviations being
  pre-approved by agency management and reviewed by an agency security liaison assigned to perform
  the review. The following shall be ensured for installed software:
  a. Establish policies governing the installation of software by users.
  b. Enforce software installation policies through automated methods, if available and technically
     configurable.
  c. Monitor policy compliance quarterly, at a minimum.
  d. Ensure only software programs that are from validated media are installed and are free of harmful
     code or other destructive aspects.

                                                                                       Document No.
                               Configuration                                           SCIO-SEC-305

                             Management Policy
Effective Date                     Review Date                             Version     Page No.
01/29/2018                         03/26/2025                              4           15 of 15

  e. Refer to the Statewide Acceptable Use Policy (AUP) for additional requirements.

CM-12 – Information Location
  The following shall be done:
  a. Identify and document the location of “organizational-defined information” and the specific
     system components on which the information is processed and stored.
  b. Identify and document the users who have access to the system and system components where
     the information is processed and stored.
  c. Document changes to the location (i.e., system or system components) where the information is
     processed and stored.

CM-12 (1) – Information Location |Automated Tools to Support
Information Location
  Where technically configurable, automated tools shall be used to identify organizational-defined
  information by information type on system components to ensure controls are in place to protect
  organizational information and individual privacy.

Enforcement
  Violations of this policy or failure to implement provisions of this policy may result in disciplinary
  action up to and including termination, civil litigation, and/or criminal prosecution.

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
