---
schema_version: 1
corpus: states-government-it
jurisdiction: missouri
id: mo-firewall-administration-cc
title: Firewall Administration
doc_type: standard
citation: 'Security Domain Compliance Component: Firewall Administration'
authority_level: ''
issuing_body: Office of Administration, Information Technology Services Division
source_url: https://itsd.oa.mo.gov/sites/g/files/zuston256/files/media/pdf/2025/04/CC-FirewallAdminARCApp.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 86303261325f1bd27643ff3c7a4dde11a59aa264dece357213956e27249dc3b9
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

# Firewall Administration (Security Domain Compliance Component: Firewall Administration)

## At a glance

Row 'Firewall Administration' of the Security Domain's Approved Standards page (https://itsd.oa.mo.gov/it-governance/enterprise-architecture/security-domain/approved-standards-security-domain), the statewide IT security standards library of ITSD's enterprise architecture. Its viewer page is https://itsd.oa.mo.gov/media/pdf/firewall-administration-cc; the PDF address is the file that viewer page embeds. A 'Compliance Component' document of the Security Domain framework. Printed status (read by rendering the PDF page, because the check boxes are drawn marks with no text layer) is classification Current and status Approved, with Date Approved / Rejected 06/08/2004. The index lists it as an approved standard.

## Full text

                                            C
                                            Coom
                                               mpplliiaannccee C
                                                               Coom
                                                                  mppoonneenntt

                                                   D
                                                   DEEFFIIN
                                                          NIITTIIO
                                                                 ONN
Name           Firewall Administration
               Firewall Administration is ensuring the proper management, configuration, and
               change management of the firewall. It is comprised of controlling access to the
Description
               platform, platform operating system builds, log reviews, time synchronization and
               backups.
               Given the critical role of firewalls, the manner in which they are managed and
Rationale
               maintained is crucial to the agency’s security posture.
                      •   Allows for consistent operation of the network
                      •   Assists in preventing lapses in confidentiality, availability and integrity of all
                          the agency’s systems and data

Benefits
               NOTE:
                      •   Firewall Administration requires specialized training
                      •   Firewalls are vulnerable to mis-configurations and the failure to properly
                          apply needed patches or other security enhancements
                                   A
                                   ASSSSO
                                        OCCIIA
                                             ATTEED
                                                  DAARRC
                                                       CHHIITTEEC
                                                                CTTU
                                                                   URREE LLEEVVEELLSS
List the Domain Name      Security
List the Discipline
                          Technical Controls
Name
List the Technology
                          Secure Gateways and Firewalls
Area Name
List Product
Component Name
                                      C
                                      COOM
                                         MPPLLIIA
                                                ANNC
                                                   CEE C
                                                       COOM
                                                          MPPO
                                                             ONNEEN
                                                                  NTT TTYYPPEE
Document the
Compliance                Guideline
Component Type
Component Sub-type
                                             C
                                             COOM
                                                MPPLLIIA
                                                       ANNC
                                                          CEE D
                                                              DEETTA
                                                                   AIILL
                          Access to the Firewall Platform
                              •   Access to the firewall console and any graphic management interface
                                  shall be controlled through the use of encryption, or restriction of
State the Guideline,              access by IP address combined with user authentication.
Standard or Legislation              o Encryption may be in the form of internal encryption, Secure
                                          Sockets Layer (SSL) encryption or tunneling solutions such as
                                          the Secure Shell (SSH).
                                     o IP address restriction shall be combined with user
                                          authentication such as:

                  •   an individual userID and password,
                  •   a single administration account and its password,
                  •   token-based authentication, or
                  •   a centralized authentication server such as RADIUS or
                      TACACS/TACACS+.
Firewall Platform Operating System Builds
   •   Firewall operating system builds shall be based upon minimal feature
       sets.
           o All unnecessary operating system features, especially
              compilers, shall be removed from the build prior to firewall
              implementation.
           o All appropriate operating system patches should be applied
              before any installation of firewall components.
           o Any unused networking protocols shall be removed from the
              firewall operating system build.
           o Any unused network services shall be removed or disabled.
   •   Any unused applications shall be removed or disabled.
   •   Any unused user or system accounts shall be removed or disabled.
   •   Patches shall always be tested on a non-production system prior to
       rollout to any production systems. This pre-rollout testing shall
       include several specific events:
           o A change of the system time (minute-by-minute, and hour-by-
               hour).
           o A change of the system date (both natural, and manual).
           o Adding and deleting of appropriate system users and groups.
           o Startup and shutdown of the operating system.
           o Startup and shutdown of the firewall software itself.
           o System backups, if appropriate.
   •   Unused physical network interfaces shall be disabled or removed from
       the appliance chassis.
Firewall Logging
   •   Firewalls shall provide a logging functionality. A logging program or
       daemon is available for nearly all major operating systems, including
       Windows NT, 2000 and XP, and all UNIX and Linux variants.
   •   All logging environments shall provide input to intrusion detection and
       forensic analysis packages, if available.
   •   Firewall administrators should review the logs daily.
Time Synchronization
   •   All firewalls and other logging systems, such as intrusion detection
       systems, should employ time synchronization in order to reconstruct
       security incidents.
Firewall Backups
   •   Firewalls shall be backed up immediately prior to production release.
   •   All firewall backups shall be full backups.

                         •   Firewalls shall use their own backup device. Media shall not be left in
                             the device unless a backup is being performed.
                         •   Firewalls shall not be backed up to a centralized backup server, as
                             this would present a high risk to the privacy of the backups.
                         •   It is desirable to deploy firewalls that have all critical file systems
                             burned to CDROM. (However, deployment of Windows-based
                             firewalls with read-only file systems is not possible at this time.)
                      Change Management
                         •   Management shall authorize all modifications to the firewall before
                             implementation.
                         •   Administrators shall keep a log to track inspections and modifications
                             of the firewall.
                         • Administrators should stay current on vulnerabilities and incidents.
Document Source       NIST Special Publication 800-41, Guidelines on Firewalls and Firewall Policy
Reference #              (Jan 2002) (found at www.csrc.nist.gov)
                                         Standard Organization
                      NIST Federal Information                      www.csrc.nist.gov/publications/fips/
Name                                                    Website
                      Processing Standards                          index.html
Contact Information   inquiries@nist.gov
                                            Government Body
                      National Institute of
                      Standards and Technology
                                                                    www.csrc.nist.gov/publications/fips/
Name                  (NIST), Computer                  Website
                                                                    index.html
                      Security Resource Center
                      (CSRC)
Contact Information   inquiries@nist.gov
                                               KKEEYYW
                                                     WOORRD
                                                          DSS
                      Ports, sockets, audit, log, configuration, virus, worm, malicious code, Trojan,
List all Keywords     block, change management, time synchronization, backup, vulnerabilities,
                      penetration
                                   C
                                   COOM
                                      MPPO
                                         ONNEEN
                                              NTT C
                                                  CLLA
                                                     ASSSSIIFFIIC
                                                                CAATTIIO
                                                                       ONN
Provide the
                        Emerging              Current             Twilight      Sunset
Classification
                              Rationale for Component Classification
Document the
Rationale for
Component
Classification
                                      Conditional Use Restrictions
Document the
Conditional Use
Restrictions

                                              Migration Strategy
Document the
Migration Strategy
                                           Impact Position Statement
Document the Position
Statement on Impact
                                             C
                                             CUURRRREEN
                                                      NTT SSTTA
                                                              ATTU
                                                                 USS
Provide the Current
                          In Development        Under Review           Approved     Rejected
Status)
                                                A
                                                AUUD
                                                   DIITT TTRRA
                                                             AIILL
Creation Date           03/11/2004                 Date Accepted / Rejected   06/08/2004
    Reason for
Rejection
Last Date Reviewed                                 Last Date Updated
    Reason for
Update

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
