---
schema_version: 1
corpus: states-government-it
jurisdiction: delaware
id: de-in-dbms-002
title: Database Management Systems Guideline
doc_type: standard
citation: DTI Guideline ID IN-DBMS-002
authority_level: ''
issuing_body: Delaware Department of Technology and Information (DTI)
source_url: https://webfiles.dti.delaware.gov/pdfs/pp/DatabaseManagementSystemsGuideline.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 2fc2e4345b117ca2570ab1b48e58267a0f1993ed658c838489daf99ef7c1a0da
effective_date: '2023-01-13'
source_version: Revision 2 (reviewed 07/18/2024)
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
- data
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Database Management Systems Guideline (DTI Guideline ID IN-DBMS-002)

## At a glance

Item of the DTI Standards and Policies library, section 'Information': a guideline of the Delaware State-Wide Information Technology and Architecture Standards (Domain: Platform; Discipline: Data Management).

## Full text

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

            Guideline ID:     IN-DBMS-002

                   Title:     Database Management Systems Guideline

     Revision Number:         2

                Domain:       Platform

              Discipline:     Data Management

               Effective:     01/13/2023
              Reviewed:       07/18/2024
        Approved By:          Chief Technology Officer
               Sponsor:       Chief Technology Officer

I.            Authority, Applicability and Purpose
      A. Authority: Title 29 Chapter 90C Delaware Code, §9004C – General Powers, duties and
         functions of DTI “2) Create, implement and enforce statewide and agency technology solutions,
         policies, standards and guidelines, including as recommended by the CIO”
      B. Applicability: Applies to all State of Delaware communications and computing resources. The
         Department of Technology and Information (DTI) is an Executive Branch Agency and has no
         authority over the customers in Legislative and Judicial Branches, as well as Local Education
         Agencies, and other Federal and Local Government entities that use these resources. However,
         all users, including these entities, must agree to abide by all policies, standards promulgated by
         DTI as a condition of funding, access and continued use of these resources.
      C. Purpose: Currently, the State has multiple database management systems in production with
         multiple number of versions of these database management systems. This guideline will identify
         those database management systems and versions that are considered appropriate for the State
         to concentrate on in the future.

II. Scope
       A.    Areas Covered: Only general use DBMS are covered by this guideline, not proprietary use
             databases such as laboratory or instrumentation databases, not Document Management
             Systems or specific-use applications like Active Directory, Outlook, e-mail, or Calendaring.
             When available, a general use DBMS is recommended over a proprietary solution.
       B.    Environments: This guideline will cover all database management systems (DBMS) installed
             or in use by the State of Delaware, including data owned by the State but housed by third-party
             contractors. This guideline does not apply to computer systems where the Federal Government
             dictates what DBMS to be used.

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            1 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

III. Process
     A.    Adoption: These guidelines have been adopted by the Department of Technology and
           Information (DTI) through the Technology and Architecture Standards Committee (TASC) and
           are applicable to all Information Technology use throughout the State of Delaware.
     B.    Revision: Technology is constantly evolving; therefore the guidelines will need to be regularly
           reviewed. It is the intent of the TASC to review this guideline annually. The TASC is open to
           suggestions and comments from knowledgeable individuals within the state, although we ask
           that they be channeled through your Information Resource Manager (IRM).
     C.    Contractors: Contractors or other third parties are required to comply with these guidelines
           when proposing technology solutions to DTI or other state entities. Failure to do so could result
           in rejection of the proposed technology solution. For further guidance, or to seek review of a
           component that is not rated below, contact the TASC at dti_tasc@delaware.gov.
     D.    Implementation responsibility: DTI and/or the organization’s technical staff will implement
           these guidelines during the course of normal business activities, including business case
           review, architectural review, project execution and the design, development, or support of
           systems.
     E.    Enforcement: DTI will enforce these guidelines during the course of normal business activities,
           including business case and architectural review of proposed projects and during the design,
           development, or support of systems. These guidelines may also be enforced by others during
           the course of their normal business activities, including audits and design reviews.
     F.    Contact us: Any questions or comments should be directed to dti_tasc@delaware.gov.

IV. Definitions/Declarations
     A.    Definitions
              1. Database: A collection of information organized in such a way that a computer program
                 can quickly select desired pieces of data. Traditional databases are organized by field,
                 record and file. A field is a single piece of information; a record is one complete set of
                 fields; and a file is a collection of records. To access information from a database, a
                 database management system (DBMS) is needed. This is a collection of programs that
                 enables the user to enter, organize, and select data in a database.

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            2 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

              2. Database Management System (DBMS): A collection of programs that provides the
                 capability to store, modify, and extract information from a database. There are many
                 different types of DBMS's, ranging from small systems that run on personal computers to
                 large systems that run on midrange or mainframes. The terms relational, flat, network
                 and hierarchical all refer to the way a DBMS organizes information internally. The internal
                 organization can affect how quickly information can be extracted. Requests for
                 information from a database are made in the form of a query, which is a stylized question.
                 The set of rules for constructing queries is known as a query language. Different DBMS's
                 support different query languages, although there is a semi-standardized query language
                 called SQL (structured query language). For the purposes of this document, database
                 and database management system are used interchangeably.
              3. Scalable: Scalable database is defined as the capability of the database to meet
                 current/future requirements without major effects on the existing structures. A scalable
                 database will easily grow in both size and infrastructure with little or no measurable
                 impact on the performance of the operational database, system, or network
              4. Enterprise Database: A database or group of databases supporting a Statewide or multi-
                 agency function or system with a single administrative authority. A database or group of
                 databases supporting operations deemed critical to the business of the State or agency.
              5. Desktop DBMS: a type of DBMS which is designed for running small scale databases,
                 generally located on personal computers.
              6. Mission Critical System: A system that is critical to the functioning of an organization and
                 the accomplishment of its mission. Therefore, if a mission critical system is lost or
                 unavailable, the agency will be unable to perform some or all of its most basic functions.
                 Also, a system is deemed mission critical if its loss would cause an unacceptable
                 slowdown in the functioning of an agency.
              7. Personal Workstation: Any computing device engineered to remain stationary that
                 contains a hard drive, memory, and CPU (the monitor and keyboard are usually separate
                 pieces from the PC case) and expansion slots. The intent of the device is to be used by
                 one person at a time, or perhaps one person and a print service.
              8. Embedded: An embedded system is some combination of computer hardware and
                 software, either fixed in capability or programmable, that is specifically designed for a
                 particular kind of application device. Industrial machines, automobiles, medical
                 equipment, cameras, household appliances, airplanes, vending machines, and toys are
                 among the possible hosts of an embedded system. Embedded systems that are
                 programmable are provided with a programming interface, and embedded systems
                 programming is a specialized occupation.
              9. System Administrator: The human being responsible for running and maintaining a
                 computer system at the Operating System (OS) level especially a mainframe,
                 minicomputer, or local area network. System administrators, sometimes called network
                 administrators, issue login names, maintain security, fix failures, and advise management
                 about hardware and software purchases.

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            3 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

              10. Remote Access: It is a means by which users can gain authenticated access to internal
                  network resources, preferably without posing a security risk to valuable assets within the
                  network.
              11. Programmable Access: It is a means of reading and updating data in a database
                  management system through controlled machine instructions.
              12. Database Administrator: A database administrator (DBA) is a person responsible for the
                  design, implementation, maintenance and repair of an organization’s database. A DBA
                  maintains database logins, maintains database security, monitors performance and
                  performs database software patches/upgrades.
              .
     B.    Declarations
          A DBMS should:

          1. Be tunable for performance and space maximization.
          2. Be scalable.
          3. Work within the State’s IT Infrastructure.
          4. Provide the ability to minimize redundant data.
          5. Be able to secure data structures.
          6. Contain data integrity facilities;
                    o    Provide Point-in-time recovery
                    o    General backup/restore methodology
                    o    Ensure that what was intended to be written was, in fact written.
          7. Be ‘system administrator’ friendly;
                    o    Contain tunable operational parameters
                    o    Provide tools for modifying data file/table design
                    o    Utility suite for support functionality.
          8. Provide audit trail capabilities.
          9. Provide for transaction rollback.
          10. Have a search/update engine that will accompany the relational database or provide a
              “vehicle” to interface with existing 3gl/4gl integrated software.
          11. Adhere to the Software Policy, Delaware Information Security Policy, and Systems
              Architecture Standard.

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            4 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

V. Guidelines

     A.    Definition of Ratings
              1.    Component Ratings

                                    COMPONENT RATING                                                     USAGE NOTES

           STANDARD – DTI offers internal support and/or has arranged for                          These components can be
           external vendor support as well (where applicable). DTI believes the                    used without explicit DTI
           component is robust and can be expected to enjoy a useful life of 3+                    approval for both new
           years from the Effective Date.                                                          projects and enhancement
                                                                                                   of existing systems.

           DECLINING – Deprecated - DTI considers the component to be a                            Via the State’s waiver
           likely candidate to have support discontinued in the near future. A                     process, these components
           deprecated element is one becoming invalid or obsolete.                                 should be explicitly approved
                                                                                                   by DTI for all projects. They
                                                                                                   should not be used for minor
                                                                                                   enhancement and system
                                                                                                   maintenance without explicit
                                                                                                   DTI approval via the State’s
                                                                                                   waiver process.

           DISALLOWED – DTI declares the component to be unacceptable for                          No waiver requests for new
           use and will actively intervene to disallow its use when discovered.                    solutions with this component
                                                                                                   rating will be considered.

              2. Missing Components – No conclusions should be inferred if a specific component is not
                 listed. Instead, contact the TASC to obtain further information
              3. Component Assessments
                         i. All DBMS's should be licensed in a manner appropriate to the way they are used
                            and up-to-date with all appropriate publisher service patches.
                        ii. All multiple-user DBMS's should be placed on servers. No multiple-user DBMS
                            will be hosted on a PC.
                        iii. All multiple-user DBMS's should be under formal support and approved by the
                             IRM.
                        iv. To determine the supported versions for the various release levels, consult the
                            vendor’s web site.
              4. Components

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            5 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

                   Component                         Rating                                Comments
        Relational DB
            Oracle Standard or                       Standard        General Release Levels
            Enterprise (See Appendix I)
                                                     Declining       Extended Support Release Levels
                                                    Disallowed       Unsupported Release Levels

            DB2 Mainframe                            Standard        General Release Levels
                                                     Declining       Extended Support Release Levels
                                                    Disallowed       Unsupported Release Levels
            SQL Server (See Appendix I)              Standard        General Release Levels

                                                     Declining       Extended Support Release Levels

                                                    Disallowed       Unsupported Release Levels

            SQL Server Express                       Standard        This version of SQL Server can be appropriate for
                                                                     a smaller database where the data size is less
                                                                     than 4GB and the end users are limited to a single
                                                                     organization.
                                                     Declining       Extended Support Release Levels
                                                    Disallowed       Unsupported Release Levels
            Personal Workstation                     Standard        For use on a desktop by one user when the
            DBMSs (e.g., Microsoft                                   DR/BCP criticality classification is minimal (5) and
            Access, SQL Server Express                               the data classification is public
            LocalDB)

                                                   Disallowed        For a system with a DR/BCP criticality
                                                                     classification of limited (4) or higher.
                                                                     Or for a system with a DR/BCP criticality
                                                                     classification of minimal (5) and the data
                                                                     classification is confidential, secret, or top secret.

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            6 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

              SYBASE                                 Declining       (General or Extended Support Release Levels)
              DB2 Server                             Declining

        Open Source                                                  Please review the State Software Policy Software
                                                                     Policy for Open Source Implications
            MySQL                                    Standard        Supported versions with current patches

            PostgreSQL                               Standard        General Release Levels

            MongoDB (See Appendix I)                 Standard        General Release Levels

        Non Relational
            IMS                                     Disallowed       No New Development (General or Extended
                                                                     Support Release Levels)
            Adabas                                   Standard        General Support Release Levels
                                                     Declining       Extended Support Release Levels
            Lotus Domino                             Declining       Database server service only (Notes Storage
                                                                     Facility)

                                                                     Version 8.5 and above

              5. Lifecycle Roadmap

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            7 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            8 of 9

                                                                  DELAWARE STATE-WIDE INFORMATION
                                                     TECHNOLOGY AND ARCHITECTURE STANDARDS

VI. Development and Revision History
     Date                     Revision
     1/13/2023                Rev 0 – Initial version based on a prior standard
     5/15/2023                Rev 1 – Updated Lifecycle Roadmap
     7/18/2024                Rev 2 – Updated Lifecyle Roadmap and removed a reference to the Technology
                              Investment Council
     11/4/2024                Rev 2 - Removed a reference to the Technology Investment Council and added a
                              clarification in the Process section. In the Applicability section, updated the
                              wording to Local Education Agencies

These guidelines are adopted by the Department of Technology and Information (DTI), through the Technology and Architecture
Standards Committee (TASC), and are applicable to all Information Technology use throughout the State of Delaware. Any
questions or comments should be directed to dti_tasc@delaware.gov.
                                                            9 of 9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
