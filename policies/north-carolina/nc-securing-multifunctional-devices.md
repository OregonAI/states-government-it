---
schema_version: 1
corpus: states-government-it
jurisdiction: north-carolina
id: nc-securing-multifunctional-devices
title: Securing Multifunctional Devices (MFDs) and Network Printers
doc_type: policy
citation: 'NCDIT: Securing Multifunctional Devices (MFDs) and Network Printers'
authority_level: ''
issuing_body: North Carolina Department of Information Technology
source_url: https://it.nc.gov/documents/files/securing-multifunctional-devices-mfds/download?attachment
source_format: pdf
retrieved: '2026-11-11'
source_sha256: da66da6b453d5d071b6009a19a02d18fe2a3feed83f7f9e50606dd0388bc8ffc
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: 'no text layer in the source PDF; text recovered by OCR. Two independent engines (tesseract
  (ocrmypdf) + paddleocr PP-OCRv6) agree on 99% of the word sequence and 100% of the 28 figures, 98% dictionary-recognizable.
  25 position(s) where the two engines read a different word or figure are listed in the scan''s ocr.json
  report (disagreements): the committed reading is tesseract''s and is contested there. The engines read
  every figure alike. Reading order of labelled or two-column layouts, bullet glyphs (read as ''e'' or
  ''o''), letterhead logos, handwriting and signatures are not reliably read or placed; the glyphs read
  from a signature field are not committed. effective_date and source_version are left empty: a date read
  from a scan is not transcribed from the source. NOT human-verified — treat every number as unchecked
  against the source'
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
text_source: ocr
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

> **MACHINE READING OF A SCAN.** The source PDF has no text layer: it is an image. The full text below was read from the image by OCR (two engines, see the curator notes) and is not the document's own text. Expect character-level errors in words and figures, and treat every number as unchecked against the source. `source_sha256` hashes this transcription; the scan is the snapshot.

# Securing Multifunctional Devices (MFDs) and Network Printers (NCDIT: Securing Multifunctional Devices (MFDs) and Network Printers)

## At a glance

The February 2015 memorandum on securing multifunctional devices and network printers. An image-only scan, read by OCR.

## Full text

State of North Carolina
Office of Information Technology Services

Pat McCrory Chris Estes

Governor State Chief Information Officer
Memorandum

To: State Security Liaisons

From: Maria S. Thompson

State Chief Information Risk Officer

Subject: Securing Multifunctional Devices (MFDs) and Network Printers

Date: February 11, 2015

The purpose of this memo is to provide guidance to the implementation, configuration and use of
multifunctional devices (MFDs) and network printers on the State and agency networks. MFD’s are
defined as those devices which offer multiple functionalities such as the following: printer, copier,
scanner, fax, and email. MFDs and network printers provide a needed function thoughout the State,
however, they can have significant vulnerabilities if not properly configured. Many devices used today
have embedded operating systems. While these may provide additional capabilities, there are also added
risks that could lead to the loss of confidentiality, integrity and availability to State data and resources.
The following is a list of recommended techniques that can reduce the risk of using these devices on the
State and agency networks and strengthen the overall information security posture. These techniques
are intended to be vendor neutral, however, many of these steps may not be applicable for specific
brands and model devices.

Configuration Security

e Replace older less secure devices with devices that support secure configuration features.
e Uninstall all unnecessary applications that are not required for business use
e Update the device firmware to the highest level available using vendor signed firmware updates.

e Disable the remote firmware update ability until it is needed. Once the firmware is updated with this
process, promptly disable the remote firmware update ability.

e Password protect the firmware update process/utility.
e Use the most currently available client and admin device management software.
P.O. Box 17209, Raleigh, NC 27619-7209
4101 Mail Service Center, Raleigh NC 27699-4101

Telephone: 919-754-6100
‘An Equal Opportunity/Affirmative Action Employer

e Change all default passwords or community strings, to strong passwords that comply with statewide
standards.

e Disable SNMP v1 & v2 and use only SNMP version 3 for printer management if supportable.
e Change the default SNMP parameters and use strong passphrases.

e Disable unneeded network protocols, printer services, and features on the device, example FTP,
Telnet, SMTP etc.

e FTP and Telnet should ONLY be enabled for firmware updates, if needed, and promptly disabled
when finished. Note: Unless there is a specific business need, most MFDs and network printers
should NOT communicate with the internet.

e Use an Access Control List (ACL) in the device configuration that restricts which subnet, IP address
range or specific hosts can use the device.

e Encrypt network traffic to/from the device and use HTTPS, using SSL/TLS for web based device
maintenance.

e Configure device authentication (account name and password) for end user functions, where
possible.

e Enable the device firewall and configure it to restrict traffic to only those hosts and services that
need access to the device.

e Enable auditing and logging on the device and ensure logs are reviewed on a regular basis.
e Generate reports from the device that show users’ printing behavior.
e Where possible, configure the device to erase data remanence after each print, scan, copy or fax job.

e Power down the device when it is not needed.

Network Security

e Install devices on an isolated network segment with no internet access.

e Assign a static Internet Protocol (IP) address and disable DHCP on the print device.

Physical Security

¢ Prevent unauthorized physical access to the device. This requirement is especially critical to those
devices used to process sensitive information

e Ifthe device has removal hard drives, restrict access to the keys and/or ability to remove the hard
drives

In addition to configuring these devices using the guidelines above, it is recommended that agency
information security officers/liaisons ensure a scan of the network be done to identify any MFDs on the
network that are vulnerable and/or configured insecurely, and take remediation actions. Note:
Depending on the type of data in use, there may be additional restrictions levied due to regulatory
requirements, e.g. IRS 1075. More information about securing MFDs and network printers may be
found at the following resources.

Resources

HP Jetdirect Security Guidelines
http://h20628.www2.hp.com/km-ext/kmesdirect/emr_na-c00746792-3.pdf

NCCIC Bulletin “Multifunction Printer Vulnerabilities
https://msisac.cisecurity.org/resources/reports/documents/A-0012-NCCIC-
130020120223MFPVulnerability.pdf

Internal Revenue Services - Publication 1075, Tax Information Security Guidelines For
Federal, State and Local Agencies - http://www. irs.gov/pub/irs-pdf/p1075.pdf

NIST National Checklist Program - http://checklists.nist.gov/nep.cfm?scap.cfm

NIST Security Configuration Checklists Program for IT Products — Guidance for
Checklists Users and Developers (SP 800-70) - http://nvd.nist.gov/docs/SP_800-
70_20050526.pdf

Please contact me if you have any questions about the guidelines mentioned in this memo:

. Thank you.

## Curator notes

no text layer in the source PDF; text recovered by OCR. Two independent engines (tesseract (ocrmypdf) + paddleocr PP-OCRv6) agree on 99% of the word sequence and 100% of the 28 figures, 98% dictionary-recognizable. 25 position(s) where the two engines read a different word or figure are listed in the scan's ocr.json report (disagreements): the committed reading is tesseract's and is contested there. The engines read every figure alike. Reading order of labelled or two-column layouts, bullet glyphs (read as 'e' or 'o'), letterhead logos, handwriting and signatures are not reliably read or placed; the glyphs read from a signature field are not committed. effective_date and source_version are left empty: a date read from a scan is not transcribed from the source. NOT human-verified — treat every number as unchecked against the source
