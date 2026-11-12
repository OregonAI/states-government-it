---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-secure-development-acquisition-standard
title: Secure Systems Development and Acquisition Standard
doc_type: standard
citation: MNIT Secure Systems Development and Acquisition Standard, Version 1.9
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Secure%20Systems%20Development%20and%20Acquisition%20Standard_tcm38-323791.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: cf5ba9598ff0e09d1933c046fc48b5030437ce7cb5f22b5b318cbcaa3014de65
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
- procurement
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Secure Systems Development and Acquisition Standard (MNIT Secure Systems Development and Acquisition Standard, Version 1.9)

## At a glance

Information security controls that must be addressed throughout system development and acquisition lifecycles, including acquisition of systems from vendors.

## Full text

Secure Systems Development and Acquisition Standard
From the Office of the Chief Information Security Officer, State of Minnesota

Version:                         1.9
Effective Date:                  1/1/2016
Revised:                         8/6/2025
Approved:                        John Israel, State Chief Information Security Officer   Date: 9/19/2025

Standard Statement
Information security controls must be addressed throughout the system development and acquisition lifecycles.

Employees must abide by the terms of this standard. Employees who violate this standard may be subject to
discipline, up to and including discharge.

Table 1. Secure Systems Development and Acquisition Controls

Secure Systems Development and Acquisition Standard                                                         1

 Control    Control Name                           Control Detail                               Applicable
 Number                                                                                            Data
                                                                                                Protection
                                                                                              Categorization

           Secure Systems   Information security resources must be engaged throughout              Low
           Development      the system development lifecycle to ensure that information
           Lifecycle        security requirements are identified, resourced, and                Moderate
                            implemented. The System Development Lifecycle (SDLC) must:
                                                                                                  High
                               •   Determine information security requirements for the
                                   system or service in mission/business process
                                   planning.
                               •   Determine, document, and allocate the resources
                                   required to protect the system or service as part of its
    1                              capital planning and investment control process.
                               •   Establish a discrete line item for information security
                                   in agency programming and budgeting
                                   documentation.
                               •   Incorporate information security considerations.
                               •   Define and document information security roles and
                                   responsibilities throughout the SDLC.
                               •   Identify individuals having information security roles
                                   and responsibilities.
                               •   Integrate the agency information security risk
                                   management process into SDLC activities.

Secure Systems Development and Acquisition Standard                                                            2

 Control    Control Name                             Control Detail                            Applicable
 Number                                                                                           Data
                                                                                               Protection
                                                                                             Categorization

           Security         Information system security engineering principles must be            Low
           Engineering      applied in the specification, design, development,
           Principles       implementation, and modification of the information system.        Moderate
                            These include:
                                                                                                 High
                                •   Developing layered protections.
                                •   Establishing sound security policy, architecture, and
                                    controls as the foundation for design.
                                •   Incorporating security requirements into the system
                                    development lifecycle.
    2                           •   Delineating physical and logical security boundaries.
                                •   Ensuring that system developers are trained on how to
                                    build secure software.
                                •   Tailoring security controls to meet organizational and
                                    operational needs.
                                •   Performing threat modeling to identify use cases,
                                    threat agents, attack vectors, and attack patterns as
                                    well as compensating controls and design patterns
                                    needed to mitigate risk.
                                •   Reducing risk to acceptable levels, thus enabling
                                    informed risk management decisions.

           Enterprise       Develop an enterprise architecture with consideration for             Low
           Architecture     information security and the resulting risk to organizational
    3                       operations, organizational assets, individuals, other              Moderate
                            organizations, and the Nation.
                                                                                                 High

Secure Systems Development and Acquisition Standard                                                           3

 Control    Control Name                            Control Detail                                 Applicable
 Number                                                                                               Data
                                                                                                   Protection
                                                                                                 Categorization

           Information      Develop an information security architecture for the system              High
           Security         that:
           Architecture
                               •   Describes the overall philosophy, requirements, and
                                   approach to be taken regarding protecting the
                                   confidentiality, integrity, and availability of State data.
                               •   Describes how the information security architecture is
    4                              integrated into and supports the enterprise
                                   architecture.
                               •   Describes any information security assumptions about,
                                   and dependencies on, external services.
                               •   Is reviewed and updated (as necessary) whenever
                                   changes are made to the enterprise architecture.
                               •   Is reflected in the security plan and
                                   procurements/acquisitions.

Secure Systems Development and Acquisition Standard                                                               4

 Control    Control Name                            Control Detail                               Applicable
 Number                                                                                             Data
                                                                                                 Protection
                                                                                               Categorization

           System           For all State systems, a documented system security plan must          High
           Security Plan    be maintained that:

                               •   Is consistent with the organization’s enterprise
                                   architecture.
                               •   Outlines the business function of the system.
                               •   Outlines the data elements the system will store,
                                   process, or transmit along with each element’s data
                                   protection categorization.
                               •   Identifies the system components and boundary.
                               •   Identifies a list of specifically needed system services,
                                   ports, and network protocols.
                               •   Identifies and describes all connections with other
    5                              systems by port, protocol, service, or other similar
                                   criteria.
                               •   Provides an overview of the security requirements for
                                   the system and describes the security controls in place
                                   or planned for meeting those requirements.
                               •   Outlines non-local maintenance procedures.
                               •   Is distributed to the system owner as well as agency
                                   and security leadership.
                               •   Contains results of risk assessments.
                               •   Is reviewed and updated upon any significant changes
                                   to the system or environment.
                               •   Is protected from unauthorized disclosure or
                                   modification.

           Security Plan    System Security Plans must be reviewed and updated at least            High
           Review           annually or whenever:

                               •   There are significant changes to the
                                   system/environment of operation that affect security.
                               •   Problems are identified during plan implementation or
    6                              security control assessments.
                               •   When the Data Protection Categorization level
                                   increases.
                               •   After a serious security violation due to changes in the
                                   threat environment.
                               •   Before the previous security authorization expires.

Secure Systems Development and Acquisition Standard                                                             5

 Control    Control Name                           Control Detail                             Applicable
 Number                                                                                          Data
                                                                                              Protection
                                                                                            Categorization

           Network          A detailed network diagram must be documented and                   High
    7      Diagram          maintained that identifies all connections between the system
                            and other networks, including wireless networks.

           Dataflow         A detailed dataflow diagram must be documented and                  High
    8      Diagram          maintained that shows how data flows across the system and
                            networks.

           System           The system must be authorized prior production deployment.           Low
           Authorization    This authorization must:
                                                                                              Moderate
                               •   Be signed by the agency commissioner or board
                                   executive director or delegate at each agency using          High
                                   the system.
                               •   Include authorizations for connections with other
                                   systems.
                               •   Be updated:
                                       o At least every three (3) years.
                                       o When significant changes are made to the
    9
                                           system.
                                       o When changes in requirements result in the
                                           need to process data of a higher Data
                                           Protection Categorization.
                                       o When changes occur to authorizing legislation
                                           or federal requirements.
                                       o After the occurrence of a serious security
                                           violation which raises questions about the
                                           validity of an earlier security authorization.
                                       o Prior to expiration of a previous security
                                           authorization.

           Controlled       The system must not release information outside of the               Low
           Release          established system boundary unless:
                                                                                              Moderate
   10                          •   The receiving system provides appropriate security
                                   controls.                                                    High
                               •   The appropriateness of the information designated for
                                   release is validated.

Secure Systems Development and Acquisition Standard                                                          6

 Control    Control Name                            Control Detail                              Applicable
 Number                                                                                            Data
                                                                                                Protection
                                                                                              Categorization

           Development      All development, test and/or custom application accounts,              Low
           Credentials      user IDs and passwords must be removed from the application
   11                       or system prior to production deployment.                           Moderate

                                                                                                  High

           Separate         All development and testing must be performed in a separate         Moderate
           Development      environment from production. Network traffic into and out of
           and Production   the development and pre-production testing environment                High
   12
           Environment      must only be permitted to facilitate system testing and must
                            be restricted by source and destination access control lists as
                            well as ports and protocols.

           Developer        Where feasible, developers must not have access to                     Low
           Access to        production systems unless the access is:
           Production                                                                           Moderate
                                •   Needed to troubleshoot a production issue.
                                •   Always monitored.                                             High
                                •   Only granted for the timeframe needed to address the
   13
                                    issue.

                            Where restricting access is not feasible, sufficient controls
                            must be in place to be able to review, recreate, and (if
                            necessary) reverse the actions taken by the developer on the
                            production system.

           Production       Control moved to Secure Configuration Standard.                     Moderate
   14      Data for
           Testing                                                                                High

           Embedded         Unencrypted static authenticators must not be embedded in              Low
           Authenticators   applications or access scripts or stored on function keys.
   15                                                                                           Moderate

                                                                                                  High

           Test Data        Development and test data must be removed prior to                     Low
                            production deployment.
   16                                                                                           Moderate

                                                                                                  High

Secure Systems Development and Acquisition Standard                                                            7

 Control    Control Name                             Control Detail                             Applicable
 Number                                                                                            Data
                                                                                                Protection
                                                                                              Categorization

           Secure            Develop software applications securely by:                            Low
           Application
           Development           •   Addressing all relevant legal and regulatory               Moderate
   17                                requirements as well as State policies and standards.
                                 •   Following industry standards and/or best practices.          High
                                 •   Incorporating information security throughout the
                                     software-development life cycle

           Information       The system must check the validity of information inputs for          Low
           Input             accuracy, completeness, validity, and authenticity as close to
   18      Validation        the point of origin as possible.                                   Moderate

                                                                                                  High

           Error Handling    The system must:                                                      Low

                                 •   Generate error messages that provide information           Moderate
   19                                necessary for corrective actions without revealing
                                     information that could be exploited by adversaries.          High
                                 •   Reveal error messages only to appropriate personnel.

           Address           Address common coding vulnerabilities in line with current            Low
           Common            industry best practices such as the Open Web Application
   20      Coding            Security Project (OWASP) Top 10 in software-development            Moderate
           Vulnerabilities   processes.
                                                                                                  High

Secure Systems Development and Acquisition Standard                                                            8

 Control    Control Name                            Control Detail                             Applicable
 Number                                                                                           Data
                                                                                               Protection
                                                                                             Categorization

           Code Security    Prior to releasing new or updated applications to production,         Low
           Testing          all code must be reviewed. This review must:
                                                                                               Moderate
                                •   Follow a security assessment plan.
                                •   Include unit, integration, system, and regression            High
                                    testing/evaluation in accordance with the defined
                                    system development life cycle.
                                •   Be documented.
                                •   Be performed by individuals other than the originating
   21                               code author who are knowledgeable about code-
                                    review techniques and secure coding practices.
                                •   Ensure code is developed according to secure coding
                                    guidelines.
                                •   Identify security flaws or weaknesses in the code.
                                •   Include the use of a static and/or dynamic code
                                    analysis software.
                                •   Results must be reviewed and approved by
                                    management prior to release.

           Flaw Reporting   Users must be provided with a way to report bugs or flaws in          Low
                            the system.
   22                                                                                          Moderate

                                                                                                 High

           Code Flaw        All identified security flaws and weaknesses in the code must         Low
           Remediation      be addressed and the resolution verified prior to the
   23                       application production deployment.                                 Moderate

                                                                                                 High

           Third Party      Maintain a list of third-party vendors and contractors with           Low
           Inventory        access to State systems or data including:
                                                                                               Moderate
                                •   A description of the data and systems the third party
   24                               will have access to.                                         High
                                •   A description of the services provided by the third
                                    party.

                            Third party inventories must be updated at least annually.

Secure Systems Development and Acquisition Standard                                                           9

           Third Party      Third party vendors and contractors that store, process or         Low
           Contracts        transmit State data must have agreements and contracts in
                            place that require the third party to:                           Moderate

                               •   Enforce adequate information security controls to           High
                                   protect State data and comply with applicable laws
                                   and regulations.
                               •   Comply with required regulatory addendums.
                               •   Provide an explanation of how State data will be
                                   protected and present evidence of appropriate
                                   security controls upon request.
                               •   Provide acceptable methods for the return,
                                   destruction, or disposal of State data in possession of
                                   the third party at the end of the contract.
                               •   Ensure all storage devices where State data has
                                   resided are securely sanitized or destroyed using
                                   methods acceptable by NSA and Central Security
                                   Service (CSS) prior to their disposal or reuse.
                               •   Use State data and systems only for the purposes of
                                   the agreement.
                               •   Isolate all State Data as well as software and services
                                   that receive, process, store, or transmit State Data to
   25                              the maximum extent possible so that other service
                                   provider customers sharing physical or virtual space
                                   cannot gain access to such data or applications.
                               •   Establish service level agreements that define
                                   expectations of performance, describe measurable
                                   outcomes, and identify remedies and response
                                   requirements for any identified instance of non-
                                   compliance.
                               •   Not disclose State data to other parties.
                               •   Allow the State to periodically assess the security of
                                   the third party’s systems and processes.
                               •   Notify the State of all security incidents/breaches
                                   impacting State data or systems.
                               •   Specify licensing arrangements, code ownership and
                                   intellectual property rights related to the outsourced
                                   content.
                               •   Encrypt all State Data in transit.
                               •   Ensure all mechanisms used to encrypt data with a
                                   Data Protection Categorization of High are FIPS 140-2
                                   compliant and operate using the FIPS 140-2 compliant
                                   module.
                               •   Provide the State an escrow arrangement for all
                                   source code.

Secure Systems Development and Acquisition Standard                                                     10

 Control    Control Name                            Control Detail                               Applicable
 Number                                                                                             Data
                                                                                                 Protection
                                                                                               Categorization

                                •   Notify the State of any vendors, contractors, or other
                                    parties with access to State data and contractually
                                    bind them to protect State data.
                                •   Periodically deliver an independent report on the
                                    effectiveness of controls and timely correct relevant
                                    issues raised in the report.
                                •   Identify the location of systems that receive, process,
                                    store, or transmit State data.
                                •   Restrict the location of information systems that
                                    receive, process, store, or transmit federally regulated
                                    data to areas within the United States territories,
                                    embassies, or military installation.
                                •   Have appropriate business continuity and disaster
                                    recovery plans in place.
                                •   Protect and share audit information with the State
                                    through the contract.
                                •   Complete the State’s third-party vendor risk
                                    assessment prior to awarding of contract and annually
                                    thereafter.

           Compliance       Notice must be given to the IRS at least 45 days prior to              High
   26      Notice           engaging a third party that will have access to federal tax
                            information or systems containing federal tax information.

Secure Systems Development and Acquisition Standard                                                         11

 Control    Control Name                             Control Detail                               Applicable
 Number                                                                                              Data
                                                                                                  Protection
                                                                                                Categorization

            Secure           User and administration documentation outlining how to               Moderate
            Configuration    install, configure, operate, use, and maintain the system
            Documentation    effectively and securely must be obtained for all systems              High
                             developed by a third party. The documentation must include
                             design and implementation information for the security
                             controls to be employed and which functions, ports, protocols,
                             and services are required for organizational use. The
                             documentation must also include known vulnerabilities
    27                       regarding configuration and use of administrative (i.e.,
                             privileged) functions.

                             This documentation must be distributed to all impacted
                             personnel and protected as needed.

                             Document attempts to obtain information system, system
                             component, or information system service documentation
                             when such documentation is either unavailable or
                             nonexistent.

            Supply Chain     Vendors providing hardware or software to the State must                Low
            Security         have controls in place to prevent tampering or other malicious
    28                       activity that may impact the hardware or software’s ability to       Moderate
                             protect the confidentiality, availability, or integrity of State
                                                                                                    High
                             data.

            Commercial       Software purchased for use with State data must be tested for           Low
            Software         security flaws and weaknesses and any identified flaws and
    29      Testing          weaknesses must be addressed prior to being used for                 Moderate
                             production purposes.
                                                                                                    High

Reason for the Standard
Including security in the development process ensures systems will adequately protect State data, comply with
State information security policies and standards, and reduce costs associated with adding security after the
system has been developed.

Secure Systems Development and Acquisition Standard                                                          12

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
    •   Project Managers and Business Analysts:
            o Ensure all project work complies with all MNIT policies, standards, and guidelines.
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
This standard applies to all departments, agencies, offices, councils, boards, commissions, and other entities in
the executive branch of Minnesota State Government.

Related Information
Information Security and Risk Management Program Policy
Secure Systems Development and Acquisition Standard                                                             13

Secure Systems Development and Acquisition Policy

State Standards and Authoritative Source Cross Mapping

Glossary of Information Security Terms

History
Table 2. Version History

    Version                                        Description                                    Date

 1.0               Initial Release                                                            4/21/2015

 1.1               Added Compliance Enforcement Date                                          12/29/2015

 1.2               Updated Compliance Enforcement Date                                        12/20/2016

 1.3               Updated Compliance Enforcement Date                                        10/22/2017

 1.4               Scheduled Document Refresh                                                 3/10/2020

 1.5               Modified control for developer access to production                        11/1/2021

 1.6               Require vendor inventory for all data categories and require vendor risk   10/1/2022
                   assessment prior to contract

 1.7               Moved control related to using prod data in non-prod environment to        10/1/2023
                   Secure Configuration Standard; updated version number and revision date

 1.8               Added enforcement language; SSPs required for all data categorizations;    12/2/2024
                   updated version and revision date

 1.9               Limited scope of system security plans to only high data systems           8/6/2025

Contact
GRC@state.mn.us

Secure Systems Development and Acquisition Standard                                                        14

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
