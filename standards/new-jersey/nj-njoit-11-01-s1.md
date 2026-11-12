---
schema_version: 1
corpus: states-government-it
jurisdiction: new-jersey
id: nj-njoit-11-01-s1
title: Remote Access Standard
doc_type: standard
citation: NJOIT Technology Circular 11-01-S1-NJOIT
authority_level: ''
issuing_body: New Jersey Office of Information Technology
source_url: https://www.nj.gov/it/docs/ps/11-01-S1-NJOIT_Remote_Access_Standard.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 34600bac65c4348fb7a00f53b407d097b2a1134cb55a10e6dcdfa2845612fa86
effective_date: '2011-07-20'
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

# Remote Access Standard (NJOIT Technology Circular 11-01-S1-NJOIT)

## At a glance

The standards for remotely connecting to the State's Garden State Network. Its parent procedure, 11-01-P1-NJOIT, is listed without a link (a stub below).

## Full text

                  NJ OFFICE OF INFORMATION TECHNOLOGY               P.O. Box 212                   www.tech.nj.gov
                  Philip D. Murphy, Governor                        300 Riverview Plaza
                  Christopher J. Rein, Chief Technology Officer     Trenton, NJ 08625-0212

                                                                  POLICY NO:
                STATE OF NEW JERSEY                                               11-01-S1-NJOIT
               TECHNOLOGY CIRCULAR                                SUPERSEDES:                EFFECTIVE DATE:
                                                                             NA                  07-20-2011
              179-01 Remote Access                                VERSION:                   LAST REVIEWED:
                    Standard                                                   2.0               07-10-2025

1.      PURPOSE
        The purpose of this document is to establish the standards for remotely connecting to the State of New
        Jersey’s Garden State Network (“GSN”). The issuance of this standard is to minimize the potential
        expose to the GSN from unauthorized access, loss of sensitive or confidential information, and/or
        damage to the State of New Jersey’s critical internal systems, and information technology assets.

2.      AUTHORITY
        The standard is established under the authority of State of New Jersey P.L.2007.c.56.

        New Jersey Statutes Annotated (N.J.S.A.), Sections C.52:18A-224 through C.52:18A-234, known as “The
        Office of Information Technology Reorganization Act."

3.      SCOPE
        This standard applies to all State of New Jersey Department, Agencies, their employees, contractors,
        consultants, temporary employees, and other workers including all personnel affiliated with third
        parties remotely utilizing access to the State of New Jersey information technology assets and the GSN.

4.      RESPONSIBILITIES
        Administrative Directors working in conjunction with the agency IT Directors shall be responsible for
        ensuring the effective implantation of statewide information technology circulars.

5.      STANDARD
        All State entities and all Authorized Users who will participating in the utilization of Remote Access
        privileges must adhere to the standards outlined below:

11-01-S1-NJOIT, Remote Access Standard                                                                          Page 1 of 3

        5.1.    Remote Access users will be authenticated by use of the State’s multi factor authentication: 1)
                a unique User ID 2) a password and 3) an approved Authentication Security Device and a
                random security code.

        5.2.    Remote Access Authorized Users will be automatically disconnected from the State of New
                Jersey GSN after thirty minutes of inactivity. The Authorized User must then log on again to
                reconnect to the GSN. A single session will be limited to a maximum connection time of 24 hours.
                The Authorized User must then log on again to reconnect to the GSN.

        5.3.    Split tunneling is NOT permitted with Remote Access; only one network connection is allowed.

        5.4.    State owned devices: State of New Jersey employees must use approved devices, including
                personal computers when connecting to the State of New Jersey GSN via any approved Remote
                Access technology.

        5.5.    Non-State owned devices: By using Remote Access technology, Authorized Users must
                understand that their devices, when connected to the GSN become a de facto extension of the
                State of New Jersey’s GSN. While connected to the GSN through Remote Access technology, all
                devices are subject to the same usage, security rules, and regulations that apply to the State of
                New Jersey’s owned equipment, i.e., their devices must be configured to comply with this
                standard, and all other related State IT circulars and policy directives related to using the GSN.
                The State of New Jersey is not responsible for supporting or maintenance of a personal device.

        5.6.    Virtual Private Network (VPN) method: When actively connected to the GSN, Remote Access
                connections will force all traffic from and to the device over the Remote Access tunnel; all other
                traffic (i.e Internet connections) not destined for the GSN will be dropped. Internet use and
                access within the GSN will be controlled through the Authorizing Entity’s Proxy and Internet
                Filtering system.

        5.7.    Minimum Security Standards

                The minimum security standards for protecting a device including a computer is based on the
                potential security threats.

                5.7.1. The software products should not be limited to just anti-virus software, but other
                       solutions to prevent spyware or malware and intrusions.

                5.7.2. Identify and locate the device and if necessary, wipe the media remotely if lost or
                       stolen.

                5.7.3. Protect the device’s media by encrypting the media.

11-01-S1-NJOIT, Remote Access Standard                                                                  Page 2 of 3

                5.7.4. The use of supported operating systems, software and web browser with the ability
                       to receive updates.

                                                 Desktop   Laptops   Mobile Devices
                             Anti-Virus             X         X            X
                             Anti-malware           X         X
                             Firewall               X         X
                             Intrusion Detection    X         X
                             Remote wipe                      X            X
                             Theft Locator                    X            X
                             Encryption                       X            X
                             Manufacturer Supported
                                Operating system    X        X             X
                                        Software    X        X             X
                                     Web Browser    X        X             X

6.      EXCEPTIONS AND NON-COMPLIANCE
        Any exceptions to this standard will be reviewed by the Statewide Remote Access
        Subcommittee Group and require approval from the Statewide Office of Information Security.

11-01-S1-NJOIT, Remote Access Standard                                                             Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
