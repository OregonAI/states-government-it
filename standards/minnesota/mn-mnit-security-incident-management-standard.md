---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-security-incident-management-standard
title: Security Incident Management Standard
doc_type: standard
citation: MNIT Security Incident Management Standard, Version 1.8
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Security%20Incident%20Management%20Standard_tcm38-323793.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 6f52cd12ba92e03d9a1234193227088df0d2175dd99cac266006d331006279f0
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
- cybersecurity
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Security Incident Management Standard (MNIT Security Incident Management Standard, Version 1.8)

## At a glance

Requirements for detecting, reporting, handling and learning from information security incidents. Named in the Related Information of the seeded Security Monitoring and Response Policy.

## Full text

Security Incident Management Standard
From the Office of the Chief Information Officer, State of Minnesota

Version:           1.8
Effective Date:    1/1/2016
Revised:           12/31/2024
Approved:          John Israel, State Chief Information Security Officer     Date: 3/20/2025

Standard Statement
Security incident management controls must be in place to ensure the effective response and handling of
information security incidents that affect the confidentiality, integrity, or availability of data that is stored,
processed, or transmitted by the State.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Security Incident Management Standard                                                                                1

Table 1. Security Incident Management Controls

                                                                                                        Applicable
 Control         Control                                                                                   Data
                                                         Control Detail
 Number           Name                                                                                  Protection
                                                                                                      Categorization

             Security         A security incident management plan must be developed and                    Low
             Incident         maintained that defines:
             Management                                                                                 Moderate
             Plan                  •   Roles and responsibilities.
                                   •   Communication and contact strategies.                              High
                                   •   Specific security incident management procedures that:
                                           o Follow the centrally managed taxonomy for
                                                defining, validating, and classifying security
                                                incidents.
                                           o Provide notification to appropriate business
                                                owners, regulatory and/or law enforcement
                                                agencies.
                                           o Identify, reference, or include security incident
                                                management procedures from regulatory or law
                                                enforcement agencies.
     1
                                           o Address alerts from security monitoring systems,
                                                including but not limited to intrusion detection,
                                                intrusion prevention, firewalls, and file integrity
                                                monitoring systems.
                                           o Coordinate incident management activities with
                                                contingency planning activities and data backup
                                                processes.
                                   •   Analysis of legal requirements for reporting compromises.
                                   •   Coverage and responses of all critical system
                                       components.
                                   •   Metrics for measuring the security incident management
                                       capability.

                              The security incident management plan must be reviewed and
                              approved by appropriate leadership.

             Security         Distribute copies of the security incident management plan to                Low
             Incident         authorized incident management personnel, legal counsel, and
     2       Management       data practices official.                                                  Moderate
             Plan
                                                                                                          High
             Distribution

Security Incident Management Standard                                                                              2

                                                                                                Applicable
 Control      Control                                                                              Data
                                                    Control Detail
 Number        Name                                                                             Protection
                                                                                              Categorization

            Security      Review and update the security incident management plan at               Low
            Incident      least annually to address:
            Management                                                                          Moderate
            Plan Review       •   System/organizational changes.
                              •   Problems encountered during plan implementation,                High
    3
                                  execution, or testing.

                          Communicate security incident management plan changes to
                          authorized security incident management personnel, legal
                          counsel, and data practices official.

            Security      Personnel must be trained in security incident management                Low
            Incident      consistent with their assigned roles and responsibilities:
            Management                                                                          Moderate
    4       Training          •   Within 90 days of assuming a security incident
                                  management role or responsibility.                              High
                              •   When required by system changes.
                              •   At least annually.

            Security      Security incident management capabilities must be tested at least        Low
            Incident      annually. The test must:
            Management                                                                          Moderate
            Testing           •   Include tabletop exercises using scenarios that include a
                                  breach of regulated data and should test the agency’s           High
                                  incident response policies and procedures.
                              •   Include a subset of all employees and contractors with
                                  access to regulated data in tabletop exercises.
                              •   Coordinate with authorized security incident
    5                             management personnel, agencies, and third parties.
                              •   Be coordinated with organizational elements responsible
                                  for related plans.
                              •   Document results and address identified gaps.

                          Produce an after-action report to improve existing processes,
                          procedures, and policies.

                          A formal test does not need to be completed if the organization
                          actively exercises its response capability using real incidents.

Security Incident Management Standard                                                                      3

                                                                                                    Applicable
 Control      Control                                                                                  Data
                                                    Control Detail
 Number        Name                                                                                 Protection
                                                                                                  Categorization

            Incident      An incident handling capability for security incidents must be               Low
            Handling      implemented that:
                                                                                                    Moderate
                              •   Includes designated personnel to be available on a 24/7
                                  basis to respond to alerts.                                         High
                              •   Includes preparation, detection and analysis,
                                  containment, eradication, and recovery.
                              •   Coordinates incident handling activities with contingency
                                  planning activities.
                              •   Addresses unauthorized access, alteration, destruction,
                                  and disclosure of information.
                              •   Employs automated mechanisms to support the incident
                                  handling process including the availability of incident
                                  response-related information and support.
                              •   Incorporates lessons learned from ongoing incident
                                  handling activities into security incident management
    6
                                  procedures, training and testing/exercises and
                                  implements the resulting changes accordingly.
                              •   Documents relevant information related to a security
                                  incident.
                              •   Preserves evidence is through:
                                      o Technical means, including secured storage of
                                           evidence media and "write" protection of
                                           evidence media.
                                      o The use of sound forensics processes and utilities
                                           that support legal requirements.
                                      o Determining and following chain of custody for
                                           forensic evidence.
                              •   Identifies vulnerability exploited during a security incident
                              •   Ensures security safeguards to reduce risk and exploit
                                  exposure for the identified vulnerability are
                                  implemented.

            Incident      All information security incidents must be tracked and                       Low
            Monitoring    documented.
    7                                                                                               Moderate

                                                                                                      High

Security Incident Management Standard                                                                          4

                                                                                                     Applicable
 Control           Control                                                                              Data
                                                         Control Detail
 Number             Name                                                                             Protection
                                                                                                   Categorization

                 Incident       Suspected security incidents must be reported to authorized             Low
                 Reporting      security incident management personnel upon discovery.
        8                                                                                            Moderate
                                Automated mechanisms must be in place to assist in the
                                reporting of security incidents.                                        High

                 Security       Designated central incident management personnel must be                Low
                 Incident       available to respond to alerts and offer assistance for the
        9        Management     handling and reporting of security incidents.                        Moderate
                 Assistance
                                                                                                        High

                 Information    Information spillage must be addressed by:                           Moderate
                 Spillage
                 Response           •   Identifying the specific information involved in the            High
                                        improper or potentially improper information disclosure.
                                    •   Alerting authorized incident response personnel of the
                                        information spill using a method of communication not
                                        associated with the spill.
                                    •   Isolating the contaminated information system or system
    10                                  component.
                                    •   Identifying other information systems or system
                                        components on which the information may have been
                                        subsequently improperly or potentially improperly shared
                                        with or disclosed to.
                                    •   Removing and destroying the information from the
                                        contaminated information system, component, or
                                        individual not authorized to handle the information.

Reason for the Standard
The State must respond to security incidents to ensure proper handling and corrective action is taken, as well as
inform impacted parties in a timely manner in compliance with federal, state, and other applicable regulations.

Roles & Responsibilities
    •       Employees, Vendors, and Contractors
               o Be aware of and follow relevant information security policies, standards, and procedures.
               o Ensure information security is incorporated into processes and procedures.

Security Incident Management Standard                                                                           5

            o   Ensure contract language with vendors and contractors includes required information security
                controls.
            o Consult with information security staff on the purchase and procurement of information
                technology systems or services.
            o Contact information security staff or email GRC@state.mn.us with questions about the
                information security policies, standards, or procedures.
    •   Supervisors and Managers
            o Ensure employees and contractors are proficient in the information security policies, standards,
                and procedures that are relevant to their role.
            o Hold employees accountable for following the information security policies, standards, and
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
            o Notify appropriate personnel of applicable threats, vulnerabilities, and risks to State data or
                systems.
    •   Agency Data Practices Personnel
            o Assist agencies and personnel with questions on proper data use, collection, storage,
                destruction, and disclosure.

Applicability
This policy applies to all departments, agencies, offices, councils, boards, commissions, and other entities in the
executive branch of Minnesota State Government.

Related Information
Security Monitoring and Response Policy

State Standards and Authoritative Source Cross Mapping

Glossary of Information Security Terms

Security Incident Management Standard                                                                                 6

History
Table 2. Version History

    Version                                      Description                           Date

 1.0               Initial Release                                                 7/8/2015

 1.1               Added Compliance Enforcement Date                               12/29/2015

 1.2               Updated Compliance Enforcement Date and Template                12/20/2016

 1.3               Updated Compliance Enforcement Date and Template                10/26/2017

 1.4               Scheduled Document Refresh                                      3/10/2020

 1.5               Scheduled Document Refresh                                      11/1/2021

 1.6               Scheduled document refresh                                      10/1/2022

 1.7               Updated version number and revision date                        10/1/2023

 1.8               Added enforcement language; updated version and revision date   12/2/2024

Contact
GRC@state.mn.us

Security Incident Management Standard                                                           7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
