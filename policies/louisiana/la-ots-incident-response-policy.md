---
schema_version: 1
corpus: states-government-it
jurisdiction: louisiana
id: la-ots-incident-response-policy
title: Incident Response Policy and Procedure
doc_type: policy
citation: OTS Incident Response Policy and Procedure, Revision 2.01
authority_level: ''
issuing_body: Office of Technology Services, Division of Administration
source_url: https://www.doa.la.gov/media/f1hooo3l/incident_response_policy_and_procedure_redacted.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 2aef73a38f9ee79c4085c49aa34e2ce3e69f5ef80f405499c95b5dba653b49c8
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: 'Pages 6, 7, 18, 19, 20, 21 of the PDF have no text layer (they are scans) and their
  text was recovered by OCR; the other pages'' text is the text layer, extracted with pdftotext -layout
  (trailing spaces and form feeds removed, ligature glyphs written as their letters). Two independent
  engines (tesseract (ocrmypdf) + paddleocr PP-OCRv6) agree on 93% of the word sequence and 94% of the
  100 figures of the scanned pages, 92% dictionary-recognizable. 47 position(s) where the two engines
  read a different word or figure are listed in the scan''s ocr.json report (disagreements): the committed
  reading is tesseract''s and is contested there. Figures read differently: tesseract read S oTS wage
  sot where paddle read LOTS Page 6 of 21 (after "981 C 082998 FF"); tesseract read ot 2 where paddle
  read of 21 (after "S OTS oage 7"); tesseract read auie reyg where paddle read Emergency 1 (after "Severity
  Description Phase Class"); tesseract read land where paddle read 2 business hours and (after "level
  to the Incident"); tesseract read nothing where paddle read Containment Medium 8 business hours (after
  "of mitigating controls to"); tesseract read Service Level Objective 2 business hours Emergency 8 business
  hours where paddle read Low (after "any possibility of Propagation"); tesseract read Emergency lbusiness
  where paddle read High 1 business (after "is the successful restoration"); tesseract read 7 orrective
  where paddle read Corrective (after "after implementing long term"); tesseract read S OTS where paddle
  read LOTS Page 18 of 21 (after "981 C 082998 FF"); tesseract read Page 18 of 21 where paddle read nothing
  (after "Response Policy and Procedure"); tesseract read Chase Hymel 23 where paddle read nothing (after
  "by 6 23 2025"); tesseract read 073408 where paddle read 9734 DF (after "675 CD 5 A"). Reading order
  of labelled or two-column layouts, bullet glyphs (read as ''e'' or ''o''), letterhead logos, handwriting
  and signatures are not reliably read or placed; the glyphs read from a signature field are not committed.
  effective_date and source_version are left empty: a date read from a scan is not transcribed from the
  source. NOT human-verified — treat every number as unchecked against the source'
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

> **MACHINE READING OF A SCAN.** Pages 6, 7, 18, 19, 20, 21 of the source PDF are images with no text layer; their text below was read from the image by OCR (two engines, see the curator notes) and is not the document's own text. Expect character-level errors in words and figures, and treat every number as unchecked against the source. `source_sha256` hashes this transcription; the scan is the snapshot.

# Incident Response Policy and Procedure (OTS Incident Response Policy and Procedure, Revision 2.01)

## At a glance

Revision 2.01, June 23, 2025: the State's incident response plan run by the Information Security team (identification, classification and the phases that follow). The file is the redacted public version, as its address says.

## Full text

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                      Incident Response Policy and Procedure

                                           Office of Technology Services
                                        Information Security and Compliance
                                                 State of Louisiana

                                                               Revision: 2.01
                                                             Date: June 23, 2025

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                                                                                Page 2 of 21
             Incident Response Policy and Procedure                                                                                                        Division of Administration
                                                                                                                                                       Office of Technology Services

             Table of Contents
             Overview ...................................................................................................................................................................... 4
             Purpose ........................................................................................................................................................................ 4
             Scope ........................................................................................................................................................................... 4
             Procedure .................................................................................................................................................................... 4
                Incident Identification and Classification ............................................................................................................ 4
                    Classification ....................................................................................................................................................... 4
                    Classification Criteria ..........................................................................................................................................5
                    Severity .................................................................................................................................................................5
                Incident Response Team ........................................................................................................................................7
                    Service Level Agreement ...................................................................................................................................7
                    Roles......................................................................................................................................................................7
                    Responsibilities ................................................................................................................................................... 8
                    Organizational Chart ......................................................................................................................................... 10
                Communications ..................................................................................................................................................... 11
                    Internal Notifications.......................................................................................................................................... 11
                    External Notifications ........................................................................................................................................ 11
                    Breach Notifications .......................................................................................................................................... 11
                Investigation and Evidence Collection ............................................................................................................... 12
                Containment .......................................................................................................................................................... 13
                    Short-term Containment ................................................................................................................................. 13
                    Long-term Containment .................................................................................................................................. 13
                Root Cause Analysis .............................................................................................................................................. 13
                Eradication ............................................................................................................................................................. 14
                Recovery and Remediation .................................................................................................................................. 14
                Lessons Learned ................................................................................................................................................... 14
                Continuous Evaluation .......................................................................................................................................... 14
                    Training ............................................................................................................................................................... 14
                    Testing ................................................................................................................................................................ 14
             References ................................................................................................................................................................... 15
             Definitions and Terms ................................................................................................................................................. 15
             Owner .......................................................................................................................................................................... 16

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                                                                              Page 3 of 21
             Incident Response Policy and Procedure                                                                                                      Division of Administration
                                                                                                                                                     Office of Technology Services

             Revision History .......................................................................................................................................................... 16
             Appendix ..................................................................................................................................................................... 19

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                     Page 4 of 21
             Incident Response Policy and Procedure                                                    Division of Administration
                                                                                                  Office of Technology Services

             Overview
             The state of Louisiana’s Incident Response Policy and Procedure (IRP) is a critical element to ensure
             effective priorities and management of an Incident is managed and prioritized as required by the state of
             Louisiana’s Information Security Policy (ISP).

             This Incident Response Policy and Procedure clearly outlines required actions in the following;
             identification, response, remediation, and follow-up to the occurrence. The intent of this policy and
             procedure is to outline actions performed by the Information Security Team (IST), and respond to
             security incidents in a timely, efficient manner.

             Purpose
             The purpose of the IRP is to ensure Incidents are fully documented from declaration through recovery
             and remediation.

             Scope
             The scope of the IRP includes Identification and Classification of an Incident; Communication;
             Investigation and Evidence Collection; Containment; Root Cause Analysis; Eradication; and Recovery and
             Remediation. All steps of the IRP must be followed, including documentation of Lessons Learned,
             Continuous Evaluation, and Annual Testing of the policy and procedure.

             Procedure
             Incident Response is the process of reacting to Information Technology (IT) threats to an organization or
             entity such as a cyberattack, server downtime, and/or security breach. The seven phases of the Office of
             Technology Services (OTS) Incident Response Policy and Procedure are detailed below.

             Incident Identification and Classification
             Upon notification and determination that a Security Event is an Incident, the Chief Information Security
             Officer(CISO) and Incident Response Team (IRT) will begin the formal Incident management process
             starting with assigning an appropriate classification level to the Incident.

             Classification
                 •    The CISO or designee within the IST will determine if the Security Event does or does not require
                      a formal Incident Response. If a Security Event does require a formal Incident Response, the
                      CISO must be involved and classify the event.
                 •    Security Events that do not require a formal written Incident Response will be forwarded to
                      appropriate staff members from either OTS, or the Agency to ensure that all support services
                      required are rendered.
                 •    Security Events that do require a formal written Incident Response will have its classification level
                      assigned by the CISO according to the Incident Classification Matrix outlined in this policy and
                      procedure.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                   Page 5 of 21
             Incident Response Policy and Procedure                                                  Division of Administration
                                                                                                 Office of Technology Services

             Classification Criteria
                 •    Classifications are determined by evaluating the likelihood versus potential impact of an Incident.
                 •    The details of Security Incidents, events, or breaches, which must be reviewed thoroughly by the
                      IST before including the CISO, to determine the likelihood of a reoccurrence of the event. The
                      IST should also perform an impact analysis and document the details (criticality of the affected
                      resources and the consequences) of the event.
                 •    The analysis of the likelihood of occurrence and the impact of the affected resources shall result
                      in the assignment of one of four classifications.

             Likelihood - shall be determined based on the following criteria:
                 o Rare - Highly unlikely, but may occur in exceptional circumstances.
                 o Unlikely - Event is not expected, and a slight possibility of occurrence may exist. Identified
                     vulnerability or issue may be legitimate; however, compensating controls are in place and make
                     exploitation impossible or unreasonably difficult.
                 o Possible - The event might occur at some time, as there is a history of casual occurrence of the
                     observed behavior.
                 o Likely - There is a strong possibility and expectation of occurrence, or there is a history of
                     frequent occurrence.
                 o Almost Certain - The event is expected to occur in most circumstances, there is a precedent
                     for regular occurrence, and preventative controls are not adequate or in place.

             Impact - shall be determined by the associated criticality of affected resources and the following criteria
             for determining the current or potential severity of the Incident:
                 o Insignificant - Identified risk impacts systems which are non-critical to business functionality,
                     which do not contain Confidential or Restricted Data, and can be replaced with an alternative
                     solution if made unavailable. Examples include printers, multi-function devices, and scanners.
                 o Minor - Identified risk impacts systems which are non-critical to business functionality, which do
                     not contain Confidential or Restricted Data, but cannot be replaced with an alternative solution if
                     made unavailable. Examples include meeting room devices and kiosk stations.
                 o Moderate - Identified risk impacts systems which are non-critical to business functionality but
                     which contain a moderate amount of Confidential or Restricted Data. Examples include end-user
                     computing devices including laptops, tablets, smartphones, and desktop computers.
                 o Major - Identified risk impacts systems which are non-critical to business functionality but
                     contain a large volume of Confidential or Restricted Data. Major criticality may also be assigned
                     to systems which are critical to business functionality but which do not contain Confidential or
                     Restricted Data. Examples include file servers, development and test resources, and business
                     analytics systems.
                 o Severe - Identified risk impacts systems which are critical to agency functionality and contain
                     Confidential or Restricted Data. Exposure of systems determined to be critical may result in
                     severe consequences including loss of Confidential or Restricted Data. Removing the affected
                     resource from production will have a negative impact to agency functionality. Examples include
                     *.laworks.net, external service applications.

             Severity
             Based on the likelihood of occurrence and the impact to the affected resources, the CISO will assign one
             of four incident severity classifications to an incident.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

S.oTS wage sot

Incident Response Policy and Procedure Division of Administration
Office of Technology Services

Once the Incident Management Team Leader (IMTL) has declared a security incident and its severity
level, the Incident Response Leader will initiate an appropriate response for the given incident.

Impact - shall be determined by the associated criticality of affected resources and the following criteria
for determining the current or potential severity of the Incident:

¢ Low- One instance of potentially unfriendly activity (e.g., port scan, malware detection,
unexpected performance peak, observation of potentially malicious user activity, theft of a
device, etc.)

¢ Medium - One instance of a clear attempt to obtain unauthorized information or access (e.g.,
attempted download of secure password files, attempt to access restricted areas, single
computer infection on a non-critical system, successful unauthorized vulnerability scan, etc.) ora
repeated or persistent Low Incident. Incidents classified as Medium risk may also include the
incidental internal exposure of one employee record. Medium incidents may also include
vulnerabilities with a rare rate of occurrence on critical systems, due to either compensating
controls, network isolation, or other factors.

° High - Serious attempt or actual interruption in availability, or negative impact to confidently or
integrity, or Data Breach. (e.g., multi-pronged attack, denial of service attempt, virus infection of
a critical system or the network, multiple concurrent infections of systems, successful
buffer/stack overflow, successful unauthorized access to systems hosting or transmitting
Confidential or Restricted Data, broken lock, stolen papers, etc.) Or; a repeated or persistent
Medium Incident. Incidents with a high criticality may include systems with low to moderate
criticalities, which are affected by vulnerabilities are most likely to be exploited.

¢ Emergency - Incidents that involve the potential breach of Restricted or Confidential Data.
Incidents classified as Emergency risk require immediate attention including the engagement of
Data Owners and SMEs to perform short-term containment including taking down potentially
compromised systems and applications. Incidents with an emergency criticality are likely to be
assets with high criticality to business functionality, affected by threats, and almost certain to
occur.

Likelihood

Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

S.OTS oage7ot2

Incident Response Policy and Procedure Division of Administration
Office of Technology Services

Incident Response Team
Service Level Agreement
e Incident Management Service Level Agreements (SLAs) shall be based on the severity
classification.
SLAs shall include metrics for acceptance, containment, and resolution phases of the Incident
Management process.
¢ The IRT leader shall remain aware of pending SLA violations by identifying when a metric is within
a specified threshold of violation.

Response _ Severity Description
Phase Class

auie(reyg hour (24x7) [Acceptance is the receipt of an incident
1 business hours by the IST. Acceptance includes
lassigning a criticality level to the Incident
~ land initiating the formal Incident

8 business hours Response Policy and Procedure.

3 hours (24x7) [Containment is the successful

5S hours (24x7) implementation of mitigating controls to
|prevent any possibility of Propagation.

Service Level Objective

2 business hours

Emergency

8 business hours
2 business days
8 business hours Resolution is the successful restoration

Emergency

lbusiness days lof an affected resource to production
Recovery 3 business days luse after implementing long-term
7 ‘orrective actions.
5 business days
Roles

Individuals from applicable operational areas or sections within OTS and Agencies will have
responsibilities assigned as outlined below. This team may be use additional staff as warranted by
the specific circumstance of the incident.

The following table notes the individuals and roles comprising the Incident Response Team (IRT).

Group Roles Primary Secondary

Security Steering | ClO, CISO, and Designees | Evelina Broussard Michael Allison

Group (SSG)

Incident CcISO Chase Hymel Donny Brown

Management Barry Faulk

Team Lead

Incident CISO, Data Center Joe Lee - DCO. Eric Grimmer - DCO

Management Operations (DCO), Michael Andresen - Tammy Stalsby - ADM

(IMT) Applications and Data ADM Tonya Monette - DCO NS
Management (ADM), Catherine Shain - Debbie Griffith - EUC
Network Services (NS), DCO Network Donna Roman - EUC Voice
End User Computing Eric Cloud - EUC Brad Coney - ARM

Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                    Page 8 of 21
             Incident Response Policy and Procedure                                                   Division of Administration
                                                                                                  Office of Technology Services

                                     (EUC), Agency                 Jolene Ardoin –EUC
                                     Relationship Manager          Voice
                                     (ARM)                         Thomas Allsup –
                                                                   ARM
              IMT– Incident          IRM - designated by the       Appointed by the         Appointed by the IMTL
              Response               Incident Response Team        IMTL
              Manager (IRM)          Lead
              IMT – Legal            Subject Matter Expert in      Stephen Kogos            TBD
                                     Legal and Compliance
              IMT – Public           Subject Matter Expert in      TBD                      TBD
              Relations              Public Communications
              IMT – Human            Subject Matter Expert in      Cheryl Shillings         TBD
              Resources              HR
              IRT – Incident         Lead IRT Resource –           Appointed by IRTL        Appointed by IRTL
              Handler                Assigned Permanently
                                     until the Incident is
                                     resolved
              IRT - Investigator     IMT/IRT member                Appointed by IRTL        Appointed by IRTL
              IRT – Infosec          Subject Matter Expert in      Appointed by IMTL        Appointed by IMTL
              Specialist             Information Security
              IRT – Agency           Appointed by OTS for          As applicable            As applicable
              Relationship           Service Management for
              Manager (ARM)          each State Agency
              IRT – Asset Owner      Effected agency owner or      As applicable            As applicable
              / Agency Contact       designee, as identified by
                                     the ARM
              IRT – Specialist/      Subject Matter Expert in      As applicable            As applicable
              SMEs                   OTS Section or Business
                                     Services Areas

             Responsibilities
             The following provides the list of all primary responsibilities of the roles listed above.
                • Security Steering Group (SSG) Members
                     o Take responsibility for overall incident management and response concept.
                     o Approve exceptions/deviations.
                     o Make final decisions.
                     o Review, update, and approve the IRP annually

                 •    Incident Management Team (IMT)
                      o In coordination with SSG and IRT, under the guidance of IMT Lead, the IMT manages the
                          incident.

                 •    IMT Lead (IMTL) [CISO]
                      o Develops and maintains incident management and response capability.
                      o Effectively manages identified Security Events, Risks, and Incidents.
                      o Performs proactive and reactive measures to reduce information risk to an acceptable level.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                 Page 9 of 21
             Incident Response Policy and Procedure                                                Division of Administration
                                                                                               Office of Technology Services

                      o   Effectively communicates IRT needs or hurdles to SSG.
                      o   Manages communications outside of IRT resources.
                      o   Appoints Incident Response Manager and Information Security Specialist(s).

                 •    Incident Response Manger (IRM)
                      o Review the ticket information, incident documentation and any associated events/reports.
                      o Appoints Incident Handler.
                      o Responsible for creation and updating of Incident Report.
                      o Provides direction and manages IRT activities.
                      o Coordinates resources to effectively perform incident response tasks.
                      o Escalates IRT resource needs, SLA violations, and challenges to IMT in a timely manner.
                      o Sets up the communication channels for IRT upon notification of the incident (conference
                          call, meeting, cell phones, emails, etc.)
                      o Coordinates the response and investigation phases.
                      o Responsible for successful execution of Incident Response Policy and Procedure.
                      o Presents incident response report and lessons learned to IMT Leader and SSG members.

                 •    Incident Handler/Incident Response Team (IRT)
                      o Assigned as a dedicated resource until Incident has successfully completed all phases.
                      o Follows Incident Response Policy and Procedure, and Processes as documented.
                      o Logs details of IRT activities and provides timely and reoccurring updates to IRM.
                      o Verifies all phases of Incident Management Response were successfully completed.
                      o Coordinates with IRT members to complete each phase of Incident Response.
                      o Responsible for evidence collection retention and chain of custody.
                      o Assist IRM with post-incident closure activities and the Lessons Learned process.

                 •    Agency Relationship Manager (ARM)
                      o Coordinates with IRM and IMTL for any Agency level communication.
                      o Identifies Agency contacts or Asset owners.
                      o Coordinates any additional Agency resources or Process SMEs as needed by the IRT.

                 •    Asset Owner (Agency Leadership or Delegate)
                      o Make decisions related to assets/systems when an incident happens, based on IMTL/IRT
                         recommendations.
                      o Provide clear overview of potential process impact during IRT activities.

                 •    Technical or Process Specialists/Representatives
                      o Provide support to lMT or lRT when resolving incidents.
                      o Maintain information systems in a good condition per company policy and best practices.
                      o Report any additional information as applicable to incident.
                      o Not authorized to share details of any incident outside of IRT without explicit direction from
                         IMTL.

                 •    Legal/Compliance
                      o Provide legal response to a breach including compliance with notification requirements for
                         the Payment Card Industry Data Security Standard (PCI DSS), consumer and employee
                         privacy, third-parties, and additional as required.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                      Page 10 of 21
             Incident Response Policy and Procedure                                                      Division of Administration
                                                                                                     Office of Technology Services

                      o   Coordinate with the IMTL and SSG whether general counsel is required for Incidents with
                          legal impacts and ramifications, to include collection of evidence, prosecution of individuals,
                          lawsuits, etc.

                      Note: Legal or Compliance Resources may be internal or external counsel that is specifically
                      designated by the Asset Owner or as applicable for the impacted Agency or Agencies.

                 •    Human Resources
                      o Provide disciplinary or consulting support for instances where an internal employee was the
                        cause of, or impacted by, the Incident.
                      o Integrates HR policy to support Incident Management Program.
                      o Sanctions to employees found in violation of Acceptable Use or involved in an incident.

                 •    Public Relations
                      o In coordination with Legal and SSG, provides all external relations and centralized responses
                         to public entities or additionally identified resources.

             Organizational Chart
             The following provides the list of all primary responsibilities of the roles listed above.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                    Page 11 of 21
             Incident Response Policy and Procedure                                                   Division of Administration
                                                                                                 Office of Technology Services

             Communications
             Timely, accurate, and consistent notification is a critical operational requirement of any Incident
             Managementeffort and as such, any incident or breach notification must follow the processes outlined
             below.

             Internal Notifications
                 •    Incidents involving, or potentially involving, Confidential or Restricted Data must be
                      communicated to all applicable IRT members, including, Legal, Human Resource, and Public
                      Relations contacts, to ensure that appropriate measures are taken to report the incident both
                      internally and externally.
                 •    Incidents specifically involving employee personally identifiable information (PII) elements will
                      ensure appropriate members of Human Resources are involved prior to any internal or external
                      communication is released.
                 •    Progress notifications and applicable updates to IMT and SSG will only be sent from the IRM.
                 •    Any other notification containing incident or investigation details to resources outside of the IRT
                      is strictly prohibited, without prior approval from the IMTL.

             External Notifications
                 •    The IMT will discuss the potential need for external notifications with Legal, Public Relations, and
                      SSG.
                 •    Legal will then determine if there are legal requirements for notifying external parties of the
                      incident, whether actual or suspected.
                 •    Communications sent to any external or public entity (with exception of Partners required for
                      Incident Response activities that have signed a Non-Discloser Agreement) will only initiate from
                      Legal or Public Relations representatives.
                 •    IMT, in conjunction with other applicable organizational or Agency members, will determine the
                      need for any external professional services such as forensic analysis, malware detection, etc.
                 •    Depending upon the actual or potential criminal elements of the Incident, the IMTL, in
                      conjunction with Legal and SSG, will review the need to involve the appropriate State or Federal
                      enforcement Agency.

                      Note: Primary and Secondary Enforcement Contacts are listed within the Contacts table located
                      within the last section of this document.

             Breach Notifications
             The Breach Notification process will depend on the Agency and Restricted Data elements impacted by
             the Incident. Each Agency has specific regulatory, legal, or contractual obligations to initially notify a
             Federal Department or Partner.

                 •    Within the first initial hour of Incident, the IMTL or designee, working with applicable Legal
                      resources, will review the need to notify any external Federal Agency or Agency Partner.
                      o If initial notification to a Federal Agency or Partner is required, the IMTL will notify the SSG.
                      o The SSG will assign an individual within the IMT to establish and maintain communication with
                          the required Federal Agency or Partner during the course of the Incident.
                          Note: Federal Agency and Partner Contacts are listed in the contacts table located within
                          the last section of this document.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                 Page 12 of 21
             Incident Response Policy and Procedure                                                 Division of Administration
                                                                                                Office of Technology Services

                      o    Incidents involving or potentially involving unauthorized disclosure of Federal Tax
                           Information (FTI) requires immediate notification, but no later than 24 hours after
                           identification of a possible issue involving FTI data, to the local Treasury Inspector General
                           for Tax Administration (TIGTA) Field Division Office, to the Special Agent-in-Charge and to
                           the IRS Office of Safeguards.
                 •    If the organization experiences or suspects a breach or loss of PII or a security incident, which
                      includes Social Security Administration (SSA) provided information, they must notify the State
                      officials responsible for Systems Security designated in the agreement. That State official or
                      delegate must then notify the SSA Regional Office Contact or the SSA Systems Security
                      Contact identified in the agreement. If, for any reason, the responsible State official or delegate
                      is unable to notify the SSA Regional Office or the SSA Systems Security Contact within one hour,
                      the responsible State organization official or delegate must report the incident by contacting
                      SSA’s National Network Service Center (NNSC) toll free at 1-877-697-4889 (select “Security
                      and PII Reporting” from the options list). As the final option, in the event SSA contacts and
                      NNSC both cannot be reached, the organization is to contact SSA’s Office of Information
                      Security, Security Operations Center at 1-866-718-6425. OTS IST will provide updates as they
                      become available to SSA contact, as appropriate. The link for the worksheet provided in the
                      Memorandum of Understanding (MOU) agreement to facilitate gathering and organizing
                      information about an incident can be found in the Reference section of this procedure.
                 •    If the organization experiences or suspects a breach or loss of PHI/PII or a security incident,
                      which includes Center for Medicare and Medicaid Services (CMS) provided information, the
                      IMTL or designee must notify the State agency official responsible for Systems Security
                      designated in the agreement. OTS Compliance will notify the designated LDH Legal/Privacy
                      Officer, who is responsible for notifying CMS within one (1) hour.
                 •    If the organization experiences or suspects a breach or loss of Criminal Justice Information
                      Systems (CJIS) data, the IMTL or designee must notify the state CJIS ISO, the state CJIS CSO,
                      and the state CJIS Systems Agency (CSA) the Louisiana State Police. The state CJIS ISO will
                      notify the FBI CJIS ISO within one (1) hour and will remain in communication with the IMT, CSA,
                      CJIS CSO and the FBI CJIS ISO throughout the incident response.
                 •    Any additional required breach notifications will be facilitated by an individual designated by
                      Legal or SSG, working with IMTL or designee.

             Investigation and Evidence Collection
             Should there be an explicit or implied need to collect evidence the following requirements will apply.

             Data Retention

                 •    Retention of audit logs, e-mails, memos, etc. shall be maintained in accordance with State
                      Record Retention Policy.

             Chain of Custody

                 •    An accurately maintained Chain of Custody is required when collecting and retaining the
                      following evidence types.
                      o Device or System images
                      o Drive or Disk captures
                      o Forensic System Exports

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                 Page 13 of 21
             Incident Response Policy and Procedure                                                 Division of Administration
                                                                                                Office of Technology Services

             Required Evidence

                 •    As required by the Incident Management and Response Policy, the following evidence should be
                      collected, based on Incident severity, when available or applicable.
                      o Application, System, or Security Logs
                      o Applicable Reports
                      o Emails (including message headers)
                      o Helpdesk Tickets
                      o Signed Statements of first-hand accounts

             Containment
             The primary goal of the Containment phase is to prevent any increase in impact by additional data or
             system exposure, or allowing any propagation of unauthorized software.

             Additionally, when possible, the Incident should be contained in a manner that will allow assigned IRT
             resources acceptable time to analyze to determine root cause.

             Short-term Containment
             If appropriate, the following actions shall be taken:
                  • Network Isolation via Firewall or Internal Routers
                  • Disabling of Account Credentials
                  • Blocking outbound or inbound traffic via Web Proxy or Intrusion Prevention Systems
                  • End User Education

             Long-term Containment
             When required, in addition to Short-Term Containment options, the following Long-term containment
             options shall be taken:
                 • System, Application, or Database Isolation via termination of physical network cable or virtual
                     network interface.
                 • System, Application, or Database Isolation via host migration to separate Physically isolated
                     Non- Production Network
                 • Code Change in Application
                 • Any additional technical control approved by the IMTL

             Root Cause Analysis
             The IRT shall review all available network, system, database, and application logs to determine the Root
             Cause of the incident.

             The Root Cause analyst shall cover the following:
                • Point of Entry or Compromise
                • Source (to include user, IP, mac address, email address, etc.)
                • Impacted Systems and Application
                • Data Types Accessed, Disclosed, or Modified

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                               Page 14 of 21
             Incident Response Policy and Procedure                                               Division of Administration
                                                                                              Office of Technology Services

             Eradication
             Depending on the details, cause, and scope of the Incident, eradication may be required. The
             requirements are applicable under the following conditions.
                 • Unauthorized Software or Configuration has been added to or modified on any system or device.
                 • Confidential or Restricted Data has been moved or replicated to an unauthorized storage
                     location.
                 • If required, an eradication strategy or approach should be used that will also the system to be
                     validated or measure to confirm eradication was successful.

             Recovery and Remediation
             The goal of the Recovery and Remediation phase is to both restore any impacted technical or operational
             service and ensure the environmental changes necessary have been successfully implemented to prevent
             a repeat incident.

             As applicable, based on Root Cause analysis, the following Recovery and Remediation options shall be
             used:
                 • Fresh Install and Patched Operating System
                 • Fresh install and Patched Application
                 • Modification of impacted control to prevent future incident
                 • Updated Impacted Application to mitigate identified vulnerability
                 • Implementation of new Information Security control or technology to prevent Incident

             Lessons Learned
             Once the Recovery and Remediation phase is complete, the IMTL will schedule a meeting with all IMT
             and IRT members to discuss the details associated with the Incident.

             Minimally, the following areas or topics shall be discussed:
                 • Was this Incident due to a control failure? If so, how has it been improved to prevent future
                     incidents?
                 • Does the remediation method or newly improved or implemented control impact other
                     operational areas? Does it need to impact other areas to address similar risk?
                 • How could operational processes be improved to identify similar vulnerabilities prior to an
                     incident?

             Continuous Evaluation
             Training
                 •    All State employees, contractors, consultants, temporary employees, and other staff members,
                      receive security awareness training upon hire and annually thereafter, that includes their
                      responsibilities in notifying the CISO, or designee when they become aware or observe a Security
                      Event.
                 •    Applicable IRT members, and others as warranted, are required to attend incident response
                      training on a regular basis as well as the Incident Response Procedures on an annual basis.

             Testing
                 •    The Incident Response Policy and Procedure must be organized by the CISO to be tested at

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                  Page 15 of 21
             Incident Response Policy and Procedure                                                  Division of Administration
                                                                                                 Office of Technology Services

                      least every 12 months basis without prior notification to the remainder of the IMT. Upon the
                      reasonable discretion of the CISO, prior notification may be made to the Public Relations
                      contacts so that external parties are not mistakenly notified because of testing.
                 •    Following the test, the IMTL must compile a report to be distributed to the IMT & IRT with
                      comments that may include:
                      o Was the incident responded to following the policy and procedure?
                      o Were the appropriate personnel notified internally?
                      o Were the necessary technology resources available as needed?
                      o Was the incident contained with the least amount of impact on other systems?
                      o Are there any improvements to be made to the process?

             References
             NIST Computer Security Incident Handling Guide
             OTS Information Security Policy (ISP)

             Definitions and Terms
             The terms and definitions below are listed for the purpose of this document.

                 •    Agency – organizational units within the Louisiana Department of Administration established to
                      provide services to the citizens of Louisiana.
                 •    ARM – Agency Relationship Manager – OTS liaison who works with the customer agency.
                 •    Chain of Custody – Agency Relationship Manager – OTS liaison who works with the customer
                      agency.
                 •    CISO - Chief Information Security Officer
                 •    Confidential or Restricted Data – Confidential Data is data that the unauthorized disclosure
                      of could seriously and adversely impact an Agency, third party, suppliers, individuals, or the State
                      of Louisiana. Additionally, Confidential Data has been specifically excluded or granted exemption
                      within the State’s Public Records Law. Restricted Data is data that requires strict adherence to
                      legal obligations such as Federal, State, or local law, specific contractual agreements, or data
                      specifically designated as Restricted Data in applicable state or Agency policy. The unauthorized
                      disclosure of Restricted Data is expected to have a severe or catastrophic adverse effect on an
                      Agency, partners, individuals, or the State of Louisiana. Additionally, Restricted Data has been
                      specifically excluded or granted exemption within the State’s Public Records Law.
                 •    Containment – the third step in the seven-phase Incident Management program. A strategy
                      used to limit the impact of a cyber-attack.
                 •    Data Retention – Policies of persistent data and records management for meeting legal and
                      business data archival requirements. Eradication – the fourth step in the seven-phase Incident
                      Management program. This step presents a more permanent fix towards eliminating access
                      points for cyberattack agents.
                 •    Eradication – the fourth step in the seven-phase Incident Management program. This step
                      presents a more permanent fix towards eliminating access points for cyber-attack agents.
                 •    FTI – Federal Tax Information. Any return or return information received from the IRS or an IRS
                      secondary source, including but not limited to; Federal Office of Child Support Enforcement,
                      Bureau of Fiscal Services, or the Center of Medicare and Medicaid Services.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                    Page 16 of 21
             Incident Response Policy and Procedure                                                    Division of Administration
                                                                                                   Office of Technology Services

                 •    IMT – Incident Management Team - In coordination with SSG and IRT, under the guidance of
                      IMT Lead, the IMT manages the incident.
                 •    Incident Handler – assigned, dedicated resource until Incident has successfully completed all
                      phases.
                 •    IRT – Incident Response Team begins the formal Incident management process starting with
                      assigning an appropriate classification level to the Incident. Team of individuals from applicable
                      operational areas or sections within OTS and Agencies that will have responsibilities as assigned.
                      Depending upon the specific incident, this team may use additional staff as warranted.
                 •    NNSC – National Network Service Center - incidents involving Social Security data must be
                      reported to the SSA’s National Network Service Center.
                 •    Remediation – the act of improving or correcting something that is wrong, especially something
                      to change or stop damage to the environment.
                 •    Risk - the likelihood of a threat successfully leveraging an identified vulnerability and the level of
                      negative impact on any asset, system, data, or operational process.
                 •    Root Cause Analysis – the process of discovering the core issue or highest-level cause of
                      problems.
                 •    SLA - Service Level Agreement, a legally binding contract or agreement related to the provision
                      of goods or services that sets forth the terms, expected duties (typically including processing or
                      response time), and responsibilities of the parties.
                 •    SSA – Social Security Administration.
                 •    SSG – Security Steering Group that takes responsibility for the overall incident management and
                      response concept
                 •    Threat - any source of danger that can cause negative impact to an asset, data, and/or business
                      operations (e.g., act of nature, system vulnerability, manmade disasters, hacker, Employee, etc.).
                 •    TIGTA – Treasury Inspector General for Tax Administration – any incidents involving FTI must be
                      reported to TIGTA.

             Owner
             Division of Administration, Office of Technology Services, Information Security

             Contact Information:
             OTS Information Security Team - InfoSecTeam@la.gov
             OTS Information Security Compliance Team – InfoComp@la.gov
             OTS User Support - OTSSupport@la.gov

             Effective Date: 12/04/2015

             Revision History
              Version           Date                Description                                         Author
              1.00              09/17/2014          Initial draft for Information Security              Dustin Glover
                                                    Workgroup.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

                                                                                                                   Page 17 of 21
             Incident Response Policy and Procedure                                                   Division of Administration
                                                                                                  Office of Technology Services

              1.01              06/30/2015          Update format in preparation for adding as         Dustin Glover
                                                    Appendix item within the Information Security
                                                    Policy.

              1.02              07/29/2015          Review document and update with initial            Dustin Glover
                                                    contacts and title updates.

              1.03              12/04/2015          Remove “draft” reference.                          Dustin Glover

              1.04              11/28/2021          Review document, update grammar, and add           Paula Sobolewski
                                                    dates.

              1.05              08/30/2023          Updated SSA entry.                                 Donny Brown

              1.06              09/01/2023          Reformatted document with internal standard        Carla Simoneaud
                                                    procedure layout.

              1.06              12/06/2023          Added internal and external contact tables.        Marnie Cook
                                                    Updated page numbers in table of contents.

              1.06              12/12/2023          Reviewed and finalized document.                   Carla Simoneaud

              1.07              12/28/2023          Updated roles, formatted response phase            Marnie Cook
                                                    chart, added phase numbering, edited to
                                                    match PDF.

              1.07              01/03/2024          Updated TOC, Purpose, Scope, Roles (Primary        Susan Eversull
                                                    and Secondary Contacts) and Definitions.

              1.07              01/04/2024          Updated other areas based upon                     Susan Eversull
                                                    requirements. Corrections to spelling and
                                                    punctuation.

              1.07              01/22/2024          Updated contacts, reviewed for cleanup.            Susan Eversull

              1.07              02/08/2024          Updated CMS Section and CJIS Section;              Susan Eversull
                                                    updated contact chart with FBI CJIS.

              1.07              02/16/2024          Finalized Document.                                Susan Eversull

              1.07              02/19/2024          Reformatted using new OTS Brand Guide.             Marnie Cook

              1.07              02/19/2024          Updated Contact List, need chart on page 11        Susan Eversull
                                                    updated, so that all text shows.

             Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

S.OTS

Incident Response Policy and Procedure

Page 18 of 21
Division of Administration

Office of Technology Services

1.07 03/11/2024 Updated text and removed highlights. Susan Eversull
1.07 04/03/2024 Change from Plan to Policy and Procedure Donny Brown
2.00 04/17/2024 Updated to 2.0, corrected table of contacts, Susan Eversull
finalized document for signature
2.00 07/17/2024 Reviewed and finalized document. Chase Hymel
2.01 06/23/2025 Updated TSA and CIO information Chase Hymel
Authorization:
Signed by
Ealing Broussard 6/23/2025
Evelina Broussard, State Chief Information Officer Date
DocuSigned by:
6/23/2025
Chase Hymel, /23/
FC675CD5A073408.
Chase Hymel, Chief Information Security Officer Date

Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

Appendix

Contacts (External)

Agency
Law Enforcement

FBI - Cyber Intrusion (P)
FBI - Cyber Intrusion (S)
FBI-CJIS

LA-SAFE (Fusion Center)

LA State Police

LA Office of Inspector
General

IRS (P)
IRS (S)

TIGTA (P)
TIGTA (S)

TIGTA (S)

SSA (P)
SSA (S)

SSA (T)
TSA (P)

Contact should be coordinated via OTS-ARM assigned to DPS or coordinated via LA-SAFE for

incidents requiring escalation or involvement of Louisiana State Police.

Contact should be coordinated via the SSG for incidents requiring escalation to or involvement of Louisiana's

Office of Inspector General.

Federal Agencies

Office of Safeguards

Note: (P) - Primary, (S) - Secondary, (T) — Tertiary

I |

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

Contacts (OTS Internal)
Evelina Broussard
Michael Allison
Chase Hymel
Jeremy Deal
Thomas Allsup
Eric Cloud

Joe Lee

Michael Andresen

Catherine Shain

Data Classification Level: Confidential

Docusign Envelope ID: 54186D0F-4140-4F95-8326-981C082998FF

Jolene Ardoin Pe

Data Classification Level: Confidential

## Curator notes

Pages 6, 7, 18, 19, 20, 21 of the PDF have no text layer (they are scans) and their text was recovered by OCR; the other pages' text is the text layer, extracted with pdftotext -layout (trailing spaces and form feeds removed, ligature glyphs written as their letters). Two independent engines (tesseract (ocrmypdf) + paddleocr PP-OCRv6) agree on 93% of the word sequence and 94% of the 100 figures of the scanned pages, 92% dictionary-recognizable. 47 position(s) where the two engines read a different word or figure are listed in the scan's ocr.json report (disagreements): the committed reading is tesseract's and is contested there. Figures read differently: tesseract read S oTS wage sot where paddle read LOTS Page 6 of 21 (after "981 C 082998 FF"); tesseract read ot 2 where paddle read of 21 (after "S OTS oage 7"); tesseract read auie reyg where paddle read Emergency 1 (after "Severity Description Phase Class"); tesseract read land where paddle read 2 business hours and (after "level to the Incident"); tesseract read nothing where paddle read Containment Medium 8 business hours (after "of mitigating controls to"); tesseract read Service Level Objective 2 business hours Emergency 8 business hours where paddle read Low (after "any possibility of Propagation"); tesseract read Emergency lbusiness where paddle read High 1 business (after "is the successful restoration"); tesseract read 7 orrective where paddle read Corrective (after "after implementing long term"); tesseract read S OTS where paddle read LOTS Page 18 of 21 (after "981 C 082998 FF"); tesseract read Page 18 of 21 where paddle read nothing (after "Response Policy and Procedure"); tesseract read Chase Hymel 23 where paddle read nothing (after "by 6 23 2025"); tesseract read 073408 where paddle read 9734 DF (after "675 CD 5 A"). Reading order of labelled or two-column layouts, bullet glyphs (read as 'e' or 'o'), letterhead logos, handwriting and signatures are not reliably read or placed; the glyphs read from a signature field are not committed. effective_date and source_version are left empty: a date read from a scan is not transcribed from the source. NOT human-verified — treat every number as unchecked against the source
