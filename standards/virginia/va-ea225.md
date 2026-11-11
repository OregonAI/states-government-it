---
schema_version: 1
corpus: states-government-it
jurisdiction: virginia
id: va-ea225
title: Enterprise Architecture Standard (EA225)
doc_type: standard
citation: EA Standard EA225
authority_level: ''
issuing_body: Virginia Information Technologies Agency (VITA)
source_url: https://www.vita.virginia.gov/media/vitavirginiagov/it-governance/ea/pdf/EA225.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 1f3eed12d239f88fac01f36c2dfabe0748e65307222d9db2868a197cf540e3d7
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
- governance
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Enterprise Architecture Standard (EA225) (EA Standard EA225)

## At a glance

Item of the VITA library, topic 'Enterprise Architecture': the mandatory technical direction and requirement statements agencies follow when planning, acquiring, developing or modifying IT solutions; the umbrella of the EA requirements documents also seeded here.

## Full text

COMMONWEALTH OF VIRGINIA
Enterprise Architecture (EA)
Information Technology
Resource Management (ITRM)

              Enterprise
              architecture
              standard

                       EA Standard (EA225)
                                 May 2024

Enterprise Architecture Standard                                                        EA Standard (EA225)
                                                                                        May __ 2024

                                                    Preface
Publication Designation
Enterprise Architecture Standard (EA225)                         General Responsibilities

Subject                                                          Chief Information Officer of the
Enterprise Architecture                                          Commonwealth (CIO)
                                                                 Agency head of VITA. Responsible for and
Effective Date                                                   approves statewide technical and data policies,
Completion of guidance document process, expected                standards, guidelines, and requirements for
to be July 2024                                                  information technology, including with respect to
                                                                 information technology planning, procurement, and
Supersedes                                                       security
Past versions (see above table)
                                                                 Virginia Information Technologies Agency
Scheduled VITA Review                                            (VITA)
Periodically or as needed                                        At the direction of the CIO, VITA leads efforts that
                                                                 draft, review, and update technical and data
Authority                                                        policies, standards, guidelines, and requirements
                                                                 for information technology.
Code of Virginia, §2.2-2006
(Definitions)                                                    VITA uses requirements in IT technical and data
                                                                 related documents when establishing contracts;
Code of Virginia, §2.2-2007                                      reviewing procurement project, and security and
(Powers of the CIO)                                              budget requests and strategic plans, and when
                                                                 developing and managing IT enterprise and
Code of Virginia, §2.2-2007.1                                    infrastructure services
(Additional duties of the CIO relating to information
technology planning and budgeting)                               Executive Branch Agencies
                                                                 Provide input and review during the formulation,
Code of Virginia, § 2.2-2009                                     adoption and update of statewide technical and
(Additional duties of the CIO relating to security of            data policies, standards and guidelines for
government information)                                          information technology.

Code of Virginia, § 2.2-2012                                     Comply with the requirements established by
(Additional powers and duties related to the                     COV policies and standards. Apply for
procurement of information technology)                           exceptions to requirements when necessary.

Code of Virginia, §2.2-603(F)                                    Related ITRM Policies, Standards, and
(Authority of agency directors, with respect to IT and           Guidelines
data security and risk management)                               Enterprise Architecture Policy (EA200)

Scope
This standard is applicable to all Executive Branch
state agencies and institutions of higher education
(hereinafter collectively referred to as "agencies") that
are responsible for the management, development,
purchase, and use of information technology
resources in the Commonwealth of Virginia. This
standard does not apply to research projects,
research initiatives or instructional programs at public
institutions of higher education.

Purpose
This standard establishes the framework for
enterprise architecture direction and technical
requirements, which govern the acquisition, use and
management of information technology resources by
executive branch agencies.
                                                            ii

Enterprise Architecture Standard                                                             EA Standard (EA225)
                                                                                             May __ 2024

Reviews

Updates to this publication and opportunities for review occur through the regulatory process for guidance
documents.

Publication Version Control

Please direct questions related to this publication to VITA’s Enterprise Architecture Division (EA) at
ea@vita.virginia.gov. VITA notifies the Agency Information Technology Resources (AITRs) and other
interested parties of revisions to this document.

The following table contains a history of the revisions to this publication.
   Version        Date      Revision Description
   225-15.2       10/31/2019       Last copy of webpage version

   225-15.3        5/21/2024       Administrative revision, focused on reformatting the document to delineate the
                                   guidance document framework from the individual technical publications.

   225-15.4       5/20/2025        Links updated due to updated VITA website. No content updates.

                                                             iii

 Enterprise Architecture Standard                                                                                       EA Standard (EA225)
                                                                                                                        May __ 2024

                                                        Table of Contents

Preface ............................................................................................................. 2
     Reviews ..................................................................................................................................................... 3
     Publication Version Control ..................................................................................................................... 3

Table of Contents ............................................................................................. 4

Introduction ...................................................................................................... 5
    Background ...................................................................................................................................................5
    Acronyms ......................................................................................................................................................5
    Glossary ........................................................................................................................................................5

Enterprise Architecture Standard ...................................................................... 6
    Enterprise Architecture Components and Requirements ...............................................................................6
     Standard Inputs ........................................................................................................................................ 6
     Definition of Key Terms............................................................................................................................ 6
     Agency Exception Requests .................................................................................................................... 6
    Enterprise Business Architecture – EBA .......................................................................................................7
    Enterprise Information Architecture – EIA .....................................................................................................7
    Enterprise Solutions Architecture – ESA .......................................................................................................8
    Enterprise Technical Architecture – ETA.......................................................................................................9

                                                                             iv

Enterprise Architecture Standard                                               EA Standard (EA225)
                                                                               May __ 2024

Introduction

Background
The Commonwealth’s Enterprise Architecture is a strategic asset used to manage and align the
Commonwealth’s business processes and Information Technology (IT) infrastructure/solutions with the
state’s overall strategy.

The Enterprise Architecture is also a comprehensive framework and repository which defines:
   • models that specify the current (“as-is”) and target (“to-be”) architecture environments;
   • information necessary to perform the Commonwealth’s mission;
   • technologies necessary to perform that mission; and
   • processes necessary for implementing new technologies in response to the Commonwealth’s
       changing business needs.

Acronyms

AITR:               Agency Information Technology Resource

CIO:                Chief Information Officer of the Commonwealth

EA:                 Enterprise Architecture

IT:                 Information Technology

ITRM:               Information Technology Resource Management

ORCA:               Online Review and Comment Application

PSG:                Policy, Standard and Guideline

VITA                Virginia Information Technologies Agency

Glossary
As appropriate, terms and definitions used in this document can be found in the COV ITRM IT Glossary,
at https://www.vita.virginia.gov/it-governance/glossary/

                                                         5

 Enterprise Architecture Standard                                                  EA Standard (EA225)
                                                                                   May __ 2024

 Enterprise Architecture Standard
 Enterprise Architecture Components and Requirements
 The Enterprise Architecture contains four components as shown in the model in Figure 1.

                                    Figure 1 – COV Enterprise Architecture Model

The Business Architecture drives the Information Architecture which prescribes the Solutions Architecture
that is supported by the Technical (technology) Architecture.

 Standard Inputs
The requirements and technology component standard tables contained in this standard have been
consolidated from inputs from EA workgroups, Customer Account Managers (CAMs), Agency Information
Technology Resources (AITRs), the Architecture & Innovation Governance Forum (AIGF) and the Platform
Service Delivery Forum (PSDF) when researching, providing recommendations, and developing the
Commonwealth’s Enterprise Architecture.

 Definition of Key Terms
This standard presents two forms of architecture direction for agencies when planning or making changes or
additions to their information technology:
    •    Requirement Statements – This standard’s requirement statements present mandatory Enterprise
         Architecture direction for agencies when planning or making changes or additions to their
         information technology.
    •    Technology Roadmaps – Roadmaps indicate what technology or products agencies may acquire at
         a particular point in time, when acquiring a new or replacing an existing technology or product.

 Agency Exception Requests
The requirements included within this document are mandatory. Agencies that want to deviate from the EA
requirements and/or technology standards may request an exception using the Enterprise Architecture
                                                           6

 Enterprise Architecture Standard                                                    EA Standard (EA225)
                                                                                     May __ 2024

Change/Exception Request Form in VITA's Archer application. All exceptions must be approved prior to the
agency pursuing procurements, deployments, or development activities related to technologies that are not
compliant with this standard.

 Enterprise Business Architecture – EBA
 The EBA documents the business strategy, governance, organization and business functions of state
 government, and identifies which organizations perform those functions. The EBA provides a look at the
 big picture of state government from a business perspective to define who we are, what we do and
 where we want to go.

 The Enterprise Business Model (EBM) of the EBA was developed to define the “what we do” in terms of
 business functions independent of the organizations that perform those functions. That model was
 developed from the Federal Enterprise Architecture’s Business Reference Model and was validated
 through workshops of agency business leaders. These workshops mapped individual agency business
 functions to the EBM, thus creating the Commonwealth’s "as-is" business architecture for Executive
 Branch agencies.

 For additional information, readers can use the EBA application or consult published EBA reports on the
 COV EA225 website at:

         https://www.vita.virginia.gov/policy--governance/enterprise-architecture/

 Enterprise Information Architecture – EIA
 Government and government services are normally information driven. Government organizations
 constantly and dynamically gather and process data to create information needed to support their
 missions, whether it is disaster recovery, environmental protection, citizen security or other direct
 services. The EIA provides the framework/model and methodology that will enhance each agency’s
 ability to quickly discover, access and understand data and create the information needed to make
 critical decisions and support agency business functions.

 The EIA is designed to provide a common framework for the cost effective sharing of government
 information across organizational lines while respecting the security, privacy and appropriate use of that
 information. It enables agency leaders to manage information as a Commonwealth asset to better serve
 the citizens of Virginia. It increases the Commonwealth’s agility in drawing out the value of information
 as a strategic mission asset.

 EIA reports and publications may be found on the COV EA225 website at:

         https://www.vita.virginia.gov/policy--governance/enterprise-architecture/

                                                        7

 Enterprise Architecture Standard                                                   EA Standard (EA225)
                                                                                    May __ 2024

 Enterprise Solutions Architecture – ESA
 The expectations of government to deliver more services, to deliver them better and more cheaply
 presents a challenge for the Commonwealth. Well-engineered automated solutions [1] can increase
 productivity in service delivery to help meet these expectations.

 Commonwealth agencies make significant investments in these automated solutions in order to carry
 out the business of Virginia government. [2] The ESA provides the framework/model and methodology
 that supports the transition from silo-based, application-centric and agency-centric information
 technology investments to an enterprise approach where solutions are designed to be flexible. This
 allows agencies to take advantage of shared and reusable components, facilitates the sharing and reuse
 of data where appropriate and makes the best use of the technology infrastructure that is available.

 The ESA needs to contain a unified view of solutions to achieve this increase in reuse and the reduction
 of solution complexity. To support this, the framework/model and methodology includes inventories,
 governance/guidance, and the relationships between agency applications and the other EA component
 architectures.

                                    Figure 2 – COV ESA: Unified View of Solutions

The unified view of solutions includes the Business (EBA), Information (EIA) and Technology (ETA)
perspectives. This view also shows how agency solutions/applications connect to:
    •    The business of the Commonwealth - by sub-lines of business
    •    Data Exchanges
    •    Infrastructure Services - by Software Tools (Operating Systems, Languages, etc.)

                                                            8

Enterprise Architecture Standard                                                    EA Standard (EA225)
                                                                                    May __ 2024

ESA reports and publications may be found on the COV EA225 website at:

        https://www.vita.virginia.gov/policy--governance/enterprise-architecture/

Enterprise Technical Architecture – ETA
The ETA guides the development and support of an organization’s information systems and technology
infrastructure.

ETA reports and publications may be found on the COV EA225 website at:

        https://www.vita.virginia.gov/policy--governance/enterprise-architecture/

                                                       9

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
