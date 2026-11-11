---
schema_version: 1
corpus: states-government-it
jurisdiction: new-york
id: ny-its-p20-004
title: Technology Projects in Response to Critical Incidents and Governor's Initiatives
doc_type: policy
citation: NYS ITS Policy ITS-P20-004
authority_level: ''
issuing_body: New York State Office of Information Technology Services (ITS)
source_url: https://its.ny.gov/technology-projects
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 967fdc40b85758c882c3d01fb6ecc859a7961e25f5a2ba0cc94bf83cc5822cba
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: 'Pages 1 of the PDF have no text layer (they are scans) and their text was recovered
  by OCR; the other pages'' text is the text layer, extracted with pdftotext -layout (trailing spaces
  and form feeds removed, ligature glyphs written as their letters). Two independent engines (tesseract
  (ocrmypdf) + paddleocr PP-OCRv6) agree on 96% of the word sequence and 97% of the 33 figures of the
  scanned pages, 100% dictionary-recognizable. 7 position(s) where the two engines read a different word
  or figure are listed in the scan''s ocr.json report (disagreements): the committed reading is tesseract''s
  and is contested there. Figures read differently: tesseract read P 20 Technology Services Policy 0 where
  paddle read nothing (after "Office of Information No"). Reading order of labelled or two-column layouts,
  bullet glyphs (read as ''e'' or ''o''), letterhead logos, handwriting and signatures are not reliably
  read or placed; the glyphs read from a signature field are not committed. effective_date and source_version
  are left empty: a date read from a scan is not transcribed from the source. NOT human-verified — treat
  every number as unchecked against the source'
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
- oversight
text_source: ocr
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

> **MACHINE READING OF A SCAN.** Pages 1 of the source PDF are images with no text layer; their text below was read from the image by OCR (two engines, see the curator notes) and is not the document's own text. Expect character-level errors in words and figures, and treat every number as unchecked against the source. `source_sha256` hashes this transcription; the scan is the snapshot.

# Technology Projects in Response to Critical Incidents and Governor's Initiatives (NYS ITS Policy ITS-P20-004)

## At a glance

Item of the ITS statewide technology policy and standards library (https://its.ny.gov/policies), category 'Technology Development/Use, ITS Policies' on the listing. The listing prints original publication 12/11/2020.

## Full text

NEW YORK | Office of Information

STATE OF

OPPORTUNITY. Technology Services

State Capitol P.O. Box 2062
Albany, NY 12220-0062
www.its.ny.gov

Office of Information

. . No: -P20-{
Technology Services Policy 0: ITS-P20-004

ITS Policy: Issued: 12/11/2020

H i Issued By: NYS Office of Information
Technology Projects In Technology Services
Response to Critical
Incidents and
Governor’s Initiatives

Owner: Chief Portfolio Office

1.0 Purpose and Benefits

During Critical Incidents, the Office of Information Technology Services (ITS) is often
faced with many requests from the Executive Chamber or ITS supported agencies
(client agency) for work items to support emergency, crises, and disaster response. The
typical Information Technology (IT) Governance processes utilizing the IT Investment
Request Form, Agency Governance Boards, and Portfolio Executive Board for decision-
making may not be well suited to support all response efforts during a Critical Incident
or Governor's initiative related thereto. For these situations, ITS has created an
expedited project and initiatives submission and approval process. This policy outlines
the expedited project and initiative submission and approval process to serve as a
repeatable process during Critical Incidents or Governor's initiatives related thereto.

2.0 Authority

Section 103(10) of the State Technology Law provides ITS with the authority to establish
statewide technology policies, including technology and security standards. Section 2
of Executive Order No. 1171, established January 2002, provides the State Chief
Information Officer (CIO) with the authority to oversee, direct, and coordinate the
establishment of information technology policies, protocols, and standards for State
government, including hardware, software, security, and business re-engineering.

1 All references to Executive Order 117 refer to that which was originally issued by Governor George E. Pataki on
January 28, 2002 and continued by Executive Order 5 issued by Governor Eliot Spitzer on January 1, 2007,
Executive Order 9 issued by Governor David A. Patterson on June 18, 2008, and Executive Order 2 issued by
Governor Andrew M. Cuomo on January 1, 2011, and Executive Order 6 issued by Governor Kathy Hochul on
October 8, 2021.

   Details regarding this authority can be found in NYS ITS Policy, NYS-P08-002 Authority
   to Establish Enterprise Information Technology Policies, Standards and Guidelines.

3.0 Scope
   This policy document applies to ITS and its employees (including full-time, part-time,
   and temporary employees), contractors, consultants, volunteers, interns, and ITS
   supported agencies (“Client Agency”).

4.0 Information Statement
   The New York State Office of Emergency Management is responsible for coordinating
   the activities of all State agencies to protect New York's communities, economic well-
   being, and environment from natural and human caused disasters and emergencies.
   The State’s Emergency Operations Center has four levels of activation; this Policy
   applies when the level of activation is at either Level 1 (Full State/Federal Response) or
   Level 2 (Full Activation). This policy also applies when the request supports a
   Governor’s initiative related to a Critical Incident. All ITS executives will meet within
   one hour of receiving a project or initiative request to discuss and determine which
   teams need to take action.
   4.1       Equipment and Network Services Requests
   During a Critical Incident, all requests related to equipment and network services will be
   entered into NY Responds – the incident management tool utilized by the State to triage
   and prioritize requests. ITS will continue to use the Information Technology Service
   Management System (ITSM) for related asset tracking, and for ITS to manage service
   requests.
   4.2       New Application or Application Enhancement Requests
   Requests for new applications, new services, or application enhancements during a
   Critical Incident, or as a result of a Governor’s initiative related thereto at an initial stage
   will include:
         •   A clear business owner or sponsor for the effort.
         •   A defined business need associated with an objective that supports Critical
             Incident response.
         •   An understanding that costs may be incurred for the development, as well as
             ongoing operational/maintenance requirements; and, the business sponsor is
             accepting responsibility for financial obligations, including, but not limited to
             ascertaining whether State Finance Law Section 163 applies.
   The recipient of a request will route it to applicable Portfolio Executive Directors for
   review, coordination, and approval.

   ITS-P20-004                                                                          Page 2 of 4

   If a Portfolio Executive Director can execute a request utilizing existing tools,
   technologies, licenses, and resources, then they can approve or disapprove the request
   following consultation with the Chief Technology Officer, Chief Information Security
   Officer, and Chief Financial Officer. Requests for such applications and enhancements
   must use technologies that are currently supported by ITS. Application architecture for
   such applications must be explicitly approved by the Chief Technology Officer or a
   designee.
   If a Portfolio Executive Director cannot execute a request within their own team, then
   the request will be escalated to the State CIO and Executive Deputy CIO for review. In
   these cases, meetings may be required to discuss across ITS Divisions. Escalated
   request decisions will be communicated across the ITS Leadership Team utilizing the
   its.dl.executive.team distribution list.
      4.2.1 Tracking New Applications or Application Enhancements
      New applications, new services, or application enhancements included in a Critical
      Incident response or Governor’s initiative related thereto, will be tracked utilizing
      ITSM.
          •      Efforts costing less than $50,000 or 500 hours will be tracked in ITSM as
                 tasks and milestones under a project named for the Critical Incident or
                 Governor’s initiative related thereto.
          •      Efforts costing $50,000 or more, or more than 500 hours, will be tracked as
                 their own project within the ITSM Project Portfolio under a program
                 associated with the Critical Incident or Governor’s initiative related thereto.
      All new applications and services will be added to the ITSM Application Portfolio.

5.0 Compliance
   This Policy shall take effect upon publication. Compliance is required with all ITS
   policies and standards. ITS may amend its policies and standards at any time;
   compliance with amended policies and standards is required.

6.0 Definitions of Key Terms
   Except for terms defined in this policy, all terms shall have the meanings found in
   http://www.its.ny.gov/glossary.

7.0 Contact Information
      Submit all inquiries and requests for future enhancements to the policy owner at:
                                    Chief Portfolio Office
                                   Reference: ITS-P20-004
                        NYS Office of Information Technology Services

   ITS-P20-004                                                                        Page 3 of 4

                          Swan Street Building, Core 4, Floor 2
                           Email: its.sm.CPO-GPS@its.ny.gov

        Statewide technology policies, standards, and guidelines may be found at the
                        following website: https://its.ny.gov/policies

8.0 Revision History
   This policy should be reviewed consistent with the requirements set forth in NYS-P09-
   003 Process for Establishing Information Technology Polices, Standards and
   Guidelines.

    Date             Description of Change                           Reviewer
    12/11/2020       Issued policy                                   Chief Portfolio
                                                                     Office

9.0 Related Documents
   NYS-S13-001 Secure System Development Life Cycle

   ITS-P20-004                                                                 Page 4 of 4

## Curator notes

Pages 1 of the PDF have no text layer (they are scans) and their text was recovered by OCR; the other pages' text is the text layer, extracted with pdftotext -layout (trailing spaces and form feeds removed, ligature glyphs written as their letters). Two independent engines (tesseract (ocrmypdf) + paddleocr PP-OCRv6) agree on 96% of the word sequence and 97% of the 33 figures of the scanned pages, 100% dictionary-recognizable. 7 position(s) where the two engines read a different word or figure are listed in the scan's ocr.json report (disagreements): the committed reading is tesseract's and is contested there. Figures read differently: tesseract read P 20 Technology Services Policy 0 where paddle read nothing (after "Office of Information No"). Reading order of labelled or two-column layouts, bullet glyphs (read as 'e' or 'o'), letterhead logos, handwriting and signatures are not reliably read or placed; the glyphs read from a signature field are not committed. effective_date and source_version are left empty: a date read from a scan is not transcribed from the source. NOT human-verified — treat every number as unchecked against the source
