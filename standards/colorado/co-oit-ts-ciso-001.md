---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-ciso-001
title: Authentication & Account Management Standard v. 2026
doc_type: standard
citation: TS-CISO-001
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1xP0en_2kUgVSXDyJmERqLFTX_agiaIae
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 3fb17ddaf7ed0d143ac42c788e0daeec7fee60acb5914cbb7d59aa9e983b9cdc
effective_date: '2026-02-01'
source_version: 4.0, last updated 05/14/2026
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads 'TS-CISO-001 Authentication & Account Management Standard v. 2026', links this file
  as https://drive.google.com/file/d/1xP0en_2kUgVSXDyJmERqLFTX_agiaIae/view?usp=sharing; the text was
  fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1xP0en_2kUgVSXDyJmERqLFTX_agiaIae
  (the source URL above).
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

# Authentication & Account Management Standard v. 2026 (TS-CISO-001)

## At a glance

OIT technical standard TS-CISO-001 (Information Security): Authentication & Account Management Standard v. 2026. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-CISO-001: Authentication & Account
Management Standard
  Document ID                    TS-CISO-001
  Title                          Authentication & Account Management Standard v. 2026
  Executive Sponsor              Jill Fraser, Chief Information Security Officer
  Issuing Authority              Governor’s Office of Information Technology (OIT)
  Applies to                     All state government agencies, employees, contractors, vendors,
                                 and external users who access state government information
                                 systems and applications, regardless of location or device,
                                 including all applications, hosting environments, and physical and
                                 connected technologies.
  Instrument Type                Standard
  Version                        4.0
  Effective Date                 02/01/2026
  Last Updated                   05/14/2026

Purpose
This standard defines security requirements for secure access and account management
across all state information systems and applications, including on-premises and cloud
environments. It supports compliance with the Colorado Information Security Policies (CISPs).

Scope
This standard applies to all state government agencies, employees, contractors, vendors, and
external users who access state government information systems and applications, regardless
of location or device. This includes all applications and hosting environments, and access to
physical and connected technologies.
The appropriate authentication and account management standard security requirements are
listed below. Additional requirements must be implemented based on the regulated data
type(s).

Requirements
User Account Lifecycle Management
A standard operating procedure must be in place for all phases of a user account's existence:
creation, modification, disablement, and deletion. Accounts inactive for 90 days must be
routinely identified, monitored, and appropriately managed.

                                                                                   Page 1 of 4

Account Types
The standard recognizes two main types of accounts (basic and advanced):
   ●   Basic User Accounts: Standard accounts used for accessing State Information Systems
       and services, such as email, without administrative privileges.
   ●   Advanced Accounts: Accounts with elevated or non-personal access used for
       administrative tasks, system-level functions, or automated service operations. This
       category includes Privileged User Accounts (e.g., administrator or root) and Service
       Accounts.

Password Management – Baseline Requirements
   ●   Password Requirement: All accounts must be protected by a password. Password-less
       accounts are strictly prohibited.
   ●   Password Expiration: All account passwords must expire in accordance with an
       established and approved password expiration policy or Standard Operating Procedure
       (SOP).
   ●   Password Changes and Resets: Passwords must be changed immediately if compromise
       is suspected. In all other circumstances, password changes or resets may occur only
       upon request and after verification of identity and authorization.
   ●   Secure Password Communication: Passwords and password reset credentials must be
       communicated using secure methods, including but not limited to in-person delivery,
       HTTPS-secured communication, or encrypted email.
   ●   Password Confidentiality: Passwords must not be shared with, disclosed to, or
       accessible by anyone other than the authorized account owner or designated system
       process.
   ●   Initial Password Provisioning: For newly created accounts where an initial password is
       required for provisioning or onboarding, the password must be communicated securely
       and must be changed upon first use.

Basic User Account Passwords
The Office of Information Technology (OIT) is responsible for the establishment and
mandatory enforcement of minimum password complexity requirements. Agencies are
provided with these as options; OIT default requires Standard Option 1. All Basic User
Accounts must meet one of the two minimum standards below.
 Standard              Length        Complexity                       Expiration    Reminder
 Standard Option 1     Minimum ten   Must contain at least one (1)    Every         Users
 (Complex Password)    (10)          character from each category:    ninety (90)   receive a
                       characters.   uppercase letters, lowercase     days or       reminder
                                     letters, numeric digits, non-    when a        fourteen
                                     alphanumeric characters          compromis     (14) days
                                     (symbols/punctuation).           e is          prior to
                                                                      suspected.    expiration.
 Standard Option 2     Minimum       No additional complexity         Every three   Users
 (Long Password) —     twenty-four   requirements beyond length (no   hundred       receive a
 note: some            (24)          mandatory uppercase,             sixty-five    reminder
 regulatory            characters.   lowercase, numeric, or           (365) days    fourteen
 compliances do not                  symbols).                        or when a     (14) days
 currently allow                                                      compromis     prior to
 Option 2                                                             e is          expiration.
                                                                      suspected.

                                                                                    Page 2 of 4

New Users: For onboarding of new employees, where a hiring authority may receive a
temporary password, the password must be shared securely with the new employee. The new
employee must create a new password right away upon first login.

Advanced Account Passwords – Elevated Privilege Account Passwords

 Requirement              Detail
 Length                   Minimum sixteen (16) characters.
 Complexity               Must contain at least one (1) character from each category: uppercase
                          letters, lowercase letters, numeric digits, non-alphanumeric characters
                          (symbols/punctuation).
 MFA                      Required for all accounts with elevated privileges and all remote access.
 Expiration               Every ninety (90) days.
 Reminder                 Users receive a reminder fourteen (14) days prior to expiration.

Service Account Passwords
Starting March 1, 2026, all newly created service accounts will be required to meet the
following:
 Requirement              Detail
 Length                   Minimum twenty-four (24) characters.
 Complexity               Must contain at least two (2) characters from each of the following
                          categories: uppercase letters, lowercase letters, numeric digits, non-
                          alphanumeric characters (symbols/punctuation).
 Usage Restriction        No interactive logins.
 Storage                  Passwords must be securely stored in the designated password repository
                          associated with the service.
 Expiration               Every three hundred sixty-five (365) days or when a compromise is
                          suspected.

All default vendor passwords must be reset prior to connecting to the network and are
required to meet the requirements of elevated privilege passwords.

Multi-Factor Authentication (MFA) Requirements
   ●   The MFA solution must be configured according to vendor best practice guidance.
   ●   MFA is required for all accounts with elevated privileges and all remote access.
   ●   If a hardware MFA device is used, the devices must be securely issued, replaced,
       revoked, and disposed of when needed.

Exceptions
All exceptions must be documented, justified, and approved by the State of Colorado's Chief
Information Security Officer (CISO) or other designated authority. Compensating controls must
be documented, implemented, and maintained.

                                                                                         Page 3 of 4

Compliance
The Information Security Office will monitor and advise on compliance with this standard.

References
   ●   Password & Account Compliance Requirements
   ●   Guidance for Creating Secure Passwords
   ●   Encryption Standard TS-CISO-006

                                                                                  Page 4 of 4

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-CISO-001 Authentication & Account Management Standard v. 2026', links this file as https://drive.google.com/file/d/1xP0en_2kUgVSXDyJmERqLFTX_agiaIae/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1xP0en_2kUgVSXDyJmERqLFTX_agiaIae (the source URL above).
