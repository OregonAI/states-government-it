---
schema_version: 1
corpus: states-it-governance
jurisdiction: california
id: ca-simm-5350-a
title: Zero Trust Architecture Standard
doc_type: standard
citation: SIMM 5350-A
authority_level: ''
issuing_body: California Department of Technology
source_url: https://www.cdt.ca.gov/wp-content/uploads/policy/simm/SIMM-5350-A-Zero-Trust-Architecture-Standard.pdf
source_format: pdf
retrieved: '2026-11-11'
source_sha256: 33cc80e3f32dc6f57b9a554db6eabf32265f9783782724d9b9364bb98d3619d9
effective_date: null
source_version: January 2026
status: current
content_mode: verbatim
conversion_notes: Text extracted with pdftotext -layout (page headers, footers and column layout kept
  as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their
  letters). source_version is the month, or the revision month, the document prints (a month with no day
  is not made into a date).
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
- cloud-resilience
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Zero Trust Architecture Standard (SIMM 5350-A)

## At a glance

SIMM 5350-A, Zero Trust Architecture Standard: an item of the Office of Information Security's information security series (SIMM 5300), the California Department of Technology's library of statewide IT policies, standards, instructions, forms and templates.

## Full text

              State of California

         Department of Technology

Zero Trust Architecture Standard
 Statewide Information Management Manual – 5350-A

                  January 2026

                                               Table of Contents
Document History ............................................................................................................ 2

Introduction ..................................................................................................................... 3

   Purpose........................................................................................................................ 3

   Scope ........................................................................................................................... 3

   Compliance .................................................................................................................. 3

   Definitions .................................................................................................................... 4

Zero Trust Tenets ............................................................................................................ 4

Architecture Controls ....................................................................................................... 5

Tracking Progress ........................................................................................................... 6

Resources ....................................................................................................................... 7

References ...................................................................................................................... 8

Questions ........................................................................................................................ 8

California Department of Technology                                                                                                 1
Zero Trust Architecture Standard
SIMM Section 5350-A                                                                                                 January 2026

Document History
Revision           Date of Release            Owner                Summary of Changes
                                      Office of Information
    v.1               August 2025     Security (OIS)          Initial release
                                      Office of Information   Minor Update: Reference update
    v.2              January 2026     Security (OIS)          in support of renaming of SIMM
                                                              5350-B.

California Department of Technology                                                       2
Zero Trust Architecture Standard
SIMM Section 5350-A                                                             January 2026

Introduction

Purpose

Zero Trust Architecture (ZTA) is crucial for state governments to ensure digital trust, by
continuously validating every user, service, and device, by default, whether inside or
outside a network, reducing the risk of data breaches and cyberattacks. Instead of relying
on traditional perimeter-based security approaches that assume everything inside the
network is trustworthy, Zero Trust assumes that threats could be both external and
internal. It requires strict verification and validation for all users, devices, and network
components attempting to access resources.

This standard provides a phased approach to implementing ZTA, building upon State
Administrative Manual (SAM) 5350. State agencies and entities are required to adopt the
security controls listed in SIMM 5350-B.

Scope

This standard applies to all California state entities, including agencies, departments,
divisions, bureaus, boards, and commissions, as defined in Gov Code Section 11546.1.

Compliance

As outlined in Government Code (GC) Section 11549.3, the California Department of
Technology’s (CDT) Office of Information Security (OIS) is entrusted with creating,
issuing, and maintaining policies, standards, and procedures, overseeing information
security risk management for agencies and state entities, providing information security
and privacy guidance, and ensuring compliance with State Administrative Manual (SAM)
Chapter 5300 and Statewide Information Management Manual (SIMM) section 5300.

State entities must adhere to CDT-issued information security and privacy policies, as
well as all relevant governing laws, regulations, rules, and standards. Compliance may
be reflected in audit findings and maturity scores. Non-compliance will be addressed
according to the Office of Information Security Policy Compliance and Enforcement
Standard (SIMM 5330-H).

California Department of Technology                                                       3
Zero Trust Architecture Standard
SIMM Section 5350-A                                                             January 2026

Definitions

Zero Trust Architecture: A security trust model that assumes that no entity should be
inherently trusted, whether internal or external. It requires strict verification and
authentication for users, devices, and applications seeking access to resources.

Zero Trust Tenets
ZTA uses Zero Trust tenets to plan industrial and enterprise infrastructure and workflows.
The Cybersecurity & Infrastructure Security Agency’s (CISA) Zero Trust Maturity Model
documentation describes five ZTA pillars as the foundational layers to adopt ZTA. These
are: Identity, Devices, Networks, Applications and Workloads, and Data. Each pillar can
progress at its own pace and may progress more quickly than others until cross-pillar
coordination is required. The model is designed to augment adherence to Zero Trust
tenets listed in the National Institute for Standards and Technology’s (NIST) SP 800-207:

   1. All data sources and computing services are considered resources.
   2. All communication is secured regardless of network location.
   3. Access to individual enterprise resources is granted on a per-session basis.
   4. Access to resources is determined by dynamic policy—including the observable
       state of client identity, application/service, and the requesting asset—and may
       include other behavioral and environmental attributes.
   5. The enterprise monitors and measures the integrity and security posture of all
       owned and associated assets.
   6. All resource authentication and authorization are dynamic and strictly enforced
       before access is allowed.
   7. The enterprise collects as much information as possible about the current state of
       assets, network infrastructure and communications and uses it to improve its
       security posture.

California Department of Technology                                                     4
Zero Trust Architecture Standard
SIMM Section 5350-A                                                           January 2026

Architecture Controls
Agency/State entities are required to establish the security and privacy controls outlined
in NIST SP 800-53 Rev 5, as detailed in Appendix-A in SIMM 5350-B pertaining to the
applicable ZTA components.

Agency/State entities shall adopt a ZTA that is implemented in a phased, risk-based
manner. This shall begin with a comprehensive inventory of assets and the development
of access policies based on least-privilege and observed access patterns. Existing
security capabilities shall be evaluated for integration into the ZTA framework.
Implementation shall prioritize core components such as identity verification and device
health assessments, with ongoing monitoring and periodic reassessment to ensure
continuous alignment with evolving threats, technologies, and mission requirements. Zero
Trust shall be maintained as a continuous improvement lifecycle.

Agency/State entities are to consistently enhance their security posture by adopting the
established State Baseline Maturity (Levels 1 and 2) and subsequently progress their ZTA
maturity to the Optimized Maturity (Levels 3 and 4) where and when applicable.

Table 1 shows the State Baseline and Optimized goals by Maturity Level that entities
should progress towards. The inability to implement a required SIMM 5350-B ZTA
security control for any system must be recorded as a risk in the Risk Register and
Plan of Action Milestones (SIMM 5305-C).

California Department of Technology                                                     5
Zero Trust Architecture Standard
SIMM Section 5350-A                                                           January 2026

                 Maturity
                                                            Description
                  Level
                             Manually managed lifecycles with assigned security attributes; rigid
                             security policies addressing isolated pillars reliant on external systems;
                  Level 1
State Baseline

                             least privilege enforced only at setup; fragmented policy enforcement;
                 Traditional
                             manual threat response; and weak correlation of dependencies, logs,
                             and telemetry.
                             Automating attribute assignment, lifecycle configuration, and policy
                  Level 2    enforcement; integrating external systems for cross-pillar solutions;
                   Initial   adjusting least privilege post-provisioning; and enhancing internal
                             visibility.
                          Automated lifecycle and policy controls with cross-pillar coordination;
                  Level 3 centralized visibility and identity management; integrated enforcement;
                 Advanced predefined mitigation responses; risk-based privilege adjustments; and
Optimized

                          enterprise-wide awareness, including external resources.
                             Fully automated, just-in-time lifecycles and attribute assignments; self-
                             reporting assets with dynamic, trigger-based policies; adaptive least
                  Level 4
                             privilege access across dependencies; cross-pillar interoperability with
                  Optimal
                             continuous monitoring; and centralized visibility for situational
                             awareness.

Table 1: ZTA Maturity Levels and their description

Tracking Progress
State entities must continuously assess, document, and report their progress in
implementing ZTA principles. They are responsible for tracking completed security
measures, identifying outstanding risks, evaluating their impact, and documenting gaps
where ZTA is not applicable or feasible. Additionally, entities must maintain a structured
implementation plan to address security gaps and advance ZTA planned adoption. Key
areas of focus in the implementation plan shall include authentication, trusted networks,
enforcing least privilege principles, restricting lateral cyber threat movement, and
enhancing the rapid detection, isolation, and removal of unauthorized users and devices.

Table 2 outlines the NIST Cybersecurity Framework (CSF) 2.0 categories relevant to a
ZTA environment. The detailed mapping of CSF 2.0 objectives is highlighted in SIMM
5350-B – Supplemental CSF Mapping tab.

California Department of Technology                                                                   6
Zero Trust Architecture Standard
SIMM Section 5350-A                                                                        January 2026

  Function                                          Category

         GV.OC                 Organizational Context
         GV.RM                 Risk Management Strategy
  GOVERN GV.RR                 Roles, Responsibilities, and Authorities
         GV.PO                 Policy
         GV.SC                 Cybersecurity Supply Chain Risk Management
          ID.AM                Asset Management
 IDENTIFY ID.RA                Risk Assessment
          ID.IM                Improvement
         PR.AA                 Identity Management, Authentication, and Access Control
         PR.DS                 Data Security
 PROTECT
         PR.PS                 Platform Security
         PR.IR                 Technology Infrastructure Resilience
               DE.CM           Continuous Monitoring
  DETECT
               DE.AE           Adverse Event Analysis
         RS.MA                 Incident Management
 RESPOND RS.AN                 Incident Analysis
         RS.MI                 Incident Mitigation
 RECOVER N/A

Table 2: NIST CSF 2.0 categories relevant to a ZTA environment

Resources
SIMM 5350-B contains resources that lay out the ZTA technical roadmap. The Appendix-
A tab maps the functions provided by the logical components of the ZTA reference design
and NIST SP 800-53 security controls. Supplemental CSF Mapping tab maps the
functions of the ZTA reference design components and the NIST CSF 2.0 functions.

California Department of Technology                                                      7
Zero Trust Architecture Standard
SIMM Section 5350-A                                                           January 2026

References
•   CISA Zero Trust Maturity Model
    https://www.cisa.gov/zero-trust-maturity-model
•   DoD Zero Trust Strategy
    https://dodcio.defense.gov/Portals/0/Documents/Library/DoD-ZTStrategy.pdf
•   NIST SP 800-207 – Zero Trust Architecture
    https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
•   NIST SP 1800-35 – Implementing a Zero Trust Architecture
    https://csrc.nist.gov/pubs/sp/1800/35/final
•   NIST Cybersecurity Framework 2.0
    https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
•   NIST Security and Privacy Controls Rev5
    https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
•   SAM 5350 Operational Security
    https://www.dgs.ca.gov/Resources/SAM/TOC/5300/5350
•   SAM 4983.1 Cloud Computing Policy
    https://www.dgs.ca.gov/Resources/SAM/TOC/4900/4983-1
•   SIMM 140 Cloud Security Guide
    https://cdt.ca.gov/wp-content/uploads/2023/10/SIMM-140-Cloud-Security-Guide-
    1.docx
•   SIMM 5305-A Information Security Program Management Standard
    https://cdt.ca.gov/wp-content/uploads/2023/12/SIMM-5305_A_2023-12.pdf
•   US Government Accountability Office GAO-23-106065 Zero Trust Architecture
    https://www.gao.gov/assets/gao-23-106065.pdf

Questions
Questions regarding the implementation of this standard may be sent to:
California Department of Technology
Office of Information Security
Security@state.ca.gov
California Department of Technology                                                     8
Zero Trust Architecture Standard
SIMM Section 5350-A                                                           January 2026

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters). source_version is the month, or the revision month, the document prints (a month with no day is not made into a date).
