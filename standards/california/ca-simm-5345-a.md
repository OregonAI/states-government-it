---
schema_version: 1
corpus: states-it-governance
jurisdiction: california
id: ca-simm-5345-a
title: Vulnerability Management Standard
doc_type: standard
citation: SIMM 5345-A
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5345-A-Vulnerability-Management-Standard.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 29656156c8038d4b2ab1365031cea4fcda52e2204ef30ed921450fa2c285afca
effective_date: null
source_version: April 2025
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). source_version is the month, or the revision month, the document prints (a month with no day
  is not made into a date).
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

# Vulnerability Management Standard (SIMM 5345-A)

## At a glance

SIMM 5345-A, Vulnerability Management Standard: an item of the Office of Information Security's information security series (SIMM 5300), the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

               State of California

          Department of Technology

Vulnerability Management Standard
  Statewide Information Management Manual – 5345-A

                     April 2025

                                                     Table of Contents

Document History ......................................................................................................... 2

Introduction ................................................................................................................... 3

   Purpose........................................................................................................................ 3

   Scope ........................................................................................................................... 3

   Compliance .................................................................................................................. 3

Protection Capabilities..................................................................................................... 4

Detection Capabilities...................................................................................................... 4

Investigative Support Capabilities ................................................................................... 5

Containment Capabilities ................................................................................................ 6

Remediation Capabilities................................................................................................. 6

Questions ........................................................................................................................ 7

References ...................................................................................................................... 7

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                                                 April 2025                                                     Page | 1

Document History
Revision           Date of Release         Owner                 Summary of Changes
                                                             New Standard in support of SAM
                                     Office of Information
    1.0             January 2021                             Section 5345, Vulnerability And
                                        Security (OIS)
                                                             Threat Management
                                                             Corrected name and reference to
                                                             Security Event Notification
    1.1               April 2021             OIS
                                                             and Response Protocols (SIMM
                                                             5335-A).
                                                             Reformatted to match current
                                                             template, removed references to
    1.2               April 2025             OIS             services no longer offered by
                                                             California Department of
                                                             Technology.

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                           April 2025                                  Page | 2

Introduction

Purpose

The term "vulnerability" is framed within the concept of "susceptible to attack" or
"assailable". State entities shall continuously identify, investigate reports of, and
remediate vulnerabilities affecting their IT assets before they can be exploited.
Vulnerability management are the processes by which the continuous identification,
tracking, reporting, and remediation of vulnerabilities that exist within those IT assets
are conducted. IT assets are physical and virtual, hardware and software, processing,
networking, and storage in nature, and may exist either within a state entity’s direct
control or outside (e.g. cloud).

Scope

This standard applies to all California state entities, including agencies, departments,
divisions, bureaus, boards, and commissions, as defined in Government Code Section
11546.1.

Compliance

As outlined in Government Code (GC) Section 11549.3, the Office of Information
Security (OIS) is entrusted with creating, issuing, and maintaining policies, standards,
and procedures, overseeing information security risk management for agencies and
state entities, providing information security and privacy guidance, and ensuring
compliance with State Administrative Manual (SAM) Chapter 5300 and Statewide
Information Management Manual (SIMM) section 5300.

State entities must adhere to OIS-issued information security and privacy policies and
all relevant laws, regulations, rules, and standards governing their state entity.
Compliance may be reflected in audit findings and maturity scores. Non-compliance will
be addressed according to the Office of Information Security Policy Compliance and
Enforcement Standard (SIMM 5330-H).

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                               April 2025                                    Page | 3

Minimum Vulnerability Management Requirements

Protection Capabilities
   •   Be able to assign assets to groups.
   •   Be able to assign assets to multiple groups.
   •   Be able to generate reports based on asset groups.
   •    Be able to assign asset grouping automatically based on OS/application in
       addition to manual assignment.
   •   Support access controls to limit users’ visibility and change privileges to specific
       groups of assets.

Detection Capabilities
The vulnerability management and scanning technologies and processes used by state
entities shall (at a minimum):

   •   Be able to scan assets from inside the enterprise perimeter firewall.
   •   Be able to scan internet-facing assets from the internet.
   •   Indicate which vulnerabilities of an asset are exploitable from both outside and
       inside the network and which are only exploitable from the inside.
   •   Support credentialed and non-credentialed scanning.
   •   Support credentialed scanning for Windows, Linux, AIX, and commonly used
       network devices.
   •   Support middleware vulnerability detection for products like Microsoft SQL,
       Oracle, WebSphere, Apache web services, IIS…
   •   Be able to perform Dynamic Application Security Testing (DAST) and scan web-
       based applications for Open Web Application Security Project (OWASP) Top Ten.
   •   Be able to scan web-based interfaces and Application Programming Interfaces
       (API), to include HTTP, WebSocket, JSON, XML, REST, SOAP.
   •   Be able to exchange vulnerability data with department Security Information and
       Event Management system(s) using automated processes.

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                              April 2025                                  Page | 4

Investigative Support Capabilities
The investigative functions of the vulnerability management and scanning technologies
and processes must include a historical timeline of all detections and apparent
remediation of specific vulnerabilities and shall (at a minimum):

   •   Be able to search for specific vulnerabilities and retrieve a list of assets with
       those vulnerabilities.
   •   Be able to search for specific assets by hostname or IP and receive a list of all
       vulnerabilities on that asset.
   •   Be able to generate a report showing all vulnerabilities and assets within a
       specific user-defined or automated group.
   •   Be able to generate a report of the most critical external vulnerabilities, including
       the related assets that are vulnerable.
   •   Be able to limit reports to external vulnerabilities only, internal vulnerabilities only,
       or combined vulnerabilities
   •   Have clearly defined risk values for assets and vulnerabilities and be able to use
       those for reporting.
   •   Be able to generate a report of most critical vulnerabilities across the system or
       by user-defined or automated group.
   •   Be able to generate a report of the most critical assets across the system or by
       user-defined or automated group.
   •   Be able to generate aging reports of open vulnerabilities.
   •   Be able to provide continuous real-time results and reporting of existing and
       closed vulnerabilities.
   •   Be able to generate a risk state of the various asset groups as well as the entire
       enterprise.
   •   Be able to respond to vulnerability reports from the California Department of
       Technology, Office of Information Security, Security Operations Center and other
       external parties in accordance with the Security Event Notification and Response
       Protocols, SIMM 5335-A.

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                                April 2025                                   Page | 5

Containment Capabilities
There are no containment capabilities that are at a minimum required by the
vulnerability management and scanning technologies and processes.

Remediation Capabilities
The remediation functions of the vulnerability management and scanning technologies
and processes must (at a minimum):

   •   Maintain a registry of all detected and un-remediated vulnerabilities.
   •   Provide both automated and manual methods to show that vulnerabilities have
       been remediated.
   •   Allow different groups to manage the vulnerabilities based on assigned groups.
   •   Integrate with bug tracking and configuration management platforms.
   •   Record how remediation of a vulnerability was affected.

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                              April 2025                             Page | 6

Questions
Questions regarding this standard may be sent to:

California Department of Technology

Office of Information Security

Security@state.ca.gov

References
   •   SAM 5345: https://www.dgs.ca.gov/en/Resources/SAM/TOC/5300
   •   SIMM 5335-A: https://cdt.ca.gov/policy/simm/

Office of Information Security
Vulnerability Management Standard
SIMM 5345-A                            April 2025                   Page | 7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the month, or the revision month, the document prints (a month with no day is not made into a date).
