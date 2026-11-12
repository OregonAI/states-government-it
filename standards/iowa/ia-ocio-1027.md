---
schema_version: 1
corpus: states-government-it
jurisdiction: iowa
id: ia-ocio-1027
title: State of Iowa - Data Backup Operational Standard
doc_type: standard
citation: Iowa OCIO State of Iowa - Data Backup Operational Standard, September 2, 2014
authority_level: ''
issuing_body: Iowa Department of Management (Office of the Chief Information Officer)
source_url: https://ocio.iowa.gov/media/1027/download?inline
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 60f4f95c6c058ba3c0ea074768f8e8d48110fdbdc59f3ff9b449fb7839a9c2d2
effective_date: '2014-09-02'
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
- data
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# State of Iowa - Data Backup Operational Standard (Iowa OCIO State of Iowa - Data Backup Operational Standard, September 2, 2014)

## At a glance

Requires state agencies to back up operational and historic electronic data and to be able to restore it after a disaster.

## Full text

                                                                                 STATE OF IOWA
TERRY E. BRANSTAD, GOVERNOR                                                                   ROBERT VON W OLFFRADT
KIM REYNOLDS, LT. GOVERNOR                                                                 CHIEF INFORMATION OFFICER

                                 State of Iowa - Data Backup Operational Standard
                                                  September 2, 2014

Purpose

To prevent the loss of all operational and historic electronic data in the custody of the State by ensuring timely
backup and data restoration capability in case of disaster.

Overview

The State of Iowa is dependent on electronic data to conduct government business. In emergency disaster
efforts Iowa’s citizens hold State government to the highest standard for data availability, retention and
restoration of backup data to operational status in the shortest time possible.

State government is accountable for exercising effective data backup best practices. State of Iowa agencies
are responsible for the following: determining the criticality of data, data backup schedules, data backup
capability, security of data backup media, data storage requirements, offsite storage requirements, and data
restoration schedules based on agency disaster and contingency plans.

Each agency shall incorporate data backup and data restoration into business plans and development plans.

Scope

All State of Iowa participating agencies, and their vendors that host\store state data, shall meet the
requirements of this standard. This standard does not apply to cloud based service providers.

This standard applies to all participating agencies as defined by Iowa Code 8A.101 and in support of SF396
passed by the 85th Iowa General Assembly. Non-participating agencies are encouraged to follow the
guidelines in this and other enterprise level policies, standards, guidelines, processes and procedures.

Definitions

Selected terms used in the Data Backup Standard are defined below:

       AES 256 - the Advanced Encryption Standard specifies a U.S. Government-approved cryptographic
        algorithm that can be used to protect electronic data. The AES algorithm is a symmetric block cipher
        that can encrypt (encipher) and decrypt (decipher) information.
       Contingency Plan – Management policy and procedures designed to maintain or restore business
        operations, including computer operations, possibly at an alternate location, in the event of
        emergencies, system failures, or disaster.
       Data Backup – refers to making copies of data that may be used to restore the original data after a
        data loss event.

HOOVER STATE OFFICE BUILDING, LEVEL B, 1305 E. W ALNUT, DES MOINES, IOWA 50319    515.281.5503      CIO@IOWA.GOV

                                                                                 STATE OF IOWA
TERRY E. BRANSTAD, GOVERNOR                                                                   ROBERT VON W OLFFRADT
KIM REYNOLDS, LT. GOVERNOR                                                                 CHIEF INFORMATION OFFICER

Elements

The following are elements of the Enterprise Data Backup Operation Standard:

    1. Each agency shall establish backup policies and procedures.
    2. Data backup shall be used for the purpose of disaster recovery and file restoration. This standard does
       not satisfy records management\retention laws or policies.
    3. Each agency will establish and follow written procedure for the conduct of data backup addressing the
       following areas:
            o data backup hardware
            o software configuration
            o technician training
            o technician data backup procedures
            o data identified for back-up
            o data backup schedules
            o vendor support
            o security measures
            o data backup media requirements
            o approved off-site storage facilities
            o restoration plans
            o restoration schedules
            o technician restoration procedures
            o emergency procurement plans.
    4. Each agency shall establish metrics for minimum acceptable condition (retentivity, rewrites, and optical
       longevity) of storage media before committing backup data to storage.
    5. Each agency shall test data backup and restoration procedures for hardware and software applications.
       Data backup recovery plans shall be exercised at least once a year. The restoration exercise must
       consider risk and not interfere with current operations.
    6. Each agency shall encrypt backup confidential (as defined in Iowa Code Chapter 22.7) data in transit
       and at rest. Media containing backup data shall be encrypted. A minimum of AES 256 shall be used.
    7. Each agency conducting data backup for other agencies will establish agreements with each other in
       accordance with applicable State of Iowa IT standards and requirements:
            o lines of communication
            o security reviews
            o audit log analysis
            o security incident reporting/response
            o contingency plans
            o change management
            o security plan maintenance
            o planned disconnection
            o emergency disconnection
            o restoration of interconnection
            o data restoration
            o data backup systems policy
            o data integrity
            o expected behavior of the data backup service(s).
    8. Collaboration between agencies is strongly encouraged to minimize the number of unique systems and
       implementations to reduce costs for taxpayers.

HOOVER STATE OFFICE BUILDING, LEVEL B, 1305 E. W ALNUT, DES MOINES, IOWA 50319    515.281.5503      CIO@IOWA.GOV

                                                                                 STATE OF IOWA
TERRY E. BRANSTAD, GOVERNOR                                                                   ROBERT VON W OLFFRADT
KIM REYNOLDS, LT. GOVERNOR                                                                 CHIEF INFORMATION OFFICER

    9. Each agency shall ensure data backup data remains available to support agency requirements.
    10. Agencies shall determine criticality of data and systems.

Updates: This document shall be reviewed at least every two years and updated as needed.

Effective Date: This revised standard shall be effective September 2, 2014.

Enforcement: This standard shall be enforced pursuant to Iowa Code 8B.21.

Waiver: A wavier may be submitted to the State’s Chief Information Officer as defined in Iowa Code 8B.21.5.

HOOVER STATE OFFICE BUILDING, LEVEL B, 1305 E. W ALNUT, DES MOINES, IOWA 50319    515.281.5503      CIO@IOWA.GOV

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
