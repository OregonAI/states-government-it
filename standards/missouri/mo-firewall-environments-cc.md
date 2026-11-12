---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-firewall-environments-cc
title: Firewall Environments
doc_type: standard
citation: 'Security Domain Compliance Component: Firewall Environments'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-Firewall-Environments.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 20173a1e8294400cf6cc79a6f2dc108a66004299cb6a45533414687ae14c3179
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

# Firewall Environments (Security Domain Compliance Component: Firewall Environments)

## At a glance

Row 'Firewall Environments' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/firewall-environments-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is status Approved with no classification box marked, with Date Approved / Rejected 3-29-2017. The index lists it as an approved standard.

## Full text

                                    COMPLIANCE COMPONENT

                                                     DEFINITION
Name                   Firewall Environments
                       Firewall Environment is a term used to describe a set of systems and access
Description
                       controls between or within networks.
                       The Firewall Environment provides protection for the organization’s networks
Rationale
                       while minimizing complexity and management.
                       • One part of a defense-in-depth security strategy
                       • May integrate with other security solutions
Benefits               • Restricts connectivity between or within networks
                       • Provides network segmentation
                       • Provides remote access security

                                      ASSOCIATED ARCHITECTURE LEVELS
Specify the Domain Name         Security
Specify the Discipline Name     Technical Controls
Specify the Technology Area
                                Secure Gateways and Firewalls
Name
Specify the Product
Component Name

                                           COMPLIANCE COMPONENT TYPE
Document the Compliance
                                Guideline
Component Type
Component Sub-type

                                               COMPLIANCE DETAIL
                                Firewall Environments may consist of:
                                • Firewall(s)
                                • Demilitarized Zones (DMZs)
                                • Virtual Private Networks Concentrators (VPNs)
                                • Intranets
                                • Extranets
                                • Routers, hubs and switches
                                • Intrusion Detection Systems (IDS/IPS)
                                • Dynamic Host Configuration Protocol (DHCP)
State the Guideline, Standard
                                • Domain Name Server (DNS)
or Legislation
                                A simple firewall environment may perform only packet filtering. In a
                                more complex and secure environment, it may consist of packet
                                filtering, proxies, IPS, VPN, and specific technologies supporting
                                network security.
                                Building Firewall Environments
                                • A firewall shall be used between any agency-controlled equipment
                                     and equipment not controlled by the agency such as that owned by
                                     other agencies, contractors, business partners or public service
                                     providers.

                              •  The deployment should be as simplified as possible. Simplified
                                 firewall deployment will result in a more secure and manageable
                                 system. Complexity in deployment can lead to errors in
                                 configuration.
                              • Equipment not intended to be Firewalls should not be configured as
                                 firewalls. For example, network equipment used as firewalls are not
                                 hardened systems and can lead to vulnerabilities.
                              • A router should not be used as a firewall unless special firewall
                                 software is installed on it.
                              • Internal firewalls should be used to minimize the threat landscape.
                              DMZs
                              • A DMZ is created to provide network segmentation and access
                                 control between environments with different security requirements.
                              • Agencies should provide DMZ redundancy to minimize service
                                 degradation during denial of service attacks.
                              • DMZs shall serve as connection points for systems that require or
                                 support external connectivity, or between internal systems with
                                 different levels of access control.
                              • Agencies should place remote access servers, publically available
                                 assets and external VPN endpoints within DMZs.
                              VPNs
                              • External VPN connections shall be terminated on the firewall,
                                 ensuring that traffic passed through the VPN tunnel is encrypted
                                 between firewalls.
                              Intranets
                              • A computer network, which is not public, in contrast to the internet.
                              • An intranet should be behind the firewall.
                              • An internal firewall should be used to separate intranets.
                              Extranets
                              • An extranet is two or more networks that are joined via the Internet
                              NIST SP 800-41,
Document Source Reference #   Guideline for Firewalls and
                              Firewall Policy
                                             Compliance Sources
                              National Institute of
                              Standards and Technology
                                                                          www.csrc.nist.gov/publications/
Name                          (NIST), Computer Security         Website
                              Resource Center (CSRC)                      Intpubs

Contact Information           inquiries@nist.gov
                              National Institute of
Name                          Standards and Technology          Website   http://csrc.nist.gov/
                              (NIST)
Contact Information

                                                   KEYWORDS
                              Threat landscape, DMZ, VPN, DNS, extranet, intranet, IDS, IPS,
List Keywords                 packet filter, defense-in-depth, access control, contractors,
                              business partners, firewall
                                         COMPONENT CLASSIFICATION
Provide the Classification        Emerging                Current            Twilight             Sunset

    Sunset Date

                                                CURRENT STATUS
Provide the Current Status     In Development           Under Review              Approved      Rejected

                                                  AUDIT TRAIL
Creation Date                6-8-2004                  Date Approved / Rejected     3-29-2017
    Reason for Rejection
Last Date Reviewed           3-29-2017                 Last Date Updated            3-29-2017
    Reason for Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
