---
schema_version: 1
corpus: states-government-it
jurisdiction: maine
id: me-oit-digital-signatures
title: Digital Signatures
doc_type: policy
citation: MaineIT Digital Signatures page
authority_level: ''
issuing_body: Maine Office of Information Technology (MaineIT), Department of Administrative and Financial
  Services
source_url: https://www.maine.gov/oit/signature
source_format: html
retrieved: '2026-11-12'
source_sha256: 936b3092e361389f6a7564b8486d3b59c61f59a5f2a282ed0223154588c60e3c
effective_date: null
source_version: ''
status: current
content_mode: verbatim
conversion_notes: 'Text taken from the page on maine.gov (a Drupal site run by the issuing office): the
  page''s heading, then everything up to the site footer, one line per paragraph, heading, list item and
  table row. The site header, menus, images (a signature or letterhead image is not text), social-media
  links and footer were removed, as were the targets of links. Items of a numbered list are numbered 1.,
  2., ... within their list (nested lists indented two spaces), as a browser numbers a plain ordered list;
  the page sets no other numbering style. Bullets are written as a bullet character. The page prints no
  revision history.'
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
- digital-services
- governance
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Digital Signatures (MaineIT Digital Signatures page)

## At a glance

Requirements for digital signature products used by State agencies (X.509 PKI, PDF and Active Directory integration, certified data center, AES-256 transmission, embedded verification), the duty to consult the CIO before contracting with an approved vendor, and the products approved for the Executive Branch. Applies the Digital Signature rule.

## Full text

Digital Signatures
For state agencies: All state agencies must consult with the Chief Information Officer before contracting with an approved digital signature vendor. User education is a critical component for ensuring the viability of digital signatures and the integrity of digital signatures rests upon the confidentiality of authentication credentials.
For digital signature vendors: To become an approved vendor, the product must meet the following criteria.
1. It must be based upon the X.509 Public Key Infrastructure;
2. It must provide seamless integration with the PDF document format;
3. It must provide seamless integration with Microsoft Active Directory;
4. The interface to the Signer must be either web-based or a free download;
5. The data center must be certified as either "SSAE 16 Type II (American Institute of Certified Public Accounts)" or "FedRAMP compliant Cloud Service Provider (Federal General Services Administration)".
6. All transmission between the Signer's device and the data center must be encrypted to the AES-256 (National Institute of Standards and Technology) strength; and
7. The Verification and Tamper-Resistance elements must be embedded within the document, as well as stored in the data center
Any vendor seeking approval must complete and submit the Request for Product Acceptance (PDF) .
• Digital Signature Rule
• Approved Products: Adobe Sign, DocuSign, PandaDoc, and RightSignature and JotForm Enterprise
• For the Executive Branch, the CIO has limited the Digital Signature portfolio to Adobe Sign, DocuSign, and Jotform Enterprise.

## Curator notes

Text taken from the page on maine.gov (a Drupal site run by the issuing office): the page's heading, then everything up to the site footer, one line per paragraph, heading, list item and table row. The site header, menus, images (a signature or letterhead image is not text), social-media links and footer were removed, as were the targets of links. Items of a numbered list are numbered 1., 2., ... within their list (nested lists indented two spaces), as a browser numbers a plain ordered list; the page sets no other numbering style. Bullets are written as a bullet character. The page prints no revision history.
