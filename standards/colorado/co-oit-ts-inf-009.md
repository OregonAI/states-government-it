---
schema_version: 1
corpus: states-government-it
jurisdiction: colorado
id: co-oit-ts-inf-009
title: Infrastructure as Code Standard
doc_type: standard
citation: TS-INF-009
authority_level: ''
issuing_body: Governor's Office of Information Technology
source_url: https://drive.google.com/uc?export=download&id=10sQ9dJ_SvuqNeJrnPAKZN3LKazqPP87f
source_format: pdf
retrieved: '2026-11-11'
source_sha256: d476e6ee8740ffd0c57e22522011525adf1d3fe324f7e1456b14ad94e452b692
effective_date: '2023-08-02'
source_version: 3.0, last updated 07/20/2026
status: current
content_mode: verbatim
conversion_notes: 'Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). OIT''s page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where
  the list item reads ''TS-INF-009: Infrastructure as Code Standard'', links this file as https://drive.google.com/file/d/10sQ9dJ_SvuqNeJrnPAKZN3LKazqPP87f/view?usp=sharing;
  the text was fetched from Google Drive''s direct-download form of the same file, https://drive.google.com/uc?export=download&id=10sQ9dJ_SvuqNeJrnPAKZN3LKazqPP87f
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Infrastructure as Code Standard (TS-INF-009)

## At a glance

OIT technical standard TS-INF-009 (Infrastructure): Infrastructure as Code Standard. OIT's Technical Standards page lists it as issued by the Office of Enterprise Architecture and approved by the OIT Architecture Review Board; the file prints its own effective date, version and last-updated date.

## Full text

TS-INF-009: Infrastructure as Code Standard
  Document ID                     TS-INF-009
  Title                           Infrastructure as Code Standard
  Executive Sponsor               Infrastructure Operations/Cloud Ops
  Issuing Authority               Office of Information Technology (OIT)
  Applies to                      OIT and OIT-supported agencies, employees of OIT, agencies
                                  supported by OIT, and vendors contracted by OIT or its
                                  stakeholders.
  Tier                            Standard
  Version                         3.0
  Effective Date                  08/02/2023
  Last Updated                    07/20/2026

1. Purpose
This standard enables Infrastructure Operations (IO) to consistently automate the deployment and
maintenance of infrastructure in a secure, efficient, and repeatable manner, providing specific
requirements for automating deployments of infrastructure on-premises and in the cloud through an
Infrastructure-as-Code (IaC) approach.
The ultimate purpose of this standard is to enable OIT to efficiently define and deploy infrastructure
— such as networks, virtual machines, load balancers, security appliances, and connection topologies
— so an IaC model generates the same environment every time it deploys, provisioning the
infrastructure service request in a secure, consistent, effective, and repeatable manner through
automated scripts.

2. Scope
These standards apply to OIT and OIT-supported agencies. This standard shall be used by employees
of OIT, agencies supported by OIT, and vendors contracted by OIT or its stakeholders, as a means to
enforce technology standardization and assist in making the usage, support, and/or purchase of
technologies more consistent and efficient.
Standards instituted for use by approval of the OIT Architecture Review Board (ARB) govern purchase
and deployment decisions deemed "go-forward" or "net-new", and are not intended as a retroactively
enforceable mandate for immediate conformance, especially where cost implications may be
prohibitive.

                                                                                           Page 1 of 3

3. Roles and Responsibilities
Enterprise Architecture - Chief Enterprise Architect
   ●   Chairs and conducts business of the Architecture Review Board (ARB).
   ●   Updates effective date and/or last review date.
   ●   Publishes the ARB-approved Standard to the OIT public-facing website.
Architecture Review Board (ARB)
   ●   Engages stakeholders and subject matter experts to determine the standard.
   ●   Reviews and approves the Standard (this document).
Infrastructure Operations/Cloud Ops
   ●   Owner of Standard; engages stakeholders and subject matter experts to define the standard.
   ●   Updates document standards and version number; submits/presents to the ARB for approval.
   ●   Provides resources necessary to implement and support IaC systems in the state cloud
       environment.
   ●   Selects IaC languages, submits selections to the governing committee, and develops
       templates that meet OIT standards.
Infrastructure Operations/Network Services
   ●   Provides resources necessary to implement and support network components of IaC.
Azure DevOps Administration Team
   ●   Provisions repository and pipeline spaces for both operations teams and project teams using
       IaC.
All OIT staff are responsible for being aware of the existence of this (and all) standard(s) and its
purposes of authority and governance in support of OIT's statutorily mandated mission in service of
Colorado State Government affairs.

4. Standards
Infrastructure deployed after establishment of this standard is governed by conceptual IaC
architecture diagrams and a basic IaC flow maintained by Infrastructure Operations. The following
IaC requirements apply:
   ●   Infrastructure deployed after the establishment of this standard shall be deployed using IaC
       whenever possible.
   ●   IaC language selection shall be performed by OIT infrastructure teams and accepted by the
       committee governing the platform.
   ●   Evaluate, select, standardize, and train on IaC tools such as Terraform.
   ●   Application and infrastructure configurations shall be stored in appropriate file types in
       organizationally managed repositories.
   ●   Project-specific IaC code should be stored in a project-specific repository and deployed via a
       deployment pipeline.
   ●   IaC code should be scanned in a repeatable manner; the code scanning and code review
       processes should be documented in Standard Operating Procedures (SOPs).
   ●   IaC templates should be developed by or approved by platform management teams prior to
       dissemination to project teams and vendors.

                                                                                            Page 2 of 3

   ●   Ensure IaC files are scanned for security, compliance, and quality, with any findings
       addressed prior to deployment.
   ●   Enable IaC scanning tools such as Checkov or Veracode to produce safe infrastructure code.
   ●   Restrict access to the IaC pipelines and repositories to project personnel and infrastructure
       teams.
   ●   Infrastructure configured using IaC cannot be modified manually via the console or API, since
       those changes create drift that will be overwritten by the next IaC deployment.
   ●   Application IaC should be configured to deliver as close to identical infrastructure between
       development, test, and production environments as possible.

5. Variance and Exception Process
Any request to procure or deploy technology that is a variance to the standards and provisions stated
within this document must be requested of, and approved by, the "Owner of Standard" listed under
Roles and Responsibilities.
Requests may be acquired by completing the "EXCEPTION REQUEST to Technical Standard" form and
including the completed form (with all signatures) along with other documentation required as part
of standard procedures when executing a technology procurement or service deployment.

6. References
   ●   NIST Special Publication 800-204, Security Strategies for Microservices-based Application
       Systems
   ●   Microsoft: What is Infrastructure as Code (IaC)?
   ●   HashiCorp: Automate Infrastructure on Any Cloud
   ●   AWS: Infrastructure as Code
   ●   Snyk: IaC security for devs and DevOps

7. Definitions
Infrastructure as Code (IaC): Provisioning infrastructure through automated scripts to achieve
consistent, predictable, and repeatable configuration deployments.
Terraform: An open-source IaC tool for provisioning and managing cloud infrastructure, codifying
infrastructure in configuration files that describe the desired state for a topology.
Declarative Definition Files: Files describing the components and configuration an environment
requires, but not necessarily how to achieve that configuration.
Infrastructure Operations (IOs): Includes server, network, NetSec, and cloud teams.
Exception request: A document requesting an exception to a recognized standard, requiring a
business or technical justification, subject to review and approval by an authority in the area.

                                                                                           Page 3 of 3

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). OIT's page (https://oit.colorado.gov/standards-policies-guides/technical-standards), where the list item reads 'TS-INF-009: Infrastructure as Code Standard', links this file as https://drive.google.com/file/d/10sQ9dJ_SvuqNeJrnPAKZN3LKazqPP87f/view?usp=sharing; the text was fetched from Google Drive's direct-download form of the same file, https://drive.google.com/uc?export=download&id=10sQ9dJ_SvuqNeJrnPAKZN3LKazqPP87f (the source URL above).
