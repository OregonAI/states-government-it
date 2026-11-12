---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-data-protection-categorization-standard
title: Data Protection Categorization Standard
doc_type: standard
citation: MNIT Data Protection Categorization Standard, Version 1.8
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Data%20Protection%20Categorization%20Standard_tcm38-323779.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: d737ad305fab620437d9d290206cea458c3d36b7b84451382ee45c8c4c4b9dab
effective_date: '2016-01-01'
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
- data
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Data Protection Categorization Standard (MNIT Data Protection Categorization Standard, Version 1.8)

## At a glance

Requires all state data to be categorized High, Moderate or Low by protection requirements; the categories drive the applicable controls in every other enterprise security standard and the AI tool standard.

## Full text

Data Protection Categorization Standard
From the Office of the Chief Information Officer, State of Minnesota

Version:                        1.8
Effective Date:                 1/1/2016
Revised:                        12/31/2024
Approved:                       John Israel, State Chief Information Security Officer   Date:   03/20/2025

Standard Statement
All State data must be categorized as either High, Moderate or Low based on its protection requirements.
Factors to be considered in assessing protection requirements include, but are not limited to, the impact to
individuals or the State if the data is improperly disclosed or modified and the value of data to attackers.
Systems, paper or electronic media and physical locations must be protected according to the highest category
of data that they store, process, or transmit. Data is owned by the agencies and each agency must identify and
categorize their data based on its protection requirements.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Data Protection Categorization Standard                                                                          1

Table 1. Data Protection Categorization Controls

 Control      Control Name                                Control Detail                               Applicable
 Number                                                                                                   Data
                                                                                                       Protection
                                                                                                     Categorization

             Data Protection     State agencies must identify, categorize, and document the               Low
             Categorization      common data elements used within the agency.
                                                                                                       Moderate
                                 All data is categorized as one of the following:
                                                                                                         High
                                     •    High: Data that is highly sensitive and/or protected by
                                          law or regulation. This includes, but is not limited to:
                                              o Protected Health Information (PHI) data as
                                                  defined in the HIPAA Regulation (45 C.F.R.,
                                                  Sec. 160.103).
                                              o Social Security Administration (SSA) Data
                                              o Criminal Justice Information (CJI) data as
                                                  defined in the FBI Criminal Justice Information
                                                  Services (CJIS) Security Policy.
                                              o Government issued ID Numbers (e.g., Social
                                                  Security Numbers, Driver’s license numbers /
                                                  State ID Card numbers, Passport Numbers)
                                              o Federal Tax Information (FTI) data as defined
     1                                            in IRS Publication 1075.
                                              o Payment Card Industry (PCI) Account Data as
                                                  defined by the Payment Card Industry Data
                                                  Security Standards (PCI DSS).
                                              o Bank account numbers excluding State-owned
                                                  bank account numbers.
                                     •    Moderate: Data that does not meet the definition of
                                          Low or High. This includes, but is not limited to:
                                              o System security information.
                                              o Not public names.
                                              o Not public addresses.
                                              o Not public phone numbers.
                                              o IP addresses.
                                              o Source code.
                                              o Any Personally Identifiable Information (PII)
                                                  not previously classified as High.
                                     •    Low: Data that is defined by Minnesota Statutes
                                          Chapter 13 as “public” and is intended to be available
                                          to the public.

Data Protection Categorization Standard                                                                               2

 Control    Control Name                              Control Detail                               Applicable
 Number                                                                                               Data
                                                                                                   Protection
                                                                                                 Categorization

           System            Systems must be categorized as follows:                                  Low
           Protection
           Categorization        •   Systems must be categorized based on the highest              Moderate
                                     categorized data the system stores, processes, or
    2                                transmits.                                                      High
                                 •   Security and authentication systems must be
                                     categorized based on the highest categorized system
                                     or data that they are protecting.

           Record            State data storage must be kept to a minimum by                         High
           Retention         implementing data retention and disposal policies, procedures
                             and processes that include at least the following:

                                 •   Handling and retaining information within systems
                                     and information output from systems in accordance
                                     with applicable federal and state laws, Executive
                                     Orders, directives, policies, regulations, standards, and
                                     operational requirements.
    3                            •   Limiting data storage amount and retention time to
                                     that which is required for legal, regulatory, and/or
                                     business requirements.
                                 •   Specific retention requirements for cardholder data
                                     and other regulated data.
                                 •   Processes for secure deletion of data when no longer
                                     needed.
                                 •   A quarterly process for identifying and securely
                                     deleting stored data with a Data Protection
                                     Categorization of High that exceeds defined retention.

           Sensitive         Payment Card Industry sensitive authentication data (full track         High
           Authentication    data, card validation code or value, and PIN data) must not be
    4      Data              stored after authorization (even if encrypted). If sensitive
                             authentication data is received, render all data unrecoverable
                             upon completion of the authorization process.

           Recordkeeping     A log of all requests for FTI, including receipt and disposal of        High
                             returns or return information must be maintained. This
    5
                             includes any medium containing FTI, such as computer tapes,
                             cartridges, CDs, or data received electronically.

Data Protection Categorization Standard                                                                           3

 Control     Control Name                                Control Detail                               Applicable
 Number                                                                                                  Data
                                                                                                      Protection
                                                                                                    Categorization

            Publicly           Processes must be in place to ensure not public information is             Low
            Accessible         not published on publicly accessible systems. Processes must
            Content            include:                                                               Moderate

                                    •   Designating individuals that are authorized to post              High
                                        information onto publicly accessible systems.
                                    •   Training authorized individuals to ensure that publicly
     6                                  accessible information does not contain nonpublic
                                        information.
                                    •   Reviewing the proposed content of information prior
                                        to posting onto publicly accessible systems to ensure
                                        that nonpublic information is not included.
                                    •   Reviewing the content on publicly accessible systems
                                        for nonpublic information bi-weekly and removes such
                                        information, if discovered.

Reason for the Standard
Categorization of data is a critical part of data management, which includes identifying and implementing
appropriate security controls to support the confidentiality, availability, and integrity of data. The categorization
determines the baseline security controls for the protection of the data. These controls are identified within the
Enterprise Information Security Standards. The protection requirements follow the data between systems,
media, and physical locations.

Roles & Responsibilities
    •   Employees, Vendors, and Contractors
           o Be aware of and follow relevant information security policies, standards, and procedures.
           o Ensure information security is incorporated into processes and procedures.
           o Ensure contract language with vendors and contractors includes required information security
                controls.
           o Consult with information security staff on the purchase and procurement of information
                technology systems or services.
           o Contact information security staff or email GRC@state.mn.us with questions about the
                information security policies, standards, or procedures.
   • Supervisors and Managers
           o Ensure employees and contractors are proficient in the information security policies, standards
                and procedures that are relevant to their role.
Data Protection Categorization Standard                                                                      4

            o  Hold employees accountable for following the information security policies, standards, and
               procedures.
    •   Information Technology Personnel
            o Apply appropriate controls to the design, operation and maintenance of systems, processes, and
               procedures in conformance with the information security policies, standards, and procedures.
    •   Information Security Personnel
            o Develop, maintain, and assess compliance with the information security policies, standards, and
               procedures.
            o Develop, maintain, and implement a comprehensive information security program.
            o Provide training on information security policies, standards, and procedures.
            o Assist agencies and personnel with understanding and implementing information security
               policies, standards, and procedures.
            o Notify appropriate personnel of applicable threats, vulnerabilities and risks to State data or
               systems.
    •   Agency Data Practices Personnel
            o Assist agencies and personnel with questions on proper data use, collection, storage,
               destruction, and disclosure.

Applicability
This standard applies to all departments, agencies, offices, councils, boards, commissions, and other entities in
the executive branch of Minnesota State Government.

Related Information
Information Security and Risk Management Program Policy

Minnesota Statutes Chapter 13

Health Insurance Portability and Accountability Act of 1996 (HIPAA)

Federal Information Security Management Act (FISMA)

Criminal Justice Information Services (CJIS) Security Policy

IRS Publication 1075

Payment Card Industry Data Security Standard (PCI DSS)

State Standards and Authoritative Source Cross Mapping

Glossary of Information Security Terms

Data Protection Categorization Standard                                                                             5

History
Table 2 - Version History

    Version                                        Description                                 Date

 1.0               Initial Release                                                         4/21/2015

 1.1               Added Compliance Enforcement Date                                       12/29/2015

 1.2               Updated Compliance Enforcement Date                                     12/20/2016

 1.3               Updated Compliance Enforcement Date                                     10/26/2017

 1.4               Scheduled Document Refresh                                              3/10/2020

 1.5               Scheduled Document Refresh                                              11/1/2021

 1.6               Grammatical updates                                                     10/1/2022

 1.7               Clarified “not public” info; version number and revision date updated   10/1/2023

 1.8               Added enforcement language; added source code and PII to Moderate;      12/2/2024
                   updated version and revision date

Contact
GRC@state.mn.us

Data Protection Categorization Standard                                                                 6

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
