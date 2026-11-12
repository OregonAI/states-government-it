---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-application-authentication
title: Application Authentication Standard
doc_type: standard
citation: OMES Application Authentication Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/application-authentication-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 20469f8967c4971685f94e4818f7471023cd1c2f0420a449b7c2242d7e8facee
effective_date: '2025-05-23'
source_version: Last revised 05/23/2025
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

# Application Authentication Standard (OMES Application Authentication Standard)

## At a glance

A CIO standard in the 'Security' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document outlines the SSO requirements for all applications and services utilized by the State of Oklahoma.

## Full text

                             Application Authentication Standard

Introduction
Application authentication is the process of verifying user identity to confirm only the right people,
services and applications with the right permissions can obtain organizational resources. Single
sign-on (SSO) is an application authentication scheme allowing users to log in to multiple sites and
services with a single set of credentials. SSO users log in once and can access multiple services
without re-entering authentication factors. This helps user productivity by reducing the number of
authentication prompts needed to access multiple applications. SSO also provides support for
Multi-Factor Authentication to further protect state resources by verifying the identity of the user
requesting access.

Purpose
This document outlines the SSO requirements for all applications and services utilized by the State
of Oklahoma.

Definitions
   • Authentication factors – categories of evidence a person must present verifying they are
        who they say they are. The most common are knowledge, possession and inherence
        (something you know (password), something you have (e.g., mobile phone) and something
        you are (e.g., fingerprint).
   • Life safety system – an interior building element designed to protect and evacuate the
        building population in emergencies, including fire and tornadoes and less critical events
        such as power failures.
   • MFA – multi-factor authentication; an authentication protocol requiring two different types
        of authentication (e.g., password, biometrics, authenticator application, etc.).
   • SSO – single sign-on; an authentication method allowing users to log in with a single ID to
        several related software systems.
   • TLS – Transport Layer Security; an authentication and encryption protocol widely
        implemented in browsers and web servers.

Standard
The State of Oklahoma requires all applications and services with a logon component to adhere to
the following guidelines:
    • Applications must use a standard State of Oklahoma SSO provider aligned with the type of
         application and user audience or an alternative approved by OMES-ISD.
    • All applications must use multi-factor authentication using two different authentication
         factors.
    • Applications must use TLS 1.2 or greater to encrypt authentication and application data in
         transit over the network.
    • Applications and systems flagged as life safety or otherwise critical systems must have
         redundant authentication systems to ensure availability during a crisis.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§ 34.11.1
and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended standards
policies and standards at any time. Compliance is expected with all published policies and
standards, and any published amendments thereof. Employees found in violation of this standard
may be subject to disciplinary action, up to and including termination.

Rationale
To ensure efficient, secure, and cost-effective delivery of essential public services, all state agency
IT purchases and projects must receive central approval. This allows the Chief Information Officer
to evaluate agency needs and capabilities, strengthen data protection and security, and streamline
and consolidate systems to reduce costs for taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.

 Effective date: 05/23/2025           Review cycle: Annual
 Last revised: 05/23/2025             Last reviewed: 09/02/2026
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
