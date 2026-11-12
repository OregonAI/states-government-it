---
schema_version: 1
corpus: states-government-it
jurisdiction: oklahoma
id: ok-std-server-backup
title: Server Backup Standard
doc_type: standard
citation: OMES Server Backup Standard
authority_level: ''
issuing_body: Office of Management and Enterprise Services, Information Services
source_url: https://oklahoma.gov/content/dam/ok/en/omes/documents/server-backup-standard-UA.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 6590ffaad17ac812b08acc4f61113a6c9b47baec8f5f9c0bb8ef295f6e129426
effective_date: '2024-10-08'
source_version: Last revised 09/20/2024
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

# Server Backup Standard (OMES Server Backup Standard)

## At a glance

A CIO standard in the 'Network and Servers' group of the OMES statewide IT policy and standards library, binding on state agencies under the Information Technology Consolidation and Coordination Act. Its Purpose or Introduction, as printed: This document establishes the OMES standard of performing server backups.

## Full text

                                     Server Backup Standard

Introduction
All OMES servers perform nightly backups. Once the backup completes that data is then replicated
to an offsite location for a second copy of the data. The second copy of data will be used in case of
corruption of data in the initial backup of data and for disaster recovery purposes.

Purpose
This document establishes the OMES standard of performing server backups.

Definitions
Backup – to make a copy of a file.

Standard
The OMES Data Recovery Team will determine the best way to back up the server then configure
the server to perform scheduled nightly backups. The OMES Data Recovery Team will verify the
backups complete daily. In the event a backup is missed or fails, the OMES Data Recovery Team
will troubleshoot the event and correct any problems. After nightly backups complete, processes
are then running that will replicate the data to an offsite location. The second copy of the data is
stored not only for a backup copy but will also be used in case a disaster recovery event should
occur. Once the server is scheduled for decommission, the OMES Data Recovery Team will remove
the server from its associated backup schedule and schedule the full deletion of data and server
definitions that have been created on the backup server. Decommissioned server data will be
retained based on requirements of the agency’s data retention schedule.

Compliance
This standard shall take effect upon publication and is made pursuant to Title 62 O.S. §§ 34.11.1
and 34.12 and Title 62 O.S. § 35.8. OMES IS may amend and publish the amended standards
policies and standards at any time. Compliance is expected with all published policies and
standards, and any published amendments thereof. Employees found in violation of this standard
may be subject to disciplinary action, up to and including termination.

Rationale
To coordinate and require central approval of state agency information technology purchases and
projects to enable the chief information officer to assess the needs and capabilities of state
agencies as well as streamline and consolidate systems to ensure that the state delivers essential
public services to its citizens in the most efficient manner at the lowest possible cost to taxpayers.

Revision history
This standard is subject to periodic review to ensure relevancy.
 Effective date: 10/08/2024           Review cycle: Annual
 Last revised: 09/20/2024             Last reviewed: 10/21/2026
 Approved by: Dan Cronin, Chief Information Officer

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
