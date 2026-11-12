---
schema_version: 1
corpus: states-government-it
jurisdiction: nevada
id: nv-sec-s-5-08-01
title: Wireless Networks
doc_type: standard
citation: S.5.08.01
authority_level: ''
issuing_body: Nevada State Information Security Committee; published by the Governor's Technology Office
  (Office of Information Security and Cyber Defense)
source_url: https://it.nv.gov/siteassets/itnew.nv.gov/content/governance/security/s.5.08.01---wireless-network.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 0f3a3a6c16aa04055c9bc99ab857a5cd456ce17eb31f10b7bde8d669b9961e0c
effective_date: '2020-12-31'
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

# Wireless Networks (S.5.08.01)

## At a glance

Listed on the Governor's Technology Office page 'Security Policies, Standards & Procedures' (https://it.nv.gov/governance/security-policies-standards--procedures/) as 'S.5.08.01 - Wireless Networks - Effective 12/31/2020'. NAC 242.110 adopts the State Information Security Policies, Standards and Procedures by reference and binds every executive-branch agency, state employee and contractor with access to state information to them. Minimum basic security for IEEE 802.11x wireless devices and methods.

## Full text

                                    State of Nevada
                               Information Security Committee

                                            Standard
Document ID      Title                                            Revision     Effective Date         Page
  S.5.08.01      Wireless Networks                                    D          12/31/2020           1 of 4

1.0   PURPOSE
      This standard provides minimum requirements for the basic security of IEEE standard 802.11x
      wireless devices and methods used to establish data connections to or through such devices.
      This standard only addresses 802.11x wireless connectivity, and does not discuss microwave
      communications.

2.0   SCOPE
      This standard applies to all state agencies and authorized users meeting the criteria identified in
      the State Information Security Program Policy, Section 1.2, Scope and Applicability.

3.0   EFFECTIVE DATES
      This standard becomes effective at the time of approval of the State Chief Information Officer
      (CIO).

4.0   RESPONSIBILITIES
      The agency head and appointed agency Information Security Officer (ISO) have the responsibility
      to ensure compliance with this standard..

5.0   RELATED DOCUMENTS
      State Information Security Program Policy, 100
      Wireless Access Control, S.6.15.01

6.0   STANDARD
      6.1     Before wireless access is connected to any SilverNet network, directly or indirectly, an
              approved Wireless Request must be received and processed by the ISO of the agency
              implementing the wireless access.

      6.2     All wireless communications shall be encrypted and password protected.

      6.3     Access points and bridges shall be connected to protected ports on a Local Area Network
              (LAN) switch or router using port security based on MAC address or 802.1x.

      6.4     Antenna orientations and radiation strength should be set to minimize exposure outside of
              the areas of intended use.

      6.5     Agencies should coordinate with residents of any adjacent structure within the signal
              coverage area to ensure radio interference does not occur.

      6.6     The agency ISO or designee shall provide the Office of Information Security with an annual
              report identifying wireless devices in use by the agency. OIS will audit those devices on an
              annual basis.

      6.7     Equipment must meet all applicable rules of regulatory agencies as established by the
              Federal Communications Commission (FCC). Vendor equipment is generally marked as
              certified for WiFi use.

                                    State of Nevada
                               Information Security Committee

                                            Standard
Document ID      Title                                            Revision      Effective Date       Page
  S.5.08.01      Wireless Networks                                    D           12/31/2020        2 of 4

      6.8     Wireless access points and bridges must use secure administrative access control and
              protocols, such as IP specific administration restrictions or other methods as appropriate,
              as well as current industry-standard session encryption.

      6.9     All wireless equipment will be compliant with IEEE 802.11x.

      6.10 Abuse, interference, or disruption of authorized communications shall be reported to the
           Office of Information Security (OIS).

      6.11 A separate network authentication, authorization, and accounting process must be used
           prior to allowing authorized wireless access points, bridges, or clients access to SilverNet
           hosts. The authorization database cannot reside on the gateway between the wired and the
           wireless network and must reside within the wired network. Wireless client accounts cannot
           be maintained or managed on the wireless access point or bridge.

      6.12 Wireless Network Access to Wired Networks
              A. Installation of wireless networks using default settings shall be considered insecure.
              B. Authentication to a wireless network shall not automatically grant access to a physically
                 wired network.
              C. A separate authentication, authorization, and accounting process must take place prior
                 to allowing authorized wireless clients access to nodes in a wired network. The
                 authorization database cannot reside on the gateway between the wired and the
                 wireless network and must reside within the wired network.

7.0   DEFINITIONS
      802.11a: An IEEE specification for wireless networking in the 5GHz frequency range with a
      maximum 54Mbps data transfer rate. The 802.11a specification also includes Quality of Service
      (QoS) technology to protect voice and multimedia data.

      802.11b: International standard networking technology for LAN wireless implementation that
      revised 802.11 to increase transmission speeds to 11Mbps.

      802.11g: 802.11g will broaden 802.11b’s data rates to 54Mbps within the 2.4 GHz band using
      Orthogonal frequency division multiplexing (OFDM).

      802.11i: 802.11i is the IEEE standard for security in a wireless local area network.

      802.11n: 802.11n operates on both the 2.4 GHz and lesser-used 5 GHz bands. It operates at a
      maximum net data rate from 54 Mbit/s to 600 Mbit/s.

      Access Point (AP): Wireless LAN transmitter/receiver that acts as a connection between
      wireless clients and wired networks.

      Internal (network): A state administered network not available by default to the general public.

      Microwave: Frequencies ranging from 0.3 GHz to 300 GHz. Most applications are from 1.0 GHz
      to 40 GHz. Unlicensed point-to-point applications are typically in the 0.9 GHz, 2.4 GHz, 5.3 GHz,
      5.8 GHz, and 60 GHz frequency range; while licensed point-to-point applications are typically 4.9

                                      State of Nevada
                                Information Security Committee

                                              Standard
 Document ID      Title                                              Revision      Effective Date       Page
  S.5.08.01       Wireless Networks                                     D            12/31/2020         3 of 4

        GHz and above. Some microwave uses are connectivity between buildings, leased line
        replacement, a cost effective alternative to fiber optics, and backhaul of data, voice and video. All
        State agencies must utilize EITS services except as otherwise provided for in NRS 242.131. Any
        State agency requiring microwave services must make a request to EITS Network Transport
        Services Manager utilizing the EITS Help Desk.

        PKI: An acronym for public key infrastructure, a system of digital certificates, Certificate
        Authorities, and other registration authorities that verify and authenticate the validity of each party
        involved in an Internet transaction. PKIs are currently evolving and there is no single PKI or even
        a single agreed-upon standard for setting up a PKI. However, nearly everyone agrees that
        reliable PKIs are necessary before electronic commerce can become widespread.

        SSID: Short for service set identifier, a 32-character unique identifier attached to the header of
        packets sent over a WLAN that acts as a password when a mobile device tries to connect.

        VPN (Virtual Private Network): A private data network that uses public telecommunications
        infrastructure while preserving privacy by using a tunneling protocol and other security measures.
        Using a VPN consists of encrypting information before sending it through the public network and
        then decrypting it at the other end. Companies have recently begun to consider using VPN to
        fulfill both their Intranet and Extranet needs.

        Wireless: For the purpose of this standard, the IEEE 802.11x standards.

        WPA (Wi-Fi Protected Access): A specification of standards-based, interoperable security
        enhancements that strongly increase the level of data protection and access control for existing
        and future wireless LAN systems. Designed to run on existing hardware as a software upgrade,
        Wi-Fi Protected Access is derived from and will be forward compatible with the upcoming IEEE
        802.11i standard.

8.0     RESOURCES
        Center for Internet Security (CIS), CIS Controls v7.1 Guide
        Network Security Management, EITS Security Standard E.5.04.02
        Network Access Control, EITS Security Standard E.5.04.04

9.0     EXCEPTIONS
        Requests for exception to the requirements of this Information Security Standard must be
        documented, provided to the Office of Information Security (OIS), and approved by the State
        Chief Information Security Officer (CISO).

Approved By
Title                                                    Signature                           Approval Date
State Information Security Committee                     Approved by Committee                    11/19/2020
State Chief Information Security Officer (CISO)          Signature on File                        11/24/2020
State Chief Information Officer (CIO)                    Signature on File                        11/30/2020

                                   State of Nevada
                               Information Security Committee

                                           Standard
 Document ID     Title                                          Revision      Effective Date      Page
  S.5.08.01      Wireless Networks                                  D          12/31/2020        4 of 4

Document History
 Revision     Effective Date   Change
    A             5/01/2016    Initial release – Formerly EITS Standard 131
    B             9/29/2016    Minor changes to Section 6.0.
    C            12/26/2018    Renumbering (143 to S.5.08.01) and compliance to ADA standards
    D            12/31/2020    Biennial review for alignment with the CIS Controls v7.1, Implementation
                               Group 1 (IG1)

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
