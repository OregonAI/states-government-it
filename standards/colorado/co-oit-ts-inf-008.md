---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-inf-008
title: Network Monitoring
doc_type: standard
citation: TS-INF-008
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1LGBX23EUQUaghguhvPlm-8YOJHQW2EcL
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 24d8502c3ab3847b3f90ffab69fc1582a8b54f529b8ff6acdd31a9bb481f6607
effective_date: '2022-11-01'
source_version: 3.0, last updated 12/31/2025
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-008: Network Monitoring'', links this file as https://drive.google.com/file/d/1LGBX23EUQUaghguhvPlm-8YOJHQW2EcL/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1LGBX23EUQUaghguhvPlm-8YOJHQW2EcL
  (the source URL above).'
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

# Network Monitoring (TS-INF-008)

## At a glance

OIT technical standard TS-INF-008 (Infrastructure): Network Monitoring. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-008: Network Monitoring
  Document ID                       TS-INF-008
  Title                             Network Monitoring
  Executive Sponsor                 Network Services, Sr. Manager of Network Operations
  Issuing Authority                 Office of Information Technology (OIT)
  Applies to                        State of Colorado agencies; defines the requirements and
                                    specifications for network monitoring within the State of
                                    Colorado.
  Tier                              Standard
  Version                           3.0
  Effective Date                    11/01/2022
  Last Updated                      12/31/2025

1. Purpose
The purpose of the network monitoring standard is to provide network administrators and engineers
with valuable insights into the health and performance of the State's network. This proactive
approach helps ensure optimal network operation, identify and resolve issues before they become
critical, and plan for future network needs.

2. Scope
This technical standard defines the requirements and specifications for network monitoring within
the State of Colorado agencies. It focuses on the information collection function of network
management systems that monitor and manage the State of Colorado networks, and outlines: Data
Collection; Network Management Applications interoperability requirements; Device State
Monitoring; and Performance and Alert Monitoring.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●      Chairs and conducts business of the Architecture Review Board (ARB).
   ●      Updates effective date and/or last review date.
   ●      Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●      Engages stakeholders and subject matter experts to determine the standard.
   ●      Reviews and approves the Standard (this document).

                                                                                            Page 1 of 4

Network Services - Sr. Manager of Network Operations
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Updates document standards and version number; presents to the ARB for approval and
       adoption.
Network Services - Network Operations Staff
   ●   Keeps the application updated and verifies the system has sufficient resources.
   ●   Maintains inventory on the system; builds and provides reports; handles alerting and
       remediation.
Server Team
   ●   Keeps the server operating system updated and free from vulnerabilities.
   ●   Performs weekly backups; assists in restoring the system.
Database Team
   ●   Maintains the SQL database for the network monitoring application.
   ●   Provides the correct resources on the database server; maintains and manages database
       backups.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Monitoring Requirements
   ●   All network devices capable of being monitored must be monitored (routers, switches,
       wireless controllers, access points, load balancers, and firewalls).
   ●   The monitoring solution must collect different metrics at configurable intervals to aid in
       scaling.
   ●   Must support: SNMP Version 3 (requests and traps); Syslog; NetFlow collection (desirable); and
       custom SNMP OIDs.
Alerting Requirements
   ●   Must generate alerts based on configurable criteria with varying severity levels (minor, major,
       critical).
   ●   Must support criteria around: time of day; day of week; device name; device grouping;
       location; type of device; device component; type of metric; metric value or threshold;
       severity; compound conditions; and hold-downs/suppression.
   ●   Must support forwarding alerts to external services (email, SMS, Google Hangout).
Metric Requirements
   ●   Must collect: availability (up/down); delay; interface utilization; interface errors; CPU
       utilization; and hardware sensors.
   ●   Availability, delay, interface utilization, interface errors, and CPU utilization must be polled
       at an interval not exceeding 10 minutes, ideally every 5 minutes.
   ●   Wireless metrics: number of wireless clients per AP; total wireless users; wireless
       interference; SNR; and wireless coverage with maps.

                                                                                             Page 2 of 4

Data Retention Requirements
   ●   All metrics must be stored and provide historical information for at least one year.
   ●   Rollups at configurable periods for reducing dataset size are acceptable; recommended
       periods: 30 days, 90 days, and 1 year.
   ●   The application server and database must be backed up once a week, with a minimum of 4
       weeks of backups stored.
Reporting Requirements
   ●   Reporting capability must be provided as part of the solution, supporting customized
       reporting.
   ●   Reports must be available for all required metrics for both devices and device groups.
   ●   Must support scheduling, emailing, and recurring reports.
   ●   All reports must support HTML, PDF, Excel, and CSV formats.
   ●   Must support sending logs to an enterprise SIEM (Splunk, presently).
System Location Requirements
   ●   The network monitoring application must be on a separate network from the systems it is
       monitoring.
   ●   Must be deployed behind a robust firewall with strict access controls, configured to allow only
       the minimum necessary ports for operation.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of, and approved by, the "Owner of Standard" listed under
Roles and Responsibilities.
Requests may be acquired by completing the "EXCEPTION REQUEST to Technical Standard" form and
including the completed form (with all signatures) along with other documentation required as part
of standard procedures when executing a technology procurement or service deployment.

6. References
   ●   Techopedia: Network Performance Monitoring
   ●   SolarWinds
   ●   Washington University: Network Monitoring resources

7. Definitions
Network Monitoring: The use of a system that constantly monitors a network for slow or failing
components and notifies the network administrator of outages or troubles.
NetFlow: Network protocol for collecting and analyzing network traffic data, providing insight into
traffic patterns, bandwidth usage, and potential security threats.
SNMP: Simple Network Management Protocol — used for monitoring and managing network devices,
collecting performance data, remote configuration, and receiving alerts.
Network availability: Overall uptime of a network.
Network delay: How long it takes for a bit of data to travel across the network from one
node/endpoint to another.

                                                                                              Page 3 of 4

Interface utilization: Data transfer rate, usually expressed in bits per second (bps).

                                                                                         Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-008: Network Monitoring', links this file as https://drive.google.com/file/d/1LGBX23EUQUaghguhvPlm-8YOJHQW2EcL/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1LGBX23EUQUaghguhvPlm-8YOJHQW2EcL (the source URL above).
