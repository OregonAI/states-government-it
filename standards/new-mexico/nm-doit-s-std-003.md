---
schema_version: 1
corpus: states-government-it
jurisdiction: new-mexico
id: nm-doit-s-std-003
title: IT Risk Management Standard
doc_type: standard
citation: S-STD-003
authority_level: ''
issuing_body: Department of Information Technology (Architectural Configuration Requirements, 1.12.6 NMAC)
source_url: https://www.doit.nm.gov/files/docs/S-STD-003.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: eb78628d88d403bc983f934c2e140c5c2d30c96ab3f1a17ce3d32d931408f3c4
effective_date: '2005-04-07'
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
- oversight
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# IT Risk Management Standard (S-STD-003)

## At a glance

Statewide architectural configuration requirement of the Department of Information Technology (the page's ACR table): IT Risk Management Standard. The file prints its own effective date; it is one of the DoIT standards, guidelines and policies issued under the Department of Information Technology Act and 1.12.6 NMAC.

## Full text

                           State of New Mexico Statewide
                      Architectural Configuration Requirements
                        Title: IT Risk Management Standard
                                     S-STD003.001
                             Effective Date: April 7, 2005

     1.       Authority
              The Department of Information Technology (DoIT) shall develop, implement and
              maintain a coordinated statewide plan for information technology (IT) including the
              adoption of statewide technical, coordination, and security standards per the
              Department of Information Technology Act, NMSA 9-27-1 et. seq. (1978).

     2.       Purpose
              The purpose of this standard is to identify and establish a web-based Technology
              Infrastructure and Security Assessment application as the statewide vehicle for
              reporting compliance to statewide IT standards and security risks/vulnerabilities
              associated with IT infrastructure and security technologies for major budget units.

     3.       Scope
              This applies to all Agencies. Agency is defined as a department, commission, board,
              institution or other agency of the state organization receiving, expending or disbursing
              state funds or incurring obligations of the state including the board of regents and the
              state board of directors for community colleges but excluding the universities under the
              jurisdiction of the board of regents and the community colleges under their respective
              jurisdictions and the legislative or judicial branches.

              The Department Secretary, working in conjunction with the Department Chief
              Information Officer, shall be responsible for ensuring the effective
              implementation of Statewide Information Technology Policies, Standards, and
              Procedures (PSPs) within each agency.

       4. Standard
              4.1      Each agency shall perform risk assessments, at least annually as described in
                       4.2, for information technology (IT) systems and their environments to
                       determine security vulnerabilities. Security vulnerabilities are more heavily
                       weighted toward the impact of the loss on agency operations, agency assets, or
                       individuals than on the threat of loss.

              4.2      Each agency shall submit an annual IT Security Assessment to DoIT (see
                       Attachment A). The assessment indicates the effectiveness of security
                       controls within the agency for categories of risks derived from Federal IT

Title: IT Risk Management Standard S-STD-003.001
Approval Date: April 7, 2005                                                                Security Domain Team
                                                                                                      Page 1 of 26

                       Security guidelines. Categories of risks may change periodically; the
                       following are representative categories:

                                1.       IT Security
                                2.       IT Risk Management
                                3.       Account Management
                                4.       Configuration Management
                                5.       Authentication and Directory Services
                                6.       Session Controls
                                7.       Network Security
                                8.       Encryption Technologies
                                9.       System Administration
                                10.      Incident Response and Reporting
                                11.      Virus and Malicious Code Protection
                                12.      Business Continuity & Disaster Recovery
                                13.      Backups
                                14.      Maintenance
                                15.      Media Sanitizing/Disposal
                                16.      IT Physical Security
                                17.      Personnel Security
                                18.      Security Training & Awareness
                                19.      Application Software
                                20.      Productivity Software Tools
                                21.      Classification of Data
                                22.      Database Access

                       4.2.1    Each category contains risk statements for which the agency shall select
                                the appropriate check box of “Yes,” “No,” “To Some Extent (TSE),” or
                                “N/A” to indicate the applicable level of effectiveness currently in place
                                (from Policy to Procedure, through Implemented, to tested, and finally
                                 integrated). Each risk statement allows for comments to further explain
                                 the position of the agency.
                       4.2.2    Where a particular risk statement does not apply to an agency, the “N/A”
                                box shall be checked for “Not Applicable.”
                       4.2.4    Agency IT plans shall address vulnerabilities identified in IT Security
                                Assessment.

     5.       Definitions
              Refer to the N-DEF001.001 Glossary of Terms located on the DoIT website:
              http://www.doit.state.nm.us/standards.html

     6.       References
              None

Title: IT Risk Management Standard S-STD-003.001
Approval Date: April 7, 2005                                                                  Security Domain Team
                                                                                                        Page 2 of 26

     7.       Attachments
              Attachment A - Technical IT Security Assessment Sample

     8.       Version Control
              S-STD-003.001

     9.       Revision History
              Original 04/07/05
              Format Updated 09/18/13

Title: IT Risk Management Standard S-STD-003.001
Approval Date: April 7, 2005                                           Security Domain Team
                                                                                 Page 3 of 26

ATTACHMENT A – IT Security Assessment                 SAMPLE

                                                 State of New Mexico IT Security Assessment
                                                                (On Critical Information Assets)

      Agency:                                                          Date:

      Contact Name:                                                    Phone:

      Email:                                                           Fax:

  Control                                            Policy   Procedure     Implemented       Tested   Integrated   Comments*
1. IT SECURITY
A. Security protections in place are commensurate
with the risk and magnitude of harm resulting
from unauthorized access, use, disclosure,           Yes      Yes             Yes              Yes     Yes
modification to, or destruction of agency            No       No              No               No      No
information or information systems, or that a        TSEo     TSE             TSE              TSE     TSE
contractor or other organization uses on behalf of   N/A      N/A             N/A              N/A     N/A
agency.

   Control                                             Policy   Procedure   Implemented   Tested   Integrated        Comments*
B. Data/information contained in electronic
transactions is protected via 1) identification,       Yes      Yes         Yes           Yes      Yes
authentication, and authorization; 2) encryption, as   No       No          No            No       No
necessary; and 3) electronic signature, as             TSE      TSE         TSE           TSE      TSE
necessary.                                             N/A      N/A         N/A           N/A      N/A

C. All information collected, processed,               Yes      Yes         Yes           Yes      Yes
transmitted, stored, or disseminated in software       No       No          No            No       No
application systems is adequately secured.             TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A
D. Networks, hardware systems, and software
application systems use cost-effective management,     Yes      Yes         Yes           Yes      Yes
personnel, operational, and technical controls to      No       No          No            No       No
provide appropriate confidentiality, integrity, and    TSE      TSE         TSE           TSE      TSE
availability.
                                                       N/A      N/A         N/A           N/A      N/A

E. Sufficient security controls are applied to
information systems, resources, and data/              Yes      Yes         Yes           Yes      Yes
information to contain risk of loss or misuse of the   No       No          No            No       No
information to an acceptable level that sup-ports      TSE      TSE         TSE           TSE      TSE
the mission and operation of the agency.
                                                       N/A      N/A         N/A           N/A      N/A

F. Information security management processes are
integrated with agency strategic and operational       Yes      Yes         Yes           Yes      Yes
planning processes, including planning and             No       No          No            No       No
implementing any necessary remedial action to          TSE      TSE         TSE           TSE      TSE
address IT security deficiencies.                      N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 6 of 26

   Control                                            Policy   Procedure   Implemented   Tested   Integrated        Comments*
G. Applicable Statewide and budget-unit-specific      Yes      Yes         Yes           Yes      Yes
IT security policies and standards are                No       No          No            No       No
communicated to appropriate third-party
                                                      TSE      TSE         TSE           TSE      TSE
organizations.
                                                      N/A      N/A         N/A           N/A      N/A
H. An agency IT security program exists               Yes      Yes         Yes           Yes      Yes
including assignment of roles and responsibilities,   No       No          No            No       No
as well as creation of necessary procedures,
                                                      TSE      TSE         TSE           TSE      TSE
adherence requirements, and monitoring controls.
                                                      N/A      N/A         N/A           N/A      N/A
I. Overlapping IT security roles/responsibilities
between agencies and/or contractors relative to
security services received from, or provided to,      Yes      Yes         Yes           Yes      Yes
other agencies are identified, defined, and           No       No          No            No       No
resolved. Inter-agency Service Agreements are         TSE      TSE         TSE           TSE      TSE
enacted relative to security services, as             N/A      N/A         N/A           N/A      N/A
applicable.

J. IT projects are implemented as described in
Compliance and Project Management –                   Yes      Yes         Yes           Yes      Yes
Enterprise Project Management Office as well as       No       No          No            No       No
relevant Federal and individual agency standards.     TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

2. IT RISK MANAGEMENT

A. Risk assessments for IT systems and their
environments are performed at least annually to
determine security vulnerabilities. Security          Yes      Yes         Yes           Yes      Yes
vulnerabilities are more heavily weighted toward      No       No          No            No       No
the impact of the loss on agency operations,          TSE      TSE         TSE           TSE      TSE
agency assets, or individuals than on the threat of   N/A      N/A         N/A           N/A      N/A
loss.

Title: IT Risk Management Standard S-STD-003.001                                                               Security Domain Team
Approval Date: April 7, 2005                                                                                            Page 7 of 26

   Control                                            Policy   Procedure   Implemented   Tested   Integrated        Comments*
                                                      Yes      Yes         Yes           Yes      Yes
B. IT plans address vulnerabilities identified in
IT Security Assessment.                               No       No          No            No       No
                                                      TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

3. ACCOUNT MANAGEMENT
A. Activities for establishing on-line accounts,
levels of approval, access to confidential            Yes      Yes         Yes           Yes      Yes
information, remote access, monitoring inactive       No       No          No            No       No
accounts, forgotten passwords, and closing            TSE      TSE         TSE           TSE      TSE
accounts are controlled.
                                                      N/A      N/A         N/A           N/A      N/A

B. Management communicates that accountability
for actions taken on an IT resource (e.g., computer   Yes      Yes         Yes           Yes      Yes
system, agency or State application system, etc.)     No       No          No            No       No
belongs to the owner of the specific userID under     TSE      TSE         TSE           TSE      TSE
which those actions take place.                       N/A      N/A         N/A           N/A      N/A

C. System, application, and information access is
                                                      Yes      Yes         Yes           Yes      Yes
only granted via a formal and auditable procedure
having a retrievable, associated written record of    No       No          No            No       No
the request and subsequent authorization.             TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                               Security Domain Team
Approval Date: April 7, 2005                                                                                            Page 8 of 26

   Control                                             Policy   Procedure   Implemented   Tested   Integrated        Comments*
D. The steps and timing for granting or
withdrawing system and information access              Yes      Yes         Yes           Yes      Yes
privileges are documented and maintained In            No       No          No            No       No
accordance with Statewide Standard S-STD0011,          TSE      TSE         TSE           TSE      TSE
Personnel Security.
                                                       N/A      N/A         N/A           N/A      N/A

E. All special access privileges, including high-
level privileges (such as root access), system
                                                       Yes      Yes         Yes           Yes      Yes
utilities, and privileges that provide access to
sensitive network devices, operating system, or        No       No          No            No       No
software application capabilities are documented       TSE      TSE         TSE           TSE      TSE
and maintained.                                        N/A      N/A         N/A           N/A      N/A

F. All holders of remote access privileges to          Yes      Yes         Yes           Yes      Yes
agency IT resources, including third-party entities,   No       No          No            No       No
are documented and maintained.                         TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

4. CONFIGURATION MANAGEMENT

A. A configuration management program governs          Yes      Yes         Yes           Yes      Yes
changes to devices and/or associated software          No       No          No            No       No
components in the production IT environment.           TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A
B. A perpetual inventory, including
configuration/version information for all IT           Yes      Yes         Yes           Yes      Yes
devices and associated software assets, and IT         No       No          No            No       No
applications, is maintained within agency.             TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 9 of 26

   Control                                             Policy   Procedure   Implemented   Tested   Integrated        Comments*
C. A high-level network/ systems diagram exists,       Yes      Yes         Yes           Yes      Yes
supported by detail diagrams identifying the
                                                       No       No          No            No       No
underlying structures of the agency
computer/systems network.                              TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

5. AUTHENTICATION AND DIRECTORY SERVICES
A. All external connections to agency networks
are routed through secure gateways, encrypted, and
use strong authentication, such as
                                                       Yes      Yes         Yes           Yes      Yes
challenge/response devices, one-time passwords,
                                                       No       No          No            No       No
tokens, Kerberos, or smart cards, in addition to the
standard method of authentication required for         TSE      TSE         TSE           TSE      TSE
internal connectivity (i.e., multifactor               N/A      N/A         N/A           N/A      N/A
authentication).

B. Access to resources and services shall be in
accordance with Statewide Standard S-STD-011,
Personnel Security, and Statewide Standard S-STD-      Yes      Yes         Yes           Yes      Yes
011, Authentication and Directory Services. Internal   No       No          No            No       No
and external connectivity to networks to provide       TSE      TSE         TSE           TSE      TSE
access to resources and services shall be in           N/A      N/A         N/A           N/A      N/A
accordance with Statewide StandardS-STD-005 ,
Network Security.

C. Lightweight Directory Access Protocol               Yes      Yes         Yes           Yes      Yes
(LDAP) is used to provide access to directory and      No       No          No            No       No
application services.                                  TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 10 of 26

   Control                                            Policy   Procedure   Implemented   Tested   Integrated        Comments*
D. User authentication employs a userID               Yes      Yes         Yes           Yes      Yes
associated with something (password) only the
                                                      No       No          No            No       No
user/customer knows or something (token) only
the user possesses.                                   TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

6. SESSION CONTROLS
A. Automatic session timeouts are in place on
multi-user information systems and remote             Yes      Yes         Yes           Yes      Yes
communication systems. The maximum period of          No       No          No            No       No
inactivity is set commensurate with the sensitivity   TSE      TSE         TSE           TSE      TSE
of information housed on the individual system.       N/A      N/A         N/A           N/A      N/A

B. All system users log off at the end of the         Yes      Yes         Yes           Yes      Yes
business day. Where business requirements
                                                      No       No          No            No       No
necessitate a deviation, rationale and procedures
are documented.                                       TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A
C. Locking screensavers are used on all personal
computers (including laptops) and are                 Yes      Yes         Yes           Yes      Yes
automatically activated by the computer’s             No       No          No            No       No
operating system after a specific period of           TSE      TSE         TSE           TSE      TSE
inactivity determined by the agency.                  N/A      N/A         N/A           N/A      N/A

D. Password strength used on locking screen
savers is determined by the capabilities of the
applicable operating system. Passwords meet the       Yes      Yes         Yes           Yes      Yes
requirements of Statewide Standard S-STD-001,         No       No          No            No       No
Authentication and Directory Services, unless         TSE      TSE         TSE           TSE      TSE
otherwise prevented by the capabilities of the        N/A      N/A         N/A           N/A      N/A
operating system.

Title: IT Risk Management Standard S-STD-003.001                                                               Security Domain Team
Approval Date: April 7, 2005                                                                                            Page 11 of 26

   Control                                             Policy   Procedure   Implemented   Tested   Integrated        Comments*
E. Accounts are locked from further use following
a maximum number of detected, unsuccessful             Yes      Yes         Yes           Yes      Yes
login attempts. Resetting procedures ensure that       No       No          No            No       No
only the correct account holder is requesting the      TSE      TSE         TSE           TSE      TSE
reset.                                                 N/A      N/A         N/A           N/A      N/A

F. Where available, access logs are turned on and
protected from accidental or deliberate                Yes      Yes         Yes           Yes      Yes
overwriting, maintained for a period of time           No       No          No            No       No
determined by business need, and stored in
                                                       TSE      TSE         TSE           TSE      TSE
accordance with Statewide Standard S-STD-010
P800-S870, Backups.                                    N/A      N/A         N/A           N/A      N/A

7. NETWORK SECURITY
A. All external traffic is routed through secure       Yes      Yes         Yes           Yes      Yes
gateways, such as firewalls, employed at the edge
                                                       No       No          No            No       No
of the agency’s network, including the Internet
Gateway.                                               TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A
B. Client platform devices, including State-owned
assets, client devices used by remote workers and
telecommuters, as well as third-party entities,        Yes      Yes         Yes           Yes      Yes
connected to the agency’s internal network should      No       No          No            No       No
be protected from sending or receiving hostile         TSE      TSE         TSE           TSE      TSE
threats from unauthorized network traffic or           N/A      N/A         N/A           N/A      N/A
software applications.

C. Internetworking devices (including routers,         Yes      Yes         Yes           Yes      Yes
firewalls, switches, etc.) are controlled to prevent   No       No          No            No       No
unauthorized access.                                   TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 12 of 26

   Control                                            Policy   Procedure   Implemented   Tested   Integrated         Comments*
D. Roles, responsibilities, and related activities    Yes      Yes         Yes           Yes      Yes
for implementing patch management on
                                                      No       No          No            No       No
internetworking devices (including routers,
firewalls, switches, etc.) are identified.            TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A
E. Services provided through the Internet (web-       Yes      Yes         Yes           Yes      Yes
enabled applications, FTP, Mail, DNS, VoIP, etc.)
                                                      No       No          No            No       No
are deployed on a Demilitarized Zone (DMZ) or
proxies from a DMZ.                                   TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

F. All external connections to networks are routed    Yes      Yes         Yes           Yes      Yes
through secure gateways and protected by an           No       No          No            No       No
approved encryption method.                           TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A
G. Wireless networks employ centralized user
authentication in accordance with Statewide
                                                      Yes      Yes         Yes           Yes      Yes
Standard P800-S820, Authentication and
                                                      No       No          No            No       No
Directory Services, encryption technologies with
automated key distribution, and VPN technologies,     TSE      TSE         TSE           TSE      TSE
as appropriate.                                       N/A      N/A         N/A           N/A      N/A

H. Intrusion detection mechanisms or intrusion
prevention tools are incorporated into all servers    Yes      Yes         Yes           Yes      Yes
connected to WANs and to all internetworking          No       No          No            No       No
devices that serve as gateways between WAN            TSE      TSE         TSE           TSE      TSE
network segments.                                     N/A      N/A         N/A           N/A      N/A

I. Network and host vulnerability scanners are        Yes      Yes         Yes           Yes      Yes
used to test for the vulnerabilities of internal      No       No          No            No       No
systems and of network perimeter defenses, as
                                                      TSE      TSE         TSE           TSE      TSE
well as adherence to security policy and standards.
                                                      N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                               Security Domain Team
Approval Date: April 7, 2005                                                                                            Page 13 of 26

   Control                                          Policy   Procedure   Implemented   Tested   Integrated        Comments*
J. Hardcopy and electronic documentation of         Yes      Yes         Yes           Yes      Yes
network device configurations, network diagrams,    No       No          No            No       No
etc., is destroyed when superseded or no longer
                                                    TSE      TSE         TSE           TSE      TSE
needed.
                                                    N/A      N/A         N/A           N/A      N/A

8. ENCRYPTION TECHNOLOGIES
A. Secure e-mail communications use S/MIME          Yes      Yes         Yes           Yes      Yes
Version 3, or succeeding approved standards, for
                                                    No       No          No            No       No
encryption, sender authentication, and message
integrity services.                                 TSE      TSE         TSE           TSE      TSE
                                                    N/A      N/A         N/A           N/A      N/A

B. Security levels for specific PKI and PGP uses    Yes      Yes         Yes           Yes      Yes
have been determined in conjunction with State’s    No       No          No            No       No
Policy Authority.                                   TSE      TSE         TSE           TSE      TSE
                                                    N/A      N/A         N/A           N/A      N/A

9. INCIDENT RESPONSE AND REPORTING

A. A SIPC membership application has been           Yes      Yes         Yes           Yes      Yes
completed for the agency. Contact information for   No       No          No            No       No
SIPC is up to date.                                 TSE      TSE         TSE           TSE      TSE
                                                    N/A      N/A         N/A           N/A      N/A
B. All cyber intrusions are reported to SIPC        Yes      Yes         Yes           Yes      Yes
within one hour of discovery. A SIPC Incident       No       No          No            No       No
Report is completed for each cyber intrusion.       TSE      TSE         TSE           TSE      TSE
                                                    N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                             Security Domain Team
Approval Date: April 7, 2005                                                                                          Page 14 of 26

   Control                                             Policy   Procedure   Implemented   Tested   Integrated        Comments*
10. VIRUS AND MALICIOUS CODE PROTECTION
A. All workstations and servers are protected by       Yes      Yes         Yes           Yes      Yes
virus-scanning software that has “notify and
                                                       No       No          No            No       No
clean” enabled by default. Users are prevented
from disabling virus-scanning software.                TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A
B. Each agency shall ensure that all remote
workstations and servers used by State employees,
contractors, and third-party entities that access      Yes      Yes         Yes           Yes      Yes
agency internal networks are protected with virus-     No       No          No            No       No
scanning software equivalent to that used by the       TSE      TSE         TSE           TSE      TSE
agency. Virus-scanning software shall be               N/A      N/A         N/A           N/A      N/A
configured and kept current.

C. Virus-scanning software regularly scans all
files stored on direct attached storage devices to
the workstation and any file accessed or modified      Yes      Yes         Yes           Yes      Yes
by a workstation software application, whether         No       No          No            No       No
deployed on the individual workstation device,         TSE      TSE         TSE           TSE      TSE
host- or server-based, or application service          N/A      N/A         N/A           N/A      N/A
provider (ASP) based.

D. Specific individuals are responsible and
accountable to configure and execute appropriate
virus-scanning software on all network-attached
(wired and wireless) workstations, and to maintain     Yes      Yes         Yes           Yes      Yes
appropriate inoculants and patches for each virus or   No       No          No            No       No
malicious code infection on all network servers        TSE      TSE         TSE           TSE      TSE
that provide virus-scanning services to network-       N/A      N/A         N/A           N/A      N/A
attached (wired and wireless) workstations and on
all portable and stand-alone workstations.

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 15 of 26

   Control                                             Policy   Procedure   Implemented   Tested   Integrated        Comments*
E. All incoming email, including attachments, is       Yes      Yes         Yes           Yes      Yes
scanned for the existence of virus or malicious
                                                       No       No          No            No       No
code. Viruses and malicious code are contained
and eradicated upon discovery.                         TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A
F. Employees and contractors are provided a clear      Yes      Yes         Yes           Yes      Yes
process, including appropriate contact points, to
                                                       No       No          No            No       No
address, resolve, and report virus or malicious
code infections.                                       TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A
G. Protection techniques guard against virus and
                                                       Yes      Yes         Yes           Yes      Yes
malicious code and potential intrusion from Instant
Messaging (IM), peer-to-peer (P2P) file-sharing,       No       No          No            No       No
and Internet Relay Chat (IRC).                         TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

11. BUSINESS CONTINUITY & DISASTER RECOVERY

A. Phase I Business Impact Assessment, Phase II        Yes      Yes         Yes           Yes      Yes
Strategy Development, and Phase III Strategy           No       No          No            No       No
Implementation have all been completed.                TSE      TSE         TSE           TSE      TSE
                                                       N/A      N/A         N/A           N/A      N/A

12. BACKUPS
A. Backups are taken using a defined cycle
frequently enough to meet the time-criticality of      Yes      Yes         Yes           Yes      Yes
agency business processes, business continuity         No       No          No            No       No
plans, as well as legal, regulatory, and contractual   TSE      TSE         TSE           TSE      TSE
obligations.                                           N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 16 of 26

   Control                                               Policy   Procedure   Implemented   Tested   Integrated        Comments*
B. Backup media types (disks, RAID storage,
optical archive, tape, etc.) used are based on           Yes      Yes         Yes           Yes      Yes
business continuity planning for critical services       No       No          No            No       No
and regulatory obligations relative to permanence        TSE      TSE         TSE           TSE      TSE
of data/information.                                     N/A      N/A         N/A           N/A      N/A

C. Automated back-up management software is              Yes      Yes         Yes           Yes      Yes
used to perform the backups on designated                No       No          No            No       No
systems.                                                 TSE      TSE         TSE           TSE      TSE
                                                         N/A      N/A         N/A           N/A      N/A
                                                         Yes      Yes         Yes           Yes      Yes
D. The same controls as apply to the original data
apply to the data being backed up.                       No       No          No            No       No
                                                         TSE      TSE         TSE           TSE      TSE
                                                         N/A      N/A         N/A           N/A      N/A
E. All operating system software, application
                                                         Yes      Yes         Yes           Yes      Yes
software, related software, utilities, etc., necessary
to configure and restore critical information and        No       No          No            No       No
services are backed up.                                  TSE      TSE         TSE           TSE      TSE
                                                         N/A      N/A         N/A           N/A      N/A

F. Backups are tested on a regular basis, as             Yes      Yes         Yes           Yes      Yes
documented, for restorability, recoverability, and       No       No          No            No       No
to ensure that restored information has not been
                                                         TSE      TSE         TSE           TSE      TSE
compromised.
                                                         N/A      N/A         N/A           N/A      N/A

13. MAINTENANCE

Title: IT Risk Management Standard S-STD-003.001                                                                  Security Domain Team
Approval Date: April 7, 2005                                                                                               Page 17 of 26

   Control                                             Policy   Procedure   Implemented   Tested   Integrated         Comments*
A. Configurations of critical systems’ platform
and network infrastructure, operating system
                                                       Yes      Yes         Yes           Yes      Yes
software, software application, and related
software configurations are documented and             No       No          No            No       No
maintained. Formal change control exists for           TSE      TSE         TSE           TSE      TSE
configurations of critical systems.                    N/A      N/A         N/A           N/A      N/A

B. Sensitive data stored on systems being sent
offsite for repair or maintenance operations is        Yes      Yes         Yes           Yes      Yes
removed from the storage media in accordance           No       No          No            No       No
with Statewide Standard P800-S880, Media               TSE      TSE         TSE           TSE      TSE
Sanitizing/Disposal.                                   N/A      N/A         N/A           N/A      N/A

C. Access to critical system hardware and
software, wiring, and networks is restricted to        Yes      Yes         Yes           Yes      Yes
personnel authorized by the agency and controlled      No       No          No            No       No
by rules of least privilege required to complete the   TSE      TSE         TSE           TSE      TSE
assigned task.                                         N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                                Security Domain Team
Approval Date: April 7, 2005                                                                                             Page 18 of 26

   Control                                            Policy   Procedure   Implemented   Tested   Integrated        Comments*
14. MEDIA SANITIZING/DISPOSAL

A. Any IT device, network component, operating
system software, application software, or storage
media containing public/official records has the      Yes      Yes         Yes           Yes      Yes
final disposition of those records established with
                                                      No       No          No            No       No
New Mexico State Library, Archives, and Public
Records (ASLAPR) before it is disposed of             TSE      TSE         TSE           TSE      TSE
through State Surplus or provided to another State    N/A      N/A         N/A           N/A      N/A
organization.

B. Before disposal through State Surplus, data        Yes      Yes         Yes           Yes      Yes
stored on any IT device is deleted in a manner that   No       No          No            No       No
renders it unrecoverable.                             TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A
C. Prior to off-site repair of IT devices, network    Yes      Yes         Yes           Yes      Yes
components, operating system or application
                                                      No       No          No            No       No
software, or storage media, all agency sensitive
data is removed.                                      TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

                                                      Yes      Yes         Yes           Yes      Yes
D. Only authorized personnel remove sensitive
                                                      No       No          No            No       No
data from IT devices.
                                                      TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                               Security Domain Team
Approval Date: April 7, 2005                                                                                            Page 19 of 26

   Control                                            Policy   Procedure   Implemented   Tested   Integrated        Comments*
15. IT PHYSICAL SECURITY

A. Information systems (mainframes, servers,
etc.), media storage areas, and related               Yes      Yes         Yes           Yes      Yes
communication wiring and network devices are          No       No          No            No       No
located in secure locations that are locked and       TSE      TSE         TSE           TSE      TSE
restricted to access by authorized personnel only.    N/A      N/A         N/A           N/A      N/A

B. Physical access security measures employed         Yes      Yes         Yes           Yes      Yes
for back-up systems/facilities are equivalent to      No       No          No            No       No
those of the primary facilities.                      TSE      TSE         TSE           TSE      TSE
                                                      N/A      N/A         N/A           N/A      N/A
C. Information systems, media storage areas, and
related communication wiring and network              Yes      Yes         Yes           Yes      Yes
devices are protected against loss or malfunction     No       No          No            No       No
of environmental equipment or services necessary      TSE      TSE         TSE           TSE      TSE
for the operation of the facility that houses them.   N/A      N/A         N/A           N/A      N/A

D. Computing and telecommunications equipment
is inventoried in accordance with Statewide           Yes      Yes         Yes           Yes      Yes
Standard S-STD-002, Configuration Management,         No       No          No            No       No
accounted for, and safeguarded from loss and          TSE      TSE         TSE           TSE      TSE
resulting unauthorized use.
                                                      N/A      N/A         N/A           N/A      N/A

Title: IT Risk Management Standard S-STD-003.001                                                               Security Domain Team
Approval Date: April 7, 2005                                                                                            Page 20 of 26

Control                                             Policy   Procedure   Implemented   Tested   Integrated     Comments*
16. PERSONNEL SECURITY

A. Personnel policies and procedures show clear
accountability for security administration.         Yes      Yes         Yes           Yes      Yes
Security policies and procedures are available to
                                                    No       No          No            No       No
and
applied to every existing State employee and        TSE      TSE         TSE           TSE      TSE
contractor, as well as to new State employees       N/A      N/A         N/A           N/A      N/A
and contractors.
B. Job-related requirements for potential IT
personnel or contractors working in primary         Yes      Yes         Yes           Yes      Yes
facilities housing critical information systems     No       No          No            No       No
or handling confidential information are used       TSE      TSE         TSE           TSE      TSE
as a hiring consideration.                          N/A      N/A         N/A           N/A      N/A

17. SECURITY TRAINING AND AWARENESS

A. Security awareness training content exists       Yes      Yes         Yes           Yes      Yes
and is regularly reviewed and updated to ensure     No       No          No            No       No
that it addresses the organizational mission        TSE      TSE         TSE           TSE      TSE
including culture, business, technology,            N/A      N/A         N/A           N/A      N/A
systems, and data/information.

B. IT security roles and responsibilities of        Yes      Yes         Yes           Yes      Yes
key personnel are defined and documented.           No       No          No            No       No
                                                    TSE      TSE         TSE           TSE      TSE
                                                    N/A      N/A         N/A           N/A      N/A

18. PLATFORM INFRASTRUCTURE

Title: IT Risk Management Standard S-STD-003.001                                                             Security Domain Team
Approval Date: April 7, 2005                                                                                          Page 21 of 26

A. Platform devices have the appropriate level of      Yes   Yes   Yes   Yes   Yes
security functionality incorporated as part of the     No    No    No    No    No
installed operating system.                            TSE   TSE   TSE   TSE   TSE
                                                       N/A   N/A   N/A   N/A   N/A
B. Shared platforms (including mainframes,
servers, etc.) are controlled to prevent               Yes   Yes   Yes   Yes   Yes
unauthorized access, both internal and external,       No    No    No    No    No
in accordance with Statewide Standard S-STD-           TSE   TSE   TSE   TSE   TSE
005, Network Security.                                 N/A   N/A   N/A   N/A   N/A

C. Roles, responsibilities, and related activities     Yes   Yes   Yes   Yes   Yes
for implementing patch management on platform          No    No    No    No    No
device operating systems are identified.               TSE   TSE   TSE   TSE   TSE
                                                       N/A   N/A   N/A   N/A   N/A
D. Hardcopy and electronic documentation of            Yes   Yes   Yes   Yes   Yes
shared platform device configurations, access
                                                       No    No    No    No    No
lists, diagrams, etc., is destroyed, as appropriate,
when no longer needed.                                 TSE   TSE   TSE   TSE   TSE
                                                       N/A   N/A   N/A   N/A   N/A

E. All portable platform devices (laptops, PDAs,
etc.) capable of storing information (documents,
databases, etc.) that connect to agency networks       Yes   Yes   Yes   Yes   Yes
adhere to authentication requirements,                 No    No    No    No    No
connectivity requirements, as well as all other        TSE   TSE   TSE   TSE   TSE
applicable Statewide IT security standards have        N/A   N/A   N/A   N/A   N/A
any automatic logon capability disabled.

Title: IT Risk Management Standard S-STD-003.001                                     Security Domain Team
Approval Date: April 7, 2005                                                                  Page 22 of 26

19. APPLICATION SOFTWARE

A. All software applications are capable of          Yes   Yes   Yes   Yes   Yes
securely exchanging information and integrating
                                                     No    No    No    No    No
or interoperating with other software
applications.                                        TSE   TSE   TSE   TSE   TSE
                                                     N/A   N/A   N/A   N/A   N/A

B. Security services associated with software
applications, databases, and utility software
adhere to Statewide IT security standards, allow     Yes   Yes   Yes   Yes   Yes
for all security updates to be pushed to, or         No    No    No    No    No
accepted by, all associated software products,       TSE   TSE   TSE   TSE   TSE
and allow for an integrated lightweight directory    N/A   N/A   N/A   N/A   N/A
access protocol (LDAP) directory service.

20. PRODUCTIVITY SOFTWARE TOOLS

A. Roles, responsibilities, and related activities   Yes   Yes   Yes   Yes   Yes
for implementing patch management on                 No    No    No    No    No
productivity software are identified.                TSE   TSE   TSE   TSE   TSE
                                                     N/A   N/A   N/A   N/A   N/A

 Title: IT Risk Management Standard S-STD-003.001                                  Security Domain Team
 Approval Date: April 7, 2005                                                               Page 23 of 26

21. CLASSIFICATION OF DATA

A. Data/information is classified according to its
degree of sensitivity in a universally                 Yes   Yes   Yes   Yes   Yes
understandable manner and that maintains its           No    No    No    No    No
security classification as it traverses any physical   TSE   TSE   TSE   TSE   TSE
or logical boundary.                                   N/A   N/A   N/A   N/A   N/A

B. Data/information is classified into
“confidential” versus “public” information.            Yes   Yes   Yes   Yes   Yes
(Agencies requiring additional classifications
                                                       No    No    No    No    No
may create and document those classifications
and related owner/custodian/recipient                  TSE   TSE   TSE   TSE   TSE
responsibilities at their discretion.)                 N/A   N/A   N/A   N/A   N/A

C. Aggregates of data/information are classified
using the most secure classification level of any
                                                       Yes   Yes   Yes   Yes   Yes
individual component. Extracts of
data/information are secured to the same level as      No    No    No    No    No
the file/database from which the data/information      TSE   TSE   TSE   TSE   TSE
has been extracted.                                    N/A   N/A   N/A   N/A   N/A

 Title: IT Risk Management Standard S-STD-003.001                                    Security Domain Team
 Approval Date: April 7, 2005                                                                 Page 24 of 26

E. Data/information being shared is
appropriately and consistently classified and
protected comparably to when the                       Yes   Yes   Yes   Yes   Yes
data/information was within the original agency’s      No    No    No    No    No
immediate control. The value and classification        TSE   TSE   TSE   TSE   TSE
of the data/information is communicated to the         N/A   N/A   N/A   N/A   N/A
respective additional custodians/recipients.

22. DATABASE ACCESS

A. Database access is securely implemented             Yes   Yes   Yes   Yes   Yes
with regard for availability, integrity, and           No    No    No    No    No
confidentiality of the data.                           TSE   TSE   TSE   TSE   TSE
                                                       N/A   N/A   N/A   N/A   N/A
B. Entry and update of data stored in databases is
accomplished only in accordance with the
business rules established in software application     Yes   Yes   Yes   Yes   Yes
systems. Data access and permissions are               No    No    No    No    No
assigned within the context of the software            TSE   TSE   TSE   TSE   TSE
application and in accordance with Statewide           N/A   N/A   N/A   N/A   N/A
Standard S-STD-001, Authentication and Directory
Services.
C. Free-form data entry and update using direct
database access are restricted. Direct database
access, when required, is accomplished in
accordance with Statewide Standard S-STD-001,
Authentication and Directory Services. Owners of the   Yes   Yes   Yes   Yes   Yes
data and information stored in the relevant            No    No    No    No    No
databases provide written delegated authority or       TSE   TSE   TSE   TSE   TSE
specific access permissions to ensure that             N/A   N/A   N/A   N/A   N/A
relevant business rules implemented by the
software application system for normal entry and
update are not violated.

Title: IT Risk Management Standard S-STD-003.001                                     Security Domain Team
Approval Date: April 7, 2005                                                                  Page 25 of 26

D. Direct database access for ad-hoc queries and
end-user reporting is read-only. Software utilized   Yes   Yes   Yes
for ad-hoc queries and end-user reporting
                                                     No    No    No
conforms to database technology connectivity
and access requirements.                             TSE
                                                     N/A   TSE
                                                           N/A   N/A
                                                     N/A   N/A

Title: IT Risk Management Standard S-STD-003.001                       Security Domain Team
Approval Date: April 7, 2005                                                    Page 26 of 26

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
