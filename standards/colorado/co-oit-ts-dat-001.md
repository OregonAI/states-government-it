---
schema_version: 1
corpus: states-it-governance
jurisdiction: colorado
id: co-oit-ts-dat-001
title: Enterprise Data Access and Integration Services
doc_type: standard
citation: TS-DAT-001
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=1rbR9iUkk4Rmf82revz3i4zlkybjbEfci
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 8e2527cd23c12dbe492db927df2655eb28fc26f29246017ad8f3e06dd68366dc
effective_date: '2019-12-02'
source_version: 4.0, last updated 06/23/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-DAT-001: Enterprise Data Access and Integration Services'', links this file
  as https://drive.google.com/file/d/1rbR9iUkk4Rmf82revz3i4zlkybjbEfci/view?usp=sharing; the text was
  fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=1rbR9iUkk4Rmf82revz3i4zlkybjbEfci
  (the source URL above).'
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Enterprise Data Access and Integration Services (TS-DAT-001)

## At a glance

OIT technical standard TS-DAT-001 (Data and Databases): Enterprise Data Access and Integration Services. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-DAT-001: Enterprise Data Access and
Integration Services
  Document ID                     TS-DAT-001
  Title                           Enterprise Data Access and Integration Services
  Executive Sponsor               Chief Data Officer
  Issuing Authority               Governor’s Office of Information Technology (OIT)
  Applies to                      OIT and OIT-supported agencies, including employees of OIT,
                                  agencies supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Instrument Type                 Standard
  Version                         4.0
  Effective Date                  12/02/2019
  Last Updated                    06/23/2026

1. Purpose
OIT is statutorily obligated to provide IT support and services to the State and its stakeholders
in the most effective and efficient manner possible (as defined by C.R.S. 24-37.5). To satisfy
stakeholder needs surrounding application integration for the enterprise, this document is
submitted as the standard for providing Enterprise Data Access and Integration Services.
This document communicates the standards OIT has developed with the intent of providing
enterprise standard configurations for communication between heterogeneous systems within
the enterprise, primarily for data exchange and service governance, based on a best-of-value
decision assessment involving stakeholder needs, hardware configurations, and operational
and security best practices.
The ultimate purpose of this standard is to describe the minimum requirements for designing,
installing, securing, monitoring, maintaining, protecting, and decommissioning the application
integration and data access services for the enterprise.

2. Scope
These standards apply to OIT and OIT-supported agencies. This standard shall be used by
employees of OIT, agencies supported by OIT, and vendors contracted by OIT or its
stakeholders, as a means to enforce technology standardization and assist in making the
usage, support, and/or purchase of technologies more consistent and efficient.

                                                                                     Page 1 of 5

This standard supports OIT's intentions for a unified data management strategy and applies to
any technical requirements for providing application access to data, data integration,
message brokers, or other means of access and interaction with solution data stores. It
establishes enterprise-wide expectations for conformance to OIT's technical specifications and
support for its established API-centric and Enterprise Service Bus (ESB) platforms.

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.

Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews/approves the Standard (this document).

Chief Data Officer
    ● Owner of Standard.
    ● Engages stakeholders and subject matter experts to determine the standard.
    ● Updates document standards and version number.
    ● Presents to the Architecture Review Board for approval and adoption.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and
its purposes of authority and governance in support of OIT's statutorily mandated mission in
service of Colorado State Government affairs.

4. Standards
Authority
All data integration requirements and skills are under the authority and collaboration of the
OIT Data Integration Services Team and the Chief Data Officer (CDO).
   ●   The skills, roles, and technology required for the deployment and support of any data
       access, data integration, API, ESB, or application message brokers, are subject to
       review and approval by the OIT Data Integration Services Team and the CDO.
   ●   Any data integration or access requirements should subscribe to an API-centric
       approach; development of API connectivity is the primary objective of any data access
       or integration requirement.

Preference and Priority of an API-centric Approach
   ●   The State's Strategy for Data Integration and Sharing is API-led connectivity.
   ●   The OIT MuleSoft platform shall be used for the Integrated Development Environment
       and full API lifecycle management.
   ●   Support for RESTful API frameworks shall be the primary architectural pattern (no
       SOAP); the RAML specification shall be used to provide an API definition.
   ●   All Enterprise API Endpoints shall be managed by and integrated into OIT's MuleSoft
       Anypoint Management Platform, which governs API access through established OIT
       Enterprise Identity and Access Management processes.
                                                                                     Page 2 of 5

   ●   All Enterprise APIs will be published to the Colorado MuleSoft Anypoint Exchange to
       make API resources discoverable and reusable.
   ●   OIT standards for metadata and governance of APIs will be adhered to.
   ●   All API developers (vendors, contractors, employees) must review existing API assets in
       the Colorado MuleSoft Anypoint Exchange before developing new APIs.
   ●   API design will be reviewed by OIT's Enterprise Integrations personnel before
       development begins.
   ●   APIs will follow OIT's secure system development practices and enterprise CI/CD
       processes and platforms.

Generalized Properties of an API, Enterprise Service Bus, or Message Broker
Services relating to the use of an API, ESB, or Message Broker are referred to generally as the
application or data Integration Layer, which must provide:
   ●   Adaptation: Configuration of service requestors and providers within an environment
       of change, including where a service varies from its definition, semantically or non-
       semantically.
   ●   Auditing: The ability to audit messaging between service requesters and providers,
       including translation, transformation, or orchestration, and the addresses of the
       communicators.
   ●   Authorization / Identity Management: Authorization and/or access control
       independent of either requestor or provider.
   ●   Compensation: The ability to adapt to error conditions, maintaining integrity and
       providing for unaffected services.
   ●   Composition: The ability to mediate a set of messaging requests to smaller services
       that semantically provide for the scope of the request in aggregate.
   ●   Logging: The ability to log interactions at the message level.
   ●   Protocol Switching: Facilitating messaging between providers and requesters using
       different protocols and interaction patterns.
   ●   Rules: Allowing for both mediation flows and integrations that are rules-based.
   ●   Transformation: Altering messages semantically so an intended rule-driven or other
       interaction layer-defined configuration can be fulfilled.
   ●   Translation: Altering messages syntactically, through mediation flows and message
       models, so the requester's message can be processed by the provider for the expected
       result.

Scope of the Integration Layer
The Integration Layer should provide for Enterprise Application Interaction, with additional
features directed specifically to the properties above. Providing integrated data analytics not
meant to inform components for improved performance is considered over-reaching and anti-
competitive. The Integration Layer provider should allow customizations for mediation built
at a “freemium”, trial, or open-source tier to be used within/migrated to the commercial
context with full support.

Multi-tenancy and Cloud
   ●   The Integration Layer should allow for isolation as “tenants” within the Integration
       Layer context, including applicable role-based access control (RBAC) and other
       physical or logical security controls and resource utilization.

                                                                                    Page 3 of 5

   ●   The Integration Layer should be available as an on-premise, cloud (IaaS/SaaS), and
       hybrid offering, and as compliance controls change, the state should enjoy the
       benefits expected of the State of Colorado's Cloud-first policy.
   ● The Integration Layer should support a “scale-out” deployment model, whereby
       incremental and predictable additions to supporting infrastructure and platforms
       provide corresponding improvements in functional resources and features.
   ● The Integration Layer should provide a consolidated interface for management and
       administration of tenants, roles, functions, components, and features.
The generalized logical view of an ESB shows two services exchanging messages through a
message routing protocol, with the ESB providing mediation (semantic and syntactic handling)
and internal processing for integration, rules, and transformation/orchestration — while
remaining uninvolved with the business logic (service semantics) by design.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions
stated within this document must be requested of, and approved by, the “Owner of Standard”
listed under Roles and Responsibilities.
Requests may be acquired by completing the “EXCEPTION REQUEST to Technical Standard”
form and including the completed form (with all signatures) along with other documentation
required as part of standard procedures when executing a technology procurement or service
deployment.

6. References
   ●   OIT documents and policies - State of Colorado Style Library; TS-OEA-001: Technology
       Accessibility for Persons with Disabilities; Enforcement Category Chart
   ●   State documents and policies - Colorado Brand Guidelines; C.R.S. 24-37.5-101, et seq.;
       IAW Technology Standard
   ●   Third-party resources - My Oracle Support; Bernard Manouvrier and Laurent Menard
       (2008), Application Integration: EAI B2B BPM and SOA, Wiley-IEEE Press; “The
       Enterprise Service Bus, re-examined” (IBM developerWorks); Laura González and Raúl
       Ruggia (2010), “Towards dynamic adaptation within an ESB-based service
       infrastructure layer,” MONA '10, ACM.

7. Definitions
   ●   Communication Protocols: The application of interaction patterns within an ESB, such
       as synchronous, unidirectional, and publish/subscribe.
   ●   Cross-cutting Concern: A concern that cannot be decomposed from a system, resulting
       in scattering (duplication) and/or tangling (interdependency).
   ●   Enterprise Application Integration (EAI): An architectural concept and component (or
       set of components) that deals with non-semantic and semantic mismatches between
       applications.
   ●   Enterprise Service Bus (ESB): A middleware or integration component that fulfills, at
       minimum, the principles of Service Virtualization and Aspect-Oriented Connectivity.
   ●   Mediation: An ESB role to intercept and process messages between the service
       requester and provider so the modified syntax achieves interconnectivity.
   ●   Mediation Flows: The application of mediation patterns within an ESB to facilitate
       message transfer between parties; a flow is stateless, initiated only at the request of a
       service, and invokes only one provider.

                                                                                    Page 4 of 5

●   Message Models: The application of metamodels within an ESB regarding standards for
    translating content (e.g., HL7).
●   Principle of Aspect-Oriented Connectivity: Agents offer cross-cutting concern
    mitigation (security, management, logging, auditing) on behalf of requesters and
    providers with little or no impact to the agents themselves.
●   Principle of Service Virtualization: Service requestors and providers interacting with an
    ESB should not be restricted to the same protocol; transformation should reconcile
    differences; identities are known only to the ESB.
●   Service: The implementation of the semantics associated with achieving business goals
    as an abstraction; a specification describes the task while realization is the actual
    implementation.
●   Service Governance: Controls applied to what business functions are made reusable,
    subject to maturation and evolution, and how they are exposed.
●   Service Operational Aspects: Operational metrics such as response time, throughput,
    and availability, reportable as quality of service.
●   Service Semantics: The business task performed and a definition of the interface in
    terms of task-relevant business entities.
●   Service Syntax: Connection mechanisms, specifically protocol, message formats, and
    security.

                                                                                 Page 5 of 5

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-DAT-001: Enterprise Data Access and Integration Services', links this file as https://drive.google.com/file/d/1rbR9iUkk4Rmf82revz3i4zlkybjbEfci/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=1rbR9iUkk4Rmf82revz3i4zlkybjbEfci (the source URL above).
