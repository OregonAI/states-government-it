---
schema_version: 1
corpus: states-government-it
jurisdiction: washington
id: wa-ea-04-01-g
title: IPv6 Guidelines
doc_type: policy
citation: WaTech Guideline EA-04-01-G
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2023-12/EA-02-03-01-G%20IPV6%20Guidelines%20%282%29.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: dc034ba9b1214cf9de04d7432de0cabadc3af3d1b3f72a8c685b67cc86e705ff
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# IPv6 Guidelines (WaTech Guideline EA-04-01-G)

## At a glance

Item of the WaTech policy library, chapter '3. Enterprise Architecture' (listed as type Guidelines). Listed at https://watech.wa.gov/policies/ipv6-guidelines.

## Full text

EA-02-03-01-G                                                                                       Replaces:
State CIO Adopted: October 6, 2023                                                                       N/A
Sunset Review: October 6, 2026

                       IPV6 IMPLEMENTATION GUIDELINES
See Also:
RCW 43.105.054 OCIO Governance                        RFC Filtering
RCW 43.105.205 (3) Higher Ed                          RFC Basic IPV6 Transition Mechanisms
RCW 43.105.020 (22) “State agency”                    RFC Unique Local IPv6 Unicast Addresses
American Registry for Internet Numbers

     1. Agencies should apply static addressing to servers and storage to ensure
        functionality and availability.

              a. If servers are not manually configured with an Internet Protocol version 6
                 (IPv6) address, a new IPv6 address should be autoconfigured whenever
                 a Network Interface Controller (NIC) card is replaced.

              b. Keep the following tips in mind when you create addresses for servers:

                     i.     Give servers meaningful and stable interface identifications
                            (interface IDs).

                     ii.    One strategy is to use a sequential numbering scheme for
                            interface IDs.

     2. Agencies should Plan IPv6 addressing as follows:

              a. Plan for addressing based on the total number of sites, not the end
                 number of devices.

              b. The end user device is no longer a factor when planning the address
                 scheme.

              c. Reserve a block for infrastructure, such as internal routing interface
                 addressing, and static addresses for administration servers and devices.

              d. Lay out each subnet prefix of equal size within each level of the
                 hierarchy.

              e. Begin tracking and planning for the upgrade/replacement of devices
                 that are not IPv6 capable.

                                                                                                1

3. Address Schemes Guidelines. See Subnet Calculator and/or Test my ipv6
   Subnet Calculator.

          a. IPV6 uses hexadecimal numbering. See Hexidecimal_Binary_Chart

          b. Map to network topology.

          c. Meet current requirements under IPV6 Policy.

          d. Manually configure link-local addresses in an easily readable format.
             This will make verifying or troubleshooting routes easier.

          a. Ensure schemas align with nibble boundaries as much as possible. See
             Table_1_Nibble_Boundaries and associated examples:
                 i. Network_Allocation_Example_48_52_60
                ii. Network_Allocation_Example_36_56_64
               iii. Network_Allocation_Example_36_48_56
                 iv. Network_Allocation_Example_36_44_56

4. Security considerations for Tunneling on an Internal Agency Local Area
   Network (LAN):

               i.    Tunnel endpoints.

              ii.    Inspection.

              iii.   Access control.

              iv.    Termination.

               v.    Tunnels shall be treated as external links with the appropriate
                     security protocols in place. See NIST 800-119 Guidelines for the
                     Secure Deployment of IPV6.

5. Agencies should update the following network services to support IPv6:

     i.      Domain Naming Service (DNS) Records-

               i.    PRIMARY Records

                        A. A- IPv4

                        B. AAAA- IPv6

                        C. PTR= Pointer Records

                        D. CNAME- Canonical Name Records
                                                                                        2

                         E. NS- Name Server

                         F. MX – Mail Exchange records, add IPv6 addressing to the
                            mail server.

        b. Records to inspect for IPv6 compatibility.

        c. NIS- Name Information Server

                   i.    NFS- Name File Server

                  ii.    NTP- Network Time Protocol Server

                  iii.   WEB- Server

                  iv.    Linux and Bind Services

                   v.    Note: LDAP supports IPv6 without requiring additional
                         configuration changes.

6. Agencies should validate IPv6 capability:

     a. Validate that devices (current and future) can support IPv6 routing protocol
        of choice for both hardware/software and operating system (OS).

     b. Agencies shall ensure the current IOS is IPv6 compatible.

     c. Ensure that current or future model and version type are compatible, as a
        model may be compatible while select versions are not.

     d. Verify which hardware on the network can be upgraded to IPv6 and any
        other device. For Example:

           i.    Routers.

          ii.    Switches.

          iii.   Servers.

  7. Agencies should assess IPv6 for the agency environment:

     a. An IPv6 plan should be built for each key technology pillar (or silo) within an
        agency. Agencies are responsible for and assessing the impact of
        anycasting to:

          i.     Network – Routers, switches, wireless, load balancing, DHCP, DNS,
                 IPAM, Internet peering, routing policies.

                                                                                      3

          ii.    Security – Firewalls, IDS/IPS, logging, identity management.

          iii.   Systems and Virtualization – Host servers, applications, guest OS’s,
                 DNS, DHCP, IPAM, logging, identity management, client OS’s.

          iv.    Storage – SAN, file protocols, file services, backup, and recovery.

           v.    Database – SQL, big data, or other data analysis processes.

          vi.    Line of business applications – CRM, Human Resources, Financials,
                 or any customer applications developed by the agency itself.

8. SLAAC (Stateless Address Auto-Configuration) will not be used on the State
   Core Networks.

     i.   If an agency implements SLAAC internally on their LAN, then the entire
          LAN must be 100% IPv6.

    ii.   For stateless configuration to work properly, the advertised prefix length in
          an RA message must always be 64 bits.

REFERENCES:
     1. Subnet Calculator.
     2. Test my ipv6 Subnet Calculator.
     3. Hexidecimal_Binary_Chart.
     4. NIST 800-119 Guidelines for the Secure Deployment of IPv6.
            a. Para. 3.7.3.3 IPv6-Specific DNS Security Recommendations.
            b. Para 6.4 Dual Stack Ipv4/IPv6 Environments.
            c. Para 6.5.1 General Security Considerations for Tunneling.
     5. Statewide Migration to IPv6.
     6. Table 1 Information System (Nibble) Boundaries.
     7. Network_Allocation_Example_48_52_60.
     8. Network_Allocation_Example_36_56_64.
     9. Network_Allocation_Example_36_48_56.
     10. Network_Allocation_Example_36_44_56.

                                                                                        4

Table 1: Information System (Nibble) Boundaries, with prefix notations (these
are not CIDRs notations):

/36 includes
16- /40         /40 includes       /44 includes
                                                    /48 includes
256 /44         16 - /44’s         16 - /48’s
                                                    16 - /52’s
4,096 /48       256 /48’s          256 - /52’s
                                                    256 - /56’s
65,536 /52      4,096 /52’s        4,096 /56’s
                                                    4,096 /60’s
1,048,576 /56 65,536 /56’s         65,536 /60’s
                                                    65,536 /64
16,777,216 /60 1,048,576 /60’s     1,048,576 /64
268,435,456 /64 16,777,216 /64’s

/52 includes                                        /64 includes
                /56 includes
16 - /56’s                         /60 includes     1- /64 =
                16 - /60’s
256 - /60’s                        16 - /64’s       (18,446,744,073,709,551,616
                256 - /64’s                         host addresses)
4,096 /64’s

Back to REFERENCES

                                                                                5

Network Address Allocation Examples
  EXAMPLE                                                                                                                                                                 EXAMPLE
             Example /36 Broken into /40 to /56 to /64 assigned to devices

                                                                                                                                           /64           /64                     /64        /64
                                                                                                                                     /64 DHCPv6         Static    /64      /64 DHCPv6      Static /64
                                                                                                                                    DHCPv6                       DHCPv6   DHCPv6                DHCPv6

                                                                APP VRF (on-prem)                                                                  HQ                                  Site 1
                                                                    Aggregate                                                                   Aggregate                            Aggregate
                                                               1234:5678:9F00:/40                                                         1234:5678:9000:ff00:/56             1234:5678:9000:0100:/56
                                                                                                                                                 256/64's                            256 /64's

                                              Watech Link IP

                                                                                                                Watech Link IP        Watech Link IP
                                                                                                                    /64                   /64
                                                                                                                                                                                          Site 2
                          Watech Link IP                                                                                                                                                Aggregate
                                                                                                                                                                                 1234:5678:9000:0200:/56
                                                                                                                                       Watech Link IP                                    256/64's
                                                                                         Core VRF                                          /64
          Fusion                                                                        Aggregate
                                  Watech Link IP               Watech Link IP                            /40 = 256 / 48
    1234:5678:9000::/36                                                             1234:5678:9000:/40
                                                                                       65,536/56's
                                                                                                                                       Watech Link IP
                                                                                                                                           /64
                                                                                      40-44-48                                                                                            Site 3
                                                                                                                                    Watech Link IP                                      Aggregate
                                                                                                                                        /64                                      1234:5678:9000:0300::/56
                                                                                                                   Watech Link IP                                                        256/64's
                                                                                                                       /64

                                                                                                                                                                                     Site 4
                                                                                                                                                                                   Aggregate
                                                                                                                                                                            1234:5678:9000:0400::/56
                                                                                                                                                       Site 5
                                                                                                                                                                                    256/64's
                                                                                                                                                     Aggregate
                                                                                                                                              1234:5678:9000:0500::/56
                                                                                                                                                     256 /64's

   EXAMPLE                                                                                                                                                           EXAMPLE
Back to REFERENCES

                                                                                                                                                                                                            6

 Example /36 Broken into /44 into /48 to /56                                                                                                   1234:5678:9000:0101:/64
                                                                                                                                               1234:5678:9000:0102:/64
                                                                                                                                               1234:5678:9000:0103:/64
                                                                                                                                               1234:5678:9000:0104:/64

 EXAMPLE
                                                                                                                                               1234:5678:9000:0105:/64
                                                                                                                                                           Etc
                                                                                                                                               1234:5678:9000:01FF:/64

                                                                                                             /64        /64                       /64              /64
                                                                                                       /64 DHCPv6      Static               /64 DHCPv6            Static /64
                                                                                                      DHCPv6                               DHCPv6                      DHCPv6
                                                                                                                   HQ
                                                               APP VRF (o n-prem)                                                                          Site 1
                                                                                                                Aggregate
                                                                   Aggregate                                                                             Aggregate
                                                                                                          1234:5678:9000:ff00:/56
                                                              1234:5678:9F00:/44                                                                  1234:5678:9000:0100:/56
                                                                                                                 256 /64's                                                                           Site 2
                                                                                                                                                         256 /64's
                                                                                                                                                                                                   Aggregate
                                                                                                                                                                                            1234:5678:9000:0200:/56
                                             Watech Link IP                             /64                                                                                                        256 /64's
                                                                                      SSLVPN                                                                     Watech Link IP
                                                                                                                                          Watech Link IP
                                                                                    (Watech IP)                                               /64                    /64            Watech Link IP
                                                                                     (example)
                                                                                                                                                                                        /64
                        Watech Link IP

                                                                                          Core VRF                                                                         Island VRF
        Fusion                                                                           Aggregate                                                                        Aggregate
                                 Watech Link IP               Watech Link IP                                   Watech Link IP             Watech Link IP
  1234:5678:9000::/36                                                                1234:5678:9000:/44                                                               1234:5678:9000::/48
                                                                                           16/48's                                                                          256 /56's

                           Watech Link IP
                                                                                 /64

                                                                                                      EXAMPLE
                                                                                                                                                                                     Watech Link IP
    Watech Link IP                                                        WaTech Pvt Cloud                                                                                               /64
                                                                          hosts (Watech IP)
                                                                             (example)                                                                                  Watech Link IP
                                                                                                                                                   Watech Link IP
                                                                                                                                                       /64                  /64
                                                      Watech Link IP                                                                                                                                   Site 3
                                                                                                                                                                                                     Aggregate
                                                                                                                                                                                              1234:5678:9000:0300::/56
                Watech Link IP                                                                                                                                                                       256 /64's
                                                                          AGCY-BP VRF (on-prem)
                                                                               Aggregate
                                                                           1234:5678:9a00:/44                                                                              Site 4
                                APP VRF (data center)                                                                                                                    Aggregate
                                     Aggregate                                                                                  Site 5                            1234:5678:9000:0400::/56
                               WATE:CH:IP:SPAC:E::/64                                                                         Aggregate                                  256 /64's
                                  (invalid address)                                                                    1234:5678:9000:0500::/56
                                                                                                                              256 /64's

                     EXAMPLE                                                                                                                                         EXAMPLE

Back to REFERENCES

                                                                                                                                                                                                         7

 Example /36 Broken into /48 into /56                                                                                                         1234:5678:9000:0101:/64
                                                                                                                                              1234:5678:9000:0102:/64
                                                                                                                                              1234:5678:9000:0103:/64
                                                                                                                                              1234:5678:9000:0104:/64
                                                                                                                                              1234:5678:9000:0105:/64
                                                                                                                                                          Etc
                                                                                                                                              1234:5678:9000:01FF:/64

                                                                                                            /64        /64                       /64              /64
                                                                                                      /64 DHCPv6      Static               /64 DHCPv6            Static /64

 EXAMPLE
                                                                                                     DHCPv6                               DHCPv6                      DHCPv6
                                                                                                                  HQ
                                                              APP VRF (o n-prem)                                                                          Site 1
                                                                                                               Aggregate
                                                                  Aggregate                                                                             Aggregate
                                                                                                         1234:5678:9000:ff00:/56
                                                             1234:5678:9F00:/48                                                                  1234:5678:9000:0100:/56
                                                                                                                256 /64's                                                                           Site 2
                                                                                                                                                        256 /64's
                                                                                                                                                                                                  Aggregate
                                                                                                                                                                                           1234:5678:9000:0200:/56
                                            Watech Link IP                             /64                                                                                                        256 /64's
                                                                                     SSLVPN                                                                     Watech Link IP
                                                                                                                                         Watech Link IP
                                                                                   (Watech IP)                                               /64                    /64            Watech Link IP
                                                                                    (example)
                                                                                                                                                                                       /64
                       Watech Link IP

                                                                                         Core VRF                                                                         Island VRF
       Fusion                                                                           Aggregate                                                                        Aggregate
                                Watech Link IP               Watech Link IP                                   Watech Link IP             Watech Link IP
 1234:5678:9000::/36                                                                1234:5678:9000:/48                                                               1234:5678:9000::/48
                                                                                         256 /56's                                                                         256 /56's

                          Watech Link IP
                                                                                /64

                                                                                                     EXAMPLE
                                                                                                                                                                                    Watech Link IP
   Watech Link IP                                                        WaTech Pvt Cloud                                                                                               /64
                                                                         hosts (Watech IP)
                                                                            (example)                                                                                  Watech Link IP
                                                                                                                                                  Watech Link IP
                                                                                                                                                      /64                  /64
                                                     Watech Link IP                                                                                                                                   Site 3
                                                                                                                                                                                                    Aggregate
                                                                                                                                                                                             1234:5678:9000:0300::/56
               Watech Link IP                                                                                                                                                                       256 /64's
                                                                         AGCY-BP VRF (on-prem)
                                                                              Aggregate
                                                                          1234:5678:9a00:/48                                                                              Site 4
                               APP VRF (data center)                                                                                                                    Aggregate
                                    Aggregate                                                                                  Site 5                            1234:5678:9000:0400::/56
                              WATE:CH:IP:SPAC:E::/64                                                                         Aggregate                                  256 /64's
                                 (invalid address)                                                                    1234:5678:9000:0500::/56
                                                                                                                             256 /64's

                    EXAMPLE                                                                                                                                         EXAMPLE

Back to REFERENCES

                                                                                                                                                                                                                     8

 Example /36 Broken into /48 into /52 into /60 for site’s

                                                                                                             /64         /64                      /64            /64
                                                                                                       /64 DHCPv6       Static              /64 DHCPv6          Static /64

 EXAMPLE
                                                                                                      DHCPv6                               DHCPv6                    DHCPv6
                                                                                                                    HQ
                                                              APP VRF (on-prem)                                                                            Site 1
                                                                                                                 Aggregate
                                                                  Aggregate                                                                              Aggregate
                                                                                                          1234:5678:9000:ff00::/60
                                                             1234:5678:9F00::/48                                                                  1234:5678:9000:0100::/60
                                                                                                                 256 /64's                                                                         Site 2
                                                                                                                                                         256 /64's
                                                                                                                                                                                                 Aggregate
                                                                                                                                                                                          1234:5678:9000:0200::/60
                                            Watech Link IP                             /64                                                                                                       256 /64's
                                                                                     SSLVPN                                                                    Watech Link IP
                                                                                                                                          Watech Link IP
                                                                                   (Watech IP)                                                /64                  /64            Watech Link IP
                                                                                    (example)
                                                                                                                                                                                      /64
                       Watech Link IP

                                                                                         Core VRF                                                                        Island VRF
       Fusion                                                                           Aggregate                                                                       Aggregate
                                Watech Link IP                Watech Link IP                                    Watech Link IP            Watech Link IP
 1234:5678:9000::/36                                                                1234:5678:9000::/48                                                             1234:5678:9000::/52
                                                                                         256 /56's                                                                        256 /60s

                          Watech Link IP
                                                                                 /64

                                                                                                      EXAMPLE
                                                                                                                                                                                   Watech Link IP
   Watech Link IP                                                         WaTech Pvt Cloud                                                                                             /64
                                                                          hosts (Watech IP)
                                                                             (example)                                                                                Watech Link IP
                                                                                                                                                   Watech Link IP
                                                                                                                                                       /64                /64
                                                     Watech Link IP                                                                                                                                  Site 3
                                                                                                                                                                                                   Aggregate
                                                                                                                                                                                            1234:5678:9000:0300::/60
               Watech Link IP                                                                                                                                                                      256 /64's
                                                                         AGCY-BP VRF (on-prem)
                                                                              Aggregate
                                                                          1234:5678:9a00::/48                                                                            Site 4
                               APP VRF (data center)                                                                                                                   Aggregate
                                    Aggregate                                                                                   Site 5                          1234:5678:9000:0400::/60
                              WATE:CH:IP:SPAC:E::/64                                                                          Aggregate                                256 /64's
                                 (invalid address)                                                                     1234:5678:9000:0500::/60
                                                                                                                              256 /64's

                    EXAMPLE                                                                                                                                         EXAMPLE

Back to REFERENCES

                                                                                                                                                                                                                     9

Hexidecimal/Binary Chart

Back to REFERENCES

                           10

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
