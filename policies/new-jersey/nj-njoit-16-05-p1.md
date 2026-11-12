---
schema_version: 1
corpus: states-government-it
jurisdiction: new-jersey
id: nj-njoit-16-05-p1
title: System Architecture Review (SAR) Procedure
doc_type: policy
citation: NJOIT Technology Circular 16-05-P1-NJOIT
authority_level: ''
issuing_body: New Jersey Office of Information Technology
source_url: https://www.nj.gov/it/docs/ps/16-05-P1-NJOIT_System_Architecture_Review_Procedure.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 9532eca43e074090faf58a323154b41025d27ba8d9ca70efd45ad203af4794fd
effective_date: '2016-12-12'
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
- oversight
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# System Architecture Review (SAR) Procedure (NJOIT Technology Circular 16-05-P1-NJOIT)

## At a glance

The SAR process: what it informs agencies of (cybersecurity and privacy, interoperability, data reuse, economies of scale, infrastructure impact, resource prioritisation, disaster recovery) and how a review proceeds.

## Full text

                   State of New Jersey
                   Technology Circular

 System Architecture Review (SAR) Procedure                             16-05-P1-NJOIT

 Approved By: Kevin Dehmer, Chief Technology Officer

 Version: 3.0                                      Supersedes: NA
 Effective Date: 12/12/2016                        Revision Date: 7/14/2026

1.       OBJECTIVE
The New Jersey Office of Information Technology (NJOIT), under the direction of the
Chief Technology Officer (CTO), perform a System Architecture Review (SAR) to ensure
that technology solutions for the Executive Branch of State are designed, developed,
and deployed to maximize benefits and functionality while minimizing costs and risks.
The SAR process also ensures compliance with cybersecurity and architecture standards
and best practices. It provides for the controlled introduction of new technologies and
the appropriate reuse of existing technology to increase returns on investment.

The SAR process informs agency representatives regarding:

     •   Cybersecurity and privacy requirements;
     •   Cross-Agency interoperability of systems;

     •   Data sharing and reuse;

     •   Opportunities to leverage economies of scale and/or existing solutions;
     •   Impact on existing technology infrastructure and operations;

     •   Prioritization of resources, including staff levels; and

     •   Disaster recovery & business continuity requirements.

2.       PARTY PARTICIPATION
All relevant stakeholders from NJOIT, New Jersey Office of Homeland Security and
Preparedness (NJOHSP), the Division of Purchase and Property (DPP), and the reviewee-
Agency will participate in SAR reviews. Participation will be done either through
meetings or electronic review, depending on the nature of the checkpoint.

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                         Page 1 of 7

Participation will be determined based on the expertise required for the specific project.
The Agency’s Business Owner/Project Sponsor or their designee must attend scheduled
SAR review meetings.

3.       CRITERIA
A SAR is required when a new solution/component/module is being developed or
acquired, including but not limited to:

     •   Procurement of a Commercial-off-the-Shelf (COTS) package;
     •   Utilizing an “X as a Service” solution, including, but not limited to Software (SaaS),
         Platform (PaaS), or Infrastructure (IaaS);

     •   Custom development software applications;

     •   Integrating new hardware within the Garden State Network;

     •   Installing new hardware at any of the State Enterprise Data Centers.
     •   When a significant enhancement or modification is being made to an existing
         solution. Significant enhancements/modification examples include, but are not
         limited to:

         o Addition, modification or removal of enterprise solutions or functionality such
           as e-mail, e-payment, myNJ (SSO), or reporting functionality;

         o Addition, modification or removal of application specific functionality such as
           adding/removing a server call, adding/removing a web service call;
         o Changes to an extranet or firewall;

         o Changes to any information system platform (e.g. database, web server,
           application server, etc.);

         o An information or data system with application design changes since the last
           SAR;
         o A vendor solicitation with an information technology requirement. e.g.,
           Request for Proposal (RFP); Request for Quotation (RFQ); Request for
           Information (RFI).

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                          Page 2 of 7

4.       PROCEDURE
The SAR process should begin as early as possible in the project lifecycle, ideally before
any procurement or development activities begin. There are four stages to the SAR
process.

Step 1: Technology Initiation Proposal (TIP)

Submission of a Technology Initiation Proposal (TIP) by the Agency is the required first
step.
     •   A TIP Request, with complete supporting documentation, must be submitted to
         SAR. SAR related forms for submission can be found at
         https://nj.gov/it/whatwedo/sar/. Any questions regarding completion of the
         documentation may be sent to SAR@tech.nj.gov.

     •   Only one phase of SAR should be requested at a time (Technology Initiation
         Proposal, Logical, Validated Design, or Implementation).

     •   Electronic reviews (eReviews) are held as warranted.
     •   SAR documents older than one year must be updated with current
         information before submitting.

     •   If providing an update, resubmissions must identify the reason(s) for the change
         or modification.

     •   Scheduling is handled on a first submitted, first reviewed basis.
     •   TIP meetings are scheduled weekly on Monday afternoons.

A TIP review is performed before a final RFP/RFQ/RFI is generated and after the Agency
obtains internal approval of the business case. During the TIP review, NJOIT shall
facilitate discussion and:

     •   Evaluate the documentation provided. Documents should be reviewed section by
         section during the meeting, any changes or questions must be noted;
     •   Confirm the project aligns with the State’s enterprise architecture strategy,
         standards, and processes;

     •   Confirm the project aligns with the State’s data and information management
         strategy, standards, and processes;

     •   Evaluate the request’s impact on existing infrastructure or IT capacity;

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                          Page 3 of 7

   •   As appropriate, recommend leveraging existing State assets and consider how
       the proposed solution might be used by others;

   •   Confirm the plan complies with State and/or federal cybersecurity
       requirements;
   •   Review and validate data classification for the proposed solution; and

   •   Identify the costs and risks of certain decisions.

Upon completion of the TIP review, a marked up TIP document is distributed along with a
meeting RECAP (excel spreadsheet) via e-mail to all participants. The TIP document and
RECAP include discussion points from the meeting and any Action Items that must be
resolved before the Logical SAR.

Step 2: Logical SAR (LSAR)

For the next step, the Agency submits their completed LSAR (On Premises or Cloud) to
request a review, along with their updated RECAP spreadsheet.

   •   An LSAR review is performed before any hardware or software is installed, before
       any coding has begun, and after an RFP or RFQ is awarded.

   •   Reviews may be conducted electronically (eReview) or via scheduled meetings,
       depending on the complexity of the project and the nature of the feedback
       required, at the discretion of the SAR internal review team.
   •   Meetings are scheduled on the second and fourth Thursdays of the month.
       Exceptions to this are the months of November and December where the reviews
       may be rescheduled to alternate Thursdays due to the holidays.

During the LSAR review, NJOIT shall facilitate discussion and:

   •   Evaluate the documentation provided. Documents are reviewed section by
       section during the meeting and any changes or questions are noted;
   •   Ensure that capacity, resources, hardware and software needs are identified;

   •   Ensure that the data requirements are defined;

   •   Ensure that infrastructure requirements are defined; and
   •   Reaffirm that cybersecurity requirements are defined.

Upon completion of the LSAR meeting (or eReview) a marked up LSAR document is
distributed via e-mail along with a meeting RECAP (excel spreadsheet) to all participants,

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                      Page 4 of 7

which includes discussion points from the meeting and any Action Items that must be
resolved before the final SAR, the Implementation review (IR).

Step 3: Validated Design

In this step, the Agency creates and submits their completed design document to the
NJOIT Solutions Architecture (SA) Team.

   •   The SA Team provides guidance in the creation of the design document when
       needed and then presents them to NJOIT’s Information Security Unit (ISU) and
       NJOHSP for approval.

   •   The Validated Design checkpoint is the point in a project’s lifecycle that marks the
       end of the design phase. This means that the system components, data and
       control flows, and interfaces have been finalized and documented in diagram
       form.

   •   The final design is also used as the reference point for any operational work that
       needs to be done, (e.g., firewall rule requests, server build work, etc.). Completion
       of Validated Design is a prerequisite for the IR stage.
During the Validated Design, NJOIT shall facilitate discussion and:

   •   Update the logical design from the LSAR with system components, data and
       control flows, and all interfaces;

   •   Ensure that required resources and integrations are identified; and
   •   Ensure the design is vetted by security teams, to ensure compliance with
       appropriate governance.

Upon approval of the Validated Design, NJOIT will notify the Agency that the Validated
Design is complete. The Agency then needs to submit work requests to trigger NJOIT
business units’ work related to the solution.

Step 4: Implementation Review (IR) SAR

In this final step, the Agency submits their completed IR form (On Premises or Cloud) to
request a review, along with their updated RECAP spreadsheet.

   •   An IR SAR should be requested no less than two weeks before go-live of any
       phase.

   •   An IR is held electronically and there is a five-business day review cycle.

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                           Page 5 of 7

During the Implementation Review, NJOIT shall facilitate discussion and:

     •   Evaluate the documentation provided. Documents are reviewed section by
         section and any changes or questions are noted;
     •   Determine whether the project is ready for deployment – all outstanding action
         items are resolved and/or remediated;

     •   Ensure that all cybersecurity requirements are successfully tested; and

     •   Ensure that the date for deployment, impact on other systems and related
         deployment activities have been assigned, agreed upon, and communicated to
         stakeholders well in advance.
Upon completion of the review, a marked-up IR document is distributed via e-mail along
with a RECAP (excel spreadsheet) to all participants, which includes discussion points
from the review and any Action Items that must be resolved before project end.

During an e-Review:

     •   There is a five-business day review cycle.
     •   NJOIT distributes the SAR request and documents to all participants for their
         review and comment.

     •   The Agency is responsible for answering any questions/concerns raised during
         the eReview.

     •   NJOIT compiles questions and responses into notes, which are sent out at the
         end of the e-Review cycle, along with any notes on Action Items that have been
         raised. (Note: Please allow approximately five business days after the end of the
         stated review period for the closing notes to be distributed.)

     •   NJOIT will cancel the e-Review and schedule a formal meeting if the questions
         raised during the review cycle require more discussion than can be successfully
         concluded through e-mail.
NJOIT reserves the right to change or amend this Procedure at any time.

5.       RELATED FORMS AND DOCUMENTS
Forms and templates required for the SAR process can be found on the NJOIT website:
https://nj.gov/it/whatwedo/sar/. Ancillary SAR documents may also be found at this
location.

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                         Page 6 of 7

6.         ADMINISTRATION
This Policy is administered and monitored by the CTO at 300 Riverview Plaza, Trenton,
NJ 08625. The Policy must be reviewed annually; however, the CTO reserves the right to
change or amend the Policy at any time.

Signature on File                                                  7/14/2026
Kevin J. Dehmer, Chief Technology Officer                          Date

 Version    Published Date         CTO         Sections Modified   Description of Modifications
   1.0        12-12-2016      Christopher J.                          Original Published Date
                                   Rein
     2.0      09-13-2024      Christopher J.         1-5
                                   Rein
     3.0      07/14/2026     Kevin J. Dehmer          1-4          Updated Format and Procedures.
                                                                     Updated CTO and Governor
                                                                    Name. Clarified descriptions;
                                                                        removed PSAR step

16-05-P1-NJOIT, System Architecture Review (SAR) Procedure                             Page 7 of 7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
