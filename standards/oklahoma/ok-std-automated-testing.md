---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-automated-testing
title: Automated Testing Standard
doc_type: standard
citation: OMES Automated Testing Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/automated-testing-standard-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: f584a81786bc4a0601e1c7b4d75decddaf1494ecdd212a2c3243bd762cfcd815
effective_date: '2022-12-14'
source_version: Last revised 03/23/2026
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
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Automated Testing Standard (OMES Automated Testing Standard)

## At a glance

A CIO standard in the 'IT Enterprise Governance' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document establishes the requirements and procedures for the quality assurance division of OMES.

## Full text

                                 Automated Testing Standard

Introduction
State employees, agencies and external partners have an ever-increasing need for testing web-
based applications and websites for errors, broken links and security risks. OMES is committed
to solving these issues using automated software that would relieve users of repetitive tasks
while also testing the integrity and working functionality of the websites and web applications.

Purpose
This document establishes the requirements and procedures for the quality assurance division
of OMES.

Definitions
API – application programming interface.
REST API (RESTful API or RESTful web service) – a software architectural style for an
application program interface that uses HTTP requests to access and use data. REST is a
widely accepted set of guidelines for creating stateless, reliable web APIs.
Mobile device – a portable computing device that has a small form factor such that it can easily
be carried by a single individual; is designed to operate without a physical connection (e.g.
wirelessly transmit or receive information); possesses local, non-removable data storage; and
includes a self-contained power source. Mobile devices may also include voice communication
capabilities, on-board sensors that allow the devices to capture information or built-in features
that synchronize local data with remote locations. Examples include smartphones, tablets and
e-readers.
User interface (UI) – how the user and a computer system interact.
Performance testing – a non-functional software testing technique that determines how the
stability, speed, scalability and responsiveness of an application performs under a given
workload.

Standard
The automated tools approved for application testing are listed below:
*Only the versions listed have been approved by OMES CyberCommand

   •   User interface.
          o Katalon Studio.
          o Katalon Recorder.
          o SauceLabs.
          o Selenium WebDriver.
          o Selenium IDE
   •   Mobile device testing.
          o Katalon Studio.
          o SauceLabs.
   •   REST API.

          o Katalon Studio.
          o Postman.
          o Swagger.
          o Advanced REST Client by Mulesoft.
   •   Performance testing (load, stress, value).
          o Apache JMeter.
          o Azure Load Testing.
          o BlazeMeter Chrome Extension.
          o Locust ver. 2.33.0.
   •   IDE.
          o Eclipse.
          o IntelliJ (Java JDK).
          o Java SDK.
          o Maven.
          o Python.
          o PyTest.
   •   Container orchestration
          o Docker ver. 24.0.
          o Kubernetes ver. 1.28.0.
   •   Cross-platform tools/environments.
          o Appium ver. 2.0.
   •   Optical Character Recognition
          o Tesseract ver. 5.5.0.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§
34.11.1 and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended
standards policies and standards at any time. Compliance is expected with all published policies
and standards, and any published amendments thereof. Employees found in violation of this
standard may be subject to disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases
and projects to enable the chief information officer to assess the needs and capabilities of state
agencies as well as streamline and consolidate systems to ensure that the state delivers
essential public services to its citizens in the most efficient manner at the lowest possible cost to
taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 12/14/2022         Review cycle: Annual
 Last revised: 03/23/2026           Last reviewed: 03/23/2026
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
