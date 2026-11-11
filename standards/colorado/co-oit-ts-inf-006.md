---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-inf-006
title: Enterprise Load Balancing
doc_type: standard
citation: TS-INF-006
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=13BkR1afnErVlnDZNlelYVJdsWuSr1l5-
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 588383a5754cbd76c760557f02ac7099f8bdb44c0d5863427cf49db6a14e0cc8
effective_date: '2025-07-01'
source_version: 3.0, last updated 07/23/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-006: Enterprise Load Balancing'', links this file as https://drive.google.com/file/d/13BkR1afnErVlnDZNlelYVJdsWuSr1l5-/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=13BkR1afnErVlnDZNlelYVJdsWuSr1l5-
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

# Enterprise Load Balancing (TS-INF-006)

## At a glance

OIT technical standard TS-INF-006 (Infrastructure): Enterprise Load Balancing. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-006: Enterprise Load Balancing
  Document ID                     TS-INF-006
  Title                           Enterprise Load Balancing
  Executive Sponsor               Network Operations, Sr. Manager of Network Services
  Issuing Authority               Office of Information Technology (OIT)
  Applies to                      OIT and OIT-supported agencies, employees of OIT, agencies
                                  supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Tier                            Standard

  Version                         3.0
  Effective Date                  07/01/2025
  Last Updated                    07/23/2026

1. Purpose
OIT is statutorily obligated to provide IT support and services to the State and its stakeholders in the
most effective and efficient manner possible (as defined by C.R.S. 24-37.5). To satisfy stakeholder
needs surrounding Enterprise Load Balancing, this document is submitted as the standard for
technology and specifications to provide the service.
The ultimate purpose of this standard is to describe the minimum requirements for designing,
installing, securing, monitoring, maintaining, protecting, and decommissioning a load balancing
service. Load balancing seeks to: distribute client requests; ensure high availability; meet demand by
increasing or decreasing scale; and facilitate continuous integration and delivery.

2. Scope
These standards apply to OIT and OIT-supported agencies. This standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to
enforce technology standardization and assist in making the usage, support, and/or purchase of
technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

                                                                                             Page 1 of 3

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Network Operations - Sr. Manager of Network Services
   ●   Owner of Standard; engages stakeholders and subject matter experts to determine the
       standard.
   ●   Updates document standards and version number.
   ●   Presents to the Architecture Review Board for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Features
   ●   SSL Session Handling: Must provide the ability to terminate SSL sessions or support SSL pass-
       through; dedicated SSL offloading on hardware-based load balancers.
   ●   Clustering: Must be deployed in a highly available cluster of at least two units, able to sync
       configurations and session data between members.
   ●   Session Awareness: Must maintain session state with backend services using Layer 3/4
       information (sticky sessions) and cookies (session- or time-based).
   ●   Balancing Methods: Must support at minimum round robin and least connections.
   ●   Health Checks: Must provide health checks to verify whether a member server is functioning,
       with configurable response (e.g., a dedicated health URL).
   ●   Resource Management: Adding and removing member servers without interrupting overall
       service must be supported, both dynamically and manually.
Design
   ●   The load balancer should have an interface placed in the same VLAN as member servers.
   ●   Services presented by the load balancer must reside behind a firewall.
   ●   The load balancer must not provide indirect access to services that would not otherwise be
       allowed.
   ●   If used in a production environment, it must also be used in an immediate pre-production test
       environment (Test/UAT/Staging).
Managing
   ●   There must be a dedicated out-of-band management interface for each member of the load
       balancer cluster.
   ●   Configurations must be manageable using a GUI and an API (or CLI in lieu of an API).

                                                                                            Page 2 of 3

Monitoring — Required Metrics
   ●   Status of member servers and member server groups.
   ●   Status of overall services presented by the load balancer.
   ●   Number of connections to overall services and to each member server.
   ●   Throughput or data counts to overall services and to each member server.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of, and approved by, the "Owner of Standard" listed under
Roles and Responsibilities.
Requests may be acquired by completing the "EXCEPTION REQUEST to Technical Standard" form and
including the completed form (with all signatures) along with other documentation required as part
of standard procedures when executing a technology procurement or service deployment.

6. References
   ●   Load balancing (computing) — Wikipedia
   ●   Cloud load balancing — Wikipedia
   ●   NGINX: What Is Load Balancing?
   ●   OSI model — Wikipedia

7. Definitions
API (Application Programming Interface): A set of routines, protocols, and tools for managing a
device, specifying how software components should interact.
CLI (Command Line Interface): A means of interacting with a network or computing device via
successive lines of text commands.
Cluster: A set of tightly connected load balancers that work together so they can be viewed as a
single system.
Cookie: A small piece of data created by a website or load balancer and stored on the user's
computer by the browser.
GUI (Graphical User Interface): A human-computer interface using windows, icons, and menus,
manipulated by a mouse, trackpad, touch screen, and/or keyboard.
Member server: A single resource behind a load balancer to which connections are given; typically
multiple member servers exist for redundancy and scale.
SSL (Secure Sockets Layer): The standard security technology for establishing an encrypted link
between a web server and a browser.

                                                                                          Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-006: Enterprise Load Balancing', links this file as https://drive.google.com/file/d/13BkR1afnErVlnDZNlelYVJdsWuSr1l5-/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=13BkR1afnErVlnDZNlelYVJdsWuSr1l5- (the source URL above).
