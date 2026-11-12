---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-network-based-ids-cc
title: Network Based IDS
doc_type: standard
citation: 'Security Domain Compliance Component: Network Based IDS'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-NetworkBasedIDS.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 6e68c63a844ca771cb9f61412e73021b33faada96398492824557fbbabee705f
effective_date: null
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

# Network Based IDS (Security Domain Compliance Component: Network Based IDS)

## At a glance

Row 'Network Based IDS' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/network-based-ids-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 5/14/2003. The index lists it as an approved standard.

## Full text

                                             C
                                             Coom
                                                mpplliiaannccee C
                                                                Coom
                                                                   mppoonneenntt

                                                    D
                                                    DEEFFIIN
                                                           NIITTIIO
                                                                  ONN
Name                   Network-Based Intrusion Detection Systems (NIDS)
                       Network-Based Intrusion Detection Systems (NIDS) detect attacks by capturing
                       and analyzing network traffic. NIDS are dedicated software or hardware
                       systems that “sit” on a network and analyze network packets.
Description
                       NIDS often consist of a set of single-purpose sensors placed at various points in
                       a network. These sensors monitor network traffic, performing local analysis of
                       that traffic and reporting attacks to a centralized console.

                       The first step in delivering an efficient and secure network intrusion protection
                       strategy is accurately detecting all possible threats. To achieve this goal,
                       multiple detection methods should be employed to ensure comprehensive
                       coverage.
Rationale
                       The failure to secure State of Missouri networks with NIDS puts agencies at a
                       much greater risk of loss. A single attack can cost millions of dollars in time
                       spent recovering from the attack and liability for compromised data and
                       hardware. The damage from an attack to State of Missouri services can also
                       include inconvenience to citizens and the loss of public confidence.
                       • NIDS identify and prevent security threats from compromising secure
                           networks.
                       •   The deployment of NIDS has little impact on network performance. NIDS
Benefits                   are usually passive devices that listen on a network without interfering with
                           the normal operation of a network.
                       •   NIDS can be made very secure against attack and even made invisible to
                           many attackers.
                                    A
                                    ASSSSO
                                         OCCIIA
                                              ATTEED
                                                   DAARRC
                                                        CHHIITTEEC
                                                                 CTTU
                                                                    URREE LLEEVVEELLSS
List the Domain Name            Security
List the Discipline Name        Technical Controls
List the Technology Area Name   Intrusion Detection Systems
List Product Component Name
                                      C
                                      COOM
                                         MPPLLIIA
                                                ANNC
                                                   CEE C
                                                       COOM
                                                          MPPO
                                                             ONNEEN
                                                                  NTT TTYYPPEE
Document the Compliance
                                Guideline
Component Type
Component Sub-type
                                              C
                                              COOM
                                                 MPPLLIIA
                                                        ANNC
                                                           CEE D
                                                               DEETTA
                                                                    AIILL
                                General NIDS Requirements
State the Guideline, Standard
or Legislation                  •    Administrators shall be trained on the IDS before implementation.
                                     Despite vendor claims of ease of use, training and/or experience are

    necessary to manage any IDS.
•   It is preferred to have the NIDS controlled directly from a central
    location(s). However, the NIDS may be agent-based where
    response decisions are made at the agent.
•   IDS administrators shall be able to create or change policies easily.

NIDS Deployment Requirements
•   NIDS shall be deployed in conjunction with Host-Based IDS to fully
    protect the system.
•   It is recommended that organizations install the NIDS first on critical
    networks. Once administrators are familiar with the NIDS, it may be
    installed on the remainder of the organization’s networks.
•   NIDS shall be installed on any Network where sensitive or critical
    information is transmitted.
•   It is preferred to install IDS Management software on a dedicated
    system in the target networks being monitored.
•   It is preferred to have the NIDS use an agent-manager (server)
    architecture, where policy is created and modified on the manager
    and automatically distributed to all agents.
•   It is preferred that Server agents poll the manager at periodic
    intervals for policy changes or new software updates.

NIDS Analysis Requirements

•   NIDS shall utilize information from operating system audit trails and
    system logs.
•   NIDS shall have easy-to-use tools to analyze the logs.
•   NIDS shall detect, and preferably prevent, the following:
    •   System scanning (probing the target with different kinds of
        packets to garner information about the system, such as
        topology, active systems, operating systems and software in
        use),
    •   Denial of Service (DoS) (slow or shut down targeted systems or
        hosts), and
    •   Penetration (unauthorized acquisition and/or alteration of system
        privileges, resources, or data).
•   NIDS shall use Misuse Detection methods (matching a predefined
    pattern of events describing an attack) and may include Anomaly
    Detection (abnormal, unusual behavior) components.
•   Administrators shall follow a schedule for checking the results of the
    NIDS to ensure attackers have not modified the system.

NIDS Response Requirements
•   NIDS shall respond in real-time.
•   It is preferred that IDS provide active responses to intrusions by:
    •   Collecting additional information:

        •   Turning up the number of events logged, or
        •   Capturing all packets, not just those targeting a particular
            port or system.
    •   Changing the environment:
        •   Terminating the connection, or
        •   Reconfiguring routers and firewalls to:
            •   Block packets from the intruder’s IP address,
            •   Block network ports, protocols or services, or
            •   Sever all connections that use certain network interfaces.
•   NIDS administrators shall work closely with router and firewall
    administrators when creating rules for routers and firewalls to
    ensure intruders cannot abuse the feature to deny access to
    legitimate users.
•   NIDS may provide passive responses requiring subsequent human
    action to intrusions by:
    •   Generating alarms and notifications with popup windows, cellular
        phones, pagers and email, or
    •   Reporting alarms and alerts using SNMP traps and plug-ins to
        central network management consoles.
•   All NIDS communications shall be secure and use encrypted tunnels
    or other cryptographic measures.
•   NIDS shall create output with the following information for each
    intrusion detected:
    •   Time/date
    •   Sensor IP address
    •   Specific attack name
    •   Source and destination IP addresses
    •   Source and destination port numbers
    •   Network protocol used
    •   Description of the attack type
    •   Attack severity level
    •   Type of loss expected
    •   Type of vulnerability exploited
    •   Input validation (buffer overflow or boundary condition)
    •   Access validation (faulty access control mechanism)
    •   Exceptional condition
    •   Environmental (unexpected interaction with an application and
        the operating system or between two applications)
    •   Server Configuration
    •   Race (delay between the time a system checks to see if an
        operation is allowed and the time it performs the operation)

                                   •    Design
                                   •    Software types and versions vulnerable
                                   •    Patch information to counter the attack
                                   •    References to advisories about the attack or vulnerability
                               •   It is preferred that NIDS reports combine redundant attack entries
                                   and make attacks of highest importance stand out.

                               NIST SP 800-31 (www.csrc.nist.gov/publications/nistpubs)
                               Intrusion Detection Systems (IDS),

Document Source Reference #    NIST SP 800-18 (www.csrc.nist.gov/publications/nistpubs)
                               CERT Guide to System and Network Security Practices
                               (www.cert.org/security-improvement/)

                                               Standard Organization
Name                                                              Website
Contact Information
                                                 Government Body
                               National Institute of
                               Standards and Technology
                                                                              http://csrc.nist.gov/
Name                           (NIST), Computer                   Website
                               Security Resource Center
                               (CSRC)
Contact Information            inquiries@nist.gov
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
                               Honey Pot, intrusion, cracker, buffer overflows, passwords, sniffing,
List all Keywords
                               exploit, denial-of-service, Java, ActiveX, SMURF, DNS, probes
                                       C
                                       COOM
                                          MPPO
                                             ONNEEN
                                                  NTT C
                                                      CLLA
                                                         ASSSSIIFFIIC
                                                                    CAATTIIO
                                                                           ONN
Provide the Classification         Emerging             Current             Twilight      Sunset
                                   Rationale for Component Classification
Document the Rationale for
Component Classification
                                          Conditional Use Restrictions
Document the Conditional Use
Restrictions
                                                 Migration Strategy
Document the Migration
Strategy
                                              Impact Position Statement
Document the Position
Statement on Impact

                                            C
                                            CUURRRREEN
                                                     NTT SSTTA
                                                             ATTU
                                                                USS
Provide the Current Status)     In Development         Under Review           Approved     Rejected
                                                 A
                                                 AUUD
                                                    DIITT TTRRA
                                                              AIILL
Creation Date                 04/03/2003                  Date Accepted / Rejected   5/14/2003
    Reason for Rejection
Last Date Reviewed                                        Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
