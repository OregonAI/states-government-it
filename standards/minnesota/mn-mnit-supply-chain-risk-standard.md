---
schema_version: 1
corpus: states-government-it
jurisdiction: minnesota
id: mn-mnit-supply-chain-risk-standard
title: Supply Chain Risk Management Standard
doc_type: standard
citation: MNIT Supply Chain Risk Management Standard, Issued 06/11/2026
authority_level: ''
issuing_body: Minnesota IT Services (Office of the Chief Information Officer, State of Minnesota)
source_url: https://mn.gov/mnit/assets/Supply-Chain-Risk-Management-Standard_tcm38-754632.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 025f07294010ae9c48b8f9f7016a9452c2a21ea5b35e7effe925f4bce8351378
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

# Supply Chain Risk Management Standard (MNIT Supply Chain Risk Management Standard, Issued 06/11/2026)

## At a glance

The requirements that carry out the Supply Chain Risk Management Policy for in-scope state entities and their vendors and contractors. Named in the Related Information of the seeded Supply Chain Risk Management Policy.

## Full text

Supply Chain Risk                                           Date Issued: 06/11/2026
                                                            Revised Date: 06/11/2026
Management Standard                                         Authority:    Chief Information Security Officer

Standard Statement
The Supply Chain Risk Management standard outlines the requirements necessary to achieve compliance with
the Supply Chain Risk Management Policy.

This standard is based on the National Institute of Standards and Technologies (NIST) SP 800-53, Security and
Privacy Controls, specifically the Supply Chain Risk Management Control Family.

Applicability of controls and control enhancements are applied utilizing the NIST SP 800-53B Control Baselines,
Table 3-20. Security control baselines have an applicability based on level of impact (low-impact, moderate-
impact, high-impact) derived from NIST SP800-60 Guide for Mapping of Information and Information System to
Security Categories.

The control number “SR” identified on each control or control enhancement represents the NIST control number
within the NIST SP 800-53 Supply Chain Risk Management Control Family.

Reason for the Standard
This standard is designed to address risks that can arise from vendors, contractors, and/or suppliers and ensure
that MNIT proactively manages risks that could disrupt operations or compromise data security.

Applicability
This standard applies to all departments, agencies, offices, councils, boards, commissions, and other entities in
the executive branch of Minnesota State Government. This document also applies to all vendors and contractors
providing goods and services to these State entities.

MNIT Supply Chain Risk Management Standard                                                                         1

Controls
Table 1: Supply Chain Risk Management Controls

                                                                                                Applicable Data
  Control
                Control Name                            Control Detail                            Protection
  Number
                                                                                                Categorization

                                      1. Develop a Supply Chain Risk Management (SCRM)
                                         plan for managing supply chain risks associated
                                         with acquisition, delivery, integration, operations
                                         and maintenance, and disposal of systems, system       Low
               Supply Chain              components and/or system services: Agency-
               Risk                      defined systems, system components, or systems
 SR-2                                    services.                                              Moderate
               Management
               Plan                   2. The SCRM Team must review and update the
                                         SCRM plan on an annual basis or as required, to        High
                                         address threat, organizational, and/or
                                         environmental changes.
                                      3. The SCRM plan must be protected from
                                         unauthorized disclosure and modification.

                                  Establish a Supply Chain Risk Management (SCRM) Team          Low
                                  consisting of personnel with diverse roles to lead and
               Establish SCRM     support the SCRM activities including CISO or CISO
 SR-2(1)                                                                                        Moderate
               Team               designee(s), information technology, contracting, privacy,
                                  legal, acquisition, business continuity, and other relevant
                                  functions.                                                    High

                                      1. Establish a process(es) to identify and address
                                         weaknesses or deficiencies in the supply chain
                                         element and processes of SCRM Team-defined
                                         system(s) and/or system components                     Low
                                      2. Employ controls to protect against supply chain
               Supply Chain
                                         risks to the system, system component, or system
 SR-3          Controls and                                                                     Moderate
                                         service to limit the harm or consequences from
               Processes
                                         supply chain-related events.
                                      3. Document the selected and implemented supply           High
                                         chain processes and controls within system
                                         security plans, assessments, SCRM plan, agency-
                                         defined documents.

MNIT Supply Chain Risk Management Standard                                                                        2

                                                                                           Applicable Data
  Control
              Control Name                         Control Detail                            Protection
  Number
                                                                                           Categorization

                             Employ one or more of the following controls to limit
                             harm from potential adversaries identifying and targeting
                             the organizational supply chain: agency-defined controls.

                                 1. Avoid purchase of custom or non-standardized
                                    configurations.
                                 2. Employ approved vendor lists with standing
                                    reputations in industry.
             Limitation of
 SR-3(2)                         3. Follow pre-agreed maintenance schedules update         High
             Harm
                                    and patch delivery mechanisms.
                                 4. Maintain a contingency plan in case of supply
                                    chain event.
                                 5. Utilize procurement carve-outs that provide
                                    exclusions to commitments or obligations.
                                 6. Use diverse delivery routes.
                                 7. Minimize the time between purchase decisions
                                    and delivery.
                             Ensure that the controls included in the contracts of prime
             Sub-Tier Flow
 SR-3(3)                     contractors are also included in the contracts of             High
             Down
                             subcontractors

                                                                                           Low
             Acquisition
                             Employ SCRM Team-defined acquisition strategies,
             Strategies,
 SR-5                        contract tools, and procurement methods to protect            Moderate
             Tools, and
                             against, identify, and mitigate supply chain risks.
             Methods
                                                                                           High

             Assessments
             Prior to
             Selection,      Assess the system, system component, or system service
 SR-5(2)                                                                                   High
             Acceptance,     prior to selection, acceptance, modification, or update.
             Modification,
             or Update

                             Assess and review annually the supply chain-related risks     Moderate
             Supplier
                             associated with vendors, suppliers, and/or contractors and
 SR-6        Assessments
                             the system, system component, or system service they
             and Reviews                                                                   High
                             provide.

MNIT Supply Chain Risk Management Standard                                                                   3

                                                                                           Applicable Data
  Control
              Control Name                          Control Detail                           Protection
  Number
                                                                                           Categorization

                               Employ one or more: organizational analysis, independent
                               third-party analysis, organizational testing, independent
             Testing and
 SR-6(1)                       third-party testing of supply chain elements processes,     High
             Analysis
                               and/or actors associated with the system, system
                               component, and/or system service.

                               Establish agreements and procedures with entities           Low
                               involved in the supply chain for the system, system
             Notification      component, or system service for the (one or more):
 SR-8                                                                                      Moderate
             Agreements
                                  1. Notification of supply chain compromises
                                  2. Agency-defined results of assessments or audits       High

             Tamper
                               Implement a tamper protection program for the system,
 SR-9        Resistance and                                                                High
                               system component, or system service.
             Detection

             Multiple Stages
             of System         Employ anti-tamper technologies, tools, and techniques
 SR-9(1)                                                                                   High
             Development       throughout the system development life cycle.
             Lifecycle

                                                                                           Low
                            Inspect Agency-defined systems or system components
             Inspection of
                            [Selection (one or more): at random; at an Agency-defined
 SR-10       Systems and/or                                                                Moderate
                            frequency, upon Agency-defined indications of need for
             Components
                            inspection] to detect tampering.
                                                                                           High

                                  1. Develop and implement anti-counterfeit policy
                                     and procedures that include the means to detect
                                                                                           Low
                                     and prevent counterfeit components from
                                     entering the system; and
             Component
 SR-11                            2. Report counterfeit system components to (one or       Moderate
             Authenticity
                                     more):
                                         a. SCRM team-defined external reporting
                                                                                           High
                                             agencies
                                         b. Source of counterfeit component

MNIT Supply Chain Risk Management Standard                                                                   4

                                                                                            Applicable Data
  Control
               Control Name                           Control Detail                          Protection
  Number
                                                                                            Categorization

              Anti-             Train SCRM team-defined personnel or roles to detect        Low
 SR-11(1)     Counterfeit       counterfeit system components (including hardware,
              Training          software, and firmware).                                    Moderate

                                                                                            High

                                                                                            Low
                                Maintain configuration control over the following system
              Anti-
                                components awaiting service or repair and serviced or
 SR-11(2)     Counterfeit                                                                   Moderate
                                repaired components awaiting return to service: SCRM
              Scanning
                                team-defined system components.
                                                                                            High

                                                                                            Low
                                Dispose of Agency-defined data, documentation, tools,
              Component
 SR-12                          and/or system components using SCRM defined media           Moderate
              Disposal
                                sanitization and disposal techniques and methods
                                                                                            High

Roles & Responsibilities
1. Employees, Vendors, and Contractors are responsible for:
   1.1. Reading, understanding, and applying relevant supply chain risk management policies, standards, and
        procedures.
   1.2. Ensure supply chain risk management is incorporated into vendor solicitation, project planning,
        procurement, system integration, and vendor management processes prior to submitting a requisition
        request.
   1.3. Ensure that vendors and contractors follow required supply chain risk management controls.
   1.4. Contact appropriate management personnel with questions about supply chain risk management
        policies, standards, or procedures.
2. Supervisors and Managers are responsible for:
   2.1. Ensure employees and contractors are proficient in supply chain risk management policies, standards,
        and procedures that are relevant to their roles.
   2.2. Ensuring that the standard is implemented and enforced for all third-party engagements.
   2.3. Hold employees accountable for following supply chain risk management policies and procedures.
   2.4. Ensuring that KPIs are measured, monitored, and reported to the CISO on a quarterly/annual basis.

MNIT Supply Chain Risk Management Standard                                                                     5

3. Project Managers, Product Owners, and Business Analysts are responsible for:
   3.1. Ensure all project scoping and project work complies with all MNIT policies, standards, and guidelines.
   3.2. Ensure that risk assessments are completed for all supply chain suppliers and service providers before
        procurement, focusing on cybersecurity, operational, and regulatory risks.
   3.3. Where feasible, ensure an approved list of alternate suppliers and service providers in case of failure or
        disruption from a key supplier.
   3.4. In partnership with Security personnel, conduct additional due diligence on suppliers, including
        evaluating their financial stability, security posture, and ability to meet organizational requirements.
   3.5. Communicate to procurement when a potential purchase may be in scope for supply chain risk
        management
4. Procurement Personnel are responsible for:
   4.1. Incorporate standards in procurement processes to satisfy in-scope requirements of this document.
   4.2. Work with in-scope vendors and suppliers to include MNIT template language in contract documents.
   4.3. Establish notification agreements with in-scope suppliers requiring timely disclosure of supply-chain
        incidents, breaches, or material changes affecting component integrity or provenance.
5. Information Technology Personnel are responsible for:
   5.1. Apply appropriate supply chain risk controls during the design, operation, and maintenance of systems
        and services.
   5.2. Work with third parties to ensure security controls are implemented for critical systems and
        components.
6. Information Security Personnel are responsible for:
   6.1. Ensure supply chain security requirements are aligned with supply chain risk management and
        organizational security policies.
   6.2. Monitor supply chain risks and respond to any security breaches or incidents within the supply chain.
   6.3. Coordinate supply chain notifications and determine escalation and public disclosure in coordination
        with Legal.
   6.4. Review and update supply chain risk management solicitation and contract language as needed
7. Governance, Risk, and Compliance Personnel are responsible for:
   7.1. Develop, maintain, and assess compliance with supply chain risk management requirements.
   7.2. Provide training on supply chain risk management policies, standards, and procedures.
   7.3. Assist with the interpretation and application of supply chain risk management policies.
8. State Chief Information Security Officer (CISO) and/or designee is accountable for:
   8.1. Review and approve this standard.

Related Information
National Institute for Standards and Technologies (NIST) SP800-53A, Rev 5

National Institute for Standards and Technologies (NIST) SP800-53B, Rev 5

Secure Systems Development and Acquisition Standard

Supply Chain Risk Management Policy

Threat and Vulnerability Management Standard

MNIT Supply Chain Risk Management Standard                                                                       6

Definitions
Table 2 – Definitions

         Term                                                     Definition
 Agency-defined         Agency-stated parameters.
 Supply chain           Linked set of resources and processes between and among multiple levels of
                        organizations, each of which is an acquirer, that begins with the sourcing of products and
                        services and extends through their life cycle.

History
Table 3 – Version History

    Version                                         Description                                        Date
 1.0               Initial version reviewed and approved executive leadership                     6/11/2026

Contact
grc@state.mn.us

MNIT Supply Chain Risk Management Standard                                                                           7

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
