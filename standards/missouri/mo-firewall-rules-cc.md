---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-firewall-rules-cc
title: Firewall Rules
doc_type: standard
citation: 'Security Domain Compliance Component: Firewall Rules'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallRulesARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 6116422ce4366bc219eab4c7258ddb99cb1a68f6c96e9bda0b5de50d713ca3b4
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

# Firewall Rules (Security Domain Compliance Component: Firewall Rules)

## At a glance

Row 'Firewall Rules' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/firewall-rules-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/08/2004. The index lists it as an approved standard.

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
Name                   Firewall Rules
                       Firewall Rules describe how security policy will be implemented by the firewall
                       and associated security mechanisms. The rules dictate how a firewall should
Description            handle traffic such as web, email, or telnet. The rules also describe how the
                       firewall is to be managed and updated. The contents of these rule sets
                       determine the actual functionality of a firewall.
                       The firewall itself may become a security problem if there are no rules to guide
Rationale
                       firewall implementation and administration.
                       • Enforces security policies
                       • Protects internal networks from exploitation of vulnerabilities from outside
                           entities and vice versa
Benefits               • Helps the organization establish trust with external connections
                       NOTE:
                       • Requires continual monitoring and updating to be effective
                       • Rules are often complex and may slow the throughput
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
List the Technology Area Name   Secure Gateways and Firewalls
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
                                •    A risk analysis must be performed before firewall rules can be
                                     created.
                                •    General rules should be kept as simple as possible, so as not to
                                     accidentally introduce holes that might allow unauthorized or
                                     unwanted traffic.
State the Guideline, Standard
or Legislation                  •    The general rule for handling inbound traffic should be to block all
                                     packets and connections unless the traffic type and connections
                                     have been specifically permitted.
                                •    Exceptions to the general firewall rules should be as specific as
                                     possible with regards to the network traffic they control.
                                •    The firewall rules should block the following types of traffic:
                                             o   Inbound traffic from a non-authenticated source system

        with a destination address of the firewall. (This type of
        packet normally represents some type of probe or attack
        against the firewall.)
    o   Inbound traffic with a source address indicating that the
        packet originated on a network behind the firewall. (This
        type of packet likely represents some type of spoofing
        attempt.)
    o   Inbound traffic containing Internet Control Message
        Protocol (ICMP) traffic. (ICMP can be used to map the
        networks behind certain types of firewalls.)
    o   Inbound or outbound traffic from a source address that
        falls within the address ranges set aside in RFC 1918 for
        private networks. (Such traffic typically indicates a
        denial-of-service attack.)
    o   Inbound traffic from a non-authenticated source system
        containing Simple Network Management Protocol (SNMP)
        traffic. (These packets can indicate that an intruder is
        probing a network.)
    o   Inbound traffic containing IP Source Routing information.
        (Source Routing has the potential to permit an attacker to
        construct a network packet that bypasses firewall
        controls.)
    o   Inbound or outbound network traffic containing a source
        or destination address of 127.0.0.1 or 0.0.0.0. (Some
        operating systems interpret these addresses as either
        local host or as a broadcast address, and these packets
        can be used for attack purposes.)
    o   Inbound or outbound traffic containing directed broadcast
        addresses.
    o   Executable files that should be considered for blocking
        include the following:
        .ade .cmd .eml .ins .mdb .mst .reg .url .wsf
        .adp .com .exe .isp .mde .pcd .scr .vb .wsh
        .bas .cpl .hlp .js .msc .pif .sct .vbe
        .bat .crt    .hta .jse .msi .pl .scx .vbs
        .chm .dll    .inf .lnk .msp .pot .shs .wsc
o   The following services and applications traffic thus should be
    blocked inbound by that policy, with exceptions noted.

     Application                 Port Numbers                               Action
                        telnet - 23/tcp                     restrict w/strong authentication
                        SSH - 22/tcp                        restrict to specific systems
    Login services      FTP - 21/tcp                        restrict w/strong authentication
                        NetBIOS - 139/tcp                   always block
                        R services - 512/tcp - 514/tcp      always block

                        portmap/rpcbind - 111/tcp/udp       always block
    RPC and NFS         NFS - 2049/tcp/udp                  always block
                        Locked - 4045/tcp/udp               always block

                        135/tcp/udp                         always block
                        137/udp                             always block
    NetBIOS in
                        138/udp                             always block
    Windows NT
                        139/udp                             always block
                        445/tcp/udp in Windows 2000         always block

     X Windows          6000/tcp - 6255/tcp                 always block

                        DNS - 53/udp                        restrict to external DNS servers
Naming Services         DNS zone transfers - 53/tcp         block unless external secondary
                        LDAP - 389/tcp/udp                  always block

                        SMTP - 25/tcp                       block unless external mail relays
         Mail           POP - 109/tcp and 110/tcp           always block
                        IMAP - 143/tcp                      always block

                        HTTP - 80/tcp and SSL 443/tcp block unless to public web servers
        Web             may also want to block common high-order HTTP port choices –
                        8000/tcp, 8080/tcp, 8888/tcp, etc.

                        ports below 20/tcp/udp              always block
"Small Services"
                        time - 37/tcp/udp                   always block

                        TFTP - 69/udp                       always block
                        finger - 79/tcp                     always block
                        NNTP - 119/tcp                      always block
                        NTP - 123/tcp                       always block
                        LPD - 515/tcp                       always block
    Miscellaneous
                        syslog - 514/udp                    always block
                        SNMP - 161/tcp/udp,
                                                            always block
                        162/tcp/udp
                        BGP - 179/tcp                       always block
                        SOCKS - 1080/tcp                    always block

                        block incoming echo request (ping and Windows traceroute)
                        block outgoing echo replies, time exceeded, and destination
        ICMP            unreachable messages except "packet too big" messages (type 3,
                        code 4). This item assumes that you are willing to forego the legitimate
                        uses of ICMP echo request to block some known malicious uses.

•     Firewall rules should be reviewed and updated at least twice per
      year, or whenever there are any enterprise computing environment
      modifications, or after any significant security incident. Both of the
      following methods should be used to review the firewall rules.
                o    Obtain hardcopies of the current firewall configurations
                     and compare these against the expected configuration

                                                  based on the rules.
                                            o     Verify the configuration of a device by attempting to
                                                  perform operations that should be prohibited.

Document Source Reference #    NIST Special Publication 800-41
                                                Standard Organization
Name                           NIST                                Website        www.csrc.nist.gov
Contact Information            inquiries@nist.gov
                                                  Government Body
                               National Institute of
                               Standards and Technology
Name                           (NIST), Computer                    Website        www.csrc.nist.gov/publications/
                               Security Resource Center
                               (CSRC)
Contact Information            inquiries@nist.gov
                                                    KKEEYYW
                                                          WOORRD
                                                               DSS
                               Filter, packets, Simple Network Management Protocol (SNMP), traffic,
List all Keywords
                               configuration, risk assessment, routing, directed broadcast
                                      C
                                      COOM
                                         MPPO
                                            ONNEEN
                                                 NTT C
                                                     CLLA
                                                        ASSSSIIFFIIC
                                                                   CAATTIIO
                                                                          ONN
Provide the Classification       Emerging                Current                Twilight         Sunset
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
Provide the Current Status)      In Development          Under Review           Approved         Rejected
                                                   A
                                                   AUUD
                                                      DIITT TTRRA
                                                                AIILL
Creation Date                  05/27/2004                   Date Accepted / Rejected       06/08/2004
     Reason for Rejection
Last Date Reviewed                                          Last Date Updated
     Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
