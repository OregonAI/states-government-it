---
schema_version: 1
corpus: states-government-it
jurisdiction: washington
id: wa-ea-01-04-s
title: Email Address Naming Standard
doc_type: standard
citation: WaTech Standard EA-01-04-S
authority_level: ''
issuing_body: Washington Technology Solutions (WaTech), Office of the State Chief Information Officer
source_url: https://watech.wa.gov/sites/default/files/2025-06/EA-01-04-S%20Email%20Address%20Naming%20Standard.pdf
source_format: pdf
retrieved: '2026-11-10'
source_sha256: b45480db9eea7d4fe162a5c10ab884278f378cbeadd75e7fe20c4da9335d3328
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
- digital-services
---

> **NON-AUTHORITATIVE.** This is a convenience copy for machine reading. The official text is published at the source URL above. Verify at source before relying on it.

# Email Address Naming Standard (WaTech Standard EA-01-04-S)

## At a glance

Item of the WaTech policy library, chapter '3. Enterprise Architecture' (listed as type Standards). Listed at https://watech.wa.gov/policies/email-address-naming-standard-0.

## Full text

EA-01-04-S                                                                                                                Replaces:
State CIO Adopted: Dec. 10, 2024                                                                IT Enterprise Architecture Standard
TSB Approved: Dec. 10, 2024                                                                         171.10- Email Address Naming
Sunset Review: Dec. 10, 2027                                                                                    December 14, 2021

                        EMAIL ADDRESS NAMING STANDARD

 See Also:
 RCW 43.105.054 WaTech Governance
 RCW 43.105.205 (3) Higher Ed
 RCW 43.105.020 (22) “State agency”
 Microsoft 365 email address contains an underscore character after directory synchronization

     1. When creating email accounts for individuals, agencies must use the naming
        format of FirstName.LastName@agency.wa.gov or
        Firstname.mi.LastName@agency.wa.gov for the primary SMTP email address
        and the User Principal Name (UPN). This applies to any individual that is
        assigned a state email address.

               a. LastName can be one or more last names. Examples:
                  Person.Smith@agy.wa.gov, Person.SmithJones@agy.wa.gov,
                  Person.Smith-Jones@agy.wa.gov.

               b. Email accounts must be unique within each agency namespace.
                  Duplicates may be resolved by adding a middle initial or a number
                  following the LastName of the email address. Examples:
                  Person.Smith1@agy.wa.gov, Person.Smith2@agy.wa.gov or
                  Person.A.Smith@agy.wa.gov, Person.B.Smith@agy.wa.gov.

               c. Where the name exceeds 64 characters, names may be shortened.

               d. The Primary SMTP and UPN must match.

               e. Exceptions to this requirement include:

                          i.    Employees where the email address of the individual should be
                                obfuscated for the protection of the individual in accordance
                                with agency policy.

                         ii.    An individual may use their legal name or their preferred name
                                that they are commonly known by as long as it meets the
                                agency’s policy. This may include, but is not limited to, a single
                                name or where a last name is traditionally first.

               f. Sub addressing, also known as plus addressing, is permitted. Sub
                  addressing allows users to create a tag on the email address, for
                  example first.last+billing@agy.wa.gov. See support documentation Plus
                  Addressing in Exchange Online.

   2. The local part (before the @) of the address cannot exceed 64 characters total
      as outlined in Request For Comment (RFC) 7504 SMTP 521 and 526 Reply
      Codes, and the entirety of the address cannot exceed 256 characters.

   3. The format for authoritative, administrative, service, and secondary/proxy
      addresses is at the discretion of the agency.

REFERENCES

1. RFC 7504 SMTP 521 and 556 Reply Codes.
2. Plus Addressing in Exchange Online.
3. Definition of Terms Used in Policies and Reports.

CONTACT

   •   For questions about this policy, please email the WaTech Policy Mailbox.
   •   For support with email services, please file a support ticket.

## Curator notes

Text extracted with pdftotext -layout (page headers, footers and column layout kept as extracted; form feeds and trailing spaces removed; ligature glyphs such as fi and fl written as their letters).
