---
schema_version: 1
corpus: states-government-it
jurisdiction: washington
id: wa-sec-09-01-s
title: Security Logging Standard
doc_type: standard
citation: WaTech Standard SEC-09-01-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2024-09/SEC-09-01-S%20Security%20Logging%20Standard_1.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: feffa4c405aeb52961d26a58398c186952e3ed6f72c58326969a825bf841abf1
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Security Logging Standard (WaTech Standard SEC-09-01-S)

## At a glance

Item of the WaTech policy library, chapter '4. IT Security' (listed as type Standards). Listed at https://watech.wa.gov/policies/security-logging-standard.

## Full text

SEC-09-01-S                                                                                                  Replaces:
State CIO Adopted: April 1, 2024                                                       IT Security Standard 141.10 (10)
TSB Approved: June 24, 2024                                                                         December 11, 2017
Sunset Review: June 24, 2027

                           SECURITY LOGGING STANDARD
See Also:
RCW 43.105.054 WaTech Governance
RCW 43.105.052 Powers and duties of agency—Application to higher education, legislature, and judiciary.
RCW 43.105.020 (22) “State agency”
RCW 43.105.450 Office of Cybersecurity
SEC-04-02-S Media Sanitization and Disposal
NIST 800-171 Protecting Controlled by Unclassified Information in Nonfederal Systems and Organizations.

    1. Agencies must configure their information technology systems and networks to
       generate security logs (See NIST 800-92 - Guide to Computer Security Log
       Management).

            a. Data contained in security logs is considered Category 3 data and is exempt
                from public records disclosure per RCW 42.56.420. See SEC-08-01-S Data
                Classification Standard.

            b. Agencies must configure the following systems to log information,
               exceptions, and user account activity necessary to reconstruct security
               events:

                     i. Security software.

                     ii. Antivirus software.

                     iii. Firewalls

                     iv. Intrusion detection and prevention systems.

                     v. Operating systems and servers.

                     vi. Workstations.

                     vii. Network equipment.

                     viii.Applications.

                     ix. Management decision stated as a sentence.

                                                                                                                 1

2. Each log entry must include the following data, where available:

      a. Account / User ID

      b. Port Number

      c. Type of event

      d. Success or failure of the event

      e. Date and time of the event (timestamp)

      f. Source and Destination IP addresses

3. Agencies must configure agency security log generation processes to notify
   agency security administrators in the event of a log generation error. Alerts must
   be auditable and as close to real time as possible. See SEC-09 Audit and
   Accountability Policy.

4. Agencies must harden their logging infrastructure according to the SEC-04-03-S
   Configuration Management Standard.

5. Agencies must protect agency security logs from unauthorized access,
   modification, and deletion.

6. Agencies must retain the agency’s security logs for at least one year. See
   Washington Secretary of State’s General Records Retention Schedule.

      a. Agencies must ensure retained security logs are not corrupted.

      b. Agencies may need to meet longer log retention criteria due to Criminal
         Justice Information Services (CJIS) and Health Insurance Portability and
         Accountability Act (HIPAA) requirements.

      c. Agencies must develop and document a process to provide for log
          preservation requests, such as a legal requirement to prevent the alteration
          and destruction of log records.

REFERENCES

   1. Definitions of Terms Used in WaTech Policies and Reports.
   2. NIST Special Publication 800-92 Guide to Computer Security Log
      Management.
   3. RCW 42.56.420— Security.

                                                                                     2

  4. SEC-08-01-S Data Classification Standard.
  5. SEC-09 Audit and Accountability Policy.
  6. SEC-04-03-S Configuration Management Standard.
  7. Washington Secretary of State’s General Records Retention Schedule.
  8. NIST Cybersecurity Framework Mapping:
        • PROTECT.PROTECTIVE TECHNOLOGY-1: Audit/log records are
           determined, documented, implemented, and reviewed in accordance
           with policy.
        • DETECT.ANOMOLIES AND EVENTS-3: Event data are collected and
           correlated from multiple sources and sensors.

CONTACT INFORMATION

  •   For questions about this policy, please email the WaTech Policy Mailbox.

                                                                                 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
