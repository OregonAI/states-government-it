---
schema_version: 1
corpus: states-it-governance
jurisdiction: california
id: ca-simm-180
title: Statement of Work (SOW) Guidelines
doc_type: policy
citation: SIMM 180
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-180-SOW-Guidelines.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 44560b799312fd92a5a08150ad4babc09e1c2d9305326cbec4753c591852430a
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
- procurement
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Statement of Work (SOW) Guidelines (SIMM 180)

## At a glance

SIMM 180, Statement of Work (SOW) Guidelines: an item of the SIMM's guidelines, the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

                State of California

            Department of Technology

      Statement of Work (SOW)
            Guidelines
Statewide Information Management Manual (SIMM) – 180

                    March 2024

                                            REVISION HISTORY

                     REVISION
    REVISION                               SUMMARY OF CHANGES                  AUTHOR
                       DATE
   Release          August 2016                                             California
                                                                            Department of
                                                                            Technology
   Update           March 2024       Updated SOW Guidelines with:           California
                                       • Latest information from CDT        Department of
                                           Policy & Guidelines.             Technology
                                       • Fixed broken links.
                                       • Included Generative Artificial
                                           Intelligence (GenAI) guidance.

                                                                                                 2
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                March 2024

                                                      TABLE OF CONTENTS

   Introduction ............................................................................................................................. 4
      1.1.     Background ................................................................................................................ 4
      1.2.     Overview ..................................................................................................................... 4
      1.3.     Performance/Deliverables Based ............................................................................. 5
      1.4.     Design/Detailed .......................................................................................................... 5
      1.5.     Level of Effort/Time and Material .............................................................................. 5
      1.6.     SOW Development ..................................................................................................... 9
      1.7.     SOW Sections............................................................................................................. 9
      1.8.     SOW Guidelines ....................................................................................................... 10
   Tips for Development – Do’s and Do Not’s ......................................................................... 39
   COTS, MOTS, and Custom Hints ......................................................................................... 41
   Resources .............................................................................................................................. 42
      Attachment A – Glossary of Terms .................................................................................. 43
      Attachment B - Examples of commonly used SOW Text ............................................... 46

                                                                                                                                             3
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                                                         March 2024

   Introduction
   The Statement of Work (SOW) Guidelines (Guidelines) are designed to provide
   Agencies/State entities with assistance in developing a SOW. The Guidelines include general
   information, recommendations, and headers (sections) that are commonly used for reportable
   IT projects.

   1.1. Background
   The California Department of Technology (CDT) has adopted the Project Approval Lifecycle
   (PAL) to improve the quality, value, and likelihood of success for information technology (IT)
   projects undertaken by the State of California. As Agencies/State entities develop a SOW,
   keep in mind that the SOW must follow the Project Approval Lifecycle (PAL) process and be
   consistent with the PAL deliverables. For more information on the PAL process, refer to
   Statewide Information Management Manual (SIMM), Section 19.

   1.2. Overview
   An SOW is a formal document that captures the contractual obligations between the state and
   contractor. It defines a contractor’s work activities to be performed, deliverables to be
   completed, and the timeline adhered to in the performance of specified work for the state. The
   SOW is the most essential document in any solicitation and/or contract. The SOW includes,
   but is not limited to, traceability to the detailed solution requirements, contractor
   requirements/responsibilities, payment milestones, and standard regulatory terms and
   conditions.

   The SOW is read, interpreted, and used by both technical and non-technical personnel with
   different backgrounds. Therefore, clearly written, high quality SOWs easily understood by both
   technical and non-technical personnel will:
       •   Enable the contractor to clearly understand the requirements and needs of the state.
       •   Allow the contractor to cost out their proposal more accurately and submit higher
           quality technical proposals during the solicitation.
       •   Provide a baseline for the development of other parts of the solicitation document(s),
           particularly the evaluation criteria and proposal instructions.
       •   Minimize the need for change orders during project implementation, which can increase
           costs and delay project completion.
       •   Allow both the state and the contractor to assess performance.
       •   Help to reduce claims and disputes under the contract.

   Types of SOWs
   There are primarily three types of SOW methodologies:
       1. Performance/Deliverables Based
       2. Design/Detailed
       3. Level of Effort/Time and Material
   Depending on the level of effort for each project, the contractual obligations (i.e.,

                                                                                                    4
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                   March 2024

   requirements) will drive the procurement effort and resulting contract.
   1.3. Performance/Deliverables Based
   The Performance/Deliverables Based SOW is the best type of methodology to use for projects
   employing an Agile methodology.

   The Performance/Deliverables Based SOW allows the state entity to specify the business
   problem to be solved, deliverables required, and timeframe for completion without identifying
   the specific method or detail of its execution or implementation. A performance or
   deliverables-based SOW structures all aspects of an acquisition around the purpose of the
   work to be performed and does not dictate how the work is to be accomplished. It is written to
   ensure that bidders, and eventually contractors, are given the freedom to determine how to
   meet the state’s performance objectives and provides for payment only when the results meet
   these objectives. It maximizes the contractor control of work processes and allows for
   innovation in approaching the various work deliverables. Performance or deliverables-based
   SOWs emphasize performance that is contractually defined so the contractor’s efforts can be
   measured in terms of technical and quality achievement, schedule progress, or actual tangible
   and measurable performance.

   The goals for this type of SOW are to:
       •   Reduce contractor costs by eliminating unnecessary effort through contractor
           innovation.
       •   Enable the state to shift its emphasis from processes to measurable deliverables.
       •   Hold contractors accountable for the end results.
       •   Ensure contractors are given the freedom to determine how to meet the State’s
           performance objectives within the contract terms.

   1.4. Design/Detailed
   The Design/Detailed SOW is the most detailed of all the SOW types. It may include precise
   measurements, tolerances, materials, quality control requirements, and state requirements
   that control the processes of the contractor. There are wide variances in the use of this type of
   SOW; it is as diverse as the requirements specified in them. In this type of SOW, the state (to
   a large degree) requires the contractor to follow the state’s methods to perform tasks. This
   causes the performance risks to be borne by the state. For instance, if the contractor builds
   and/or performs a task and follows the state’s requirements exactly and the product or service
   is faulty, then the state shoulders the blame. Absent substandard workmanship and/or
   performance, the contractor cannot be faulted if they adhered to the specifications and terms
   in the SOW. While very risky on one-hand, this type of SOW affords a greater amount of
   control over the product(s) or services being delivered. This type of SOW is primarily used for
   contracts that involve commercial off-the-shelf (COTS) products or maintenance and
   operations (M&O).

   1.5. Level of Effort/Time and Material
   The real deliverable under this type of SOW is “hour(s) of work” or timeframe. These SOWs

                                                                                                    5
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                   March 2024

   are usually broad and describe the general nature, scope or complexity of the services or
   products procured over a given period. It is important to ensure that all work performed is
   specifically covered in the SOW. All activities outside of the SOW must be acquired through a
   separate procurement vehicle. This methodology is more commonly used for staff
   augmentation contracts, personnel services against a Leverage Procurement Agreement
   (LPA), or for smaller dollar amount contracts. Under this type of SOW, the state assumes
   100% liability if the product does not work as designed by the state. The state is strictly buying
   resource hours to “build” the product, as designed by the State, and under the State’s
   management.

   Table 1 below shows how these three SOW types differ from one another:
   Table 1

                             Performance/                                  Level of Effort/Time and
      SOW Type                                      Design/Detailed
                         Deliverables Based                                          Material
     Overview          Describes performance      Describes both          Describes the work to be
                       attributes to the          method and design       performed (e.g., training,
                       contractor and allows      but does not specify    consulting), means to a
                       the contractor to revise   performance.            product or material (e.g.,
                       approach to achieve the                            develop a training
                       end-product or design.                             curriculum, input data),
                                                                          and hours or timeframe to
                                                                          completion. Does not
                                                                          detail an end-product and
                                                                          allows work to proceed
                                                                          within the limits of the
                                                                          hours or timeframe
                                                                          specified.
     Scope       Deliverables describe            Technical               Skill of the contractor
                 the performance sought           requirements form the   helps frame the effort and
                 or end-product to be             parameters of the       time requirements.
                 achieved.                        design
     Requirement A statement of fact              Describes the design    Describes the means,
                 concerning the required          of the equipment or     materials, and the hours
                 deliverables from the            layout.                 or timeframe.
                 contractor.
     Objective   Attributes are specified         Must build to           Not specified as to a final
                 but method to attain is          specification or        or finished product if end
                 not defined.                     design.                 cannot be met. (However,
                                                                          there should be an end-
                                                                          product in mind.)
     Result            Able to verify and test    Able to validate “as    Allows for phasing and
                       to ensure performance      built” against          peer review on the work
                       criteria are met.          deliverable.            performed.

                                                                                                        6
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                    March 2024

   Development Considerations

   In the development of an SOW, Agencies/State entities should consider the following:
       •   A Work Breakdown Structure (WBS) (as defined in A Guide to the Project Management
           Body of Knowledge [PMBOK Guide]). A WBS may include components, such as:
                o Phases with product and project deliverables
                o Major deliverables with verifiable products, services, or results

           The WBS is useful in formulating the SOW, functional and non-functional requirements,
           and other applicable planning documents. A WBS is used to develop the contents in
           the SOW and will provide a measure to validate the work scope, project deliverables,
           and estimated cost and activity durations.

       •   The SOW should include, as applicable, a high-level description of the system, system
           subcomponents, and interfaces/integrations to systems, either existing or to be
           determined, while referencing/pointing to the detailed functional and non-functional
           requirements.

                o Cost worksheets may be used to trace the SOW requirements and deliverables.

       •   Effective April 30, 2024, and thereafter, all IT, non-IT, and Telecommunications
           solicitations, regardless of acquisition type or method, must contain the GenAI
           disclosure notification language requiring vendors to identify any GenAI technology.
               o Reference the State of California GenAI Guidelines for Public Sector
                   Procurement, Uses, and Training document for details.
               o Reference the GenAI Toolkit for details.
               o For any GenAI purchase, prior to July 1, 2024, AIO/CIO/Designee must consult
                   with the CDT GenAI intake to proceed.

       •   Effective July 1, 2024, and thereafter,
              o State entities acquiring GenAI tools must complete a SIMM 5305-F Generative
                  Artificial Intelligence Risk Assessment. The assessment is required to determine
                  whether a GenAI technology function or service is rated low, moderate, or high
                  risk.
                       All IT, non-IT, and Telecommunication procurements with GenAI
                          technology classified as moderate or high risk require consultation with
                          CDT prior to award. Those classified as low risk GenAI acquisitions do
                          not require CDT consultation.

                o Procurements with Generative Artificial Intelligence (GenAI) technologies with
                  “Moderate” or “High” risk levels identified in the Generative Artificial Intelligence
                  Risk Assessment (SIMM 5305-F) must go through the CDT consultation and
                  assessment.

                o The Generative Artificial Intelligence Risk Assessment (SIMM 5305-F) must be
                  used to classify a GenAI solution as “Low,” “Moderate,” or “High” risk based on

                                                                                                          7
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                      March 2024

                    the GenAI solution, the data underlying it, and the way each state entity aims to
                    use the technology, including who it may impact.

                           When the GenAI Risk Assessment classifies a GenAI technology as
                            “Low” risk, the state entity does not need to consult with CDT. For any
                            GenAI purchase, prior to July 1, 2024, the AIO/CIO/Designee must
                            consult with the CDT GenAI intake to proceed. State entities must work
                            with their CIOs/AIOs or designees to create policies and processes that
                            address GenAI risk. Please reference the GenAI Toolkit for further
                            guidance.
                           For “Low” risk procurements, state entities will work with their
                            CIO/AIO/Legal teams to identify any potential risks or problems with
                            GenAI so informed decisions can be made.

                o Effective July 1, 2024, and thereafter, when the GenAI Risk Assessment
                  classifies a GenAI technology as “Moderate” or “High” risk, the state entities
                  must consult with CDT. A risk assessment may be needed at multiple phases
                  throughout the procurement process and contract implementation. Review
                  Section “Required GenAI Consultation by California Department of Technology”
                  in the GenAI Toolkit. CDT will continue to develop policies specific to GenAI
                  technologies to reinforce the California GenAI Risk Management Principles and
                  provide additional guidance to CIOs and AIOs in conducting risk assessments
                  for GenAI acquisitions.

                o For additional details about the required steps for GenAI risk assessment and
                  mitigation, please see the GenAI Toolkit.

       •   A requirement is generally a documented representation of a condition or capability
           needed by a user to solve a problem or achieve an objective. A requirement can be a
           condition or capability or work product that must be met or possessed by a system or
           system component to satisfy a contract, standard, specification, or other formally
           imposed documents. Solution requirements written for inclusion in the contract should
           be:

                o   Complete to Deliverables
                o   Specific
                o   Unambiguous
                o   Testable
                o   Traceable

   For purposes of the PAL process, requirements may be expressed from various
   perspectives— from abstract stakeholder needs, to well drilled-down functional, non-
   functional, and project/contract requirements that will be captured at various stages of the
   PAL. The level of detail for each type of requirement will depend on the purpose, project type,
   and stage of the PAL. Refer to SIMM Section 170A General Requirements Guidelines and
   Section 170B Project Requirements Development Instructions for guidance on requirements

                                                                                                        8
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                     March 2024

   development for PAL.

   1.6. SOW Development
   This document provides a state entity with recommendations on areas to consider during
   SOW development. Depending on the type of SOW, some sections 1.7 will not be applicable.
   The state entity must use their knowledge of the business objectives to ensure the necessary
   sections and appropriate text, specific to the type of SOW considered are applicable to the
   SOW.

   Note: Do not incorporate terms and conditions into the SOW

   A preliminary step in developing an SOW addresses the following questions:

       •   Who needs the services?
       •   What services are needed?
       •   Why are the services needed?
       •   When are the services needed?
       •   Where will services be provided?
       •   How will the services provided be verified and validated?
       •   In some cases, “How” will the services be done?
       •   How will the services be tested and
       •   How will the services be maintained?

   1.7. SOW Sections
   The SOW list below is not all-inclusive of the sections addressed in an SOW; however, the
   following list contains the sections that need to be considered during the SOW development.
   Refer to Table 2 for details on each section, as follows:
       1. Background and Purpose
       2. Description of Proposed New System or Service
       3. Term of the Contract
       4. Contract Contacts
       5. Solution Requirements
       6. State Data Center or Contractor Hosted Facility Environment
       7. State’s Roles and Responsibilities
       8. Contractor’s Roles and Responsibilities
       9. Key Staff Qualifications and Skills
       10. Key Personnel Changes
       11. Escalation Process
       12. Change Control Procedures
       13. Project (Contractor) Tasks and Deliverable Requirements
       14. Deliverable Acceptance/Rejection Process
       15. Data Handling and Ownership
       16. Reporting
       17. Security

                                                                                                  9
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                               March 2024

       18. Disaster Recovery
       19. Delivery (Hardware and Software)
       20. Hardware and Software Needs
       21. Escrow Source Code
       22. Compatibility and Interface
       23. System Installation
       24. System Implementation or Integration
       25. Technology Refresh
       26. System Testing and Acceptance Procedures
       27. Transition of Operation to New Contractor or to State
       28. Knowledge Transfer and/or Training
       29. Maintenance and Operations (M&O)
       30. Help Desk/Call Center
       31. Insurance Requirements
       32. Warranty
       33. Service Level Agreements (SLAs)
       34. Liquidated Damages
       35. Unanticipated Tasks
       36. Budget Detail and Payment Provisions
       37. GSPD-401IT General Provisions – Information Technology
       38. Miscellaneous
       39. Glossary of Terms

   1.8. SOW Guidelines
   Regardless of the relevant sections included in a SOW, all SOWs need to follow the
   guidelines below:
       •   Establish a scope statement identifying the project objective or purpose that includes a
           description of the type of work being performed with any boundaries associated with
           performance and duties.
       •   List all tasks performed and indicate any performance requirements and all project
           requirements the contractor must comply with during contract performance.
       •   Group similar or related tasks together and organize them in a logical order.
       •   Identify resources (including state resources) necessary to complete each task,
           specifying labor, equipment, or material.
       •   Identify project deliverables required for the project completion.
       •   Identify time-sensitive milestones or deliverables.
       •   Describe quality expectations and applicable deadlines in terms of quality, quantity,
           time, and appearance. Performance deliverables must be specific, measurable,
           achievable, relevant, and time bound.
       •   Determine method to monitor, validate, and approve deliverables.
       •   Develop all SOW areas for clarity and understandability.
       •   Structure requirements so they do not lead to assumptions.
       •   Structure requirements that are accurate, clear, concise, and complete.

                                                                                                  10
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                  March 2024

   Table 2, below, provides a basis to develop the SOW content. Note: This list is not all-
   inclusive of the sections addressed in an SOW but supports an overall SOW order—general
   contract information, solution requirements, typical contractual language, and budget
   information.

   The “Section” column represents an SOW section header. The “What to Consider”
   column represents the areas that a state entity must define/develop as it relates to the
   SOW section header and the specific project.

   Table 2

          Section                             What to Consider
     1.   Background and Purpose             The following areas should be addressed:
                                              • The state entity’s core business
                                              • The business need for the project must be in
                                                sufficient detail to provide the contractor with
                                                an understanding of the business needs.
                                              • All critical partners involved (local agencies,
                                                federal government, etc.) and how these
                                                partners are the involved in the project

                                                                                                   11
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                                  March 2024

          Section                       What to Consider
     2.   Description of Proposed New   The following areas should be addressed:
          System or Service              •   Product or service to be provided.
                                         •   Project design, development, and/or
                                             integration of a new system or system
                                             upgrade
                                         •   Define whether the purchase of commercially
                                             available hardware is required.
                                         •   Define whether the state is seeking a COTS
                                             software solution.
                                         •   Define acceptable percentage level of
                                             COTS modification.
                                         •   Define if the solution will be a custom
                                             developed software.
                                         •   Define if the solution includes GenAI
                                             technologies.
                                                o Refer to SIMM 5305-F - Generative
                                                   Artificial Intelligence Risk Management
                                                   Assessment.

                                         Note: The description of the system and/or
                                         service must be clearly defined in terms that
                                         a non-technical person reading this section
                                         can understand what is being requested.
     3.   Term of the Contract          The following areas should be addressed:
                                         •   Define the term of the base contract.
                                         •   Define the term of any optional year(s)
                                             extensions.
                                         •   Define the purpose of the optional year(s)
                                             (M&O, knowledge transfer, etc.)
                                         •   Provide contract terms that are clearly
                                             defined with specific start and end dates,
                                             not open- ended
     4.   Contract Contacts             The following areas should be addressed:
                                         •   Name of the State’s and contractor’s
                                             project manager(s)
                                         •   State and contractor’s address
                                         •   State and contractor’s contact information
                                              o Phone number(s)
                                              o Email address(es)

                                                                                             12
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                            March 2024

          Section                      What to Consider
     5.   Solution Requirements        The following should be included:
                                         •   Functional requirements
                                         •   Non-Functional requirements
                                         •   Project/Transition requirements

                                        These requirements are typically included as
                                        an attachment to the SOW rather than
                                        embedding them in the body of the SOW.

                                        Refer to SIMM Section: 19C.1, 170A, and 170B for
                                        the definitions and detailed information regarding
                                        requirements.

                                        Refer to SIMM Section 19C.3 Stage 3 Solution
                                        Requirements Template tool for documenting
                                        requirements.
     6.   State Data Center or         The following areas should be addressed:
          Contractor Hosted Facility     •   Define whether the solution is to be hosted at a
          Environment                        state data center or a contractor hosted facility.
                                       Contractor Hosted:
                                         •   Define the requirements of where the data
                                             center can be housed (may preclude out-of-
                                             country)
                                         •   Define the security requirements and
                                             conditions of the data center.
                                       State Hosted:
                                         •   Define the necessary components
                                             (hardware/software) for the solution operation
                                             at the state data center. Identify:
                                              o If a physical hardware environment is
                                                  required, include:
                                                     Server quantity
                                              o If environment is a virtual environment,
                                                  include:
                                                     Processor quantity per environment
                                                     Memory requirements per
                                                        environment
                                                     Storage requirement per
                                                        environment
                                              o Licenses or licensing, per environment or
                                                  processor/core
                                              o Operating system

                                                                                              13
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                              March 2024

          Section                     What to Consider
                                          o Bandwidth requirements
                                     General Hosting:
                                      •   Define whether a help desk or hot line for
                                          questions and problems is required. Identify:
                                           o The services and tasks provided by the
                                               contractor.
                                           o Escalation process
                                           o Process for fixes
                                           o Levels of severity
                                      •   Define the outputs (reports). Identify:
                                           o Types of issues reported.
                                           o How often each output is required.
                                           o Who receives the output?
                                           o What the format (e.g., electronic) is for the
                                               output
                                      •   Define the operations schedule. Identify:
                                           o If 24-hour schedule
                                           o If business days/hours
                                           o If other
                                      •   Define the data center’s scalability to meet
                                          the state’s future needs.

                                     Note: The state entity must adhere to CDT’s Cloud
                                     Computing Policy, whenever feasible,
                                     Agencies/state entities will utilize the Cloud services
                                     provided by CDT. These service options include
                                     Platform as a Service (PaaS), and Infrastructure as
                                     a Service (IaaS).
     7.   State’s Roles and          The following areas should be addressed:
          Responsibilities            •   Define the state’s tasks, roles, and
                                          responsibilities as it relates to each area in
                                          the contract.
                                      •   Define the number of state resources,
                                          percentage of commitment and expertise, for
                                          each area in the contract, as this is used by
                                          the contractor to determine project schedule
                                          and cost for the state’s resources allocated,
                                          their expertise, and percentage of
                                          commitment

                                                                                           14
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                        What to Consider
     8.   Contractor’s Roles and         The following areas should be addressed:
          Responsibilities                •   Define the contractor’s tasks, roles, and
                                              responsibilities as it relates to each area in
                                              the contract.
                                          •   All contractor deliverables must be clearly
                                              identified and defined.
                                          •   Solicitations and contracts must include
                                              required language to identify GenAI
                                              through disclosure by the vendor/bidder
                                              as well as special provisions to protect
                                              the state, ensure that services provided
                                              to citizens of California are free of
                                              discrimination, are equitable, and of
                                              excellent quality through accuracy.
                                          •   Contractor requirements must be clear,
                                              understandable, and verifiable
     9.   Key Staff Qualifications and   The following areas should be addressed:
          Skills                          •   Define the minimum roles and responsibilities
                                              of the contractor’s key staff, as determined by
                                              the state.
                                          •   Define the minimum qualifications and skills of
                                              the contractor’s key staff.
                                          •   Define the staff qualifications and skill
                                              requirements needed to meet the project
                                              scope.
                                          •   Define if there is an anticipated timeframe or
                                              plan when key staff resources will be
                                              required (e.g., during design, development,
                                              and implementation [DD&I] and/or M&O)
                                          •   Define if multiple roles can be fulfilled by one
                                              person.

                                         Note: The staff qualifications, skills, and experience
                                         must be consistent with the requirements of the
                                         solicitation.

                                                                                               15
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                               March 2024

          Section                    What to Consider
    10. Key Personnel Changes        The following areas should be addressed:
                                      •   Define the process for “Key Personnel
                                          Changes”
                                          Define the conditions when the contractor
                                          may request staff and/or subcontractor
                                          replacements.
                                      •   Define the conditions when and process to
                                          use for the state to dismiss contractor staff.
                                      •   Define the conditions when and process to
                                          use for the state to replace contractor staff.
                                      •   Define the timeframe for contractor to
                                          replace personnel.
                                      •   Define the state’s approval process for key
                                          personnel replacements.
                                      •   Define the criteria to evaluate personnel
                                          replacements. Must use the same criteria and
                                          form used during the solicitation.
                                      •   Define how the contractor will manage their
                                          staff.
                                      •   Define the escalation and dispute
                                          procedures for key personnel changes

    11. Escalation Process           The following areas should be addressed:
                                      •   Define the state and contractor’s roles and
                                          responsibilities in the escalation process.
                                      •   Clearly define the escalation process
                                      •   All expectations must be clear and
                                          understandable.
                                      •   Describe the contract performance corrective
                                          action plan process.
                                      •   Describe the “Cure Notice” process

                                                                                           16
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
    12. Change Control Procedures    The following areas should be addressed:
                                      •   Define the process for changes. Identify and
                                          detail:
                                           o The basis for approving changes
                                           o Governance process (who does what and
                                               when)
                                                 The membership of the Change
                                                    Control Board(s)
                                           o The process, procedures, tools, forms, etc.
                                           o The protocols and levels of authority for
                                               changes (e.g., what types of changes
                                               can be approved via a contract
                                               amendment, NCB, work authorization)
                                           o Other management procedures (e.g., issue
                                               management process, configuration
                                               management) that have a role in the
                                               change control procedures.
                                           o The tools that will be used to support and
                                               manage the process
                                           o How you will communicate and promote
                                               the process and its importance to all
                                               participants
                                      •   Define the review process, which may
                                          include details, such as:
                                           o Minor changes within scope can be
                                               approved by the project manager or
                                               designee.
                                           o Changes to scope and contract
                                               amendments require the approval of
                                               the Steering Committee (or Change
                                               Control Board)

                                                                                       17
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
    13. Project (Contractor) Tasks    •   The following areas should be addressed:
        and Deliverable               •   Define the transitional requirements and
        Requirements                      deliverables (project management plan that
                                          may include a scope management plan,
                                          requirements management plan, schedule
                                          management plan, cost management plan,
                                          quality management plan, process
                                          improvement plan, human resources and
                                          staff management plan, communication
                                          management plan, risk management plan,
                                          M&O transition management plan for the
                                          transition phase, procurement management
                                          plan, training plan, etc.)
                                      •   Deliverables should be listed in the order
                                          they are due.
                                      •   Deliverables must be clearly defined and
                                          measurable.
                                      •   Due dates and milestones for each
                                          deliverable must be identified.
                                      •   Due dates for deliverables must be
                                          reasonable for both the contractor and the
                                          state.
                                      •   SOW tasks should tie to deliverables.
                                      •   Deliverables should tie to requirements.
                                      •   SOW tasks and/or deliverables should tie to
                                          cost/payment milestones in the cost
                                          worksheets.
                                      •   Define all Deliverable Expectation
                                          Documents (DED) requirements.
                                      •   For every DED, there must be a contractor
                                          requirement in the SOW which defines the
                                          minimum output/responsibility or task(s) of
                                          the contractor.
                                      •   Ensure that the state has access to all
                                          deliverable and electronic project repositories
                                          when contract is complete. The contractor
                                          should not own the vendor library
                                      •   Throughout the SOW, each responsibility
                                          and/or deliverable must clearly define:
                                      •   Who is responsible?
                                      •   What are they responsible for?
                                      •   When is it due?
                                      •   What process is to be used?
                                      •   What criteria is used to evaluate completion?

                                                                                            18
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                    What to Consider
    14. Deliverable                  The following areas should be addressed:
        Acceptance/Rejection          •  Describe how the deliverable will be sent to
        Process                          the state (e.g., format, number of copies)
                                      • Identify the state staff who will review and
                                         approve the deliverable(s)
                                      • Define the state’s process and timeframe to
                                         review, respond, accept, or reject each
                                         deliverable.
                                      • Define the process including the next steps
                                         to follow if the deliverable is rejected.
                                      • Define the process and timeframes for the
                                         contractor to respond to state’s acceptance
                                         or rejection of the deliverable(s)
                                      • Define a corrective action plan which includes
                                         a rejection process, steps to correct
                                         deficiencies, the number of review cycles
                                         before a cure notice is written, and the
                                         escalation process to resolve disputes.
                                      • Do not bind the state to unrealistic
                                         expectations
    15. Data Handling and            The following areas should be addressed:
        Ownership                     •   Define who is responsible for data
                                          conversion, data cleansing, data migration
                                          and/or data handling.
                                      •   Defined scope and timing for data
                                          conversion, data cleansing, data migration
                                          and/or data handling.
                                      •   Provide a matrix that defines current and
                                          projected capacity with respect to the data
                                          and its users.
                                      •   Define requirements for current
                                          volume/capacity and future growth for data
                                          storage.
                                      •   Define data entry requirements.
                                      •   Define the frequency of data modification or
                                          updates.
                                      •   Define whether real-time access to the data
                                          is required.
                                      •   Define the response time for:
                                           o Accessing data
                                           o Entering data
                                           o Maintaining data

                                                                                         19
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
                                      • Define types of and roles for database access
                                      • Define requirements for data access, such as:
                                          o From multiple locations
                                          o By multiple agencies
                                      • Define the security requirements for the data.
                                          o If implementing GenAI as part of this
                                              procurement, please describe how data
                                              used within the GenAI model(s) will
                                              conform to the State GenAI Policies. Refer
                                              to the State of California GenAI Guidelines
                                              for Public Sector Procurement, Uses, and
                                              Training.
                                      • Vendor is required to disclose the data sources
                                         and data governance for handling and
                                         validating the GenAI technologies.
    16. Reporting                    The following areas should be addressed:
                                      •   Define the data types and/or fields to be
                                          system generated.
                                      •   Define the requirements of the system
                                          generated report(s) and data to be provided:
                                          o Describe the standard form or format.
                                          o Who receives the report(s)
                                          o Define report due dates.
                                          o Define whether ad hoc reporting is
                                             required.
                                      •   Define any project reporting requirements.
                                          o Project status reports
                                                Frequency
                                                Content
                                          o Weekly, monthly meetings
                                          o Performance meetings and their frequency

                                                                                       20
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
   17.    Security                   The following areas should be addressed:
                                      •   Define the security issues, such as:
                                          o Preventative measures to prevent laptops
                                              from “walking-off”.
                                          o Measures to protect sensitive information.
                                      •   Define potential threats.
                                      •   Define privacy and regulatory requirements
                                          through the completion of a Privacy
                                          Threshold Assessment / Privacy Impact
                                          Analysis, SIMM 5310 – C.
                                      •   Define whether the pre-employment
                                          criminal background Investigations law
                                          applies, in accordance with Government
                                          Code Section 11546.6.
                                      •   Define whether other state entity
                                          background checks policies apply.
                                      •   Define the security risk assessment plan
                                          actions with milestones for the proposed
                                          system.
                                      •   Define all applicable security standards,
                                          which may be referenced as an attachment to
                                          the SOW. Identify and detail:
                                          o Access (public, internal state staff, external
                                              state staff, etc.) information
                                          o Type of information (personal, health, tax,
                                              financial, legal, confidential, etc.)
                                          o Protective measures (technical security,
                                              physical security, identity authorization and
                                              authentication, backup, and recovery, etc.)
                                      •   Refer to the State Administrative Manual
                                          (SAM) 5305.5, Information Asset
                                          Management, and SIMM Section 5305-A
                                          and detail the information assets:
                                          o Categorization and protection level needed
                                              (low, moderate, or high)
                                          o Owner
                                          o Custodian
                                          o Users
                                          o Information classification (public or
                                              confidential, whether it contains personal
                                              and/or sensitive data)
                                      •   List references to any applicable policies,
                                          government code, State Contracting Manual
                                          (SCM), contract code, general provisions

                                                                                          21
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                    What to Consider
                                        and/or special provisions that may be
                                        impacted by the information asset.
                                        o If implementing GenAI technologies as
                                            part of this procurement, refer to the State
                                            of California GenAI Guidelines for Public
                                            Sector Procurement, Uses, and Training
                                            and Generative Artificial Intelligence Risk
                                            Assessment (SIMM 5305-F).

                                     Note: Security requirements must be reviewed and
                                     approved by the Department of Technology
                                     California Information Security Office (CISO).
    18. Disaster Recovery            The following areas should be addressed:
                                      •   Define the timeframe when the system
                                          must be back up and operational.
                                      •   Define the location of the back-up site.
                                          o Out of state
                                          o In state
                                          o Number of miles from the primary site

                                                                                           22
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
    19. Delivery (Hardware and       The following areas should be addressed:
        Software)                     •   Define when the hardware and/or software
                                          is needed.
                                      •   Define the quantity(s) to be delivered (the
                                          purchase price/quantities should have been
                                          identified and evaluated in the solicitation
                                          process)
                                      •   Define the Free on Board (F.O.B.) point,
                                          destination for hardware.
                                      •   Define how you want the software delivered.
                                      •   Define the packing and shipping
                                          requirements for hardware and/or software.
                                      •   Define who is responsible for unpacking.
                                      •   Define who is responsible for assembling
                                          the hardware.
                                      •   Define who is responsible for the disposal of
                                          packing material.
                                      •   Define how partial shipments, back orders
                                          or staggered delivery(s) will be handled.
                                      •   Define how problems or deficiencies in
                                          delivery will be handled.

                                     Note: Refer to GSPD-401IT General Provisions,
                                     section 16 for the defined acceptance procedures
                                     for deliveries.

                                                                                          23
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
    20. Hardware and Software        The following areas should be addressed:
        Needs                        For Hardware:
                                      • Define the system hardware needed for the
                                         system (the purchase price/quantity(s)
                                         should have been identified and evaluated in
                                         the solicitation process)
                                      • Define the physical requirements for the
                                         hardware.
                                          o Space requirements
                                          o Operating conditions
                                          o Storage requirements
                                          o Cabling
                                          o Wiring
                                      • Define the system performance requirements.
                                      • Define if any hardware/software system
                                         documentation will be required.
                                      • Define all the necessary features of the
                                         hardware.
                                      • Define any existing system hardware
                                         interfaces to the new system
                                         equipment.
                                      • Define requirements for accessibility and use
                                         by handicapped users.
                                      • Ensure that the specifications trace back to
                                         the requirements.
                                      • Define the availability of replacement parts.

                                     For Software:
                                      • Define the software required.
                                      • Interface requirements
                                      • Define if software can be custom developed
                                         or COTS.
                                      • Define how software upgrades will be handled.
                                      • Define terms such as upgrades,
                                         enhancements, deficiencies, error
                                         corrections, and maintenance.
                                      • Define the licensing requirements.
                                          o Define whether the license is by machine,
                                             by site, by seat, or by agency.
                                          o Define if license is perpetual, annual,
                                             monthly, or extended use
                                          o Define the rights of licensor and licensee
                                             to use, disclose, sell, or reproduce the
                                             software.

                                                                                        24
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
                                      • Ensure licenses (including third-party) are in
                                        the state’s name and the state is not paying
                                        for transfer costs. (Costs should have been
                                        identified and evaluated in the solicitation
                                        process). Refer to GSPD-401IT #38 and
                                        other related provisions.
                                      • Define whether manuals on using the
                                        software is required.
                                        o Are the manuals standard or custom?
                                        o Define whether there is a minimum
                                            requirement for content/format.
                                        o Define the minimum number of copies
                                            required.
                                      • Define whether commercial software
                                        documentation is required.
                                      • Define programming tools (and if not
                                        used), define the availability of these
                                        tools for the state’s use.

    21. Escrow Source Code           The following areas should be addressed:
                                      •   Availability
                                          o For custom software
                                          o For commercial software
                                      •   Define who owns the source code.
                                      •   Include a deliverable requirement for the
                                          source code.
                                      •   Define how you want the source code
                                          delivered (format)
                                      •   Include “Right to sell” language.
                                      •   Define whether a copy of all the source code
                                          is required versus putting the source code in
                                          an escrow account.
                                      •   Define how the source code will be maintained
                                          as the source is updated

                                                                                         25
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                     What to Consider
    22. Compatibility and Interface   The following areas should be addressed:
                                       •  Define all interfaces.
                                       •  Define any incompatibility and interface
                                          requirements and/or concerns.
                                       • Define the current components and/or
                                          software that are already in use and must
                                          interface with the IT components and/or
                                          software of the new system.
                                       • Define the documentation requirements
                                          the contractor must provide regarding
                                          interfaces.
                                       • Determine if there is a possibility that the
                                          existing files will work with new
                                          hardware/software (and if not):
                                           o Define the format of the existing files (in
                                               hard copy or electronic)
                                           o Define who will be responsible to clean,
                                               check for errors, and stage data for new
                                               system.
                                       • Ensure timeline allocated for data
                                          conversions, data cleaning, and data
                                          verifications are achievable
   23.    System Installation         The following areas should be addressed:
                                       •   Define the installation requirements for
                                           equipment and/or software.
                                       •   Define when the contractor can inspect the
                                           installation location(s)
                                       •   Define who is responsible for developing the
                                           specifications for the installation location(s)
                                       •   Define the existing physical conditions and
                                           configuration at the installation location(s)
                                       •   Define who is responsible for modifications
                                           to the installation location to prepare the site
                                           to receive the equipment.
                                       •   Define who is responsible for the
                                           architecture and engineering associated with
                                           required modifications.
                                       •   Define who is responsible for any
                                           construction at any facilities.
                                       •   Define who is responsible for specifying
                                           cabling and wiring requirements.
                                       •   Define who is responsible for installing

                                                                                              26
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                            March 2024

          Section                    What to Consider
                                        cabling and wiring.
                                      • Define who is responsible for
                                        communications costs:
                                        o Telephone
                                        o Data lines
                                      • Define who is responsible for the
                                        installation of new equipment.
                                      • Define who is responsible for preparing the
                                        existing hardware to receive new software.
                                      • Define who is responsible for installing new
                                        software.
                                      • Define the requirement timeframes for
                                        delivery, installation, inspection and testing,
                                        and operations.
                                      • The timeframe for all the necessary system
                                        installation steps must be reasonable for
                                        both the contractor and state
                                      • Define the resources for system installation
                                        for the state and the contractor.

                                     Note: If there is a public works component, it must
                                     have been addressed in the solicitation process.
    24. System Implementation or     The following areas should be addressed:
        Integration                   •   Define the system(s) to be
                                          implemented/integrated.
                                       • Define the system(s) implementation or
                                          integration activities.
                                           o Define how the system roll out will be
                                               conducted (regions, districts,
                                               counties, etc.)
                                           o Define whether a pilot will be required
                                               and determine if it will be:
                                                  A regional pilot
                                                  By districts, county office, etc.
                                           o Define who (state or contractor) is
                                               responsible for assembling, installing,
                                               testing, implementing, and making
                                               the system operational.
                                     Include Organizational Change Management (OCM)
                                     requirements, if applicable

                                                                                           27
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                    What to Consider
    25. Technology Refresh           The following areas should be addressed:
                                      •   Define the requirements if the state requires
                                          the technology to be refreshed:
                                          o Before or after initial delivery
                                          o At same or lower cost
                                          o Define minimum refresh intervals.
                                          o Define whether costs increase will be
                                              allowed if improved functionality is
                                              provided or are they included in the
                                              proposed fixed price (must be evaluated as
                                              part of the solicitation process)
                                      •   Define the state resources for a technology
                                          refresh.
                                      •   Define who is responsible for the disposal
                                          and removal of replaced components.
                                      •   Define who is responsible for the removal of
                                          packing material of new components

    26. System Testing and            •   Define the minimum requirements for the test
        Acceptance Procedures             procedures, test plan, and test reports.
                                      •   Define the deliverables for each phase of
                                          testing.
                                      •   Define the contractor testing procedures
                                          and state acceptance criteria.
                                      •   Define the retesting procedures for failed test
                                          scripts.
                                      •   Define the exit criteria (e.g., do not go into
                                          production if high critical defects have not
                                          been fixed) for each phase (e.g., testing,
                                          production) in the project.
                                      •   Define the process for fixes.
                                      •   Define how deficiencies will be addressed,
                                          reported, and completed.
                                      •   Define terms, such as upgrades,
                                          enhancements, deficiencies, error
                                          corrections, and maintenance.
                                      •   Define exit criteria for each phase or rollout of
                                          the project.
                                      •   Define “go/no go” criteria and process for
                                          system rollout.
                                      •   Define the criteria for “final” full system
                                          acceptance.
                                      •   Define required response time for deficiencies:

                                                                                          28
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                    What to Consider
                                          o Criticality and severity levels
                                          o Contractor and the state responsibilities
                                               within the given criticality and severity
                                               level
                                          o Response time to communicate the
                                              issue(s)
                                                 To whom
                                                 Method (e.g., email, in writing)
                                      • Define the escalation process for high
                                         criticality problems and their
                                         resolution.
                                      • Define the requirements of a traceability
                                         analysis/matrix, if applicable
                                      • The timeframe to perform all necessary
                                         testing must be reasonable for the size and
                                         complexity of the system.
                                          o Allow time in schedule for any issues/fixes
                                              that may occur.
                                          o Define the resources for each phase of
                                              testing for both the state and the
                                              contractor
    27. Transition of Operation to   The following areas should be addressed:
        New Contractor or to State    •   Define the requirements for transition of
                                          system operations from the state or previous
                                          contract to the new contractor or to the
                                          state.
                                      •   Define the timeframe for the transition
                                      •   Define the state’s or previous contractor's
                                          responsibilities and tasks for transition.
                                      •   Define the new contractor's responsibilities
                                          and transition tasks.
                                      •   Describe any existing provisions in the
                                          current contract that need to be taken into
                                          consideration during the new transition of
                                          operations.
                                      •   Define who is responsible for providing a
                                          “Transition-in Plan” and “Transition-out
                                          Plan” and schedule.
                                      •   Define all roles and responsibilities for the
                                          state and the contractor for the transition of
                                          operation.
                                      •   Define the skill sets of personnel to take on
                                          operations.
                                      •   Define both the state and the contractor

                                                                                           29
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
                                         resources for the transition.
                                      • Transition timeline must be achievable for
                                         both the contractor and state
    28. Knowledge Transfer and/or    The following areas should be addressed:
        Training                      •   Define who is responsible for providing the
                                          training.
                                      •   Define the requirements for training:
                                           o Who will be trained?
                                           o When the training will occur
                                            o The methodology that will be used
                                               (classroom, web based, computer
                                               based, one-on-one, train the trainer,
                                               etc.)
                                            o The minimum/maximum number of people
                                               to be trained.
                                      •   Define the types of training required:
                                           o User training
                                           o Super user training
                                           o Administrator training
                                           o Technical/support staff training
                                      •   Ensure training is on the most recent
                                          software version for those maintaining it.
                                      •   Define the “Transfer of Knowledge”
                                          requirements along with the method on how
                                          this will be accomplished.
                                           o Who will be trained?
                                            o When the training will occur (during DD&I
                                               or during M&O)
                                            o How knowledge transfer/training
                                               effectiveness will be measured
                                      •   Define where the training will be conducted:
                                           o Local
                                           o Distant location
                                           o On-site in a state location
                                           o Contractor’s site
                                      •   Define who is responsible for providing
                                          necessary training components.
                                      •   Define the components needed to provide
                                          training:
                                           o Hardware
                                           o Software
                                           o Connectivity
                                           o Audio/visual equipment
                                      •   Define the required outputs from the training:

                                                                                           30
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
                                         o Maintenance manuals
                                         o User manual
                                         o Operator manual
                                         o Administrator manual
                                         o The minimum quantities for each output
                                         o Output format (hard copy, soft copy, etc.)
    29. Maintenance and Operations   The following areas should be addressed:
        (M&O)                         •   Define the M&O requirements for the system.
                                          o Software upgrades, patches
                                          o Define what is included (e.g., hardware
                                              and/or software)
                                          o Define when it will be performed.
                                          o Define whether it will occur during
                                              business hours or after business hours.
                                          o Define how long it will take.
                                      •   Define parameters regarding system
                                          downtime during preventive maintenance.
                                      •   Define the process as to how and when the
                                          state will be notified of scheduled
                                          maintenance.
                                      •   Define the roles and responsibilities for the
                                          state and the contractor.
                                      •   Define the Service Level Agreement’s
                                          (SLA’s) required response time from
                                          service/support call:
                                          o Define the criticality and severity levels.
                                          o SLA response time for standby or on-call
                                              maintenance periods
                                          o Define whether SLAs will vary depending
                                              on the time of day and/or day of week.
                                          o SLAs must be realistic.
                                      •   Define the contractor and the state
                                          responsibilities within the given response
                                          time(s)
                                          o Response time to communicate the
                                              issue(s)
                                                 To whom
                                                 How you want the communication
                                           o Just show up.
                                           o Fix the problem.
                                           o Other
                                      •   Define the requirements regarding any varying
                                          maintenance periods (principal periods of
                                          maintenance versus secondary) include the

                                                                                        31
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
                                         different levels of required support.
                                      • Define the different types of support that is
                                         required.
                                              o On-site
                                              o Use of remote diagnostics
                                              o Hot line support
                                      • Define the requirements or process for issue
                                         resolution.
                                      • Define who, for an in state hosted
                                         environment, is responsible for the
                                         maintenance of software and/or hardware
                                         (contractor hosting would inherently be the
                                         responsibility of the contractor)
                                      • Define how the data management
                                         practices, including data collection,
                                         storage, and quality been managed?
                                      • If implementing GenAI technologies as
                                         part of this procurement, refer to the State
                                         of California GenAI Guidelines for Public
                                         Sector Procurement, Uses, and Training
   30. Help Desk/Call Center         The following areas should be addressed:
                                      •   Define the resources intended to provide
                                          the customer or end user with information
                                          and support.
                                       • Define customers/end users.
                                       • Define who is responsible for
                                          troubleshooting problems.
                                       • Define the escalation process for high
                                          criticality problems and resolution.
                                       • Define how the contractor will provide help
                                          for desk support.
                                          o Toll-free numbers
                                          o Websites
                                          o Instant messaging or email
                                     In-house help desks designed to provide help to
                                     employees.
    31. Insurance Requirements         • Provisions of the insurance should address:
                                          o Notification within five (5) business days of
                                               any cancellation
                                          o Contractor is responsible for any
                                               deductible or self-insured retention
                                               contained within the insurance
                                               program.

                                                                                        32
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
                                        o Termination of the contract will result if
                                            contractor fails to always keep coverage
                                            in effect.
                                        o Provision that any insurance required to be
                                            carried shall be primary, and not in addition
                                            to any other insurance carried by the state.
                                      • At a minimum, the following types of insurance
                                        must be included:
                                        o Commercial General Liability
                                        o Workers’ Compensation/Employer’s
                                            Liability
                                        o Other types of insurance include
                                            Automobile Liability, Aircraft
                                            Liability, Cyber Liability, IP Liability,
                                            Pollution Liability, Professional
                                            Liability, Builder’s Risk/Installation
                                            Floater, and Fidelity Bond/Crime
                                            Insurance.

                                     Note: state entity must work with DGS, ORIM for
                                     assistance to determine appropriate types and
                                     amounts to include in the contract. These
                                     requirements must have been addressed during the
                                     solicitation process.
    32. Warranty                     The following areas should be addressed:
                                      •   Define the warranty provisions and
                                          expectations for both the state and
                                          contractor.
                                      •   Define the warranty time, such as:
                                          o When it begins and ends
                                          o If it begins after full system acceptance
                                          o If warranty period starts over if any defects
                                               are detected
                                          o If warranty period starts over based on a
                                               defined severity level
                                      •   Define the escalation process for high
                                          criticality problems and their
                                          resolution.
                                      •   If there is a phased implementation
                                          (e.g., by county, by department)
                                          ensure that all phases are covered
                                          from defects and warranty begins after
                                          full system acceptance and not after
                                          each individual phase.

                                                                                        33
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
                                      •   Define whether the state requires a warranty
                                          for free repair for defects appearing within a
                                          given time and/or for repair of defective
                                          parts.
                                      •   Define whether the state wants to include
                                          liquidated damages; if so, the process must
                                          be defined.
                                      •   Include language that the contractor
                                          warrants it has the right to sell the software.

                                     Note: See General Provisions – Information
                                     Technology (GSPD-401IT), Provision 18, Warranty,
                                     and other related provisions. If there is a warranty
                                     section within the SOW, ensure that is does not
                                     conflict with the GSPD-401IT General Provisions.
    33. Service Level Agreements     The following areas should be addressed:
        (SLAs)                        •    Each service level objective must be:
                                              o Achievable
                                              o Repeatable
                                              o Measurable
                                              o Understandable
                                              o Meaningful
                                              o Controllable
                                              o Affordable
                                      •   Ensure a standard metric is used as a basis
                                          for the performance, such as:
                                              o Abandonment Rate: Percentage of
                                                  calls abandoned while waiting to be
                                                  answered.
                                              o ASA (Average Speed to Answer):
                                                  Average time (usually in seconds) it
                                                  takes for a call to be answered by the
                                                  service desk.
                                              o TSF (Time Service Factor): Percentage
                                                  of calls answered within a definite
                                                  timeframe, e.g., 80% in 20 seconds.
                                              o FCR (First-Call Resolution):
                                                  Percentage of incoming calls that can
                                                  be resolved without the use of a
                                                  callback or without having the caller
                                                  call back the helpdesk to finish
                                                  resolving the case.
                                              o TAT (Turnaround Time): Time
                                                  taken to complete a certain task.

                                                                                            34
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                    What to Consider
                                      • Define the service level priorities and
                                        criticality levels.
                                      • Each service level objective description
                                        must have a cause for the action taken.
                                      • Define escalation procedures for SLA disputes.
                                      • In a state hosted environment with the
                                        contractor responsible for maintaining the
                                        software application but not the platform, all
                                        state and contractor roles and responsibilities
                                        must be clearly defined.

                                     Note: state entity must have their legal staff review
                                     and approve.
    34. Liquidated Damages           The following areas should be addressed:
                                      •   Provisions for liquidated damages and
                                          compensation must be clearly defined and
                                          reasonable.
                                      •   Calculation of the compensation must be
                                          clearly defined and reasonable.
                                      •   The compensation should not be
                                          disproportionate to the actual harm done to
                                          the state.
                                      •   Liquidated damages must be tied to a
                                          contractual requirement.
                                      •   Define the escalation dispute procedures for
                                          liquidated damages.

                                     Note: state entity will be required to justify how
                                     the number of liquidated damages charged was
                                     determined/derived.
    35. Unanticipated Tasks          The following areas should be addressed:
                                      •   Define the percentage allocated to
                                          unanticipated tasks.
                                           o The budget for unanticipated work shall not
                                              exceed 5% of the sum of the base contract
                                              (DD&I portion used during DD&I phase)
                                      •   Unanticipated task language (if applicable to
                                          the project) must be defined to include, at a
                                          minimum:
                                           o The definition of unanticipated task work
                                           o The state’s process for approving
                                              unanticipated tasks.

                                                                                             35
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                          March 2024

          Section                    What to Consider
                                          o As an SOW attachment, the approval
                                              document/form (e.g., Work
                                              Authorization form) that will be used to
                                              authorize each unanticipated task work
                                              item. At a minimum, the form must
                                              include the following fields:
                                                  Task summary of work to be
                                                    performed.
                                                  Schedule dates of work
                                                  Estimated labor hours.
                                                  Labor hour rates
                                                  Estimated total costs.
                                                  Contractor personnel to be assigned.
                                                  Job classification/skill level
                                                  Completion criteria and/or
                                                    deliverables
                                                  Approval signature lines for the
                                                    contractor and the state
                                     Note: Unanticipated task amounts over 5% of the
                                     base contract must be approved by Statewide
                                     Technology Procurement (STP).
   36. Budget Detail and Payment     The following areas should be addressed:
       Provisions                     • Cost worksheets should be an attachment to
                                         the SOW and referenced for payments.
                                      • Define how the contractor will get paid, such
                                         as:
                                          o By approved deliverable, useable
                                              milestone
                                                 Milestones and payments should
                                                    represent project progress, not
                                                    process execution (e.g., software in
                                                    produc33tion environment versus
                                                    writing test scripts)
                                          o Time and material
                                          o Defined intervals for on-going costs
                                              (e.g., monthly payments for M&O)
                                      • Payments should be based on performance
                                         or outcomes as opposed to paying for paper
                                         deliverables only.
                                      • Costs for M&O optional years must be
                                         clearly outlined.
                                          o M&O costs must have been
                                              evaluated during the solicitation
                                              process.
                                      • Define payment provisions for unanticipated

                                                                                       36
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

          Section                    What to Consider
                                        tasks, such as:
                                         o Hourly labor rates. Note: Hourly labor
                                             rates for unanticipated tasks must
                                             have been evaluated during the
                                             solicitation process
                                         o The state limits the budget for
                                             unanticipated tasks not to exceed 5%
                                             of the sum of the base contract (not to
                                             include the M&O portion of the
                                             contract)
                                      • Define whether the contractor is paid for travel
                                        and identify:
                                         o If travel is built into contractor’s cost
                                         o Travel and Per Diem provisions
                                      • Define payment schedule(s)
                                      • Payment(s) should be structured so that the
                                        percentage of the contract value is not heavily
                                        weighted early in the implementation of the
                                        project. This reduces the risk of the contractor
                                        walking away if the contract is not going well.
                                      • Define whether incentive/bonus provisions
                                        are included in the payment structure; if so,
                                        they must be clearly defined, measurable,
                                        and verifiable. The incentive plan must clearly
                                        define the state’s responsibilities.

                                     Note: Contract payment withholds must be utilized
                                     in accordance with Public Contract Code, Section
                                     12112, which states that the state will withhold from
                                     each invoiced payment amount to the contractor an
                                     amount equal to ten percent (10%)

                                                                                        37
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                         March 2024

          Section                    What to Consider
    37. GSPD-401IT General           The following areas should be addressed:
        Provisions – Information      •   All IT General Provisions carve outs must
        Technology                        be clear and understandable.
                                      •   Ensure that none of the SOW requirements
                                          conflict with the IT General Provisions

                                     Note: Any modifications to the General Provisions
                                     including carve outs and non-carve outs must be
                                     approved by the STP Assistant Deputy Director
                                     and the California Department of Technology
                                     Legal Division. Furthermore, any changes to the
                                     GSPDs (carve outs and non-carve outs) must be
                                     listed in the Standard Agreement (STD. 213) by
                                     the modified GSPD-401IT paragraph number
                                     (i.e., non- carve outs) and the specific SOW
                                     paragraph section (number) modified forthwith
                                     (i.e., carve- outs).

    38. Miscellaneous                The following areas should be addressed:
                                      •   Any special provisions unique the state
                                          entity (e.g., security provisions, federal
                                          terms, and conditions)
                                      •   *Bond requirements
                                      •   Confidentially forms that must be signed by
                                          contractor and subcontractor.
                                      •   GS $mart provisions, if applicable

                                     *Bond requirement(s) must have been addressed
                                     during the solicitation process. The SOW must
                                     include the requirement for delivery of the
                                     performance bond. For more information, see SCM,
                                     Volume 1, Chapter 10: IT Risk Criteria Guidelines
                                     and Financial Protection Measures - 1010
    39. Glossary of Terms            Terms/acronyms should be defined in a glossary
                                     and attached to the SOW. The glossary should
                                     encompass terms used both in the solicitation and
                                     the SOW to eliminate misinterpretations. Review
                                     SCM for existing terminology.

                                                                                         38
Statewide Technology Procurement
Statement of Work (SOW) Guidelines
SIMM 180                                                                        March 2024

Tips for Development - Do’s and Do Not’s
Table 3
       DO                                        DO NOT
  1.   Do research prior purchases that          Do not simply cut/paste together
       are similar in nature when preparing      clauses from previous procurements
       the SOW language (however,                as they could result in inconsistencies
       prepare a                                 or erroneous references to older
       unique SOW for each procurement.)         technology.

       Do include the IT General Provisions      Do not incorporate terms and
       as a separate exhibit with the            conditions into the SOW
       language, “incorporated by reference
       and made part of the Contract” on
       the STD. 213. Reference the
       appropriate web links.
  2.   Do include cost details as part of        Do not include the dollar amount in the
       a separate exhibit.                       body of the SOW. The dollar amount
                                                 will be entered on the STD. 213,
                                                 contract cover page.
  3.   Do include the IT General Provisions      Do not duplicate or include clauses that
       as a separate exhibit with the            conflict with the IT General Provisions.
       language, “incorporated by reference
       and made part of the Contract” on
       the STD. 213. Reference the
       appropriate web links.
  4.   Do include business requirements          Do not confuse the administrative
       that are defined as the “higher-level     requirements and forms (required from
       statements of the goals, objectives, or   the prospective bidders to be responsive
       needs of the state entity.”               to the solicitation) with the business
                                                 requirements that may be included in the
                                                 SOW.
  5.   Do include anything that should be        Do not duplicate language that is
       legally-binding upon the contractor       already included or is more appropriate
       in the SOW and Exhibits.                  to include in the solicitation document.
                                                 One can risk contradicting language
                                                 when it is duplicative in nature.
  6.   Do define the resource minimum            Do not fail to include the contractor’s
       qualifications (MQs) when                 key staff MQs as part of the SOW.
       preparing the solicitation for
       services. Experience MQs should
       be compatible with the skill level
       required of the project.

 California Department of Technology                                                        39
 SIMM Section 180
 Statement of Work Guidelines                                                     March 2024

 7.    Do determine the full range of the         Do not include the problem statement
       problem and include the narrative          as part of the SOW.
       details as part of the solicitation.
 8.    Do include glossary, and acronyms,         Do not incorporate a glossary in the body
       used as a separate attachment              of the SOW. The glossary should be an
       within the solicitation document.          attachment to the SOW.
 9.    Do include provisions to protect the       Do not assume the system will
       state in the event of a system             function correctly all the time.
       failure.
 10.   Do reference the prospective               Do not include references to
       contractor in the SOW as                   “vendor” or “bidder” in the SOW
       “Contractor.” The correct references       as this becomes the contract.
       to a “responder to the solicitation” are   The correct term is “Contractor.”
       as follows:
            4 IFB = bidder submits a bid
            5 RFO = offeror submits an offer
            6 RFP = proposer or bidder
                submits a proposal
       RFQ = respondent submits a quote
 11.   Do describe the work and                   Do not use ambiguous statements or
       associated requirements as fully and       words with multiple meanings, such as
       clearly as possible to assume a            “include,” “average,” “adequate,” or
       complete understanding.                    “equal,” etc.
 12.   Do describe the extent of the need,        Do not use “catch-all” phrases,
       how the extent is to be determined,        such as “to the extent
       and the maximum extent not-to-             necessary,” “as required,” or “as
       exceed.                                    applicable.”
 13.   Do use the same descriptive                Do not infer a requirement or state a
       terminology each time a part,              requirement as an adjunct to another
       component, or item is referenced.          requirement. The contractor may
                                                  overlook the inference or true
                                                  objective.
 14. Do include illustrations, diagrams,          Do not overlook the opportunity to
       tables, and charts if they assist in       include as much information as you can
       describing the work or related             to aid the contractor in understanding
       requirements.                              your business, technical, and functional
                                                  needs.
 15. Do have the SOW critiqued by                 Do not rely solely on spell check and
       others. Such reviews often uncover.        copying information provided by
       discrepancies, inconsistencies,            business, and technical teams, into your
       conflicts, or ambiguous                    SOW without a third-party review.
       descriptions.

California Department of Technology                                                       40
SIMM Section 180
Statement of Work Guidelines                                                      March 2024

COTS, MOTS, and Custom Hints
It is important to view software from a “source code rights” perspective. An easy way to
differentiate between COTS, modified off-the shelf (MOTS), and Custom is the ability to
attain the rights to the source code. For example, COTS does not allow for changes to
the source code and, therefore, does not provide any rights to the source code. MOTS
typically provides source code rights to some of the source code, generally limited to the
customized or modified code. For Custom, the state gets rights to all the source code.
When the state pays for the development of Custom code to go with the contractor
developed code, the contractor will jointly share the rights to the modified code with the
state. If the state pays for all new code, the state will generally share the rights of the
code with the contractor. It is important to note that some previously developed software
may provide source code rights (e.g., open-source applications, most federally funded
software)

Hint: When thinking of a state system or solution, think of it as a collection of software
products and components. Rarely will a solution consist of only one software
product/component. Some components are true COTS where the state gets the pre-built
application, installs it, configures it, and uses it without customization (e.g., Oracle or MS
SQL). Other products or components are pre-developed software modified to meet the
state’s needs, considered MOTS, and other components applicable to almost all software
projects are custom developed software where no existing products exist. Almost all state
projects have custom components (e.g., components used to build interfaces between
systems). Custom developed software may leverage the COTS and MOTS components,
but they consist of new source code.

A typical state project consists of all of these to some degree. The State of California’s
rights to the source code is extremely important to maintain the system in the future.
Remember…COTS = no rights, MOTS = limited rights to only the new code, and Custom
= full rights to the code.

 California Department of Technology                                                       41
 SIMM Section 180
 Statement of Work Guidelines                                                      March 2024

Resources
It is the state entity’s responsibility to comply with all established CDT policies,
procedures, and methods when soliciting proposals and developing contracts
for IT procurements.

  •   Resources for State IT Policy, Standards, Instructions and Guidelines can be
      found at: https://cdt.ca.gov/policy/
         o SAM
         o SIMM
         o Technology Letters

  •   Per the State’s Cloud Computing Policy, whenever feasible, Agencies/State
      entities will utilize the Cloud services provided by CDT. These service
      options include Platform as a Service (PaaS), and Infrastructure as a Service
      (IaaS). For this RFP, Cloud services provided by CDT are not a viable option
      due to various requirements identified in EXHIBIT A: FUNCTIONAL AND
      NON-FUNCTIONAL REQUIREMENTS. Vendors are required to host their
      proposed solution in a manner that complies with the requirements identified
      in EXHIBIT A: FUNCTIONAL AND NON-FUNCTIONAL REQUIREMENTS
      and if applicable, the Cloud Computing Services Special Provisions for
      Software as a Service (SaaS) or Cloud Computing Services Special
      Provisions of IaaS or PaaS

  •   Policies, procedures, and methods to promote sound business decision practices in
      securing necessary IT Goods and Services for the State can be found on the DGS
      website, Statewide Contracting Manual (SCM)
        o SCM, Volume 2: Information Technology Procurements

  •   Information on requirements can be found at:
         o SIMM Section 170 Requirements Guidelines Set and Instructions:
         o A. General Requirements Guidelines (PDF)
         o B. Project Requirements Development Instructions

  •   The California Department of Technology Project Management Framework and
      templates can be found at: https://capmf.cdt.ca.gov/

  •   The California Project Management Office (CA-PMO) developed the California Agile
      Framework (CA-Agile) to provide project practitioners with practical guidance for
      managing iterative incremental project delivery activities) which can be found at:
      https://projectresources.cdt.ca.gov/agile/

California Department of Technology                                                           42
SIMM Section 180
Statement of Work Guidelines                                                           March 2024

Attachment A – Glossary of Terms

Table 4: Definitions, Acronyms, and Abbreviations

      Term/Acronym                                      Definition
  State Entity               Includes every state office, officer, department, division,
                             bureau, board, and commission, including Constitutional
                             Officers. “state entity” does not include the University of
                             California, California State University, the State Compensation
                             Insurance Fund, the Legislature, or the Legislative Data Center
                             in the Legislative Counsel Bureau.
  Business                   Higher-level statement of the goals, objectives, or needs of the
  Requirement                state entity. Business requirements describe the reasons why
                             a project has been initiated, the objective that the project will
                             achieve, and the metrics that will be used to measure its
                             success. Business requirements describe the needs of the
                             state entity, not the groups or stakeholders within it.

                             For the purposes of the PAL, business requirements are the
                             Business Problem or Opportunities and Objectives table
                             identified in SIMM Section 19A.1, Stage 1 Business Analysis
                             Preparation Instructions, Section 1.10.
  Commercial off-the-        COTS product – Typically, a ready-made computer hardware
  shelf Software             or software product for specific uses and available for sale to
  (COTS)                     the public. COTS products are designed to be installed without
                             requiring custom development. For example, Microsoft Office
                             is a COTS product that is a packaged software solution for
                             businesses and individuals. The Federal Acquisition
                             Regulation (FAR) defines the rules for COTS products.
  Custom solution            Typically, computer software developed for a specific customer
                             to accommodate the customer's particular requirements,
                             preferences, and expectations.
  Functional                 Functional requirements represent the business objectives,
  Requirements               needs and outcomes of all stakeholders. They should be
                             organized and presented in context of and with a baseline
                             business process/workflow that they describe. They provide a
                             description of what an enabling solution should provide and
                             specify essential details of a solution for stakeholders to
                             express and manage expectations. They describe actions and
                             operations that the solution must be able to perform. They can
                             describe services, reactions, and behaviors of the solution.
                             They also describe information the solution will manage. The
                             requirements should be expressed in business terms and
                             should not include any technical references. The requirement
                             should identify “what” is required to meet the business
                             objective, not “how” the requirement will be implemented.
 California Department of Technology                                                        43
 SIMM Section 180
 Statement of Work Guidelines                                                       March 2024

 Modified off-the-          MOTS product – Typically, a COTS product with source code
 shelf (MOTS)               made available to the purchaser to allow for modifications. The
                            product may be customized by the purchaser, by a vendor, or
                            by another party to meet the requirements of the customer.
                            Since MOTS product specifications are written by external
                            sources, purchasers may not have control of future changes to
                            the product.
 Non-functional             Non-functional requirements provide criteria to evaluate the
 Requirements               operation of an enabling solution and primarily represent
                            qualities of (expectations and characteristics) and constraints
                            on (e.g., governmental regulations) the solution. They capture
                            conditions that do not directly relate to the behavior or
                            functionality of the solution, but rather describe environmental
                            conditions of an effective solution or productive qualities of the
                            solution. Mid-level non- functional requirements also define
                            quality of service requirements, such as those relating to
                            required capacity, speed, security, privacy, availability,
                            response time, throughput, usability, and the information
                            architecture and presentation of the user interfaces.
 Open Source                As defined in SAM Section 4819.2, “Software that includes
                            distribution terms that comply with the following criteria provided
                            by the Open Source Initiative: (The open source definition used
                            here is from the Open Source Initiative and is licensed under a
                            Creative Commons Attribution 2.5 License
                            (http://creativecommons.org/licenses/by/2.5/)
                                • Free Redistribution: The software can be given as
                                      part of a package with other applications.
                                • Source Code: The code must either be distributed
                                      with the software or easily accessible.
                                • Derived Works: The code can be altered and
                                      distributed by the new author under the same license
                                      conditions as the product on which it is based.
                                • Integrity of the author's source code: Derived works
                                      must not interfere with the original author's intent or
                                      work.
                                • No discrimination against persons or groups.
                                • No discrimination against fields of endeavor: Distributed
                                      software cannot be restricted in who can use it based
                                      on their intent.
                                • Distribution of license: The rights of the program
                                      must apply to all to whom the program is re-
                                      distributed without need for an additional license.
California Department of Technology                                                             44
SIMM Section 180
Statement of Work Guidelines                                                             March 2024

                                • License must not be specific to a product; Meaning that
                                      an operating system product cannot be restricted to be
                                      free only if used with another specific product.
                                 • License must not contaminate other software; and
                                 • License must be technology neutral.
 Project/Transition         Project/transition requirements describe capabilities that the
 Requirements               solution must have to facilitate the transition from the current
                            state of the enterprise to a desired future state. Mid-level
                            project/transition requirements are differentiated from other
                            requirement types because they are usually temporary in
                            nature and will not be needed once the transition is complete.
                            They typically cover process requirements imposed through the
                            contract, such as mandating a particular design method,
                            administrative requirements, data conversion and migration
                            from existing systems, interfaces, skill gaps that must be
                            addressed, and other related changes required to reach the
                            desired future state.
 Solution                   Describes the characteristics of a solution that will meet the
 Requirements               business requirements. Solution requirements describe
                            specific characteristics of the solution both in terms of
                            functionality and quality of service. Solution requirements are
                            sub-classified into functional requirements, non-functional
                            requirements, and project/transition requirements.
 Transition/Project         See “Project/Transition Requirements” above.
 Requirements

California Department of Technology                                                            45
SIMM Section 180
Statement of Work Guidelines                                                         March 2024

Attachment B - Examples of commonly used SOW Text

The following are paragraphs that are commonly used in a SOW. If the state entity is
modifying the following paragraphs or changing the intent of the text, STP recommends
that the state entity discuss with STP. The paragraphs below are not all-inclusive.

Unanticipated Tasks
[INSTRUCTIONS: state entity information: Unless otherwise specified, the SOW shall
define and authorize work on a Fixed Price basis, with a guarantee of task completion.
To the extent that additional work not foreseen at the time the Contract is executed and
must be accomplished, Work Authorizations, as described in the SOW, will be the means
for defining and authorizing such work on a Labor Hour basis.]

       •   If additional work must be performed which was wholly unanticipated and is
           not specified in the SOW but which in the opinion of both parties is necessary
           to the successful accomplishment of the general scope of work outlined, the
           procedures outlined in this Section will be employed.

       •   For each item of unanticipated work not specified in the SOW, a Work
           Authorization will be prepared in accordance with the sample attached as
           Exhibit X. [INSTRUCTIONS: state entity to provide and attach a sample Work
           Authorization (Exhibit X) to their SOW].

       •   It is understood and agreed by both parties to this Contract that all the terms
           and conditions of this Contract shall remain in force with the inclusion of any
           such Work Authorization. Such Work Authorization shall in no way constitute
           a Contract other than as provided pursuant to this Contract nor in any way
           amend or supersede any of the other provisions of this Contract.

       •   Each Work Authorization shall consist of a detailed statement of the purpose,
           objective, or goals to be undertaken by the contractor, the job classification(s)
           or approximate skill level(s) of the personnel to be made available by the
           contractor, an identification of all significant material to be developed by the
           contractor and delivered to the state, an identification of all significant
           materials to be delivered by the state to the contractor, an estimated time
           schedule for the provisions of these services by the contractor, completion
           criteria for the work to be performed, the name or identification of the
           contractor personnel to be assigned, the contractor's estimated work hours
           required to accomplish the purpose, objective or goals, the contractor's billing
           rates as identified in Exhibit XX per work hour, and the contractor's estimated
           total cost of the Work Authorization. [INSTRUCTIONS: state entity’s should
           have evaluated the classification rates and the defined skill level(s) during the
           solicitation process and must refer to those rates as referenced in Exhibit XX.]
       •   All Work Authorizations must be in writing prior to beginning work and
           signed by the Contractor and the State.
 California Department of Technology                                                         46
 SIMM Section 180
 Statement of Work Guidelines                                                       March 2024

       •   The State has the right to require the Contractor to stop or suspend work on
           any Work Authorization pursuant to the “Stop Work” provision of the General
           Provisions.

       •   Personnel resources will not be expended (at a cost to the State) on task
           accomplishment more than estimated work hours required unless the
           procedure below is followed:

              o If, in the performance of the work, the Contractor determines that a
                Work Authorization to be performed under this Contract cannot be
                accomplished within the estimated work hours, the Contractor will
                immediately notify the State in writing of the Contractor's estimate of the
                work hours which will be required to complete the Work Authorization in
                full. Upon receipt of such notification, the State may:

                           Authorize the Contractor to expend the estimated additional
                            work hours or service more than the original estimate
                            necessary to accomplish the Work Authorization (such an
                            authorization not unreasonably to be withheld), or
                           Terminate the Work Authorization, or
                           Alter the scope of the Work Authorization to define tasks
                            that can be accomplished within the remaining estimated
                            work hours.

              o The State will notify the Contractor in writing of its election within seven
                (7) calendar days after receipt of the Contractor's notification. If notice of
                the election is given to proceed, the Contractor may expend the
                estimated additional work hours or services. The State agrees to
                reimburse the Contractor for such additional work hours.
Amendment
The contract may be amended, consistent with the terms and conditions of the contract
and by mutual consent of both parties, subject to approval by the Statewide Technology
Procurement Division under PCC 12120. No amendment or variation of the terms of this
Agreement shall be valid unless made in writing, signed by the parties, and approved as
required. No Oral understanding not incorporated in the Agreement is binding on any of
the parties.

 California Department of Technology                                                        47
 SIMM Section 180
 Statement of Work Guidelines                                                       March 2024

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
