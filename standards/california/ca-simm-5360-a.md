---
schema_version: 1
corpus: states-government-it
jurisdiction: california
id: ca-simm-5360-a
title: Telework and Remote Access Security Standard
doc_type: standard
citation: SIMM 5360-A
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/policy/simm/simm-5300/simm-5360-a-telework-and-remote-access-security-standard/
source_format: html
retrieved: '2026-11-11'
source_sha256: bd6a5d2760217fb30883e495f0ce95a94b33b706c2b9170df7753db4724deda4
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: 'Text taken from the California Department of Technology''s web page for the instrument:
  from the page heading to the end of the page''s content, one line per paragraph, heading, list item
  and table row (a table row''s cells are joined by '' | ''), with markup, the site menu, the side navigation,
  the page''s contents list (''On this page''), the print button, scripts, the footer and non-breaking
  spaces removed.'
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

# Telework and Remote Access Security Standard (SIMM 5360-A)

## At a glance

SIMM 5360-A, Telework and Remote Access Security Standard: an item of the Office of Information Security's information security series (SIMM 5300), the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

SIMM 5360-A Telework and Remote Access Security Standard

Revision history
Version | Date | Owner | Change Summary
v.1 | December 2012 | California Information Security Office (CISO) | Initial release
v.2 | September 2013 | CISO | SIMM number change
v.3 | January 2018 | Office of Information Security (OIS) | Office name change
v.4 | October 2018 | OIS | Added requirement to require web-based connection to utilize two-factor authentication
v.5 | July 2022 | OIS | Updated URL to link to updated Statewide Policy (SAM Section 181) and added missing “AND” in Section 7
Heading.
v.6 | November 2024 | OIS | Format change and the addition of physical location in USA requirement
Purpose
This standard provides guidelines to effectively and securely work remotely while ensuring continuity of operations, maintaining productivity, and safeguarding organizational resources. This policy outlines the requirements, responsibilities, and security measures to protect data integrity, confidentiality, and availability.
This standard is not to be construed as either replacing or superseding any other applicable statewide, federal or private industry security policy, standard or requirement including, but not limited to, State Administrative Manual (SAM) Section 181, SAM Section 5100, and SAM Section 5300.
The material in this standard is technically oriented, and it is assumed that readers have at least a basic understanding of remote access, networking, network security, and system security.
Those not having this level of understanding should consult their agency Chief Information Officer and Information Security Officers for assistance.
Scope
This standard applies to telework and remote access users who have access to California State information technology (IT) infrastructure and information assets through public networks. In addition to remote access user users, this standard is applicable to security, system, and network engineers and administrators, as well as computer security program managers, who are responsible for the technical aspects of preparing, operating, and securing remote access solutions and telework client devices, and state entity heads and program managers responsible for the overall security of information assets within their agencies.
Compliance
Government Code (GOV) Section 11549.3 tasks the Office of Information Security (OIS) to create, issue, and maintain policies, standards, and procedures; oversee information security risk management for agencies and state entities; provide information security and privacy guidance; and ensure compliance with State Administrative Manual (SAM) Chapter 5300 and Statewide Information Management Manual (SIMM) section 5300.
State entities must adhere to OIS-issued information security and privacy policies and all relevant laws, regulations, rules, and standards governing their agency/state entity. Full compliance is expected, and noncompliance will be addressed according to this standard and its associated procedures.
Definitions
Agency – When used lower case (agency), refers to any office, department, board, bureau, commission or other organizational entity within state government. When capitalized (Agency), the term refers to one of the state’s super agencies; such as the State and Consumer Services Agency or the Health and Human Services Agency (see SAM Section 4819.2 definitions).
Direct Application Access Architecture[1] – A high-level remote access architecture that allows teleworkers to access an individual application directly, without using remote access software.
Information Assets – All categories of information (confidential, personal, sensitive, or public), all forms of information assets (paper or electronic), information technology facilities, equipment and software owned or leased by state agencies. (See SAM Section 5300.4 definitions; Condensed).
IT Administrators – The agency’s IT staff such as those individuals responsible for support and security of the IT infrastructure.
IT Infrastructure – An agency’s information technology platform for the support of agency programs and management. Included in the infrastructure are equipment, software, communication networks. (See SAM Section 4989.1 definitions; Adapted.)
Mobile Computing Device – Portable-computing devices that can connect by cable, telephone wire, wireless transmission, or via any Internet connection to an agency’s IT infrastructure and/ or data systems. (See SAM Section 4989.1).
Multi-homed connection – A host connected to two or more networks or having two or more network addresses. For example, a computer may be connected to a serial line and a LAN or to multiple LANs.
Network-level Connection – The connection provides access to a state private network through a tunneling or a remote desktop access architecture and the software and data that reside on the internal information assets.
Portal Architecture – A high-level remote access architecture that is based on a server that offers teleworkers access to one or more applications through a single, centralized interface.
Remote Access[2] – The connection of an information asset from an off-site location to an information asset on state IT infrastructure.
Remote Desktop Access Architecture – A high-level remote access architecture that gives a teleworker the ability to remotely control a particular desktop computer at the organization, most often the computer assigned to the user that resides at the organization’s office from a telework device.
Smartphone – A mobile computing device that provides advanced computing capability and connectivity and runs a complete operating system and platform for application developers and users to install and run more advanced applications.
Split Tunneling – The process of allowing a remote VPN user to access a public network, most commonly the Internet, while the user is allowed to access resources on the VPN. A disadvantage of this method is that it essentially renders the VPN vulnerable to attack as it is accessible through the public, non-secure network.
Strong password – A minimum of eight characters using a combination of upper and lowercase letters, numbers and special characters.
Telework – An arrangement in which an employee regularly performs officially assigned duties at home or an alternate work site.
Tunneling Architecture – A high-level remote access architecture that provides a secure tunnel between a telework device and a tunneling server through which application traffic may pass. Tunnels use cryptography to protect the confidentiality and integrity of the transmitted information between client device and the VPN gateway
Two-factor authentication – Authentication based on two of the following: something you know (i.e., password), something you have (i.e., token or smartcard), or something you are (i.e., a biometric).
Virtual Private Network (VPN) – A virtual network, built on top of existing physical networks, that provides a secure communications tunnel for data and other information transmitted between networks.
Web-based Connection – the connection provides access to one or more applications through a single centralized interface through a direct application access or portal architecture (typically a web-browser to a portal server located within the demilitarized zone [DMZ]). This type ofconnection creates an area that serves as a boundary between two or more networks and isolates the information asset from the internal private network.
[1] The National Institute of Standards and Technology (NIST) Special Publication 800-46, Appendix A Glossary is the source of remote architecture definitions.
[2] For the remainder of this document teleworker, telework user and remote access user are interchangeable.
Additional resources
I. Agency Head Requirements
Training of Telework and Remote Access Users
Before authorizing employees to connect to state IT infrastructure for telework or any remote access purposes, agency heads shall ensure that managers, supervisors, and telework users receive security training addressing at least the following subjects:
a. The responsibilities outlined in this standard.
b. The potential enterprise risks to both the agency’s information assets and the information assets of other government entities that are interconnected and/or available to authorized users through the agency’s IT infrastructure.
c. The potential risks to employees if an exception is made to authorize the use of personally owned information assets and the agency’s limitations on guidance and support of personally owned information assets.
d. How information is to be backed up and destroyed, including cache clearing and telework document shredding in the telework setting.
e. Protection of remote access-specific authenticators, such as passwords, personal identification numbers (PIN), and hardware tokens.
f. Recognition of social engineering attack techniques and appropriate mitigation measures.
g. The consequences for disabling, altering or circumventing the security configurations that protect state information assets.
h. Security incident management and breach disclosure procedures.
II. Agency Management Requirements
Identify the Needs of Remote Access Users
Before managers and/or supervisors authorize work to be performed under a remote access arrangement they must do the following:
a. Identify the type of work to be performed through the remote access arrangement.
b. Only authorize remote access user access to resources which are necessary to carry out the telework arrangement safely and securely. Managers and/or supervisors shall consider whether the needs to support the remote access arrangement can be met with less access and connectivity than provided at the main office. Work to be performed during an emergency situation to maintain essential operations may not warrant the remote access user to have the same access or connectivity as they do at the main office. In many cases, a telephone and email access through a Web-based connection may be all that is required.
c. Users who are authorized for remote access into state information assets must be physically located within the continental United States.
d. As applicable, ensure a telework agreement and remote access agreement between the telework/remote access user and manager is signed and maintained in the agency file pursuant to the October 2021 Statewide Telework Policy (SAM Section 181) and Model Program.
III. Agency IT Administrator Requirements
Agency IT Administrators shall ensure that the control requirements which are applied to remote access users of both state-owned and personally owned information assets are in place before connections to state IT infrastructure are allowed. In addition, before connections are made, agency IT Administrators shall ensure that the following requirements are met:
1. Maintain software updates
a. Agency IT Administrators shall ensure that information assets used to connect to the agency IT infrastructure are checked and use up-to-date operating system software and security software (anti-virus, anti-spyware, firewall, and host intrusion prevention) every time a remote connection is initiated.
b. This is typically accomplished through a Network Access Control (NAC) solution which integrates an automatic remediation process that fixes a non-compliant information asset before allowing access into the network systems. This ensures the information asset is operating securely before interoperability with agency IT infrastructure is allowed.
2. Maintain software updates
a. Each remote access user shall have an individual user account that does not have elevated privileges. Accounts with elevated privileges create an increased security risk because they allow the user to change security settings and install applications.
b. Remote access user accounts shall require two-factor authentication, including when using a Web-based connection, such as Outlook Web Access (OWA) or another similar interface.
c. Remote access user accounts shall, as a rule, be set up to have limited privileges. Remote access users will not normally require accounts with full privileges (i.e., administrative accounts). In the unusual event that remote access users require administrative accounts, they shall be used only when performing authorized IT Administrator tasks, such as installing updates and application software, managing user accounts, and modifying operating system and application settings on the information asset.
3. Validate control requirements
a. Agency IT Administrators shall log and monitor all remote access. Log files shall capture sufficient detail to allow a virtual reconstruction of the end-to-end network session. This level of detail will be necessary in the event of a breach or malware infection.
b. Agency IT Administrators shall periodically assess the controls on personally owned information assets used to connect to State IT infrastructure to ensure the information asset is operating securely before interoperability with agency IT infrastructure is allowed. This is typically accomplished automatically at each connection attempt through a NAC solution which integrates an ability to deny connections made from information assets lacking the required controls.
IV. Remote Access User Requirements
1. State-owned Information Assets to be Used for Network-Level Connections
Telework users shall ensure that all computing equipment which is connected to the state IT infrastructure network for telework purposes are state-owned information assets which have been configured in accordance with secure enterprise and agency standard configurations, including those set forth herein. Telework users shall not connect personally owned information assets to the state IT infrastructure at the network-level unless an approved written exception applies and is implemented in accordance with the additional standards which apply to use of personally owned information assets herein.
2. Web-based Connections
Telework users that connect to state IT infrastructure without network-level access, such as utilizing a web browser to connect to authorized Internet-facing infrastructures (e.g., Outlook Web Access, Novell, Lotus Notes) need not initiate connections from state-owned information assets.
3. Secure Connections
Telework users shall only connect to state IT infrastructure through secure encrypted channels that are authorized by agency management. These channels may include encrypted virtual private networks (VPNs), encrypted web access, encrypted broadband and encrypted dial-up connections. At no time may the telework user initiate two simultaneous connections to different networks (e.g., no split tunneling and no multi-homed connection).
4. Maintaining Security of Information Assets Used for Telework
Just as in the agency main office, security measures cover not only information systems and technology, but all aspects of the information and information systems used by the employee, including paper files, other media, storage devices, and telecommunications equipment (e.g., laptops, Personal Digital Assistants [PDAs], Blackberries and smart cell phones) used in the course of work. Employees must keep government property and information safe, secure, and separated from their personal property and information.
Further, telework users shall adhere to all other information security policies, standards and procedures, regarding the use of state information assets, regardless of the work location including not disabling, altering or circumventing established security controls on state information assets used to connect to state IT infrastructure, such as antivirus and antispyware software, personal firewalls, content filtering software and automatic updates.
5. Protection from Unauthorized Physical Access
Telework users shall ensure that information assets used to telework or connect to state IT infrastructure are physically secured. Telework users must implement the following controls:
i. Protecting information assets from unauthorized access and use by others, including family members, friends and other visitors.
ii. Leaving information assets only in secured locations (e.g., locked cabinet or drawer, locked rooms in locked buildings as applicable and in accordance with the state entity’s information handling policies and procedures) and not in unattended vehicles or other locations where they may be easily stolen.
iii. Using additional physical security controls, such as locking the telework device to a stationary object (e.g., desk or chair) with a computer cable lock, where appropriate.
iv. Using agency approved encryption software to ensure sensitive, personal, and/or confidential information is stored and transmitted securely and not accessible by unauthorized individuals.
v. Using and securely maintaining (e.g., not written down or shared with anyone) strong passwords for all information assets that can be set up to restrict access with a password.
V. Exceptions for Personally Owned Information Assets
1. Exception and risk approval process
a. In the rare situation where it is not possible to use state-owned information assets to establish a network-level connection in order to telework, the agency head, in consultation with the agency Chief Information Officer (CIO) and Information Security Officer (ISO), will consider the increased risk to the state, the agency, and the telework user posed by the telework user connecting to state IT infrastructure with personally-owned information assets. There is increased risk with use of personally owned information assets because, unlike state information assets, they are not managed by IT Administrators dedicated specifically to perform the necessary maintenance. These risks may include, but are not limited to, unauthorized access to other government agency information assets, the comingling of agency information with individual’s personal information on personally owned information assets which must be made available in the litigation hold and e-discovery, public disclosure, and audit processes.
b. If the Agency Head chooses to accept the risk, then the personally owned information assets authorized for use in a telework arrangement must be configured and operated in accordance with the requirements that apply to state-owned assets, and the additional requirements below. The exception and risk approval shall be in writing and maintained for at least two years following the termination of the telework arrangement.
c. Telework users who require assistance in making the configuration changes necessary to meet the following requirements to their personal computing assets may need to seek the assistance of professional computer support/repair services at their own expense. The US-CERT online reading room provides free less technical resources to assist individuals with securing their personal computers and home networks. These are available at: Before You Connect a New Computer to the Internet
2. Additional Training Requirements
a. Agency Management must provide specialized training for telework users who are authorized to use personally owned information assets to connect to state IT infrastructure to educate the user on how to take the security precautions outlined below, including performing software updates and disabling unneeded application features.
3. User Account Passwords
a. Each telework user account shall have a strong password to prevent unauthorized access through password guessing, password cracking software, and other similar techniques used to compromise the telework user account.
4. Networking Configuration
a. Telework users shall ensure that their personally owned information assets are configured to limit network access, including:
  i. Ensure the firewall software included with the computer is turned on and set to block all incoming connections from other computers and outside sources on the Internet.
  ii. Disabling non-essential services, such as file and print sharing.
  iii. Disabling unneeded networking features such as wireless network access features (e.g., IEEE 802.11a/b/g/n, Bluetooth, and infrared).
  iv. Limiting the use of remote access utilities (e.g., for remote technical support) and configuring the information asset to require the remote person to be authenticated before gaining access to the information asset.
  v. Configuring information assets so that they do not automatically attempt to join wireless networks they detect.
5. Attack Prevention
a. Telework users shall ensure that a combination of software and software features are installed and operating on their information assets to prevent attacks, including:
  i. Antivirus and antispyware software.
  ii. Personal firewalls that deny all types of communications that users have not specifically approved as being permitted.
6. Maintain Software Updates
a. Telework users shall ensure that manufacturer recommended security updates and configuration changes are applied regularly to the software on their information assets. Manufacturers will usually release updates for their products following the discovery of a vulnerability. Telework users must watch for critical notices and periodic reminders from the manufacturer and agency about the availability of security updates that fix discovered vulnerabilities and take the actions necessary to apply the security update within the required timeframe so that the telework user’s personally owned information asset is correctly maintained and conforms to these standards. In addition to the operating system, updates shall, at a minimum be applied to the following types of software as soon as they become available:
  i. Web browsers (program that facilitates access to the Internet, such as Internet Explorer, Mozilla Firefox, etc.).
  ii. Email clients (software and a service that facilitates email communication, such as Outlook, Lotus Notes, etc.).
  iii. Instant messaging clients (software and a service that facilitates instant voice chat and text chat communications and file sharing, such as AIM, ICQ, Jabber, etc.).
  iv. Antivirus and antispyware software (software that detects and blocks malicious code).
  v. Personal firewalls (software and/or hardware that allows the user to define access policies for inbound connections to the computer they are protecting and outbound services the computer is authorized to access).
  vi. Content filtering software (software that blocks access to certain websites and services).
b. Telework users shall review manufacturer documentation for each software program their information asset contains in these categories to determine each program’s update capabilities and enable automatic updates where possible.
7. Secure Application Configurations
i. Telework users shall configure their applications (typically this can be accomplished through the “Tools” and “Options” in the application, though it may vary by manufacturer and application) to decrease risk and to support security, including:
ii. Generally:
  i. Disabling unneeded application features and configuring applications to stop or block activity that is likely to be malicious (the more applications installed and more application features enabled, the greater the security risk and maintenance responsibility);
  ii. Avoiding downloading and installing software if the software is not provided by either the agency, the information asset’s manufacturer or a reputable vendor.
iii. Web browsers:Email clients:
  i. Restricting Web browser cookies (small data files created by a Web server that is stored on the computer either temporarily for that session only [session cookie] or permanently on the hard disk [persistent cookie]. Cookies are a concern because they can be set to store personal information, including user login ids and passwords).
  ii. Blocking pop-up windows (a small window that is displayed on top of an existing open window or application).
  iii. Enabling phishing (type of scam) filtering (software that can detect specific patterns in email as a potential scam and either delete or send to a folder for further review) capabilities.
  iv. Removing unneeded browser plug-ins (a small program that enhances the capabilities of a larger software program, usually associated with image editing, or audio or video programs).
  v. Protecting sensitive information stored by the browser (e.g., passwords).
  vi. Preventing website passwords from being saved by the browser and recalled automatically during the logon process.
  vii. Running browsers with the fewest privileges possible by limiting options and disabling unnecessary features, (e.g., disabling Java© and JavaScript, disabling pop-ups and not loading images automatically).
iv. Email clients:
  i. Preventing automatic loading of remote email images.
  ii. Limiting mobile code execution (e.g., disabling Active X, Java© and JavaScript where possible).
  iii. Setting default message reading format and sending format to plain text.
  iv. Disabling automatic previewing and opening of email messages.
  v. Enabling spam (unsolicited email) filtering.
v. Instant messaging client:
  i. Preventing automatic loading of remote email images.
  ii. Restricting file transfers.
vi. Office productivity applications:
  i. Restricting macro (a special purpose command that provides a short-cut for a sequence of repeatable keystrokes or actions) use to permit macros only from trusted locations or which prompt the user to approve or reject each attempt to run a macro.
  ii. Limiting personal information, such as name, initials, mailing address, and phone number, stored with each document created to that which is specifically required.
  iii. Using secured folders for saving documents and holding temporary files, including auto- save and backup copies of documents.
  iv. Automatically and/or manually deleting documents which are no longer required.
8. Remote Access Software Configuration
a. If telework users are required to install remote access software onto their information assets or configure software built into the information asset’s operating system, this software shall be configured based on the agency’s requirements and recommendations. Remote access software shall be configured so that only the necessary functions are enabled. Telework users shall also ensure that whenever updates to the remote access software are available, that they are acquired and installed. If the agency provides the updates, the telework user shall take the appropriate action (such as install the update) in a timely manner when updates are available.
9. Security Maintenance and Monitoring
a. Telework users shall maintain their information assets’ security on an ongoing basis, at a minimum once a month, including:
  i. Confirming periodically that the operating system and primary applications are up to date.
  ii. Checking the status of security software periodically to ensure that it is still enabled, configured properly, and up to date.
  iii. Creating a new user account whenever another individual needs to start using the information asset, as well as disabling or deleting a user account whenever the associated individual no longer needs to use the information asset. All the user accounts shall be reviewed periodically to ensure that only the necessary accounts are enabled.
  iv. Changing the user’s system account and remote access passwords regularly.
  v. Periodically checking for potential security issues on the information asset (e.g., running utilities that check the computer for potential problems).
  vi. Investigating any cases in which the information asset begins to display unusual behavior.
VI. Restrictions and Security with Use of Third-Party Devices
Telework users shall consider the security risks related to the environment/location of a third- party device (e.g., public kiosks, such as hotel business centers) before deciding whether to use it. Users shall also consider who is responsible for securing a third-party device and who can access the device.
Teleworkers may check email via a Web-based connection (such as, OWA, Novell, and Lotus Notes) from public kiosks; however, telework users shall not use any third-party devices for performing sensitive functions or accessing confidential, personal or sensitive information.
VII. Securing Personal Networks
a. Personal networks can be wired or wireless. A wired network requires use of a cable between the computing device and cable modem. The telework user shall take the following precautions before connecting to a state agency IT infrastructure from an information asset attached to a wired personal network:
  i. Separate the personal network from the Internet Service Provider’s (ISP) network with a security device between the two, such as a broadband router, cable modem router, DSL router or a firewall appliance capable of enforcing the required network security policy.
  ii. This security device shall be configured to prevent computers outside the personal network from initiating communications with any of the devices on the personal network, including the telework device.
  iii. A firewall appliance or broadband router shall also be used to provide an additional layer of security, even if each device uses a personal firewall.
  iv. When installing and configuring firewall appliances or broadband routers, users shall perform the security precautions described in the manufacturer’s documentation, including:
  v. Changing default passwords on the device.
  vi. Configuring the device so that it cannot be administered from outside the personal network.
  vii. Configuring the device to silently ignore unsolicited outside connection attempts unless properly authenticated access is required by the ISP to support necessary communications with the IP’s infrastructure.
  viii. Checking for software updates and applying them periodically, as explained in the manufacturer’s documentation―either automatically (typically daily or weekly) or manually (to be performed by the user at least monthly).
  ix. For broadband routers, turning off or disabling built-in wireless access points (AP) which are not used.
2. Securing Wireless Personal Networks
a. A wireless network uses electromagnetic waves instead of a cable to carry the signal over the communication path. The telework user shall take the following precautions before connecting to state agency IT infrastructure from an information asset attached to a wireless personal network:
  i. Use strong encryption over the wireless network to protect communications. Configure the wireless network to use one of the following security protocols in order of decreasing preference:
    a. Wi-Fi Protected Access 2 (WPA2), with Advanced Encryption Standard (AES).
    b. WPA with AES.
    c. WPA with Temporal Key Integrity Protocol (TKIP). (WEP is NOT an authorized encryption protocol)
  ii. Use a long and complex key length.
  iii. Only permit access for specified wireless network cards.
  iv. Change the default service set identifier (SSID).
  v. Disable SSID broadcasts from the wireless access point.
  vi. Disable Access Point (AP) administration through wireless communications.
  vii. Change the default administrative password to a unique strong password.

## Curator notes

Text taken from the California Department of Technology's web page for the instrument: from the page heading to the end of the page's content, one line per paragraph, heading, list item and table row (a table row's cells are joined by ' | '), with markup, the site menu, the side navigation, the page's contents list ('On this page'), the print button, scripts, the footer and non-breaking spaces removed.
