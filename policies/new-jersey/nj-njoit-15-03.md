---
schema_version: 1
corpus: states-government-it
jurisdiction: new-jersey
id: nj-njoit-15-03
title: Firewall Management Policy
doc_type: policy
citation: NJOIT Technology Circular 15-03-NJOIT
authority_level: ''
issuing_body: New Jersey Office of Information Technology
source_url: https://www.nj.gov/it/docs/ps/15-03-NJOIT_165-Firewall_Management_Policy.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: d134456a9ce648ff0df4b8b3800505f77e948297c78fa8cae72c4204d287adc9
effective_date: '2015-01-22'
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Firewall Management Policy (NJOIT Technology Circular 15-03-NJOIT)

## At a glance

Requirements for managing the electronic firewalls that protect the State's systems and infrastructure.

## Full text

             NJ OFFICE OF INFORMATION TECHNOLOGY                P.O. Box 212          www.tech.nj.gov
            Philip D. Murphy, Governor                          300 Riverview Plaza
            Christopher J. Rein, Chief Technology Officer         Trenton, NJ 08625-0212

                                                          POLICY NO:

           STATE OF NEW JERSEY                                  15-03-NJOIT
         TECHNOLOGY CIRCULAR                              SUPERSEDES:              EFFECTIVE DATE:
                                                                N/A                01-22-2015
    165-Firewall Management
             Policy                                       VERSION:                 LAST REVIEWED:
                                                              2.0                  02-10-2025

ATTN: Directors of Administration and Agency IT Managers

1       PURPOSE

        The purpose of this policy is to establish requirements for managing electronic firewalls
        that protect the State of New Jersey’s systems and infrastructure. This policy is designed
        to assist IT administrators in establishing strict rules for firewall configuration and
        management. It aims to prevent the risk of unauthorized access to networks, loss of
        sensitive or confidential information, and/or damage of the State of New Jersey’s critical
        internal systems and information technology assets.

2       AUTHORITY
        New Jersey Statutes Annotated (N.J.S.A.), Sections C.52:18A-224 through C.52:18A-234,
        known as “The Office of Information Technology Reorganization Act."

        NJOIT reserves the right to change or amend this Policy to comply with changes in
        Agency procedures. Any changes or amendments will be announced and made available
        on NJOIT’s intranet under Policies. Changes in this Policy will be effective upon such
        publication or distribution and will not require employee sign-off.

3       SCOPE

        This policy applies to all State of New Jersey Departments, Agencies, State Authorities,
        “in but not of” entities, their employees, contractors, consultants, temporary employees,

15-03-NJOIT, 165-Firewall Management Policy                                                      Page 1 of 5

        and other workers including all personnel who are responsible for managing and
        protecting the State of New Jersey resources, systems, and infrastructure.

4       DEFINITIONS

        Please refer to the Statewide Policy Glossary at NJOIT Intranet | Glossary (state.nj.us).

5       POLICY

        The following requirements provide a policy for managing a firewall connected to the
        State of New Jersey's networks:
        5.1.1   A baseline firewall configuration shall be created for each firewall. Changes to the
                firewall device's hardware, software, or operating environment as well as any
                modification to the rule base shall be documented in accordance with the SISM
                CM-04 Configuration Change Control. Firewall configuration changes shall be
                backed up and secure copies maintained.

        5.1.2   Firewall rule submissions and configuration changes are to be scheduled. The OIT
                schedule for submission is 3 p.m. on Friday and, for configuration changes, the
                following Wednesday.

        5.1.3   Emergency firewall rules must be approved by the Deputy CTO for OIT's
                Infrastructure Support Services and the Manager for OIT's Statewide Office of
                Information Security (SOIS).

        5.1.4   Agencies are to identify personnel who are authorized to submit firewall rules on
                the agency's behalf and provide a list to the manager of OIT's SOIS.

        5.1.5   Firewall rules are to be reviewed yearly and removed if no longer required.

        5.1.6   All State firewalls shall be configured to "deny by default" and block all traffic that
                has not been expressly permitted by firewall policy.

        5.1.7   All State firewall policies should be based on source and destination as well as
                content and sensitivity of the traffic. A standard configuration will be developed
                and implemented under the direction of the State's Information Security Officer.

15-03-NJOIT, 165-Firewall Management Policy                                                 Page 2 of 5

        5.1.8    Traffic inbound to the State's networks containing ICMP (Internet Control Message
                 Protocol) traffic will be blocked at the perimeter.

        5.1.9    IPsec or SSL Virtual Private Networks (VPN's) should be used to authenticate users
                 by firewalls utilizing an identity policy.

        5.1.10   An explanation of each rule should be included with its rule base entry.

        5.1.11 Firewalls should have an inactivity network disconnect associated with its firewall
               policy and that time period of inactivity is up to the discretion of the agency and
               the application requirements. Firewall default is set to 60 seconds.
        5.1.12 Management logging and auditing shall be implemented on all firewall devices
               that support logging and auditing. Log events must be forwarded to the State's
               Security Incident Event Management (SIEM) system. Firewalls must utilize an
               authentication mechanism (i.e. AAA authentication, TACACS, Radius
               Authentication) that provides accountability for the user and accessibility through
               a secure channel (i.e. SSH).
        5.1.13 All firewalls should record their traffic, especially blocked traffic, and this data
               should be reviewed regularly.
        5.1.14 All State firewalls shall be physically secured by being installed in an access­
               controlled area. Access to the firewalls shall be limited to the appropriate Agency
               Wide Area Network (WAN) security administrators.
        5.1.15 All Agencies shall utilize dedicated hardware devices for firewall protection to
               ensure that all confidential, proprietary and/or sensitive information is secure
               within the state's networks. Firewalls shall conform to the ICSA Labs compliance
               criteria, Version 4.0 or the latest version.

6       ROLES AND RESPONSIBILITIES

        The State of New Jersey

        6.1.1    The Wide Area Network Unit within the Office of Information Technology
                 will confgure and manage the State's frewalls in accordance with best
                 practices and industry standards in order to protect the state's networks.
                 Department and Agency staff members are responsible for the
                 management of agency frewalls, unless an agreement has been made with

15-03-NJOIT, 165-Firewall Management Policy                                                 Page 3 of 5

                Oil's WAN unit for management of said device(s). Any Departments, Agencies,
                State Authorities, "in but not of" entities, requiring deviations from the
                standard confguration must formally request these changes and take
                responsibility to provide compensating controls to ensure the security of
                the state's networks.

        6.1.2   The Statewide Information Security Office within the Office of Information
                Technology will set up and manage the authentication of frewalls and
                perform the administrative functions in order to maintain the lifecycle
                management processes in accordance with best practices and industry
                standards.

        6.1.3   The Statewide Cyber Security Threat Mitigation Committee (CSTMC) will
                approve, publish, and update the security standards under the guidance of the
                State's Information Security Officer.

7       ENFORCEMENT

        Any firewall Authorized User found to have violated this policy may be subject to
        disciplinary action by the appropriate department or agency, and loss of firewall
        management privileges. IN ADDITION, VIOLATORS MAY BE SUBJECT TO CRIMINAL
        PROSECUTION, CIVIL LIABILITY, OR BOTH FOR UNLAWFUL USE OF ANY ACCESS.

8       EXCEPTIONS AND NON-COMPLIANCE

        Departments and Agencies shall comply with this policy within 90 days of its effective
        date.
        Requests for exceptions for non-compliance with this policy shall be processed in
        accordance with Statewide IT Circular 08-02-NJOIT. 111 - Information Security Managing
        Exceptions.

9       Administration

        This Policy is administered and monitored by the CTO at 300 Riverview Plaza, Trenton,
        NJ 08625.

15-03-NJOIT, 165-Firewall Management Policy                                           Page 4 of 5

           The Policy must be reviewed annually; however, the CTO reserves the right to change
           or amend the Policy at any time.

            Signature on File                                           02/10/2025
          Christopher J. Rein, Chief Technology Officer                   Date

   10      DOCUMENT HISTORY

Version      Published          CTO       Sections Modified      Description of Modifications
               Date
  1.0       01/22/2015                                            Original Published Date
  2.0       02/10/2025        C. Rein            All                      Format

   15-03-NJOIT, 165-Firewall Management Policy                                       Page 5 of 5

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
