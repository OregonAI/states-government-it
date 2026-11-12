---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-personal-firewalls-cc
title: Personal Firewalls
doc_type: standard
citation: 'Security Domain Compliance Component: Personal Firewalls'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallsPersonalARC.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 953850ed911a185784d0df430b695301e42146fa6e7f8b8c18cd676ad6fbdf14
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

# Personal Firewalls (Security Domain Compliance Component: Personal Firewalls)

## At a glance

Row 'Personal Firewalls' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/personal-firewalls-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/24/2004. The index lists it as an approved standard.

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
Name                   Personal Firewalls
                       Personal Firewalls are devices or systems that control the flow of traffic between
Description            a network (including wireless network) and a personal computing device or a
                       small network.
                       Securing personal computers at remote locations is as important as securing
                       them at the office. People who telecommute or access agency systems
                       remotely must protect their systems and the data. Users accessing external
                       networks should have personal firewall protection. Other networks and Internet
Rationale
                       Service Providers (ISPs) cannot be relied upon to provide adequate firewall
                       protection. Therefore, personal firewalls have been developed to provide
                       protection for remote systems and to perform many of the same functions as
                       larger firewalls.
                       • Provide protection when connecting to external networks, or from internal
Benefits                   network threats.
                       • Can be used as an endpoint for a Virtual Private Network (VPN).
                                    A
                                    ASSSSO
                                         OCCIIA
                                              ATTEED
                                                   DAARRC
                                                        CHHIITTEEC
                                                                 CTTU
                                                                    URREE LLEEVVEELLSS
List the Domain Name            Security
List the Discipline Name        Technology Controls
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
                                •    Personal Firewalls shall be used on all personal computing devices
                                     that can be connected to any untrusted network.
                                •    Personal Firewalls shall be able to:
                                        o Control ports and protocols that applications use,
                                        o Work with local area network (LAN), Point-to-Point Protocol
                                          Over Ethernet (PPPoE), VPN, and dial-up connections,
State the Guideline, Standard
                                        o Specify the systems or networks with which programs can
or Legislation
                                          communicate (i.e., create trusted zones or networks),
                                        o Allow virus detection software to function,
                                        o Create logs and make them available to the administrator,
                                        o Alert the user of any unusual activity,
                                        o Function as a stateful packet filter,
                                        o Be disabled and enabled by an administrator, and
                                        o Cover its IP address (operate in stealth mode).

                               •   Personal Firewalls should be able to associate each application with
                                   the traffic it initiates.
                               •   Personal Firewalls are implemented in one of two configurations as
                                   follows:
                                       o Personal Firewall Software shall be installed on the individual
                                         system, such as the laptop, it is meant to protect. Personal
                                         firewall software is not designed to offer protection to other
                                         systems or resources
                                       o Personal Firewall Appliances shall be used to protect small
                                         networks. Appliances include:
                                               Cable Modem WAN Routing
                                               LAN Routing (dynamic routing support)
                                               Network hub
                                               Network switch
                                               Dynamic Host Configuration Protocol (DHCP) server
                                               Simple Network Management Protocol (SNMP) agent
                                               Application-proxy agents
                               •   Refer to the Firewall Rules Compliance Component for configuration
                                   guidance
Document Source Reference #
                                              Standard Organization
                               NIST SP 800-41,
                                                                             www.csrc.nist.gov/publications/
Name                           Guideline for Firewalls and       Website
                                                                             nistpubs
                               Firewall Policy
Contact Information
                                                Government Body
                               National Institute of
Name                           Standards and Technology          Website     http://csrc.nist.gov/
                               (NIST)
Contact Information
                                                  KKEEYYW
                                                        WOORRD
                                                             DSS
                               Personal Computer, PC, VPN, telecommute, laptop, portable, firewall
List all Keywords              rules, firewall appliance, port scan, mobile user, DSL, MDT, PDA,
                               wireless
                                      C
                                      COOM
                                         MPPO
                                            ONNEEN
                                                 NTT C
                                                     CLLA
                                                        ASSSSIIFFIIC
                                                                   CAATTIIO
                                                                          ONN
Provide the Classification         Emerging            Current             Twilight      Sunset
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
Provide the Current Status)     In Development          Under Review           Approved     Rejected
                                                  A
                                                  AUUD
                                                     DIITT TTRRA
                                                               AIILL
Creation Date                 06/24/2004                   Date Accepted / Rejected   06/24/2004
    Reason for Rejection
Last Date Reviewed                                         Last Date Updated
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
