---
schema_version: 1
corpus: states-government-it
jurisdiction: washington
id: wa-sec-04-04-s
title: Firewall Standard
doc_type: standard
citation: WaTech Standard SEC-04-04-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2024-08/SEC-04-04-S%20Firewall%20Standard.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: 77cae7e0f9ef62b279e337d4f2749bd5fb30ea95bddba56568fbc5e8e5827557
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

# Firewall Standard (WaTech Standard SEC-04-04-S)

## At a glance

Item of the WaTech policy library, chapter '4. IT Security' (listed as type Standards). Listed at https://watech.wa.gov/policies/firewall-standard.

## Full text

SEC-04-04-S                                                                                                   Replaces:
State CIO Adopted: June 8, 2023                                                      IT Security Standard 141.10 (5.1. 2)
TSB Approved: June 8, 2023                                                                          December 11, 2017
Sunset Review: June 8, 2026

                                     FIREWALL STANDARD
See Also:
RCW 43.105.054 WaTech Governance
RCW 43.105.052 Powers and duties of agency—Application to higher education, legislature, and judiciary.
RCW 43.105.020 (22) “State agency”
RCW 43.105.450 Office of Cybersecurity

    1. Agencies must implement and annually review the baseline firewall security
       configuration requirements described below:

            a. Change vendor-supplied default passwords and firewall configurations.

            b. Remove or disable all unnecessary default accounts before installing a
                firewall on the network.

            c. All firewall systems must fail in a closed state, allowing no traffic to pass.

            d. All firewalls must support inbound and outbound IPv4 and IPv6 traffic.

            e. All firewalls must generate event logs resulting from the creation of sessions
                and denial of traffic where appropriate.

            f. The firewall configuration must be reviewed at least annually, or more
                frequently based on agency business requirements.

    2. Agencies must institute network access and authorization controls to ensure that
       only authorized administrators have access to change firewall rules. The
       administrative interface to the firewall must support the following:

            a. Identification and authentication of firewall administrators.

            b. Encryption of administrative traffic over a separate management network.

            c. Always use Multifactor Authentication (MFA) for Internet-facing firewall
                administrative interfaces.

            d. Agency-managed firewalls must utilize MFA to access the firewall
               management interface. This could be either through an isolated and
               secured management network or when the firewall is accessed directly.

                                                                                                                   1

      e. Local, physical console access does not require MFA. Configurations for
          local console access accounts to support emergency local access must be
          configured with recommended secure configurations based on vendor
          guidance or the CIS benchmarks per the Configuration Management
          Standard. Physical access to the firewall must be tightly controlled with
          locked cabinets or other datacenter environment access controls to prevent
          unauthorized access.

      f. Access to the administrative interfaces will generate an access audit log.

3. Agencies must implement the following minimum technical security standards
   when configuring their firewall rulesets.

      a. Block traffic originating from outside the agency network if it contains
          addresses within the agency network.

      b. Block services, protocols, and ports not specifically allowed by the agency
          security policy.,

      c. Allow only agency-approved out-going network traffic from the internal
          network to the DMZ or Internet. Approved out-going network traffic may
          include agency communications to other agencies, service providers, or
          authorized destinations.

      d. Allow only WaTech and agency-approved in-coming network traffic to the
         internal network from the DMZ, Internet, wireless networks and SGN.
         Approved in-coming network traffic may include communications from
         other agencies, service providers, or authorized sources.

      e. Block traffic with invalid incoming source or outgoing destination addresses.
          Examples of relatively common invalid IPv4 addresses are 127.0.0.0 to
          127.255.255.255 (also known as the localhost addresses) and 0.0.0.0
          (interpreted by some operating systems as a localhost or a broadcast
          address). These have no legitimate use on a network. Also, traffic using link-
          local addresses (169.254.0.0 to 169.254.255.255) should be blocked.

      f. Block traffic with private incoming source or outgoing destination addresses
          to or from the Internet. The most common type of invalid external
          addresses is an IPv4 address within the ranges in RFC 1918, Address
          Allocation for Private Internets, that are reserved for private networks.
          These ranges are 10.0.0.0 to 10.255.255.255 (10.0.0.0/8 in Classless Inter-
          Domain Routing [CIDR] notation), 172.16.0.0 to 172.31.255.255
          (172.16.0.0/12), and 192.168.0.0 to 192.168.255.255 (192.168.0.0/16).

                                                                                        2

       g. Changes to the firewall ruleset must be reviewed when they are proposed.
          This review must align with the agency’s change management policy. This
          review may require WaTech approval as appropriate.

REFERENCES

  1.    Center for Internet Security (CIS) benchmarks.
  2.    NIST 800-41 Guidelines on Firewalls and Firewall Policy.
  3.    NIST Cybersecurity Framework Mapping:
       • Protection.Data Security-5: Protections against data leaks are implemented.
       • Protection.Access Control-5: Network integrity is protected (e.g., network
          segregation, network segmentation).
       • Protection.Protective Technology-4: Communications and control networks
          are protected.

CONTACT INFORMATION

  •    For questions about this policy, please email the WaTech Policy Mailbox.
  •    For questions about risk assessments and management, please email
       the Risk Management Mailbox.

                                                                                     3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
