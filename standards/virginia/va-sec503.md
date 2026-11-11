---
schema_version: 1
corpus: states-government-it
jurisdiction: virginia
id: va-sec503
title: Secure Remote Access to Online Court Documents Standard (SEC503)
doc_type: standard
citation: ITRM Standard SEC503
authority_level: ''
issuing_body: Virginia Information Technologies Agency (VITA)
source_url: https://www.vita.virginia.gov/media/vitavirginiagov/it-governance/psgs/pdf/RemoteAccessDocsCrtContrdSEC503.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 9b9f065aad1747e460a1d924b8cda77a7eb173a8c971bbadcbc6de686cd59364
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
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Secure Remote Access to Online Court Documents Standard (SEC503) (ITRM Standard SEC503)

## At a glance

Item of the VITA library, topic 'Information Security', Information Security Standards: security standard for remote access to online court documents. The obligated parties are the clerks and courts that offer remote access, not executive branch agencies; seeded because the library lists it as a standard.

## Full text

    COMMONWEALTH OF VIRGINIA
    Enterprise Architecture (EA)
    Information Technology
    Resource Management (ITRM)

                  Security Standard for
                  Remote Access to
                  Court Documents
                  Online

                     ITRM Standard (SEC 503-03)
                                          2025
1

 Security Standard for Remote Access to Court Documents Online                                  ITRM Standard SEC503-03

PUBLICATION VERSION CONTROL

 Publication Version Control: It is the user's responsibility to ensure they have the latest version of
 this ITRM publication. Questions should be directed to VITA’s Director, Security Governance, within
 Commonwealth Security and Risk Management (CSRM). Changes to this Standard will be posted
 on the Virginia Regulatory Townhall, at: https://townhall.virginia.gov/L/GDocs.cfm?BoardID=165.

Version             Date                                Purpose of Revision
Original            11/07/2003                          Base Document
Revision 1          12/17/2003                          Removed the notion of “purpose” from the document
                                                        by eliminating
                                                        language that mentions “business use.”
Revision 2          03/28/2005                          Update the Standard to comply with statutory changes,
                                                        including to Virginia Code § 2.2-3808.2 regarding the
                                                        certifying entity for secure remote access to
                                                        documents on court-controlled websites, Virginia Code
                                                        § 17.1- 279 concerning circuit court clerks certifying
                                                        their compliance with security standards developed by
                                                        VITA, and a modification to the definition of
                                                        “Subscriber” to include “Corporate Subscriber.”
                    12/08/2016                          Administrative update. No substantive changes were
Revision 2.1                                            made to this document.

Revision 2.2 6/21/2017                                  Administrative update. No substantive changes were
                                                        made to this document.

Revision 3          See Virginia                        Administrative update. Moving into the guidance
                    Regulatory Town                     document process.
                    Hall. Approximately
                    03/2025

 PREFACE
 Publication Designation
 ITRM Standard SEC503: Security Standard for Remote Access to Court Documents Online

 Subject
 Security standard for remote access to documents on court controlled websites

 Effective Date
 See Virginia Regulatory Town Hall. Approximately 03/2025

 Supersedes
 All prior versions of COV ITRM Standard SEC503

 Scheduled Review
 Will be performed as required

Security Standard for Remote Access to Court Documents Online                     ITRM Standard SEC503-03

Authority and Related Code Sections

Code of Virginia §17.1-279
(Additional fee to be assessed by circuit court clerks for information technology)

Code of Virginia §17.1-292
(Applicability; definitions)

Code of Virginia §17.1-293
(Posting and availability of certain information on the Internet; prohibitions)

Code of Virginia §17.1-294
(Secure remote access to land records)

Code of Virginia §2.2-3803

(Administration of systems including personal information; Internet privacy policy; exceptions)

Code of Virginia §17.1-227
(Documents to be recorded in deed books; social security numbers)

Code of Virginia § 20-121.03
(Identifying information confidential; separate addendum)

Scope
Pursuant to Code of Virginia, §17.1-279, circuit court clerks’ offices or application service providers
will provide secure remote access to land records via paid subscription service. Such access will
comply with security standards developed by VITA, pursuant to §17.1- 294.

Objectives
To set forth the components for a security standard to govern subscribers’ access to court
documents on court controlled websites.

General Responsibilities

Virginia Information Technologies Agency (VITA)
VITA is responsible for developing standards for the security of remote access to documents on
court controlled websites, in consultation with the circuit court clerks, the Office of the Executive
Secretary of the Supreme Court, the Compensation Board, and other stakeholders.

Court Clerks
Responsible for complying with ITRM Standard SEC503.

Related COV ITRM Policies, Standards and Guidelines
ITRM Standard SEC530_(Information_Security_Standard) (virginia.gov)
Information Systems Facilities Security Guideline SEC517

       Security Standard for Remote Access to Court Documents Online                                                        ITRM Standard SEC503-03

                                                                  Table of Contents

PUBLICATION VERSION CONTROL ....................................................................................................... 2
1.     INTRODUCTION ................................................................................................................................ 1
     1.1      Authority ..................................................................................................................................... 1
     1.2      Approach .................................................................................................................................... 1
     1.3      Reviews ...................................................................................................................................... 1
     1.4      Definitions .................................................................................................................................. 1
REQUIREMENTS FOR RESTRICTED REMOTE ACCESS TO DOCUMENTS ON COURT-
CONTROLLED WEBSITES........................................................................................................................ 2
     1.5      Establish a Precondition for Access to a Network or System ........................................... 2
     1.6      Restricted Access Requirements ........................................................................................... 2
     1.7      Secure Website Certification................................................................................................... 3
2.     APPENDICES ..................................................................................................................................... 5
     2.1      Appendix A: Example Application .......................................................................................... 5
     2.2      Appendix B: Example Subscriber Agreement ....................................................................... 6
     2.3      Appendix C: Self-Certification ................................................................................................. 9

     Security Standard for Remote Access to Court Documents Online         ITRM Standard SEC503-03

1.   INTRODUCTION

1.1 Authority

     This standard pertains only to the access to documents posted on court-controlled websites
     through the use of the Internet.

1.2 Approach

     This standard is consistent with the provisions of COV ITRM Standard SEC530: Information
     Technology Security Standard (SEC530).

     The standard consists of the following:

           • Establish a Precondition for Access to a Network or System
           • The Restricted Access Requirements
           • Secure Website Certification

     These components provide a framework to restrict remote access to all documents on court-
     controlled websites. For each component listed above a subset of standards has been
     identified that comprises this standard.

     1.3 Reviews

     A full review of this standard will be performed when requested or required by law.

     1.4 Definitions

        “Public access” means that the public can inspect and obtain a copy of the information in a
        court record.

        “Remote access” means that inspection can be made without the need to physically visit
        the courthouse where the court record is maintained.

        “Subscriber” means any person authorized by the Clerk of a Circuit Court to have remote
        access to court documents on its website. If a business or non-profit entity, organization or
        association (referred to collectively as “Corporate Subscriber”) wishes to become a
        subscriber, it shall identify each individual employee who will have remote access to the
        documents on the circuit court-controlled website and each individual employee shall
        obtain a User ID and Password from the clerk. However, the Corporate Subscriber shall
        execute the Subscriber Agreement and be responsible to the circuit court for the fees and
        the proper use of the website pursuant to the Subscriber Agreement.

         “Court Controlled Website for Documents” means a website or remote access system
         owned and operated by the Court or a public or private agent that operates the website for
         the Court.

                                                    1

Security Standard for Remote Access to Court Documents Online         ITRM Standard SEC503-03

REQUIREMENTS FOR RESTRICTED REMOTE ACCESS TO
DOCUMENTS ON COURT-CONTROLLED WEBSITES
This section sets forth the specifications for the Security Standard for Restricted Remote
Access to Documents on Court- Controlled Websites pursuant to § 17.1-294 of the Code of
Virginia.

1.5 Establish a Precondition for Access to a Network or System

As a precondition and a safeguard, the Subscriber shall complete an application for Internet
access to court-controlled documents. The application form (an example of which is in
Appendix A) consists of basic identification information, including the prospective Subscriber's
identity, business or residence address, and citizenship status.

  2.1.1 To register a prospective Subscriber shall provide the following information:
             • Last Name
             • First Name
             • Business Name (if applicable)
             • Street Address
             • City/State/Zip Code
             • Phone Number
             • Email Address
             • Citizenship Status
             • Signature

  2.1.2 Registration must be in person or by means of a notarized or otherwise sworn
  application that establishes the prospective Subscriber’s identity, business or residence
  address, and citizenship status.

  2.1.3 By signing the Application (See: Appendix A, Example Application), the Subscriber
  acknowledges and accepts the terms and conditions of the Subscription Agreement for
  Internet Access to Circuit Court Documents (see: Appendix B, Example Subscriber
  Agreement).

1.6 Restricted Access Requirements

Remote access to any document posted on a court-controlled website is restricted to pre-
registered Subscribers.

  2.2.1 Pursuant to § 17.1-294 of the Code of Virginia, an application must be completed and
  approved by the Clerk of the Circuit Court from which the Subscriber wishes to inspect and
  obtain a remote copy of information via the Circuit Court website. This requirement applies
  to all individuals accessing documents on court-controlled websites regardless of whether
  they were a user of this service prior to the effective date of this standard. An example
  Application is in Appendix A.

  2.2.2 The pre-registered Subscriber must comply with the terms of the Subscription
  Agreement for Internet Access to Circuit Court Documents, referred to as “Agreement.” An
  example Agreement is in Appendix B.

                                               2

Security Standard for Remote Access to Court Documents Online           ITRM Standard SEC503-03

1.7 Secure Website Certification

Pursuant to §17.1-294 and §17.1-279 of the Code of Virginia, VITA is responsible to develop
security standards for secure remote access to any document posted on a court controlled
website; and the individual circuit court clerks or their vendor/service provider on their behalf
shall certify compliance to the Compensation Board (herein after referred to as “the Board”)
with such security standard.

 2.3.1 No Clerk shall post on a court-controlled website any document that is restricted,
 pursuant to §17.1-294 or §2.2-3808.2 of the Code of Virginia, without first certifying to VITA
 and the Board that its court-controlled website is secure and provides for restricted access.

 2.3.2 To certify and to retain certification as secure for restricted remote access, pursuant to
 § 17.1-279 of the Code of Virginia, a court-controlled website shall comply with both this
 security standard and SEC530. Regarding SEC530, the following sections are mandatory: (A.)
 Business Analysis and Risk Assessment; (E.) Authentication, Authorization and Encryption;
 (F.) Data Security; (G.) Systems Interoperability Security; (H.) Physical Security; (I.) Personnel
 Security; and (J.) Threat Detection. The other sections of SEC530 are highly recommended
 as best practices.

 A complete risk assessment is appropriate the earlier of (i) every five years measured from
 the date of the last complete risk assessment, (ii) whenever a change occurs in the physical
 plant of the court facilities that affects security, or (iii) a change occurs in the technological
 systems utilized by the court that affects security. When a change in either physical plant or
 technological systems occurs, the clerk should provide a certification that either (a) the level
 of risk has not changed, or (b) if the level of risk changed, that a supplemental risk
 assessment has been provided. The clerk may base his/her certification upon the
 representation of any vendor that any change in the physical or technology system should
 not compromise system security. However, no additional risk assessment is appropriate if
 the changes to the physical plant or the technological systems are implementations of a
 previous risk assessment.

 2.3.3 A Clerk shall self-certify, or cause to be self-certified by their vendor/service provider on
 their behalf, a court-controlled website by one of the following methods:

             (i) Self-certified to the Board via its automated web system during the
             annual Technology Trust Fund budget cycle.

             (ii) Complete and return the Self-Certification form (see: Appendix C) to the
             Board.

   The Board shall confirm receipt to the Clerk by email within five (5) business days after
  receipt of the Self-Certification form.

 2.3.4 All Clerks shall maintain a record of each Subscriber application received, regardless of
 whether the application was approved or not, as well as a record of all remote access
 permitted to court-controlled documents on its website. Commercial software is available,
 for web servers that do not have a built-in monitoring and surveillance capability, to keep
 electronic logs of transactions.

                                                3

Security Standard for Remote Access to Court Documents Online         ITRM Standard SEC503-03

 2.3.4 VITA or the Clerk’s auditor may inspect the records pertaining to remote access and
 audit compliance with this standard and SEC530 of certified court- controlled websites, upon
 reasonable prior written notice to the Clerk.

 2.3.5 If a court-controlled website is not in compliance with this standard, the Clerk shall be
 immediately informed by email to discontinue all public access to the website until it can re-
 certify to be in compliance.

                                               4

     Security Standard for Remote Access to Court Documents Online            ITRM Standard SEC503-03

2.   APPENDICES
     2.1 Appendix A: Example Application
      (may be varied by the Clerk as necessary/appropriate)

      APPLICATION FOR INTERNET ACCESS TO RECORDS MANAGEMENT SYSTEM

     The approval of this application is at the Clerk of the Circuit Court's discretion. By signing this
     application the Subscriber acknowledges and accepts the terms and conditions of the
     Subscriber Agreement for Internet Access to Circuit Court Documents.

     SUBSCRIBER:
       CORPORATE NAME:

     INDIVIDUAL’S LAST NAME:

     INDIVIDUAL’S FIRST NAME:

     BUSINESS NAME (if applicable)

     STREET ADDRESS
     CITY/STATE/ZIP
     PHONE NUMBER
     EMAIL ADDRESS

     UNITED STATES CITIZEN             Y       N (Please circle one )

     SIGNATURE

     I certify that the information above is true and correct.

     I, _______________________, a Notary Public, do hereby certify that on this ___ day of _____________,
     20___ , ______________________________ personally appeared before me and swore and
     acknowledged to me that the statements contained therein are true and correct.
     Notary Public, County of ___________________________________________
     Name (Typed or Printed):___________________________________________
     My Commission Expires: ___________________________________________
     Notary Phone Number:

     For use by Circuit Court Clerk's Office only
     SUBSCRIBER ID
     PASSWORD
     EXPIRATION DATE

                                                      5

Security Standard for Remote Access to Court Documents Online            ITRM Standard SEC503-03

2.2 Appendix B: Example Subscriber Agreement
(may be varied by the Clerk as necessary/appropriate)

                 SUBSCRIBER AGREEMENT FOR INTERNET ACCESS TO
                             CIRCUIT COURT DOCUMENTS

   1.     TERM OF AGREEMENT

It is the intent of both parties to participate in a remote access program to commence on the
day the User ID and Password are assigned and continue until terminated as provided herein.

   2.     SUBSCRIBER OPTIONS

The Clerk provides an on-line database allowing “inquiry-only” access to the particular court's
indices and/or documents.

   3.     DAYS AND HOURS OF OPERATION

The Internet access to the Circuit Court documents may be available seven days a week, twenty-
four hours a day, including all holidays, or otherwise at the discretion of the Clerk, except during
periods:

           a.     Of preventative and remedial maintenance
           b.     Of operational issues beyond the control of the Clerk
           c.     When intrusions against security are being remedied

   4.     FEES

The fee for the Subscriber is $_ per ; and the transactional fee is $ per transaction. Fees are
charged at the discretion of the Clerk. If a fee is charged, payment is due upon the issuance of
the User ID and Password. The transactional fee is due upon receipt. The Clerk reserves the
right to suspend or terminate service to the Subscriber if payment is not received. All fees are
subject to change.

   5.     SERVICES

The Clerk, deputies, employees or agents shall provide the Subscriber with “inquiry-only” access
to the documents management system database (the Database).

The Clerk, deputies, employees or agents shall provide the Subscriber with documentation and
limited consultation on specific problems that arise in the use of the website. The Clerk does
not guarantee consultation results nor warrant or represent that all errors or problems shall be
corrected.

   6.     SUBSCRIBER'S OBLIGATIONS

It is the responsibility of the Subscriber to purchase computer hardware and software and/or
make modifications to their existing equipment that are necessary for access to the Database.

                                                 6

Security Standard for Remote Access to Court Documents Online          ITRM Standard SEC503-03

The Subscriber is responsible for ensuring that unauthorized personnel do not use the
Subscriber’s computer. Information accessed from the Database is for the use of the
Subscriber.

   7.     LIMITATION OF LIABILITY

The Subscriber relieves and releases the Clerk, deputies, employees or agents from liability for
any and all damages resulting from interrupted service of any kind. The Subscriber further
relieves and releases the City/County of                        , its Board of Supervisors,
officers and their deputies, employees and agents from liability for any and all damages
resulting from interrupted service of any kind. The Subscriber also relieves and releases the
Office of the Executive Secretary, Supreme Court of Virginia, employees and agents from
liability for any and all damages resulting from interrupted service of any kind.

The Subscriber hereby relieves and releases and holds harmless the Clerk, the City/County of
                   , its Board of Supervisors, officers and their deputies, employees or agents of
any liability for any and all damage resulting from incorrect data or any other misinformation
accessed from this service. The Subscriber also relieves and releases the Office of the
Executive Secretary, Supreme Court of Virginia, employees and agents from liability for any and
all damages resulting from incorrect data or any other misinformation accessed from this
service.

The Subscriber agrees that the Clerk, the City/County of_________________, its Board of
Supervisors, officers and their deputies, employees or agents shall not be liable for negligence
or lost profits resulting from any claim or demand against the subscriber by any other party.
The Subscriber also relieves and releases the Office of the Executive Secretary, Supreme Court
of Virginia, employees and agents from liability for any and all damages resulting from any
claim or demand against the subscriber by any other party.

The information or data accessed by the Subscriber may or may not be the official government
record required by law. In order to assure the accuracy of the data or information, the Subscriber
should consult the official governmental record.

  8.      TERMINATION

Either party may terminate this agreement without cause with fifteen (15) days email notice to
the other. Subscriber remains responsible for payment of fees, pro rata, for services rendered
or obligations incurred.

This agreement may be immediately terminated by the Clerk for Subscriber's failure to provide
correct or complete information on the application, failure to comply with the terms of this
agreement, failure to make payments of fees or breach of agreement.

This agreement shall terminate immediately if the Commonwealth of Virginia or City/County of
_______________fail to appropriate and continue funding for services provided under this
agreement.

  9.      DEFINITIONS

        i. “Public access” means that the public can inspect and obtain a copy of the
        information in a court record.

                                                7

Security Standard for Remote Access to Court Documents Online         ITRM Standard SEC503-03

        ii. “Remote access” means that inspection can be made without the need to physically
        visit the courthouse where the court record is maintained.

        iii.      “Subscriber” means any person authorized by the Clerk of a Circuit Court to
        have remote access to court documents on its website. If a business or non- profit
        entity, organization or association (referred to collectively as “Corporate Subscriber”)
        wishes to become a subscriber, it shall identify each employee who will have remote
        access to the documents on the circuit court-controlled website and each employee
        shall obtain a User ID and Password from the clerk. However, the Corporate Subscriber
        shall execute the Subscriber Agreement and be responsible to the circuit court for the
        fees and the proper use of the website pursuant to the Subscriber Agreement.

        iv.      “Court Controlled Website for Documents” means a website or remote access
        system owned and operated by the Court or a public or private agent that operates the
        website for the Court.

  10.      APPLICATION

Pursuant to §17.1-294 of the Code of Virginia, an application must be completed. The
application must be approved by the Clerk's office before the User ID and Password can be
issued.

                                               8

Security Standard for Remote Access to Court Documents Online                 ITRM Standard SEC503-03

2.3 Appendix C: Self-Certification
(Vendor/Service Provider on behalf of a Circuit Court Clerk)

               CIRCUIT COURT-CONTROLLED WEBSITE SELF-CERTIFICATION

                   Chief Information Officer
                   Virginia Information Technologies Agency
                   7325 Beaufont Springs Drive
                   Richmond, VA 23225

TO:                Executive Secretary
                   Compensation Board
                   P.O. Box 710
                   Richmond, VA 23218-0710

FROM:              Clerk of the Circuit Court of                          City/County

RE:                Certification   of   Circuit    Court-Controlled
                   Website

I, (Full Name of Clerk), Circuit Court Clerk, Court of                  City/County
certify that, as of this date and to the best of my knowledge, information, and belief, this Court’s
website and supporting computer network or system:

      1.     Restricts remote access to court-controlled documents posted on it that contain the
      following information: (i) an actual signature; (ii) a social security number; (iii) a date of birth
      identified with a particular person; (iv) the maiden name of a person's parent so as to be
      identified with a particular person; (v) any financial account number or numbers; or (vi) the
      name and age of any minor child – to only those Subscribers approved by myself or my
      designee.

      2.    Is consistent with §17.1-293 of the Code of Virginia (Posting and availability of certain
      information on the Internet; prohibitions).

  In compliance with the following mandatory provisions of ITRM Standard SEC 530:
  Information Security Standard: (A.) Business Analysis and Risk Assessment; (E.)
  Authentication, Authorization and Encryption; (F.) Data Security; (G.) Systems Interoperability
  Security: (H.) Physical Security: (I.) Personnel Security; and (J.) Threat Detection.

      3.    In compliance with the provisions of ITRM Standard SEC503: Security Standard for
      Restricted Remote Access to Documents on Court-Controlled Websites.

Signature of the Clerk of the Circuit Court          Date

Print Name
Clerk of the Circuit Court,                          City/County

                                                     9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
