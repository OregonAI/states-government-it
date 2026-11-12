---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-salesforce-executive-summary
title: 'Salesforce Governance: Executive Summary'
doc_type: policy
citation: 'MaineIT Salesforce Governance: Executive Summary'
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/SalesforceGovExecutiveSummary.pdf
source_format: pdf
retrieved: '2026-11-12'
source_sha256: 3d0f422e9b3606801b8e4217bf2dfcd0cba923bc5781f58a9d6bd9ed98e4efa2
effective_date: null
source_version: 'Latest Revision: 22 September 2021'
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
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Salesforce Governance: Executive Summary (MaineIT Salesforce Governance: Executive Summary)

## At a glance

A one-page summary of Salesforce governance in the Executive Branch: the Salesforce Governance Committee, under the authority of the CIO, oversees all Executive Branch Salesforce use.

## Full text

                     Salesforce Governance: Executive Summary

Purpose
This is an Executive Summary for Salesforce Governance within the SOM Executive Branch.

Salesforce Governance Committee
Oversees all Executive Branch Salesforce utilization. Under the authority of the CIO, the committee
includes key stakeholders from departments invested in Salesforce.

Org Strategy
Org structures within Salesforce will be adopted through structured criteria and cost-benefit
analysis, including the total cost of ownership, with the final recommendation made by the
Governance Committee.

Org Naming Convention
Production Orgs within Salesforce will be named “SOM” followed by a 2-digit number (SOM01).
Lower environments will use the Production name suffixed with environment type (SOM01Test).

Development and Interface
All net-new apps within Salesforce Orgs shall adopt turnkey SaaS products developed using
Lightning Experience. All apps must follow an Agile Software Development Life Cycle. Additionally,
the Maine Service Bus must be the first consideration for any external interfaces.

Configuration vs. Customization
AppExchange and Configuration must be considered first. Where Configuration is not easily
accomplished, Customization may be used as a secondary method. Customizations/Configurations
must comply with Salesforce Naming Conventions. Customizations must comply with the Apex
Design Best Practices and the Execution Governor Limits.

Security
Security configurations will be implemented to align with I.T. policies, and any relevant regulatory
stipulation. All Orgs with TLP: Amber, TLP: Amber+Strict, or TLP: Red data must be audited using
the native Salesforce auditing capability.

Integrations
An Org must be integrated with an Active Directory group, with Single Sign-on enabled.

Milestones/Changes
Apps set for production must complete Application Deployment Certification before going live. A
point-in-time cloud-to-cloud backup is required at all major milestones, with the relevant code
versions copied to the OIT enterprise source configuration management system. All major
milestones/production changes must comply with the OIT Change Management Policy.

Support and Monitoring
Apps must provision a support model for post-go-live support. All contracted Salesforce vendors
will be accountable for deliverables, and responsible for defined criteria, including, KPIs, quality of
service, and technical documentation.

Initial Issue: 22 September 2021
Latest Revision: 22 September 2021
Point-of-Contact: PolicyTeam.OIT@Maine.Gov

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
